"""
Linear regression is the most basic type of regression commonly used for
predictive analysis. The idea is pretty simple: we have a dataset and we have
features associated with it. Features should be chosen very cautiously
as they determine how much our model will be able to make future predictions.
We try to set the weight of these features, over many iterations, so that they best
fit our dataset. In this particular code, I had used a CSGO dataset (ADR vs
Rating). We try to best fit a line through dataset and estimate the parameters.
"""

# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "httpx",
#     "numpy",
# ]
# ///

import httpx
import numpy as np
import time
import logging
logger = logging.getLogger(__name__)


def collect_dataset():
    __log_start = time.time()
    """Collect dataset of CSGO
    The dataset contains ADR vs Rating of a Player
    :return : dataset obtained from the link, as matrix
    """
    logger.error(">>> Entering collect_dataset()", extra={"event.action": "collect_dataset"})
    response = httpx.get(
        "https://raw.githubusercontent.com/yashLadha/The_Math_of_Intelligence/"
        "master/Week1/ADRvsRating.csv",
        timeout=10,
    )
    logger.error("collect_dataset(): response → %s", response, extra={"event.action": "collect_dataset"})
    lines = response.text.splitlines()
    logger.error("collect_dataset(): lines → %s", lines, extra={"event.action": "collect_dataset"})
    data = []
    logger.error("collect_dataset(): data → %s", data, extra={"event.action": "collect_dataset"})
    for item in lines:
        item = item.split(",")
        logger.error("collect_dataset(): item → %s", item, extra={"event.action": "collect_dataset"})
        data.append(item)
    data.pop(0)  # This is for removing the labels from the list
    logger.error("collect_dataset()=: external service call took %s ms", int((time.time() - __log_start) * 1000), extra={"event.action": "collect_dataset", "event.category": "network"})
    dataset = np.matrix(data)
    logger.error("collect_dataset(): dataset → %s", dataset, extra={"event.action": "collect_dataset"})
    logger.warning("<<< Exiting collect_dataset()", extra={"event.action": "collect_dataset"})
    return dataset


def run_steep_gradient_descent(data_x, data_y, len_data, alpha, theta):
    """Run steep gradient descent and updates the Feature vector accordingly_
    :param data_x   : contains the dataset
    :param data_y   : contains the output associated with each data-entry
    :param len_data : length of the data_
    :param alpha    : Learning rate of the model
    :param theta    : Feature vector (weight's for our model)
    ;param return    : Updated Feature's, using
                       curr_features - alpha_ * gradient(w.r.t. feature)
    >>> import numpy as np
    >>> data_x = np.array([[1, 2], [3, 4]])
    >>> data_y = np.array([5, 6])
    >>> len_data = len(data_x)
    >>> alpha = 0.01
    >>> theta = np.array([0.1, 0.2])
    >>> run_steep_gradient_descent(data_x, data_y, len_data, alpha, theta)
    array([0.196, 0.343])
    """
    logger.error(">>> Entering run_steep_gradient_descent(data_x=%s,data_y=%s,len_data=%s,alpha=%s,theta=%s)", data_x, data_y, len_data, alpha, theta, extra={"event.action": "run_steep_gradient_descent", "logrite.data_x": data_x, "logrite.data_y": data_y, "logrite.len_data": len_data, "logrite.alpha": alpha, "logrite.theta": theta})
    n = len_data

    prod = np.dot(theta, data_x.transpose())
    logger.error("run_steep_gradient_descent(data_x=%s,data_y=%s,len_data=%s,alpha=%s,theta=%s): prod → %s", data_x, data_y, len_data, alpha, theta, prod, extra={"event.action": "run_steep_gradient_descent", "logrite.data_x": data_x, "logrite.data_y": data_y, "logrite.len_data": len_data, "logrite.alpha": alpha, "logrite.theta": theta})
    prod -= data_y.transpose()
    sum_grad = np.dot(prod, data_x)
    logger.error("run_steep_gradient_descent(data_x=%s,data_y=%s,len_data=%s,alpha=%s,theta=%s): sum_grad → %s", data_x, data_y, len_data, alpha, theta, sum_grad, extra={"event.action": "run_steep_gradient_descent", "logrite.data_x": data_x, "logrite.data_y": data_y, "logrite.len_data": len_data, "logrite.alpha": alpha, "logrite.theta": theta})
    theta = theta - (alpha / n) * sum_grad
    logger.error("run_steep_gradient_descent(data_x=%s,data_y=%s,len_data=%s,alpha=%s,theta=%s): theta → %s", data_x, data_y, len_data, alpha, theta, theta, extra={"event.action": "run_steep_gradient_descent", "logrite.data_x": data_x, "logrite.data_y": data_y, "logrite.len_data": len_data, "logrite.alpha": alpha, "logrite.theta": theta})
    logger.warning("<<< Exiting run_steep_gradient_descent(data_x=%s,data_y=%s,len_data=%s,alpha=%s,theta=%s)", data_x, data_y, len_data, alpha, theta, extra={"event.action": "run_steep_gradient_descent", "logrite.data_x": data_x, "logrite.data_y": data_y, "logrite.len_data": len_data, "logrite.alpha": alpha, "logrite.theta": theta})
    return theta


