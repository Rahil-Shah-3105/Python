"""
Simple multithreaded algorithm to show how the 4 phases of a genetic algorithm works
(Evaluation, Selection, Crossover and Mutation)
https://en.wikipedia.org/wiki/Genetic_algorithm
Author: D4rkia
"""

from __future__ import annotations

import random
import logging
logger = logging.getLogger(__name__)

# Maximum size of the population.  Bigger could be faster but is more memory expensive.
N_POPULATION = 200
# Number of elements selected in every generation of evolution. The selection takes
# place from best to worst of that generation and must be smaller than N_POPULATION.
N_SELECTED = 50
# Probability that an element of a generation can mutate, changing one of its genes.
# This will guarantee that all genes will be used during evolution.
MUTATION_PROBABILITY = 0.4
# Just a seed to improve randomness required by the algorithm.
random.seed(random.randint(0, 1000))


def evaluate(item: str, main_target: str) -> tuple[str, float]:
    """
    Evaluate how similar the item is with the target by just
    counting each char in the right position
    >>> evaluate("Helxo Worlx", "Hello World")
    ('Helxo Worlx', 9.0)
    """
    logger.error(">>> Entering evaluate(item=%s,main_target=%s)", item, main_target, extra={"event.action": "evaluate", "logrite.item": item, "logrite.main_target": main_target})
    score = len([g for position, g in enumerate(item) if g == main_target[position]])
    logger.error("evaluate(item=%s,main_target=%s): score → %s", item, main_target, score, extra={"event.action": "evaluate", "logrite.item": item, "logrite.main_target": main_target})
    logger.warning("<<< Exiting evaluate(item=%s,main_target=%s)", item, main_target, extra={"event.action": "evaluate", "logrite.item": item, "logrite.main_target": main_target})
    return (item, float(score))


def crossover(parent_1: str, parent_2: str) -> tuple[str, str]:
    """
    Slice and combine two strings at a random point.
    >>> random.seed(42)
    >>> crossover("123456", "abcdef")
    ('12345f', 'abcde6')
    """
    logger.error(">>> Entering crossover(parent_1=%s,parent_2=%s)", parent_1, parent_2, extra={"event.action": "crossover", "logrite.parent_1": parent_1, "logrite.parent_2": parent_2})
    random_slice = random.randint(0, len(parent_1) - 1)
    logger.error("crossover(parent_1=%s,parent_2=%s): random_slice → %s", parent_1, parent_2, random_slice, extra={"event.action": "crossover", "logrite.parent_1": parent_1, "logrite.parent_2": parent_2})
    child_1 = parent_1[:random_slice] + parent_2[random_slice:]
    child_2 = parent_2[:random_slice] + parent_1[random_slice:]
    logger.warning("<<< Exiting crossover(parent_1=%s,parent_2=%s)", parent_1, parent_2, extra={"event.action": "crossover", "logrite.parent_1": parent_1, "logrite.parent_2": parent_2})
    return (child_1, child_2)


def mutate(child: str, genes: list[str]) -> str:
    """
    Mutate a random gene of a child with another one from the list.
    >>> random.seed(123)
    >>> mutate("123456", list("ABCDEF"))
    '12345A'
    """
    logger.error(">>> Entering mutate(child=%s,genes=%s)", child, genes, extra={"event.action": "mutate", "logrite.child": child, "logrite.genes": genes})
    child_list = list(child)
    logger.error("mutate(child=%s,genes=%s): child_list → %s", child, genes, child_list, extra={"event.action": "mutate", "logrite.child": child, "logrite.genes": genes})
    if random.uniform(0, 1) < MUTATION_PROBABILITY:
        child_list[random.randint(0, len(child)) - 1] = random.choice(genes)
    logger.warning("<<< Exiting mutate(child=%s,genes=%s)", child, genes, extra={"event.action": "mutate", "logrite.child": child, "logrite.genes": genes})
    return "".join(child_list)


# Select, crossover and mutate a new population.
def select(
    parent_1: tuple[str, float],
    population_score: list[tuple[str, float]],
    genes: list[str],
) -> list[str]:
    logger.error(">>> Entering select(parent_1=%s,population_score=%s,genes=%s)", parent_1, population_score, genes, extra={"event.action": "select", "logrite.parent_1": parent_1, "logrite.population_score": population_score, "logrite.genes": genes})
    """
    Select the second parent and generate new population

    >>> random.seed(42)
    >>> parent_1 = ("123456", 8.0)
    >>> population_score = [("abcdef", 4.0), ("ghijkl", 5.0), ("mnopqr", 7.0)]
    >>> genes = list("ABCDEF")
    >>> child_n = int(min(parent_1[1] + 1, 10))
    >>> population = []
    >>> for _ in range(child_n):
    ...     parent_2 = population_score[random.randrange(len(population_score))][0]
    ...     child_1, child_2 = crossover(parent_1[0], parent_2)
    ...     population.extend((mutate(child_1, genes), mutate(child_2, genes)))
    >>> len(population) == (int(parent_1[1]) + 1) * 2
    True
    """
    pop = []
    # Generate more children proportionally to the fitness score.
    child_n = int(parent_1[1] * 100) + 1
    child_n = 10 if child_n >= 10 else child_n
    for _ in range(child_n):
        parent_2 = population_score[random.randint(0, N_SELECTED)][0]
        logger.error("select(parent_1=%s,population_score=%s,genes=%s): parent_2 → %s", parent_1, population_score, genes, parent_2, extra={"event.action": "select", "logrite.parent_1": parent_1, "logrite.population_score": population_score, "logrite.genes": genes})

        child_1, child_2 = crossover(parent_1[0], parent_2)
        # Append new string to the population list.
        pop.append(mutate(child_1, genes))
        pop.append(mutate(child_2, genes))
    logger.warning("<<< Exiting select(parent_1=%s,population_score=%s,genes=%s)", parent_1, population_score, genes, extra={"event.action": "select", "logrite.parent_1": parent_1, "logrite.population_score": population_score, "logrite.genes": genes})
    return pop


