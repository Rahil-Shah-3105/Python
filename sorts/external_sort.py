#!/usr/bin/env python

#
# Sort large text files in a minimum amount of memory
#
import argparse
import os
import logging
logger = logging.getLogger(__name__)


class FileSplitter:
    BLOCK_FILENAME_FORMAT = "block_{0}.dat"

    def __init__(self, filename):
        logger.debug(">>> Entering __init__(filename=%s)", filename)
        self.filename = filename
        logger.debug("__init__(self=%s,filename=%s): self.filename → %s", self, filename, self.filename)
        self.block_filenames = []
        logger.debug("__init__(self=%s,filename=%s): self.block_filenames → %s", self, filename, self.block_filenames)
        logger.debug("<<< Exiting __init__(filename=%s)", filename)
        logger.debug(">>> Entering __init__(files=%s)", files)
        logger.debug("__init__(self=%s,files=%s): self.files → %s", self, files, self.files)
        logger.debug("__init__(files=%s): self.empty → %s", files, self.empty)
        logger.debug("__init__(files=%s): self.num_buffers → %s", files, self.num_buffers)
        logger.debug("<<< Exiting __init__(files=%s)", files)

    def write_block(self, data, block_number):
        logger.debug(">>> Entering write_block(data=%s,block_number=%s)", data, block_number)
        filename = self.BLOCK_FILENAME_FORMAT.format(block_number)
        logger.debug("write_block(data=%s,block_number=%s): filename → %s", data, block_number, filename)
        logger.debug("write_block(self=%s,data=%s,block_number=%s): filename → %s", self, data, block_number, filename)
        with open(filename, "w") as file:
            file.write(data)
            logger.error("Exception in write_block(data=%s,block_number=%s)", data, block_number, exc_info=True)
        self.block_filenames.append(filename)
        logger.debug("<<< Exiting write_block(data=%s,block_number=%s)", data, block_number)

    def get_block_filenames(self):
        logger.debug(">>> Entering get_block_filenames()")
        logger.debug("<<< Exiting get_block_filenames()")
        return self.block_filenames

    def split(self, block_size, sort_key=None):
        logger.debug(">>> Entering split(block_size=%s,sort_key=%s)", block_size, sort_key)
        i = 0
        with open(self.filename) as file:
            logger.error("Exception in split(block_size=%s,sort_key=%s)", block_size, sort_key, exc_info=True)
            while True:
                lines = file.readlines(block_size)
                logger.debug("split(block_size=%s,sort_key=%s): lines → %s", block_size, sort_key, lines)

                if lines == []:
                    break

                if sort_key is None:
                    lines.sort()
                else:
                    lines.sort(key=sort_key)

                self.write_block("".join(lines), i)
                i += 1
                logger.debug("<<< Exiting split(block_size=%s,sort_key=%s)", block_size, sort_key)

    def cleanup(self):
        logger.debug(">>> Entering cleanup()")
        map(os.remove, self.block_filenames)
        logger.debug("<<< Exiting cleanup()")


class NWayMerge:
    def select(self, choices):
        logger.debug(">>> Entering select(choices=%s)", choices)
        min_index = -1
        logger.debug("select(self=%s,choices=%s): min_index → %s", self, choices, min_index)
        min_str = None
        logger.debug("select(self=%s,choices=%s): min_str → %s", self, choices, min_str)

        for i in range(len(choices)):
            if min_str is None or choices[i] < min_str:
                min_index = i

        logger.debug("<<< Exiting select(choices=%s)", choices)
        return min_index


class FilesArray:
    def __init__(self, files):
        self.files = files
        self.empty = set()
        self.num_buffers = len(files)
        self.buffers = dict.fromkeys(range(self.num_buffers))
        logger.debug("__init__(files=%s): self.buffers → %s", files, self.buffers)
        logger.debug(">>> Entering __init__(merge_strategy=%s)", merge_strategy)
        logger.debug("<<< Exiting __init__(merge_strategy=%s)", merge_strategy)

    def get_dict(self):
        logger.debug(">>> Entering get_dict()")
        return {
            i: self.buffers[i] for i in range(self.num_buffers) if i not in self.empty
        }
        logger.debug("<<< Exiting get_dict()")

    def refresh(self):
        logger.debug(">>> Entering refresh()")
        for i in range(self.num_buffers):
            if self.buffers[i] is None and i not in self.empty:
                self.buffers[i] = self.files[i].readline()

                if self.buffers[i] == "":
                    self.empty.add(i)
                    self.files[i].close()

        logger.debug("<<< Exiting refresh()")
        return len(self.empty) != self.num_buffers

    def unshift(self, index):
        logger.debug(">>> Entering unshift(index=%s)", index)
        value = self.buffers[index]
        logger.debug("unshift(self=%s,index=%s): value → %s", self, index, value)
        self.buffers[index] = None

        logger.debug("<<< Exiting unshift(index=%s)", index)
        return value


