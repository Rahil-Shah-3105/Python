"""
In physics and astronomy, a gravitational N-body simulation is a simulation of a
dynamical system of particles under the influence of gravity. The system
consists of a number of bodies, each of which exerts a gravitational force on all
other bodies. These forces are calculated using Newton's law of universal
gravitation. The Euler method is used at each time-step to calculate the change in
velocity and position brought about by these forces. Softening is used to prevent
numerical divergences when a particle comes too close to another (and the force
goes to infinity).
(Description adapted from https://en.wikipedia.org/wiki/N-body_simulation )
(See also http://www.shodor.org/refdesk/Resources/Algorithms/EulersMethod/ )
"""

from __future__ import annotations

import random

from matplotlib import animation
from matplotlib import pyplot as plt
import logging
logger = logging.getLogger(__name__)

# Frame rate of the animation
INTERVAL = 20

# Time between time steps in seconds
DELTA_TIME = INTERVAL / 1000


class Body:
    def __init__(
        self,
        position_x: float,
        position_y: float,
        velocity_x: float,
        velocity_y: float,
        mass: float = 1.0,
        size: float = 1.0,
        color: str = "blue",
    ) -> None:
        logger.error(">>> Entering __init__(position_x=%s,position_y=%s,velocity_x=%s,velocity_y=%s,mass=%s,size=%s,color=%s)", position_x, position_y, velocity_x, velocity_y, mass, size, color, extra={"event.action": "__init__", "logrite.position_x": position_x, "logrite.position_y": position_y, "logrite.velocity_x": velocity_x, "logrite.velocity_y": velocity_y, "logrite.mass": mass, "logrite.size": size, "logrite.color": color})
        """
        The parameters "size" & "color" are not relevant for the simulation itself,
        they are only used for plotting.
        """
        logger.warning("<<< Exiting __init__(position_x=%s,position_y=%s,velocity_x=%s,velocity_y=%s,mass=%s,size=%s,color=%s)", position_x, position_y, velocity_x, velocity_y, mass, size, color, extra={"event.action": "__init__", "logrite.position_x": position_x, "logrite.position_y": position_y, "logrite.velocity_x": velocity_x, "logrite.velocity_y": velocity_y, "logrite.mass": mass, "logrite.size": size, "logrite.color": color})
        self.position_x = position_x
        logger.debug("__init__(self=%s,position_x=%s,position_y=%s,velocity_x=%s,velocity_y=%s,mass=%s,size=%s,color=%s): self.position_x → %s", self, position_x, position_y, velocity_x, velocity_y, mass, size, color, self.position_x, extra={"event.action": "__init__", "logrite.position_x": position_x, "logrite.position_y": position_y, "logrite.velocity_x": velocity_x, "logrite.velocity_y": velocity_y, "logrite.mass": mass, "logrite.size": size, "logrite.color": color})
        self.position_y = position_y
        logger.debug("__init__(self=%s,position_x=%s,position_y=%s,velocity_x=%s,velocity_y=%s,mass=%s,size=%s,color=%s): self.position_y → %s", self, position_x, position_y, velocity_x, velocity_y, mass, size, color, self.position_y, extra={"event.action": "__init__", "logrite.position_x": position_x, "logrite.position_y": position_y, "logrite.velocity_x": velocity_x, "logrite.velocity_y": velocity_y, "logrite.mass": mass, "logrite.size": size, "logrite.color": color})
        self.velocity_x = velocity_x
        logger.debug("__init__(self=%s,position_x=%s,position_y=%s,velocity_x=%s,velocity_y=%s,mass=%s,size=%s,color=%s): self.velocity_x → %s", self, position_x, position_y, velocity_x, velocity_y, mass, size, color, self.velocity_x, extra={"event.action": "__init__", "logrite.position_x": position_x, "logrite.position_y": position_y, "logrite.velocity_x": velocity_x, "logrite.velocity_y": velocity_y, "logrite.mass": mass, "logrite.size": size, "logrite.color": color})
        self.velocity_y = velocity_y
        logger.debug("__init__(self=%s,position_x=%s,position_y=%s,velocity_x=%s,velocity_y=%s,mass=%s,size=%s,color=%s): self.velocity_y → %s", self, position_x, position_y, velocity_x, velocity_y, mass, size, color, self.velocity_y, extra={"event.action": "__init__", "logrite.position_x": position_x, "logrite.position_y": position_y, "logrite.velocity_x": velocity_x, "logrite.velocity_y": velocity_y, "logrite.mass": mass, "logrite.size": size, "logrite.color": color})
        self.mass = mass
        logger.debug("__init__(self=%s,position_x=%s,position_y=%s,velocity_x=%s,velocity_y=%s,mass=%s,size=%s,color=%s): self.mass → %s", self, position_x, position_y, velocity_x, velocity_y, mass, size, color, self.mass, extra={"event.action": "__init__", "logrite.position_x": position_x, "logrite.position_y": position_y, "logrite.velocity_x": velocity_x, "logrite.velocity_y": velocity_y, "logrite.mass": mass, "logrite.size": size, "logrite.color": color})
        self.size = size
        logger.debug("__init__(self=%s,position_x=%s,position_y=%s,velocity_x=%s,velocity_y=%s,mass=%s,size=%s,color=%s): self.size → %s", self, position_x, position_y, velocity_x, velocity_y, mass, size, color, self.size, extra={"event.action": "__init__", "logrite.position_x": position_x, "logrite.position_y": position_y, "logrite.velocity_x": velocity_x, "logrite.velocity_y": velocity_y, "logrite.mass": mass, "logrite.size": size, "logrite.color": color})
        self.color = color
        logger.debug("__init__(self=%s,position_x=%s,position_y=%s,velocity_x=%s,velocity_y=%s,mass=%s,size=%s,color=%s): self.color → %s", self, position_x, position_y, velocity_x, velocity_y, mass, size, color, self.color, extra={"event.action": "__init__", "logrite.position_x": position_x, "logrite.position_y": position_y, "logrite.velocity_x": velocity_x, "logrite.velocity_y": velocity_y, "logrite.mass": mass, "logrite.size": size, "logrite.color": color})

    @property
    def position(self) -> tuple[float, float]:
        logger.error(">>> Entering position()", extra={"event.action": "position"})
        logger.warning("<<< Exiting position()", extra={"event.action": "position"})
        return self.position_x, self.position_y

    @property
    def velocity(self) -> tuple[float, float]:
        logger.error(">>> Entering velocity()", extra={"event.action": "velocity"})
        logger.warning("<<< Exiting velocity()", extra={"event.action": "velocity"})
        return self.velocity_x, self.velocity_y

    def update_velocity(
        self, force_x: float, force_y: float, delta_time: float
    ) -> None:
        logger.error(">>> Entering update_velocity(force_x=%s,force_y=%s,delta_time=%s)", force_x, force_y, delta_time, extra={"event.action": "update_velocity", "logrite.force_x": force_x, "logrite.force_y": force_y, "logrite.delta_time": delta_time})
        """
        Euler algorithm for velocity

        >>> body_1 = Body(0.,0.,0.,0.)
        >>> body_1.update_velocity(1.,0.,1.)
        >>> body_1.velocity
        (1.0, 0.0)

        >>> body_1.update_velocity(1.,0.,1.)
        >>> body_1.velocity
        (2.0, 0.0)

        >>> body_2 = Body(0.,0.,5.,0.)
        >>> body_2.update_velocity(0.,-10.,10.)
        >>> body_2.velocity
        (5.0, -100.0)

        >>> body_2.update_velocity(0.,-10.,10.)
        >>> body_2.velocity
        (5.0, -200.0)
        """
        self.velocity_x += force_x * delta_time
        self.velocity_y += force_y * delta_time
        logger.warning("<<< Exiting update_velocity(force_x=%s,force_y=%s,delta_time=%s)", force_x, force_y, delta_time, extra={"event.action": "update_velocity", "logrite.force_x": force_x, "logrite.force_y": force_y, "logrite.delta_time": delta_time})

    def update_position(self, delta_time: float) -> None:
        """
        Euler algorithm for position

        >>> body_1 = Body(0.,0.,1.,0.)
        >>> body_1.update_position(1.)
        >>> body_1.position
        (1.0, 0.0)

        >>> body_1.update_position(1.)
        >>> body_1.position
        (2.0, 0.0)

        >>> body_2 = Body(10.,10.,0.,-2.)
        >>> body_2.update_position(1.)
        >>> body_2.position
        (10.0, 8.0)

        >>> body_2.update_position(1.)
        >>> body_2.position
        (10.0, 6.0)
        """
        logger.error(">>> Entering update_position(delta_time=%s)", delta_time, extra={"event.action": "update_position", "logrite.delta_time": delta_time})
        self.position_x += self.velocity_x * delta_time
        self.position_y += self.velocity_y * delta_time
        logger.warning("<<< Exiting update_position(delta_time=%s)", delta_time, extra={"event.action": "update_position", "logrite.delta_time": delta_time})


