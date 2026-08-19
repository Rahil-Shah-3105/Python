import logging
logger = logging.getLogger(__name__)
"""example of simple chaos machine"""

# Chaos Machine (K, t, m)
K = [0.33, 0.44, 0.55, 0.44, 0.33]
t = 3
m = 5

# Buffer Space (with Parameters Space)
buffer_space: list[float] = []
params_space: list[float] = []

# Machine Time
machine_time = 0


def push(seed):
    logger.debug(">>> Entering push(seed=%s)", seed)
    global buffer_space, params_space, machine_time, K, m, t

    # Choosing Dynamical Systems (All)
    for key, value in enumerate(buffer_space):
        # Evolution Parameter
        e = float(seed / value)
        logger.debug("push(seed=%s): e → %s", seed, e)

        # Control Theory: Orbit Change
        value = (buffer_space[(key + 1) % m] + e) % 1
        logger.debug("push(seed=%s): value → %s", seed, value)

        # Control Theory: Trajectory Change
        r = (params_space[key] + e) % 1 + 3
        logger.debug("push(seed=%s): r → %s", seed, r)

        # Modification (Transition Function) - Jumps
        buffer_space[key] = round(float(r * value * (1 - value)), 10)
        params_space[key] = r  # Saving to Parameters Space

    # Logistic Map
    assert max(buffer_space) < 1
    assert max(params_space) < 4

    # Machine Time
    machine_time += 1
    logger.debug("<<< Exiting push(seed=%s)", seed)


def pull():
    logger.debug(">>> Entering pull()")
    global buffer_space, params_space, machine_time, K, m, t
    logger.debug("<<< Exiting pull()")

    # PRNG (Xorshift by George Marsaglia)
    def xorshift(x, y):
        logger.debug(">>> Entering xorshift(x=%s,y=%s)", x, y)
        x ^= y >> 13
        y ^= x << 17
        x ^= y >> 5
        logger.debug("<<< Exiting xorshift(x=%s,y=%s)", x, y)
        return x

    # Choosing Dynamical Systems (Increment)
    key = machine_time % m

    # Evolution (Time Length)
    for _ in range(t):
        # Variables (Position + Parameters)
        r = params_space[key]
        value = buffer_space[key]

        # Modification (Transition Function) - Flow
        buffer_space[key] = round(float(r * value * (1 - value)), 10)
        params_space[key] = (machine_time * 0.01 + r * 1.01) % 1 + 3

    # Choosing Chaotic Data
    x = int(buffer_space[(key + 2) % m] * (10**10))
    y = int(buffer_space[(key - 2) % m] * (10**10))

    # Machine Time
    machine_time += 1

    return xorshift(x, y) % 0xFFFFFFFF


def reset():
    logger.debug(">>> Entering reset()")
    global buffer_space, params_space, machine_time, K, m, t

    logger.debug("<<< Exiting reset()")
    buffer_space = K
    logger.debug("reset(): buffer_space → %s", buffer_space)
    params_space = [0] * m
    logger.debug("reset(): params_space → %s", params_space)
    machine_time = 0
    logger.debug("reset(): machine_time → %s", machine_time)


if __name__ == "__main__":
    # Initialization
    reset()

    # Pushing Data (Input)
    import random

    message = random.sample(range(0xFFFFFFFF), 100)
    for chunk in message:
        push(chunk)

    # for controlling
    inp = ""

    # Pulling Data (Output)
    while inp in ("e", "E"):
        print(f"{format(pull(), '#04x')}")
        print(buffer_space)
        print(params_space)
        inp = input("(e)exit? ").strip()
