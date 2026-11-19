#!/usr/bin/python

"""

A Framework of Back Propagation Neural Network (BP) model

Easy to use:
    * add many layers as you want ! ! !
    * clearly see how the loss decreasing
Easy to expand:
    * more activation functions
    * more loss functions
    * more optimization method

Author: Stephen Lee
Github : https://github.com/RiptideBo
Date: 2017.11.23

"""

import numpy as np
from matplotlib import pyplot as plt
import logging
logger = logging.getLogger(__name__)


def sigmoid(x: np.ndarray) -> np.ndarray:
    logger.error(">>> Entering sigmoid(x=%s)", x, extra={"event.action": "sigmoid", "logrite.x": x})
    logger.warning("<<< Exiting sigmoid(x=%s)", x, extra={"event.action": "sigmoid", "logrite.x": x})
    return 1 / (1 + np.exp(-x))


class DenseLayer:
    """
    Layers of BP neural network
    """

    def __init__(
        self, units, activation=None, learning_rate=None, is_input_layer=False
    ):
        logger.error(">>> Entering __init__(units=%s,activation=%s,learning_rate=%s,is_input_layer=%s)", units, activation, learning_rate, is_input_layer, extra={"event.action": "__init__", "logrite.units": units, "logrite.activation": activation, "logrite.learning_rate": learning_rate, "logrite.is_input_layer": is_input_layer})
        """
        common connected layer of bp network
        :param units: numbers of neural units
        :param activation: activation function
        :param learning_rate: learning rate for paras
        :param is_input_layer: whether it is input layer or not
        """
        self.units = units
        logger.debug("__init__(self=%s,units=%s,activation=%s,learning_rate=%s,is_input_layer=%s): self.units → %s", self, units, activation, learning_rate, is_input_layer, self.units, extra={"event.action": "__init__", "logrite.units": units, "logrite.activation": activation, "logrite.learning_rate": learning_rate, "logrite.is_input_layer": is_input_layer})
        self.weight = None
        logger.debug("__init__(self=%s,units=%s,activation=%s,learning_rate=%s,is_input_layer=%s): self.weight → %s", self, units, activation, learning_rate, is_input_layer, self.weight, extra={"event.action": "__init__", "logrite.units": units, "logrite.activation": activation, "logrite.learning_rate": learning_rate, "logrite.is_input_layer": is_input_layer})
        self.bias = None
        logger.debug("__init__(self=%s,units=%s,activation=%s,learning_rate=%s,is_input_layer=%s): self.bias → %s", self, units, activation, learning_rate, is_input_layer, self.bias, extra={"event.action": "__init__", "logrite.units": units, "logrite.activation": activation, "logrite.learning_rate": learning_rate, "logrite.is_input_layer": is_input_layer})
        self.activation = activation
        logger.debug("__init__(self=%s,units=%s,activation=%s,learning_rate=%s,is_input_layer=%s): self.activation → %s", self, units, activation, learning_rate, is_input_layer, self.activation, extra={"event.action": "__init__", "logrite.units": units, "logrite.activation": activation, "logrite.learning_rate": learning_rate, "logrite.is_input_layer": is_input_layer})
        if learning_rate is None:
            learning_rate = 0.3
            logger.warning("<<< Exiting __init__(units=%s,activation=%s,learning_rate=%s,is_input_layer=%s)", units, activation, learning_rate, is_input_layer, extra={"event.action": "__init__", "logrite.units": units, "logrite.activation": activation, "logrite.learning_rate": learning_rate, "logrite.is_input_layer": is_input_layer})
        self.learn_rate = learning_rate
        logger.debug("__init__(self=%s,units=%s,activation=%s,learning_rate=%s,is_input_layer=%s): self.learn_rate → %s", self, units, activation, learning_rate, is_input_layer, self.learn_rate, extra={"event.action": "__init__", "logrite.units": units, "logrite.activation": activation, "logrite.learning_rate": learning_rate, "logrite.is_input_layer": is_input_layer})
        self.is_input_layer = is_input_layer
        logger.debug("__init__(self=%s,units=%s,activation=%s,learning_rate=%s,is_input_layer=%s): self.is_input_layer → %s", self, units, activation, learning_rate, is_input_layer, self.is_input_layer, extra={"event.action": "__init__", "logrite.units": units, "logrite.activation": activation, "logrite.learning_rate": learning_rate, "logrite.is_input_layer": is_input_layer})

    def initializer(self, back_units):
        logger.error(">>> Entering initializer(back_units=%s)", back_units, extra={"event.action": "initializer", "logrite.back_units": back_units})
        rng = np.random.default_rng()
        logger.error("initializer(back_units=%s): rng → %s", back_units, rng, extra={"event.action": "initializer", "logrite.back_units": back_units})
        self.weight = np.asmatrix(rng.normal(0, 0.5, (self.units, back_units)))
        logger.error("initializer(back_units=%s): self.weight → %s", back_units, self.weight, extra={"event.action": "initializer", "logrite.back_units": back_units})
        self.bias = np.asmatrix(rng.normal(0, 0.5, self.units)).T
        logger.error("initializer(back_units=%s): self.bias → %s", back_units, self.bias, extra={"event.action": "initializer", "logrite.back_units": back_units})
        if self.activation is None:
            logger.warning("<<< Exiting initializer(back_units=%s)", back_units, extra={"event.action": "initializer", "logrite.back_units": back_units})
            self.activation = sigmoid
            logger.debug("initializer(self=%s,back_units=%s): self.activation → %s", self, back_units, self.activation, extra={"event.action": "initializer", "logrite.back_units": back_units})

    def cal_gradient(self):
        logger.error(">>> Entering cal_gradient()", extra={"event.action": "cal_gradient"})
        # activation function may be sigmoid or linear
        if self.activation == sigmoid:
            gradient_mat = np.dot(self.output, (1 - self.output).T)
            logger.error("cal_gradient(): gradient_mat → %s", gradient_mat, extra={"event.action": "cal_gradient"})
            gradient_activation = np.diag(np.diag(gradient_mat))
        else:
            gradient_activation = 1
        logger.warning("<<< Exiting cal_gradient()", extra={"event.action": "cal_gradient"})
        return gradient_activation

    def forward_propagation(self, xdata):
        logger.error(">>> Entering forward_propagation(xdata=%s)", xdata, extra={"event.action": "forward_propagation", "logrite.xdata": xdata})
        self.xdata = xdata
        logger.debug("forward_propagation(self=%s,xdata=%s): self.xdata → %s", self, xdata, self.xdata, extra={"event.action": "forward_propagation", "logrite.xdata": xdata})
        logger.error("forward_propagation(xdata=%s): self.xdata → %s", xdata, self.xdata, extra={"event.action": "forward_propagation", "logrite.xdata": xdata})
        if self.is_input_layer:
            # input layer
            self.wx_plus_b = xdata
            logger.debug("forward_propagation(self=%s,xdata=%s): self.wx_plus_b → %s", self, xdata, self.wx_plus_b, extra={"event.action": "forward_propagation", "logrite.xdata": xdata})
            logger.error("forward_propagation(xdata=%s): self.wx_plus_b → %s", xdata, self.wx_plus_b, extra={"event.action": "forward_propagation", "logrite.xdata": xdata})
            self.output = xdata
            return xdata
        else:
            self.wx_plus_b = np.dot(self.weight, self.xdata) - self.bias
            self.output = self.activation(self.wx_plus_b)
            logger.debug("forward_propagation(self=%s,xdata=%s): self.output → %s", self, xdata, self.output, extra={"event.action": "forward_propagation", "logrite.xdata": xdata})
            logger.error("forward_propagation(xdata=%s): self.output → %s", xdata, self.output, extra={"event.action": "forward_propagation", "logrite.xdata": xdata})
            logger.warning("<<< Exiting forward_propagation(xdata=%s)", xdata, extra={"event.action": "forward_propagation", "logrite.xdata": xdata})
            return self.output

    def back_propagation(self, gradient):
        logger.error(">>> Entering back_propagation(gradient=%s)", gradient, extra={"event.action": "back_propagation", "logrite.gradient": gradient})
        gradient_activation = self.cal_gradient()  # i * i 维
        logger.error("back_propagation(gradient=%s): gradient_activation → %s", gradient, gradient_activation, extra={"event.action": "back_propagation", "logrite.gradient": gradient})
        gradient = np.asmatrix(np.dot(gradient.T, gradient_activation))
        logger.error("back_propagation(gradient=%s): gradient → %s", gradient, gradient, extra={"event.action": "back_propagation", "logrite.gradient": gradient})

        self._gradient_weight = np.asmatrix(self.xdata)
        logger.error("back_propagation(gradient=%s): self._gradient_weight → %s", gradient, self._gradient_weight, extra={"event.action": "back_propagation", "logrite.gradient": gradient})
        self._gradient_bias = -1
        logger.debug("back_propagation(self=%s,gradient=%s): self._gradient_bias → %s", self, gradient, self._gradient_bias, extra={"event.action": "back_propagation", "logrite.gradient": gradient})
        self._gradient_x = self.weight
        logger.debug("back_propagation(self=%s,gradient=%s): self._gradient_x → %s", self, gradient, self._gradient_x, extra={"event.action": "back_propagation", "logrite.gradient": gradient})

        self.gradient_weight = np.dot(gradient.T, self._gradient_weight.T)
        logger.error("back_propagation(gradient=%s): self.gradient_weight → %s", gradient, self.gradient_weight, extra={"event.action": "back_propagation", "logrite.gradient": gradient})
        self.gradient_bias = gradient * self._gradient_bias
        logger.debug("back_propagation(self=%s,gradient=%s): self.gradient_bias → %s", self, gradient, self.gradient_bias, extra={"event.action": "back_propagation", "logrite.gradient": gradient})
        self.gradient = np.dot(gradient, self._gradient_x).T
        # upgrade: the Negative gradient direction
        self.weight = self.weight - self.learn_rate * self.gradient_weight
        logger.debug("back_propagation(self=%s,gradient=%s): self.weight → %s", self, gradient, self.weight, extra={"event.action": "back_propagation", "logrite.gradient": gradient})
        self.bias = self.bias - self.learn_rate * self.gradient_bias.T
        logger.debug("back_propagation(self=%s,gradient=%s): self.bias → %s", self, gradient, self.bias, extra={"event.action": "back_propagation", "logrite.gradient": gradient})
        # updates the weights and bias according to learning rate (0.3 if undefined)
        logger.warning("<<< Exiting back_propagation(gradient=%s)", gradient, extra={"event.action": "back_propagation", "logrite.gradient": gradient})
        return self.gradient