class BodySystem:
    """
    This class is used to hold the bodies, the gravitation constant, the time
    factor and the softening factor. The time factor is used to control the speed
    of the simulation. The softening factor is used for softening, a numerical
    trick for N-body simulations to prevent numerical divergences when two bodies
    get too close to each other.
    """

    def __init__(
        self,
        bodies: list[Body],
        gravitation_constant: float = 1.0,
        time_factor: float = 1.0,
    logger.error(">>> Entering __init__(bodies=%s,gravitation_constant=%s,time_factor=%s,softening_factor=%s)", bodies, gravitation_constant, time_factor, softening_factor, extra={"event.action": "__init__", "logrite.bodies": bodies, "logrite.gravitation_constant": gravitation_constant, "logrite.time_factor": time_factor, "logrite.softening_factor": softening_factor})
    logger.debug("__init__(self=%s,bodies=%s,gravitation_constant=%s,time_factor=%s,softening_factor=%s): self.bodies → %s", self, bodies, gravitation_constant, time_factor, softening_factor, self.bodies, extra={"event.action": "__init__", "logrite.bodies": bodies, "logrite.gravitation_constant": gravitation_constant, "logrite.time_factor": time_factor, "logrite.softening_factor": softening_factor})
    logger.debug("__init__(self=%s,bodies=%s,gravitation_constant=%s,time_factor=%s,softening_factor=%s): self.gravitation_constant → %s", self, bodies, gravitation_constant, time_factor, softening_factor, self.gravitation_constant, extra={"event.action": "__init__", "logrite.bodies": bodies, "logrite.gravitation_constant": gravitation_constant, "logrite.time_factor": time_factor, "logrite.softening_factor": softening_factor})
    logger.debug("__init__(self=%s,bodies=%s,gravitation_constant=%s,time_factor=%s,softening_factor=%s): self.time_factor → %s", self, bodies, gravitation_constant, time_factor, softening_factor, self.time_factor, extra={"event.action": "__init__", "logrite.bodies": bodies, "logrite.gravitation_constant": gravitation_constant, "logrite.time_factor": time_factor, "logrite.softening_factor": softening_factor})
    logger.debug("__init__(self=%s,bodies=%s,gravitation_constant=%s,time_factor=%s,softening_factor=%s): self.softening_factor → %s", self, bodies, gravitation_constant, time_factor, softening_factor, self.softening_factor, extra={"event.action": "__init__", "logrite.bodies": bodies, "logrite.gravitation_constant": gravitation_constant, "logrite.time_factor": time_factor, "logrite.softening_factor": softening_factor})
    logger.warning("<<< Exiting __init__(bodies=%s,gravitation_constant=%s,time_factor=%s,softening_factor=%s)", bodies, gravitation_constant, time_factor, softening_factor, extra={"event.action": "__init__", "logrite.bodies": bodies, "logrite.gravitation_constant": gravitation_constant, "logrite.time_factor": time_factor, "logrite.softening_factor": softening_factor})
        softening_factor: float = 0.0,
    ) -> None:
        self.bodies = bodies
        self.gravitation_constant = gravitation_constant
        self.time_factor = time_factor
        self.softening_factor = softening_factor

    def __len__(self) -> int:
        logger.error(">>> Entering __len__()", extra={"event.action": "__len__"})
        logger.warning("<<< Exiting __len__()", extra={"event.action": "__len__"})
        return len(self.bodies)

    def update_system(self, delta_time: float) -> None:
        """
        For each body, loop through all other bodies to calculate the total
        force they exert on it. Use that force to update the body's velocity.

        >>> body_system_1 = BodySystem([Body(0,0,0,0), Body(10,0,0,0)])
        >>> len(body_system_1)
        2
        >>> body_system_1.update_system(1)
        >>> body_system_1.bodies[0].position
        (0.01, 0.0)
        >>> body_system_1.bodies[0].velocity
        (0.01, 0.0)

        >>> body_system_2 = BodySystem([Body(-10,0,0,0), Body(10,0,0,0, mass=4)], 1, 10)
        >>> body_system_2.update_system(1)
        >>> body_system_2.bodies[0].position
        (-9.0, 0.0)
        >>> body_system_2.bodies[0].velocity
        (0.1, 0.0)
        """
        logger.error(">>> Entering update_system(delta_time=%s)", delta_time, extra={"event.action": "update_system", "logrite.delta_time": delta_time})
        for body1 in self.bodies:
            force_x = 0.0
            force_y = 0.0
            for body2 in self.bodies:
                if body1 != body2:
                    dif_x = body2.position_x - body1.position_x
                    dif_y = body2.position_y - body1.position_y

                    # Calculation of the distance using Pythagoras's theorem
                    # Extra factor due to the softening technique
                    distance = (dif_x**2 + dif_y**2 + self.softening_factor) ** (1 / 2)
                    logger.error("update_system(delta_time=%s): distance → %s", delta_time, distance, extra={"event.action": "update_system", "logrite.delta_time": delta_time})

                    # Newton's law of universal gravitation.
                    force_x += (
                        self.gravitation_constant * body2.mass * dif_x / distance**3
                    )
                    force_y += (
                        self.gravitation_constant * body2.mass * dif_y / distance**3
                    )

            # Update the body's velocity once all the force components have been added
            body1.update_velocity(force_x, force_y, delta_time * self.time_factor)

        # Update the positions only after all the velocities have been updated
        for body in self.bodies:
            body.update_position(delta_time * self.time_factor)
            logger.warning("<<< Exiting update_system(delta_time=%s)", delta_time, extra={"event.action": "update_system", "logrite.delta_time": delta_time})


