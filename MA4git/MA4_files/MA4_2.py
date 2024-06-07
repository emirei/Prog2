#!/usr/bin/env python3
#Redovisat för Viktor Lindström 21/05/2024

from person import Person
from numba import njit
from time import perf_counter
import matplotlib.pyplot as plt

def fib_py(n):
	if n <= 1:
		return n
	else:
		return(fib_py(n-1) + fib_py(n-2))
@njit
def fib_numba(n):
	if n <= 1:
		return n
	else:
		return(fib_numba(n-1) + fib_numba(n-2))

def main():
	f = Person(50)
	print(f.getAge())
	print(f.getDecades())


	timeLst = []
	for i in range(20, 40):
		start = perf_counter()
		fib_py(i)
		end = perf_counter()
		timeLst.append(end-start)
	plt.plot([ii for ii in range(20,40)], timeLst)

	timeLst = []
	for i in range(20, 40):
		start = perf_counter()
		fib_numba(i)
		end = perf_counter()
		timeLst.append(end-start)
	plt.plot([ii for ii in range(20,40)], timeLst)

	timeLst = []
	for i in range(20, 40):
		start = perf_counter()
		f = Person(i)
		f.fib()
		end = perf_counter()
		timeLst.append(end-start)
	plt.plot([ii for ii in range(20,40)], timeLst)
	plt.legend(["fib_py", "fib_numba", "f.fib"])
	plt.savefig(f'Time for each type of calculation plotted.png')
	plt.show()

if __name__ == '__main__':
	main()


#Value for fib_numba 47 = 2971215073
#Value for f.fib 47 = -547084288
