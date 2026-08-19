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
    logger.debug(">>> Entering sigmoid(x=%s)", x)
    logger.debug("<<< Exiting sigmoid(x=%s)", x)
    return 1 / (1 + np.exp(-x))


class DenseLayer:
    """
    Layers of BP neural network
    """

    def __init__(
        self, units, activation=None, learning_rate=None, is_input_layer=False
    ):
        """
        common connected layer of bp network
        :param units: numbers of neural units
        :param activation: activation function
        :param learning_rate: learning rate for paras
        :param is_input_layer: whether it is input layer or not
        """
        self.units = units
        self.weight = None
        self.bias = None
        self.activation = activation
        if learning_rate is None:
            learning_rate = 0.3
        self.learn_rate = learning_rate
        self.is_input_layer = is_input_layer
        logger.debug(">>> Entering __init__()")
        logger.debug("__init__(self=%s): self.layers → %s", self, self.layers)
        logger.debug("__init__(self=%s): self.train_mse → %s", self, self.train_mse)
        logger.debug("__init__(): self.fig_loss → %s", self.fig_loss)
        logger.debug("<<< Exiting __init__()")

    def initializer(self, back_units):
        logger.debug(">>> Entering initializer(back_units=%s)", back_units)
        logger.debug("initializer(self=%s,back_units=%s): self.activation → %s", self, back_units, self.activation)
        rng = np.random.default_rng()
        logger.debug("initializer(back_units=%s): rng → %s", back_units, rng)
        logger.debug("initializer(self=%s,back_units=%s): rng → %s", self, back_units, rng)
        self.weight = np.asmatrix(rng.normal(0, 0.5, (self.units, back_units)))
        logger.debug("initializer(back_units=%s): self.weight → %s", back_units, self.weight)
        self.bias = np.asmatrix(rng.normal(0, 0.5, self.units)).T
        logger.debug("initializer(back_units=%s): self.bias → %s", back_units, self.bias)
        if self.activation is None:
            self.activation = sigmoid
            logger.debug("<<< Exiting initializer(back_units=%s)", back_units)

    def cal_gradient(self):
        logger.debug(">>> Entering cal_gradient()")
        # activation function may be sigmoid or linear
        if self.activation == sigmoid:
            gradient_mat = np.dot(self.output, (1 - self.output).T)
            logger.debug("cal_gradient(self=%s): gradient_mat → %s", self, gradient_mat)
            logger.debug("cal_gradient(): gradient_mat → %s", gradient_mat)
            gradient_activation = np.diag(np.diag(gradient_mat))
            logger.debug("cal_gradient(self=%s): gradient_activation → %s", self, gradient_activation)
        else:
            gradient_activation = 1
        logger.debug("<<< Exiting cal_gradient()")
        return gradient_activation

    def forward_propagation(self, xdata):
        logger.debug(">>> Entering forward_propagation(xdata=%s)", xdata)
        logger.debug("forward_propagation(xdata=%s): self.wx_plus_b → %s", xdata, self.wx_plus_b)
        logger.debug("forward_propagation(self=%s,xdata=%s): self.wx_plus_b → %s", self, xdata, self.wx_plus_b)
        logger.debug("forward_propagation(self=%s,xdata=%s): self.output → %s", self, xdata, self.output)
        logger.debug("forward_propagation(xdata=%s): self.output → %s", xdata, self.output)
        self.xdata = xdata
        logger.debug("forward_propagation(xdata=%s): self.xdata → %s", xdata, self.xdata)
        logger.debug("forward_propagation(self=%s,xdata=%s): self.xdata → %s", self, xdata, self.xdata)
        if self.is_input_layer:
            # input layer
            self.wx_plus_b = xdata
            self.output = xdata
            return xdata
        else:
            self.wx_plus_b = np.dot(self.weight, self.xdata) - self.bias
            self.output = self.activation(self.wx_plus_b)
            logger.debug("<<< Exiting forward_propagation(xdata=%s)", xdata)
            return self.output

    def back_propagation(self, gradient):
        logger.debug(">>> Entering back_propagation(gradient=%s)", gradient)
        gradient_activation = self.cal_gradient()  # i * i 维
        logger.debug("back_propagation(gradient=%s): gradient_activation → %s", gradient, gradient_activation)
        logger.debug("back_propagation(self=%s,gradient=%s): gradient_activation → %s", self, gradient, gradient_activation)
        gradient = np.asmatrix(np.dot(gradient.T, gradient_activation))
        logger.debug("back_propagation(gradient=%s): gradient → %s", gradient, gradient)

        self._gradient_weight = np.asmatrix(self.xdata)
        logger.debug("back_propagation(gradient=%s): self._gradient_weight → %s", gradient, self._gradient_weight)
        self._gradient_bias = -1
        logger.debug("back_propagation(self=%s,gradient=%s): self._gradient_bias → %s", self, gradient, self._gradient_bias)
        self._gradient_x = self.weight
        logger.debug("back_propagation(self=%s,gradient=%s): self._gradient_x → %s", self, gradient, self._gradient_x)

        self.gradient_weight = np.dot(gradient.T, self._gradient_weight.T)
        logger.debug("back_propagation(gradient=%s): self.gradient_weight → %s", gradient, self.gradient_weight)
        self.gradient_bias = gradient * self._gradient_bias
        logger.debug("back_propagation(self=%s,gradient=%s): self.gradient_bias → %s", self, gradient, self.gradient_bias)
        self.gradient = np.dot(gradient, self._gradient_x).T
        # upgrade: the Negative gradient direction
        self.weight = self.weight - self.learn_rate * self.gradient_weight
        logger.debug("back_propagation(self=%s,gradient=%s): self.weight → %s", self, gradient, self.weight)
        self.bias = self.bias - self.learn_rate * self.gradient_bias.T
        logger.debug("back_propagation(self=%s,gradient=%s): self.bias → %s", self, gradient, self.bias)
        # updates the weights and bias according to learning rate (0.3 if undefined)
        logger.debug("<<< Exiting back_propagation(gradient=%s)", gradient)
        return self.gradient


