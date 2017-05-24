def double_it(formal_parameter):
    print(formal_parameter, id(formal_parameter))
    doubled = formal_parameter * 2
    print(doubled, id(doubled))
    return doubled

argument_value = 3 
print(argument_value, id(argument_value))
returned_value = double_it(argument_value)
print(returned_value, id(returned_value))
    