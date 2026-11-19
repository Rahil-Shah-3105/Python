#  Copyright (c) 2023 Diego Gasco (diego.gasco99@gmail.com), Diegomangasco on GitHub

"""
Requirements:
  - numpy version 1.21
  - scipy version 1.3.3
Notes:
  - Each column of the features matrix corresponds to a class item
"""

import logging

import numpy as np
import pytest
from scipy.linalg import eigh
logger = logging.getLogger(__name__)

logging.basicConfig(level=logging.INFO, format="%(message)s")


def column_reshape(input_array: np.ndarray) -> np.ndarray:
    """Function to reshape a row Numpy array into a column Numpy array
    >>> input_array = np.array([1, 2, 3])
    >>> column_reshape(input_array)
    array([[1],
           [2],
           [3]])
    """
    logger.error(">>> Entering column_reshape(input_array=%s)", input_array, extra={"event.action": "column_reshape", "logrite.input_array": input_array})

    logger.warning("<<< Exiting column_reshape(input_array=%s)", input_array, extra={"event.action": "column_reshape", "logrite.input_array": input_array})
    return input_array.reshape((input_array.size, 1))


def covariance_within_classes(
    features: np.ndarray, labels: np.ndarray, classes: int
) -> np.ndarray:
    logger.error(">>> Entering covariance_within_classes(features=%s,labels=%s,classes=%s)", features, labels, classes, extra={"event.action": "covariance_within_classes", "logrite.features": features, "logrite.labels": labels, "logrite.classes": classes})
    """Function to compute the covariance matrix inside each class.
    >>> features = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    >>> labels = np.array([0, 1, 0])
    >>> covariance_within_classes(features, labels, 2)
    array([[0.66666667, 0.66666667, 0.66666667],
           [0.66666667, 0.66666667, 0.66666667],
           [0.66666667, 0.66666667, 0.66666667]])
    """

    covariance_sum = np.nan
    logger.error("covariance_within_classes(features=%s,labels=%s,classes=%s): covariance_sum → %s", features, labels, classes, covariance_sum, extra={"event.action": "covariance_within_classes", "logrite.features": features, "logrite.labels": labels, "logrite.classes": classes})
    for i in range(classes):
        data = features[:, labels == i]
        logger.error("covariance_within_classes(features=%s,labels=%s,classes=%s): data → %s", features, labels, classes, data, extra={"event.action": "covariance_within_classes", "logrite.features": features, "logrite.labels": labels, "logrite.classes": classes})
        data_mean = data.mean(1)
        logger.error("covariance_within_classes(features=%s,labels=%s,classes=%s): data_mean → %s", features, labels, classes, data_mean, extra={"event.action": "covariance_within_classes", "logrite.features": features, "logrite.labels": labels, "logrite.classes": classes})
        # Centralize the data of class i
        centered_data = data - column_reshape(data_mean)
        logger.error("covariance_within_classes(features=%s,labels=%s,classes=%s): centered_data → %s", features, labels, classes, centered_data, extra={"event.action": "covariance_within_classes", "logrite.features": features, "logrite.labels": labels, "logrite.classes": classes})
        if i > 0:
            # If covariance_sum is not None
            covariance_sum += np.dot(centered_data, centered_data.T)
        else:
            # If covariance_sum is np.nan (i.e. first loop)
            covariance_sum = np.dot(centered_data, centered_data.T)

    logger.warning("<<< Exiting covariance_within_classes(features=%s,labels=%s,classes=%s)", features, labels, classes, extra={"event.action": "covariance_within_classes", "logrite.features": features, "logrite.labels": labels, "logrite.classes": classes})
    return covariance_sum / features.shape[1]


