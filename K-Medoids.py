def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def k_medoids(data, k, initial_medoids):
    n = len(data)
    medoid_indices = initial_medoids[:]
    assignments = [0] * n
    changed = True

    while changed:
        changed = False

        for i in range(n):
            distances = [manhattan_distance(data[i], data[m]) for m in medoid_indices]
            assignments[i] = distances.index(min(distances))


        for i in range(k):
            cluster_points = [idx for idx, a in enumerate(assignments) if a == i]
            best_cost = float("inf")
            best_medoid = medoid_indices[i]

            for j in cluster_points:
                cost = sum(manhattan_distance(data[j], data[l]) for l in cluster_points)
                if cost < best_cost:
                    best_cost = cost
                    best_medoid = j

            if medoid_indices[i] != best_medoid:
                medoid_indices[i] = best_medoid
                changed = True

    return medoid_indices, assignments


if __name__ == "__main__":
    k = 2
    data = [
        (2, 6), (3, 4), (3, 8), (4, 7), (6, 2),
        (6, 4), (7, 3), (7, 4), (8, 5), (7, 6)
    ]
    initial_medoids = [0, 3]

    medoid_indices, assignments = k_medoids(data, k, initial_medoids)

    print("Final Medoids:")
    for i, medoid_idx in enumerate(medoid_indices, start=1):
        print(f"Cluster {i} Medoid -> Point (x={data[medoid_idx][0]}, y={data[medoid_idx][1]})")

    print("\nCluster Assignments:")
    for i, (x, y) in enumerate(data, start=1):
        print(f"Point {i} -> (x={x}, y={y}) in Cluster {assignments[i-1] + 1}")
