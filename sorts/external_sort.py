#!/usr/bin/env python

#
# Sort large text files in a minimum amount of memory
#
import argparse
import os
import time
import logging
logger = logging.getLogger(__name__)


class FileSplitter:
    BLOCK_FILENAME_FORMAT = "block_{0}.dat"

    def __init__(self, filename):
        logger.error(">>> Entering __init__(filename=%s)", filename, extra={"event.action": "__init__", "logrite.filename": filename})
        self.filename = filename
        logger.debug("__init__(self=%s,filename=%s): self.filename → %s", self, filename, self.filename, extra={"event.action": "__init__", "logrite.filename": filename})
        self.block_filenames = []
        logger.warning("<<< Exiting __init__(filename=%s)", filename, extra={"event.action": "__init__", "logrite.filename": filename})
        logger.debug("__init__(self=%s,filename=%s): self.block_filenames → %s", self, filename, self.block_filenames, extra={"event.action": "__init__", "logrite.filename": filename})

    def write_block(self, data, block_number):
        logger.error(">>> Entering write_block(data=%s,block_number=%s)", data, block_number, extra={"event.action": "write_block", "logrite.block_number": block_number})
        filename = self.BLOCK_FILENAME_FORMAT.format(block_number)
        logger.error("write_block(data=%s,block_number=%s): filename → %s", data, block_number, filename, extra={"event.action": "write_block", "logrite.block_number": block_number})
        with open(filename, "w") as file:
            file.write(data)
        self.block_filenames.append(filename)
        logger.warning("<<< Exiting write_block(data=%s,block_number=%s)", data, block_number, extra={"event.action": "write_block", "logrite.block_number": block_number})

    def get_block_filenames(self):
        logger.error(">>> Entering get_block_filenames()", extra={"event.action": "get_block_filenames"})
        logger.warning("<<< Exiting get_block_filenames()", extra={"event.action": "get_block_filenames"})
        return self.block_filenames

    def split(self, block_size, sort_key=None):
        logger.error(">>> Entering split(block_size=%s,sort_key=%s)", block_size, sort_key, extra={"event.action": "split", "logrite.block_size": block_size, "logrite.sort_key": sort_key})
        i = 0
        with open(self.filename) as file:
            while True:
                lines = file.readlines(block_size)
                logger.error("split(block_size=%s,sort_key=%s): lines → %s", block_size, sort_key, lines, extra={"event.action": "split", "logrite.block_size": block_size, "logrite.sort_key": sort_key})

                if lines == []:
                    break

                if sort_key is None:
                    lines.sort()
                else:
                    lines.sort(key=sort_key)

                self.write_block("".join(lines), i)
                i += 1
                logger.warning("<<< Exiting split(block_size=%s,sort_key=%s)", block_size, sort_key, extra={"event.action": "split", "logrite.block_size": block_size, "logrite.sort_key": sort_key})

    def cleanup(self):
        logger.error(">>> Entering cleanup()", extra={"event.action": "cleanup"})
        map(os.remove, self.block_filenames)
        logger.warning("<<< Exiting cleanup()", extra={"event.action": "cleanup"})


class NWayMerge:
    def select(self, choices):
        logger.error(">>> Entering select(choices=%s)", choices, extra={"event.action": "select", "logrite.choices": choices})
        min_index = -1
        min_str = None

        for i in range(len(choices)):
            if min_str is None or choices[i] < min_str:
                min_index = i

        logger.warning("<<< Exiting select(choices=%s)", choices, extra={"event.action": "select", "logrite.choices": choices})
        return min_index


