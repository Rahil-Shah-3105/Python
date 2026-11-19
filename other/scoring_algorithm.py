"""
| developed by: markmelnic
| original repo: https://github.com/markmelnic/Scoring-Algorithm

Analyse data using a range based percentual proximity algorithm
and calculate the linear maximum likelihood estimation.
The basic principle is that all values supplied will be broken
down to a range from ``0`` to ``1`` and each column's score will be added
up to get the total score.

Example for data of vehicles
::

    price|mileage|registration_year
    20k  |60k    |2012
    22k  |50k    |2011
    23k  |90k    |2015
    16k  |210k   |2010

We want the vehicle with the lowest price,
lowest mileage but newest registration year.
Thus the weights for each column are as follows:
``[0, 0, 1]``
"""
import logging
logger = logging.getLogger(__name__)


def get_data(source_data: list[list[float]]) -> list[list[float]]:
    """
    >>> get_data([[20, 60, 2012],[23, 90, 2015],[22, 50, 2011]])
    [[20.0, 23.0, 22.0], [60.0, 90.0, 50.0], [2012.0, 2015.0, 2011.0]]
    """
    logger.error(">>> Entering get_data(source_data=%s)", source_data, extra={"event.action": "get_data", "logrite.source_data": source_data})
    data_lists: list[list[float]] = []
    for data in source_data:
        for i, el in enumerate(data):
            if len(data_lists) < i + 1:
                data_lists.append([])
            data_lists[i].append(float(el))
    logger.warning("<<< Exiting get_data(source_data=%s)", source_data, extra={"event.action": "get_data", "logrite.source_data": source_data})
    return data_lists


def calculate_each_score(
    data_lists: list[list[float]], weights: list[int]
) -> list[list[float]]:
    logger.error(">>> Entering calculate_each_score(data_lists=%s,weights=%s)", data_lists, weights, extra={"event.action": "calculate_each_score", "logrite.data_lists": data_lists, "logrite.weights": weights})
    """
    >>> calculate_each_score([[20, 23, 22], [60, 90, 50], [2012, 2015, 2011]],
    ...                      [0, 0, 1])
    [[1.0, 0.0, 0.33333333333333337], [0.75, 0.0, 1.0], [0.25, 1.0, 0.0]]
    """
    score_lists: list[list[float]] = []
    for dlist, weight in zip(data_lists, weights):
        mind = min(dlist)
        logger.error("calculate_each_score(data_lists=%s,weights=%s): mind → %s", data_lists, weights, mind, extra={"event.action": "calculate_each_score", "logrite.data_lists": data_lists, "logrite.weights": weights})
        maxd = max(dlist)
        logger.error("calculate_each_score(data_lists=%s,weights=%s): maxd → %s", data_lists, weights, maxd, extra={"event.action": "calculate_each_score", "logrite.data_lists": data_lists, "logrite.weights": weights})

        score: list[float] = []
        # for weight 0 score is 1 - actual score
        if weight == 0:
            for item in dlist:
                try:
                    score.append(1 - ((item - mind) / (maxd - mind)))
                except ZeroDivisionError:
                    logger.error("Exception in calculate_each_score(data_lists=%s,weights=%s)", data_lists, weights, exc_info=True, extra={"event.action": "calculate_each_score", "event.category": "process", "logrite.data_lists": data_lists, "logrite.weights": weights})
                    score.append(1)

        elif weight == 1:
            for item in dlist:
                try:
                    score.append((item - mind) / (maxd - mind))
                except ZeroDivisionError:
                    score.append(0)

        # weight not 0 or 1
        else:
            msg = f"Invalid weight of {weight:f} provided"
            logger.error("calculate_each_score(data_lists=%s,weights=%s): msg → %s", data_lists, weights, msg, extra={"event.action": "calculate_each_score", "logrite.data_lists": data_lists, "logrite.weights": weights})
            raise ValueError(msg)

        score_lists.append(score)

    logger.warning("<<< Exiting calculate_each_score(data_lists=%s,weights=%s)", data_lists, weights, extra={"event.action": "calculate_each_score", "logrite.data_lists": data_lists, "logrite.weights": weights})
    return score_lists


def generate_final_scores(score_lists: list[list[float]]) -> list[float]:
    """
    >>> generate_final_scores([[1.0, 0.0, 0.33333333333333337],
    ...                        [0.75, 0.0, 1.0],
    ...                        [0.25, 1.0, 0.0]])
    [2.0, 1.0, 1.3333333333333335]
    """
    logger.error(">>> Entering generate_final_scores(score_lists=%s)", score_lists, extra={"event.action": "generate_final_scores", "logrite.score_lists": score_lists})
    # initialize final scores
    final_scores: list[float] = [0 for i in range(len(score_lists[0]))]

    for slist in score_lists:
        for j, ele in enumerate(slist):
            final_scores[j] = final_scores[j] + ele

    logger.warning("<<< Exiting generate_final_scores(score_lists=%s)", score_lists, extra={"event.action": "generate_final_scores", "logrite.score_lists": score_lists})
    return final_scores


def procentual_proximity(
    source_data: list[list[float]], weights: list[int]
) -> list[list[float]]:
    logger.error(">>> Entering procentual_proximity(source_data=%s,weights=%s)", source_data, weights, extra={"event.action": "procentual_proximity", "logrite.source_data": source_data, "logrite.weights": weights})
    """
    | `weights` - ``int`` list
    | possible values - ``0`` / ``1``

        * ``0`` if lower values have higher weight in the data set
        * ``1`` if higher values have higher weight in the data set

    >>> procentual_proximity([[20, 60, 2012],[23, 90, 2015],[22, 50, 2011]], [0, 0, 1])
    [[20, 60, 2012, 2.0], [23, 90, 2015, 1.0], [22, 50, 2011, 1.3333333333333335]]
    """

    data_lists = get_data(source_data)
    logger.error("procentual_proximity(source_data=%s,weights=%s): data_lists → %s", source_data, weights, data_lists, extra={"event.action": "procentual_proximity", "logrite.source_data": source_data, "logrite.weights": weights})
    score_lists = calculate_each_score(data_lists, weights)
    logger.error("procentual_proximity(source_data=%s,weights=%s): score_lists → %s", source_data, weights, score_lists, extra={"event.action": "procentual_proximity", "logrite.source_data": source_data, "logrite.weights": weights})
    final_scores = generate_final_scores(score_lists)
    logger.error("procentual_proximity(source_data=%s,weights=%s): final_scores → %s", source_data, weights, final_scores, extra={"event.action": "procentual_proximity", "logrite.source_data": source_data, "logrite.weights": weights})

    # append scores to source data
    for i, ele in enumerate(final_scores):
        source_data[i].append(ele)

    logger.warning("<<< Exiting procentual_proximity(source_data=%s,weights=%s)", source_data, weights, extra={"event.action": "procentual_proximity", "logrite.source_data": source_data, "logrite.weights": weights})
    return source_data