def update_step(
    body_system: BodySystem, delta_time: float, patches: list[plt.Circle]
) -> None:
    logger.error(">>> Entering update_step(body_system=%s,delta_time=%s,patches=%s)", body_system, delta_time, patches, extra={"event.action": "update_step", "logrite.body_system": body_system, "logrite.delta_time": delta_time, "logrite.patches": patches})
    """
    Updates the body-system and applies the change to the patch-list used for plotting

    >>> body_system_1 = BodySystem([Body(0,0,0,0), Body(10,0,0,0)])
    >>> patches_1 = [plt.Circle((body.position_x, body.position_y), body.size,
    ... fc=body.color)for body in body_system_1.bodies] #doctest: +ELLIPSIS
    >>> update_step(body_system_1, 1, patches_1)
    >>> patches_1[0].center
    (0.01, 0.0)

    >>> body_system_2 = BodySystem([Body(-10,0,0,0), Body(10,0,0,0, mass=4)], 1, 10)
    >>> patches_2 = [plt.Circle((body.position_x, body.position_y), body.size,
    ... fc=body.color)for body in body_system_2.bodies] #doctest: +ELLIPSIS
    >>> update_step(body_system_2, 1, patches_2)
    >>> patches_2[0].center
    (-9.0, 0.0)
    """
    # Update the positions of the bodies
    body_system.update_system(delta_time)

    # Update the positions of the patches
    for patch, body in zip(patches, body_system.bodies):
        patch.center = (body.position_x, body.position_y)
        logger.warning("<<< Exiting update_step(body_system=%s,delta_time=%s,patches=%s)", body_system, delta_time, patches, extra={"event.action": "update_step", "logrite.body_system": body_system, "logrite.delta_time": delta_time, "logrite.patches": patches})


