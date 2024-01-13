from ortools.sat.python import cp_model #import the library
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
	
	def solve(self):
		model = cp_model.CpModel()#the data model

		for i in range(self.N):
			for j in range(self.M):
				self.X[i][j] = model.NewIntVar(0, 1, f'x{i}{j}') 
				if j+1 not in self.L[i]:
					model.Add(self.X[i][j] == 0)
					
			model.Add(sum(self.X[i]) == self.b)

		obj = model.NewIntVar(0, self.N, 'obj')
		model.AddMaxEquality(obj, [sum([self.X[i][j] for i in range(self.N)]) for j in range(self.M)])
		model.Minimize(obj)
		
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
	sol.solve()
	sol.print_sol()
if __name__ == "__main__":
	main()
