def assign_reviewers(N, M, b, papers):
    # Initialize reviewer loads
    reviewer_loads = [0] * M

    # Initialize the assignment matrix
    assignment_matrix = []

    for i, paper in enumerate(papers):
        paper_id, reviewers = paper[0], paper[1]

        # Sort reviewers based on their current loads and original order
        reviewers.sort(key=lambda x: (reviewer_loads[x - 1], x))

        # Assign b reviewers to the paper
        assignment_matrix.append([reviewers[i] for i in range(b)])

        # Update reviewer loads
        for reviewer in reviewers[:b]:
            reviewer_loads[reviewer - 1] += 1

    # Print the output
    print(N)
    for i, assignment in enumerate(assignment_matrix):
        print(b, *assignment)

# Example usage
N, M, b = map(int, input().split())
papers = []

for i in range(N):
    paper_info = list(map(int, input().split()))
    papers.append((i + 1, paper_info[1:]))


assign_reviewers(N, M, b, papers)