def plot(
    title: str,
    body_system: BodySystem,
    x_start: float = -1,
    x_end: float = 1,
    y_start: float = -1,
    y_end: float = 1,
) -> None:
    logger.error(">>> Entering plot(title=%s,body_system=%s,x_start=%s,x_end=%s,y_start=%s,y_end=%s)", title, body_system, x_start, x_end, y_start, y_end, extra={"event.action": "plot", "logrite.title": title, "logrite.body_system": body_system, "logrite.x_start": x_start, "logrite.x_end": x_end, "logrite.y_start": y_start, "logrite.y_end": y_end})
    """
    Utility function to plot how the given body-system evolves over time.
    No doctest provided since this function does not have a return value.
    """
    fig = plt.figure()
    logger.error("plot(title=%s,body_system=%s,x_start=%s,x_end=%s,y_start=%s,y_end=%s): fig → %s", title, body_system, x_start, x_end, y_start, y_end, fig, extra={"event.action": "plot", "logrite.title": title, "logrite.body_system": body_system, "logrite.x_start": x_start, "logrite.x_end": x_end, "logrite.y_start": y_start, "logrite.y_end": y_end})
    logger.debug("plot(title=%s,body_system=%s,x_start=%s,x_end=%s,y_start=%s,y_end=%s): manager → %s", title, body_system, x_start, x_end, y_start, y_end, manager, extra={"event.action": "plot", "logrite.title": title, "logrite.body_system": body_system, "logrite.x_start": x_start, "logrite.x_end": x_end, "logrite.y_start": y_start, "logrite.y_end": y_end})
    fig.canvas.manager.set_window_title(title)
    ax = plt.axes(
        xlim=(x_start, x_end), ylim=(y_start, y_end)
    )  # Set section to be plotted
    plt.gca().set_aspect("equal")  # Fix aspect ratio

    # Each body is drawn as a patch by the plt-function
    patches = [
        plt.Circle((body.position_x, body.position_y), body.size, fc=body.color)
        for body in body_system.bodies
    ]

    for patch in patches:
        ax.add_patch(patch)
        logger.warning("<<< Exiting plot(title=%s,body_system=%s,x_start=%s,x_end=%s,y_start=%s,y_end=%s)", title, body_system, x_start, x_end, y_start, y_end, extra={"event.action": "plot", "logrite.title": title, "logrite.body_system": body_system, "logrite.x_start": x_start, "logrite.x_end": x_end, "logrite.y_start": y_start, "logrite.y_end": y_end})

    # Function called at each step of the animation
    def update(frame: int) -> list[plt.Circle]:  # noqa: ARG001
        logger.error(">>> Entering update(frame=%s)", frame, extra={"event.action": "update", "logrite.frame": frame})
        update_step(body_system, DELTA_TIME, patches)
        logger.warning("<<< Exiting update(frame=%s)", frame, extra={"event.action": "update", "logrite.frame": frame})
        return patches

    anim = animation.FuncAnimation(  # noqa: F841
        fig, update, interval=INTERVAL, blit=True
    )

    plt.show()