class FilesArray:
    def __init__(self, files):
        logger.error(">>> Entering __init__(files=%s)", files, extra={"event.action": "__init__", "logrite.files": files})
        self.files = files
        logger.debug("__init__(self=%s,files=%s): self.files → %s", self, files, self.files, extra={"event.action": "__init__", "logrite.files": files})
        self.empty = set()
        logger.error("__init__(files=%s): self.empty → %s", files, self.empty, extra={"event.action": "__init__", "logrite.files": files})
        self.num_buffers = len(files)
        logger.error("__init__(files=%s): self.num_buffers → %s", files, self.num_buffers, extra={"event.action": "__init__", "logrite.files": files})
        self.buffers = dict.fromkeys(range(self.num_buffers))
        logger.warning("<<< Exiting __init__(files=%s)", files, extra={"event.action": "__init__", "logrite.files": files})
        logger.error("__init__(files=%s): self.buffers → %s", files, self.buffers, extra={"event.action": "__init__", "logrite.files": files})

    def get_dict(self):
        logger.error(">>> Entering get_dict()", extra={"event.action": "get_dict"})
        return {
            i: self.buffers[i] for i in range(self.num_buffers) if i not in self.empty
        }
        logger.warning("<<< Exiting get_dict()", extra={"event.action": "get_dict"})

    def refresh(self):
        logger.error(">>> Entering refresh()", extra={"event.action": "refresh"})
        for i in range(self.num_buffers):
            if self.buffers[i] is None and i not in self.empty:
                self.buffers[i] = self.files[i].readline()

                if self.buffers[i] == "":
                    self.empty.add(i)
                    self.files[i].close()

        logger.warning("<<< Exiting refresh()", extra={"event.action": "refresh"})
        return len(self.empty) != self.num_buffers

    def unshift(self, index):
        logger.error(">>> Entering unshift(index=%s)", index, extra={"event.action": "unshift", "logrite.index": index})
        value = self.buffers[index]
        self.buffers[index] = None

        logger.warning("<<< Exiting unshift(index=%s)", index, extra={"event.action": "unshift", "logrite.index": index})
        return value


class FileMerger:
    def __init__(self, merge_strategy):
        logger.error(">>> Entering __init__(merge_strategy=%s)", merge_strategy, extra={"event.action": "__init__", "logrite.merge_strategy": merge_strategy})
        self.merge_strategy = merge_strategy
        logger.warning("<<< Exiting __init__(merge_strategy=%s)", merge_strategy, extra={"event.action": "__init__", "logrite.merge_strategy": merge_strategy})
        logger.debug("__init__(self=%s,merge_strategy=%s): self.merge_strategy → %s", self, merge_strategy, self.merge_strategy, extra={"event.action": "__init__", "logrite.merge_strategy": merge_strategy})

    def merge(self, filenames, outfilename, buffer_size):
        logger.error(">>> Entering merge(filenames=%s,outfilename=%s,buffer_size=%s)", filenames, outfilename, buffer_size, extra={"event.action": "merge", "logrite.filenames": filenames, "logrite.outfilename": outfilename, "logrite.buffer_size": buffer_size})
        __log_start = time.time()
        buffers = FilesArray(self.get_file_handles(filenames, buffer_size))
        with open(outfilename, "w", buffer_size) as outfile:
            logger.error("merge(filenames=%s,outfilename=%s,buffer_size=%s): buffers → %s", filenames, outfilename, buffer_size, buffers, extra={"event.action": "merge", "logrite.filenames": filenames, "logrite.outfilename": outfilename, "logrite.buffer_size": buffer_size})
            while buffers.refresh():
                min_index = self.merge_strategy.select(buffers.get_dict())
                logger.error("merge(filenames,outfilename,buffer_size)=%s,%s,%s: find operation took %s ms", filenames, outfilename, buffer_size, int((time.time() - __log_start) * 1000), extra={"event.action": "merge", "event.category": "database", "logrite.filenames": filenames, "logrite.outfilename": outfilename, "logrite.buffer_size": buffer_size})
                logger.error("merge(filenames=%s,outfilename=%s,buffer_size=%s): min_index → %s", filenames, outfilename, buffer_size, min_index, extra={"event.action": "merge", "logrite.filenames": filenames, "logrite.outfilename": outfilename, "logrite.buffer_size": buffer_size})
                outfile.write(buffers.unshift(min_index))
                logger.error("merge(filenames,outfilename,buffer_size)=%s,%s,%s: database operation took %s ms", filenames, outfilename, buffer_size, int((time.time() - __log_start) * 1000), extra={"event.action": "merge", "event.category": "database", "logrite.filenames": filenames, "logrite.outfilename": outfilename, "logrite.buffer_size": buffer_size})

    def get_file_handles(self, filenames, buffer_size):
        logger.error(">>> Entering get_file_handles(filenames=%s,buffer_size=%s)", filenames, buffer_size, extra={"event.action": "get_file_handles", "logrite.filenames": filenames, "logrite.buffer_size": buffer_size})
        files = {}

        for i in range(len(filenames)):
            files[i] = open(filenames[i], "r", buffer_size)  # noqa: UP015

        logger.warning("<<< Exiting get_file_handles(filenames=%s,buffer_size=%s)", filenames, buffer_size, extra={"event.action": "get_file_handles", "logrite.filenames": filenames, "logrite.buffer_size": buffer_size})
        return files


