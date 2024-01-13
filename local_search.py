#PYTHON 
import time
import random

# Đọc dữ liệu input
N, M, b = map(int, input().split())
papers = []
for _ in range(N):
    reviewers = list(map(int, input().split()))[1:]
    papers.append(reviewers)

# Hàm tạo phân bố ngẫu nhiên ban đầu, đảm bảo chọn reviewer từ danh sách ưu tiên của paper
def initialize_assignment():
    assignment = []
    for paper_reviewers in papers:
        if len(paper_reviewers) <= b:
            assignment.append(paper_reviewers + [random.choice(paper_reviewers) for _ in range(b - len(paper_reviewers))])
        else:
            assignment.append(random.sample(paper_reviewers, b))
    return assignment

# Hàm tính toán tải công việc của mỗi reviewer
def calculate_load(assignments):
    loads = {}
    for paper_assignments in assignments:
        for reviewer in paper_assignments:
            if reviewer in loads:
                loads[reviewer] += 1
            else:
                loads[reviewer] = 1
    return max(loads.values())

# Local search
def local_search():
    current_assignment = initialize_assignment()
    best_assignment = current_assignment.copy()
    best_load = calculate_load(best_assignment)

    iterations = 1000
    for _ in range(iterations):
        paper_to_change = random.randint(0, N - 1)
        
        new_assignment = current_assignment.copy()
        if len(papers[paper_to_change]) <= b:
            new_assignment[paper_to_change] = papers[paper_to_change] + [random.choice(papers[paper_to_change]) for _ in range(b - len(papers[paper_to_change]))]
        else:
            new_assignment[paper_to_change] = random.sample(papers[paper_to_change], b)
        
        new_load = calculate_load(new_assignment)
        if new_load < best_load:
            best_load = new_load
            best_assignment = new_assignment.copy()
        
        current_assignment = new_assignment.copy()
    
    return best_assignment

# In ra output theo định dạng
def print_assignment(assignment):
    print(N)
    for paper_assignments in assignment:
        print(b, *paper_assignments)

# Thực thi thuật toán local search và in ra phân bố tối ưu
a = time.time()
best_assignment = local_search()
b = time.time()
c = b-a
print(round(c, 2))

