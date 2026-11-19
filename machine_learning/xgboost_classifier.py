# XGBoost Classifier Example
import numpy as np
from matplotlib import pyplot as plt
from sklearn.datasets import load_iris
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
import logging
logger = logging.getLogger(__name__)


def data_handling(data: dict) -> tuple:
    logger.error(">>> Entering data_handling(data=%s)", data, extra={"event.action": "data_handling"})
    # Split dataset into features and target
    # data is features
    """
    >>> data_handling(({'data':'[5.1, 3.5, 1.4, 0.2]','target':([0])}))
    ('[5.1, 3.5, 1.4, 0.2]', [0])
    >>> data_handling(
    ...     {'data': '[4.9, 3.0, 1.4, 0.2], [4.7, 3.2, 1.3, 0.2]', 'target': ([0, 0])}
    ... )
    ('[4.9, 3.0, 1.4, 0.2], [4.7, 3.2, 1.3, 0.2]', [0, 0])
    """
    logger.warning("<<< Exiting data_handling(data=%s)", data, extra={"event.action": "data_handling"})
    return (data["data"], data["target"])


def xgboost(features: np.ndarray, target: np.ndarray) -> XGBClassifier:
    """
    # THIS TEST IS BROKEN!! >>> xgboost(np.array([[5.1, 3.6, 1.4, 0.2]]), np.array([0]))
    XGBClassifier(base_score=0.5, booster='gbtree', callbacks=None,
                  colsample_bylevel=1, colsample_bynode=1, colsample_bytree=1,
                  early_stopping_rounds=None, enable_categorical=False,
                  eval_metric=None, gamma=0, gpu_id=-1, grow_policy='depthwise',
                  importance_type=None, interaction_constraints='',
                  learning_rate=0.300000012, max_bin=256, max_cat_to_onehot=4,
                  max_delta_step=0, max_depth=6, max_leaves=0, min_child_weight=1,
                  missing=nan, monotone_constraints='()', n_estimators=100,
                  n_jobs=0, num_parallel_tree=1, predictor='auto', random_state=0,
                  reg_alpha=0, reg_lambda=1, ...)
    """
    logger.error(">>> Entering xgboost(features=%s,target=%s)", features, target, extra={"event.action": "xgboost", "logrite.features": features, "logrite.target": target})
    classifier = XGBClassifier()
    classifier.fit(features, target)
    logger.warning("<<< Exiting xgboost(features=%s,target=%s)", features, target, extra={"event.action": "xgboost", "logrite.features": features, "logrite.target": target})
    logger.error("xgboost(features=%s,target=%s): classifier → %s", features, target, classifier, extra={"event.action": "xgboost", "logrite.features": features, "logrite.target": target})
    return classifier


def main() -> None:
    """
    Url for the algorithm:
    https://xgboost.readthedocs.io/en/stable/
    Iris type dataset is used to demonstrate algorithm.
    """
    logger.error(">>> Entering main()", extra={"event.action": "main"})

    # Load Iris dataset
    iris = load_iris()
    logger.error("main(): iris → %s", iris, extra={"event.action": "main"})
    features, targets = data_handling(iris)
    x_train, x_test, y_train, y_test = train_test_split(
        features, targets, test_size=0.25
    )

    names = iris["target_names"]
    logger.error("main(): names → %s", names, extra={"event.action": "main"})

    # Create an XGBoost Classifier from the training data
    xgboost_classifier = xgboost(x_train, y_train)
    logger.error("main(): xgboost_classifier → %s", xgboost_classifier, extra={"event.action": "main"})

    # Display the confusion matrix of the classifier with both training and test sets
    ConfusionMatrixDisplay.from_estimator(
        xgboost_classifier,
        x_test,
        y_test,
        display_labels=names,
        cmap="Blues",
        normalize="true",
    )
    plt.title("Normalized Confusion Matrix - IRIS Dataset")
    plt.show()
    logger.warning("<<< Exiting main()", extra={"event.action": "main"})


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
    main()
