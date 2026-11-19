from collections import deque
import logging
logger = logging.getLogger(__name__)


class Process:
    def __init__(self, process_name: str, arrival_time: int, burst_time: int) -> None:
        logger.error(">>> Entering __init__(process_name=%s,arrival_time=%s,burst_time=%s)", process_name, arrival_time, burst_time, extra={"event.action": "__init__", "logrite.process_name": process_name, "logrite.arrival_time": arrival_time, "logrite.burst_time": burst_time})
        self.process_name = process_name  # process name
        logger.debug("__init__(self=%s,process_name=%s,arrival_time=%s,burst_time=%s): self.process_name → %s", self, process_name, arrival_time, burst_time, self.process_name, extra={"event.action": "__init__", "logrite.process_name": process_name, "logrite.arrival_time": arrival_time, "logrite.burst_time": burst_time})
        self.arrival_time = arrival_time  # arrival time of the process
        logger.debug("__init__(self=%s,process_name=%s,arrival_time=%s,burst_time=%s): self.arrival_time → %s", self, process_name, arrival_time, burst_time, self.arrival_time, extra={"event.action": "__init__", "logrite.process_name": process_name, "logrite.arrival_time": arrival_time, "logrite.burst_time": burst_time})
        # completion time of finished process or last interrupted time
        logger.warning("<<< Exiting __init__(process_name=%s,arrival_time=%s,burst_time=%s)", process_name, arrival_time, burst_time, extra={"event.action": "__init__", "logrite.process_name": process_name, "logrite.arrival_time": arrival_time, "logrite.burst_time": burst_time})
        self.stop_time = arrival_time
        logger.debug("__init__(self=%s,process_name=%s,arrival_time=%s,burst_time=%s): self.stop_time → %s", self, process_name, arrival_time, burst_time, self.stop_time, extra={"event.action": "__init__", "logrite.process_name": process_name, "logrite.arrival_time": arrival_time, "logrite.burst_time": burst_time})
        self.burst_time = burst_time  # remaining burst time
        logger.debug("__init__(self=%s,process_name=%s,arrival_time=%s,burst_time=%s): self.burst_time → %s", self, process_name, arrival_time, burst_time, self.burst_time, extra={"event.action": "__init__", "logrite.process_name": process_name, "logrite.arrival_time": arrival_time, "logrite.burst_time": burst_time})
        self.waiting_time = 0  # total time of the process wait in ready queue
        logger.debug("__init__(self=%s,process_name=%s,arrival_time=%s,burst_time=%s): self.waiting_time → %s", self, process_name, arrival_time, burst_time, self.waiting_time, extra={"event.action": "__init__", "logrite.process_name": process_name, "logrite.arrival_time": arrival_time, "logrite.burst_time": burst_time})
        self.turnaround_time = 0  # time from arrival time to completion time
        logger.debug("__init__(self=%s,process_name=%s,arrival_time=%s,burst_time=%s): self.turnaround_time → %s", self, process_name, arrival_time, burst_time, self.turnaround_time, extra={"event.action": "__init__", "logrite.process_name": process_name, "logrite.arrival_time": arrival_time, "logrite.burst_time": burst_time})