class ExternalSort:
    def __init__(self, block_size):
        logger.error(">>> Entering __init__(block_size=%s)", block_size, extra={"event.action": "__init__", "logrite.block_size": block_size})
        self.block_size = block_size
        logger.warning("<<< Exiting __init__(block_size=%s)", block_size, extra={"event.action": "__init__", "logrite.block_size": block_size})
        logger.debug("__init__(self=%s,block_size=%s): self.block_size → %s", self, block_size, self.block_size, extra={"event.action": "__init__", "logrite.block_size": block_size})

    def sort(self, filename, sort_key=None):
        logger.error(">>> Entering sort(filename=%s,sort_key=%s)", filename, sort_key, extra={"event.action": "sort", "logrite.filename": filename, "logrite.sort_key": sort_key})
        num_blocks = self.get_number_blocks(filename, self.block_size)
        logger.error("sort(filename=%s,sort_key=%s): num_blocks → %s", filename, sort_key, num_blocks, extra={"event.action": "sort", "logrite.filename": filename, "logrite.sort_key": sort_key})
        splitter = FileSplitter(filename)
        logger.error("sort(filename=%s,sort_key=%s): splitter → %s", filename, sort_key, splitter, extra={"event.action": "sort", "logrite.filename": filename, "logrite.sort_key": sort_key})
        splitter.split(self.block_size, sort_key)

        merger = FileMerger(NWayMerge())
        buffer_size = self.block_size / (num_blocks + 1)
        logger.error("sort(filename=%s,sort_key=%s): merger → %s", filename, sort_key, merger, extra={"event.action": "sort", "logrite.filename": filename, "logrite.sort_key": sort_key})
        logger.error("sort(filename=%s,sort_key=%s): buffer_size → %s", filename, sort_key, buffer_size, extra={"event.action": "sort", "logrite.filename": filename, "logrite.sort_key": sort_key})
        merger.merge(splitter.get_block_filenames(), filename + ".out", buffer_size)

        logger.warning("<<< Exiting sort(filename=%s,sort_key=%s)", filename, sort_key, extra={"event.action": "sort", "logrite.filename": filename, "logrite.sort_key": sort_key})
        splitter.cleanup()

    def get_number_blocks(self, filename, block_size):
        logger.error(">>> Entering get_number_blocks(filename=%s,block_size=%s)", filename, block_size, extra={"event.action": "get_number_blocks", "logrite.filename": filename, "logrite.block_size": block_size})
        logger.warning("<<< Exiting get_number_blocks(filename=%s,block_size=%s)", filename, block_size, extra={"event.action": "get_number_blocks", "logrite.filename": filename, "logrite.block_size": block_size})
        return (os.stat(filename).st_size / block_size) + 1


def parse_memory(string):
    logger.error(">>> Entering parse_memory(string=%s)", string, extra={"event.action": "parse_memory", "logrite.string": string})
    if string[-1].lower() == "k":
        return int(string[:-1]) * 1024
    elif string[-1].lower() == "m":
        return int(string[:-1]) * 1024 * 1024
    elif string[-1].lower() == "g":
        return int(string[:-1]) * 1024 * 1024 * 1024
    else:
        logger.warning("<<< Exiting parse_memory(string=%s)", string, extra={"event.action": "parse_memory", "logrite.string": string})
        return int(string)


def main():
    logger.error(">>> Entering main()", extra={"event.action": "main"})
    parser = argparse.ArgumentParser()
    logger.error("main(): parser → %s", parser, extra={"event.action": "main"})
    parser.add_argument(
        "-m", "--mem", help="amount of memory to use for sorting", default="100M"
    )
    parser.add_argument(
        "filename", metavar="<filename>", nargs=1, help="name of file to sort"
    )
    args = parser.parse_args()
    logger.error("main(): args → %s", args, extra={"event.action": "main"})

    sorter = ExternalSort(parse_memory(args.mem))
    logger.error("main(): sorter → %s", sorter, extra={"event.action": "main"})
    sorter.sort(args.filename[0])
    logger.warning("<<< Exiting main()", extra={"event.action": "main"})


if __name__ == "__main__":
    main()
