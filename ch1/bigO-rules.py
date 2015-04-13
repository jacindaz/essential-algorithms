# Rule 1:
#   If an algo performs a certain sequence of steps
#   f(n) times for a mathematical function f, it takes
#   O(f(n)) steps

array = [100, 21, 53, 78, 42, 30, 899]
def find_largest_integer(array):
    largest_num = array[0]
    for integer in array:
        if integer > largest_num:
            largest_num = integer
    print "%s %d" %("Largest number is:", largest_num)
    return largest_num

find_largest_integer(array)

# Rule 2:
#   If an algo performs an operation that takes O(f(n)) steps
#   and then performs a 2nd operation that takes O(g(n)) steps
#   for functions f and g, the algo's total performance is
#   O( f(n) + g(n) )

# Bryan says this would be O(2n) ???
array = [100, 21, 53, 698, 78, 42, 30, 899]
def find_largest_even_integer(array):
    largest_num = array[0]
    for integer in array:
        if integer > largest_num and integer % 2 == 0:
            largest_num = integer
    print "%s %d" %("Largest even number is:", largest_num)
    return largest_num

find_largest_even_integer(array)

# Rule 4:
#	if an algo performs an operation that takes O(f(n)) steps
# 	and for every step in that operation it performs another
#	O(g(n)) steps, the algo's total performance is O( f(n) + g(n) )

array1 = [1, 2, 3, 4]
array2 = [8, 9, 10, 1]
def is_duplicate(array1, array2):
	for index1, value1 in enumerate(array1):
		for index2, value2 in enumerate(array2):
			if value1 != value2:
				if array[index1] == array[index2]:
					break
	print "There is a duplicate."
	return False

is_duplicate(array1, array2)


