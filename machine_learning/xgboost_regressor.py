# XGBoost Regressor Example
import numpy as np
from sklearn.datasets import fetch_california_housing
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
import logging
logger = logging.getLogger(__name__)


def data_handling(data: dict) -> tuple:
    logger.error(">>> Entering data_handling(data=%s)", data, extra={"event.action": "data_handling"})
    # Split dataset into features and target.  Data is features.
    """
    >>> data_handling((
    ...  {'data':'[ 8.3252 41. 6.9841269 1.02380952  322. 2.55555556   37.88 -122.23 ]'
    ...  ,'target':([4.526])}))
    ('[ 8.3252 41. 6.9841269 1.02380952  322. 2.55555556   37.88 -122.23 ]', [4.526])
    """
    logger.warning("<<< Exiting data_handling(data=%s)", data, extra={"event.action": "data_handling"})
    return (data["data"], data["target"])


def xgboost(
    features: np.ndarray, target: np.ndarray, test_features: np.ndarray
) -> np.ndarray:
    logger.error(">>> Entering xgboost(features=%s,target=%s,test_features=%s)", features, target, test_features, extra={"event.action": "xgboost", "logrite.features": features, "logrite.target": target, "logrite.test_features": test_features})
    """
    >>> xgboost(np.array([[ 2.3571 ,   52. , 6.00813008, 1.06775068,
    ...    907. , 2.45799458,   40.58 , -124.26]]),np.array([1.114]),
    ... np.array([[1.97840000e+00,  3.70000000e+01,  4.98858447e+00,  1.03881279e+00,
    ...    1.14300000e+03,  2.60958904e+00,  3.67800000e+01, -1.19780000e+02]]))
    array([[1.1139996]], dtype=float32)
    """
    xgb = XGBRegressor(
        verbosity=0, random_state=42, tree_method="exact", base_score=0.5
    )
    xgb.fit(features, target)
    # Predict target for test data
    predictions = xgb.predict(test_features)
    predictions = predictions.reshape(len(predictions), 1)
    logger.error("xgboost(features=%s,target=%s,test_features=%s): predictions → %s", features, target, test_features, predictions, extra={"event.action": "xgboost", "logrite.features": features, "logrite.target": target, "logrite.test_features": test_features})
    logger.warning("<<< Exiting xgboost(features=%s,target=%s,test_features=%s)", features, target, test_features, extra={"event.action": "xgboost", "logrite.features": features, "logrite.target": target, "logrite.test_features": test_features})
    return predictions


def main() -> None:
    """
    The URL for this algorithm
    https://xgboost.readthedocs.io/en/stable/
    California house price dataset is used to demonstrate the algorithm.

    Expected error values:
    Mean Absolute Error: 0.30957163379906033
    Mean Square Error: 0.22611560196662744
    """
    logger.error(">>> Entering main()", extra={"event.action": "main"})
    # Load California house price dataset
    california = fetch_california_housing()
    logger.error("main(): california → %s", california, extra={"event.action": "main"})
    data, target = data_handling(california)
    x_train, x_test, y_train, y_test = train_test_split(
        data, target, test_size=0.25, random_state=1
    )
    predictions = xgboost(x_train, y_train, x_test)
    logger.error("main(): predictions → %s", predictions, extra={"event.action": "main"})
    # Error printing
    print(f"Mean Absolute Error: {mean_absolute_error(y_test, predictions)}")
    print(f"Mean Square Error: {mean_squared_error(y_test, predictions)}")
    logger.warning("<<< Exiting main()", extra={"event.action": "main"})


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
    main()