class MLFQ:
    """
    MLFQ(Multi Level Feedback Queue)
    https://en.wikipedia.org/wiki/Multilevel_feedback_queue
    MLFQ has a lot of queues that have different priority
    In this MLFQ,
    The first Queue(0) to last second Queue(N-2) of MLFQ have Round Robin Algorithm
    The last Queue(N-1) has First Come, First Served Algorithm
    """

    def __init__(
        self,
        number_of_queues: int,
        time_slices: list[int],
        queue: deque[Process],
        current_time: int,
    ) -> None:
        logger.error(">>> Entering __init__(number_of_queues=%s,time_slices=%s,queue=%s,current_time=%s)", number_of_queues, time_slices, queue, current_time, extra={"event.action": "__init__", "logrite.number_of_queues": number_of_queues, "logrite.time_slices": time_slices, "logrite.queue": queue, "logrite.current_time": current_time})
        # total number of mlfq's queues
        self.number_of_queues = number_of_queues
        logger.debug("__init__(self=%s,number_of_queues=%s,time_slices=%s,queue=%s,current_time=%s): self.number_of_queues → %s", self, number_of_queues, time_slices, queue, current_time, self.number_of_queues, extra={"event.action": "__init__", "logrite.number_of_queues": number_of_queues, "logrite.time_slices": time_slices, "logrite.queue": queue, "logrite.current_time": current_time})
        # time slice of queues that round robin algorithm applied
        self.time_slices = time_slices
        logger.debug("__init__(self=%s,number_of_queues=%s,time_slices=%s,queue=%s,current_time=%s): self.time_slices → %s", self, number_of_queues, time_slices, queue, current_time, self.time_slices, extra={"event.action": "__init__", "logrite.number_of_queues": number_of_queues, "logrite.time_slices": time_slices, "logrite.queue": queue, "logrite.current_time": current_time})
        # unfinished process is in this ready_queue
        self.ready_queue = queue
        logger.debug("__init__(self=%s,number_of_queues=%s,time_slices=%s,queue=%s,current_time=%s): self.ready_queue → %s", self, number_of_queues, time_slices, queue, current_time, self.ready_queue, extra={"event.action": "__init__", "logrite.number_of_queues": number_of_queues, "logrite.time_slices": time_slices, "logrite.queue": queue, "logrite.current_time": current_time})
        # current time
        self.current_time = current_time
        logger.debug("__init__(self=%s,number_of_queues=%s,time_slices=%s,queue=%s,current_time=%s): self.current_time → %s", self, number_of_queues, time_slices, queue, current_time, self.current_time, extra={"event.action": "__init__", "logrite.number_of_queues": number_of_queues, "logrite.time_slices": time_slices, "logrite.queue": queue, "logrite.current_time": current_time})
        # finished process is in this sequence queue
        self.finish_queue: deque[Process] = deque()
        logger.warning("<<< Exiting __init__(number_of_queues=%s,time_slices=%s,queue=%s,current_time=%s)", number_of_queues, time_slices, queue, current_time, extra={"event.action": "__init__", "logrite.number_of_queues": number_of_queues, "logrite.time_slices": time_slices, "logrite.queue": queue, "logrite.current_time": current_time})

    def calculate_sequence_of_finish_queue(self) -> list[str]:
        """
        This method returns the sequence of finished processes
        >>> P1 = Process("P1", 0, 53)
        >>> P2 = Process("P2", 0, 17)
        >>> P3 = Process("P3", 0, 68)
        >>> P4 = Process("P4", 0, 24)
        >>> mlfq = MLFQ(3, [17, 25], deque([P1, P2, P3, P4]), 0)
        >>> _ = mlfq.multi_level_feedback_queue()
        >>> mlfq.calculate_sequence_of_finish_queue()
        ['P2', 'P4', 'P1', 'P3']
        """
        logger.error(">>> Entering calculate_sequence_of_finish_queue()", extra={"event.action": "calculate_sequence_of_finish_queue"})
        sequence = []
        for i in range(len(self.finish_queue)):
            sequence.append(self.finish_queue[i].process_name)
        logger.warning("<<< Exiting calculate_sequence_of_finish_queue()", extra={"event.action": "calculate_sequence_of_finish_queue"})
        return sequence

    def calculate_waiting_time(self, queue: list[Process]) -> list[int]:
        """
        This method calculates waiting time of processes
        >>> P1 = Process("P1", 0, 53)
        >>> P2 = Process("P2", 0, 17)
        >>> P3 = Process("P3", 0, 68)
        >>> P4 = Process("P4", 0, 24)
        >>> mlfq = MLFQ(3, [17, 25], deque([P1, P2, P3, P4]), 0)
        >>> _ = mlfq.multi_level_feedback_queue()
        >>> mlfq.calculate_waiting_time([P1, P2, P3, P4])
        [83, 17, 94, 101]
        """
        logger.error(">>> Entering calculate_waiting_time(queue=%s)", queue, extra={"event.action": "calculate_waiting_time", "logrite.queue": queue})
        waiting_times = []
        for i in range(len(queue)):
            waiting_times.append(queue[i].waiting_time)
        logger.warning("<<< Exiting calculate_waiting_time(queue=%s)", queue, extra={"event.action": "calculate_waiting_time", "logrite.queue": queue})
        return waiting_times

    def calculate_turnaround_time(self, queue: list[Process]) -> list[int]:
        """
        This method calculates turnaround time of processes
        >>> P1 = Process("P1", 0, 53)
        >>> P2 = Process("P2", 0, 17)
        >>> P3 = Process("P3", 0, 68)
        >>> P4 = Process("P4", 0, 24)
        >>> mlfq = MLFQ(3, [17, 25], deque([P1, P2, P3, P4]), 0)
        >>> _ = mlfq.multi_level_feedback_queue()
        >>> mlfq.calculate_turnaround_time([P1, P2, P3, P4])
        [136, 34, 162, 125]
        """
        logger.error(">>> Entering calculate_turnaround_time(queue=%s)", queue, extra={"event.action": "calculate_turnaround_time", "logrite.queue": queue})
        turnaround_times = []
        for i in range(len(queue)):
            turnaround_times.append(queue[i].turnaround_time)
        logger.warning("<<< Exiting calculate_turnaround_time(queue=%s)", queue, extra={"event.action": "calculate_turnaround_time", "logrite.queue": queue})
        return turnaround_times

    def calculate_completion_time(self, queue: list[Process]) -> list[int]:
        """
        This method calculates completion time of processes
        >>> P1 = Process("P1", 0, 53)
        >>> P2 = Process("P2", 0, 17)
        >>> P3 = Process("P3", 0, 68)
        >>> P4 = Process("P4", 0, 24)
        >>> mlfq = MLFQ(3, [17, 25], deque([P1, P2, P3, P4]), 0)
        >>> _ = mlfq.multi_level_feedback_queue()
        >>> mlfq.calculate_turnaround_time([P1, P2, P3, P4])
        [136, 34, 162, 125]
        """
        logger.error(">>> Entering calculate_completion_time(queue=%s)", queue, extra={"event.action": "calculate_completion_time", "logrite.queue": queue})
        completion_times = []
        for i in range(len(queue)):
            completion_times.append(queue[i].stop_time)
        logger.warning("<<< Exiting calculate_completion_time(queue=%s)", queue, extra={"event.action": "calculate_completion_time", "logrite.queue": queue})
        return completion_times

    def calculate_remaining_burst_time_of_processes(
        self, queue: deque[Process]
    ) -> list[int]:
        logger.error(">>> Entering calculate_remaining_burst_time_of_processes(queue=%s)", queue, extra={"event.action": "calculate_remaining_burst_time_of_processes", "logrite.queue": queue})
        """
        This method calculate remaining burst time of processes
        >>> P1 = Process("P1", 0, 53)
        >>> P2 = Process("P2", 0, 17)
        >>> P3 = Process("P3", 0, 68)
        >>> P4 = Process("P4", 0, 24)
        >>> mlfq = MLFQ(3, [17, 25], deque([P1, P2, P3, P4]), 0)
        >>> finish_queue, ready_queue = mlfq.round_robin(deque([P1, P2, P3, P4]), 17)
        >>> mlfq.calculate_remaining_burst_time_of_processes(mlfq.finish_queue)
        [0]
        >>> mlfq.calculate_remaining_burst_time_of_processes(ready_queue)
        [36, 51, 7]
        >>> finish_queue, ready_queue = mlfq.round_robin(ready_queue, 25)
        >>> mlfq.calculate_remaining_burst_time_of_processes(mlfq.finish_queue)
        [0, 0]
        >>> mlfq.calculate_remaining_burst_time_of_processes(ready_queue)
        [11, 26]
        """
        logger.warning("<<< Exiting calculate_remaining_burst_time_of_processes(queue=%s)", queue, extra={"event.action": "calculate_remaining_burst_time_of_processes", "logrite.queue": queue})
        return [q.burst_time for q in queue]

    def update_waiting_time(self, process: Process) -> int:
        """
        This method updates waiting times of unfinished processes
        >>> P1 = Process("P1", 0, 53)
        >>> P2 = Process("P2", 0, 17)
        >>> P3 = Process("P3", 0, 68)
        >>> P4 = Process("P4", 0, 24)
        >>> mlfq = MLFQ(3, [17, 25], deque([P1, P2, P3, P4]), 0)
        >>> mlfq.current_time = 10
        >>> P1.stop_time = 5
        >>> mlfq.update_waiting_time(P1)
        5
        """
        logger.error(">>> Entering update_waiting_time(process=%s)", process, extra={"event.action": "update_waiting_time", "logrite.process": process})
        process.waiting_time += self.current_time - process.stop_time
        logger.warning("<<< Exiting update_waiting_time(process=%s)", process, extra={"event.action": "update_waiting_time", "logrite.process": process})
        return process.waiting_time

    def first_come_first_served(self, ready_queue: deque[Process]) -> deque[Process]:
        """
        FCFS(First Come, First Served)
        FCFS will be applied to MLFQ's last queue
        A first came process will be finished at first
        >>> P1 = Process("P1", 0, 53)
        >>> P2 = Process("P2", 0, 17)
        >>> P3 = Process("P3", 0, 68)
        >>> P4 = Process("P4", 0, 24)
        >>> mlfq = MLFQ(3, [17, 25], deque([P1, P2, P3, P4]), 0)
        >>> _ = mlfq.first_come_first_served(mlfq.ready_queue)
        >>> mlfq.calculate_sequence_of_finish_queue()
        ['P1', 'P2', 'P3', 'P4']
        """
        logger.error(">>> Entering first_come_first_served(ready_queue=%s)", ready_queue, extra={"event.action": "first_come_first_served", "logrite.ready_queue": ready_queue})
        finished: deque[Process] = deque()  # sequence deque of finished process
        while len(ready_queue) != 0:
            cp = ready_queue.popleft()  # current process
            logger.error("first_come_first_served(ready_queue=%s): cp → %s", ready_queue, cp, extra={"event.action": "first_come_first_served", "logrite.ready_queue": ready_queue})

            # if process's arrival time is later than current time, update current time
            if self.current_time < cp.arrival_time:
                self.current_time += cp.arrival_time

            # update waiting time of current process
            self.update_waiting_time(cp)
            # update current time
            self.current_time += cp.burst_time
            # finish the process and set the process's burst-time 0
            cp.burst_time = 0
            logger.debug("first_come_first_served(self=%s,ready_queue=%s): cp.burst_time → %s", self, ready_queue, cp.burst_time, extra={"event.action": "first_come_first_served", "logrite.ready_queue": ready_queue})
            # set the process's turnaround time because it is finished
            cp.turnaround_time = self.current_time - cp.arrival_time
            logger.debug("first_come_first_served(self=%s,ready_queue=%s): cp.turnaround_time → %s", self, ready_queue, cp.turnaround_time, extra={"event.action": "first_come_first_served", "logrite.ready_queue": ready_queue})
            # set the completion time
            cp.stop_time = self.current_time
            logger.debug("first_come_first_served(self=%s,ready_queue=%s): cp.stop_time → %s", self, ready_queue, cp.stop_time, extra={"event.action": "first_come_first_served", "logrite.ready_queue": ready_queue})
            # add the process to queue that has finished queue
            finished.append(cp)

        self.finish_queue.extend(finished)  # add finished process to finish queue
        # FCFS will finish all remaining processes
        logger.warning("<<< Exiting first_come_first_served(ready_queue=%s)", ready_queue, extra={"event.action": "first_come_first_served", "logrite.ready_queue": ready_queue})
        return finished

    def round_robin(
        self, ready_queue: deque[Process], time_slice: int
    ) -> tuple[deque[Process], deque[Process]]:
        logger.error(">>> Entering round_robin(ready_queue=%s,time_slice=%s)", ready_queue, time_slice, extra={"event.action": "round_robin", "logrite.ready_queue": ready_queue, "logrite.time_slice": time_slice})
        """
        RR(Round Robin)
        RR will be applied to MLFQ's all queues except last queue
        All processes can't use CPU for time more than time_slice
        If the process consume CPU up to time_slice, it will go back to ready queue
        >>> P1 = Process("P1", 0, 53)
        >>> P2 = Process("P2", 0, 17)
        >>> P3 = Process("P3", 0, 68)
        >>> P4 = Process("P4", 0, 24)
        >>> mlfq = MLFQ(3, [17, 25], deque([P1, P2, P3, P4]), 0)
        >>> finish_queue, ready_queue = mlfq.round_robin(mlfq.ready_queue, 17)
        >>> mlfq.calculate_sequence_of_finish_queue()
        ['P2']
        """
        finished: deque[Process] = deque()  # sequence deque of terminated process
        # just for 1 cycle and unfinished processes will go back to queue
        for _ in range(len(ready_queue)):
            cp = ready_queue.popleft()  # current process
            logger.error("round_robin(ready_queue=%s,time_slice=%s): cp → %s", ready_queue, time_slice, cp, extra={"event.action": "round_robin", "logrite.ready_queue": ready_queue, "logrite.time_slice": time_slice})

            # if process's arrival time is later than current time, update current time
            if self.current_time < cp.arrival_time:
                self.current_time += cp.arrival_time

            # update waiting time of unfinished processes
            self.update_waiting_time(cp)
            # if the burst time of process is bigger than time-slice
            if cp.burst_time > time_slice:
                # use CPU for only time-slice
                self.current_time += time_slice
                # update remaining burst time
                cp.burst_time -= time_slice
                # update end point time
                cp.stop_time = self.current_time
                logger.debug("round_robin(self=%s,ready_queue=%s,time_slice=%s): cp.stop_time → %s", self, ready_queue, time_slice, cp.stop_time, extra={"event.action": "round_robin", "logrite.ready_queue": ready_queue, "logrite.time_slice": time_slice})
                # locate the process behind the queue because it is not finished
                ready_queue.append(cp)
            else:
                # use CPU for remaining burst time
                self.current_time += cp.burst_time
                # set burst time 0 because the process is finished
                cp.burst_time = 0
                logger.debug("round_robin(self=%s,ready_queue=%s,time_slice=%s): cp.burst_time → %s", self, ready_queue, time_slice, cp.burst_time, extra={"event.action": "round_robin", "logrite.ready_queue": ready_queue, "logrite.time_slice": time_slice})
                # set the finish time
                cp.stop_time = self.current_time
                # update the process' turnaround time because it is finished
                cp.turnaround_time = self.current_time - cp.arrival_time
                logger.debug("round_robin(self=%s,ready_queue=%s,time_slice=%s): cp.turnaround_time → %s", self, ready_queue, time_slice, cp.turnaround_time, extra={"event.action": "round_robin", "logrite.ready_queue": ready_queue, "logrite.time_slice": time_slice})
                # add the process to queue that has finished queue
                finished.append(cp)

        self.finish_queue.extend(finished)  # add finished process to finish queue
        # return finished processes queue and remaining processes queue
        logger.warning("<<< Exiting round_robin(ready_queue=%s,time_slice=%s)", ready_queue, time_slice, extra={"event.action": "round_robin", "logrite.ready_queue": ready_queue, "logrite.time_slice": time_slice})
        return finished, ready_queue

    def multi_level_feedback_queue(self) -> deque[Process]:
        """
        MLFQ(Multi Level Feedback Queue)
        >>> P1 = Process("P1", 0, 53)
        >>> P2 = Process("P2", 0, 17)
        >>> P3 = Process("P3", 0, 68)
        >>> P4 = Process("P4", 0, 24)
        >>> mlfq = MLFQ(3, [17, 25], deque([P1, P2, P3, P4]), 0)
        >>> finish_queue = mlfq.multi_level_feedback_queue()
        >>> mlfq.calculate_sequence_of_finish_queue()
        ['P2', 'P4', 'P1', 'P3']
        """
        logger.error(">>> Entering multi_level_feedback_queue()", extra={"event.action": "multi_level_feedback_queue"})

        #  all queues except last one have round_robin algorithm
        for i in range(self.number_of_queues - 1):
            _finished, self.ready_queue = self.round_robin(
                self.ready_queue, self.time_slices[i]
            )
        #  the last queue has first_come_first_served algorithm
        self.first_come_first_served(self.ready_queue)

        logger.warning("<<< Exiting multi_level_feedback_queue()", extra={"event.action": "multi_level_feedback_queue"})
        return self.finish_queue


