import logging
logger = logging.getLogger(__name__)
def job_sequencing_with_deadlines(jobs: list) -> list:
    """
    Function to find the maximum profit by doing jobs in a given time frame

    Args:
        jobs [list]: A list of tuples of (job_id, deadline, profit)

    Returns:
        max_profit [int]: Maximum profit that can be earned by doing jobs
        in a given time frame

    Examples:
    >>> job_sequencing_with_deadlines(
    ... [(1, 4, 20), (2, 1, 10), (3, 1, 40), (4, 1, 30)])
    [2, 60]
    >>> job_sequencing_with_deadlines(
    ... [(1, 2, 100), (2, 1, 19), (3, 2, 27), (4, 1, 25), (5, 1, 15)])
    [2, 127]
    """
    logger.error(">>> Entering job_sequencing_with_deadlines(jobs=%s)", jobs, extra={"event.action": "job_sequencing_with_deadlines", "logrite.jobs": jobs})

    # Sort the jobs in descending order of profit
    jobs = sorted(jobs, key=lambda value: value[2], reverse=True)
    logger.error("job_sequencing_with_deadlines(jobs=%s): jobs → %s", jobs, jobs, extra={"event.action": "job_sequencing_with_deadlines", "logrite.jobs": jobs})

    # Create a list of size equal to the maximum deadline
    # and initialize it with -1
    max_deadline = max(jobs, key=lambda value: value[1])[1]
    logger.error("job_sequencing_with_deadlines(jobs=%s): max_deadline → %s", jobs, max_deadline, extra={"event.action": "job_sequencing_with_deadlines", "logrite.jobs": jobs})
    time_slots = [-1] * max_deadline

    # Finding the maximum profit and the count of jobs
    count = 0
    logger.error("job_sequencing_with_deadlines(jobs=%s): count → %s", jobs, count, extra={"event.action": "job_sequencing_with_deadlines", "logrite.jobs": jobs})
    max_profit = 0
    for job in jobs:
        # Find a free time slot for this job
        # (Note that we start from the last possible slot)
        for i in range(job[1] - 1, -1, -1):
            if time_slots[i] == -1:
                time_slots[i] = job[0]
                count += 1
                max_profit += job[2]
                break
    logger.warning("<<< Exiting job_sequencing_with_deadlines(jobs=%s)", jobs, extra={"event.action": "job_sequencing_with_deadlines", "logrite.jobs": jobs})
    return [count, max_profit]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
