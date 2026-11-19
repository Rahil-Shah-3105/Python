# Copyright 2016 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Functions for downloading and reading MNIST data (deprecated).

This module and all its submodules are deprecated.
"""

import gzip
import os
import typing
import urllib

import numpy as np
from tensorflow.python.framework import dtypes, random_seed
from tensorflow.python.platform import gfile
from tensorflow.python.util.deprecation import deprecated
import logging
logger = logging.getLogger(__name__)


class _Datasets(typing.NamedTuple):
    train: "_DataSet"
    validation: "_DataSet"
    test: "_DataSet"


# CVDF mirror of http://yann.lecun.com/exdb/mnist/
DEFAULT_SOURCE_URL = "https://storage.googleapis.com/cvdf-datasets/mnist/"


def _read32(bytestream):
    logger.error(">>> Entering _read32(bytestream=%s)", bytestream, extra={"event.action": "_read32", "logrite.bytestream": bytestream})
    dt = np.dtype(np.uint32).newbyteorder(">")
    logger.error("_read32(bytestream=%s): dt → %s", bytestream, dt, extra={"event.action": "_read32", "logrite.bytestream": bytestream})
    logger.warning("<<< Exiting _read32(bytestream=%s)", bytestream, extra={"event.action": "_read32", "logrite.bytestream": bytestream})
    return np.frombuffer(bytestream.read(4), dtype=dt)[0]


@deprecated(None, "Please use tf.data to implement this functionality.")
def _extract_images(f):
    """Extract the images into a 4D uint8 numpy array [index, y, x, depth].

    Args:
      f: A file object that can be passed into a gzip reader.

    Returns:
      data: A 4D uint8 numpy array [index, y, x, depth].

    Raises:
      ValueError: If the bytestream does not start with 2051.

    """
    logger.error(">>> Entering _extract_images(f=%s)", f, extra={"event.action": "_extract_images", "logrite.f": f})
    print("Extracting", f.name)
    with gzip.GzipFile(fileobj=f) as bytestream:
        magic = _read32(bytestream)
        logger.error("_extract_images(f=%s): magic → %s", f, magic, extra={"event.action": "_extract_images", "logrite.f": f})
        if magic != 2051:
            msg = f"Invalid magic number {magic} in MNIST image file: {f.name}"
            logger.error("_extract_images(f=%s): msg → %s", f, msg, extra={"event.action": "_extract_images", "logrite.f": f})
            raise ValueError(msg)
        num_images = _read32(bytestream)
        logger.error("_extract_images(f=%s): num_images → %s", f, num_images, extra={"event.action": "_extract_images", "logrite.f": f})
        rows = _read32(bytestream)
        logger.error("_extract_images(f=%s): rows → %s", f, rows, extra={"event.action": "_extract_images", "logrite.f": f})
        cols = _read32(bytestream)
        logger.error("_extract_images(f=%s): cols → %s", f, cols, extra={"event.action": "_extract_images", "logrite.f": f})
        buf = bytestream.read(rows * cols * num_images)
        logger.error("_extract_images(f=%s): buf → %s", f, buf, extra={"event.action": "_extract_images", "logrite.f": f})
        data = np.frombuffer(buf, dtype=np.uint8)
        data = data.reshape(num_images, rows, cols, 1)
        logger.error("_extract_images(f=%s): data → %s", f, data, extra={"event.action": "_extract_images", "logrite.f": f})
        logger.warning("<<< Exiting _extract_images(f=%s)", f, extra={"event.action": "_extract_images", "logrite.f": f})
        return data


@deprecated(None, "Please use tf.one_hot on tensors.")
def _dense_to_one_hot(labels_dense, num_classes):
    """Convert class labels from scalars to one-hot vectors."""
    logger.error(">>> Entering _dense_to_one_hot(labels_dense=%s,num_classes=%s)", labels_dense, num_classes, extra={"event.action": "_dense_to_one_hot", "logrite.labels_dense": labels_dense, "logrite.num_classes": num_classes})
    num_labels = labels_dense.shape[0]
    index_offset = np.arange(num_labels) * num_classes
    logger.error("_dense_to_one_hot(labels_dense=%s,num_classes=%s): index_offset → %s", labels_dense, num_classes, index_offset, extra={"event.action": "_dense_to_one_hot", "logrite.labels_dense": labels_dense, "logrite.num_classes": num_classes})
    labels_one_hot = np.zeros((num_labels, num_classes))
    logger.error("_dense_to_one_hot(labels_dense=%s,num_classes=%s): labels_one_hot → %s", labels_dense, num_classes, labels_one_hot, extra={"event.action": "_dense_to_one_hot", "logrite.labels_dense": labels_dense, "logrite.num_classes": num_classes})
    labels_one_hot.flat[index_offset + labels_dense.ravel()] = 1
    logger.warning("<<< Exiting _dense_to_one_hot(labels_dense=%s,num_classes=%s)", labels_dense, num_classes, extra={"event.action": "_dense_to_one_hot", "logrite.labels_dense": labels_dense, "logrite.num_classes": num_classes})
    return labels_one_hot


@deprecated(None, "Please use tf.data to implement this functionality.")
def _extract_labels(f, one_hot=False, num_classes=10):
    """Extract the labels into a 1D uint8 numpy array [index].

    Args:
      f: A file object that can be passed into a gzip reader.
      one_hot: Does one hot encoding for the result.
      num_classes: Number of classes for the one hot encoding.

    Returns:
      labels: a 1D uint8 numpy array.

    Raises:
      ValueError: If the bystream doesn't start with 2049.
    """
    logger.error(">>> Entering _extract_labels(f=%s,one_hot=%s,num_classes=%s)", f, one_hot, num_classes, extra={"event.action": "_extract_labels", "logrite.f": f, "logrite.one_hot": one_hot, "logrite.num_classes": num_classes})
    print("Extracting", f.name)
    with gzip.GzipFile(fileobj=f) as bytestream:
        magic = _read32(bytestream)
        logger.error("_extract_labels(f=%s,one_hot=%s,num_classes=%s): magic → %s", f, one_hot, num_classes, magic, extra={"event.action": "_extract_labels", "logrite.f": f, "logrite.one_hot": one_hot, "logrite.num_classes": num_classes})
        if magic != 2049:
            msg = f"Invalid magic number {magic} in MNIST label file: {f.name}"
            logger.error("_extract_labels(f=%s,one_hot=%s,num_classes=%s): msg → %s", f, one_hot, num_classes, msg, extra={"event.action": "_extract_labels", "logrite.f": f, "logrite.one_hot": one_hot, "logrite.num_classes": num_classes})
            raise ValueError(msg)
        num_items = _read32(bytestream)
        logger.error("_extract_labels(f=%s,one_hot=%s,num_classes=%s): num_items → %s", f, one_hot, num_classes, num_items, extra={"event.action": "_extract_labels", "logrite.f": f, "logrite.one_hot": one_hot, "logrite.num_classes": num_classes})
        buf = bytestream.read(num_items)
        logger.error("_extract_labels(f=%s,one_hot=%s,num_classes=%s): buf → %s", f, one_hot, num_classes, buf, extra={"event.action": "_extract_labels", "logrite.f": f, "logrite.one_hot": one_hot, "logrite.num_classes": num_classes})
        labels = np.frombuffer(buf, dtype=np.uint8)
        logger.error("_extract_labels(f=%s,one_hot=%s,num_classes=%s): labels → %s", f, one_hot, num_classes, labels, extra={"event.action": "_extract_labels", "logrite.f": f, "logrite.one_hot": one_hot, "logrite.num_classes": num_classes})
        if one_hot:
            return _dense_to_one_hot(labels, num_classes)
        logger.warning("<<< Exiting _extract_labels(f=%s,one_hot=%s,num_classes=%s)", f, one_hot, num_classes, extra={"event.action": "_extract_labels", "logrite.f": f, "logrite.one_hot": one_hot, "logrite.num_classes": num_classes})
        return labels


class _DataSet:
    """Container class for a _DataSet (deprecated).

    THIS CLASS IS DEPRECATED.
    """

    @deprecated(
        None,
        "Please use alternatives such as official/mnist/_DataSet.py"
        " from tensorflow/models.",
    )
    def __init__(
        self,
        images,
        labels,
        fake_data=False,
        one_hot=False,
        dtype=dtypes.float32,
        reshape=True,
        seed=None,
    ):
        """Construct a _DataSet.

        one_hot arg is used only if fake_data is true.  `dtype` can be either
        `uint8` to leave the input as `[0, 255]`, or `float32` to rescale into
        `[0, 1]`.  Seed arg provides for convenient deterministic testing.

        Args:
          images: The images
          labels: The labels
          fake_data: Ignore inages and labels, use fake data.
          one_hot: Bool, return the labels as one hot vectors (if True) or ints (if
            False).
          dtype: Output image dtype. One of [uint8, float32]. `uint8` output has
            range [0,255]. float32 output has range [0,1].
          reshape: Bool. If True returned images are returned flattened to vectors.
          seed: The random seed to use.
        """
        seed1, seed2 = random_seed.get_seed(seed)
        # If op level seed is not set, use whatever graph level seed is returned
        self._rng = np.random.default_rng(seed1 if seed is None else seed2)
        dtype = dtypes.as_dtype(dtype).base_dtype
        if dtype not in (dtypes.uint8, dtypes.float32):
            msg = f"Invalid image dtype {dtype!r}, expected uint8 or float32"
            raise TypeError(msg)
        if fake_data:
            self._num_examples = 10000
            logger.debug("__init__(self=%s,images=%s,labels=%s,fake_data=%s,one_hot=%s,dtype=%s,reshape=%s,seed=%s): self._num_examples → %s", self, images, labels, fake_data, one_hot, dtype, reshape, seed, self._num_examples, extra={"event.action": "__init__", "logrite.images": images, "logrite.labels": labels, "logrite.fake_data": fake_data, "logrite.one_hot": one_hot, "logrite.dtype": dtype, "logrite.reshape": reshape, "logrite.seed": seed})
            self.one_hot = one_hot
        else:
            logger.debug("__init__(self=%s,images=%s,labels=%s,fake_data=%s,one_hot=%s,dtype=%s,reshape=%s,seed=%s): self.one_hot → %s", self, images, labels, fake_data, one_hot, dtype, reshape, seed, self.one_hot, extra={"event.action": "__init__", "logrite.images": images, "logrite.labels": labels, "logrite.fake_data": fake_data, "logrite.one_hot": one_hot, "logrite.dtype": dtype, "logrite.reshape": reshape, "logrite.seed": seed})
            assert images.shape[0] == labels.shape[0], (
                f"images.shape: {images.shape} labels.shape: {labels.shape}"
            )
            self._num_examples = images.shape[0]

            # Convert shape from [num examples, rows, columns, depth]
            # to [num examples, rows*columns] (assuming depth == 1)
            if reshape:
                assert images.shape[3] == 1
                images = images.reshape(
                    images.shape[0], images.shape[1] * images.shape[2]
                )
            if dtype == dtypes.float32:
                # Convert from [0, 255] -> [0.0, 1.0].
                images = images.astype(np.float32)
                images = np.multiply(images, 1.0 / 255.0)
        self._images = images
        logger.debug("__init__(self=%s,images=%s,labels=%s,fake_data=%s,one_hot=%s,dtype=%s,reshape=%s,seed=%s): self._images → %s", self, images, labels, fake_data, one_hot, dtype, reshape, seed, self._images, extra={"event.action": "__init__", "logrite.images": images, "logrite.labels": labels, "logrite.fake_data": fake_data, "logrite.one_hot": one_hot, "logrite.dtype": dtype, "logrite.reshape": reshape, "logrite.seed": seed})
        self._labels = labels
        logger.debug("__init__(self=%s,images=%s,labels=%s,fake_data=%s,one_hot=%s,dtype=%s,reshape=%s,seed=%s): self._labels → %s", self, images, labels, fake_data, one_hot, dtype, reshape, seed, self._labels, extra={"event.action": "__init__", "logrite.images": images, "logrite.labels": labels, "logrite.fake_data": fake_data, "logrite.one_hot": one_hot, "logrite.dtype": dtype, "logrite.reshape": reshape, "logrite.seed": seed})
        self._epochs_completed = 0
        logger.debug("__init__(self=%s,images=%s,labels=%s,fake_data=%s,one_hot=%s,dtype=%s,reshape=%s,seed=%s): self._epochs_completed → %s", self, images, labels, fake_data, one_hot, dtype, reshape, seed, self._epochs_completed, extra={"event.action": "__init__", "logrite.images": images, "logrite.labels": labels, "logrite.fake_data": fake_data, "logrite.one_hot": one_hot, "logrite.dtype": dtype, "logrite.reshape": reshape, "logrite.seed": seed})
        self._index_in_epoch = 0
        logger.debug("__init__(self=%s,images=%s,labels=%s,fake_data=%s,one_hot=%s,dtype=%s,reshape=%s,seed=%s): self._index_in_epoch → %s", self, images, labels, fake_data, one_hot, dtype, reshape, seed, self._index_in_epoch, extra={"event.action": "__init__", "logrite.images": images, "logrite.labels": labels, "logrite.fake_data": fake_data, "logrite.one_hot": one_hot, "logrite.dtype": dtype, "logrite.reshape": reshape, "logrite.seed": seed})

    @property
    def images(self):
        logger.error(">>> Entering images()", extra={"event.action": "images"})
        logger.warning("<<< Exiting images()", extra={"event.action": "images"})
        return self._images

    @property
    def labels(self):
        logger.error(">>> Entering labels()", extra={"event.action": "labels"})
        logger.warning("<<< Exiting labels()", extra={"event.action": "labels"})
        return self._labels

    @property
    def num_examples(self):
        logger.error(">>> Entering num_examples()", extra={"event.action": "num_examples"})
        logger.warning("<<< Exiting num_examples()", extra={"event.action": "num_examples"})
        return self._num_examples

    @property
    def epochs_completed(self):
        logger.error(">>> Entering epochs_completed()", extra={"event.action": "epochs_completed"})
        logger.warning("<<< Exiting epochs_completed()", extra={"event.action": "epochs_completed"})
        return self._epochs_completed

    def next_batch(self, batch_size, fake_data=False, shuffle=True):
        """Return the next `batch_size` examples from this data set."""
        logger.error(">>> Entering next_batch(batch_size=%s,fake_data=%s,shuffle=%s)", batch_size, fake_data, shuffle, extra={"event.action": "next_batch", "logrite.batch_size": batch_size, "logrite.fake_data": fake_data, "logrite.shuffle": shuffle})
        if fake_data:
            fake_image = [1] * 784
            fake_label = [1] + [0] * 9 if self.one_hot else 0
            return (
                [fake_image for _ in range(batch_size)],
                [fake_label for _ in range(batch_size)],
            )
        start = self._index_in_epoch
        # Shuffle for the first epoch
        if self._epochs_completed == 0 and start == 0 and shuffle:
            perm0 = np.arange(self._num_examples)
            self._rng.shuffle(perm0)
            self._images = self.images[perm0]
            logger.debug("next_batch(self=%s,batch_size=%s,fake_data=%s,shuffle=%s): self._images → %s", self, batch_size, fake_data, shuffle, self._images, extra={"event.action": "next_batch", "logrite.batch_size": batch_size, "logrite.fake_data": fake_data, "logrite.shuffle": shuffle})
            self._labels = self.labels[perm0]
            logger.debug("next_batch(self=%s,batch_size=%s,fake_data=%s,shuffle=%s): self._labels → %s", self, batch_size, fake_data, shuffle, self._labels, extra={"event.action": "next_batch", "logrite.batch_size": batch_size, "logrite.fake_data": fake_data, "logrite.shuffle": shuffle})
        # Go to the next epoch
        if start + batch_size > self._num_examples:
            # Finished epoch
            self._epochs_completed += 1
            # Get the rest examples in this epoch
            rest_num_examples = self._num_examples - start
            images_rest_part = self._images[start : self._num_examples]
            labels_rest_part = self._labels[start : self._num_examples]
            # Shuffle the data
            if shuffle:
                perm = np.arange(self._num_examples)
                self._rng.shuffle(perm)
                self._images = self.images[perm]
                self._labels = self.labels[perm]
            # Start next epoch
            start = 0
            self._index_in_epoch = batch_size - rest_num_examples
            logger.debug("next_batch(self=%s,batch_size=%s,fake_data=%s,shuffle=%s): self._index_in_epoch → %s", self, batch_size, fake_data, shuffle, self._index_in_epoch, extra={"event.action": "next_batch", "logrite.batch_size": batch_size, "logrite.fake_data": fake_data, "logrite.shuffle": shuffle})
            end = self._index_in_epoch
            images_new_part = self._images[start:end]
            labels_new_part = self._labels[start:end]
            return (
                np.concatenate((images_rest_part, images_new_part), axis=0),
                np.concatenate((labels_rest_part, labels_new_part), axis=0),
            )
        else:
            self._index_in_epoch += batch_size
            end = self._index_in_epoch
            logger.warning("<<< Exiting next_batch(batch_size=%s,fake_data=%s,shuffle=%s)", batch_size, fake_data, shuffle, extra={"event.action": "next_batch", "logrite.batch_size": batch_size, "logrite.fake_data": fake_data, "logrite.shuffle": shuffle})
            return self._images[start:end], self._labels[start:end]


@deprecated(None, "Please write your own downloading logic.")
def _maybe_download(filename, work_directory, source_url):
    """Download the data from source url, unless it's already here.

    Args:
        filename: string, name of the file in the directory.
        work_directory: string, path to working directory.
        source_url: url to download from if file doesn't exist.

    Returns:
        Path to resulting file.
    """
    logger.error(">>> Entering _maybe_download(filename=%s,work_directory=%s,source_url=%s)", filename, work_directory, source_url, extra={"event.action": "_maybe_download", "logrite.filename": filename, "logrite.work_directory": work_directory, "logrite.source_url": source_url})
    if not gfile.Exists(work_directory):
        gfile.MakeDirs(work_directory)
    filepath = os.path.join(work_directory, filename)
    logger.error("_maybe_download(filename=%s,work_directory=%s,source_url=%s): filepath → %s", filename, work_directory, source_url, filepath, extra={"event.action": "_maybe_download", "logrite.filename": filename, "logrite.work_directory": work_directory, "logrite.source_url": source_url})
    if not gfile.Exists(filepath):
        urllib.request.urlretrieve(source_url, filepath)  # noqa: S310
        with gfile.GFile(filepath) as f:
            size = f.size()
            logger.error("_maybe_download(filename=%s,work_directory=%s,source_url=%s): size → %s", filename, work_directory, source_url, size, extra={"event.action": "_maybe_download", "logrite.filename": filename, "logrite.work_directory": work_directory, "logrite.source_url": source_url})
        print("Successfully downloaded", filename, size, "bytes.")
    logger.warning("<<< Exiting _maybe_download(filename=%s,work_directory=%s,source_url=%s)", filename, work_directory, source_url, extra={"event.action": "_maybe_download", "logrite.filename": filename, "logrite.work_directory": work_directory, "logrite.source_url": source_url})
    return filepath


@deprecated(None, "Please use alternatives such as: tensorflow_datasets.load('mnist')")
def read_data_sets(
    train_dir,
    fake_data=False,
    one_hot=False,
    dtype=dtypes.float32,
    reshape=True,
    validation_size=5000,
    seed=None,
    source_url=DEFAULT_SOURCE_URL,
):
    logger.error(">>> Entering read_data_sets(train_dir=%s,fake_data=%s,one_hot=%s,dtype=%s,reshape=%s,validation_size=%s,seed=%s,source_url=%s)", train_dir, fake_data, one_hot, dtype, reshape, validation_size, seed, source_url, extra={"event.action": "read_data_sets", "logrite.train_dir": train_dir, "logrite.fake_data": fake_data, "logrite.one_hot": one_hot, "logrite.dtype": dtype, "logrite.reshape": reshape, "logrite.validation_size": validation_size, "logrite.seed": seed, "logrite.source_url": source_url})
    logger.error("read_data_sets(train_dir=%s,fake_data=%s,one_hot=%s,dtype=%s,reshape=%s,validation_size=%s,seed=%s,source_url=%s): fake_data → %s", train_dir, fake_data, one_hot, dtype, reshape, validation_size, seed, source_url, fake_data, extra={"event.action": "read_data_sets", "logrite.train_dir": train_dir, "logrite.fake_data": fake_data, "logrite.one_hot": one_hot, "logrite.dtype": dtype, "logrite.reshape": reshape, "logrite.validation_size": validation_size, "logrite.seed": seed, "logrite.source_url": source_url})
    if fake_data:

        logger.warning("<<< Exiting read_data_sets(train_dir=%s,fake_data=%s,one_hot=%s,dtype=%s,reshape=%s,validation_size=%s,seed=%s,source_url=%s)", train_dir, fake_data, one_hot, dtype, reshape, validation_size, seed, source_url, extra={"event.action": "read_data_sets", "logrite.train_dir": train_dir, "logrite.fake_data": fake_data, "logrite.one_hot": one_hot, "logrite.dtype": dtype, "logrite.reshape": reshape, "logrite.validation_size": validation_size, "logrite.seed": seed, "logrite.source_url": source_url})
        def fake():
            logger.error(">>> Entering fake()", extra={"event.action": "fake"})
            logger.warning("<<< Exiting fake()", extra={"event.action": "fake"})
            return _DataSet(
                [], [], fake_data=True, one_hot=one_hot, dtype=dtype, seed=seed
            )

        train = fake()
        validation = fake()
        test = fake()
        return _Datasets(train=train, validation=validation, test=test)

    if not source_url:  # empty string check
        source_url = DEFAULT_SOURCE_URL

    train_images_file = "train-images-idx3-ubyte.gz"
    train_labels_file = "train-labels-idx1-ubyte.gz"
    test_images_file = "t10k-images-idx3-ubyte.gz"
    test_labels_file = "t10k-labels-idx1-ubyte.gz"

    local_file = _maybe_download(
        train_images_file, train_dir, source_url + train_images_file
    )
    with gfile.Open(local_file, "rb") as f:
        train_images = _extract_images(f)

    local_file = _maybe_download(
        train_labels_file, train_dir, source_url + train_labels_file
    )
    with gfile.Open(local_file, "rb") as f:
        train_labels = _extract_labels(f, one_hot=one_hot)

    local_file = _maybe_download(
        test_images_file, train_dir, source_url + test_images_file
    )
    with gfile.Open(local_file, "rb") as f:
        test_images = _extract_images(f)

    local_file = _maybe_download(
        test_labels_file, train_dir, source_url + test_labels_file
    )
    with gfile.Open(local_file, "rb") as f:
        test_labels = _extract_labels(f, one_hot=one_hot)

    if not 0 <= validation_size <= len(train_images):
        msg = (
            "Validation size should be between 0 and "
            f"{len(train_images)}. Received: {validation_size}."
        )
        raise ValueError(msg)

    validation_images = train_images[:validation_size]
    validation_labels = train_labels[:validation_size]
    train_images = train_images[validation_size:]
    train_labels = train_labels[validation_size:]

    options = {"dtype": dtype, "reshape": reshape, "seed": seed}

    train = _DataSet(train_images, train_labels, **options)
    validation = _DataSet(validation_images, validation_labels, **options)
    test = _DataSet(test_images, test_labels, **options)

    return _Datasets(train=train, validation=validation, test=test)
