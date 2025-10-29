import math

def k_means(data, k, max_iterations=100):
    n = len(data)

    centroids = [list(data[i]) for i in range(k)]
    assignments = [0] * n

    for _ in range(max_iterations):
        for i in range(n):
            min_distance = float("inf")
            cluster_id = -1
            for j in range(k):
                dist = math.sqrt(
                    (data[i][0] - centroids[j][0]) ** 2 +
                    (data[i][1] - centroids[j][1]) ** 2
                )
                if dist < min_distance:
                    min_distance = dist
                    cluster_id = j
            assignments[i] = cluster_id

        new_centroids = [[0, 0] for _ in range(k)]
        counts = [0] * k

        for i in range(n):
            cluster_id = assignments[i]
            new_centroids[cluster_id][0] += data[i][0]
            new_centroids[cluster_id][1] += data[i][1]
            counts[cluster_id] += 1

        for i in range(k):
            if counts[i] > 0:
                centroids[i][0] = new_centroids[i][0] / counts[i]
                centroids[i][1] = new_centroids[i][1] / counts[i]
                
    return assignments, centroids


if __name__ == "__main__":
    n = int(input("Enter the number of data points: "))

    data = []
    for i in range(n):
        x = float(input(f"Enter x for point {i+1}: "))
        y = float(input(f"Enter y for point {i+1}: "))
        data.append((x, y))

    k = int(input("Enter the number of clusters (k): "))

    assignments, centroids = k_means(data, k)

    print("\nFinal cluster assignments:")
    for (x, y), cluster in zip(data, assignments):
        print(f"Point ({x:.2f}, {y:.2f}) -> Cluster {cluster + 1}")

    print("\nFinal centroids:")
    for i, (cx, cy) in enumerate(centroids, start=1):
        print(f"Cluster {i} centroid: ({cx:.2f}, {cy:.2f})")
