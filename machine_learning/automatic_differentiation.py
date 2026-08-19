"""
Demonstration of the Automatic Differentiation (Reverse mode).

Reference: https://en.wikipedia.org/wiki/Automatic_differentiation

Author: Poojan Smart
Email: smrtpoojan@gmail.com
"""

from __future__ import annotations

from collections import defaultdict
from enum import Enum
from types import TracebackType
from typing import Any

import numpy as np
from typing_extensions import Self  # noqa: UP035
import logging
logger = logging.getLogger(__name__)


class OpType(Enum):
    """
    Class represents list of supported operations on Variable for gradient calculation.
    """

    ADD = 0
    SUB = 1
    MUL = 2
    DIV = 3
    MATMUL = 4
    POWER = 5
    NOOP = 6


class Variable:
    """
    Class represents n-dimensional object which is used to wrap numpy array on which
    operations will be performed and the gradient will be calculated.

    Examples:
    >>> Variable(5.0)
    Variable(5.0)
    >>> Variable([5.0, 2.9])
    Variable([5.  2.9])
    >>> Variable([5.0, 2.9]) + Variable([1.0, 5.5])
    Variable([6.  8.4])
    >>> Variable([[8.0, 10.0]])
    Variable([[ 8. 10.]])
    """

    def __init__(self, value: Any) -> None:
        logger.debug(">>> Entering __init__(value=%s)", value)
        self.value = np.array(value)
        logger.debug("__init__(value=%s): self.value → %s", value, self.value)

        # pointers to the operations to which the Variable is input
        self.param_to: list[Operation] = []
        # pointer to the operation of which the Variable is output of
        self.result_of: Operation = Operation(OpType.NOOP)
        logger.debug("<<< Exiting __init__(value=%s)", value)
        logger.debug(">>> Entering __init__()")
        logger.debug("<<< Exiting __init__()")

    def __repr__(self) -> str:
        logger.debug(">>> Entering __repr__()")
        logger.debug("<<< Exiting __repr__()")
        return f"Variable({self.value})"

    def to_ndarray(self) -> np.ndarray:
        logger.debug(">>> Entering to_ndarray()")
        logger.debug("<<< Exiting to_ndarray()")
        return self.value

    def __add__(self, other: Variable) -> Variable:
        logger.debug(">>> Entering __add__(other=%s)", other)
        result = Variable(self.value + other.value)
        logger.debug("__add__(other=%s): result → %s", other, result)

        with GradientTracker() as tracker:
            logger.error("Exception in __add__(other=%s)", other, exc_info=True)
            # if tracker is enabled, computation graph will be updated
            if tracker.enabled:
                tracker.append(OpType.ADD, params=[self, other], output=result)
        logger.debug("<<< Exiting __add__(other=%s)", other)
        return result

    def __sub__(self, other: Variable) -> Variable:
        logger.debug(">>> Entering __sub__(other=%s)", other)
        result = Variable(self.value - other.value)
        logger.debug("__sub__(other=%s): result → %s", other, result)

        with GradientTracker() as tracker:
            logger.error("Exception in __sub__(other=%s)", other, exc_info=True)
            # if tracker is enabled, computation graph will be updated
            if tracker.enabled:
                tracker.append(OpType.SUB, params=[self, other], output=result)
        logger.debug("<<< Exiting __sub__(other=%s)", other)
        return result

    def __mul__(self, other: Variable) -> Variable:
        logger.debug(">>> Entering __mul__(other=%s)", other)
        result = Variable(self.value * other.value)
        logger.debug("__mul__(other=%s): result → %s", other, result)

        with GradientTracker() as tracker:
            logger.error("Exception in __mul__(other=%s)", other, exc_info=True)
            # if tracker is enabled, computation graph will be updated
            if tracker.enabled:
                tracker.append(OpType.MUL, params=[self, other], output=result)
        logger.debug("<<< Exiting __mul__(other=%s)", other)
        return result

    def __truediv__(self, other: Variable) -> Variable:
        logger.debug(">>> Entering __truediv__(other=%s)", other)
        result = Variable(self.value / other.value)
        logger.debug("__truediv__(other=%s): result → %s", other, result)

        with GradientTracker() as tracker:
            logger.error("Exception in __truediv__(other=%s)", other, exc_info=True)
            # if tracker is enabled, computation graph will be updated
            if tracker.enabled:
                tracker.append(OpType.DIV, params=[self, other], output=result)
        logger.debug("<<< Exiting __truediv__(other=%s)", other)
        return result

    def __matmul__(self, other: Variable) -> Variable:
        logger.debug(">>> Entering __matmul__(other=%s)", other)
        result = Variable(self.value @ other.value)
        logger.debug("__matmul__(other=%s): result → %s", other, result)

        with GradientTracker() as tracker:
            logger.error("Exception in __matmul__(other=%s)", other, exc_info=True)
            # if tracker is enabled, computation graph will be updated
            if tracker.enabled:
                tracker.append(OpType.MATMUL, params=[self, other], output=result)
        logger.debug("<<< Exiting __matmul__(other=%s)", other)
        return result

    def __pow__(self, power: int) -> Variable:
        logger.debug(">>> Entering __pow__(power=%s)", power)
        logger.debug("__pow__(self=%s,power=%s): other_params → %s", self, power, other_params)
        logger.debug("__pow__(self=%s,power=%s): output → %s", self, power, output)
        logger.debug("__pow__(self=%s,power=%s): params → %s", self, power, params)
        result = Variable(self.value**power)
        logger.debug("__pow__(power=%s): result → %s", power, result)

        with GradientTracker() as tracker:
            logger.error("Exception in __pow__(power=%s)", power, exc_info=True)
            # if tracker is enabled, computation graph will be updated
            if tracker.enabled:
                tracker.append(
                    OpType.POWER,
                    params=[self],
                    output=result,
                    other_params={"power": power},
                )
                logger.debug("__pow__(power=%s): other_params → %s", power, other_params)
        logger.debug("<<< Exiting __pow__(power=%s)", power)
        return result

    def add_param_to(self, param_to: Operation) -> None:
        logger.debug(">>> Entering add_param_to(param_to=%s)", param_to)
        self.param_to.append(param_to)
        logger.debug("<<< Exiting add_param_to(param_to=%s)", param_to)

    def add_result_of(self, result_of: Operation) -> None:
        logger.debug(">>> Entering add_result_of(result_of=%s)", result_of)
        self.result_of = result_of
        logger.debug("add_result_of(self=%s,result_of=%s): self.result_of → %s", self, result_of, self.result_of)
        logger.debug("add_result_of(result_of=%s): self.result_of → %s", result_of, self.result_of)

        logger.debug("<<< Exiting add_result_of(result_of=%s)", result_of)

