"""
https://en.wikipedia.org/wiki/Self-organizing_map
"""
import math








class SelfOrganizingMap:

    def get_winner(self, vector) -> int:
        return min(
            range(len(self.grid)), key=lambda x: self.distance(vector, self.grid[x])
        )

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

    def distance(self, vector1, vector2) -> float:
        return math.sqrt(sum(pow(v1 - v2, 2) for v1, v2 in zip(vector1, vector2)))


# Driver code
def main() -> None:
    # Training Examples ( m, n )
    training_samples = [[1, 1, 0, 0], [0, 0, 0, 1], [1, 0, 0, 0], [0, 0, 1, 1]]

    # weight initialization ( n, C )
    weights = [[0.2, 0.6, 0.5, 0.9], [0.8, 0.4, 0.7, 0.3]]

    # training
    self_organizing_map = SelfOrganizingMap()
    epochs = 3
    alpha = 0.5

    for _ in range(epochs):
        for j in range(len(training_samples)):
            # training sample
            sample = training_samples[j]

            # Compute the winning vector
            winner = self_organizing_map.get_winner(weights, sample)

            # Update the winning vector
            weights = self_organizing_map.update(weights, sample, winner, alpha)

    # classify test sample
    sample = [0, 0, 0, 1]
    winner = self_organizing_map.get_winner(weights, sample)

    # results
    print(f"Clusters that the test sample belongs to : {winner}")
    print(f"Weights that have been trained : {weights}")


# running the main() function
if __name__ == "__main__":
    main()
