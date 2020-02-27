"""
+++++++++++++++++++++++ Python Code +++++++++++++++++++++++

Here is a simple task. Take an array/tuple of unique positive integers, and two additional positive integers. Here's an example below:

arr = (3,5,7,1,6,8,2,4)
n = 3 # span length
q = 13 # weight threshold

Try to re-arrange arr so that the sum of any n consecutive values does not exceed q.

solver(arr,n,q) ## one possible solution: (4,7,1,5,6,2,3,8)

Did you succeed? Great! Now teach a computer to do it.

Technical Details
  All test inputs will be valid
  All test cases will have 0 or more possible solutions
  If a test case has no solution, return an empty array/tuple
  Test constraints:
  2 <= n <= 6
  4 <= arr length < 12
  n < arr length
  Every value in arr will be less than q
  11 fixed tests, 25 random tests
  In JavaScript, module and require are disabled
  For JavaScript, use Node 10+
  For Python, use Python 3.6+

"""

def solver(arr,n,q):
	realArr = [i for i in arr]
	realArr.sort()
	moduls = []
	targets = []
	newArr = []
	halfL = len(arr) // 2
	newArr.append(realArr[len(realArr)-1])
	for i in range(1,halfL+1):
		res = q % realArr[len(realArr)-i]
		moduls.append(res)
	for elem in moduls:
		if elem in realArr:
			targets.append(elem)
			realArr.pop(realArr.index(elem))
	
	if len(targets) > 0:
		for elem in targets:
			newArr.insert(0, elem)
	print(newArr)

solver((3,5,7,1,6,8,2,4),3,13)

"""
@test.describe('Example Tests')
def example_tests():
	examples = (
		((3,5,7,1,6,8,2,4),3,13),
		((7,12,6,10,3,8,5,4,13,2,9),4,28),
		((9,16,11,6,15,14,19,3,12,18,7),3,35),
		((33,34,29,25,36,30,27,32,21,35,39),5,155),
		((22,14,30,25,29,19,21,17,15,32,20),4,92),
	)
	example_solutions = (
		(4,7,1,5,6,2,3,8),
		(4,9,10,3,5,8,12,2,6,7,13),
		(11,18,3,14,15,6,12,16,7,9,19),
		(32,33,34,21,30,36,25,27,35,29,39),
		(32,14,15,19,20,30,22,17,21,25,29),
	)
	for i,v in enumerate(examples):
		test.expect(*check_solution(solver(*v),example_solutions[i],*v))
		"""