class Operation:
    """
    Class represents operation between single or two Variable objects.
    Operation objects contains type of operation, pointers to input Variable
    objects and pointer to resulting Variable from the operation.
    """

    def __init__(
        self,
        op_type: OpType,
        other_params: dict | None = None,
    ) -> None:
        self.op_type = op_type
        self.other_params = {} if other_params is None else other_params

    def add_params(self, params: list[Variable]) -> None:
        logger.debug(">>> Entering add_params(params=%s)", params)
        self.params = params
        logger.debug("add_params(self=%s,params=%s): self.params → %s", self, params, self.params)
        logger.debug("<<< Exiting add_params(params=%s)", params)

    def add_output(self, output: Variable) -> None:
        logger.debug(">>> Entering add_output(output=%s)", output)
        self.output = output
        logger.debug("add_output(self=%s,output=%s): self.output → %s", self, output, self.output)
        logger.debug("<<< Exiting add_output(output=%s)", output)

    def __eq__(self, value) -> bool:
        logger.debug(">>> Entering __eq__(value=%s)", value)
        logger.debug("<<< Exiting __eq__(value=%s)", value)
        return self.op_type == value if isinstance(value, OpType) else False


class GradientTracker:
    """
    Class contains methods to compute partial derivatives of Variable
    based on the computation graph.

    Examples:

    >>> with GradientTracker() as tracker:
    ...     a = Variable([2.0, 5.0])
    ...     b = Variable([1.0, 2.0])
    ...     m = Variable([1.0, 2.0])
    ...     c = a + b
    ...     d = a * b
    ...     e = c / d
    >>> tracker.gradient(e, a)
    array([-0.25, -0.04])
    >>> tracker.gradient(e, b)
    array([-1.  , -0.25])
    >>> tracker.gradient(e, m) is None
    True

    >>> with GradientTracker() as tracker:
    ...     a = Variable([[2.0, 5.0]])
    ...     b = Variable([[1.0], [2.0]])
    ...     c = a @ b
    >>> tracker.gradient(c, a)
    array([[1., 2.]])
    >>> tracker.gradient(c, b)
    array([[2.],
           [5.]])

    >>> with GradientTracker() as tracker:
    ...     a = Variable([[2.0, 5.0]])
    ...     b = a ** 3
    >>> tracker.gradient(b, a)
    array([[12., 75.]])
    """

    instance = None

    def __new__(cls) -> Self:
        """
        Executes at the creation of class object and returns if
        object is already created. This class follows singleton
        design pattern.
        """
        logger.debug(">>> Entering __new__()")
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        logger.debug("<<< Exiting __new__()")
        return cls.instance

    def __init__(self) -> None:
        self.enabled = False
        logger.debug("__init__(self=%s): self.enabled → %s", self, self.enabled)

    def __enter__(self) -> Self:
        logger.debug(">>> Entering __enter__()")
        self.enabled = True
        logger.debug("__enter__(self=%s): self.enabled → %s", self, self.enabled)
        logger.debug("<<< Exiting __enter__()")
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        self.enabled = False

    def append(
        self,
        op_type: OpType,
        params: list[Variable],
        output: Variable,
        other_params: dict | None = None,
    ) -> None:
        """
        Adds Operation object to the related Variable objects for
        creating computational graph for calculating gradients.

        Args:
            op_type: Operation type
            params: Input parameters to the operation
            output: Output variable of the operation
        """
        operation = Operation(op_type, other_params=other_params)
        param_nodes = []
        for param in params:
            param.add_param_to(operation)
            param_nodes.append(param)
        output.add_result_of(operation)

        operation.add_params(param_nodes)
        operation.add_output(output)

    def gradient(self, target: Variable, source: Variable) -> np.ndarray | None:
        """
        Reverse accumulation of partial derivatives to calculate gradients
        of target variable with respect to source variable.

        Args:
            target: target variable for which gradients are calculated.
            source: source variable with respect to which the gradients are
            calculated.

        Returns:
            Gradient of the source variable with respect to the target variable
        """
        logger.debug(">>> Entering gradient(target=%s,source=%s)", target, source)

        # partial derivatives with respect to target
        partial_deriv = defaultdict(lambda: 0)
        logger.debug("gradient(self=%s,target=%s,source=%s): partial_deriv → %s", self, target, source, partial_deriv)
        logger.debug("gradient(target=%s,source=%s): partial_deriv → %s", target, source, partial_deriv)
        partial_deriv[target] = np.ones_like(target.to_ndarray())

        # iterating through each operations in the computation graph
        operation_queue = [target.result_of]
        logger.debug("gradient(self=%s,target=%s,source=%s): operation_queue → %s", self, target, source, operation_queue)
        while len(operation_queue) > 0:
            operation = operation_queue.pop()
            logger.debug("gradient(self=%s,target=%s,source=%s): operation → %s", self, target, source, operation)
            for param in operation.params:
                # as per the chain rule, multiplying partial derivatives
                # of variables with respect to the target
                dparam_doutput = self.derivative(param, operation)
                logger.debug("gradient(self=%s,target=%s,source=%s): dparam_doutput → %s", self, target, source, dparam_doutput)
                logger.debug("gradient(target=%s,source=%s): dparam_doutput → %s", target, source, dparam_doutput)
                dparam_dtarget = dparam_doutput * partial_deriv[operation.output]
                logger.debug("gradient(self=%s,target=%s,source=%s): dparam_dtarget → %s", self, target, source, dparam_dtarget)
                partial_deriv[param] += dparam_dtarget

                if param.result_of and param.result_of != OpType.NOOP:
                    operation_queue.append(param.result_of)

        logger.debug("<<< Exiting gradient(target=%s,source=%s)", target, source)
        return partial_deriv.get(source)

    def derivative(self, param: Variable, operation: Operation) -> np.ndarray:
        """
        Compute the derivative of given operation/function

        Args:
            param: variable to be differentiated
            operation: function performed on the input variable

        Returns:
            Derivative of input variable with respect to the output of
            the operation
        """
        logger.debug(">>> Entering derivative(param=%s,operation=%s)", param, operation)
        params = operation.params
        logger.debug("derivative(self=%s,param=%s,operation=%s): params → %s", self, param, operation, params)

        if operation == OpType.ADD:
            return np.ones_like(params[0].to_ndarray(), dtype=np.float64)
        if operation == OpType.SUB:
            if params[0] == param:
                return np.ones_like(params[0].to_ndarray(), dtype=np.float64)
            return -np.ones_like(params[1].to_ndarray(), dtype=np.float64)
        if operation == OpType.MUL:
            return (
                params[1].to_ndarray().T
                if params[0] == param
                else params[0].to_ndarray().T
            )
        if operation == OpType.DIV:
            if params[0] == param:
                return 1 / params[1].to_ndarray()
            return -params[0].to_ndarray() / (params[1].to_ndarray() ** 2)
        if operation == OpType.MATMUL:
            return (
                params[1].to_ndarray().T
                if params[0] == param
                else params[0].to_ndarray().T
            )
        if operation == OpType.POWER:
            power = operation.other_params["power"]
            logger.debug("derivative(self=%s,param=%s,operation=%s): power → %s", self, param, operation, power)
            logger.debug("<<< Exiting derivative(param=%s,operation=%s)", param, operation)
            return power * (params[0].to_ndarray() ** (power - 1))

        err_msg = f"invalid operation type: {operation.op_type}"
        logger.debug("derivative(self=%s,param=%s,operation=%s): err_msg → %s", self, param, operation, err_msg)
        raise ValueError(err_msg)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
