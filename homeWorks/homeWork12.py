def print_params(a=1, b='Str', c=True):
    print(a, b, c)


print_params()

print_params(2, 'Goal')

print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [12, False, "Text"]
values_dict = {'a': 45, 'b': 'Text 2', 'c': False}


print_params(*values_list)
print_params(**values_dict)

values_list2 = ['Text 3', 77]
print_params(*values_list2, 42)