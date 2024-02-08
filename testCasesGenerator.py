import random

# Constant
NUM_OF_TEST_CASE = int(1e5)
LOWER_BOUND = int(-2e4)
UPPER_BOUND = int(2e4)

def main():
	
	print(NUM_OF_TEST_CASE)
	print(LOWER_BOUND)
	print(UPPER_BOUND)

	# Worst case scenario - N = MAX VALUE
	file = open('bigTestCase.txt', 'w+')
	file.write(f'{1}\n')

	#genereting the x
	line = ""
	for i in range(NUM_OF_TEST_CASE):
		line += str(random.randint(LOWER_BOUND,UPPER_BOUND)) + (',' if i < NUM_OF_TEST_CASE - 1 else '\n')
	file.write(line)

	#genereting the y
	line = ""
	for i in range(NUM_OF_TEST_CASE):
		line += str(random.randint(LOWER_BOUND,UPPER_BOUND)) + (',' if i < NUM_OF_TEST_CASE - 1 else '\n')
	file.write(line)

	#genereting the colors
	line = ""
	for i in range(NUM_OF_TEST_CASE):
		line += ('R' if random.random() >= 0.5 else 'G') + ('' if i < NUM_OF_TEST_CASE - 1 else '\n')
	file.write(line)

	file.close()

if __name__ == '__main__':
	main()