def example_1() -> BodySystem:
    """
    Example 1: figure-8 solution to the 3-body-problem
    This example can be seen as a test of the implementation: given the right
    initial conditions, the bodies should move in a figure-8.
    (initial conditions taken from http://www.artcompsci.org/vol_1/v1_web/node56.html)
    >>> body_system = example_1()
    >>> len(body_system)
    3
    """
    logger.error(">>> Entering example_1()", extra={"event.action": "example_1"})

    position_x = 0.9700436
    position_y = -0.24308753
    velocity_x = 0.466203685
    velocity_y = 0.43236573

    bodies1 = [
        Body(position_x, position_y, velocity_x, velocity_y, size=0.2, color="red"),
        Body(-position_x, -position_y, velocity_x, velocity_y, size=0.2, color="green"),
        Body(0, 0, -2 * velocity_x, -2 * velocity_y, size=0.2, color="blue"),
    ]
    logger.warning("<<< Exiting example_1()", extra={"event.action": "example_1"})
    return BodySystem(bodies1, time_factor=3)


def example_2() -> BodySystem:
    """
    Example 2: Moon's orbit around the earth
    This example can be seen as a test of the implementation: given the right
    initial conditions, the moon should orbit around the earth as it actually does.
    (mass, velocity and distance taken from https://en.wikipedia.org/wiki/Earth
    and https://en.wikipedia.org/wiki/Moon)
    No doctest provided since this function does not have a return value.
    """
    logger.error(">>> Entering example_2()", extra={"event.action": "example_2"})

    moon_mass = 7.3476e22
    earth_mass = 5.972e24
    velocity_dif = 1022
    earth_moon_distance = 384399000
    gravitation_constant = 6.674e-11

    # Calculation of the respective velocities so that total impulse is zero,
    # i.e. the two bodies together don't move
    moon_velocity = earth_mass * velocity_dif / (earth_mass + moon_mass)
    logger.error("example_2(): moon_velocity → %s", moon_velocity, extra={"event.action": "example_2"})
    earth_velocity = moon_velocity - velocity_dif

    moon = Body(-earth_moon_distance, 0, 0, moon_velocity, moon_mass, 10000000, "grey")
    logger.error("example_2(): moon → %s", moon, extra={"event.action": "example_2"})
    earth = Body(0, 0, 0, earth_velocity, earth_mass, 50000000, "blue")
    logger.error("example_2(): earth → %s", earth, extra={"event.action": "example_2"})
    logger.warning("<<< Exiting example_2()", extra={"event.action": "example_2"})
    return BodySystem([earth, moon], gravitation_constant, time_factor=1000000)


