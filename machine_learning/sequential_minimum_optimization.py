"""
Sequential minimal optimization (SMO) for support vector machines (SVM)

Sequential minimal optimization (SMO) is an algorithm for solving the quadratic
programming (QP) problem that arises during the training of SVMs. It was invented by
John Platt in 1998.

Input:
    0: type: numpy.ndarray.
    1: first column of ndarray must be tags of samples, must be 1 or -1.
    2: rows of ndarray represent samples.

Usage:
    Command:
        python3 sequential_minimum_optimization.py
    Code:
        from sequential_minimum_optimization import SmoSVM, Kernel

        kernel = Kernel(kernel='poly', degree=3., coef0=1., gamma=0.5)
        init_alphas = np.zeros(train.shape[0])
        SVM = SmoSVM(train=train, alpha_list=init_alphas, kernel_func=kernel, cost=0.4,
                     b=0.0, tolerance=0.001)
        SVM.fit()
        predict = SVM.predict(test_samples)

Reference:
    https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/smo-book.pdf
    https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/tr-98-14.pdf
"""

import os
import sys
import urllib.request

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.datasets import make_blobs, make_circles
from sklearn.preprocessing import StandardScaler
import time
import logging
logger = logging.getLogger(__name__)

CANCER_DATASET_URL = (
    "https://archive.ics.uci.edu/ml/machine-learning-databases/"
    "breast-cancer-wisconsin/wdbc.data"
)


