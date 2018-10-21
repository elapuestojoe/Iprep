class Solution:
	# @param a : list of list of integers
	# @return a list of list of integers
	def diagonal(self, a):
		solution = []
		for x in xrange(len(a[0])):
			y = 0
			tempX = x
			tempSolution = []
			while(tempX > 0 and y < len(a[0])):
				tempSolution.append(a[tempX][y])
				y += 1
				tempX -= 1
			solution.append(tempSolution)

		for y in xrange(1, len(a)):
			tempY = y
			x = len(a[0])-1
			tempSolution = []
			while(tempY < len(a) and x > 0):
				tempSolution.append(a[tempX][y])
				x -= 1
				tempY += 1
		return solution