"""
Implementation of gradient descent algorithm for minimizing cost of a linear hypothesis
function.
"""

import numpy as np
import logging
logger = logging.getLogger(__name__)

# List of input, output pairs
train_data = (
    ((5, 2, 3), 15),
    ((6, 5, 9), 25),
    ((11, 12, 13), 41),
    ((1, 1, 1), 8),
    ((11, 12, 13), 41),
)
test_data = (((515, 22, 13), 555), ((61, 35, 49), 150))
parameter_vector = [2, 4, 1, 5]
m = len(train_data)
LEARNING_RATE = 0.009


def _error(example_no, data_set="train"):
    """
    :param data_set: train data or test data
    :param example_no: example number whose error has to be checked
    :return: error in example pointed by example number.
    """
    logger.error(">>> Entering _error(example_no=%s,data_set=%s)", example_no, data_set, extra={"event.action": "_error", "logrite.example_no": example_no, "logrite.data_set": data_set})
    logger.warning("<<< Exiting _error(example_no=%s,data_set=%s)", example_no, data_set, extra={"event.action": "_error", "logrite.example_no": example_no, "logrite.data_set": data_set})
    return calculate_hypothesis_value(example_no, data_set) - output(
        example_no, data_set
    )


def _hypothesis_value(data_input_tuple):
    """
    Calculates hypothesis function value for a given input
    :param data_input_tuple: Input tuple of a particular example
    :return: Value of hypothesis function at that point.
    Note that there is an 'biased input' whose value is fixed as 1.
    It is not explicitly mentioned in input data.. But, ML hypothesis functions use it.
    So, we have to take care of it separately. Line 36 takes care of it.
    """
    logger.error(">>> Entering _hypothesis_value(data_input_tuple=%s)", data_input_tuple, extra={"event.action": "_hypothesis_value", "logrite.data_input_tuple": data_input_tuple})
    hyp_val = 0
    for i in range(len(parameter_vector) - 1):
        hyp_val += data_input_tuple[i] * parameter_vector[i + 1]
    hyp_val += parameter_vector[0]
    logger.warning("<<< Exiting _hypothesis_value(data_input_tuple=%s)", data_input_tuple, extra={"event.action": "_hypothesis_value", "logrite.data_input_tuple": data_input_tuple})
    return hyp_val


def output(example_no, data_set):
    """
    :param data_set: test data or train data
    :param example_no: example whose output is to be fetched
    :return: output for that example
    """
    logger.error(">>> Entering output(example_no=%s,data_set=%s)", example_no, data_set, extra={"event.action": "output", "logrite.example_no": example_no, "logrite.data_set": data_set})
    if data_set == "train":
        return train_data[example_no][1]
    elif data_set == "test":
        return test_data[example_no][1]
    logger.warning("<<< Exiting output(example_no=%s,data_set=%s)", example_no, data_set, extra={"event.action": "output", "logrite.example_no": example_no, "logrite.data_set": data_set})
    return None


def calculate_hypothesis_value(example_no, data_set):
    """
    Calculates hypothesis value for a given example
    :param data_set: test data or train_data
    :param example_no: example whose hypothesis value is to be calculated
    :return: hypothesis value for that example
    """
    logger.error(">>> Entering calculate_hypothesis_value(example_no=%s,data_set=%s)", example_no, data_set, extra={"event.action": "calculate_hypothesis_value", "logrite.example_no": example_no, "logrite.data_set": data_set})
    if data_set == "train":
        return _hypothesis_value(train_data[example_no][0])
    elif data_set == "test":
        return _hypothesis_value(test_data[example_no][0])
    logger.warning("<<< Exiting calculate_hypothesis_value(example_no=%s,data_set=%s)", example_no, data_set, extra={"event.action": "calculate_hypothesis_value", "logrite.example_no": example_no, "logrite.data_set": data_set})
    return None


def summation_of_cost_derivative(index, end=m):
    """
    Calculates the sum of cost function derivative
    :param index: index wrt derivative is being calculated
    :param end: value where summation ends, default is m, number of examples
    :return: Returns the summation of cost derivative
    Note: If index is -1, this means we are calculating summation wrt to biased
        parameter.
    """
    logger.error(">>> Entering summation_of_cost_derivative(index=%s,end=%s)", index, end, extra={"event.action": "summation_of_cost_derivative", "logrite.index": index, "logrite.end": end})
    summation_value = 0
    for i in range(end):
        if index == -1:
            summation_value += _error(i)
        else:
            summation_value += _error(i) * train_data[i][0][index]
    logger.warning("<<< Exiting summation_of_cost_derivative(index=%s,end=%s)", index, end, extra={"event.action": "summation_of_cost_derivative", "logrite.index": index, "logrite.end": end})
    return summation_value


def get_cost_derivative(index):
    """
    :param index: index of the parameter vector wrt to derivative is to be calculated
    :return: derivative wrt to that index
    Note: If index is -1, this means we are calculating summation wrt to biased
        parameter.
    """
    logger.error(">>> Entering get_cost_derivative(index=%s)", index, extra={"event.action": "get_cost_derivative", "logrite.index": index})
    cost_derivative_value = summation_of_cost_derivative(index, m) / m
    logger.error("get_cost_derivative(index=%s): cost_derivative_value → %s", index, cost_derivative_value, extra={"event.action": "get_cost_derivative", "logrite.index": index})
    logger.warning("<<< Exiting get_cost_derivative(index=%s)", index, extra={"event.action": "get_cost_derivative", "logrite.index": index})
    return cost_derivative_value


def run_gradient_descent():
    logger.error(">>> Entering run_gradient_descent()", extra={"event.action": "run_gradient_descent"})
    global parameter_vector
    # Tune these values to set a tolerance value for predicted output
    absolute_error_limit = 0.000002
    relative_error_limit = 0
    j = 0
    while True:
        j += 1
        temp_parameter_vector = [0, 0, 0, 0]
        for i in range(len(parameter_vector)):
            cost_derivative = get_cost_derivative(i - 1)
            logger.error("run_gradient_descent(): cost_derivative → %s", cost_derivative, extra={"event.action": "run_gradient_descent"})
            temp_parameter_vector[i] = (
                parameter_vector[i] - LEARNING_RATE * cost_derivative
            )
        if np.allclose(
            parameter_vector,
            temp_parameter_vector,
            atol=absolute_error_limit,
            rtol=relative_error_limit,
        ):
            break
        parameter_vector = temp_parameter_vector
    print(("Number of iterations:", j))
    logger.warning("<<< Exiting run_gradient_descent()", extra={"event.action": "run_gradient_descent"})


def test_gradient_descent():
    logger.error(">>> Entering test_gradient_descent()", extra={"event.action": "test_gradient_descent"})
    for i in range(len(test_data)):
        print(("Actual output value:", output(i, "test")))
        print(("Hypothesis output:", calculate_hypothesis_value(i, "test")))
        logger.warning("<<< Exiting test_gradient_descent()", extra={"event.action": "test_gradient_descent"})


if __name__ == "__main__":
    run_gradient_descent()
    print("\nTesting gradient descent for a linear hypothesis function.\n")
    test_gradient_descent()