class SmoSVM:
    def __init__(
        self,
        train,
        kernel_func,
        alpha_list=None,
        cost=0.4,
        b=0.0,
        tolerance=0.001,
        auto_norm=True,
    ):
        logger.error(">>> Entering __init__(train=%s,kernel_func=%s,alpha_list=%s,cost=%s,b=%s,tolerance=%s,auto_norm=%s)", train, kernel_func, alpha_list, cost, b, tolerance, auto_norm, extra={"event.action": "__init__", "logrite.train": train, "logrite.kernel_func": kernel_func, "logrite.alpha_list": alpha_list, "logrite.cost": cost, "logrite.b": b, "logrite.tolerance": tolerance, "logrite.auto_norm": auto_norm})
        self._init = True
        logger.debug("__init__(self=%s,train=%s,kernel_func=%s,alpha_list=%s,cost=%s,b=%s,tolerance=%s,auto_norm=%s): self._init → %s", self, train, kernel_func, alpha_list, cost, b, tolerance, auto_norm, self._init, extra={"event.action": "__init__", "logrite.train": train, "logrite.kernel_func": kernel_func, "logrite.alpha_list": alpha_list, "logrite.cost": cost, "logrite.b": b, "logrite.tolerance": tolerance, "logrite.auto_norm": auto_norm})
        self._auto_norm = auto_norm
        logger.debug("__init__(self=%s,train=%s,kernel_func=%s,alpha_list=%s,cost=%s,b=%s,tolerance=%s,auto_norm=%s): self._auto_norm → %s", self, train, kernel_func, alpha_list, cost, b, tolerance, auto_norm, self._auto_norm, extra={"event.action": "__init__", "logrite.train": train, "logrite.kernel_func": kernel_func, "logrite.alpha_list": alpha_list, "logrite.cost": cost, "logrite.b": b, "logrite.tolerance": tolerance, "logrite.auto_norm": auto_norm})
        self._c = np.float64(cost)
        logger.error("__init__(train=%s,kernel_func=%s,alpha_list=%s,cost=%s,b=%s,tolerance=%s,auto_norm=%s): self._c → %s", train, kernel_func, alpha_list, cost, b, tolerance, auto_norm, self._c, extra={"event.action": "__init__", "logrite.train": train, "logrite.kernel_func": kernel_func, "logrite.alpha_list": alpha_list, "logrite.cost": cost, "logrite.b": b, "logrite.tolerance": tolerance, "logrite.auto_norm": auto_norm})
        self._b = np.float64(b)
        logger.error("__init__(train=%s,kernel_func=%s,alpha_list=%s,cost=%s,b=%s,tolerance=%s,auto_norm=%s): self._b → %s", train, kernel_func, alpha_list, cost, b, tolerance, auto_norm, self._b, extra={"event.action": "__init__", "logrite.train": train, "logrite.kernel_func": kernel_func, "logrite.alpha_list": alpha_list, "logrite.cost": cost, "logrite.b": b, "logrite.tolerance": tolerance, "logrite.auto_norm": auto_norm})
        self._tol = np.float64(tolerance) if tolerance > 0.0001 else np.float64(0.001)
        logger.error("__init__(train=%s,kernel_func=%s,alpha_list=%s,cost=%s,b=%s,tolerance=%s,auto_norm=%s): self._tol → %s", train, kernel_func, alpha_list, cost, b, tolerance, auto_norm, self._tol, extra={"event.action": "__init__", "logrite.train": train, "logrite.kernel_func": kernel_func, "logrite.alpha_list": alpha_list, "logrite.cost": cost, "logrite.b": b, "logrite.tolerance": tolerance, "logrite.auto_norm": auto_norm})

        self.tags = train[:, 0]
        logger.debug("__init__(self=%s,train=%s,kernel_func=%s,alpha_list=%s,cost=%s,b=%s,tolerance=%s,auto_norm=%s): self.tags → %s", self, train, kernel_func, alpha_list, cost, b, tolerance, auto_norm, self.tags, extra={"event.action": "__init__", "logrite.train": train, "logrite.kernel_func": kernel_func, "logrite.alpha_list": alpha_list, "logrite.cost": cost, "logrite.b": b, "logrite.tolerance": tolerance, "logrite.auto_norm": auto_norm})
        self.samples = self._norm(train[:, 1:]) if self._auto_norm else train[:, 1:]
        logger.error("__init__(train=%s,kernel_func=%s,alpha_list=%s,cost=%s,b=%s,tolerance=%s,auto_norm=%s): self.samples → %s", train, kernel_func, alpha_list, cost, b, tolerance, auto_norm, self.samples, extra={"event.action": "__init__", "logrite.train": train, "logrite.kernel_func": kernel_func, "logrite.alpha_list": alpha_list, "logrite.cost": cost, "logrite.b": b, "logrite.tolerance": tolerance, "logrite.auto_norm": auto_norm})
        self.alphas = alpha_list if alpha_list is not None else np.zeros(train.shape[0])
        logger.error("__init__(train=%s,kernel_func=%s,alpha_list=%s,cost=%s,b=%s,tolerance=%s,auto_norm=%s): self.alphas → %s", train, kernel_func, alpha_list, cost, b, tolerance, auto_norm, self.alphas, extra={"event.action": "__init__", "logrite.train": train, "logrite.kernel_func": kernel_func, "logrite.alpha_list": alpha_list, "logrite.cost": cost, "logrite.b": b, "logrite.tolerance": tolerance, "logrite.auto_norm": auto_norm})
        self.Kernel = kernel_func
        logger.debug("__init__(self=%s,train=%s,kernel_func=%s,alpha_list=%s,cost=%s,b=%s,tolerance=%s,auto_norm=%s): self.Kernel → %s", self, train, kernel_func, alpha_list, cost, b, tolerance, auto_norm, self.Kernel, extra={"event.action": "__init__", "logrite.train": train, "logrite.kernel_func": kernel_func, "logrite.alpha_list": alpha_list, "logrite.cost": cost, "logrite.b": b, "logrite.tolerance": tolerance, "logrite.auto_norm": auto_norm})

        self._eps = 0.001
        logger.debug("__init__(self=%s,train=%s,kernel_func=%s,alpha_list=%s,cost=%s,b=%s,tolerance=%s,auto_norm=%s): self._eps → %s", self, train, kernel_func, alpha_list, cost, b, tolerance, auto_norm, self._eps, extra={"event.action": "__init__", "logrite.train": train, "logrite.kernel_func": kernel_func, "logrite.alpha_list": alpha_list, "logrite.cost": cost, "logrite.b": b, "logrite.tolerance": tolerance, "logrite.auto_norm": auto_norm})
        self._all_samples = list(range(self.length))
        logger.error("__init__(train=%s,kernel_func=%s,alpha_list=%s,cost=%s,b=%s,tolerance=%s,auto_norm=%s): self._all_samples → %s", train, kernel_func, alpha_list, cost, b, tolerance, auto_norm, self._all_samples, extra={"event.action": "__init__", "logrite.train": train, "logrite.kernel_func": kernel_func, "logrite.alpha_list": alpha_list, "logrite.cost": cost, "logrite.b": b, "logrite.tolerance": tolerance, "logrite.auto_norm": auto_norm})
        self._K_matrix = self._calculate_k_matrix()
        logger.error("__init__(train=%s,kernel_func=%s,alpha_list=%s,cost=%s,b=%s,tolerance=%s,auto_norm=%s): self._K_matrix → %s", train, kernel_func, alpha_list, cost, b, tolerance, auto_norm, self._K_matrix, extra={"event.action": "__init__", "logrite.train": train, "logrite.kernel_func": kernel_func, "logrite.alpha_list": alpha_list, "logrite.cost": cost, "logrite.b": b, "logrite.tolerance": tolerance, "logrite.auto_norm": auto_norm})
        self._error = np.zeros(self.length)
        logger.error("__init__(train=%s,kernel_func=%s,alpha_list=%s,cost=%s,b=%s,tolerance=%s,auto_norm=%s): self._error → %s", train, kernel_func, alpha_list, cost, b, tolerance, auto_norm, self._error, extra={"event.action": "__init__", "logrite.train": train, "logrite.kernel_func": kernel_func, "logrite.alpha_list": alpha_list, "logrite.cost": cost, "logrite.b": b, "logrite.tolerance": tolerance, "logrite.auto_norm": auto_norm})
        self._unbound = []
        logger.debug("__init__(self=%s,train=%s,kernel_func=%s,alpha_list=%s,cost=%s,b=%s,tolerance=%s,auto_norm=%s): self._unbound → %s", self, train, kernel_func, alpha_list, cost, b, tolerance, auto_norm, self._unbound, extra={"event.action": "__init__", "logrite.train": train, "logrite.kernel_func": kernel_func, "logrite.alpha_list": alpha_list, "logrite.cost": cost, "logrite.b": b, "logrite.tolerance": tolerance, "logrite.auto_norm": auto_norm})

        logger.warning("<<< Exiting __init__(train=%s,kernel_func=%s,alpha_list=%s,cost=%s,b=%s,tolerance=%s,auto_norm=%s)", train, kernel_func, alpha_list, cost, b, tolerance, auto_norm, extra={"event.action": "__init__", "logrite.train": train, "logrite.kernel_func": kernel_func, "logrite.alpha_list": alpha_list, "logrite.cost": cost, "logrite.b": b, "logrite.tolerance": tolerance, "logrite.auto_norm": auto_norm})
        self.choose_alpha = self._choose_alphas()
        logger.error("__init__(train=%s,kernel_func=%s,alpha_list=%s,cost=%s,b=%s,tolerance=%s,auto_norm=%s): self.choose_alpha → %s", train, kernel_func, alpha_list, cost, b, tolerance, auto_norm, self.choose_alpha, extra={"event.action": "__init__", "logrite.train": train, "logrite.kernel_func": kernel_func, "logrite.alpha_list": alpha_list, "logrite.cost": cost, "logrite.b": b, "logrite.tolerance": tolerance, "logrite.auto_norm": auto_norm})

    # Calculate alphas using SMO algorithm
    def fit(self):
        logger.error(">>> Entering fit()", extra={"event.action": "fit"})
        k = self._k
        state = None
        logger.error("fit(): state → %s", state, extra={"event.action": "fit"})
        while True:
            # 1: Find alpha1, alpha2
            try:
                i1, i2 = self.choose_alpha.send(state)
                state = None
            except StopIteration:
                print("Optimization done!\nEvery sample satisfy the KKT condition!")
                break

            # 2: calculate new alpha2 and new alpha1
            y1, y2 = self.tags[i1], self.tags[i2]
            a1, a2 = self.alphas[i1].copy(), self.alphas[i2].copy()
            e1, e2 = self._e(i1), self._e(i2)
            args = (i1, i2, a1, a2, e1, e2, y1, y2)
            logger.error("fit(): args → %s", args, extra={"event.action": "fit"})
            a1_new, a2_new = self._get_new_alpha(*args)
            if not a1_new and not a2_new:
                state = False
                continue
            self.alphas[i1], self.alphas[i2] = a1_new, a2_new

            # 3: update threshold(b)
            b1_new = np.float64(
                -e1
                - y1 * k(i1, i1) * (a1_new - a1)
                - y2 * k(i2, i1) * (a2_new - a2)
                + self._b
            )
            b2_new = np.float64(
                -e2
                - y2 * k(i2, i2) * (a2_new - a2)
                - y1 * k(i1, i2) * (a1_new - a1)
                + self._b
            )
            if 0.0 < a1_new < self._c:
                b = b1_new
                logger.error("fit(): b → %s", b, extra={"event.action": "fit"})
            if 0.0 < a2_new < self._c:
                b = b2_new
            if not (np.float64(0) < a2_new < self._c) and not (
                np.float64(0) < a1_new < self._c
            ):
                b = (b1_new + b2_new) / 2.0
            b_old = self._b
            self._b = b
            logger.debug("fit(self=%s): self._b → %s", self, self._b, extra={"event.action": "fit"})

            # 4: update error, here we only calculate the error for non-bound samples
            self._unbound = [i for i in self._all_samples if self._is_unbound(i)]
            logger.error("fit(): self._unbound → %s", self._unbound, extra={"event.action": "fit"})
            for s in self.unbound:
                if s in (i1, i2):
                    continue
                self._error[s] += (
                    y1 * (a1_new - a1) * k(i1, s)
                    + y2 * (a2_new - a2) * k(i2, s)
                    + (self._b - b_old)
                )

            # if i1 or i2 is non-bound, update their error value to zero
            if self._is_unbound(i1):
                self._error[i1] = 0
            if self._is_unbound(i2):
                self._error[i2] = 0
                logger.warning("<<< Exiting fit()", extra={"event.action": "fit"})

    # Predict test samples
    def predict(self, test_samples, classify=True):
        logger.error(">>> Entering predict(test_samples=%s,classify=%s)", test_samples, classify, extra={"event.action": "predict", "logrite.test_samples": test_samples, "logrite.classify": classify})
        if test_samples.shape[1] > self.samples.shape[1]:
            raise ValueError(
                "Test samples' feature length does not equal to that of train samples"
            )

        if self._auto_norm:
            test_samples = self._norm(test_samples)
            logger.error("predict(test_samples=%s,classify=%s): test_samples → %s", test_samples, classify, test_samples, extra={"event.action": "predict", "logrite.test_samples": test_samples, "logrite.classify": classify})

        results = []
        logger.error("predict(test_samples=%s,classify=%s): results → %s", test_samples, classify, results, extra={"event.action": "predict", "logrite.test_samples": test_samples, "logrite.classify": classify})
        for test_sample in test_samples:
            result = self._predict(test_sample)
            logger.error("predict(test_samples=%s,classify=%s): result → %s", test_samples, classify, result, extra={"event.action": "predict", "logrite.test_samples": test_samples, "logrite.classify": classify})
            if classify:
                results.append(1 if result > 0 else -1)
            else:
                results.append(result)
        logger.warning("<<< Exiting predict(test_samples=%s,classify=%s)", test_samples, classify, extra={"event.action": "predict", "logrite.test_samples": test_samples, "logrite.classify": classify})
        return np.array(results)

    # Check if alpha violates the KKT condition
    def _check_obey_kkt(self, index):
        logger.error(">>> Entering _check_obey_kkt(index=%s)", index, extra={"event.action": "_check_obey_kkt", "logrite.index": index})
        alphas = self.alphas
        tol = self._tol
        r = self._e(index) * self.tags[index]
        logger.error("_check_obey_kkt(index=%s): r → %s", index, r, extra={"event.action": "_check_obey_kkt", "logrite.index": index})
        c = self._c

        logger.warning("<<< Exiting _check_obey_kkt(index=%s)", index, extra={"event.action": "_check_obey_kkt", "logrite.index": index})
        return (r < -tol and alphas[index] < c) or (r > tol and alphas[index] > 0.0)

    # Get value calculated from kernel function
    def _k(self, i1, i2):
        logger.error(">>> Entering _k(i1=%s,i2=%s)", i1, i2, extra={"event.action": "_k", "logrite.i1": i1, "logrite.i2": i2})
        # for test samples, use kernel function
        if isinstance(i2, np.ndarray):
            return self.Kernel(self.samples[i1], i2)
        # for training samples, kernel values have been saved in matrix
        else:
            logger.warning("<<< Exiting _k(i1=%s,i2=%s)", i1, i2, extra={"event.action": "_k", "logrite.i1": i1, "logrite.i2": i2})
            return self._K_matrix[i1, i2]

    # Get error for sample
    def _e(self, index):
        """
        Two cases:
            1: Sample[index] is non-bound, fetch error from list: _error
            2: sample[index] is bound, use predicted value minus true value: g(xi) - yi
        """
        logger.error(">>> Entering _e(index=%s)", index, extra={"event.action": "_e", "logrite.index": index})
        # get from error data
        if self._is_unbound(index):
            return self._error[index]
        # get by g(xi) - yi
        else:
            gx = np.dot(self.alphas * self.tags, self._K_matrix[:, index]) + self._b
            yi = self.tags[index]
            logger.warning("<<< Exiting _e(index=%s)", index, extra={"event.action": "_e", "logrite.index": index})
            return gx - yi

    # Calculate kernel matrix of all possible i1, i2, saving time
    def _calculate_k_matrix(self):
        logger.error(">>> Entering _calculate_k_matrix()", extra={"event.action": "_calculate_k_matrix"})
        k_matrix = np.zeros([self.length, self.length])
        logger.error("_calculate_k_matrix(): k_matrix → %s", k_matrix, extra={"event.action": "_calculate_k_matrix"})
        for i in self._all_samples:
            for j in self._all_samples:
                k_matrix[i, j] = np.float64(
                    self.Kernel(self.samples[i, :], self.samples[j, :])
                )
        logger.warning("<<< Exiting _calculate_k_matrix()", extra={"event.action": "_calculate_k_matrix"})
        return k_matrix

    # Predict tag for test sample
    def _predict(self, sample):
        logger.error(">>> Entering _predict(sample=%s)", sample, extra={"event.action": "_predict", "logrite.sample": sample})
        k = self._k
        predicted_value = (
            np.sum(
                [
                    self.alphas[i1] * self.tags[i1] * k(i1, sample)
                    for i1 in self._all_samples
                ]
            )
            + self._b
        )
        logger.warning("<<< Exiting _predict(sample=%s)", sample, extra={"event.action": "_predict", "logrite.sample": sample})
        return predicted_value

    # Choose alpha1 and alpha2
    def _choose_alphas(self):
        logger.error(">>> Entering _choose_alphas()", extra={"event.action": "_choose_alphas"})
        loci = yield from self._choose_a1()
        logger.error("_choose_alphas(): loci → %s", loci, extra={"event.action": "_choose_alphas"})
        if not loci:
            return None
        logger.warning("<<< Exiting _choose_alphas()", extra={"event.action": "_choose_alphas"})
        return loci

    def _choose_a1(self):
        """
        Choose first alpha
        Steps:
            1: First loop over all samples
            2: Second loop over all non-bound samples until no non-bound samples violate
               the KKT condition.
            3: Repeat these two processes until no samples violate the KKT condition
               after the first loop.
        """
        logger.error(">>> Entering _choose_a1()", extra={"event.action": "_choose_a1"})
        while True:
            all_not_obey = True
            # all sample
            print("Scanning all samples!")
            for i1 in [i for i in self._all_samples if self._check_obey_kkt(i)]:
                all_not_obey = False
                yield from self._choose_a2(i1)

            # non-bound sample
            print("Scanning non-bound samples!")
            while True:
                not_obey = True
                for i1 in [
                    i
                    for i in self._all_samples
                    if self._check_obey_kkt(i) and self._is_unbound(i)
                ]:
                    not_obey = False
                    yield from self._choose_a2(i1)
                if not_obey:
                    print("All non-bound samples satisfy the KKT condition!")
                    break
            if all_not_obey:
                print("All samples satisfy the KKT condition!")
                break
        logger.warning("<<< Exiting _choose_a1()", extra={"event.action": "_choose_a1"})
        return False

    def _choose_a2(self, i1):
        """
        Choose the second alpha using a heuristic algorithm
        Steps:
            1: Choose alpha2 that maximizes the step size (|E1 - E2|).
            2: Start in a random point, loop over all non-bound samples till alpha1 and
               alpha2 are optimized.
            3: Start in a random point, loop over all samples till alpha1 and alpha2 are
               optimized.
        """
        logger.error(">>> Entering _choose_a2(i1=%s)", i1, extra={"event.action": "_choose_a2", "logrite.i1": i1})
        self._unbound = [i for i in self._all_samples if self._is_unbound(i)]
        logger.error("_choose_a2(i1=%s): self._unbound → %s", i1, self._unbound, extra={"event.action": "_choose_a2", "logrite.i1": i1})

        if len(self.unbound) > 0:
            tmp_error = self._error.copy().tolist()
            logger.error("_choose_a2(i1=%s): tmp_error → %s", i1, tmp_error, extra={"event.action": "_choose_a2", "logrite.i1": i1})
            tmp_error_dict = {
                index: value
                for index, value in enumerate(tmp_error)
                if self._is_unbound(index)
            }
            if self._e(i1) >= 0:
                i2 = min(tmp_error_dict, key=lambda index: tmp_error_dict[index])
            else:
                i2 = max(tmp_error_dict, key=lambda index: tmp_error_dict[index])
                logger.error("_choose_a2(i1=%s): i2 → %s", i1, i2, extra={"event.action": "_choose_a2", "logrite.i1": i1})
            cmd = yield i1, i2
            if cmd is None:
                return

        rng = np.random.default_rng()
        for i2 in np.roll(self.unbound, rng.choice(self.length)):
            cmd = yield i1, i2
            if cmd is None:
                return

        for i2 in np.roll(self._all_samples, rng.choice(self.length)):
            cmd = yield i1, i2
            if cmd is None:
                logger.warning("<<< Exiting _choose_a2(i1=%s)", i1, extra={"event.action": "_choose_a2", "logrite.i1": i1})
                return

    # Get the new alpha2 and new alpha1
    def _get_new_alpha(self, i1, i2, a1, a2, e1, e2, y1, y2):
        logger.error(">>> Entering _get_new_alpha(i1=%s,i2=%s,a1=%s,a2=%s,e1=%s,e2=%s,y1=%s,y2=%s)", i1, i2, a1, a2, e1, e2, y1, y2, extra={"event.action": "_get_new_alpha", "logrite.i1": i1, "logrite.i2": i2, "logrite.a1": a1, "logrite.a2": a2, "logrite.e1": e1, "logrite.e2": e2, "logrite.y1": y1, "logrite.y2": y2})
        k = self._k
        if i1 == i2:
            return None, None

        # calculate L and H which bound the new alpha2
        s = y1 * y2
        if s == -1:
            l, h = max(0.0, a2 - a1), min(self._c, self._c + a2 - a1)  # noqa: E741
        else:
            l, h = max(0.0, a2 + a1 - self._c), min(self._c, a2 + a1)  # noqa: E741
        if l == h:
            return None, None

        # calculate eta
        k11 = k(i1, i1)
        k22 = k(i2, i2)
        k12 = k(i1, i2)

        # select the new alpha2 which could achieve the minimal objectives
        if (eta := k11 + k22 - 2.0 * k12) > 0.0:
            a2_new_unc = a2 + (y2 * (e1 - e2)) / eta
            # a2_new has a boundary
            if a2_new_unc >= h:
                a2_new = h
            elif a2_new_unc <= l:
                a2_new = l
            else:
                a2_new = a2_new_unc
        else:
            b = self._b
            l1 = a1 + s * (a2 - l)
            h1 = a1 + s * (a2 - h)

            # Method 1
            f1 = y1 * (e1 + b) - a1 * k(i1, i1) - s * a2 * k(i1, i2)
            f2 = y2 * (e2 + b) - a2 * k(i2, i2) - s * a1 * k(i1, i2)
            ol = (
                l1 * f1
                + l * f2
                + 1 / 2 * l1**2 * k(i1, i1)
                + 1 / 2 * l**2 * k(i2, i2)
                + s * l * l1 * k(i1, i2)
            )
            oh = (
                h1 * f1
                + h * f2
                + 1 / 2 * h1**2 * k(i1, i1)
                + 1 / 2 * h**2 * k(i2, i2)
                + s * h * h1 * k(i1, i2)
            )
            """
            Method 2: Use objective function to check which alpha2_new could achieve the
            minimal objectives
            """
            if ol < (oh - self._eps):
                a2_new = l
            elif ol > oh + self._eps:
                a2_new = h
            else:
                a2_new = a2

        # a1_new has a boundary too
        a1_new = a1 + s * (a2 - a2_new)
        if a1_new < 0:
            a2_new += s * a1_new
            a1_new = 0
        if a1_new > self._c:
            a2_new += s * (a1_new - self._c)
            a1_new = self._c

        logger.warning("<<< Exiting _get_new_alpha(i1=%s,i2=%s,a1=%s,a2=%s,e1=%s,e2=%s,y1=%s,y2=%s)", i1, i2, a1, a2, e1, e2, y1, y2, extra={"event.action": "_get_new_alpha", "logrite.i1": i1, "logrite.i2": i2, "logrite.a1": a1, "logrite.a2": a2, "logrite.e1": e1, "logrite.e2": e2, "logrite.y1": y1, "logrite.y2": y2})
        return a1_new, a2_new

    # Normalize data using min-max method
    def _norm(self, data):
        logger.error(">>> Entering _norm(data=%s)", data, extra={"event.action": "_norm"})
        if self._init:
            self._min = np.min(data, axis=0)
            logger.error("_norm(data=%s): self._min → %s", data, self._min, extra={"event.action": "_norm"})
            self._max = np.max(data, axis=0)
            logger.error("_norm(data=%s): self._max → %s", data, self._max, extra={"event.action": "_norm"})
            self._init = False
            logger.debug("_norm(self=%s,data=%s): self._init → %s", self, data, self._init, extra={"event.action": "_norm"})
            return (data - self._min) / (self._max - self._min)
        else:
            logger.warning("<<< Exiting _norm(data=%s)", data, extra={"event.action": "_norm"})
            return (data - self._min) / (self._max - self._min)

    def _is_unbound(self, index):
        logger.error(">>> Entering _is_unbound(index=%s)", index, extra={"event.action": "_is_unbound", "logrite.index": index})
        logger.warning("<<< Exiting _is_unbound(index=%s)", index, extra={"event.action": "_is_unbound", "logrite.index": index})
        return bool(0.0 < self.alphas[index] < self._c)

    def _is_support(self, index):
        logger.error(">>> Entering _is_support(index=%s)", index, extra={"event.action": "_is_support", "logrite.index": index})
        logger.warning("<<< Exiting _is_support(index=%s)", index, extra={"event.action": "_is_support", "logrite.index": index})
        return bool(self.alphas[index] > 0)

    @property
    def unbound(self):
        logger.error(">>> Entering unbound()", extra={"event.action": "unbound"})
        logger.warning("<<< Exiting unbound()", extra={"event.action": "unbound"})
        return self._unbound

    @property
    def support(self):
        logger.error(">>> Entering support()", extra={"event.action": "support"})
        logger.warning("<<< Exiting support()", extra={"event.action": "support"})
        return [i for i in range(self.length) if self._is_support(i)]

    @property
    def length(self):
        logger.error(">>> Entering length()", extra={"event.action": "length"})
        logger.warning("<<< Exiting length()", extra={"event.action": "length"})
        return self.samples.shape[0]


