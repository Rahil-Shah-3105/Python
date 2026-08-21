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
        """
        :param conv1_get: [a,c,d], size, number, step of convolution kernel
        :param size_p1: pooling size
        :param bp_num1: units number of flatten layer
        :param bp_num2: units number of hidden layer
        :param bp_num3: units number of output layer
        :param rate_w: rate of weight learning
        :param rate_t: rate of threshold learning
        """
        self.num_bp1 = bp_num1
        self.num_bp2 = bp_num2
        self.num_bp3 = bp_num3
        self.conv1 = conv1_get[:2]
        self.step_conv1 = conv1_get[2]
        self.size_pooling1 = size_p1
        self.rate_weight = rate_w
        self.rate_thre = rate_t
        rng = np.random.default_rng()
        self.w_conv1 = [
            np.asmatrix(-1 * rng.random((self.conv1[0], self.conv1[0])) + 0.5)
            for i in range(self.conv1[1])
        ]
        self.wkj = np.asmatrix(-1 * rng.random((self.num_bp3, self.num_bp2)) + 0.5)
        self.vji = np.asmatrix(-1 * rng.random((self.num_bp2, self.num_bp1)) + 0.5)
        self.thre_conv1 = -2 * rng.random(self.conv1[1]) + 1
        self.thre_bp2 = -2 * rng.random(self.num_bp2) + 1
        self.thre_bp3 = -2 * rng.random(self.num_bp3) + 1

    def save_model(self, save_path):
        logger.debug(">>> Entering save_model(save_path=%s)", save_path)
        logger.debug("save_model(self=%s,save_path=%s): model_dic → %s", self, save_path, model_dic)
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
        logger.debug("<<< Exiting save_model(save_path=%s)", save_path)

    @classmethod
    def read_model(cls, model_path):
        logger.debug(">>> Entering read_model(model_path=%s)", model_path)
        logger.debug("read_model(model_path=%s): model_dic → %s", model_path, model_dic)
        logger.debug("read_model(cls=%s,model_path=%s): model_dic → %s", cls, model_path, model_dic)
        logger.debug("read_model(model_path=%s): conv_get → %s", model_path, conv_get)
        logger.debug("read_model(cls=%s,model_path=%s): conv_get → %s", cls, model_path, conv_get)
        logger.debug("read_model(model_path=%s): size_p1 → %s", model_path, size_p1)
        logger.debug("read_model(cls=%s,model_path=%s): size_p1 → %s", cls, model_path, size_p1)
        logger.debug("read_model(cls=%s,model_path=%s): bp1 → %s", cls, model_path, bp1)
        logger.debug("read_model(model_path=%s): bp1 → %s", model_path, bp1)
        logger.debug("read_model(cls=%s,model_path=%s): bp2 → %s", cls, model_path, bp2)
        logger.debug("read_model(model_path=%s): bp2 → %s", model_path, bp2)
        logger.debug("read_model(cls=%s,model_path=%s): bp3 → %s", cls, model_path, bp3)
        logger.debug("read_model(model_path=%s): bp3 → %s", model_path, bp3)
        logger.debug("read_model(cls=%s,model_path=%s): r_w → %s", cls, model_path, r_w)
        logger.debug("read_model(model_path=%s): r_w → %s", model_path, r_w)
        logger.debug("read_model(cls=%s,model_path=%s): r_t → %s", cls, model_path, r_t)
        logger.debug("read_model(model_path=%s): r_t → %s", model_path, r_t)
        logger.debug("read_model(cls=%s,model_path=%s): conv_ins → %s", cls, model_path, conv_ins)
        logger.debug("read_model(model_path=%s): conv_ins → %s", model_path, conv_ins)
        # read saved model
        with open(model_path, "rb") as f:
            logger.error("Exception in read_model(model_path=%s)", model_path, exc_info=True)
            model_dic = pickle.load(f)  # noqa: S301

        conv_get = model_dic.get("conv1")
        conv_get.append(model_dic.get("step_conv1"))
        size_p1 = model_dic.get("size_pooling1")
        bp1 = model_dic.get("num_bp1")
        bp2 = model_dic.get("num_bp2")
        bp3 = model_dic.get("num_bp3")
        r_w = model_dic.get("rate_weight")
        r_t = model_dic.get("rate_thre")
        # create model instance
        conv_ins = CNN(conv_get, size_p1, bp1, bp2, bp3, r_w, r_t)
        # modify model parameter
        conv_ins.w_conv1 = model_dic.get("w_conv1")
        conv_ins.wkj = model_dic.get("wkj")
        conv_ins.vji = model_dic.get("vji")
        conv_ins.thre_conv1 = model_dic.get("thre_conv1")
        conv_ins.thre_bp2 = model_dic.get("thre_bp2")
        conv_ins.thre_bp3 = model_dic.get("thre_bp3")
        logger.debug("<<< Exiting read_model(model_path=%s)", model_path)
        return conv_ins

    def sig(self, x):
        logger.debug(">>> Entering sig(x=%s)", x)
        logger.debug("<<< Exiting sig(x=%s)", x)
        return 1 / (1 + np.exp(-1 * x))

    def do_round(self, x):
        logger.debug(">>> Entering do_round(x=%s)", x)
        logger.debug("<<< Exiting do_round(x=%s)", x)
        return round(x, 3)

    def convolute(self, data, convs, w_convs, thre_convs, conv_step):
        logger.debug(">>> Entering convolute(data=%s,convs=%s,w_convs=%s,thre_convs=%s,conv_step=%s)", data, convs, w_convs, thre_convs, conv_step)
        logger.debug("convolute(data=%s,convs=%s,w_convs=%s,thre_convs=%s,conv_step=%s): size_data → %s", data, convs, w_convs, thre_convs, conv_step, size_data)
        logger.debug("convolute(self=%s,data=%s,convs=%s,w_convs=%s,thre_convs=%s,conv_step=%s): size_conv → %s", self, data, convs, w_convs, thre_convs, conv_step, size_conv)
        logger.debug("convolute(self=%s,data=%s,convs=%s,w_convs=%s,thre_convs=%s,conv_step=%s): num_conv → %s", self, data, convs, w_convs, thre_convs, conv_step, num_conv)
        logger.debug("convolute(self=%s,data=%s,convs=%s,w_convs=%s,thre_convs=%s,conv_step=%s): size_data → %s", self, data, convs, w_convs, thre_convs, conv_step, size_data)
        logger.debug("convolute(data=%s,convs=%s,w_convs=%s,thre_convs=%s,conv_step=%s): data_focus → %s", data, convs, w_convs, thre_convs, conv_step, data_focus)
        logger.debug("convolute(self=%s,data=%s,convs=%s,w_convs=%s,thre_convs=%s,conv_step=%s): data_focus → %s", self, data, convs, w_convs, thre_convs, conv_step, data_focus)
        # convolution process
        size_conv = convs[0]
        num_conv = convs[1]
        size_data = np.shape(data)[0]
        # get the data slice of original image data, data_focus
        data_focus = []
        for i_focus in range(0, size_data - size_conv + 1, conv_step):
            for j_focus in range(0, size_data - size_conv + 1, conv_step):
                focus = data[
                    i_focus : i_focus + size_conv, j_focus : j_focus + size_conv
                ]
                data_focus.append(focus)
                logger.debug("convolute(data=%s,convs=%s,w_convs=%s,thre_convs=%s,conv_step=%s): size_feature_map → %s", data, convs, w_convs, thre_convs, conv_step, size_feature_map)
                logger.debug("convolute(data=%s,convs=%s,w_convs=%s,thre_convs=%s,conv_step=%s): data_featuremap → %s", data, convs, w_convs, thre_convs, conv_step, data_featuremap)
                logger.debug("convolute(self=%s,data=%s,convs=%s,w_convs=%s,thre_convs=%s,conv_step=%s): data_featuremap → %s", self, data, convs, w_convs, thre_convs, conv_step, data_featuremap)
                logger.debug("convolute(self=%s,data=%s,convs=%s,w_convs=%s,thre_convs=%s,conv_step=%s): size_feature_map → %s", self, data, convs, w_convs, thre_convs, conv_step, size_feature_map)
                logger.debug("convolute(data=%s,convs=%s,w_convs=%s,thre_convs=%s,conv_step=%s): featuremap → %s", data, convs, w_convs, thre_convs, conv_step, featuremap)
                logger.debug("convolute(self=%s,data=%s,convs=%s,w_convs=%s,thre_convs=%s,conv_step=%s): featuremap → %s", self, data, convs, w_convs, thre_convs, conv_step, featuremap)
                logger.debug("convolute(self=%s,data=%s,convs=%s,w_convs=%s,thre_convs=%s,conv_step=%s): net_focus → %s", self, data, convs, w_convs, thre_convs, conv_step, net_focus)
        # calculate the feature map of every single kernel, and saved as list of matrix
        data_featuremap = []
        size_feature_map = int((size_data - size_conv) / conv_step + 1)
        for i_map in range(num_conv):
            featuremap = []
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
        logger.debug("convolute(self=%s,data=%s,convs=%s,w_convs=%s,thre_convs=%s,conv_step=%s): focus1_list → %s", self, data, convs, w_convs, thre_convs, conv_step, focus1_list)
        for each_focus in data_focus:
            focus1_list.extend(self.Expand_Mat(each_focus))
        focus_list = np.asarray(focus1_list)
        logger.debug("convolute(self=%s,data=%s,convs=%s,w_convs=%s,thre_convs=%s,conv_step=%s): focus_list → %s", self, data, convs, w_convs, thre_convs, conv_step, focus_list)
        logger.debug("convolute(data=%s,convs=%s,w_convs=%s,thre_convs=%s,conv_step=%s): focus_list → %s", data, convs, w_convs, thre_convs, conv_step, focus_list)
        logger.debug("<<< Exiting convolute(data=%s,convs=%s,w_convs=%s,thre_convs=%s,conv_step=%s)", data, convs, w_convs, thre_convs, conv_step)
        return focus_list, data_featuremap

    def pooling(self, featuremaps, size_pooling, pooling_type="average_pool"):
        logger.debug(">>> Entering pooling(featuremaps=%s,size_pooling=%s,pooling_type=%s)", featuremaps, size_pooling, pooling_type)
        logger.debug("pooling(featuremaps=%s,size_pooling=%s,pooling_type=%s): size_map → %s", featuremaps, size_pooling, pooling_type, size_map)
        logger.debug("pooling(self=%s,featuremaps=%s,size_pooling=%s,pooling_type=%s): size_map → %s", self, featuremaps, size_pooling, pooling_type, size_map)
        logger.debug("pooling(self=%s,featuremaps=%s,size_pooling=%s,pooling_type=%s): size_pooled → %s", self, featuremaps, size_pooling, pooling_type, size_pooled)
        logger.debug("pooling(featuremaps=%s,size_pooling=%s,pooling_type=%s): size_pooled → %s", featuremaps, size_pooling, pooling_type, size_pooled)
        logger.debug("pooling(self=%s,featuremaps=%s,size_pooling=%s,pooling_type=%s): featuremap_pooled → %s", self, featuremaps, size_pooling, pooling_type, featuremap_pooled)
        logger.debug("pooling(self=%s,featuremaps=%s,size_pooling=%s,pooling_type=%s): feature_map → %s", self, featuremaps, size_pooling, pooling_type, feature_map)
        logger.debug("pooling(self=%s,featuremaps=%s,size_pooling=%s,pooling_type=%s): map_pooled → %s", self, featuremaps, size_pooling, pooling_type, map_pooled)
        logger.debug("pooling(featuremaps=%s,size_pooling=%s,pooling_type=%s): map_pooled → %s", featuremaps, size_pooling, pooling_type, map_pooled)
        logger.debug("pooling(self=%s,featuremaps=%s,size_pooling=%s,pooling_type=%s): focus → %s", self, featuremaps, size_pooling, pooling_type, focus)
        # pooling process
        size_map = len(featuremaps[0])
        size_pooled = int(size_map / size_pooling)
        featuremap_pooled = []
        for i_map in range(len(featuremaps)):
            feature_map = featuremaps[i_map]
            map_pooled = []
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
        logger.debug("<<< Exiting pooling(featuremaps=%s,size_pooling=%s,pooling_type=%s)", featuremaps, size_pooling, pooling_type)
        return featuremap_pooled

    def _expand(self, data):
        logger.debug(">>> Entering _expand(data=%s)", data)
        logger.debug("_expand(data=%s): data_expanded → %s", data, data_expanded)
        logger.debug("_expand(self=%s,data=%s): data_expanded → %s", self, data, data_expanded)
        logger.debug("_expand(data=%s): shapes → %s", data, shapes)
        logger.debug("_expand(self=%s,data=%s): shapes → %s", self, data, shapes)
        logger.debug("_expand(self=%s,data=%s): data_listed → %s", self, data, data_listed)
        logger.debug("_expand(data=%s): data_listed → %s", data, data_listed)
        # expanding three dimension data to one dimension list
        data_expanded = []
        for i in range(len(data)):
            shapes = np.shape(data[i])
            data_listed = data[i].reshape(1, shapes[0] * shapes[1])
            data_listed = data_listed.getA().tolist()[0]
            data_expanded.extend(data_listed)
        data_expanded = np.asarray(data_expanded)
        logger.debug("<<< Exiting _expand(data=%s)", data)
        return data_expanded

    def _expand_mat(self, data_mat):
        logger.debug(">>> Entering _expand_mat(data_mat=%s)", data_mat)
        logger.debug("_expand_mat(data_mat=%s): shapes → %s", data_mat, shapes)
        logger.debug("_expand_mat(data_mat=%s): data_mat → %s", data_mat, data_mat)
        logger.debug("_expand_mat(self=%s,data_mat=%s): shapes → %s", self, data_mat, shapes)
        logger.debug("_expand_mat(self=%s,data_mat=%s): data_expanded → %s", self, data_mat, data_expanded)
        logger.debug("_expand_mat(data_mat=%s): data_expanded → %s", data_mat, data_expanded)
        # expanding matrix to one dimension list
        data_mat = np.asarray(data_mat)
        shapes = np.shape(data_mat)
        data_expanded = data_mat.reshape(1, shapes[0] * shapes[1])
        logger.debug("<<< Exiting _expand_mat(data_mat=%s)", data_mat)
        return data_expanded

    def _calculate_gradient_from_pool(
        self, out_map, pd_pool, num_map, size_map, size_pooling
    ):
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
        return pd_all

    def train(
        self, patterns, datas_train, datas_teach, n_repeat, error_accuracy, draw_e=bool
    ):
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
                data_teach = np.asarray(datas_teach[p])
                data_focus1, data_conved1 = self.convolute(
                    data_train,
                    self.conv1,
                    self.w_conv1,
                    self.thre_conv1,
                    conv_step=self.step_conv1,
                )
                data_pooled1 = self.pooling(data_conved1, self.size_pooling1)
                shape_featuremap1 = np.shape(data_conved1)
                """
                print('  -----original shape   ', np.shape(data_train))
                print('  ---- after convolution  ',np.shape(data_conv1))
                print('  -----after pooling  ',np.shape(data_pooled1))
               """
                data_bp_input = self._expand(data_pooled1)
                bp_out1 = data_bp_input

                bp_net_j = np.dot(bp_out1, self.vji.T) - self.thre_bp2
                bp_out2 = self.sig(bp_net_j)
                bp_net_k = np.dot(bp_out2, self.wkj.T) - self.thre_bp3
                bp_out3 = self.sig(bp_net_k)

                # --------------Model Leaning ------------------------
                # calculate error and gradient---------------
                pd_k_all = np.multiply(
                    (data_teach - bp_out3), np.multiply(bp_out3, (1 - bp_out3))
                )
                pd_j_all = np.multiply(
                    np.dot(pd_k_all, self.wkj), np.multiply(bp_out2, (1 - bp_out2))
                )
                pd_i_all = np.dot(pd_j_all, self.vji)

                pd_conv1_pooled = pd_i_all / (self.size_pooling1 * self.size_pooling1)
                pd_conv1_pooled = pd_conv1_pooled.T.getA().tolist()
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
                    delta_w = self.rate_weight * np.dot(pd_conv_list, data_focus1)

                    self.w_conv1[k_conv] = self.w_conv1[k_conv] + delta_w.reshape(
                        (self.conv1[0], self.conv1[0])
                    )

                    self.thre_conv1[k_conv] = (
                        self.thre_conv1[k_conv]
                        - np.sum(pd_conv1_all[k_conv]) * self.rate_thre
                    )
                # all connected layer
                self.wkj = self.wkj + pd_k_all.T * bp_out2 * self.rate_weight
                self.vji = self.vji + pd_j_all.T * bp_out1 * self.rate_weight
                self.thre_bp3 = self.thre_bp3 - pd_k_all * self.rate_thre
                self.thre_bp2 = self.thre_bp2 - pd_j_all * self.rate_thre
                # calculate the sum error of all single image
                errors = np.sum(abs(data_teach - bp_out3))
                error_count += errors
                # print('   ----Teach      ',data_teach)
                # print('   ----BP_output  ',bp_out3)
            rp = rp + 1
            mse = error_count / patterns
            all_mse.append(mse)

        def draw_error():
            logger.debug(">>> Entering draw_error()")
            yplot = [error_accuracy for i in range(int(n_repeat * 1.2))]
            logger.debug("draw_error(): yplot → %s", yplot)
            plt.plot(all_mse, "+-")
            plt.plot(yplot, "r--")
            plt.xlabel("Learning Times")
            plt.ylabel("All_mse")
            plt.grid(True, alpha=0.5)
            plt.show()
            logger.debug("<<< Exiting draw_error()")

        print("------------------Training Complete---------------------")
        print((" - - Training epoch: ", rp, f"     - - Mse: {mse:.6f}"))
        if draw_e:
            draw_error()
        return mse

    def predict(self, datas_test):
        logger.debug(">>> Entering predict(datas_test=%s)", datas_test)
        logger.debug("predict(datas_test=%s): bp_out3 → %s", datas_test, bp_out3)
        logger.debug("predict(self=%s,datas_test=%s): produce_out → %s", self, datas_test, produce_out)
        logger.debug("predict(datas_test=%s): data_bp_input → %s", datas_test, data_bp_input)
        logger.debug("predict(self=%s,datas_test=%s): conv_step → %s", self, datas_test, conv_step)
        logger.debug("predict(datas_test=%s): data_test → %s", datas_test, data_test)
        logger.debug("predict(self=%s,datas_test=%s): data_test → %s", self, datas_test, data_test)
        # model predict
        produce_out = []
        print("-------------------Start Testing-------------------------")
        print((" - - Shape: Test_Data  ", np.shape(datas_test)))
        for p in range(len(datas_test)):
            data_test = np.asmatrix(datas_test[p])
            _data_focus1, data_conved1 = self.convolute(
                data_test,
                self.conv1,
                self.w_conv1,
                self.thre_conv1,
                conv_step=self.step_conv1,
            )
            logger.debug("predict(datas_test=%s): res → %s", datas_test, res)
            logger.debug("predict(self=%s,datas_test=%s): res → %s", self, datas_test, res)
            data_pooled1 = self.pooling(data_conved1, self.size_pooling1)
            logger.debug("predict(self=%s,datas_test=%s): data_pooled1 → %s", self, datas_test, data_pooled1)
            logger.debug("predict(datas_test=%s): data_pooled1 → %s", datas_test, data_pooled1)
            data_bp_input = self._expand(data_pooled1)
            logger.debug("predict(self=%s,datas_test=%s): data_bp_input → %s", self, datas_test, data_bp_input)

            bp_out1 = data_bp_input
            logger.debug("predict(self=%s,datas_test=%s): bp_out1 → %s", self, datas_test, bp_out1)
            bp_net_j = bp_out1 * self.vji.T - self.thre_bp2
            logger.debug("predict(self=%s,datas_test=%s): bp_net_j → %s", self, datas_test, bp_net_j)
            bp_out2 = self.sig(bp_net_j)
            logger.debug("predict(self=%s,datas_test=%s): bp_out2 → %s", self, datas_test, bp_out2)
            logger.debug("predict(datas_test=%s): bp_out2 → %s", datas_test, bp_out2)
            bp_net_k = bp_out2 * self.wkj.T - self.thre_bp3
            logger.debug("predict(self=%s,datas_test=%s): bp_net_k → %s", self, datas_test, bp_net_k)
            bp_out3 = self.sig(bp_net_k)
            logger.debug("predict(self=%s,datas_test=%s): bp_out3 → %s", self, datas_test, bp_out3)
            produce_out.extend(bp_out3.getA().tolist())
        res = [list(map(self.do_round, each)) for each in produce_out]
        logger.debug("<<< Exiting predict(datas_test=%s)", datas_test)
        logger.debug("convolution(self=%s,data=%s): conv_step → %s", self, data, conv_step)
        logger.debug("convolution(self=%s,data=%s): data_pooled1 → %s", self, data, data_pooled1)
        logger.debug("convolution(data=%s): data_pooled1 → %s", data, data_pooled1)
        return np.asarray(res)

    def convolution(self, data):
        logger.debug(">>> Entering convolution(data=%s)", data)
        logger.debug("convolution(data=%s): data_test → %s", data, data_test)
        logger.debug("convolution(self=%s,data=%s): data_test → %s", self, data, data_test)
        # return the data of image after convoluting process so we can check it out
        data_test = np.asmatrix(data)
        _data_focus1, data_conved1 = self.convolute(
            data_test,
            self.conv1,
            self.w_conv1,
            self.thre_conv1,
            conv_step=self.step_conv1,
        )
        data_pooled1 = self.pooling(data_conved1, self.size_pooling1)

        logger.debug("<<< Exiting convolution(data=%s)", data)
        return data_conved1, data_pooled1


if __name__ == "__main__":
    """
    I will put the example in another file
    """
