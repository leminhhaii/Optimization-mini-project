from ortools.sat.python import cp_model #import the library
import time
def import_data():#get the data: N is the number of papers, M is the number of reviewers, b is the number of reviewers assigned to paper
	N, M, b = map(int, input().split())

	L = []

	for i in range(N):
		L.append(list(map(int, input().split()))[1:])

	return N, M, L, b


class Solver:#declare solver class
	def __init__(self, N, M, L, b):#declare the variables
		# num papers
		self.N = N
		# num reviewers
		self.M = M
		self.L = L
		self.b = b

		# N * M
		self.X = [[0 for _ in range(M)] for _ in range(N)]
		#each element in self.X is X[i][j] is a binary  variable that determines whether paper i is assigned to reviewer j. 
		#These variables are defined using model.NewIntVar(0, 1, f'x{i}{j}') inside the solve() method of the Solver class.
	
	def solve(self):
		model = cp_model.CpModel()#the data model

		for i in range(self.N):
			for j in range(self.M):
				self.X[i][j] = model.NewIntVar(0, 1, f'x{i}{j}')#Tạo ra biến quyết định X[i][j] có giá trị 0 hoặc 1, thể hiện việc gán người đánh giá j cho bài báo i.
				if j+1 not in self.L[i]:
					model.Add(self.X[i][j] == 0)
					# Thiết lập ràng buộc để đặt giá trị của biến quyết định là 0 nếu người đánh giá j không được phân cho bài báo i.
					# If a reviewer number is not included in the list of reviewers interested in reviewing a specific paper
					# the corresponding decision variable X[i][j] is set to zero

			model.Add(sum(self.X[i]) == self.b)#each paper is reviewed by a specific number of reviewers specified by self.b
			# đảm bảo mỗi tờ báo được giao cho đúng số người

		obj = model.NewIntVar(0, self.N, 'obj')#Tạo biến obj để tối thiểu hóa số lượng người đánh giá được sử dụng.

		model.AddMaxEquality(obj, [sum([self.X[i][j] for i in range(self.N)]) for j in range(self.M)])#hàm chọn ra số công việc lớn nhất của tất cả mọi người 
		# để obj đạt giá trị lớn nhất có thể thông qua việc tính tổng số lượng người đánh giá được gán cho mỗi bài báo 
		# và chọn giá trị nhỏ nhất của các tổng này để tối thiểu hóa số lượng người được sử dụng.
		model.Minimize(obj)#mục tiêu là tối ưu hóa số lượng công việc của mỗi người
		

		solver = cp_model.CpSolver()

		solver.Solve(model)

		self.result = []

		for i in range(self.N):
			self.result.append([self.b])
			for j in range(self.M):
				if solver.Value(self.X[i][j]) == 1:
					self.result[i].append(j+1)
		
	def print_sol(self):
		print(self.N)

		for result in self.result:
			print(*result)
	
def main():
	sol = Solver(*import_data())
	a = time.time()
	sol.solve()
	b = time.time()
	c = b-a
	print(c)
	# sol.print_sol()
if __name__ == "__main__":
	main()