def sum_of_square_error(data_x, data_y, len_data, theta):
    """Return sum of square error for error calculation
    :param data_x    : contains our dataset
    :param data_y    : contains the output (result vector)
    :param len_data  : len of the dataset
    :param theta     : contains the feature vector
    :return          : sum of square error computed from given feature's

    Example:
    >>> vc_x = np.array([[1.1], [2.1], [3.1]])
    >>> vc_y = np.array([1.2, 2.2, 3.2])
    >>> round(sum_of_square_error(vc_x, vc_y, 3, np.array([1])),3)
    np.float64(0.005)
    """
    logger.error(">>> Entering sum_of_square_error(data_x=%s,data_y=%s,len_data=%s,theta=%s)", data_x, data_y, len_data, theta, extra={"event.action": "sum_of_square_error", "logrite.data_x": data_x, "logrite.data_y": data_y, "logrite.len_data": len_data, "logrite.theta": theta})
    prod = np.dot(theta, data_x.transpose())
    logger.error("sum_of_square_error(data_x=%s,data_y=%s,len_data=%s,theta=%s): prod → %s", data_x, data_y, len_data, theta, prod, extra={"event.action": "sum_of_square_error", "logrite.data_x": data_x, "logrite.data_y": data_y, "logrite.len_data": len_data, "logrite.theta": theta})
    prod -= data_y.transpose()
    sum_elem = np.sum(np.square(prod))
    logger.error("sum_of_square_error(data_x=%s,data_y=%s,len_data=%s,theta=%s): sum_elem → %s", data_x, data_y, len_data, theta, sum_elem, extra={"event.action": "sum_of_square_error", "logrite.data_x": data_x, "logrite.data_y": data_y, "logrite.len_data": len_data, "logrite.theta": theta})
    error = sum_elem / (2 * len_data)
    logger.error("sum_of_square_error(data_x=%s,data_y=%s,len_data=%s,theta=%s): error → %s", data_x, data_y, len_data, theta, error, extra={"event.action": "sum_of_square_error", "logrite.data_x": data_x, "logrite.data_y": data_y, "logrite.len_data": len_data, "logrite.theta": theta})
    logger.warning("<<< Exiting sum_of_square_error(data_x=%s,data_y=%s,len_data=%s,theta=%s)", data_x, data_y, len_data, theta, extra={"event.action": "sum_of_square_error", "logrite.data_x": data_x, "logrite.data_y": data_y, "logrite.len_data": len_data, "logrite.theta": theta})
    return error