class Kernel:
    def __init__(self, kernel, degree=1.0, coef0=0.0, gamma=1.0):
        logger.error(">>> Entering __init__(kernel=%s,degree=%s,coef0=%s,gamma=%s)", kernel, degree, coef0, gamma, extra={"event.action": "__init__", "logrite.kernel": kernel, "logrite.degree": degree, "logrite.coef0": coef0, "logrite.gamma": gamma})
        logger.error("__init__(kernel=%s,degree=%s,coef0=%s,gamma=%s): degree → %s", kernel, degree, coef0, gamma, degree, extra={"event.action": "__init__", "logrite.kernel": kernel, "logrite.degree": degree, "logrite.coef0": coef0, "logrite.gamma": gamma})
        logger.error("__init__(kernel=%s,degree=%s,coef0=%s,gamma=%s): coef0 → %s", kernel, degree, coef0, gamma, coef0, extra={"event.action": "__init__", "logrite.kernel": kernel, "logrite.degree": degree, "logrite.coef0": coef0, "logrite.gamma": gamma})
        logger.error("__init__(kernel=%s,degree=%s,coef0=%s,gamma=%s): gamma → %s", kernel, degree, coef0, gamma, gamma, extra={"event.action": "__init__", "logrite.kernel": kernel, "logrite.degree": degree, "logrite.coef0": coef0, "logrite.gamma": gamma})
        self.degree = np.float64(degree)
        self.coef0 = np.float64(coef0)
        self.gamma = np.float64(gamma)
        self._kernel_name = kernel
        logger.debug("__init__(self=%s,kernel=%s,degree=%s,coef0=%s,gamma=%s): self._kernel_name → %s", self, kernel, degree, coef0, gamma, self._kernel_name, extra={"event.action": "__init__", "logrite.kernel": kernel, "logrite.degree": degree, "logrite.coef0": coef0, "logrite.gamma": gamma})
        self._kernel = self._get_kernel(kernel_name=kernel)
        logger.error("__init__(kernel=%s,degree=%s,coef0=%s,gamma=%s): self._kernel → %s", kernel, degree, coef0, gamma, self._kernel, extra={"event.action": "__init__", "logrite.kernel": kernel, "logrite.degree": degree, "logrite.coef0": coef0, "logrite.gamma": gamma})
        self._check()
        logger.warning("<<< Exiting __init__(kernel=%s,degree=%s,coef0=%s,gamma=%s)", kernel, degree, coef0, gamma, extra={"event.action": "__init__", "logrite.kernel": kernel, "logrite.degree": degree, "logrite.coef0": coef0, "logrite.gamma": gamma})

    def _polynomial(self, v1, v2):
        logger.error(">>> Entering _polynomial(v1=%s,v2=%s)", v1, v2, extra={"event.action": "_polynomial", "logrite.v1": v1, "logrite.v2": v2})
        logger.warning("<<< Exiting _polynomial(v1=%s,v2=%s)", v1, v2, extra={"event.action": "_polynomial", "logrite.v1": v1, "logrite.v2": v2})
        return (self.gamma * np.inner(v1, v2) + self.coef0) ** self.degree

    def _linear(self, v1, v2):
        logger.error(">>> Entering _linear(v1=%s,v2=%s)", v1, v2, extra={"event.action": "_linear", "logrite.v1": v1, "logrite.v2": v2})
        logger.warning("<<< Exiting _linear(v1=%s,v2=%s)", v1, v2, extra={"event.action": "_linear", "logrite.v1": v1, "logrite.v2": v2})
        return np.inner(v1, v2) + self.coef0

    def _rbf(self, v1, v2):
        logger.error(">>> Entering _rbf(v1=%s,v2=%s)", v1, v2, extra={"event.action": "_rbf", "logrite.v1": v1, "logrite.v2": v2})
        logger.warning("<<< Exiting _rbf(v1=%s,v2=%s)", v1, v2, extra={"event.action": "_rbf", "logrite.v1": v1, "logrite.v2": v2})
        return np.exp(-1 * (self.gamma * np.linalg.norm(v1 - v2) ** 2))

    def _check(self):
        logger.error(">>> Entering _check()", extra={"event.action": "_check"})
        if self._kernel == self._rbf and self.gamma < 0:
            raise ValueError("gamma value must be non-negative")
            logger.warning("<<< Exiting _check()", extra={"event.action": "_check"})

    def _get_kernel(self, kernel_name):
        logger.error(">>> Entering _get_kernel(kernel_name=%s)", kernel_name, extra={"event.action": "_get_kernel", "logrite.kernel_name": kernel_name})
        maps = {"linear": self._linear, "poly": self._polynomial, "rbf": self._rbf}
        logger.error("_get_kernel(kernel_name=%s): maps → %s", kernel_name, maps, extra={"event.action": "_get_kernel", "logrite.kernel_name": kernel_name})
        logger.warning("<<< Exiting _get_kernel(kernel_name=%s)", kernel_name, extra={"event.action": "_get_kernel", "logrite.kernel_name": kernel_name})
        return maps[kernel_name]

    def __call__(self, v1, v2):
        logger.error(">>> Entering __call__(v1=%s,v2=%s)", v1, v2, extra={"event.action": "__call__", "logrite.v1": v1, "logrite.v2": v2})
        logger.warning("<<< Exiting __call__(v1=%s,v2=%s)", v1, v2, extra={"event.action": "__call__", "logrite.v1": v1, "logrite.v2": v2})
        return self._kernel(v1, v2)

    def __repr__(self):
        logger.error(">>> Entering __repr__()", extra={"event.action": "__repr__"})
        logger.warning("<<< Exiting __repr__()", extra={"event.action": "__repr__"})
        return self._kernel_name


