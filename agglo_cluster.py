import math

def single_linkage_clustering(points):
    n = len(points)
    clusters = list(range(n)) 
    dist_matrix = [[0.0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            dist = math.sqrt((points[i][0] - points[j][0]) ** 2 + 
                             (points[i][1] - points[j][1]) ** 2)
            dist_matrix[i][j] = dist_matrix[j][i] = dist

    cluster_count = n
    print("Agglomerative Clustering using Single Linkage:")

    while cluster_count > 1:
        min_distance = float("inf")
        point1, point2 = -1, -1

        for i in range(n):
            for j in range(i + 1, n):
                if clusters[i] != clusters[j] and dist_matrix[i][j] < min_distance:
                    min_distance = dist_matrix[i][j]
                    point1, point2 = i, j

        old_cluster_id = clusters[point2]
        new_cluster_id = clusters[point1]
        print(f"\nMerging Cluster {old_cluster_id} and Cluster {new_cluster_id} (Distance: {min_distance:.2f})")

        for i in range(n):
            if clusters[i] == old_cluster_id:
                clusters[i] = new_cluster_id

        cluster_count -= 1

        print("\nClusters:")
        for i in range(n):
            print(f"Point {i + 1} -> Cluster {clusters[i]}")

    return clusters


if __name__ == "__main__":
    points = [
        (0.40, 0.53), (0.22, 0.38), (0.35, 0.32),
        (0.26, 0.19), (0.08, 0.41), (0.45, 0.30)
    ]

    single_linkage_clustering(points)
