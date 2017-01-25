def my_decorator(x_function):
    """
    The following is an example of decorators in python,
    i.e. higher-order functions, as seen in python course
    """
    def wrapper():
        num = 10
        if num == 10:
            print("before x_function() is called")
        else:
            print("No!")
        
        x_function()
        
        print("after x_function() is called")
    
    return wrapper
    
def byItselfOrImported():
    if __name__ == "__main__":
        print("run on its own")
    else:
        print("imported")

byItselfOrImported()