def count_time(func):
    logger.error(">>> Entering count_time(func=%s)", func, extra={"event.action": "count_time", "logrite.func": func})
    def call_func(*args, **kwargs):
        logger.error(">>> Entering call_func()", extra={"event.action": "call_func"})
        import time

        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        logger.error("call_func(): end_time → %s", end_time, extra={"event.action": "call_func"})
        print(f"SMO algorithm cost {end_time - start_time} seconds")
    logger.warning("<<< Exiting call_func()", extra={"event.action": "call_func"})

    return call_func


@count_time
def test_cancer_data():
    logger.error(">>> Entering test_cancer_data()", extra={"event.action": "test_cancer_data"})
    print("Hello!\nStart test SVM using the SMO algorithm!")
    # 0: download dataset and load into pandas' dataframe
    if not os.path.exists(r"cancer_data.csv"):
        request = urllib.request.Request(
            CANCER_DATASET_URL,
            headers={"User-Agent": "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"},
        )
        response = urllib.request.urlopen(request)  # noqa: S310
        logger.error("test_cancer_data(): response → %s", response, extra={"event.action": "test_cancer_data"})
        content = response.read().decode("utf-8")
        logger.error("test_cancer_data(): content → %s", content, extra={"event.action": "test_cancer_data"})
        with open(r"cancer_data.csv", "w") as f:
            f.write(content)

    data = pd.read_csv(
        "cancer_data.csv",
        header=None,
        dtype={0: str},  # Assuming the first column contains string data
    )

    # 1: pre-processing data
    del data[data.columns.tolist()[0]]
    data = data.dropna(axis=0)
    data = data.replace({"M": np.float64(1), "B": np.float64(-1)})
    logger.error("test_cancer_data(): data → %s", data, extra={"event.action": "test_cancer_data"})
    samples = np.array(data)[:, :]
    logger.error("test_cancer_data(): samples → %s", samples, extra={"event.action": "test_cancer_data"})

    # 2: dividing data into train_data data and test_data data
    train_data, test_data = samples[:328, :], samples[328:, :]
    test_tags, test_samples = test_data[:, 0], test_data[:, 1:]

    # 3: choose kernel function, and set initial alphas to zero (optional)
    my_kernel = Kernel(kernel="rbf", degree=5, coef0=1, gamma=0.5)
    logger.error("test_cancer_data(): my_kernel → %s", my_kernel, extra={"event.action": "test_cancer_data"})
    al = np.zeros(train_data.shape[0])
    logger.error("test_cancer_data(): al → %s", al, extra={"event.action": "test_cancer_data"})

    # 4: calculating best alphas using SMO algorithm and predict test_data samples
    mysvm = SmoSVM(
        train=train_data,
        kernel_func=my_kernel,
        alpha_list=al,
        cost=0.4,
        b=0.0,
        tolerance=0.001,
    )
    mysvm.fit()
    predict = mysvm.predict(test_samples)
    logger.error("test_cancer_data(): predict → %s", predict, extra={"event.action": "test_cancer_data"})

    # 5: check accuracy
    score = 0
    test_num = test_tags.shape[0]
    for i in range(test_tags.shape[0]):
        if test_tags[i] == predict[i]:
            score += 1
    print(f"\nAll: {test_num}\nCorrect: {score}\nIncorrect: {test_num - score}")
    print(f"Rough Accuracy: {score / test_tags.shape[0]}")
    logger.warning("<<< Exiting test_cancer_data()", extra={"event.action": "test_cancer_data"})


