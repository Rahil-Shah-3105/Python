"""
 - - - - - -- - - - - - - - - - - - - - - - - - - - - - -
Name - - CNN - Convolution Neural Network For Photo Recognizing
Goal - - Recognize Handwriting Word Photo
Detail: Total 5 layers neural network
        * Convolution layer
        * Pooling layer
        * Input layer layer of BP
        * Hidden layer of BP
        * Output layer of BP
Author: Stephen Lee
Github: 245885195@qq.com
Date: 2017.9.20
- - - - - -- - - - - - - - - - - - - - - - - - - - - - -
"""

import pickle

import numpy as np
from matplotlib import pyplot as plt
import logging
logger = logging.getLogger(__name__)


class CNN:
    def __init__(
        self, conv1_get, size_p1, bp_num1, bp_num2, bp_num3, rate_w=0.2, rate_t=0.2
    ):
        logger.error(">>> Entering __init__(conv1_get=%s,size_p1=%s,bp_num1=%s,bp_num2=%s,bp_num3=%s,rate_w=%s,rate_t=%s)", conv1_get, size_p1, bp_num1, bp_num2, bp_num3, rate_w, rate_t, extra={"event.action": "__init__", "logrite.conv1_get": conv1_get, "logrite.size_p1": size_p1, "logrite.bp_num1": bp_num1, "logrite.bp_num2": bp_num2, "logrite.bp_num3": bp_num3, "logrite.rate_w": rate_w, "logrite.rate_t": rate_t})
        """
        :param conv1_get: [a,c,d], size, number, step of convolution kernel
        :param size_p1: pooling size
        :param bp_num1: units number of flatten layer
        :param bp_num2: units number of hidden layer
        :param bp_num3: units number of output layer
        :param rate_w: rate of weight learning
        :param rate_t: rate of threshold learning
        """
        logger.warning("<<< Exiting __init__(conv1_get=%s,size_p1=%s,bp_num1=%s,bp_num2=%s,bp_num3=%s,rate_w=%s,rate_t=%s)", conv1_get, size_p1, bp_num1, bp_num2, bp_num3, rate_w, rate_t, extra={"event.action": "__init__", "logrite.conv1_get": conv1_get, "logrite.size_p1": size_p1, "logrite.bp_num1": bp_num1, "logrite.bp_num2": bp_num2, "logrite.bp_num3": bp_num3, "logrite.rate_w": rate_w, "logrite.rate_t": rate_t})
        self.num_bp1 = bp_num1
        logger.debug("__init__(self=%s,conv1_get=%s,size_p1=%s,bp_num1=%s,bp_num2=%s,bp_num3=%s,rate_w=%s,rate_t=%s): self.num_bp1 → %s", self, conv1_get, size_p1, bp_num1, bp_num2, bp_num3, rate_w, rate_t, self.num_bp1, extra={"event.action": "__init__", "logrite.conv1_get": conv1_get, "logrite.size_p1": size_p1, "logrite.bp_num1": bp_num1, "logrite.bp_num2": bp_num2, "logrite.bp_num3": bp_num3, "logrite.rate_w": rate_w, "logrite.rate_t": rate_t})
        self.num_bp2 = bp_num2
        logger.debug("__init__(self=%s,conv1_get=%s,size_p1=%s,bp_num1=%s,bp_num2=%s,bp_num3=%s,rate_w=%s,rate_t=%s): self.num_bp2 → %s", self, conv1_get, size_p1, bp_num1, bp_num2, bp_num3, rate_w, rate_t, self.num_bp2, extra={"event.action": "__init__", "logrite.conv1_get": conv1_get, "logrite.size_p1": size_p1, "logrite.bp_num1": bp_num1, "logrite.bp_num2": bp_num2, "logrite.bp_num3": bp_num3, "logrite.rate_w": rate_w, "logrite.rate_t": rate_t})
        self.num_bp3 = bp_num3
        logger.debug("__init__(self=%s,conv1_get=%s,size_p1=%s,bp_num1=%s,bp_num2=%s,bp_num3=%s,rate_w=%s,rate_t=%s): self.num_bp3 → %s", self, conv1_get, size_p1, bp_num1, bp_num2, bp_num3, rate_w, rate_t, self.num_bp3, extra={"event.action": "__init__", "logrite.conv1_get": conv1_get, "logrite.size_p1": size_p1, "logrite.bp_num1": bp_num1, "logrite.bp_num2": bp_num2, "logrite.bp_num3": bp_num3, "logrite.rate_w": rate_w, "logrite.rate_t": rate_t})
        self.conv1 = conv1_get[:2]
        logger.debug("__init__(self=%s,conv1_get=%s,size_p1=%s,bp_num1=%s,bp_num2=%s,bp_num3=%s,rate_w=%s,rate_t=%s): self.conv1 → %s", self, conv1_get, size_p1, bp_num1, bp_num2, bp_num3, rate_w, rate_t, self.conv1, extra={"event.action": "__init__", "logrite.conv1_get": conv1_get, "logrite.size_p1": size_p1, "logrite.bp_num1": bp_num1, "logrite.bp_num2": bp_num2, "logrite.bp_num3": bp_num3, "logrite.rate_w": rate_w, "logrite.rate_t": rate_t})
        self.step_conv1 = conv1_get[2]
        logger.debug("__init__(self=%s,conv1_get=%s,size_p1=%s,bp_num1=%s,bp_num2=%s,bp_num3=%s,rate_w=%s,rate_t=%s): self.step_conv1 → %s", self, conv1_get, size_p1, bp_num1, bp_num2, bp_num3, rate_w, rate_t, self.step_conv1, extra={"event.action": "__init__", "logrite.conv1_get": conv1_get, "logrite.size_p1": size_p1, "logrite.bp_num1": bp_num1, "logrite.bp_num2": bp_num2, "logrite.bp_num3": bp_num3, "logrite.rate_w": rate_w, "logrite.rate_t": rate_t})
        self.size_pooling1 = size_p1
        logger.debug("__init__(self=%s,conv1_get=%s,size_p1=%s,bp_num1=%s,bp_num2=%s,bp_num3=%s,rate_w=%s,rate_t=%s): self.size_pooling1 → %s", self, conv1_get, size_p1, bp_num1, bp_num2, bp_num3, rate_w, rate_t, self.size_pooling1, extra={"event.action": "__init__", "logrite.conv1_get": conv1_get, "logrite.size_p1": size_p1, "logrite.bp_num1": bp_num1, "logrite.bp_num2": bp_num2, "logrite.bp_num3": bp_num3, "logrite.rate_w": rate_w, "logrite.rate_t": rate_t})
        self.rate_weight = rate_w
        logger.debug("__init__(self=%s,conv1_get=%s,size_p1=%s,bp_num1=%s,bp_num2=%s,bp_num3=%s,rate_w=%s,rate_t=%s): self.rate_weight → %s", self, conv1_get, size_p1, bp_num1, bp_num2, bp_num3, rate_w, rate_t, self.rate_weight, extra={"event.action": "__init__", "logrite.conv1_get": conv1_get, "logrite.size_p1": size_p1, "logrite.bp_num1": bp_num1, "logrite.bp_num2": bp_num2, "logrite.bp_num3": bp_num3, "logrite.rate_w": rate_w, "logrite.rate_t": rate_t})
        self.rate_thre = rate_t
        logger.debug("__init__(self=%s,conv1_get=%s,size_p1=%s,bp_num1=%s,bp_num2=%s,bp_num3=%s,rate_w=%s,rate_t=%s): self.rate_thre → %s", self, conv1_get, size_p1, bp_num1, bp_num2, bp_num3, rate_w, rate_t, self.rate_thre, extra={"event.action": "__init__", "logrite.conv1_get": conv1_get, "logrite.size_p1": size_p1, "logrite.bp_num1": bp_num1, "logrite.bp_num2": bp_num2, "logrite.bp_num3": bp_num3, "logrite.rate_w": rate_w, "logrite.rate_t": rate_t})
        rng = np.random.default_rng()
        logger.error("__init__(conv1_get=%s,size_p1=%s,bp_num1=%s,bp_num2=%s,bp_num3=%s,rate_w=%s,rate_t=%s): rng → %s", conv1_get, size_p1, bp_num1, bp_num2, bp_num3, rate_w, rate_t, rng, extra={"event.action": "__init__", "logrite.conv1_get": conv1_get, "logrite.size_p1": size_p1, "logrite.bp_num1": bp_num1, "logrite.bp_num2": bp_num2, "logrite.bp_num3": bp_num3, "logrite.rate_w": rate_w, "logrite.rate_t": rate_t})
        self.w_conv1 = [
            np.asmatrix(-1 * rng.random((self.conv1[0], self.conv1[0])) + 0.5)
            for i in range(self.conv1[1])
        ]
        logger.debug("__init__(self=%s,conv1_get=%s,size_p1=%s,bp_num1=%s,bp_num2=%s,bp_num3=%s,rate_w=%s,rate_t=%s): self.w_conv1 → %s", self, conv1_get, size_p1, bp_num1, bp_num2, bp_num3, rate_w, rate_t, self.w_conv1, extra={"event.action": "__init__", "logrite.conv1_get": conv1_get, "logrite.size_p1": size_p1, "logrite.bp_num1": bp_num1, "logrite.bp_num2": bp_num2, "logrite.bp_num3": bp_num3, "logrite.rate_w": rate_w, "logrite.rate_t": rate_t})
        self.wkj = np.asmatrix(-1 * rng.random((self.num_bp3, self.num_bp2)) + 0.5)
        logger.error("__init__(conv1_get=%s,size_p1=%s,bp_num1=%s,bp_num2=%s,bp_num3=%s,rate_w=%s,rate_t=%s): self.wkj → %s", conv1_get, size_p1, bp_num1, bp_num2, bp_num3, rate_w, rate_t, self.wkj, extra={"event.action": "__init__", "logrite.conv1_get": conv1_get, "logrite.size_p1": size_p1, "logrite.bp_num1": bp_num1, "logrite.bp_num2": bp_num2, "logrite.bp_num3": bp_num3, "logrite.rate_w": rate_w, "logrite.rate_t": rate_t})
        self.vji = np.asmatrix(-1 * rng.random((self.num_bp2, self.num_bp1)) + 0.5)
        logger.error("__init__(conv1_get=%s,size_p1=%s,bp_num1=%s,bp_num2=%s,bp_num3=%s,rate_w=%s,rate_t=%s): self.vji → %s", conv1_get, size_p1, bp_num1, bp_num2, bp_num3, rate_w, rate_t, self.vji, extra={"event.action": "__init__", "logrite.conv1_get": conv1_get, "logrite.size_p1": size_p1, "logrite.bp_num1": bp_num1, "logrite.bp_num2": bp_num2, "logrite.bp_num3": bp_num3, "logrite.rate_w": rate_w, "logrite.rate_t": rate_t})
        self.thre_conv1 = -2 * rng.random(self.conv1[1]) + 1
        logger.error("__init__(conv1_get=%s,size_p1=%s,bp_num1=%s,bp_num2=%s,bp_num3=%s,rate_w=%s,rate_t=%s): self.thre_conv1 → %s", conv1_get, size_p1, bp_num1, bp_num2, bp_num3, rate_w, rate_t, self.thre_conv1, extra={"event.action": "__init__", "logrite.conv1_get": conv1_get, "logrite.size_p1": size_p1, "logrite.bp_num1": bp_num1, "logrite.bp_num2": bp_num2, "logrite.bp_num3": bp_num3, "logrite.rate_w": rate_w, "logrite.rate_t": rate_t})
        self.thre_bp2 = -2 * rng.random(self.num_bp2) + 1
        logger.error("__init__(conv1_get=%s,size_p1=%s,bp_num1=%s,bp_num2=%s,bp_num3=%s,rate_w=%s,rate_t=%s): self.thre_bp2 → %s", conv1_get, size_p1, bp_num1, bp_num2, bp_num3, rate_w, rate_t, self.thre_bp2, extra={"event.action": "__init__", "logrite.conv1_get": conv1_get, "logrite.size_p1": size_p1, "logrite.bp_num1": bp_num1, "logrite.bp_num2": bp_num2, "logrite.bp_num3": bp_num3, "logrite.rate_w": rate_w, "logrite.rate_t": rate_t})
        self.thre_bp3 = -2 * rng.random(self.num_bp3) + 1
        logger.error("__init__(conv1_get=%s,size_p1=%s,bp_num1=%s,bp_num2=%s,bp_num3=%s,rate_w=%s,rate_t=%s): self.thre_bp3 → %s", conv1_get, size_p1, bp_num1, bp_num2, bp_num3, rate_w, rate_t, self.thre_bp3, extra={"event.action": "__init__", "logrite.conv1_get": conv1_get, "logrite.size_p1": size_p1, "logrite.bp_num1": bp_num1, "logrite.bp_num2": bp_num2, "logrite.bp_num3": bp_num3, "logrite.rate_w": rate_w, "logrite.rate_t": rate_t})

    def save_model(self, save_path):
        logger.error(">>> Entering save_model(save_path=%s)", save_path, extra={"event.action": "save_model", "logrite.save_path": save_path})
        # save model dict with pickle
        model_dic = {
            "num_bp1": self.num_bp1,
            "num_bp2": self.num_bp2,
            "num_bp3": self.num_bp3,
            "conv1": self.conv1,
            "step_conv1": self.step_conv1,
            "size_pooling1": self.size_pooling1,
            "rate_weight": self.rate_weight,
            "rate_thre": self.rate_thre,
            "w_conv1": self.w_conv1,
            "wkj": self.wkj,
            "vji": self.vji,
            "thre_conv1": self.thre_conv1,
            "thre_bp2": self.thre_bp2,
            "thre_bp3": self.thre_bp3,
        }
        with open(save_path, "wb") as f:
            pickle.dump(model_dic, f)

        print(f"Model saved: {save_path}")
        logger.warning("<<< Exiting save_model(save_path=%s)", save_path, extra={"event.action": "save_model", "logrite.save_path": save_path})

    @classmethod
    def read_model(cls, model_path):
        logger.error(">>> Entering read_model(model_path=%s)", model_path, extra={"event.action": "read_model", "logrite.model_path": model_path})
        # read saved model
        with open(model_path, "rb") as f:
            model_dic = pickle.load(f)  # noqa: S301
            logger.error("read_model(model_path=%s): model_dic → %s", model_path, model_dic, extra={"event.action": "read_model", "logrite.model_path": model_path})

        conv_get = model_dic.get("conv1")
        logger.error("read_model(model_path=%s): conv_get → %s", model_path, conv_get, extra={"event.action": "read_model", "logrite.model_path": model_path})
        conv_get.append(model_dic.get("step_conv1"))
        size_p1 = model_dic.get("size_pooling1")
        logger.error("read_model(model_path=%s): size_p1 → %s", model_path, size_p1, extra={"event.action": "read_model", "logrite.model_path": model_path})
        bp1 = model_dic.get("num_bp1")
        logger.error("read_model(model_path=%s): bp1 → %s", model_path, bp1, extra={"event.action": "read_model", "logrite.model_path": model_path})
        bp2 = model_dic.get("num_bp2")
        logger.error("read_model(model_path=%s): bp2 → %s", model_path, bp2, extra={"event.action": "read_model", "logrite.model_path": model_path})
        bp3 = model_dic.get("num_bp3")
        logger.error("read_model(model_path=%s): bp3 → %s", model_path, bp3, extra={"event.action": "read_model", "logrite.model_path": model_path})
        r_w = model_dic.get("rate_weight")
        logger.error("read_model(model_path=%s): r_w → %s", model_path, r_w, extra={"event.action": "read_model", "logrite.model_path": model_path})
        r_t = model_dic.get("rate_thre")
        logger.error("read_model(model_path=%s): r_t → %s", model_path, r_t, extra={"event.action": "read_model", "logrite.model_path": model_path})
        # create model instance
        conv_ins = CNN(conv_get, size_p1, bp1, bp2, bp3, r_w, r_t)
        logger.error("read_model(model_path=%s): conv_ins → %s", model_path, conv_ins, extra={"event.action": "read_model", "logrite.model_path": model_path})
        # modify model parameter
        conv_ins.w_conv1 = model_dic.get("w_conv1")
        conv_ins.wkj = model_dic.get("wkj")
        conv_ins.vji = model_dic.get("vji")
        conv_ins.thre_conv1 = model_dic.get("thre_conv1")
        conv_ins.thre_bp2 = model_dic.get("thre_bp2")
        conv_ins.thre_bp3 = model_dic.get("thre_bp3")
        logger.warning("<<< Exiting read_model(model_path=%s)", model_path, extra={"event.action": "read_model", "logrite.model_path": model_path})
        return conv_ins

    def sig(self, x):
        logger.error(">>> Entering sig(x=%s)", x, extra={"event.action": "sig", "logrite.x": x})
        logger.warning("<<< Exiting sig(x=%s)", x, extra={"event.action": "sig", "logrite.x": x})
        return 1 / (1 + np.exp(-1 * x))

    def do_round(self, x):
        logger.error(">>> Entering do_round(x=%s)", x, extra={"event.action": "do_round", "logrite.x": x})
        logger.warning("<<< Exiting do_round(x=%s)", x, extra={"event.action": "do_round", "logrite.x": x})
        return round(x, 3)

    def convolute(self, data, convs, w_convs, thre_convs, conv_step):
        logger.error(">>> Entering convolute(data=%s,convs=%s,w_convs=%s,thre_convs=%s,conv_step=%s)", data, convs, w_convs, thre_convs, conv_step, extra={"event.action": "convolute", "logrite.convs": convs, "logrite.w_convs": w_convs, "logrite.thre_convs": thre_convs, "logrite.conv_step": conv_step})
        # convolution process
        size_conv = convs[0]
        num_conv = convs[1]
        size_data = np.shape(data)[0]
        logger.error("convolute(data=%s,convs=%s,w_convs=%s,thre_convs=%s,conv_step=%s): size_data → %s", data, convs, w_convs, thre_convs, conv_step, size_data, extra={"event.action": "convolute", "logrite.convs": convs, "logrite.w_convs": w_convs, "logrite.thre_convs": thre_convs, "logrite.conv_step": conv_step})
        # get the data slice of original image data, data_focus
        data_focus = []
        logger.error("convolute(data=%s,convs=%s,w_convs=%s,thre_convs=%s,conv_step=%s): data_focus → %s", data, convs, w_convs, thre_convs, conv_step, data_focus, extra={"event.action": "convolute", "logrite.convs": convs, "logrite.w_convs": w_convs, "logrite.thre_convs": thre_convs, "logrite.conv_step": conv_step})
        for i_focus in range(0, size_data - size_conv + 1, conv_step):
            for j_focus in range(0, size_data - size_conv + 1, conv_step):
                focus = data[
                    i_focus : i_focus + size_conv, j_focus : j_focus + size_conv
                ]
                data_focus.append(focus)
        # calculate the feature map of every single kernel, and saved as list of matrix
        data_featuremap = []
        logger.error("convolute(data=%s,convs=%s,w_convs=%s,thre_convs=%s,conv_step=%s): data_featuremap → %s", data, convs, w_convs, thre_convs, conv_step, data_featuremap, extra={"event.action": "convolute", "logrite.convs": convs, "logrite.w_convs": w_convs, "logrite.thre_convs": thre_convs, "logrite.conv_step": conv_step})
        size_feature_map = int((size_data - size_conv) / conv_step + 1)
        logger.error("convolute(data=%s,convs=%s,w_convs=%s,thre_convs=%s,conv_step=%s): size_feature_map → %s", data, convs, w_convs, thre_convs, conv_step, size_feature_map, extra={"event.action": "convolute", "logrite.convs": convs, "logrite.w_convs": w_convs, "logrite.thre_convs": thre_convs, "logrite.conv_step": conv_step})
        for i_map in range(num_conv):
            featuremap = []
            logger.error("convolute(data=%s,convs=%s,w_convs=%s,thre_convs=%s,conv_step=%s): featuremap → %s", data, convs, w_convs, thre_convs, conv_step, featuremap, extra={"event.action": "convolute", "logrite.convs": convs, "logrite.w_convs": w_convs, "logrite.thre_convs": thre_convs, "logrite.conv_step": conv_step})
            for i_focus in range(len(data_focus)):
                net_focus = (
                    np.sum(np.multiply(data_focus[i_focus], w_convs[i_map]))
                    - thre_convs[i_map]
                )
                featuremap.append(self.sig(net_focus))
            featuremap = np.asmatrix(featuremap).reshape(
                size_feature_map, size_feature_map
            )
            data_featuremap.append(featuremap)

        # expanding the data slice to one dimension
        focus1_list = []
        for each_focus in data_focus:
            focus1_list.extend(self.Expand_Mat(each_focus))
        focus_list = np.asarray(focus1_list)
        logger.error("convolute(data=%s,convs=%s,w_convs=%s,thre_convs=%s,conv_step=%s): focus_list → %s", data, convs, w_convs, thre_convs, conv_step, focus_list, extra={"event.action": "convolute", "logrite.convs": convs, "logrite.w_convs": w_convs, "logrite.thre_convs": thre_convs, "logrite.conv_step": conv_step})
        logger.warning("<<< Exiting convolute(data=%s,convs=%s,w_convs=%s,thre_convs=%s,conv_step=%s)", data, convs, w_convs, thre_convs, conv_step, extra={"event.action": "convolute", "logrite.convs": convs, "logrite.w_convs": w_convs, "logrite.thre_convs": thre_convs, "logrite.conv_step": conv_step})
        return focus_list, data_featuremap

    def pooling(self, featuremaps, size_pooling, pooling_type="average_pool"):
        logger.error(">>> Entering pooling(featuremaps=%s,size_pooling=%s,pooling_type=%s)", featuremaps, size_pooling, pooling_type, extra={"event.action": "pooling", "logrite.featuremaps": featuremaps, "logrite.size_pooling": size_pooling, "logrite.pooling_type": pooling_type})
        # pooling process
        size_map = len(featuremaps[0])
        logger.error("pooling(featuremaps=%s,size_pooling=%s,pooling_type=%s): size_map → %s", featuremaps, size_pooling, pooling_type, size_map, extra={"event.action": "pooling", "logrite.featuremaps": featuremaps, "logrite.size_pooling": size_pooling, "logrite.pooling_type": pooling_type})
        size_pooled = int(size_map / size_pooling)
        logger.error("pooling(featuremaps=%s,size_pooling=%s,pooling_type=%s): size_pooled → %s", featuremaps, size_pooling, pooling_type, size_pooled, extra={"event.action": "pooling", "logrite.featuremaps": featuremaps, "logrite.size_pooling": size_pooling, "logrite.pooling_type": pooling_type})
        featuremap_pooled = []
        for i_map in range(len(featuremaps)):
            feature_map = featuremaps[i_map]
            map_pooled = []
            logger.error("pooling(featuremaps=%s,size_pooling=%s,pooling_type=%s): map_pooled → %s", featuremaps, size_pooling, pooling_type, map_pooled, extra={"event.action": "pooling", "logrite.featuremaps": featuremaps, "logrite.size_pooling": size_pooling, "logrite.pooling_type": pooling_type})
            for i_focus in range(0, size_map, size_pooling):
                for j_focus in range(0, size_map, size_pooling):
                    focus = feature_map[
                        i_focus : i_focus + size_pooling,
                        j_focus : j_focus + size_pooling,
                    ]
                    if pooling_type == "average_pool":
                        # average pooling
                        map_pooled.append(np.average(focus))
                    elif pooling_type == "max_pooling":
                        # max pooling
                        map_pooled.append(np.max(focus))
            map_pooled = np.asmatrix(map_pooled).reshape(size_pooled, size_pooled)
            featuremap_pooled.append(map_pooled)
        logger.warning("<<< Exiting pooling(featuremaps=%s,size_pooling=%s,pooling_type=%s)", featuremaps, size_pooling, pooling_type, extra={"event.action": "pooling", "logrite.featuremaps": featuremaps, "logrite.size_pooling": size_pooling, "logrite.pooling_type": pooling_type})
        return featuremap_pooled

    def _expand(self, data):
        logger.error(">>> Entering _expand(data=%s)", data, extra={"event.action": "_expand"})
        # expanding three dimension data to one dimension list
        data_expanded = []
        logger.error("_expand(data=%s): data_expanded → %s", data, data_expanded, extra={"event.action": "_expand"})
        for i in range(len(data)):
            shapes = np.shape(data[i])
            logger.error("_expand(data=%s): shapes → %s", data, shapes, extra={"event.action": "_expand"})
            data_listed = data[i].reshape(1, shapes[0] * shapes[1])
            data_listed = data_listed.getA().tolist()[0]
            logger.error("_expand(data=%s): data_listed → %s", data, data_listed, extra={"event.action": "_expand"})
            data_expanded.extend(data_listed)
        data_expanded = np.asarray(data_expanded)
        logger.warning("<<< Exiting _expand(data=%s)", data, extra={"event.action": "_expand"})
        return data_expanded

    def _expand_mat(self, data_mat):
        logger.error(">>> Entering _expand_mat(data_mat=%s)", data_mat, extra={"event.action": "_expand_mat", "logrite.data_mat": data_mat})
        # expanding matrix to one dimension list
        data_mat = np.asarray(data_mat)
        logger.error("_expand_mat(data_mat=%s): data_mat → %s", data_mat, data_mat, extra={"event.action": "_expand_mat", "logrite.data_mat": data_mat})
        shapes = np.shape(data_mat)
        logger.error("_expand_mat(data_mat=%s): shapes → %s", data_mat, shapes, extra={"event.action": "_expand_mat", "logrite.data_mat": data_mat})
        data_expanded = data_mat.reshape(1, shapes[0] * shapes[1])
        logger.error("_expand_mat(data_mat=%s): data_expanded → %s", data_mat, data_expanded, extra={"event.action": "_expand_mat", "logrite.data_mat": data_mat})
        logger.warning("<<< Exiting _expand_mat(data_mat=%s)", data_mat, extra={"event.action": "_expand_mat", "logrite.data_mat": data_mat})
        return data_expanded

    def _calculate_gradient_from_pool(
        self, out_map, pd_pool, num_map, size_map, size_pooling
    ):
        logger.error(">>> Entering _calculate_gradient_from_pool(out_map=%s,pd_pool=%s,num_map=%s,size_map=%s,size_pooling=%s)", out_map, pd_pool, num_map, size_map, size_pooling, extra={"event.action": "_calculate_gradient_from_pool", "logrite.out_map": out_map, "logrite.pd_pool": pd_pool, "logrite.num_map": num_map, "logrite.size_map": size_map, "logrite.size_pooling": size_pooling})
        """
        calculate the gradient from the data slice of pool layer
        pd_pool: list of matrix
        out_map: the shape of data slice(size_map*size_map)
        return: pd_all: list of matrix, [num, size_map, size_map]
        """
        pd_all = []
        i_pool = 0
        for i_map in range(num_map):
            pd_conv1 = np.ones((size_map, size_map))
            for i in range(0, size_map, size_pooling):
                for j in range(0, size_map, size_pooling):
                    pd_conv1[i : i + size_pooling, j : j + size_pooling] = pd_pool[
                        i_pool
                    ]
                    i_pool = i_pool + 1
            pd_conv2 = np.multiply(
                pd_conv1, np.multiply(out_map[i_map], (1 - out_map[i_map]))
            )
            pd_all.append(pd_conv2)
        logger.warning("<<< Exiting _calculate_gradient_from_pool(out_map=%s,pd_pool=%s,num_map=%s,size_map=%s,size_pooling=%s)", out_map, pd_pool, num_map, size_map, size_pooling, extra={"event.action": "_calculate_gradient_from_pool", "logrite.out_map": out_map, "logrite.pd_pool": pd_pool, "logrite.num_map": num_map, "logrite.size_map": size_map, "logrite.size_pooling": size_pooling})
        return pd_all

    def train(
        self, patterns, datas_train, datas_teach, n_repeat, error_accuracy, draw_e=bool
    ):
        logger.error(">>> Entering train(patterns=%s,datas_train=%s,datas_teach=%s,n_repeat=%s,error_accuracy=%s,draw_e=%s)", patterns, datas_train, datas_teach, n_repeat, error_accuracy, draw_e, extra={"event.action": "train", "logrite.patterns": patterns, "logrite.datas_train": datas_train, "logrite.datas_teach": datas_teach, "logrite.n_repeat": n_repeat, "logrite.error_accuracy": error_accuracy, "logrite.draw_e": draw_e})
        # model training
        print("----------------------Start Training-------------------------")
        print((" - - Shape: Train_Data  ", np.shape(datas_train)))
        print((" - - Shape: Teach_Data  ", np.shape(datas_teach)))
        rp = 0
        all_mse = []
        mse = 10000
        while rp < n_repeat and mse >= error_accuracy:
            error_count = 0
            print(f"-------------Learning Time {rp}--------------")
            for p in range(len(datas_train)):
                # print('------------Learning Image: %d--------------'%p)
                data_train = np.asmatrix(datas_train[p])
                logger.error("train(patterns=%s,datas_train=%s,datas_teach=%s,n_repeat=%s,error_accuracy=%s,draw_e=%s): data_train → %s", patterns, datas_train, datas_teach, n_repeat, error_accuracy, draw_e, data_train, extra={"event.action": "train", "logrite.patterns": patterns, "logrite.datas_train": datas_train, "logrite.datas_teach": datas_teach, "logrite.n_repeat": n_repeat, "logrite.error_accuracy": error_accuracy, "logrite.draw_e": draw_e})
                data_teach = np.asarray(datas_teach[p])
                logger.error("train(patterns=%s,datas_train=%s,datas_teach=%s,n_repeat=%s,error_accuracy=%s,draw_e=%s): data_teach → %s", patterns, datas_train, datas_teach, n_repeat, error_accuracy, draw_e, data_teach, extra={"event.action": "train", "logrite.patterns": patterns, "logrite.datas_train": datas_train, "logrite.datas_teach": datas_teach, "logrite.n_repeat": n_repeat, "logrite.error_accuracy": error_accuracy, "logrite.draw_e": draw_e})
                data_focus1, data_conved1 = self.convolute(
                    data_train,
                    self.conv1,
                    self.w_conv1,
                    self.thre_conv1,
                    conv_step=self.step_conv1,
                )
                data_pooled1 = self.pooling(data_conved1, self.size_pooling1)
                logger.error("train(patterns=%s,datas_train=%s,datas_teach=%s,n_repeat=%s,error_accuracy=%s,draw_e=%s): data_pooled1 → %s", patterns, datas_train, datas_teach, n_repeat, error_accuracy, draw_e, data_pooled1, extra={"event.action": "train", "logrite.patterns": patterns, "logrite.datas_train": datas_train, "logrite.datas_teach": datas_teach, "logrite.n_repeat": n_repeat, "logrite.error_accuracy": error_accuracy, "logrite.draw_e": draw_e})
                shape_featuremap1 = np.shape(data_conved1)
                logger.error("train(patterns=%s,datas_train=%s,datas_teach=%s,n_repeat=%s,error_accuracy=%s,draw_e=%s): shape_featuremap1 → %s", patterns, datas_train, datas_teach, n_repeat, error_accuracy, draw_e, shape_featuremap1, extra={"event.action": "train", "logrite.patterns": patterns, "logrite.datas_train": datas_train, "logrite.datas_teach": datas_teach, "logrite.n_repeat": n_repeat, "logrite.error_accuracy": error_accuracy, "logrite.draw_e": draw_e})
                """
                print('  -----original shape   ', np.shape(data_train))
                print('  ---- after convolution  ',np.shape(data_conv1))
                print('  -----after pooling  ',np.shape(data_pooled1))
               """
                data_bp_input = self._expand(data_pooled1)
                logger.error("train(patterns=%s,datas_train=%s,datas_teach=%s,n_repeat=%s,error_accuracy=%s,draw_e=%s): data_bp_input → %s", patterns, datas_train, datas_teach, n_repeat, error_accuracy, draw_e, data_bp_input, extra={"event.action": "train", "logrite.patterns": patterns, "logrite.datas_train": datas_train, "logrite.datas_teach": datas_teach, "logrite.n_repeat": n_repeat, "logrite.error_accuracy": error_accuracy, "logrite.draw_e": draw_e})
                bp_out1 = data_bp_input

                bp_net_j = np.dot(bp_out1, self.vji.T) - self.thre_bp2
                logger.error("train(patterns=%s,datas_train=%s,datas_teach=%s,n_repeat=%s,error_accuracy=%s,draw_e=%s): bp_net_j → %s", patterns, datas_train, datas_teach, n_repeat, error_accuracy, draw_e, bp_net_j, extra={"event.action": "train", "logrite.patterns": patterns, "logrite.datas_train": datas_train, "logrite.datas_teach": datas_teach, "logrite.n_repeat": n_repeat, "logrite.error_accuracy": error_accuracy, "logrite.draw_e": draw_e})
                bp_out2 = self.sig(bp_net_j)
                logger.error("train(patterns=%s,datas_train=%s,datas_teach=%s,n_repeat=%s,error_accuracy=%s,draw_e=%s): bp_out2 → %s", patterns, datas_train, datas_teach, n_repeat, error_accuracy, draw_e, bp_out2, extra={"event.action": "train", "logrite.patterns": patterns, "logrite.datas_train": datas_train, "logrite.datas_teach": datas_teach, "logrite.n_repeat": n_repeat, "logrite.error_accuracy": error_accuracy, "logrite.draw_e": draw_e})
                bp_net_k = np.dot(bp_out2, self.wkj.T) - self.thre_bp3
                logger.error("train(patterns=%s,datas_train=%s,datas_teach=%s,n_repeat=%s,error_accuracy=%s,draw_e=%s): bp_net_k → %s", patterns, datas_train, datas_teach, n_repeat, error_accuracy, draw_e, bp_net_k, extra={"event.action": "train", "logrite.patterns": patterns, "logrite.datas_train": datas_train, "logrite.datas_teach": datas_teach, "logrite.n_repeat": n_repeat, "logrite.error_accuracy": error_accuracy, "logrite.draw_e": draw_e})
                bp_out3 = self.sig(bp_net_k)
                logger.error("train(patterns=%s,datas_train=%s,datas_teach=%s,n_repeat=%s,error_accuracy=%s,draw_e=%s): bp_out3 → %s", patterns, datas_train, datas_teach, n_repeat, error_accuracy, draw_e, bp_out3, extra={"event.action": "train", "logrite.patterns": patterns, "logrite.datas_train": datas_train, "logrite.datas_teach": datas_teach, "logrite.n_repeat": n_repeat, "logrite.error_accuracy": error_accuracy, "logrite.draw_e": draw_e})

                # --------------Model Leaning ------------------------
                # calculate error and gradient---------------
                pd_k_all = np.multiply(
                    (data_teach - bp_out3), np.multiply(bp_out3, (1 - bp_out3))
                )
                pd_j_all = np.multiply(
                    np.dot(pd_k_all, self.wkj), np.multiply(bp_out2, (1 - bp_out2))
                )
                pd_i_all = np.dot(pd_j_all, self.vji)
                logger.error("train(patterns=%s,datas_train=%s,datas_teach=%s,n_repeat=%s,error_accuracy=%s,draw_e=%s): pd_i_all → %s", patterns, datas_train, datas_teach, n_repeat, error_accuracy, draw_e, pd_i_all, extra={"event.action": "train", "logrite.patterns": patterns, "logrite.datas_train": datas_train, "logrite.datas_teach": datas_teach, "logrite.n_repeat": n_repeat, "logrite.error_accuracy": error_accuracy, "logrite.draw_e": draw_e})

                pd_conv1_pooled = pd_i_all / (self.size_pooling1 * self.size_pooling1)
                pd_conv1_pooled = pd_conv1_pooled.T.getA().tolist()
                logger.error("train(patterns=%s,datas_train=%s,datas_teach=%s,n_repeat=%s,error_accuracy=%s,draw_e=%s): pd_conv1_pooled → %s", patterns, datas_train, datas_teach, n_repeat, error_accuracy, draw_e, pd_conv1_pooled, extra={"event.action": "train", "logrite.patterns": patterns, "logrite.datas_train": datas_train, "logrite.datas_teach": datas_teach, "logrite.n_repeat": n_repeat, "logrite.error_accuracy": error_accuracy, "logrite.draw_e": draw_e})
                pd_conv1_all = self._calculate_gradient_from_pool(
                    data_conved1,
                    pd_conv1_pooled,
                    shape_featuremap1[0],
                    shape_featuremap1[1],
                    self.size_pooling1,
                )
                # weight and threshold learning process---------
                # convolution layer
                for k_conv in range(self.conv1[1]):
                    pd_conv_list = self._expand_mat(pd_conv1_all[k_conv])
                    logger.error("train(patterns=%s,datas_train=%s,datas_teach=%s,n_repeat=%s,error_accuracy=%s,draw_e=%s): pd_conv_list → %s", patterns, datas_train, datas_teach, n_repeat, error_accuracy, draw_e, pd_conv_list, extra={"event.action": "train", "logrite.patterns": patterns, "logrite.datas_train": datas_train, "logrite.datas_teach": datas_teach, "logrite.n_repeat": n_repeat, "logrite.error_accuracy": error_accuracy, "logrite.draw_e": draw_e})
                    delta_w = self.rate_weight * np.dot(pd_conv_list, data_focus1)
                    logger.error("train(patterns=%s,datas_train=%s,datas_teach=%s,n_repeat=%s,error_accuracy=%s,draw_e=%s): delta_w → %s", patterns, datas_train, datas_teach, n_repeat, error_accuracy, draw_e, delta_w, extra={"event.action": "train", "logrite.patterns": patterns, "logrite.datas_train": datas_train, "logrite.datas_teach": datas_teach, "logrite.n_repeat": n_repeat, "logrite.error_accuracy": error_accuracy, "logrite.draw_e": draw_e})

                    self.w_conv1[k_conv] = self.w_conv1[k_conv] + delta_w.reshape(
                        (self.conv1[0], self.conv1[0])
                    )

                    self.thre_conv1[k_conv] = (
                        self.thre_conv1[k_conv]
                        - np.sum(pd_conv1_all[k_conv]) * self.rate_thre
                    )
                # all connected layer
                self.wkj = self.wkj + pd_k_all.T * bp_out2 * self.rate_weight
                logger.debug("train(self=%s,patterns=%s,datas_train=%s,datas_teach=%s,n_repeat=%s,error_accuracy=%s,draw_e=%s): self.wkj → %s", self, patterns, datas_train, datas_teach, n_repeat, error_accuracy, draw_e, self.wkj, extra={"event.action": "train", "logrite.patterns": patterns, "logrite.datas_train": datas_train, "logrite.datas_teach": datas_teach, "logrite.n_repeat": n_repeat, "logrite.error_accuracy": error_accuracy, "logrite.draw_e": draw_e})
                self.vji = self.vji + pd_j_all.T * bp_out1 * self.rate_weight
                logger.debug("train(self=%s,patterns=%s,datas_train=%s,datas_teach=%s,n_repeat=%s,error_accuracy=%s,draw_e=%s): self.vji → %s", self, patterns, datas_train, datas_teach, n_repeat, error_accuracy, draw_e, self.vji, extra={"event.action": "train", "logrite.patterns": patterns, "logrite.datas_train": datas_train, "logrite.datas_teach": datas_teach, "logrite.n_repeat": n_repeat, "logrite.error_accuracy": error_accuracy, "logrite.draw_e": draw_e})
                self.thre_bp3 = self.thre_bp3 - pd_k_all * self.rate_thre
                logger.debug("train(self=%s,patterns=%s,datas_train=%s,datas_teach=%s,n_repeat=%s,error_accuracy=%s,draw_e=%s): self.thre_bp3 → %s", self, patterns, datas_train, datas_teach, n_repeat, error_accuracy, draw_e, self.thre_bp3, extra={"event.action": "train", "logrite.patterns": patterns, "logrite.datas_train": datas_train, "logrite.datas_teach": datas_teach, "logrite.n_repeat": n_repeat, "logrite.error_accuracy": error_accuracy, "logrite.draw_e": draw_e})
                self.thre_bp2 = self.thre_bp2 - pd_j_all * self.rate_thre
                logger.debug("train(self=%s,patterns=%s,datas_train=%s,datas_teach=%s,n_repeat=%s,error_accuracy=%s,draw_e=%s): self.thre_bp2 → %s", self, patterns, datas_train, datas_teach, n_repeat, error_accuracy, draw_e, self.thre_bp2, extra={"event.action": "train", "logrite.patterns": patterns, "logrite.datas_train": datas_train, "logrite.datas_teach": datas_teach, "logrite.n_repeat": n_repeat, "logrite.error_accuracy": error_accuracy, "logrite.draw_e": draw_e})
                # calculate the sum error of all single image
                errors = np.sum(abs(data_teach - bp_out3))
                logger.error("train(patterns=%s,datas_train=%s,datas_teach=%s,n_repeat=%s,error_accuracy=%s,draw_e=%s): errors → %s", patterns, datas_train, datas_teach, n_repeat, error_accuracy, draw_e, errors, extra={"event.action": "train", "logrite.patterns": patterns, "logrite.datas_train": datas_train, "logrite.datas_teach": datas_teach, "logrite.n_repeat": n_repeat, "logrite.error_accuracy": error_accuracy, "logrite.draw_e": draw_e})
                error_count += errors
                # print('   ----Teach      ',data_teach)
                # print('   ----BP_output  ',bp_out3)
            rp = rp + 1
            mse = error_count / patterns
            all_mse.append(mse)
            logger.warning("<<< Exiting train(patterns=%s,datas_train=%s,datas_teach=%s,n_repeat=%s,error_accuracy=%s,draw_e=%s)", patterns, datas_train, datas_teach, n_repeat, error_accuracy, draw_e, extra={"event.action": "train", "logrite.patterns": patterns, "logrite.datas_train": datas_train, "logrite.datas_teach": datas_teach, "logrite.n_repeat": n_repeat, "logrite.error_accuracy": error_accuracy, "logrite.draw_e": draw_e})

        def draw_error():
            logger.error(">>> Entering draw_error()", extra={"event.action": "draw_error"})
            yplot = [error_accuracy for i in range(int(n_repeat * 1.2))]
            logger.error("draw_error(): yplot → %s", yplot, extra={"event.action": "draw_error"})
            plt.plot(all_mse, "+-")
            plt.plot(yplot, "r--")
            plt.xlabel("Learning Times")
            plt.ylabel("All_mse")
            plt.grid(True, alpha=0.5)
            plt.show()
            logger.warning("<<< Exiting draw_error()", extra={"event.action": "draw_error"})

        print("------------------Training Complete---------------------")
        print((" - - Training epoch: ", rp, f"     - - Mse: {mse:.6f}"))
        if draw_e:
            draw_error()
        return mse

    def predict(self, datas_test):
        logger.error(">>> Entering predict(datas_test=%s)", datas_test, extra={"event.action": "predict", "logrite.datas_test": datas_test})
        # model predict
        produce_out = []
        print("-------------------Start Testing-------------------------")
        print((" - - Shape: Test_Data  ", np.shape(datas_test)))
        for p in range(len(datas_test)):
            data_test = np.asmatrix(datas_test[p])
            logger.error("predict(datas_test=%s): data_test → %s", datas_test, data_test, extra={"event.action": "predict", "logrite.datas_test": datas_test})
            _data_focus1, data_conved1 = self.convolute(
                data_test,
                self.conv1,
                self.w_conv1,
                self.thre_conv1,
                conv_step=self.step_conv1,
            )
            data_pooled1 = self.pooling(data_conved1, self.size_pooling1)
            logger.error("predict(datas_test=%s): data_pooled1 → %s", datas_test, data_pooled1, extra={"event.action": "predict", "logrite.datas_test": datas_test})
            data_bp_input = self._expand(data_pooled1)
            logger.error("predict(datas_test=%s): data_bp_input → %s", datas_test, data_bp_input, extra={"event.action": "predict", "logrite.datas_test": datas_test})

            bp_out1 = data_bp_input
            bp_net_j = bp_out1 * self.vji.T - self.thre_bp2
            bp_out2 = self.sig(bp_net_j)
            logger.error("predict(datas_test=%s): bp_out2 → %s", datas_test, bp_out2, extra={"event.action": "predict", "logrite.datas_test": datas_test})
            bp_net_k = bp_out2 * self.wkj.T - self.thre_bp3
            bp_out3 = self.sig(bp_net_k)
            logger.error("predict(datas_test=%s): bp_out3 → %s", datas_test, bp_out3, extra={"event.action": "predict", "logrite.datas_test": datas_test})
            produce_out.extend(bp_out3.getA().tolist())
        res = [list(map(self.do_round, each)) for each in produce_out]
        logger.error("predict(datas_test=%s): res → %s", datas_test, res, extra={"event.action": "predict", "logrite.datas_test": datas_test})
        logger.warning("<<< Exiting predict(datas_test=%s)", datas_test, extra={"event.action": "predict", "logrite.datas_test": datas_test})
        return np.asarray(res)

    def convolution(self, data):
        logger.error(">>> Entering convolution(data=%s)", data, extra={"event.action": "convolution"})
        # return the data of image after convoluting process so we can check it out
        data_test = np.asmatrix(data)
        logger.error("convolution(data=%s): data_test → %s", data, data_test, extra={"event.action": "convolution"})
        _data_focus1, data_conved1 = self.convolute(
            data_test,
            self.conv1,
            self.w_conv1,
            self.thre_conv1,
            conv_step=self.step_conv1,
        )
        data_pooled1 = self.pooling(data_conved1, self.size_pooling1)
        logger.error("convolution(data=%s): data_pooled1 → %s", data, data_pooled1, extra={"event.action": "convolution"})

        logger.warning("<<< Exiting convolution(data=%s)", data, extra={"event.action": "convolution"})
        return data_conved1, data_pooled1


if __name__ == "__main__":
    """
    I will put the example in another file
    """
