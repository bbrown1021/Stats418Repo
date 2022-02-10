""" Given a 2d numpy array, this module will return: 

Assignment:
**6.1**	A 2d array with rows of magnitude>1
**6.2**	A 1d array with all elements of the matrix in a column-major way
**6.3**	A 2d array with all the negative values replaced by zero
**6.4**	A 3x4 Block Matrix (2d array) with each block as the input 2d array
**6.5**	A 2d array with all elements of the input array rounded to the nearest hundred

Bonus Points:
**6.6**	A 2d array with each number converted to a python string
**6.7**	Median of all entries in the array
**6.8**	A 3d array with the numbers repeated across the 3rd axis 11 times
**6.9**	A 1d array containing maximum values of each row, in sorted order
**6.10** A file-like object on which np.save can be called to get back the input array 
**6.11** A 2d array with non-diagonal entries set to zero (given that it is square)
**6.12** A 2d array with only rows whose row numbers are perfect squares
"""

# -------------------------------- #
# Import Modules
# -------------------------------- #

import logging
import math
import numpy as np
from numpy import newaxis

from data import NEW_INPUT

# -------------------------------- #
# Set up Logging
# -------------------------------- #
logging.basicConfig(level=logging.INFO)  # basic configuration
LOGGER = logging.getLogger(__name__)  # define one logger for current file

LOGGER.info("-------------------------------------------------")
LOGGER.info("Given the following 2d numpy array input:")
LOGGER.info("-------------------------------------------------")

INPUT = NEW_INPUT
print(INPUT)

# keep track of number of rows and columns
num_rows, num_cols = INPUT.shape

def main():

	LOGGER.info("-------------------------------------------------")
	LOGGER.info(" Part 6.1: A 2d array with rows of magnitude>1")
	LOGGER.info("-------------------------------------------------")

	# computes the magnitude of each row
	mags = (np.linalg.norm(INPUT, axis=1))

	index = []
	for x in range(num_rows):
		if mags[x] > 1: index.append(x)
	print(f'Therefore, a 2d array with only rows of magnitude greater than 1 is: \n {INPUT[index]}')

	mags = (np.linalg.norm(INPUT, axis=1))

	LOGGER.info("-------------------------------------------------")
	LOGGER.info(" Part 6.2: A 1d array with all elements of the matrix in a column-major way")
	LOGGER.info("-------------------------------------------------")

	flat_array = INPUT.flatten(order="F")
	print(flat_array)

	LOGGER.info("-------------------------------------------------")
	LOGGER.info(" Part 6.3: A 2d array with all the negative values replaced by zero")
	LOGGER.info("-------------------------------------------------")

	INPUT_neg = INPUT.copy()
	INPUT_neg[INPUT_neg < 0 ] = 0
	print(INPUT_neg)

	LOGGER.info("-------------------------------------------------")
	LOGGER.info(" Part 6.4: A 3x4 Block Matrix (2d array) with each block as the input 2d array")
	LOGGER.info("-------------------------------------------------")

	print(f'Recall that the shape of our input 2d array is {num_rows} by {num_cols}. \n')

	A = INPUT.copy()
	B = np.block([
		[A,A,A,A],
		[A,A,A,A],
		[A,A,A,A]])

	Bnum_rows, Bnum_cols = B.shape
	print(f'Therefore, our 3x4 block matrix with each block as our original input will be {Bnum_rows} by {Bnum_cols}. \n {B}')

	LOGGER.info("-------------------------------------------------")
	LOGGER.info(" Part 6.5: A 2d array with all elements of the input array rounded to the nearest hundred")
	LOGGER.info("-------------------------------------------------")

	print(f'Recall that our input 2d array is \n {INPUT}')
	print(f'Therefore, rounded to the nearest hundred is: \n {np.around(INPUT,-2)}')

	LOGGER.info("-------------------------------------------------")
	LOGGER.info(" Part 6.6: A 2d array with each number converted to a python string")
	LOGGER.info("-------------------------------------------------")

	print(INPUT.astype("str"))

	LOGGER.info("-------------------------------------------------")
	LOGGER.info(" Part 6.7: Median of all entries in the array")
	LOGGER.info("-------------------------------------------------")

	print(f'The median is: {np.median(flat_array)}')

	LOGGER.info("-------------------------------------------------")
	LOGGER.info(" Part 6.8: A 3d array with the numbers repeated across the 3rd axis 11 times")
	LOGGER.info("-------------------------------------------------")

	THREE = np.repeat(INPUT[:, :, np.newaxis], 11, axis=2)
	print(THREE)
	print(f'The dimensions of this 3d array is: {THREE.shape}')

	LOGGER.info("-------------------------------------------------")
	LOGGER.info(" Part 6.9: A 1d array containing maximum values of each row, in sorted order")
	LOGGER.info("-------------------------------------------------")

	maxElement = np.amax(INPUT, axis=1)
	print(np.sort(maxElement))

	LOGGER.info("-------------------------------------------------")
	LOGGER.info(" Part 6.10: A file-like object on which np.save can be called to get back the input array ")
	LOGGER.info("-------------------------------------------------")

	LOGGER.info("---- save input array")
	np.save("input_array.npy" , INPUT)

	LOGGER.info("---- load in saved input array")
	data_new = np.load("input_array.npy")
	print(data_new)

	LOGGER.info("-------------------------------------------------")
	LOGGER.info(" Part 6.11: A 2d array with non-diagonal entries set to zero (given that it is square)")
	LOGGER.info("-------------------------------------------------")

	NEW_INPUT = INPUT.copy()

	# deals with special case where 2d is not a square
	mn = min(NEW_INPUT.shape)
	diag = np.einsum('ii->i', NEW_INPUT[:mn, :mn])
	save = diag.copy()

	# reset with zeros and place in saved diagonal
	NEW_INPUT[...] = 0
	diag[...] = save
	print(NEW_INPUT)

	LOGGER.info("-------------------------------------------------")
	LOGGER.info(" Part 6.12: A 2d array with only rows whose row numbers are perfect squares")
	LOGGER.info("-------------------------------------------------")

	number = list(range(num_rows))
	index = []
	for x in number:
		root = math.sqrt(number[x])
		if int(root + 0.5) ** 2 == number[x]:index.append(number[x])

	print(f'The following row numbers are perfect squares: \n {index}')

	print(f'Therefore, the resulting 2d array is: \n {INPUT[index]}')

if __name__ == "__main__":
	main()




	


