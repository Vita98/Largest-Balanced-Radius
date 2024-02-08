'''
	
	Solution:
	The simplest and fastest solution found by me consist into:

	- Calculate, for each point, the distance from the origin ([0,0]) while grouping it 
	by distance into a hash data structure for fast access. The access key is the distance itself. Complexity: n
	- Reorder the distances from the furthest to the nearest to the origin. TimSort algorith complexity: O(nlog(n))
	- Begin from the furthest distance and, with the marker object, check if the inner point are balanced. 
	If true, then the solution is the sum of the red and green point. Complexity worst case scenario: n

	Total complexity: n + O(nlog(n)) + n = 2n + O(nlog(n)) = O(nlog(n))
	The biggest computations comes from the sorting algorithm

'''
import math


# Class to manage the point into a single structure
class Point:
	def __init__(self, x, y, color):
		self.x = x
		self.y = y
		self.color = color
		self.distance = (x**2 + y**2)**0.5 # Pythagorean theorem

	def __str__(self):
		return f'{self.x} - {self.y} - {self.color} - {self.distance}'

'''
Class to manage the various point with same distances:
Examples: point such as [5,1], [1,5], [-1,5], [1,-5], [-1,-5] have all the same distances.

The goal is to group all the point with the same distance and keep track of
how much of them are green and red
'''
class DistanceMarker:
	def __init__(self, color):
		if color == 'R':
			self.reds = 1
			self.greens = 0
		elif color == 'G':
			self.greens = 1
			self.reds = 0

	def add(self, color):
		if color == 'R':
			self.reds += 1
		elif color == 'G':
			self.greens += 1

	def __str__(self):
		return f'Reds: {self.reds} - Greens: {self.greens}'



def main():
	'''
		The test case file is thus formed:
		1th row: number of tast cases - N
		N * 3 rows with: x values, y values and colors. The first two rows are csv, the colors row is a plain string.
	'''
	# Reading the test cases
	file = open("bigTestCase.txt",'r')
	numTestCase = int(file.readline().lstrip().rstrip())

	for i in range(numTestCase):
		xs = list(map(int, file.readline().lstrip().rstrip().split(',') ))
		ys = list(map(int, file.readline().lstrip().rstrip().split(',') ))
		colors = file.readline().lstrip().rstrip()

		# Run the solution for each test case
		sol = solution(xs,ys,colors)
		print(f"Solution test case {i+1}: {sol}", end= "\n")


def solution(xs, ys, colors):
	points = []			# Simle list with all the Point objects
	distancesDict = {} 	# Dictionary for fast access with hash
	totalReds = 0		
	totalGreens = 0

	# Populating the points list and the distances dictionary
	for i in range(0,len(xs)):
		newPoint = Point(xs[i], ys[i], colors[i])
		points.append(newPoint)
		if newPoint.distance not in distancesDict:
			distancesDict[newPoint.distance] = DistanceMarker(colors[i])
		else:
			distancesDict[newPoint.distance].add(colors[i])

		#Calculating totals colors
		if colors[i] == 'R':
			totalReds += 1
		elif colors[i] == 'G':
			totalGreens += 1

	'''
		Sorting distances - Python uses the TimSort algorithm, an hybrid sorting algorithm
		derived from merge sort and insertion sort
	'''
	sortedDistances = sorted(distancesDict.keys(), reverse=True)

	#Iterating among all the distances and calculating di inner points
	for distance in sortedDistances:
		marker = distancesDict[distance]

		# Check if the red and green points are balanced
		if totalReds == totalGreens:
			return totalReds + totalGreens

		totalReds -= marker.reds
		totalGreens -= marker.greens

	return 0



if __name__ == '__main__':
	main()





