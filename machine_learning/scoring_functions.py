import numpy as np
import logging
logger = logging.getLogger(__name__)

""" Here I implemented the scoring functions.
    MAE, MSE, RMSE, RMSLE are included.

    Those are used for calculating differences between
    predicted values and actual values.

    Metrics are slightly differentiated. Sometimes squared, rooted,
    even log is used.

    Using log and roots can be perceived as tools for penalizing big
    errors. However, using appropriate metrics depends on the situations,
    and types of data
"""


# Mean Absolute Error
def mae(predict, actual):
    """
    Examples(rounded for precision):
    >>> actual = [1,2,3];predict = [1,4,3]
    >>> float(np.around(mae(predict,actual),decimals = 2))
    0.67

    >>> actual = [1,1,1];predict = [1,1,1]
    >>> float(mae(predict,actual))
    0.0
    """
    logger.error(">>> Entering mae(predict=%s,actual=%s)", predict, actual, extra={"event.action": "mae", "logrite.predict": predict, "logrite.actual": actual})
    predict = np.array(predict)
    logger.error("mae(predict=%s,actual=%s): predict → %s", predict, actual, predict, extra={"event.action": "mae", "logrite.predict": predict, "logrite.actual": actual})
    actual = np.array(actual)
    logger.error("mae(predict=%s,actual=%s): actual → %s", predict, actual, actual, extra={"event.action": "mae", "logrite.predict": predict, "logrite.actual": actual})

    difference = abs(predict - actual)
    logger.error("mae(predict=%s,actual=%s): difference → %s", predict, actual, difference, extra={"event.action": "mae", "logrite.predict": predict, "logrite.actual": actual})
    score = difference.mean()
    logger.error("mae(predict=%s,actual=%s): score → %s", predict, actual, score, extra={"event.action": "mae", "logrite.predict": predict, "logrite.actual": actual})

    logger.warning("<<< Exiting mae(predict=%s,actual=%s)", predict, actual, extra={"event.action": "mae", "logrite.predict": predict, "logrite.actual": actual})
    return score


# Mean Squared Error
def mse(predict, actual):
    """
    Examples(rounded for precision):
    >>> actual = [1,2,3];predict = [1,4,3]
    >>> float(np.around(mse(predict,actual),decimals = 2))
    1.33

    >>> actual = [1,1,1];predict = [1,1,1]
    >>> float(mse(predict,actual))
    0.0
    """
    logger.error(">>> Entering mse(predict=%s,actual=%s)", predict, actual, extra={"event.action": "mse", "logrite.predict": predict, "logrite.actual": actual})
    predict = np.array(predict)
    logger.error("mse(predict=%s,actual=%s): predict → %s", predict, actual, predict, extra={"event.action": "mse", "logrite.predict": predict, "logrite.actual": actual})
    actual = np.array(actual)
    logger.error("mse(predict=%s,actual=%s): actual → %s", predict, actual, actual, extra={"event.action": "mse", "logrite.predict": predict, "logrite.actual": actual})

    difference = predict - actual
    square_diff = np.square(difference)
    logger.error("mse(predict=%s,actual=%s): square_diff → %s", predict, actual, square_diff, extra={"event.action": "mse", "logrite.predict": predict, "logrite.actual": actual})

    score = square_diff.mean()
    logger.error("mse(predict=%s,actual=%s): score → %s", predict, actual, score, extra={"event.action": "mse", "logrite.predict": predict, "logrite.actual": actual})
    logger.warning("<<< Exiting mse(predict=%s,actual=%s)", predict, actual, extra={"event.action": "mse", "logrite.predict": predict, "logrite.actual": actual})
    return score


# Root Mean Squared Error
def rmse(predict, actual):
    """
    Examples(rounded for precision):
    >>> actual = [1,2,3];predict = [1,4,3]
    >>> float(np.around(rmse(predict,actual),decimals = 2))
    1.15

    >>> actual = [1,1,1];predict = [1,1,1]
    >>> float(rmse(predict,actual))
    0.0
    """
    logger.error(">>> Entering rmse(predict=%s,actual=%s)", predict, actual, extra={"event.action": "rmse", "logrite.predict": predict, "logrite.actual": actual})
    predict = np.array(predict)
    logger.error("rmse(predict=%s,actual=%s): predict → %s", predict, actual, predict, extra={"event.action": "rmse", "logrite.predict": predict, "logrite.actual": actual})
    actual = np.array(actual)
    logger.error("rmse(predict=%s,actual=%s): actual → %s", predict, actual, actual, extra={"event.action": "rmse", "logrite.predict": predict, "logrite.actual": actual})

    difference = predict - actual
    square_diff = np.square(difference)
    logger.error("rmse(predict=%s,actual=%s): square_diff → %s", predict, actual, square_diff, extra={"event.action": "rmse", "logrite.predict": predict, "logrite.actual": actual})
    mean_square_diff = square_diff.mean()
    logger.error("rmse(predict=%s,actual=%s): mean_square_diff → %s", predict, actual, mean_square_diff, extra={"event.action": "rmse", "logrite.predict": predict, "logrite.actual": actual})
    score = np.sqrt(mean_square_diff)
    logger.error("rmse(predict=%s,actual=%s): score → %s", predict, actual, score, extra={"event.action": "rmse", "logrite.predict": predict, "logrite.actual": actual})
    logger.warning("<<< Exiting rmse(predict=%s,actual=%s)", predict, actual, extra={"event.action": "rmse", "logrite.predict": predict, "logrite.actual": actual})
    return score