def test_demonstration():
    logger.error(">>> Entering test_demonstration()", extra={"event.action": "test_demonstration"})
    # change stdout
    print("\nStarting plot, please wait!")
    sys.stdout = open(os.devnull, "w")

    ax1 = plt.subplot2grid((2, 2), (0, 0))
    logger.error("test_demonstration(): ax1 → %s", ax1, extra={"event.action": "test_demonstration"})
    logger.debug("test_demonstration(): ax1 → %s", ax1, extra={"event.action": "test_demonstration"})
    ax2 = plt.subplot2grid((2, 2), (0, 1))
    logger.error("test_demonstration(): ax2 → %s", ax2, extra={"event.action": "test_demonstration"})
    ax3 = plt.subplot2grid((2, 2), (1, 0))
    logger.error("test_demonstration(): ax3 → %s", ax3, extra={"event.action": "test_demonstration"})
    ax4 = plt.subplot2grid((2, 2), (1, 1))
    logger.error("test_demonstration(): ax4 → %s", ax4, extra={"event.action": "test_demonstration"})
    ax1.set_title("Linear SVM, cost = 0.1")
    test_linear_kernel(ax1, cost=0.1)
    ax2.set_title("Linear SVM, cost = 500")
    logger.debug("test_demonstration(): ax2 → %s", ax2, extra={"event.action": "test_demonstration"})
    test_linear_kernel(ax2, cost=500)
    ax3.set_title("RBF kernel SVM, cost = 0.1")
    logger.debug("test_demonstration(): ax3 → %s", ax3, extra={"event.action": "test_demonstration"})
    test_rbf_kernel(ax3, cost=0.1)
    ax4.set_title("RBF kernel SVM, cost = 500")
    logger.debug("test_demonstration(): ax4 → %s", ax4, extra={"event.action": "test_demonstration"})
    test_rbf_kernel(ax4, cost=500)

    sys.stdout = sys.__stdout__
    logger.debug("test_demonstration(): sys.stdout → %s", sys.stdout, extra={"event.action": "test_demonstration"})
    print("Plot done!")
    logger.warning("<<< Exiting test_demonstration()", extra={"event.action": "test_demonstration"})