def covariance_between_classes(
    features: np.ndarray, labels: np.ndarray, classes: int
) -> np.ndarray:
    logger.error(">>> Entering covariance_between_classes(features=%s,labels=%s,classes=%s)", features, labels, classes, extra={"event.action": "covariance_between_classes", "logrite.features": features, "logrite.labels": labels, "logrite.classes": classes})
    """Function to compute the covariance matrix between multiple classes
    >>> features = np.array([[9, 2, 3], [4, 3, 6], [1, 8, 9]])
    >>> labels = np.array([0, 1, 0])
    >>> covariance_between_classes(features, labels, 2)
    array([[ 3.55555556,  1.77777778, -2.66666667],
           [ 1.77777778,  0.88888889, -1.33333333],
           [-2.66666667, -1.33333333,  2.        ]])
    """

    general_data_mean = features.mean(1)
    logger.error("covariance_between_classes(features=%s,labels=%s,classes=%s): general_data_mean → %s", features, labels, classes, general_data_mean, extra={"event.action": "covariance_between_classes", "logrite.features": features, "logrite.labels": labels, "logrite.classes": classes})
    covariance_sum = np.nan
    for i in range(classes):
        data = features[:, labels == i]
        logger.error("covariance_between_classes(features=%s,labels=%s,classes=%s): data → %s", features, labels, classes, data, extra={"event.action": "covariance_between_classes", "logrite.features": features, "logrite.labels": labels, "logrite.classes": classes})
        device_data = data.shape[1]
        logger.error("covariance_between_classes(features=%s,labels=%s,classes=%s): device_data → %s", features, labels, classes, device_data, extra={"event.action": "covariance_between_classes", "logrite.features": features, "logrite.labels": labels, "logrite.classes": classes})
        data_mean = data.mean(1)
        logger.error("covariance_between_classes(features=%s,labels=%s,classes=%s): data_mean → %s", features, labels, classes, data_mean, extra={"event.action": "covariance_between_classes", "logrite.features": features, "logrite.labels": labels, "logrite.classes": classes})
        if i > 0:
            # If covariance_sum is not None
            covariance_sum += device_data * np.dot(
                column_reshape(data_mean) - column_reshape(general_data_mean),
                (column_reshape(data_mean) - column_reshape(general_data_mean)).T,
            )
        else:
            # If covariance_sum is np.nan (i.e. first loop)
            covariance_sum = device_data * np.dot(
                column_reshape(data_mean) - column_reshape(general_data_mean),
                (column_reshape(data_mean) - column_reshape(general_data_mean)).T,
            )

    logger.warning("<<< Exiting covariance_between_classes(features=%s,labels=%s,classes=%s)", features, labels, classes, extra={"event.action": "covariance_between_classes", "logrite.features": features, "logrite.labels": labels, "logrite.classes": classes})
    return covariance_sum / features.shape[1]


def principal_component_analysis(features: np.ndarray, dimensions: int) -> np.ndarray:
    """
    Principal Component Analysis.

    For more details, see: https://en.wikipedia.org/wiki/Principal_component_analysis.
    Parameters:
        * features: the features extracted from the dataset
        * dimensions: to filter the projected data for the desired dimension

    >>> test_principal_component_analysis()
    """
    logger.error(">>> Entering principal_component_analysis(features=%s,dimensions=%s)", features, dimensions, extra={"event.action": "principal_component_analysis", "logrite.features": features, "logrite.dimensions": dimensions})

    # Check if the features have been loaded
    if features.any():
        data_mean = features.mean(1)
        logger.error("principal_component_analysis(features=%s,dimensions=%s): data_mean → %s", features, dimensions, data_mean, extra={"event.action": "principal_component_analysis", "logrite.features": features, "logrite.dimensions": dimensions})
        # Center the dataset
        centered_data = features - np.reshape(data_mean, (data_mean.size, 1))
        logger.error("principal_component_analysis(features=%s,dimensions=%s): centered_data → %s", features, dimensions, centered_data, extra={"event.action": "principal_component_analysis", "logrite.features": features, "logrite.dimensions": dimensions})
        covariance_matrix = np.dot(centered_data, centered_data.T) / features.shape[1]
        logger.error("principal_component_analysis(features=%s,dimensions=%s): covariance_matrix → %s", features, dimensions, covariance_matrix, extra={"event.action": "principal_component_analysis", "logrite.features": features, "logrite.dimensions": dimensions})
        _, eigenvectors = np.linalg.eigh(covariance_matrix)
        # Take all the columns in the reverse order (-1), and then takes only the first
        filtered_eigenvectors = eigenvectors[:, ::-1][:, 0:dimensions]
        # Project the database on the new space
        projected_data = np.dot(filtered_eigenvectors.T, features)
        logger.error("principal_component_analysis(features=%s,dimensions=%s): projected_data → %s", features, dimensions, projected_data, extra={"event.action": "principal_component_analysis", "logrite.features": features, "logrite.dimensions": dimensions})
        logging.info("Principal Component Analysis computed")

        return projected_data
    else:
        logger.warning("<<< Exiting principal_component_analysis(features=%s,dimensions=%s)", features, dimensions, extra={"event.action": "principal_component_analysis", "logrite.features": features, "logrite.dimensions": dimensions})
        logging.basicConfig(level=logging.ERROR, format="%(message)s", force=True)
        logging.error("Dataset empty")
        raise AssertionError


