"""example of simple chaos machine"""
import logging
logger = logging.getLogger(__name__)

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
    logger.error(">>> Entering push(seed=%s)", seed, extra={"event.action": "push", "logrite.seed": seed})
    global buffer_space, params_space, machine_time, K, m, t

    # Choosing Dynamical Systems (All)
    for key, value in enumerate(buffer_space):
        # Evolution Parameter
        e = float(seed / value)
        logger.error("push(seed=%s): e → %s", seed, e, extra={"event.action": "push", "logrite.seed": seed})

        # Control Theory: Orbit Change
        value = (buffer_space[(key + 1) % m] + e) % 1
        logger.error("push(seed=%s): value → %s", seed, value, extra={"event.action": "push", "logrite.seed": seed})

        # Control Theory: Trajectory Change
        r = (params_space[key] + e) % 1 + 3
        logger.error("push(seed=%s): r → %s", seed, r, extra={"event.action": "push", "logrite.seed": seed})

        # Modification (Transition Function) - Jumps
        buffer_space[key] = round(float(r * value * (1 - value)), 10)
        params_space[key] = r  # Saving to Parameters Space

    # Logistic Map
    assert max(buffer_space) < 1
    assert max(params_space) < 4

    # Machine Time
    machine_time += 1
    logger.warning("<<< Exiting push(seed=%s)", seed, extra={"event.action": "push", "logrite.seed": seed})


def pull():
    logger.error(">>> Entering pull()", extra={"event.action": "pull"})
    global buffer_space, params_space, machine_time, K, m, t
    logger.warning("<<< Exiting pull()", extra={"event.action": "pull"})

    # PRNG (Xorshift by George Marsaglia)
    def xorshift(x, y):
        logger.error(">>> Entering xorshift(x=%s,y=%s)", x, y, extra={"event.action": "xorshift", "logrite.x": x, "logrite.y": y})
        x ^= y >> 13
        y ^= x << 17
        x ^= y >> 5
        logger.warning("<<< Exiting xorshift(x=%s,y=%s)", x, y, extra={"event.action": "xorshift", "logrite.x": x, "logrite.y": y})
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
    logger.error(">>> Entering reset()", extra={"event.action": "reset"})
    global buffer_space, params_space, machine_time, K, m, t

    buffer_space = K
    params_space = [0] * m
    machine_time = 0
    logger.warning("<<< Exiting reset()", extra={"event.action": "reset"})


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
