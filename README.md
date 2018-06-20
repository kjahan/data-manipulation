# data-manipulation
This is a collection of cheat sheets for data manipulation.

numpy_cheatsheet.py: demos a number of examples on how to create/use numpy arrays and matrixes. It's important to note that numpy arrays are much more efficient than Python lists. 

For example, creating two numpy arrays with dimension of 100000 and multiplying them takes ~0.02349 seconds on a MBP (CPU: 2.9 GHz Intel Core i7, Memory: 8 GB 1600 MHz DDR3). On the other hand, performing the same operation using Python list data structure with the same array dimension takes ~0.50372 seconds which is 21 times slower!

pandas_cheatsheet.py: demos a number of examples on how to use and manipulate pandas data frames.
