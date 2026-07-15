def add(a, b):
    return a + b

#print(add(1,7, 3))

def add1(*args):
    print(type(args))
    result = 0
    for arg in args:
        result += arg
    return result
        
print(add1(1, 34, 34, 2, 3))


def display_name(*args):
    for arg in args:
        print(arg, end =" ")
display_name ("Dr.", "Muhammad Idrees", "Harold", "Squareparents", "III")


def print_address(**kwargs):
    
   #print(type(kwargs))
   for value in kwargs.values():
       print(value)
   for key in kwargs.keys():
       print(key)
   for key, value in kwargs.items():
       print(f"{key}:{value}")
print_address(street="123 Mianwali", ciy="Minwali",  state="Punjab", zip="42220", apt="100")




def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end =" ")
    print()
    
    for value in kwargs.values():
        print(value, end=" ")
    print()
    if "apt" in kwargs:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    else:
        print(f"{kwargs.get('street')}")
        
    print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('city')} {kwargs.get('state')} {kwargs.get('zip')} {kwargs.get('apt')}")
    
shipping_label("Dr.", "Muhammad Idrees", "Harold", "Squareparents", "III",
               street="123 Mianwali", city="Minwali",  state="Punjab", zip="42220", apt="123")