if __name__ == "__main__":
    import doctest

    P1 = Process("P1", 0, 53)
    P2 = Process("P2", 0, 17)
    P3 = Process("P3", 0, 68)
    P4 = Process("P4", 0, 24)
    number_of_queues = 3
    time_slices = [17, 25]
    queue = deque([P1, P2, P3, P4])

    if len(time_slices) != number_of_queues - 1:
        raise SystemExit(0)

    doctest.testmod(extraglobs={"queue": deque([P1, P2, P3, P4])})

    P1 = Process("P1", 0, 53)
    P2 = Process("P2", 0, 17)
    P3 = Process("P3", 0, 68)
    P4 = Process("P4", 0, 24)
    number_of_queues = 3
    time_slices = [17, 25]
    queue = deque([P1, P2, P3, P4])
    mlfq = MLFQ(number_of_queues, time_slices, queue, 0)
    finish_queue = mlfq.multi_level_feedback_queue()

    # print total waiting times of processes(P1, P2, P3, P4)
    print(
        f"waiting time:\
        \t\t\t{MLFQ.calculate_waiting_time(mlfq, [P1, P2, P3, P4])}"
    )
    # print completion times of processes(P1, P2, P3, P4)
    print(
        f"completion time:\
        \t\t{MLFQ.calculate_completion_time(mlfq, [P1, P2, P3, P4])}"
    )
    # print total turnaround times of processes(P1, P2, P3, P4)
    print(
        f"turnaround time:\
        \t\t{MLFQ.calculate_turnaround_time(mlfq, [P1, P2, P3, P4])}"
    )
    # print sequence of finished processes
    print(
        f"sequence of finished processes:\
        {mlfq.calculate_sequence_of_finish_queue()}"
    )