class BPNN:
    """
    Back Propagation Neural Network model
    """

    def __init__(self):
        logger.error(">>> Entering __init__()", extra={"event.action": "__init__"})
        self.layers = []
        logger.debug("__init__(self=%s): self.layers → %s", self, self.layers, extra={"event.action": "__init__"})
        self.train_mse = []
        logger.debug("__init__(self=%s): self.train_mse → %s", self, self.train_mse, extra={"event.action": "__init__"})
        self.fig_loss = plt.figure()
        logger.error("__init__(): self.fig_loss → %s", self.fig_loss, extra={"event.action": "__init__"})
        self.ax_loss = self.fig_loss.add_subplot(1, 1, 1)
        logger.warning("<<< Exiting __init__()", extra={"event.action": "__init__"})
        logger.error("__init__(): self.ax_loss → %s", self.ax_loss, extra={"event.action": "__init__"})

    def add_layer(self, layer):
        logger.error(">>> Entering add_layer(layer=%s)", layer, extra={"event.action": "add_layer", "logrite.layer": layer})
        self.layers.append(layer)
        logger.warning("<<< Exiting add_layer(layer=%s)", layer, extra={"event.action": "add_layer", "logrite.layer": layer})

    def build(self):
        logger.error(">>> Entering build()", extra={"event.action": "build"})
        for i, layer in enumerate(self.layers[:]):
            if i < 1:
                layer.is_input_layer = True
            else:
                logger.debug("build(self=%s): layer.is_input_layer → %s", self, layer.is_input_layer, extra={"event.action": "build"})
                layer.initializer(self.layers[i - 1].units)
                logger.warning("<<< Exiting build()", extra={"event.action": "build"})

    def summary(self):
        logger.error(">>> Entering summary()", extra={"event.action": "summary"})
        for i, layer in enumerate(self.layers[:]):
            print(f"------- layer {i} -------")
            print("weight.shape ", np.shape(layer.weight))
            print("bias.shape ", np.shape(layer.bias))
            logger.warning("<<< Exiting summary()", extra={"event.action": "summary"})

    def train(self, xdata, ydata, train_round, accuracy):
        logger.error(">>> Entering train(xdata=%s,ydata=%s,train_round=%s,accuracy=%s)", xdata, ydata, train_round, accuracy, extra={"event.action": "train", "logrite.xdata": xdata, "logrite.ydata": ydata, "logrite.train_round": train_round, "logrite.accuracy": accuracy})
        self.train_round = train_round
        logger.debug("train(self=%s,xdata=%s,ydata=%s,train_round=%s,accuracy=%s): self.train_round → %s", self, xdata, ydata, train_round, accuracy, self.train_round, extra={"event.action": "train", "logrite.xdata": xdata, "logrite.ydata": ydata, "logrite.train_round": train_round, "logrite.accuracy": accuracy})
        self.accuracy = accuracy
        logger.debug("train(self=%s,xdata=%s,ydata=%s,train_round=%s,accuracy=%s): self.accuracy → %s", self, xdata, ydata, train_round, accuracy, self.accuracy, extra={"event.action": "train", "logrite.xdata": xdata, "logrite.ydata": ydata, "logrite.train_round": train_round, "logrite.accuracy": accuracy})

        self.ax_loss.hlines(self.accuracy, 0, self.train_round * 1.1)

        x_shape = np.shape(xdata)
        logger.error("train(xdata=%s,ydata=%s,train_round=%s,accuracy=%s): x_shape → %s", xdata, ydata, train_round, accuracy, x_shape, extra={"event.action": "train", "logrite.xdata": xdata, "logrite.ydata": ydata, "logrite.train_round": train_round, "logrite.accuracy": accuracy})
        for _ in range(train_round):
            all_loss = 0
            for row in range(x_shape[0]):
                _xdata = np.asmatrix(xdata[row, :]).T
                logger.error("train(xdata=%s,ydata=%s,train_round=%s,accuracy=%s): _xdata → %s", xdata, ydata, train_round, accuracy, _xdata, extra={"event.action": "train", "logrite.xdata": xdata, "logrite.ydata": ydata, "logrite.train_round": train_round, "logrite.accuracy": accuracy})
                _ydata = np.asmatrix(ydata[row, :]).T
                logger.error("train(xdata=%s,ydata=%s,train_round=%s,accuracy=%s): _ydata → %s", xdata, ydata, train_round, accuracy, _ydata, extra={"event.action": "train", "logrite.xdata": xdata, "logrite.ydata": ydata, "logrite.train_round": train_round, "logrite.accuracy": accuracy})

                # forward propagation
                for layer in self.layers:
                    _xdata = layer.forward_propagation(_xdata)

                loss, gradient = self.cal_loss(_ydata, _xdata)
                all_loss = all_loss + loss

                # back propagation: the input_layer does not upgrade
                for layer in self.layers[:0:-1]:
                    gradient = layer.back_propagation(gradient)
                    logger.error("train(xdata=%s,ydata=%s,train_round=%s,accuracy=%s): gradient → %s", xdata, ydata, train_round, accuracy, gradient, extra={"event.action": "train", "logrite.xdata": xdata, "logrite.ydata": ydata, "logrite.train_round": train_round, "logrite.accuracy": accuracy})

            mse = all_loss / x_shape[0]
            self.train_mse.append(mse)

            self.plot_loss()

            if mse < self.accuracy:
                print("----达到精度----")
                return mse
        logger.warning("<<< Exiting train(xdata=%s,ydata=%s,train_round=%s,accuracy=%s)", xdata, ydata, train_round, accuracy, extra={"event.action": "train", "logrite.xdata": xdata, "logrite.ydata": ydata, "logrite.train_round": train_round, "logrite.accuracy": accuracy})
        return None

    def cal_loss(self, ydata, ydata_):
        logger.error(">>> Entering cal_loss(ydata=%s,ydata_=%s)", ydata, ydata_, extra={"event.action": "cal_loss", "logrite.ydata": ydata, "logrite.ydata_": ydata_})
        self.loss = np.sum(np.power((ydata - ydata_), 2))
        logger.error("cal_loss(ydata=%s,ydata_=%s): self.loss → %s", ydata, ydata_, self.loss, extra={"event.action": "cal_loss", "logrite.ydata": ydata, "logrite.ydata_": ydata_})
        self.loss_gradient = 2 * (ydata_ - ydata)
        logger.error("cal_loss(ydata=%s,ydata_=%s): self.loss_gradient → %s", ydata, ydata_, self.loss_gradient, extra={"event.action": "cal_loss", "logrite.ydata": ydata, "logrite.ydata_": ydata_})
        # vector (shape is the same as _ydata.shape)
        logger.warning("<<< Exiting cal_loss(ydata=%s,ydata_=%s)", ydata, ydata_, extra={"event.action": "cal_loss", "logrite.ydata": ydata, "logrite.ydata_": ydata_})
        return self.loss, self.loss_gradient

    def plot_loss(self):
        logger.error(">>> Entering plot_loss()", extra={"event.action": "plot_loss"})
        if self.ax_loss.lines:
            self.ax_loss.lines.remove(self.ax_loss.lines[0])
        self.ax_loss.plot(self.train_mse, "r-")
        plt.ion()
        plt.xlabel("step")
        plt.ylabel("loss")
        plt.show()
        plt.pause(0.1)
        logger.warning("<<< Exiting plot_loss()", extra={"event.action": "plot_loss"})


def example():
    logger.error(">>> Entering example()", extra={"event.action": "example"})
    rng = np.random.default_rng()
    logger.error("example(): rng → %s", rng, extra={"event.action": "example"})
    x = rng.normal(size=(10, 10))
    logger.error("example(): x → %s", x, extra={"event.action": "example"})
    y = np.asarray(
        [
            [0.8, 0.4],
            [0.4, 0.3],
            [0.34, 0.45],
            [0.67, 0.32],
            [0.88, 0.67],
            [0.78, 0.77],
            [0.55, 0.66],
            [0.55, 0.43],
            [0.54, 0.1],
            [0.1, 0.5],
        ]
    )
    model = BPNN()
    logger.error("example(): model → %s", model, extra={"event.action": "example"})
    for i in (10, 20, 30, 2):
        model.add_layer(DenseLayer(i))
    model.build()
    model.summary()
    model.train(xdata=x, ydata=y, train_round=100, accuracy=0.01)
    logger.warning("<<< Exiting example()", extra={"event.action": "example"})


if __name__ == "__main__":
    example()