def run_linear_regression(data_x, data_y):
    """Implement Linear regression over the dataset
    :param data_x  : contains our dataset
    :param data_y  : contains the output (result vector)
    :return        : feature for line of best fit (Feature vector)
    """
    logger.error(">>> Entering run_linear_regression(data_x=%s,data_y=%s)", data_x, data_y, extra={"event.action": "run_linear_regression", "logrite.data_x": data_x, "logrite.data_y": data_y})
    iterations = 100000
    alpha = 0.0001550

    no_features = data_x.shape[1]
    len_data = data_x.shape[0] - 1
    logger.error("run_linear_regression(data_x=%s,data_y=%s): len_data → %s", data_x, data_y, len_data, extra={"event.action": "run_linear_regression", "logrite.data_x": data_x, "logrite.data_y": data_y})

    theta = np.zeros((1, no_features))
    logger.error("run_linear_regression(data_x=%s,data_y=%s): theta → %s", data_x, data_y, theta, extra={"event.action": "run_linear_regression", "logrite.data_x": data_x, "logrite.data_y": data_y})

    for i in range(iterations):
        theta = run_steep_gradient_descent(data_x, data_y, len_data, alpha, theta)
        error = sum_of_square_error(data_x, data_y, len_data, theta)
        logger.error("run_linear_regression(data_x=%s,data_y=%s): error → %s", data_x, data_y, error, extra={"event.action": "run_linear_regression", "logrite.data_x": data_x, "logrite.data_y": data_y})
        print(f"At Iteration {i + 1} - Error is {error:.5f}")

    logger.warning("<<< Exiting run_linear_regression(data_x=%s,data_y=%s)", data_x, data_y, extra={"event.action": "run_linear_regression", "logrite.data_x": data_x, "logrite.data_y": data_y})
    return theta


def mean_absolute_error(predicted_y, original_y):
    """Return sum of square error for error calculation
    :param predicted_y   : contains the output of prediction (result vector)
    :param original_y    : contains values of expected outcome
    :return          : mean absolute error computed from given feature's

    >>> predicted_y = [3, -0.5, 2, 7]
    >>> original_y = [2.5, 0.0, 2, 8]
    >>> mean_absolute_error(predicted_y, original_y)
    0.5
    """
    logger.error(">>> Entering mean_absolute_error(predicted_y=%s,original_y=%s)", predicted_y, original_y, extra={"event.action": "mean_absolute_error", "logrite.predicted_y": predicted_y, "logrite.original_y": original_y})
    total = sum(abs(y - predicted_y[i]) for i, y in enumerate(original_y))
    logger.error("mean_absolute_error(predicted_y=%s,original_y=%s): total → %s", predicted_y, original_y, total, extra={"event.action": "mean_absolute_error", "logrite.predicted_y": predicted_y, "logrite.original_y": original_y})
    logger.warning("<<< Exiting mean_absolute_error(predicted_y=%s,original_y=%s)", predicted_y, original_y, extra={"event.action": "mean_absolute_error", "logrite.predicted_y": predicted_y, "logrite.original_y": original_y})
    return total / len(original_y)


def main():
    """Driver function"""
    logger.error(">>> Entering main()", extra={"event.action": "main"})
    data = collect_dataset()
    logger.error("main(): data → %s", data, extra={"event.action": "main"})

    len_data = data.shape[0]
    logger.error("main(): len_data → %s", len_data, extra={"event.action": "main"})
    data_x = np.c_[np.ones(len_data), data[:, :-1]].astype(float)
    logger.error("main(): data_x → %s", data_x, extra={"event.action": "main"})
    data_y = data[:, -1].astype(float)
    logger.error("main(): data_y → %s", data_y, extra={"event.action": "main"})

    theta = run_linear_regression(data_x, data_y)
    logger.error("main(): theta → %s", theta, extra={"event.action": "main"})
    len_result = theta.shape[1]
    logger.error("main(): len_result → %s", len_result, extra={"event.action": "main"})
    print("Resultant Feature vector : ")
    for i in range(len_result):
        print(f"{theta[0, i]:.5f}")
        logger.warning("<<< Exiting main()", extra={"event.action": "main"})


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