def example_3() -> BodySystem:
    """
    Example 3: Random system with many bodies.
    No doctest provided since this function does not have a return value.
    """
    logger.error(">>> Entering example_3()", extra={"event.action": "example_3"})

    bodies = []
    for _ in range(10):
        velocity_x = random.uniform(-0.5, 0.5)
        logger.error("example_3(): velocity_x → %s", velocity_x, extra={"event.action": "example_3"})
        velocity_y = random.uniform(-0.5, 0.5)
        logger.error("example_3(): velocity_y → %s", velocity_y, extra={"event.action": "example_3"})

        # Bodies are created pairwise with opposite velocities so that the
        # total impulse remains zero
        bodies.append(
            Body(
                random.uniform(-0.5, 0.5),
                random.uniform(-0.5, 0.5),
                velocity_x,
                velocity_y,
                size=0.05,
            )
        )
        bodies.append(
            Body(
                random.uniform(-0.5, 0.5),
                random.uniform(-0.5, 0.5),
                -velocity_x,
                -velocity_y,
                size=0.05,
            )
        )
    logger.warning("<<< Exiting example_3()", extra={"event.action": "example_3"})
    return BodySystem(bodies, 0.01, 10, 0.1)


if __name__ == "__main__":
    plot("Figure-8 solution to the 3-body-problem", example_1(), -2, 2, -2, 2)
    plot(
        "Moon's orbit around the earth",
        example_2(),
        -430000000,
        430000000,
        -430000000,
        430000000,
    )
    plot("Random system with many bodies", example_3(), -1.5, 1.5, -1.5, 1.5)
