from ortools.linear_solver import pywraplp


def main():
    solver = pywraplp.Solver.CreateSolver('SCIP')
   
    n, m, b = map(int, input().split())
   
    lst = []
   
    for _ in range(n):
        lst.append(list(map(int, input().split())))


    L = []
    for i in range(n):
       
        if lst[i][0] == m:
            L.append(lst[i][1:])
       
        else:
       
            l = lst[i][1:]
            a = []
           
            for i in range(1, m + 1):
               
                if i not in l:
                    a.append(0)
               
                else:
                    a.append(i)
            L.append(a)
   
    for i in range(n):
        for j in range(m):
           
            if L[i][j] == j + 1:
                L[i][j] = 1
           
            else:
                L[i][j] = 0
   
    X = {}
   
    for i in range(n):
        for j in range(m):
           
            X[i, j] = solver.IntVar(0, 1, f'X[{i}, {j}]')
   
    Z = solver.IntVar(0, n, f'Z')
  
   
    for i in range(n):
       
        solver.Add(sum([L[i][j] * X[i, j] for j in range(m)]) == b)
   
    for j in range(m):
       
        solver.Add(Z >= sum([L[i][j] * X[i, j] for i in range(n)]))
   
    solver.Minimize(Z)
    status = solver.Solve()
   
    if status == pywraplp.Solver.OPTIMAL:
        print(n)
       
        for i in range(n):
            print(b, end = ' ')
           
            for j in range(m):
                if int(L[i][j] * X[i, j].solution_value()) == 1:
                    print(j + 1, end = ' ')
           
            print()
           
if __name__ == "__main__":
   
    main()


