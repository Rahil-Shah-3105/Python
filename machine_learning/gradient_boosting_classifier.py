import numpy as np
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
import logging
logger = logging.getLogger(__name__)


class GradientBoostingClassifier:
    def __init__(self, n_estimators: int = 100, learning_rate: float = 0.1) -> None:
        """
        Initialize a GradientBoostingClassifier.

        Parameters:
        - n_estimators (int): The number of weak learners to train.
        - learning_rate (float): The learning rate for updating the model.

        Attributes:
        - n_estimators (int): The number of weak learners.
        - learning_rate (float): The learning rate.
        - models (list): A list to store the trained weak learners.
        """
        logger.debug(">>> Entering __init__(n_estimators=%s,learning_rate=%s)", n_estimators, learning_rate)
        self.n_estimators = n_estimators
        logger.debug("__init__(self=%s,n_estimators=%s,learning_rate=%s): self.n_estimators → %s", self, n_estimators, learning_rate, self.n_estimators)
        self.learning_rate = learning_rate
        logger.debug("__init__(self=%s,n_estimators=%s,learning_rate=%s): self.learning_rate → %s", self, n_estimators, learning_rate, self.learning_rate)
        self.models: list[tuple[DecisionTreeRegressor, float]] = []
        logger.debug("<<< Exiting __init__(n_estimators=%s,learning_rate=%s)", n_estimators, learning_rate)

    def fit(self, features: np.ndarray, target: np.ndarray) -> None:
        """
        Fit the GradientBoostingClassifier to the training data.

        Parameters:
        - features (np.ndarray): The training features.
        - target (np.ndarray): The target values.

        Returns:
        None

        >>> import numpy as np
        >>> from sklearn.datasets import load_iris
        >>> clf = GradientBoostingClassifier(n_estimators=100, learning_rate=0.1)
        >>> iris = load_iris()
        >>> X, y = iris.data, iris.target
        >>> clf.fit(X, y)
        >>> # Check if the model is trained
        >>> len(clf.models) == 100
        True
        """
        logger.debug(">>> Entering fit(features=%s,target=%s)", features, target)
        for _ in range(self.n_estimators):
            # Calculate the pseudo-residuals
            logger.debug("fit(features=%s,target=%s): model → %s", features, target, model)
            logger.debug("fit(self=%s,features=%s,target=%s): model → %s", self, features, target, model)
            residuals = -self.gradient(target, self.predict(features))
            logger.debug("fit(self=%s,features=%s,target=%s): residuals → %s", self, features, target, residuals)
            logger.debug("fit(features=%s,target=%s): residuals → %s", features, target, residuals)
            # Fit a weak learner (e.g., decision tree) to the residuals
            model = DecisionTreeRegressor(max_depth=1)
            model.fit(features, residuals)
            # Update the model by adding the weak learner with a learning rate
            self.models.append((model, self.learning_rate))
            logger.debug("<<< Exiting fit(features=%s,target=%s)", features, target)

    def predict(self, features: np.ndarray) -> np.ndarray:
        """
        Make predictions on input data.

        Parameters:
        - features (np.ndarray): The input data for making predictions.

        Returns:
        - np.ndarray: An array of binary predictions (-1 or 1).

        >>> import numpy as np
        >>> from sklearn.datasets import load_iris
        >>> clf = GradientBoostingClassifier(n_estimators=100, learning_rate=0.1)
        >>> iris = load_iris()
        >>> X, y = iris.data, iris.target
        >>> clf.fit(X, y)
        >>> y_pred = clf.predict(X)
        >>> # Check if the predictions have the correct shape
        >>> y_pred.shape == y.shape
        True
        """
        logger.debug(">>> Entering predict(features=%s)", features)
        logger.debug("predict(features=%s): predictions → %s", features, predictions)
        logger.debug("predict(self=%s,features=%s): predictions → %s", self, features, predictions)
        # Initialize predictions with zeros
        predictions = np.zeros(features.shape[0])
        for model, learning_rate in self.models:
            predictions += learning_rate * model.predict(features)
        logger.debug("<<< Exiting predict(features=%s)", features)
        return np.sign(predictions)  # Convert to binary predictions (-1 or 1)

    def gradient(self, target: np.ndarray, y_pred: np.ndarray) -> np.ndarray:
        """
        Calculate the negative gradient (pseudo-residuals) for logistic loss.

        Parameters:
        - target (np.ndarray): The target values.
        - y_pred (np.ndarray): The predicted values.

        Returns:
        - np.ndarray: An array of pseudo-residuals.

        >>> import numpy as np
        >>> clf = GradientBoostingClassifier(n_estimators=100, learning_rate=0.1)
        >>> target = np.array([0, 1, 0, 1])
        >>> y_pred = np.array([0.2, 0.8, 0.3, 0.7])
        >>> residuals = clf.gradient(target, y_pred)
        >>> # Check if residuals have the correct shape
        >>> residuals.shape == target.shape
        True
        """
        logger.debug(">>> Entering gradient(target=%s,y_pred=%s)", target, y_pred)
        logger.debug("<<< Exiting gradient(target=%s,y_pred=%s)", target, y_pred)
        return -target / (1 + np.exp(target * y_pred))


if __name__ == "__main__":
    iris = load_iris()
    X, y = iris.data, iris.target
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    clf = GradientBoostingClassifier(n_estimators=100, learning_rate=0.1)
    clf.fit(X_train, y_train)

    y_pred = clf.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {accuracy:.2f}")
