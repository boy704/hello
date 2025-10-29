import math

D = 0.85       
PR_ITER = 100     
HITS_ITER = 20     

def main():
    N = int(input("Enter number of pages/nodes: "))

    print(f"\nEnter adjacency matrix ({N} x {N}):")
    print("(1 means link from row -> column, 0 means no link)")

    A = []
    for i in range(N):
        row = list(map(int, input().split()))
        A.append(row)

    print("\n=== PAGE RANK RESULTS ===")

    outdeg = [sum(A[i]) for i in range(N)]

    M = [[0.0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if A[j][i] == 1 and outdeg[j] != 0:
                M[i][j] = 1.0 / outdeg[j]
            else:
                M[i][j] = 0.0

    rank = [1.0 / N for _ in range(N)]

    for _ in range(PR_ITER):
        new_rank = []
        for i in range(N):
            s = sum(M[i][j] * rank[j] for j in range(N))
            new_rank.append((1 - D) / N + D * s)
        rank = new_rank

    for i in range(N):
        print(f"Page {i + 1}: {rank[i]:.6f}")

    print("\n=== HITS RESULTS ===")

    authority = [1.0 for _ in range(N)]
    hub = [1.0 for _ in range(N)]

    for _ in range(HITS_ITER):
        new_authority = []
        for i in range(N):
            val = sum(hub[j] for j in range(N) if A[j][i] == 1)
            new_authority.append(val)
        norm = math.sqrt(sum(x * x for x in new_authority))
        authority = [x / norm if norm != 0 else 0 for x in new_authority]

        new_hub = []
        for i in range(N):
            val = sum(authority[j] for j in range(N) if A[i][j] == 1)
            new_hub.append(val)
        norm = math.sqrt(sum(x * x for x in new_hub))
        hub = [x / norm if norm != 0 else 0 for x in new_hub]

    for i in range(N):
        print(f"Page {i + 1} -> Authority: {authority[i]:.6f}, Hub: {hub[i]:.6f}")


if __name__ == "__main__":
    main()