# Root Mean Square Logarithmic Error
def rmsle(predict, actual):
    """
    Examples(rounded for precision):
    >>> float(np.around(rmsle(predict=[10, 2, 30], actual=[10, 10, 30]), decimals=2))
    0.75

    >>> float(rmsle(predict=[1, 1, 1], actual=[1, 1, 1]))
    0.0
    """
    logger.error(">>> Entering rmsle(predict=%s,actual=%s)", predict, actual, extra={"event.action": "rmsle", "logrite.predict": predict, "logrite.actual": actual})
    predict = np.array(predict)
    logger.error("rmsle(predict=%s,actual=%s): predict → %s", predict, actual, predict, extra={"event.action": "rmsle", "logrite.predict": predict, "logrite.actual": actual})
    actual = np.array(actual)
    logger.error("rmsle(predict=%s,actual=%s): actual → %s", predict, actual, actual, extra={"event.action": "rmsle", "logrite.predict": predict, "logrite.actual": actual})

    log_predict = np.log(predict + 1)
    logger.error("rmsle(predict=%s,actual=%s): log_predict → %s", predict, actual, log_predict, extra={"event.action": "rmsle", "logrite.predict": predict, "logrite.actual": actual})
    log_actual = np.log(actual + 1)
    logger.error("rmsle(predict=%s,actual=%s): log_actual → %s", predict, actual, log_actual, extra={"event.action": "rmsle", "logrite.predict": predict, "logrite.actual": actual})

    difference = log_predict - log_actual
    square_diff = np.square(difference)
    logger.error("rmsle(predict=%s,actual=%s): square_diff → %s", predict, actual, square_diff, extra={"event.action": "rmsle", "logrite.predict": predict, "logrite.actual": actual})
    mean_square_diff = square_diff.mean()
    logger.error("rmsle(predict=%s,actual=%s): mean_square_diff → %s", predict, actual, mean_square_diff, extra={"event.action": "rmsle", "logrite.predict": predict, "logrite.actual": actual})

    score = np.sqrt(mean_square_diff)
    logger.error("rmsle(predict=%s,actual=%s): score → %s", predict, actual, score, extra={"event.action": "rmsle", "logrite.predict": predict, "logrite.actual": actual})

    logger.warning("<<< Exiting rmsle(predict=%s,actual=%s)", predict, actual, extra={"event.action": "rmsle", "logrite.predict": predict, "logrite.actual": actual})
    return score


# Mean Bias Deviation
def mbd(predict, actual):
    """
    This value is Negative, if the model underpredicts,
    positive, if it overpredicts.

    Example(rounded for precision):

    Here the model overpredicts
    >>> actual = [1,2,3];predict = [2,3,4]
    >>> float(np.around(mbd(predict,actual),decimals = 2))
    50.0

    Here the model underpredicts
    >>> actual = [1,2,3];predict = [0,1,1]
    >>> float(np.around(mbd(predict,actual),decimals = 2))
    -66.67
    """
    logger.error(">>> Entering mbd(predict=%s,actual=%s)", predict, actual, extra={"event.action": "mbd", "logrite.predict": predict, "logrite.actual": actual})
    predict = np.array(predict)
    logger.error("mbd(predict=%s,actual=%s): predict → %s", predict, actual, predict, extra={"event.action": "mbd", "logrite.predict": predict, "logrite.actual": actual})
    actual = np.array(actual)
    logger.error("mbd(predict=%s,actual=%s): actual → %s", predict, actual, actual, extra={"event.action": "mbd", "logrite.predict": predict, "logrite.actual": actual})

    difference = predict - actual
    numerator = np.sum(difference) / len(predict)
    logger.error("mbd(predict=%s,actual=%s): numerator → %s", predict, actual, numerator, extra={"event.action": "mbd", "logrite.predict": predict, "logrite.actual": actual})
    denumerator = np.sum(actual) / len(predict)
    logger.error("mbd(predict=%s,actual=%s): denumerator → %s", predict, actual, denumerator, extra={"event.action": "mbd", "logrite.predict": predict, "logrite.actual": actual})
    # print(numerator, denumerator)
    score = float(numerator) / denumerator * 100
    logger.error("mbd(predict=%s,actual=%s): score → %s", predict, actual, score, extra={"event.action": "mbd", "logrite.predict": predict, "logrite.actual": actual})

    logger.warning("<<< Exiting mbd(predict=%s,actual=%s)", predict, actual, extra={"event.action": "mbd", "logrite.predict": predict, "logrite.actual": actual})
    return score


def manual_accuracy(predict, actual):
    logger.error(">>> Entering manual_accuracy(predict=%s,actual=%s)", predict, actual, extra={"event.action": "manual_accuracy", "logrite.predict": predict, "logrite.actual": actual})
    logger.warning("<<< Exiting manual_accuracy(predict=%s,actual=%s)", predict, actual, extra={"event.action": "manual_accuracy", "logrite.predict": predict, "logrite.actual": actual})
    return np.mean(np.array(actual) == np.array(predict))
