def to_number(string):
    new_int = int(string)
    return new_int

def add_two(n1,n2):
    summation = n1 + n2
    return summation

def cube(n): 
    cubed = n**3
    return cubed

print cube(add_two(to_number('6'),to_number('5')))
