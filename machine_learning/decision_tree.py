"""
Implementation of a basic regression decision tree.
Input data set: The input data set must be 1-dimensional with continuous labels.
Output: The decision tree maps a real number input to a real number output.
"""

import numpy as np
import logging
logger = logging.getLogger(__name__)


class DecisionTree:
    def __init__(self, depth=5, min_leaf_size=5):
        logger.error(">>> Entering __init__(depth=%s,min_leaf_size=%s)", depth, min_leaf_size, extra={"event.action": "__init__", "logrite.depth": depth, "logrite.min_leaf_size": min_leaf_size})
        self.depth = depth
        logger.debug("__init__(self=%s,depth=%s,min_leaf_size=%s): self.depth → %s", self, depth, min_leaf_size, self.depth, extra={"event.action": "__init__", "logrite.depth": depth, "logrite.min_leaf_size": min_leaf_size})
        self.decision_boundary = 0
        logger.debug("__init__(self=%s,depth=%s,min_leaf_size=%s): self.decision_boundary → %s", self, depth, min_leaf_size, self.decision_boundary, extra={"event.action": "__init__", "logrite.depth": depth, "logrite.min_leaf_size": min_leaf_size})
        self.left = None
        logger.debug("__init__(self=%s,depth=%s,min_leaf_size=%s): self.left → %s", self, depth, min_leaf_size, self.left, extra={"event.action": "__init__", "logrite.depth": depth, "logrite.min_leaf_size": min_leaf_size})
        self.right = None
        logger.debug("__init__(self=%s,depth=%s,min_leaf_size=%s): self.right → %s", self, depth, min_leaf_size, self.right, extra={"event.action": "__init__", "logrite.depth": depth, "logrite.min_leaf_size": min_leaf_size})
        self.min_leaf_size = min_leaf_size
        logger.debug("__init__(self=%s,depth=%s,min_leaf_size=%s): self.min_leaf_size → %s", self, depth, min_leaf_size, self.min_leaf_size, extra={"event.action": "__init__", "logrite.depth": depth, "logrite.min_leaf_size": min_leaf_size})
        self.prediction = None
        logger.warning("<<< Exiting __init__(depth=%s,min_leaf_size=%s)", depth, min_leaf_size, extra={"event.action": "__init__", "logrite.depth": depth, "logrite.min_leaf_size": min_leaf_size})
        logger.debug("__init__(self=%s,depth=%s,min_leaf_size=%s): self.prediction → %s", self, depth, min_leaf_size, self.prediction, extra={"event.action": "__init__", "logrite.depth": depth, "logrite.min_leaf_size": min_leaf_size})

    def mean_squared_error(self, labels, prediction):
        """
        mean_squared_error:
        @param labels: a one-dimensional numpy array
        @param prediction: a floating point value
        return value: mean_squared_error calculates the error if prediction is used to
            estimate the labels
        >>> tester = DecisionTree()
        >>> test_labels = np.array([1,2,3,4,5,6,7,8,9,10])
        >>> test_prediction = float(6)
        >>> bool(tester.mean_squared_error(test_labels, test_prediction) == (
        ...     TestDecisionTree.helper_mean_squared_error_test(test_labels,
        ...         test_prediction)))
        True
        >>> test_labels = np.array([1,2,3])
        >>> test_prediction = float(2)
        >>> bool(tester.mean_squared_error(test_labels, test_prediction) == (
        ...     TestDecisionTree.helper_mean_squared_error_test(test_labels,
        ...         test_prediction)))
        True
        """
        logger.error(">>> Entering mean_squared_error(labels=%s,prediction=%s)", labels, prediction, extra={"event.action": "mean_squared_error", "logrite.labels": labels, "logrite.prediction": prediction})
        if labels.ndim != 1:
            print("Error: Input labels must be one dimensional")

        logger.warning("<<< Exiting mean_squared_error(labels=%s,prediction=%s)", labels, prediction, extra={"event.action": "mean_squared_error", "logrite.labels": labels, "logrite.prediction": prediction})
        return np.mean((labels - prediction) ** 2)

    def train(self, x, y):
        """
        train:
        @param x: a one-dimensional numpy array
        @param y: a one-dimensional numpy array.
        The contents of y are the labels for the corresponding X values

        train() does not have a return value

        Examples:
        1. Try to train when x & y are of same length & 1 dimensions (No errors)
        >>> dt = DecisionTree()
        >>> dt.train(np.array([10,20,30,40,50]),np.array([0,0,0,1,1]))

        2. Try to train when x is 2 dimensions
        >>> dt = DecisionTree()
        >>> dt.train(np.array([[1,2,3,4,5],[1,2,3,4,5]]),np.array([0,0,0,1,1]))
        Traceback (most recent call last):
            ...
        ValueError: Input data set must be one-dimensional

        3. Try to train when x and y are not of the same length
        >>> dt = DecisionTree()
        >>> dt.train(np.array([1,2,3,4,5]),np.array([[0,0,0,1,1],[0,0,0,1,1]]))
        Traceback (most recent call last):
            ...
        ValueError: x and y have different lengths

        4. Try to train when x & y are of the same length but different dimensions
        >>> dt = DecisionTree()
        >>> dt.train(np.array([1,2,3,4,5]),np.array([[1],[2],[3],[4],[5]]))
        Traceback (most recent call last):
            ...
        ValueError: Data set labels must be one-dimensional

        This section is to check that the inputs conform to our dimensionality
        constraints
        """
        logger.error(">>> Entering train(x=%s,y=%s)", x, y, extra={"event.action": "train", "logrite.x": x, "logrite.y": y})
        if x.ndim != 1:
            raise ValueError("Input data set must be one-dimensional")
        if len(x) != len(y):
            raise ValueError("x and y have different lengths")
        if y.ndim != 1:
            raise ValueError("Data set labels must be one-dimensional")

        if len(x) < 2 * self.min_leaf_size:
            self.prediction = np.mean(y)
            logger.error("train(x=%s,y=%s): self.prediction → %s", x, y, self.prediction, extra={"event.action": "train", "logrite.x": x, "logrite.y": y})
            return

        if self.depth == 1:
            self.prediction = np.mean(y)
            return

        best_split = 0
        min_error = self.mean_squared_error(x, np.mean(y)) * 2

        """
        loop over all possible splits for the decision tree. find the best split.
        if no split exists that is less than 2 * error for the entire array
        then the data set is not split and the average for the entire array is used as
        the predictor
        """
        for i in range(len(x)):
            if len(x[:i]) < self.min_leaf_size:  # noqa: SIM114
                continue
            elif len(x[i:]) < self.min_leaf_size:
                continue
            else:
                error_left = self.mean_squared_error(x[:i], np.mean(y[:i]))
                error_right = self.mean_squared_error(x[i:], np.mean(y[i:]))
                error = error_left + error_right
                if error < min_error:
                    best_split = i
                    min_error = error

        if best_split != 0:
            left_x = x[:best_split]
            left_y = y[:best_split]
            right_x = x[best_split:]
            right_y = y[best_split:]

            self.decision_boundary = x[best_split]
            logger.debug("train(self=%s,x=%s,y=%s): self.decision_boundary → %s", self, x, y, self.decision_boundary, extra={"event.action": "train", "logrite.x": x, "logrite.y": y})
            self.left = DecisionTree(
                depth=self.depth - 1, min_leaf_size=self.min_leaf_size
            )
            self.right = DecisionTree(
                depth=self.depth - 1, min_leaf_size=self.min_leaf_size
            )
            self.left.train(left_x, left_y)
            self.right.train(right_x, right_y)
        else:
            self.prediction = np.mean(y)

        logger.warning("<<< Exiting train(x=%s,y=%s)", x, y, extra={"event.action": "train", "logrite.x": x, "logrite.y": y})
        return

    def predict(self, x):
        """
        predict:
        @param x: a floating point value to predict the label of
        the prediction function works by recursively calling the predict function
        of the appropriate subtrees based on the tree's decision boundary
        """
        logger.error(">>> Entering predict(x=%s)", x, extra={"event.action": "predict", "logrite.x": x})
        if self.prediction is not None:
            return self.prediction
        elif self.left is not None and self.right is not None:
            if x >= self.decision_boundary:
                return self.right.predict(x)
            else:
                return self.left.predict(x)
        else:
            logger.warning("<<< Exiting predict(x=%s)", x, extra={"event.action": "predict", "logrite.x": x})
            raise ValueError("Decision tree not yet trained")