class FileMerger:
    def __init__(self, merge_strategy):
        self.merge_strategy = merge_strategy
        logger.debug("__init__(self=%s,merge_strategy=%s): self.merge_strategy → %s", self, merge_strategy, self.merge_strategy)
        logger.debug(">>> Entering __init__(block_size=%s)", block_size)
        logger.debug("<<< Exiting __init__(block_size=%s)", block_size)

    def merge(self, filenames, outfilename, buffer_size):
        logger.debug(">>> Entering merge(filenames=%s,outfilename=%s,buffer_size=%s)", filenames, outfilename, buffer_size)
        buffers = FilesArray(self.get_file_handles(filenames, buffer_size))
        with open(outfilename, "w", buffer_size) as outfile:
            logger.debug("merge(self=%s,filenames=%s,outfilename=%s,buffer_size=%s): buffers → %s", self, filenames, outfilename, buffer_size, buffers)
            logger.debug("merge(filenames=%s,outfilename=%s,buffer_size=%s): buffers → %s", filenames, outfilename, buffer_size, buffers)
            import time; __log_start = time.time()
            while buffers.refresh():
                min_index = self.merge_strategy.select(buffers.get_dict())
                outfile.write(buffers.unshift(min_index))
                logger.info("merge(filenames,outfilename,buffer_size)=%s,%s,%s: database operation took %s ms", filenames, outfilename, buffer_size, int((time.time() - __log_start) * 1000))
                logger.error("Exception in merge(filenames=%s,outfilename=%s,buffer_size=%s)", filenames, outfilename, buffer_size, exc_info=True)
                logger.debug("<<< Exiting merge(filenames=%s,outfilename=%s,buffer_size=%s)", filenames, outfilename, buffer_size)

    def get_file_handles(self, filenames, buffer_size):
        files = {}
        logger.debug(">>> Entering get_file_handles(filenames=%s,buffer_size=%s)", filenames, buffer_size)
        logger.debug("get_file_handles(self=%s,filenames=%s,buffer_size=%s): files → %s", self, filenames, buffer_size, files)

        for i in range(len(filenames)):
            files[i] = open(filenames[i], "r", buffer_size)  # noqa: UP015

        logger.debug("<<< Exiting get_file_handles(filenames=%s,buffer_size=%s)", filenames, buffer_size)
        return files


class ExternalSort:
    def __init__(self, block_size):
        self.block_size = block_size
        logger.debug("__init__(self=%s,block_size=%s): self.block_size → %s", self, block_size, self.block_size)

    def sort(self, filename, sort_key=None):
        logger.debug(">>> Entering sort(filename=%s,sort_key=%s)", filename, sort_key)
        num_blocks = self.get_number_blocks(filename, self.block_size)
        logger.debug("sort(filename=%s,sort_key=%s): num_blocks → %s", filename, sort_key, num_blocks)
        logger.debug("sort(self=%s,filename=%s,sort_key=%s): num_blocks → %s", self, filename, sort_key, num_blocks)
        splitter = FileSplitter(filename)
        logger.debug("sort(filename=%s,sort_key=%s): splitter → %s", filename, sort_key, splitter)
        logger.debug("sort(self=%s,filename=%s,sort_key=%s): splitter → %s", self, filename, sort_key, splitter)
        splitter.split(self.block_size, sort_key)

        merger = FileMerger(NWayMerge())
        buffer_size = self.block_size / (num_blocks + 1)
        logger.debug("sort(self=%s,filename=%s,sort_key=%s): merger → %s", self, filename, sort_key, merger)
        logger.debug("sort(filename=%s,sort_key=%s): merger → %s", filename, sort_key, merger)
        logger.debug("sort(self=%s,filename=%s,sort_key=%s): buffer_size → %s", self, filename, sort_key, buffer_size)
        logger.debug("sort(filename=%s,sort_key=%s): buffer_size → %s", filename, sort_key, buffer_size)
        merger.merge(splitter.get_block_filenames(), filename + ".out", buffer_size)

        logger.debug("<<< Exiting sort(filename=%s,sort_key=%s)", filename, sort_key)
        splitter.cleanup()

    def get_number_blocks(self, filename, block_size):
        logger.debug(">>> Entering get_number_blocks(filename=%s,block_size=%s)", filename, block_size)
        logger.debug("<<< Exiting get_number_blocks(filename=%s,block_size=%s)", filename, block_size)
        return (os.stat(filename).st_size / block_size) + 1


def parse_memory(string):
    logger.debug(">>> Entering parse_memory(string=%s)", string)
    if string[-1].lower() == "k":
        return int(string[:-1]) * 1024
    elif string[-1].lower() == "m":
        return int(string[:-1]) * 1024 * 1024
    elif string[-1].lower() == "g":
        return int(string[:-1]) * 1024 * 1024 * 1024
    else:
        logger.debug("<<< Exiting parse_memory(string=%s)", string)
        return int(string)


def main():
    logger.debug(">>> Entering main()")
    parser = argparse.ArgumentParser()
    logger.debug("main(): parser → %s", parser)
    parser.add_argument(
        "-m", "--mem", help="amount of memory to use for sorting", default="100M"
    )
    parser.add_argument(
        "filename", metavar="<filename>", nargs=1, help="name of file to sort"
    )
    args = parser.parse_args()
    logger.debug("main(): args → %s", args)

    sorter = ExternalSort(parse_memory(args.mem))
    logger.debug("main(): sorter → %s", sorter)
    sorter.sort(args.filename[0])
    logger.debug("<<< Exiting main()")


if __name__ == "__main__":
    main()
