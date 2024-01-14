def assign_reviewers(N, M, b, papers):
    reviewer_loads = [0] * M
    assignment = []

    for reviewers in papers:
        # Sort reviewers based on their current loads
        reviewers.sort(key=lambda x: reviewer_loads[x - 1])

        # Assign b reviewers to the paper
        assignment.append(reviewers[:b])

        # Update reviewer loads
        for reviewer in reviewers[:b]:
            reviewer_loads[reviewer - 1] += 1

    print(N)
    for paper in assignment:
        print(b, *paper)

N, M, b = map(int, input().split())
papers = [list(map(int, input().split()))[1:] for _ in range(N)]

assign_reviewers(N, M, b, papers)
