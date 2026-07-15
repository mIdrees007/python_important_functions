# Decorator is function that extends teh behaviour of another function w/o modifying the base function
# pass the base function as an argument to the decorator

# @ addd_Sprinkles
# get_ice_cream("vanilla")
def add_Sprinkles(func):
    def wrapper(*args, **kwargs):
        print("you add sprinkles ")
        func(args, **kwargs)
    return wrapper

def add_fudge(func):
    def wrapper(args, **kwargs):
        print(f"you added fudge")
        func(args, **kwargs)
    return wrapper


@add_Sprinkles
@add_fudge
def get_ice_cream(flavor):
    print("Here is your ice cream {flavor} ")
get_ice_cream("vanilla")