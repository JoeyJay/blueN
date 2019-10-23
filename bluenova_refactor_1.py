#   Refactoring Quiz
colours = ['blue', 'green', 'yellow', 'black', 'orange']
fruits = ['berry', 'apple', 'banana', 'currant']

'''
#   ugly
for i in range(len(colours)-1, -1, -1):
    print(colours[i])

#   refactor below
'''


def reverse(collection):
    start = len(collection) - 1
    b = 0
    while b < start:
        collection[b], collection[start] = collection[start], collection[b]
        b += 1
        start -= 1


def print_collection(collection):
    print(collection)


#reverse(colours)
#print_collection(colours)
#   END OF TASK 1
'''
#   ugly
for i in range(len(colours)):
    print(i, colours[i])
'''

'''
for index, colour in enumerate(colours):
    print(index, colour)
    
#   END OF TASK 2
'''
'''
#   ugly
min_length = min(len(colours), len(fruits))
print(min_length)
for i in range(min_length):
    print(colours[i], fruits[i])

'''

'''
def get_min_length(collection1, collection2):
    return min(len(collection1), len(collection2))


def _print_collection(collection1, collection2, _min_length):
    index = 0
    while index < _min_length:
        print(collection1[index], collection2[index])
        index += 1


_min_length = get_min_length(colours, fruits)
_print_collection(colours, fruits, _min_length)

#   END OF TASK 3
'''


def evaluate_vars(a, b, c, d, f, g):
    val = 'pass'
    temp = None
    var_list = [a, b, c, d, f, g]
    length = len(var_list) - 1
    for i in range(len(var_list)):
        if var_list[i] > g:  # program should fail if any value is > g
            val = 'fail'
        temp = var_list[i]
        if i == length:
            break
        if temp > var_list[i + 1]:
            val = 'fail'
    print(val)


evaluate_vars(1, 1, 2, 3, 7, 8)

# END OF TASK 4
