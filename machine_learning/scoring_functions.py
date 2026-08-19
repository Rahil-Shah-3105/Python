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
    logger.debug(">>> Entering mae(predict=%s,actual=%s)", predict, actual)
    predict = np.array(predict)
    logger.debug("mae(predict=%s,actual=%s): predict → %s", predict, actual, predict)
    actual = np.array(actual)
    logger.debug("mae(predict=%s,actual=%s): actual → %s", predict, actual, actual)

    difference = abs(predict - actual)
    logger.debug("mae(predict=%s,actual=%s): difference → %s", predict, actual, difference)
    score = difference.mean()
    logger.debug("mae(predict=%s,actual=%s): score → %s", predict, actual, score)

    logger.debug("<<< Exiting mae(predict=%s,actual=%s)", predict, actual)
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
    logger.debug(">>> Entering mse(predict=%s,actual=%s)", predict, actual)
    predict = np.array(predict)
    logger.debug("mse(predict=%s,actual=%s): predict → %s", predict, actual, predict)
    actual = np.array(actual)
    logger.debug("mse(predict=%s,actual=%s): actual → %s", predict, actual, actual)

    difference = predict - actual
    logger.debug("mse(predict=%s,actual=%s): difference → %s", predict, actual, difference)
    square_diff = np.square(difference)
    logger.debug("mse(predict=%s,actual=%s): square_diff → %s", predict, actual, square_diff)

    score = square_diff.mean()
    logger.debug("mse(predict=%s,actual=%s): score → %s", predict, actual, score)
    logger.debug("<<< Exiting mse(predict=%s,actual=%s)", predict, actual)
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
    logger.debug(">>> Entering rmse(predict=%s,actual=%s)", predict, actual)
    predict = np.array(predict)
    logger.debug("rmse(predict=%s,actual=%s): predict → %s", predict, actual, predict)
    actual = np.array(actual)
    logger.debug("rmse(predict=%s,actual=%s): actual → %s", predict, actual, actual)

    difference = predict - actual
    logger.debug("rmse(predict=%s,actual=%s): difference → %s", predict, actual, difference)
    square_diff = np.square(difference)
    logger.debug("rmse(predict=%s,actual=%s): square_diff → %s", predict, actual, square_diff)
    mean_square_diff = square_diff.mean()
    logger.debug("rmse(predict=%s,actual=%s): mean_square_diff → %s", predict, actual, mean_square_diff)
    score = np.sqrt(mean_square_diff)
    logger.debug("rmse(predict=%s,actual=%s): score → %s", predict, actual, score)
    logger.debug("<<< Exiting rmse(predict=%s,actual=%s)", predict, actual)
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
    logger.debug(">>> Entering rmsle(predict=%s,actual=%s)", predict, actual)
    predict = np.array(predict)
    logger.debug("rmsle(predict=%s,actual=%s): predict → %s", predict, actual, predict)
    actual = np.array(actual)
    logger.debug("rmsle(predict=%s,actual=%s): actual → %s", predict, actual, actual)

    log_predict = np.log(predict + 1)
    logger.debug("rmsle(predict=%s,actual=%s): log_predict → %s", predict, actual, log_predict)
    log_actual = np.log(actual + 1)
    logger.debug("rmsle(predict=%s,actual=%s): log_actual → %s", predict, actual, log_actual)

    difference = log_predict - log_actual
    logger.debug("rmsle(predict=%s,actual=%s): difference → %s", predict, actual, difference)
    square_diff = np.square(difference)
    logger.debug("rmsle(predict=%s,actual=%s): square_diff → %s", predict, actual, square_diff)
    mean_square_diff = square_diff.mean()
    logger.debug("rmsle(predict=%s,actual=%s): mean_square_diff → %s", predict, actual, mean_square_diff)

    score = np.sqrt(mean_square_diff)
    logger.debug("rmsle(predict=%s,actual=%s): score → %s", predict, actual, score)

    logger.debug("<<< Exiting rmsle(predict=%s,actual=%s)", predict, actual)
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
    logger.debug(">>> Entering mbd(predict=%s,actual=%s)", predict, actual)
    predict = np.array(predict)
    logger.debug("mbd(predict=%s,actual=%s): predict → %s", predict, actual, predict)
    actual = np.array(actual)
    logger.debug("mbd(predict=%s,actual=%s): actual → %s", predict, actual, actual)

    difference = predict - actual
    logger.debug("mbd(predict=%s,actual=%s): difference → %s", predict, actual, difference)
    numerator = np.sum(difference) / len(predict)
    logger.debug("mbd(predict=%s,actual=%s): numerator → %s", predict, actual, numerator)
    denumerator = np.sum(actual) / len(predict)
    logger.debug("mbd(predict=%s,actual=%s): denumerator → %s", predict, actual, denumerator)
    # print(numerator, denumerator)
    score = float(numerator) / denumerator * 100
    logger.debug("mbd(predict=%s,actual=%s): score → %s", predict, actual, score)

    logger.debug("<<< Exiting mbd(predict=%s,actual=%s)", predict, actual)
    return score


def manual_accuracy(predict, actual):
    logger.debug(">>> Entering manual_accuracy(predict=%s,actual=%s)", predict, actual)
    logger.debug("<<< Exiting manual_accuracy(predict=%s,actual=%s)", predict, actual)
    return np.mean(np.array(actual) == np.array(predict))
