import numpy as np

def solve_R(p):
	return np.log(np.log(1-p)/np.log(0.95))+25.66

print(solve_R(0.1150))
print(solve_R(0.1108))
print(solve_R(0.0940))
print(solve_R(0.0105))
