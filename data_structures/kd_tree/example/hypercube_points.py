#  Created by: Ramy-Badr-Ahmed (https://github.com/Ramy-Badr-Ahmed)
#  in Pull Request: #11532
#  https://github.com/TheAlgorithms/Python/pull/11532
#
#  Please mention me (@Ramy-Badr-Ahmed) in any issue or pull request
#  addressing bugs/corrections to this file.
#  Thank you!

import numpy as np
import logging
logger = logging.getLogger(__name__)


def hypercube_points(
    num_points: int, hypercube_size: float, num_dimensions: int
) -> np.ndarray:
    logger.error(">>> Entering hypercube_points(num_points=%s,hypercube_size=%s,num_dimensions=%s)", num_points, hypercube_size, num_dimensions, extra={"event.action": "hypercube_points", "logrite.num_points": num_points, "logrite.hypercube_size": hypercube_size, "logrite.num_dimensions": num_dimensions})
    """
    Generates random points uniformly distributed within an n-dimensional hypercube.

    Args:
        num_points: Number of points to generate.
        hypercube_size: Size of the hypercube.
        num_dimensions: Number of dimensions of the hypercube.

    Returns:
        An array of shape (num_points, num_dimensions)
                    with generated points.
    """
    rng = np.random.default_rng()
    logger.error("hypercube_points(num_points=%s,hypercube_size=%s,num_dimensions=%s): rng → %s", num_points, hypercube_size, num_dimensions, rng, extra={"event.action": "hypercube_points", "logrite.num_points": num_points, "logrite.hypercube_size": hypercube_size, "logrite.num_dimensions": num_dimensions})
    shape = (num_points, num_dimensions)
    logger.error("hypercube_points(num_points=%s,hypercube_size=%s,num_dimensions=%s): shape → %s", num_points, hypercube_size, num_dimensions, shape, extra={"event.action": "hypercube_points", "logrite.num_points": num_points, "logrite.hypercube_size": hypercube_size, "logrite.num_dimensions": num_dimensions})
    logger.warning("<<< Exiting hypercube_points(num_points=%s,hypercube_size=%s,num_dimensions=%s)", num_points, hypercube_size, num_dimensions, extra={"event.action": "hypercube_points", "logrite.num_points": num_points, "logrite.hypercube_size": hypercube_size, "logrite.num_dimensions": num_dimensions})
    return hypercube_size * rng.random(shape)