def test_linear_kernel(ax, cost):
    logger.error(">>> Entering test_linear_kernel(ax=%s,cost=%s)", ax, cost, extra={"event.action": "test_linear_kernel", "logrite.ax": ax, "logrite.cost": cost})
    train_x, train_y = make_blobs(
        n_samples=500, centers=2, n_features=2, random_state=1
    )
    train_y[train_y == 0] = -1
    scaler = StandardScaler()
    logger.error("test_linear_kernel(ax=%s,cost=%s): scaler → %s", ax, cost, scaler, extra={"event.action": "test_linear_kernel", "logrite.ax": ax, "logrite.cost": cost})
    train_x_scaled = scaler.fit_transform(train_x, train_y)
    logger.error("test_linear_kernel(ax=%s,cost=%s): train_x_scaled → %s", ax, cost, train_x_scaled, extra={"event.action": "test_linear_kernel", "logrite.ax": ax, "logrite.cost": cost})
    train_data = np.hstack((train_y.reshape(500, 1), train_x_scaled))
    logger.error("test_linear_kernel(ax=%s,cost=%s): train_data → %s", ax, cost, train_data, extra={"event.action": "test_linear_kernel", "logrite.ax": ax, "logrite.cost": cost})
    my_kernel = Kernel(kernel="linear", degree=5, coef0=1, gamma=0.5)
    logger.error("test_linear_kernel(ax=%s,cost=%s): my_kernel → %s", ax, cost, my_kernel, extra={"event.action": "test_linear_kernel", "logrite.ax": ax, "logrite.cost": cost})
    mysvm = SmoSVM(
        train=train_data,
        kernel_func=my_kernel,
        cost=cost,
        tolerance=0.001,
        auto_norm=False,
    )
    mysvm.fit()
    plot_partition_boundary(mysvm, train_data, ax=ax)
    logger.warning("<<< Exiting test_linear_kernel(ax=%s,cost=%s)", ax, cost, extra={"event.action": "test_linear_kernel", "logrite.ax": ax, "logrite.cost": cost})


