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
    return largest_num

find_largest_integer(array)
