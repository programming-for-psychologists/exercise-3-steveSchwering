import random

### Exercise 3
### Part 1
print("PART 1: ")
def repetition(letters, numberBeforeSwitch, numRepetitions):
	trials = []
	for i in range(numRepetitions):
		for letter in letters:
			for j in range(numberBeforeSwitch):
				trials.append(letter)
	printArr(trials)
	return trials

def printArr(arr):
	for item in arr:
		print(str(item) + "\t"),
		print("")

trialsAB = repetition(['A', 'B'], 2, 2)

### Part 2
print("\n\nPART 2: ")
def printArr2(arr):
	for trial in arr:
		for item in trial:
			print(str(item) + "\t"),
		print("")

conMask = ['mask', 'mask', 'nonmask']
conSide = ['right', 'left']
blocks = 5
def repetitionMask(masks, sides, block):
	trials = []
	for i in range(block):
		for mask in masks:
			for side in sides:
				trials.append([i, mask, side])
	printArr2(trials)
	return trials

trialsMask = repetitionMask(conMask, conSide, blocks)

### Part 3
print("\n\nPART 3: ")
conMask = ['mask', 'mask', 'nonmask']
conSide = ['right', 'left']
blocks = 5
def repetitionMaskRan(masks, sides, block):
	trials = []
	for i in range(block):
		for mask in masks:
			for side in sides:
				trials.append([i, mask, side])
	random.shuffle(trials)
	printArr2(trials)
	return trials

trialsRan = repetitionMaskRan(conMask, conSide, blocks)

### Part 4
print("\n\nPART 4: ")
def printArr3(arr):
	for block in arr:
		for trial in block:
			for item in trial:
				print(str(item) + "\t"),
			print("")

conMask = ['mask', 'mask', 'nonmask']
conSide = ['right', 'left']
blocks = 5
def repetitionMaskRanBlock(masks, sides, block):
	trials = []
	for i in range(block):
		block = []
		for mask in masks:
			for side in sides:
				block.append([i, mask, side])
		random.shuffle(block)
		trials.append(block)
	random.shuffle(trials)
	printArr3(trials)
	return trials

trialsRanBlock = repetitionMaskRanBlock(conMask, conSide, blocks)

### Part 5
print("\n\nPART 5: ")
conMask = ['mask', 'mask', 'nonmask']
conSide = ['right', 'left']
blocks = 5
scale = 2
def repetitionMaskRanBlockScale(masks, sides, block, scale):
	trials = []
	for i in range(block):
		block = []
		for j in range(scale):	
			for mask in masks:
				for side in sides:
					block.append([i, mask, side])
		random.shuffle(block)
		trials.append(block)
	random.shuffle(trials)
	printArr3(trials)
	return trials

trialsRanBlockScale = repetitionMaskRanBlockScale(conMask, conSide, blocks, scale)