class BPNN:
    """
    Back Propagation Neural Network model
    """

    def __init__(self):
        self.layers = []
        self.train_mse = []
        self.fig_loss = plt.figure()
        self.ax_loss = self.fig_loss.add_subplot(1, 1, 1)
        logger.debug("__init__(): self.ax_loss → %s", self.ax_loss)

    def add_layer(self, layer):
        logger.debug(">>> Entering add_layer(layer=%s)", layer)
        self.layers.append(layer)
        logger.debug("<<< Exiting add_layer(layer=%s)", layer)

    def build(self):
        logger.debug(">>> Entering build()")
        for i, layer in enumerate(self.layers[:]):
            if i < 1:
                layer.is_input_layer = True
                logger.debug("build(self=%s): layer.is_input_layer → %s", self, layer.is_input_layer)
            else:
                layer.initializer(self.layers[i - 1].units)
                logger.debug("<<< Exiting build()")

    def summary(self):
        logger.debug(">>> Entering summary()")
        for i, layer in enumerate(self.layers[:]):
            print(f"------- layer {i} -------")
            print("weight.shape ", np.shape(layer.weight))
            print("bias.shape ", np.shape(layer.bias))
            logger.debug("<<< Exiting summary()")

    def train(self, xdata, ydata, train_round, accuracy):
        logger.debug(">>> Entering train(xdata=%s,ydata=%s,train_round=%s,accuracy=%s)", xdata, ydata, train_round, accuracy)
        self.train_round = train_round
        logger.debug("train(self=%s,xdata=%s,ydata=%s,train_round=%s,accuracy=%s): self.train_round → %s", self, xdata, ydata, train_round, accuracy, self.train_round)
        self.accuracy = accuracy
        logger.debug("train(self=%s,xdata=%s,ydata=%s,train_round=%s,accuracy=%s): self.accuracy → %s", self, xdata, ydata, train_round, accuracy, self.accuracy)

        self.ax_loss.hlines(self.accuracy, 0, self.train_round * 1.1)

        logger.debug("train(xdata=%s,ydata=%s,train_round=%s,accuracy=%s): _ydata → %s", xdata, ydata, train_round, accuracy, _ydata)
        logger.debug("train(self=%s,xdata=%s,ydata=%s,train_round=%s,accuracy=%s): all_loss → %s", self, xdata, ydata, train_round, accuracy, all_loss)
        logger.debug("train(xdata=%s,ydata=%s,train_round=%s,accuracy=%s): _xdata → %s", xdata, ydata, train_round, accuracy, _xdata)
        logger.debug("train(self=%s,xdata=%s,ydata=%s,train_round=%s,accuracy=%s): _xdata → %s", self, xdata, ydata, train_round, accuracy, _xdata)
        logger.debug("train(self=%s,xdata=%s,ydata=%s,train_round=%s,accuracy=%s): _ydata → %s", self, xdata, ydata, train_round, accuracy, _ydata)
        x_shape = np.shape(xdata)
        logger.debug("train(self=%s,xdata=%s,ydata=%s,train_round=%s,accuracy=%s): x_shape → %s", self, xdata, ydata, train_round, accuracy, x_shape)
        logger.debug("train(xdata=%s,ydata=%s,train_round=%s,accuracy=%s): x_shape → %s", xdata, ydata, train_round, accuracy, x_shape)
        for _ in range(train_round):
            all_loss = 0
            for row in range(x_shape[0]):
                _xdata = np.asmatrix(xdata[row, :]).T
                _ydata = np.asmatrix(ydata[row, :]).T

                # forward propagation
                for layer in self.layers:
                    _xdata = layer.forward_propagation(_xdata)

                loss, gradient = self.cal_loss(_ydata, _xdata)
                all_loss = all_loss + loss

                # back propagation: the input_layer does not upgrade
                for layer in self.layers[:0:-1]:
                    gradient = layer.back_propagation(gradient)
                    logger.debug("train(self=%s,xdata=%s,ydata=%s,train_round=%s,accuracy=%s): gradient → %s", self, xdata, ydata, train_round, accuracy, gradient)
                    logger.debug("train(xdata=%s,ydata=%s,train_round=%s,accuracy=%s): gradient → %s", xdata, ydata, train_round, accuracy, gradient)

            mse = all_loss / x_shape[0]
            logger.debug("train(self=%s,xdata=%s,ydata=%s,train_round=%s,accuracy=%s): mse → %s", self, xdata, ydata, train_round, accuracy, mse)
            self.train_mse.append(mse)

            self.plot_loss()

            if mse < self.accuracy:
                print("----达到精度----")
                return mse
        return None

    def cal_loss(self, ydata, ydata_):
        logger.debug(">>> Entering cal_loss(ydata=%s,ydata_=%s)", ydata, ydata_)
        self.loss = np.sum(np.power((ydata - ydata_), 2))
        logger.debug("cal_loss(ydata=%s,ydata_=%s): self.loss → %s", ydata, ydata_, self.loss)
        self.loss_gradient = 2 * (ydata_ - ydata)
        logger.debug("cal_loss(ydata=%s,ydata_=%s): self.loss_gradient → %s", ydata, ydata_, self.loss_gradient)
        # vector (shape is the same as _ydata.shape)
        logger.debug("<<< Exiting cal_loss(ydata=%s,ydata_=%s)", ydata, ydata_)
        return self.loss, self.loss_gradient

    def plot_loss(self):
        logger.debug(">>> Entering plot_loss()")
        if self.ax_loss.lines:
            self.ax_loss.lines.remove(self.ax_loss.lines[0])
        self.ax_loss.plot(self.train_mse, "r-")
        plt.ion()
        plt.xlabel("step")
        plt.ylabel("loss")
        plt.show()
        plt.pause(0.1)
        logger.debug("<<< Exiting plot_loss()")


def example():
    logger.debug(">>> Entering example()")
    rng = np.random.default_rng()
    logger.debug("example(): rng → %s", rng)
    x = rng.normal(size=(10, 10))
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
    logger.debug("example(): x → %s", x)
    model = BPNN()
    logger.debug("example(): model → %s", model)
    for i in (10, 20, 30, 2):
        model.add_layer(DenseLayer(i))
    model.build()
    model.summary()
    model.train(xdata=x, ydata=y, train_round=100, accuracy=0.01)
    logger.debug("<<< Exiting example()")


if __name__ == "__main__":
    example()
