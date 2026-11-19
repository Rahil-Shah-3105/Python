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
        logger.error(">>> Entering __init__(value=%s)", value, extra={"event.action": "__init__", "logrite.value": value})
        self.value = np.array(value)
        logger.error("__init__(value=%s): self.value → %s", value, self.value, extra={"event.action": "__init__", "logrite.value": value})

        # pointers to the operations to which the Variable is input
        self.param_to: list[Operation] = []
        # pointer to the operation of which the Variable is output of
        self.result_of: Operation = Operation(OpType.NOOP)
        logger.warning("<<< Exiting __init__(value=%s)", value, extra={"event.action": "__init__", "logrite.value": value})

    def __repr__(self) -> str:
        logger.error(">>> Entering __repr__()", extra={"event.action": "__repr__"})
        logger.warning("<<< Exiting __repr__()", extra={"event.action": "__repr__"})
        return f"Variable({self.value})"

    def to_ndarray(self) -> np.ndarray:
        logger.error(">>> Entering to_ndarray()", extra={"event.action": "to_ndarray"})
        logger.warning("<<< Exiting to_ndarray()", extra={"event.action": "to_ndarray"})
        return self.value

    def __add__(self, other: Variable) -> Variable:
        logger.error(">>> Entering __add__(other=%s)", other, extra={"event.action": "__add__", "logrite.other": other})
        result = Variable(self.value + other.value)
        logger.error("__add__(other=%s): result → %s", other, result, extra={"event.action": "__add__", "logrite.other": other})

        with GradientTracker() as tracker:
            # if tracker is enabled, computation graph will be updated
            if tracker.enabled:
                tracker.append(OpType.ADD, params=[self, other], output=result)
        logger.warning("<<< Exiting __add__(other=%s)", other, extra={"event.action": "__add__", "logrite.other": other})
        return result

    def __sub__(self, other: Variable) -> Variable:
        logger.error(">>> Entering __sub__(other=%s)", other, extra={"event.action": "__sub__", "logrite.other": other})
        result = Variable(self.value - other.value)
        logger.error("__sub__(other=%s): result → %s", other, result, extra={"event.action": "__sub__", "logrite.other": other})

        with GradientTracker() as tracker:
            # if tracker is enabled, computation graph will be updated
            if tracker.enabled:
                tracker.append(OpType.SUB, params=[self, other], output=result)
        logger.warning("<<< Exiting __sub__(other=%s)", other, extra={"event.action": "__sub__", "logrite.other": other})
        return result

    def __mul__(self, other: Variable) -> Variable:
        logger.error(">>> Entering __mul__(other=%s)", other, extra={"event.action": "__mul__", "logrite.other": other})
        result = Variable(self.value * other.value)
        logger.error("__mul__(other=%s): result → %s", other, result, extra={"event.action": "__mul__", "logrite.other": other})

        with GradientTracker() as tracker:
            # if tracker is enabled, computation graph will be updated
            if tracker.enabled:
                tracker.append(OpType.MUL, params=[self, other], output=result)
        logger.warning("<<< Exiting __mul__(other=%s)", other, extra={"event.action": "__mul__", "logrite.other": other})
        return result

    def __truediv__(self, other: Variable) -> Variable:
        logger.error(">>> Entering __truediv__(other=%s)", other, extra={"event.action": "__truediv__", "logrite.other": other})
        result = Variable(self.value / other.value)
        logger.error("__truediv__(other=%s): result → %s", other, result, extra={"event.action": "__truediv__", "logrite.other": other})

        with GradientTracker() as tracker:
            # if tracker is enabled, computation graph will be updated
            if tracker.enabled:
                tracker.append(OpType.DIV, params=[self, other], output=result)
        logger.warning("<<< Exiting __truediv__(other=%s)", other, extra={"event.action": "__truediv__", "logrite.other": other})
        return result

    def __matmul__(self, other: Variable) -> Variable:
        logger.error(">>> Entering __matmul__(other=%s)", other, extra={"event.action": "__matmul__", "logrite.other": other})
        result = Variable(self.value @ other.value)
        logger.error("__matmul__(other=%s): result → %s", other, result, extra={"event.action": "__matmul__", "logrite.other": other})

        with GradientTracker() as tracker:
            # if tracker is enabled, computation graph will be updated
            if tracker.enabled:
                tracker.append(OpType.MATMUL, params=[self, other], output=result)
        logger.warning("<<< Exiting __matmul__(other=%s)", other, extra={"event.action": "__matmul__", "logrite.other": other})
        return result

    def __pow__(self, power: int) -> Variable:
        logger.error(">>> Entering __pow__(power=%s)", power, extra={"event.action": "__pow__", "logrite.power": power})
        result = Variable(self.value**power)
        logger.error("__pow__(power=%s): result → %s", power, result, extra={"event.action": "__pow__", "logrite.power": power})

        with GradientTracker() as tracker:
            # if tracker is enabled, computation graph will be updated
            if tracker.enabled:
                tracker.append(
                    OpType.POWER,
                    params=[self],
                    output=result,
                    other_params={"power": power},
                )
        logger.warning("<<< Exiting __pow__(power=%s)", power, extra={"event.action": "__pow__", "logrite.power": power})
        return result

    def add_param_to(self, param_to: Operation) -> None:
        logger.error(">>> Entering add_param_to(param_to=%s)", param_to, extra={"event.action": "add_param_to", "logrite.param_to": param_to})
        self.param_to.append(param_to)
        logger.warning("<<< Exiting add_param_to(param_to=%s)", param_to, extra={"event.action": "add_param_to", "logrite.param_to": param_to})

    def add_result_of(self, result_of: Operation) -> None:
        logger.error(">>> Entering add_result_of(result_of=%s)", result_of, extra={"event.action": "add_result_of", "logrite.result_of": result_of})
        self.result_of = result_of
        logger.error("add_result_of(result_of=%s): self.result_of → %s", result_of, self.result_of, extra={"event.action": "add_result_of", "logrite.result_of": result_of})
        logger.debug("add_result_of(self=%s,result_of=%s): self.result_of → %s", self, result_of, self.result_of, extra={"event.action": "add_result_of", "logrite.result_of": result_of})

        logger.warning("<<< Exiting add_result_of(result_of=%s)", result_of, extra={"event.action": "add_result_of", "logrite.result_of": result_of})

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
        logger.error(">>> Entering __init__(op_type=%s,other_params=%s)", op_type, other_params, extra={"event.action": "__init__", "logrite.op_type": op_type, "logrite.other_params": other_params})
        self.op_type = op_type
        logger.debug("__init__(self=%s,op_type=%s,other_params=%s): self.op_type → %s", self, op_type, other_params, self.op_type, extra={"event.action": "__init__", "logrite.op_type": op_type, "logrite.other_params": other_params})
        self.other_params = {} if other_params is None else other_params
        logger.debug("__init__(self=%s,op_type=%s,other_params=%s): self.other_params → %s", self, op_type, other_params, self.other_params, extra={"event.action": "__init__", "logrite.op_type": op_type, "logrite.other_params": other_params})

        logger.warning("<<< Exiting __init__(op_type=%s,other_params=%s)", op_type, other_params, extra={"event.action": "__init__", "logrite.op_type": op_type, "logrite.other_params": other_params})
    def add_params(self, params: list[Variable]) -> None:
        logger.error(">>> Entering add_params(params=%s)", params, extra={"event.action": "add_params"})
        self.params = params
        logger.warning("<<< Exiting add_params(params=%s)", params, extra={"event.action": "add_params"})
        logger.debug("add_params(self=%s,params=%s): self.params → %s", self, params, self.params, extra={"event.action": "add_params"})

    def add_output(self, output: Variable) -> None:
        logger.error(">>> Entering add_output(output=%s)", output, extra={"event.action": "add_output", "logrite.output": output})
        self.output = output
        logger.warning("<<< Exiting add_output(output=%s)", output, extra={"event.action": "add_output", "logrite.output": output})
        logger.debug("add_output(self=%s,output=%s): self.output → %s", self, output, self.output, extra={"event.action": "add_output", "logrite.output": output})

    def __eq__(self, value) -> bool:
        logger.error(">>> Entering __eq__(value=%s)", value, extra={"event.action": "__eq__", "logrite.value": value})
        logger.warning("<<< Exiting __eq__(value=%s)", value, extra={"event.action": "__eq__", "logrite.value": value})
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
        logger.error(">>> Entering __new__()", extra={"event.action": "__new__"})
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        logger.warning("<<< Exiting __new__()", extra={"event.action": "__new__"})
        return cls.instance

    def __init__(self) -> None:
        self.enabled = False
        logger.debug("__init__(self=%s): self.enabled → %s", self, self.enabled, extra={"event.action": "__init__"})

    def __enter__(self) -> Self:
        logger.error(">>> Entering __enter__()", extra={"event.action": "__enter__"})
        self.enabled = True
        logger.debug("__enter__(self=%s): self.enabled → %s", self, self.enabled, extra={"event.action": "__enter__"})
        logger.warning("<<< Exiting __enter__()", extra={"event.action": "__enter__"})
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        logger.error(">>> Entering __exit__(exc_type=%s,exc=%s,traceback=%s)", exc_type, exc, traceback, extra={"event.action": "__exit__", "logrite.exc_type": exc_type, "logrite.exc": exc, "logrite.traceback": traceback})
        self.enabled = False
        logger.debug("__exit__(self=%s,exc_type=%s,exc=%s,traceback=%s): self.enabled → %s", self, exc_type, exc, traceback, self.enabled, extra={"event.action": "__exit__", "logrite.exc_type": exc_type, "logrite.exc": exc, "logrite.traceback": traceback})
        logger.warning("<<< Exiting __exit__(exc_type=%s,exc=%s,traceback=%s)", exc_type, exc, traceback, extra={"event.action": "__exit__", "logrite.exc_type": exc_type, "logrite.exc": exc, "logrite.traceback": traceback})

    def append(
        self,
        op_type: OpType,
        params: list[Variable],
        output: Variable,
        other_params: dict | None = None,
    ) -> None:
        logger.error(">>> Entering append(op_type=%s,params=%s,output=%s,other_params=%s)", op_type, params, output, other_params, extra={"event.action": "append", "logrite.op_type": op_type, "logrite.output": output, "logrite.other_params": other_params})
        """
        Adds Operation object to the related Variable objects for
        creating computational graph for calculating gradients.

        Args:
            op_type: Operation type
            params: Input parameters to the operation
            output: Output variable of the operation
        """
        operation = Operation(op_type, other_params=other_params)
        logger.error("append(op_type=%s,params=%s,output=%s,other_params=%s): operation → %s", op_type, params, output, other_params, operation, extra={"event.action": "append", "logrite.op_type": op_type, "logrite.output": output, "logrite.other_params": other_params})
        param_nodes = []
        for param in params:
            param.add_param_to(operation)
            param_nodes.append(param)
        output.add_result_of(operation)

        operation.add_params(param_nodes)
        operation.add_output(output)
        logger.warning("<<< Exiting append(op_type=%s,params=%s,output=%s,other_params=%s)", op_type, params, output, other_params, extra={"event.action": "append", "logrite.op_type": op_type, "logrite.output": output, "logrite.other_params": other_params})

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
        logger.error(">>> Entering gradient(target=%s,source=%s)", target, source, extra={"event.action": "gradient", "logrite.target": target, "logrite.source": source})

        # partial derivatives with respect to target
        partial_deriv = defaultdict(lambda: 0)
        logger.error("gradient(target=%s,source=%s): partial_deriv → %s", target, source, partial_deriv, extra={"event.action": "gradient", "logrite.target": target, "logrite.source": source})
        partial_deriv[target] = np.ones_like(target.to_ndarray())

        # iterating through each operations in the computation graph
        operation_queue = [target.result_of]
        while len(operation_queue) > 0:
            operation = operation_queue.pop()
            logger.error("gradient(target=%s,source=%s): operation → %s", target, source, operation, extra={"event.action": "gradient", "logrite.target": target, "logrite.source": source})
            for param in operation.params:
                # as per the chain rule, multiplying partial derivatives
                # of variables with respect to the target
                dparam_doutput = self.derivative(param, operation)
                logger.error("gradient(target=%s,source=%s): dparam_doutput → %s", target, source, dparam_doutput, extra={"event.action": "gradient", "logrite.target": target, "logrite.source": source})
                dparam_dtarget = dparam_doutput * partial_deriv[operation.output]
                partial_deriv[param] += dparam_dtarget

                if param.result_of and param.result_of != OpType.NOOP:
                    operation_queue.append(param.result_of)

        logger.warning("<<< Exiting gradient(target=%s,source=%s)", target, source, extra={"event.action": "gradient", "logrite.target": target, "logrite.source": source})
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
        logger.error(">>> Entering derivative(param=%s,operation=%s)", param, operation, extra={"event.action": "derivative", "logrite.param": param, "logrite.operation": operation})
        params = operation.params

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
            logger.warning("<<< Exiting derivative(param=%s,operation=%s)", param, operation, extra={"event.action": "derivative", "logrite.param": param, "logrite.operation": operation})
            return power * (params[0].to_ndarray() ** (power - 1))

        err_msg = f"invalid operation type: {operation.op_type}"
        raise ValueError(err_msg)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