class TestDecisionTree:
    """Decision Tres test class"""

    @staticmethod
    def helper_mean_squared_error_test(labels, prediction):
        """
        helper_mean_squared_error_test:
        @param labels: a one dimensional numpy array
        @param prediction: a floating point value
        return value: helper_mean_squared_error_test calculates the mean squared error
        """
        logger.error(">>> Entering helper_mean_squared_error_test(labels=%s,prediction=%s)", labels, prediction, extra={"event.action": "helper_mean_squared_error_test", "logrite.labels": labels, "logrite.prediction": prediction})
        squared_error_sum = float(0)
        for label in labels:
            squared_error_sum += (label - prediction) ** 2

        logger.warning("<<< Exiting helper_mean_squared_error_test(labels=%s,prediction=%s)", labels, prediction, extra={"event.action": "helper_mean_squared_error_test", "logrite.labels": labels, "logrite.prediction": prediction})
        return float(squared_error_sum / labels.size)


def main():
    """
    In this demonstration we're generating a sample data set from the sin function in
    numpy.  We then train a decision tree on the data set and use the decision tree to
    predict the label of 10 different test values. Then the mean squared error over
    this test is displayed.
    """
    logger.error(">>> Entering main()", extra={"event.action": "main"})
    x = np.arange(-1.0, 1.0, 0.005)
    logger.error("main(): x → %s", x, extra={"event.action": "main"})
    y = np.sin(x)
    logger.error("main(): y → %s", y, extra={"event.action": "main"})

    tree = DecisionTree(depth=10, min_leaf_size=10)
    logger.error("main(): tree → %s", tree, extra={"event.action": "main"})
    tree.train(x, y)

    rng = np.random.default_rng()
    logger.error("main(): rng → %s", rng, extra={"event.action": "main"})
    test_cases = (rng.random(10) * 2) - 1
    logger.error("main(): test_cases → %s", test_cases, extra={"event.action": "main"})
    predictions = np.array([tree.predict(x) for x in test_cases])
    logger.error("main(): predictions → %s", predictions, extra={"event.action": "main"})
    avg_error = np.mean((predictions - test_cases) ** 2)
    logger.error("main(): avg_error → %s", avg_error, extra={"event.action": "main"})

    print("Test values: " + str(test_cases))
    print("Predictions: " + str(predictions))
    print("Average error: " + str(avg_error))
    logger.warning("<<< Exiting main()", extra={"event.action": "main"})


if __name__ == "__main__":
    main()
    import doctest

    doctest.testmod(name="mean_squared_error", verbose=True)