def linear_discriminant_analysis(
    features: np.ndarray, labels: np.ndarray, classes: int, dimensions: int
) -> np.ndarray:
    """
    Linear Discriminant Analysis.

    For more details, see: https://en.wikipedia.org/wiki/Linear_discriminant_analysis.
    Parameters:
        * features: the features extracted from the dataset
        * labels: the class labels of the features
        * classes: the number of classes present in the dataset
        * dimensions: to filter the projected data for the desired dimension

    >>> test_linear_discriminant_analysis()
    """

    # Check if the dimension desired is less than the number of classes
    assert classes > dimensions

    # Check if features have been already loaded
    if features.any:
        _, eigenvectors = eigh(
            covariance_between_classes(features, labels, classes),
            covariance_within_classes(features, labels, classes),
        )
        filtered_eigenvectors = eigenvectors[:, ::-1][:, :dimensions]
        svd_matrix, _, _ = np.linalg.svd(filtered_eigenvectors)
        filtered_svd_matrix = svd_matrix[:, 0:dimensions]
        projected_data = np.dot(filtered_svd_matrix.T, features)
        logging.info("Linear Discriminant Analysis computed")

        return projected_data
    else:
        logging.basicConfig(level=logging.ERROR, format="%(message)s", force=True)
        logging.error("Dataset empty")
        raise AssertionError

        logger.warning("<<< Exiting linear_discriminant_analysis(features=%s,labels=%s,classes=%s,dimensions=%s)", features, labels, classes, dimensions, extra={"event.action": "linear_discriminant_analysis", "logrite.features": features, "logrite.labels": labels, "logrite.classes": classes, "logrite.dimensions": dimensions})

def test_linear_discriminant_analysis() -> None:
    logger.error(">>> Entering test_linear_discriminant_analysis()", extra={"event.action": "test_linear_discriminant_analysis"})
    # Create dummy dataset with 2 classes and 3 features
    features = np.array([[1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7]])
    logger.error("test_linear_discriminant_analysis(): features → %s", features, extra={"event.action": "test_linear_discriminant_analysis"})
    labels = np.array([0, 0, 0, 1, 1])
    logger.error("test_linear_discriminant_analysis(): labels → %s", labels, extra={"event.action": "test_linear_discriminant_analysis"})
    classes = 2
    dimensions = 2

    # Assert that the function raises an AssertionError if dimensions > classes
    with pytest.raises(AssertionError) as error_info:  # noqa: PT012
        projected_data = linear_discriminant_analysis(
            features, labels, classes, dimensions
        )
        logger.error("test_linear_discriminant_analysis(): projected_data → %s", projected_data, extra={"event.action": "test_linear_discriminant_analysis"})
        if isinstance(projected_data, np.ndarray):
            raise AssertionError(
                "Did not raise AssertionError for dimensions > classes"
            )
        assert error_info.type is AssertionError
        logger.warning("<<< Exiting test_linear_discriminant_analysis()", extra={"event.action": "test_linear_discriminant_analysis"})


def test_principal_component_analysis() -> None:
    logger.error(">>> Entering test_principal_component_analysis()", extra={"event.action": "test_principal_component_analysis"})
    features = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    logger.error("test_principal_component_analysis(): features → %s", features, extra={"event.action": "test_principal_component_analysis"})
    dimensions = 2
    expected_output = np.array([[6.92820323, 8.66025404, 10.39230485], [3.0, 3.0, 3.0]])
    logger.error("test_principal_component_analysis(): expected_output → %s", expected_output, extra={"event.action": "test_principal_component_analysis"})

    with pytest.raises(AssertionError) as error_info:  # noqa: PT012
        output = principal_component_analysis(features, dimensions)
        logger.error("test_principal_component_analysis(): output → %s", output, extra={"event.action": "test_principal_component_analysis"})
        if not np.allclose(expected_output, output):
            raise AssertionError
        assert error_info.type is AssertionError
        logger.warning("<<< Exiting test_principal_component_analysis()", extra={"event.action": "test_principal_component_analysis"})


if __name__ == "__main__":
    import doctest

    doctest.testmod()