def test_rbf_kernel(ax, cost):
    logger.error(">>> Entering test_rbf_kernel(ax=%s,cost=%s)", ax, cost, extra={"event.action": "test_rbf_kernel", "logrite.ax": ax, "logrite.cost": cost})
    train_x, train_y = make_circles(
        n_samples=500, noise=0.1, factor=0.1, random_state=1
    )
    train_y[train_y == 0] = -1
    scaler = StandardScaler()
    logger.error("test_rbf_kernel(ax=%s,cost=%s): scaler → %s", ax, cost, scaler, extra={"event.action": "test_rbf_kernel", "logrite.ax": ax, "logrite.cost": cost})
    train_x_scaled = scaler.fit_transform(train_x, train_y)
    logger.error("test_rbf_kernel(ax=%s,cost=%s): train_x_scaled → %s", ax, cost, train_x_scaled, extra={"event.action": "test_rbf_kernel", "logrite.ax": ax, "logrite.cost": cost})
    train_data = np.hstack((train_y.reshape(500, 1), train_x_scaled))
    logger.error("test_rbf_kernel(ax=%s,cost=%s): train_data → %s", ax, cost, train_data, extra={"event.action": "test_rbf_kernel", "logrite.ax": ax, "logrite.cost": cost})
    my_kernel = Kernel(kernel="rbf", degree=5, coef0=1, gamma=0.5)
    logger.error("test_rbf_kernel(ax=%s,cost=%s): my_kernel → %s", ax, cost, my_kernel, extra={"event.action": "test_rbf_kernel", "logrite.ax": ax, "logrite.cost": cost})
    mysvm = SmoSVM(
        train=train_data,
        kernel_func=my_kernel,
        cost=cost,
        tolerance=0.001,
        auto_norm=False,
    )
    mysvm.fit()
    plot_partition_boundary(mysvm, train_data, ax=ax)
    logger.warning("<<< Exiting test_rbf_kernel(ax=%s,cost=%s)", ax, cost, extra={"event.action": "test_rbf_kernel", "logrite.ax": ax, "logrite.cost": cost})


