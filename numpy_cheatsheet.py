import numpy as np
import random
import time
import pickle

#See this link for some background: https://stackoverflow.com/questions/993984/why-numpy-instead-of-python-lists
def numpy_multiply(dim):
	x = np.arange(dim)
	y = np.random.rand(dim)
	z = np.multiply(x, y)

	#print z.shape

	with open("numpy_array.bin", "wb") as fp:
		np.save(fp, z)

	return 0

def python_list_multiply(dim):
	x = range(dim)
	y = [random.random() for k in range(dim)]
	z = [x[i]*y[i] for i in range(dim)]

	with open("python_list.pkl", "wb") as fp:
		pickle.dump(z, fp)

	return 0


def measure_multiply_perf():
    dim = 100000
    start = time.time()
    numpy_multiply(dim)
    end = time.time()
    print "Numpy performance for dimension", dim, ":" 
    print(end - start)
    print "-----------------------"
    start = time.time()
    python_list_multiply(dim)
    end = time.time()
    print "Python list performance for dimension", dim, ":" 
    print(end - start)
    print "-----------------------"    


def numpy_array_creation_demo():
	#create an array of zeros with 8 entries
	zeros_array = np.zeros(8)
	print "np.zeros(8) : numpy zero array with one row & eight columns:\n", zeros_array, "\n-----------------------"
	zeros_array = np.zeros((4,2))
	print "np.zeros((4,2)): numpy zero array with four rows & two columns:\n", zeros_array, "\n-----------------------"
	#create an array of ones
	ones_array = np.ones((2,4))
	print "np.ones((2,4)): numpy zero array with two rows & four columns:\n", ones_array, "\n-----------------------"

def numpy_range_demo():
	x = np.arange(5)
	print "np.arange(5): a linear array in [0,5) range:\n", x, "\n-----------------------"
	x = np.arange(1, 10, 2)
	print "np.arange(1, 10, 2): a linear array in [1,10) range with step size two:\n", x, "\n-----------------------"
	x = np.linspace(0.0, 1.0, num=5)
	print "np.linspace(0.0, 1.0, num=5): a linear array in [0,1.0) range with five samples:\n", x, "\n-----------------------"


def numpy_array_funcs_demo():
	x = np.array([[1, 6], [3, 4]])
	print "x:", x
	print "np.mean(x): compute mean of flattened array x:\n", np.mean(x), "\n-----------------------"
	print "np.mean(x, axis=0): compute mean of x along columns (axis=0):\n", np.mean(x, axis=0), "\n-----------------------"
	print "np.mean(x, axis=1): compute mean of x along rows (axis=1):\n", np.mean(x, axis=1), "\n-----------------------"
	print "np.std(x): compute standard deviation of flattened x:\n", np.std(x), "\n-----------------------"


def numpy_matrix_creation_demo():
	x = np.array([[1, 2], [3, 4]])
	print "x:", x
	m = np.asmatrix(x)
	print "np.asmatrix(x) : create a matrix of a numpy array:\n", m, "\n-----------------------"
	m[0,0] = 0
	print "matrix m:", m
	x = np.arange(9).reshape((3,3))
	print "x = np.arange(9).reshape((3,3)):", x
	print "np.diag(x) : returns diagonal of 2-D array x:\n", np.diag(x), "\n-----------------------"


def numpy_matrix_operation_demo():
	print "np.dot([1, 2], [3, 4]):\n", np.dot([1, 2], [3, 4]), "\n-----------------------"
	x = [[1, 0], [0, 1]]
	y = [[4, 1], [2, 2]]
	print "x:", x
	print "y:", y
	print "matrix multiplication --> np.matmul(x, y):\n", np.matmul(x, y), "\n-----------------------"


def numpy_linear_algebra_demo():
	x = [[1, 2], [3, 7]]
	print "x:", x
	print "determinant of x:, np.linalg.det(x):\n", np.linalg.det(x), "\n-----------------------"
	x = [[4, 7], [2, 6]]
	print "x:", x
	print "inverse of x:, np.linalg.inv(x):\n", np.linalg.inv(x), "\n-----------------------"
	x = [[2, 3], [1, 4]]
	print "x:", x
	print "eigenvalues & eigenvectors of x:, np.linalg.eig(x):\n", np.linalg.eig(x), "\n-----------------------"


def run():
	# measure_multiply_perf()
 #    numpy_array_creation_demo()
 #    numpy_range_demo()
 #    numpy_array_funcs_demo()
 #    numpy_matrix_creation_demo()
 #    numpy_matrix_operation_demo()
    numpy_linear_algebra_demo()

    
if __name__ == "__main__":
	run()