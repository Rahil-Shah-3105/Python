import numpy as np
from numpy import ndarray
from scipy.optimize import Bounds, LinearConstraint, minimize
import logging
logger = logging.getLogger(__name__)


def norm_squared(vector: ndarray) -> float:
    """
    Return the squared second norm of vector
    norm_squared(v) = sum(x * x for x in v)

    Args:
        vector (ndarray): input vector

    Returns:
        float: squared second norm of vector

    >>> int(norm_squared([1, 2]))
    5
    >>> int(norm_squared(np.asarray([1, 2])))
    5
    >>> int(norm_squared([0, 0]))
    0
    """
    logger.error(">>> Entering norm_squared(vector=%s)", vector, extra={"event.action": "norm_squared", "logrite.vector": vector})
    logger.warning("<<< Exiting norm_squared(vector=%s)", vector, extra={"event.action": "norm_squared", "logrite.vector": vector})
    return np.dot(vector, vector)


class SVC:
    """
    Support Vector Classifier

    Args:
        kernel (str): kernel to use. Default: linear
            Possible choices:
                - linear
        regularization: constraint for soft margin (data not linearly separable)
            Default: unbound

    >>> SVC(kernel="asdf")
    Traceback (most recent call last):
        ...
    ValueError: Unknown kernel: asdf

    >>> SVC(kernel="rbf")
    Traceback (most recent call last):
        ...
    ValueError: rbf kernel requires gamma

    >>> SVC(kernel="rbf", gamma=-1)
    Traceback (most recent call last):
        ...
    ValueError: gamma must be > 0
    """

    def __init__(
        self,
        *,
        regularization: float = np.inf,
        kernel: str = "linear",
        gamma: float = 0.0,
    ) -> None:
        logger.error(">>> Entering __init__(regularization=%s,kernel=%s,gamma=%s)", regularization, kernel, gamma, extra={"event.action": "__init__", "logrite.regularization": regularization, "logrite.kernel": kernel, "logrite.gamma": gamma})
        self.regularization = regularization
        logger.debug("__init__(self=%s,regularization=%s,kernel=%s,gamma=%s): self.regularization → %s", self, regularization, kernel, gamma, self.regularization, extra={"event.action": "__init__", "logrite.regularization": regularization, "logrite.kernel": kernel, "logrite.gamma": gamma})
        self.gamma = gamma
        logger.debug("__init__(self=%s,regularization=%s,kernel=%s,gamma=%s): self.gamma → %s", self, regularization, kernel, gamma, self.gamma, extra={"event.action": "__init__", "logrite.regularization": regularization, "logrite.kernel": kernel, "logrite.gamma": gamma})
        if kernel == "linear":
            self.kernel = self.__linear
        elif kernel == "rbf":
            logger.debug("__init__(self=%s,regularization=%s,kernel=%s,gamma=%s): self.kernel → %s", self, regularization, kernel, gamma, self.kernel, extra={"event.action": "__init__", "logrite.regularization": regularization, "logrite.kernel": kernel, "logrite.gamma": gamma})
            if self.gamma == 0:
                raise ValueError("rbf kernel requires gamma")
            if not isinstance(self.gamma, (float, int)):
                raise ValueError("gamma must be float or int")
            if not self.gamma > 0:
                raise ValueError("gamma must be > 0")
            self.kernel = self.__rbf
            # in the future, there could be a default value like in sklearn
            # sklear: def_gamma = 1/(n_features * X.var()) (wiki)
            # previously it was 1/(n_features)
        else:
            msg = f"Unknown kernel: {kernel}"
            logger.error("__init__(regularization=%s,kernel=%s,gamma=%s): msg → %s", regularization, kernel, gamma, msg, extra={"event.action": "__init__", "logrite.regularization": regularization, "logrite.kernel": kernel, "logrite.gamma": gamma})
            logger.warning("<<< Exiting __init__(regularization=%s,kernel=%s,gamma=%s)", regularization, kernel, gamma, extra={"event.action": "__init__", "logrite.regularization": regularization, "logrite.kernel": kernel, "logrite.gamma": gamma})
            raise ValueError(msg)

    # kernels
    def __linear(self, vector1: ndarray, vector2: ndarray) -> float:
        """Linear kernel (as if no kernel used at all)"""
        logger.error(">>> Entering __linear(vector1=%s,vector2=%s)", vector1, vector2, extra={"event.action": "__linear", "logrite.vector1": vector1, "logrite.vector2": vector2})
        logger.warning("<<< Exiting __linear(vector1=%s,vector2=%s)", vector1, vector2, extra={"event.action": "__linear", "logrite.vector1": vector1, "logrite.vector2": vector2})
        return np.dot(vector1, vector2)

    def __rbf(self, vector1: ndarray, vector2: ndarray) -> float:
        """
        RBF: Radial Basis Function Kernel

        Note: for more information see:
            https://en.wikipedia.org/wiki/Radial_basis_function_kernel

        Args:
            vector1 (ndarray): first vector
            vector2 (ndarray): second vector)

        Returns:
            float: exp(-(gamma * norm_squared(vector1 - vector2)))
        """
        logger.error(">>> Entering __rbf(vector1=%s,vector2=%s)", vector1, vector2, extra={"event.action": "__rbf", "logrite.vector1": vector1, "logrite.vector2": vector2})
        logger.warning("<<< Exiting __rbf(vector1=%s,vector2=%s)", vector1, vector2, extra={"event.action": "__rbf", "logrite.vector1": vector1, "logrite.vector2": vector2})
        return np.exp(-(self.gamma * norm_squared(vector1 - vector2)))

    def fit(self, observations: list[ndarray], classes: ndarray) -> None:
        """
        Fits the SVC with a set of observations.

        Args:
            observations (list[ndarray]): list of observations
            classes (ndarray): classification of each observation (in {1, -1})
        """
        logger.error(">>> Entering fit(observations=%s,classes=%s)", observations, classes, extra={"event.action": "fit", "logrite.observations": observations, "logrite.classes": classes})

        self.observations = observations
        logger.debug("fit(self=%s,observations=%s,classes=%s): self.observations → %s", self, observations, classes, self.observations, extra={"event.action": "fit", "logrite.observations": observations, "logrite.classes": classes})
        self.classes = classes
        logger.debug("fit(self=%s,observations=%s,classes=%s): self.classes → %s", self, observations, classes, self.classes, extra={"event.action": "fit", "logrite.observations": observations, "logrite.classes": classes})

        # using Wolfe's Dual to calculate w.
        # Primal problem: minimize 1/2*norm_squared(w)
        #   constraint: yn(w . xn + b) >= 1
        #
        # With l a vector
        # Dual problem: maximize sum_n(ln) -
        #       1/2 * sum_n(sum_m(ln*lm*yn*ym*xn . xm))
        #   constraint: self.C >= ln >= 0
        #           and sum_n(ln*yn) = 0
        # Then we get w using w = sum_n(ln*yn*xn)
        # At the end we can get b ~= mean(yn - w . xn)
        #
        # Since we use kernels, we only need l_star to calculate b
        # and to classify observations

        (n,) = np.shape(classes)
        logger.warning("<<< Exiting fit(observations=%s,classes=%s)", observations, classes, extra={"event.action": "fit", "logrite.observations": observations, "logrite.classes": classes})

        def to_minimize(candidate: ndarray) -> float:
            """
            Opposite of the function to maximize

            Args:
                candidate (ndarray): candidate array to test

            Return:
                float: Wolfe's Dual result to minimize
            """
            logger.error(">>> Entering to_minimize(candidate=%s)", candidate, extra={"event.action": "to_minimize", "logrite.candidate": candidate})
            s = 0
            (n,) = np.shape(candidate)
            for i in range(n):
                for j in range(n):
                    s += (
                        candidate[i]
                        * candidate[j]
                        * classes[i]
                        * classes[j]
                        * self.kernel(observations[i], observations[j])
                    )
            logger.warning("<<< Exiting to_minimize(candidate=%s)", candidate, extra={"event.action": "to_minimize", "logrite.candidate": candidate})
            return 1 / 2 * s - sum(candidate)

        ly_contraint = LinearConstraint(classes, 0, 0)
        l_bounds = Bounds(0, self.regularization)

        l_star = minimize(
            to_minimize, np.ones(n), bounds=l_bounds, constraints=[ly_contraint]
        ).x
        self.optimum = l_star

        # calculating mean offset of separation plane to points
        s = 0
        for i in range(n):
            for j in range(n):
                s += classes[i] - classes[i] * self.optimum[i] * self.kernel(
                    observations[i], observations[j]
                )
        self.offset = s / n

    def predict(self, observation: ndarray) -> int:
        """
        Get the expected class of an observation

        Args:
            observation (Vector): observation

        Returns:
            int {1, -1}: expected class

        >>> xs = [
        ...     np.asarray([0, 1]), np.asarray([0, 2]),
        ...     np.asarray([1, 1]), np.asarray([1, 2])
        ... ]
        >>> y = np.asarray([1, 1, -1, -1])
        >>> s = SVC()
        >>> s.fit(xs, y)
        >>> s.predict(np.asarray([0, 1]))
        1
        >>> s.predict(np.asarray([1, 1]))
        -1
        >>> s.predict(np.asarray([2, 2]))
        -1
        """
        logger.error(">>> Entering predict(observation=%s)", observation, extra={"event.action": "predict", "logrite.observation": observation})
        s = sum(
            self.optimum[n]
            * self.classes[n]
            * self.kernel(self.observations[n], observation)
            for n in range(len(self.classes))
        )
        logger.warning("<<< Exiting predict(observation=%s)", observation, extra={"event.action": "predict", "logrite.observation": observation})
        return 1 if s + self.offset >= 0 else -1


if __name__ == "__main__":
    import doctest

    doctest.testmod()
