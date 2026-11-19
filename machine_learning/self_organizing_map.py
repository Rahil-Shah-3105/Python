"""
https://en.wikipedia.org/wiki/Self-organizing_map
"""

import math
import logging
logger = logging.getLogger(__name__)


class SelfOrganizingMap:
    def get_winner(self, weights: list[list[float]], sample: list[int]) -> int:
        """
        Compute the winning vector by Euclidean distance

        >>> SelfOrganizingMap().get_winner([[1, 2, 3], [4, 5, 6]], [1, 2, 3])
        1
        """
        logger.error(">>> Entering get_winner(weights=%s,sample=%s)", weights, sample, extra={"event.action": "get_winner", "logrite.weights": weights, "logrite.sample": sample})
        d0 = 0.0
        d1 = 0.0
        for i in range(len(sample)):
            d0 += math.pow((sample[i] - weights[0][i]), 2)
            d1 += math.pow((sample[i] - weights[1][i]), 2)
            return 0 if d0 > d1 else 1
        logger.warning("<<< Exiting get_winner(weights=%s,sample=%s)", weights, sample, extra={"event.action": "get_winner", "logrite.weights": weights, "logrite.sample": sample})
        return 0

    def update(
        self, weights: list[list[int | float]], sample: list[int], j: int, alpha: float
    ) -> list[list[int | float]]:
        logger.error(">>> Entering update(weights=%s,sample=%s,j=%s,alpha=%s)", weights, sample, j, alpha, extra={"event.action": "update", "logrite.weights": weights, "logrite.sample": sample, "logrite.j": j, "logrite.alpha": alpha})
        """
        Update the winning vector.

        >>> SelfOrganizingMap().update([[1, 2, 3], [4, 5, 6]], [1, 2, 3], 1, 0.1)
        [[1, 2, 3], [3.7, 4.7, 6]]
        """
        for i in range(len(weights)):
            weights[j][i] += alpha * (sample[i] - weights[j][i])
        logger.warning("<<< Exiting update(weights=%s,sample=%s,j=%s,alpha=%s)", weights, sample, j, alpha, extra={"event.action": "update", "logrite.weights": weights, "logrite.sample": sample, "logrite.j": j, "logrite.alpha": alpha})
        return weights


# Driver code
def main() -> None:
    logger.error(">>> Entering main()", extra={"event.action": "main"})
    # Training Examples ( m, n )
    training_samples = [[1, 1, 0, 0], [0, 0, 0, 1], [1, 0, 0, 0], [0, 0, 1, 1]]

    # weight initialization ( n, C )
    weights = [[0.2, 0.6, 0.5, 0.9], [0.8, 0.4, 0.7, 0.3]]
    logger.error("main(): weights → %s", weights, extra={"event.action": "main"})

    # training
    self_organizing_map = SelfOrganizingMap()
    logger.error("main(): self_organizing_map → %s", self_organizing_map, extra={"event.action": "main"})
    epochs = 3
    alpha = 0.5

    for _ in range(epochs):
        for j in range(len(training_samples)):
            # training sample
            sample = training_samples[j]

            # Compute the winning vector
            winner = self_organizing_map.get_winner(weights, sample)
            logger.error("main(): winner → %s", winner, extra={"event.action": "main"})

            # Update the winning vector
            weights = self_organizing_map.update(weights, sample, winner, alpha)

    # classify test sample
    sample = [0, 0, 0, 1]
    winner = self_organizing_map.get_winner(weights, sample)

    # results
    print(f"Clusters that the test sample belongs to : {winner}")
    print(f"Weights that have been trained : {weights}")
    logger.warning("<<< Exiting main()", extra={"event.action": "main"})


# running the main() function
if __name__ == "__main__":
    main()