def plot_partition_boundary(
    model, train_data, ax, resolution=100, colors=("b", "k", "r")
):
    """
    We cannot get the optimal w of our kernel SVM model, which is different from a
    linear SVM.  For this reason, we generate randomly distributed points with high
    density, and predicted values of these points are calculated using our trained
    model. Then we could use this predicted values to draw contour map, and this contour
    map represents the SVM's partition boundary.
    """
    train_data_x = train_data[:, 1]
    train_data_y = train_data[:, 2]
    train_data_tags = train_data[:, 0]
    xrange = np.linspace(train_data_x.min(), train_data_x.max(), resolution)
    yrange = np.linspace(train_data_y.min(), train_data_y.max(), resolution)
    test_samples = np.array([(x, y) for x in xrange for y in yrange]).reshape(
        resolution * resolution, 2
    )

    test_tags = model.predict(test_samples, classify=False)
    grid = test_tags.reshape((len(xrange), len(yrange)))

    # Plot contour map which represents the partition boundary
    ax.contour(
        xrange,
        yrange,
        np.asmatrix(grid).T,
        levels=(-1, 0, 1),
        linestyles=("--", "-", "--"),
        linewidths=(1, 1, 1),
        colors=colors,
    )
    # Plot all train samples
    ax.scatter(
        train_data_x,
        train_data_y,
        c=train_data_tags,
        cmap=plt.cm.Dark2,
        lw=0,
        alpha=0.5,
    )

    # Plot support vectors
    support = model.support
    ax.scatter(
        train_data_x[support],
        train_data_y[support],
        c=train_data_tags[support],
        cmap=plt.cm.Dark2,
    )


if __name__ == "__main__":
    test_cancer_data()
    test_demonstration()
    plt.show()
