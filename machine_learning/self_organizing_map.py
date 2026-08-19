"""
https://en.wikipedia.org/wiki/Self-organizing_map
"""

import math
import logging
logger = logging.getLogger(__name__)


class SelfOrganizingMap:
    def get_winner(self, weights: list[list[float]], sample: list[int]) -> int:
        """
        Compute the winning vector by Euclidean distance

        >>> SelfOrganizingMap().get_winner([[1, 2, 3], [4, 5, 6]], [1, 2, 3])
        1
        """
        logger.debug(">>> Entering get_winner(weights=%s,sample=%s)", weights, sample)
        d0 = 0.0
        d1 = 0.0
        for i in range(len(sample)):
            d0 += math.pow((sample[i] - weights[0][i]), 2)
            d1 += math.pow((sample[i] - weights[1][i]), 2)
            return 0 if d0 > d1 else 1
        logger.debug("<<< Exiting get_winner(weights=%s,sample=%s)", weights, sample)
        return 0

    def update(
        self, weights: list[list[int | float]], sample: list[int], j: int, alpha: float
    ) -> list[list[int | float]]:
        """
        Update the winning vector.

        >>> SelfOrganizingMap().update([[1, 2, 3], [4, 5, 6]], [1, 2, 3], 1, 0.1)
        [[1, 2, 3], [3.7, 4.7, 6]]
        """
        for i in range(len(weights)):
            weights[j][i] += alpha * (sample[i] - weights[j][i])
        return weights


# Driver code
def main() -> None:
    logger.debug(">>> Entering main()")
    # Training Examples ( m, n )
    training_samples = [[1, 1, 0, 0], [0, 0, 0, 1], [1, 0, 0, 0], [0, 0, 1, 1]]
    logger.debug("main(): training_samples → %s", training_samples)

    # weight initialization ( n, C )
    weights = [[0.2, 0.6, 0.5, 0.9], [0.8, 0.4, 0.7, 0.3]]
    logger.debug("main(): weights → %s", weights)

    # training
    self_organizing_map = SelfOrganizingMap()
    logger.debug("main(): self_organizing_map → %s", self_organizing_map)
    epochs = 3
    logger.debug("main(): epochs → %s", epochs)
    alpha = 0.5
    logger.debug("main(): alpha → %s", alpha)

    for _ in range(epochs):
        for j in range(len(training_samples)):
            # training sample
            sample = training_samples[j]
            logger.debug("main(): sample → %s", sample)

            # Compute the winning vector
            winner = self_organizing_map.get_winner(weights, sample)
            logger.debug("main(): winner → %s", winner)

            # Update the winning vector
            weights = self_organizing_map.update(weights, sample, winner, alpha)

    # classify test sample
    sample = [0, 0, 0, 1]
    winner = self_organizing_map.get_winner(weights, sample)

    # results
    print(f"Clusters that the test sample belongs to : {winner}")
    print(f"Weights that have been trained : {weights}")
    logger.debug("<<< Exiting main()")


# running the main() function
if __name__ == "__main__":
    main()