def basic(target: str, genes: list[str], debug: bool = True) -> tuple[int, int, str]:
    """
    Verify that the target contains no genes besides the ones inside genes variable.

    >>> from string import ascii_lowercase
    >>> basic("doctest", ascii_lowercase, debug=False)[2]
    'doctest'
    >>> genes = list(ascii_lowercase)
    >>> genes.remove("e")
    >>> basic("test", genes)
    Traceback (most recent call last):
        ...
    ValueError: ['e'] is not in genes list, evolution cannot converge
    >>> genes.remove("s")
    >>> basic("test", genes)
    Traceback (most recent call last):
        ...
    ValueError: ['e', 's'] is not in genes list, evolution cannot converge
    >>> genes.remove("t")
    >>> basic("test", genes)
    Traceback (most recent call last):
        ...
    ValueError: ['e', 's', 't'] is not in genes list, evolution cannot converge
    """
    logger.error(">>> Entering basic(target=%s,genes=%s,debug=%s)", target, genes, debug, extra={"event.action": "basic", "logrite.target": target, "logrite.genes": genes, "logrite.debug": debug})

    # Verify if N_POPULATION is bigger than N_SELECTED
    if N_POPULATION < N_SELECTED:
        msg = f"{N_POPULATION} must be bigger than {N_SELECTED}"
        logger.error("basic(target=%s,genes=%s,debug=%s): msg → %s", target, genes, debug, msg, extra={"event.action": "basic", "logrite.target": target, "logrite.genes": genes, "logrite.debug": debug})
        raise ValueError(msg)
    # Verify that the target contains no genes besides the ones inside genes variable.
    not_in_genes_list = sorted({c for c in target if c not in genes})
    logger.error("basic(target=%s,genes=%s,debug=%s): not_in_genes_list → %s", target, genes, debug, not_in_genes_list, extra={"event.action": "basic", "logrite.target": target, "logrite.genes": genes, "logrite.debug": debug})
    if not_in_genes_list:
        msg = f"{not_in_genes_list} is not in genes list, evolution cannot converge"
        raise ValueError(msg)

    # Generate random starting population.
    population = []
    for _ in range(N_POPULATION):
        population.append("".join([random.choice(genes) for i in range(len(target))]))

    # Just some logs to know what the algorithms is doing.
    generation, total_population = 0, 0

    # This loop will end when we find a perfect match for our target.
    while True:
        generation += 1
        total_population += len(population)

        # Random population created. Now it's time to evaluate.

        # (Option 1) Adding a bit of concurrency can make everything faster,
        #
        # import concurrent.futures
        # population_score: list[tuple[str, float]] = []
        # with concurrent.futures.ThreadPoolExecutor(
        #                                   max_workers=NUM_WORKERS) as executor:
        #     futures = {executor.submit(evaluate, item, target) for item in population}
        #     concurrent.futures.wait(futures)
        #     population_score = [item.result() for item in futures]
        #
        # but with a simple algorithm like this, it will probably be slower.
        # (Option 2) We just need to call evaluate for every item inside the population.
        population_score = [evaluate(item, target) for item in population]

        # Check if there is a matching evolution.
        population_score = sorted(population_score, key=lambda x: x[1], reverse=True)
        if population_score[0][0] == target:
            logger.warning("<<< Exiting basic(target=%s,genes=%s,debug=%s)", target, genes, debug, extra={"event.action": "basic", "logrite.target": target, "logrite.genes": genes, "logrite.debug": debug})
            return (generation, total_population, population_score[0][0])

        # Print the best result every 10 generation.
        # Just to know that the algorithm is working.
        if debug and generation % 10 == 0:
            print(
                f"\nGeneration: {generation}"
                f"\nTotal Population:{total_population}"
                f"\nBest score: {population_score[0][1]}"
                f"\nBest string: {population_score[0][0]}"
            )

        # Flush the old population, keeping some of the best evolutions.
        # Keeping this avoid regression of evolution.
        population_best = population[: int(N_POPULATION / 3)]
        population.clear()
        population.extend(population_best)
        # Normalize population score to be between 0 and 1.
        population_score = [
            (item, score / len(target)) for item, score in population_score
        ]

        # This is selection
        for i in range(N_SELECTED):
            population.extend(select(population_score[int(i)], population_score, genes))
            # Check if the population has already reached the maximum value and if so,
            # break the cycle.  If this check is disabled, the algorithm will take
            # forever to compute large strings, but will also calculate small strings in
            # a far fewer generations.
            if len(population) > N_POPULATION:
                break


if __name__ == "__main__":
    target_str = (
        "This is a genetic algorithm to evaluate, combine, evolve, and mutate a string!"
    )
    genes_list = list(
        " ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklm"
        "nopqrstuvwxyz.,;!?+-*#@^'èéòà€ù=)(&%$£/\\"
    )
    generation, population, target = basic(target_str, genes_list)
    print(
        f"\nGeneration: {generation}\nTotal Population: {population}\nTarget: {target}"
    )
