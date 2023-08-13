def flatten_and_sort(array):
    integers = []
    sorted_result = sorted(array)
    return sorted_result

input_array = [[5, 4, 3], [7, 6, 5]]
sorted_array = flatten_and_sort(input_array)
print(sorted_array)

"""How does this solution ensure data immutability?
because it doesnt modify the original input"""

"""Is this solution a pure function? Why or why not?
yes, because it producesthe same output for the same input"""

"""Is this solution a higher order function? Why or why not?
no because it doesnt require a function as an argument"""

"""Would it have been easier to solve this problem using a different programming style?
this is the most effective way to write this code as it is a defenitive problem"""

"""Why in particular is functional programming a helpful paradigm when solving this problem?
it is more concise and straightforward to use pure functions"""