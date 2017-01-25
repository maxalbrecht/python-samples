def my_decorator(some_function):
    def wrapper():
        num = 10
        if num== 10:
            print("Yes!")
        else:
            print("No!")
        
        some_function()
        
        print("something is happening after some_function() is called.")
    
    return wrapper
    
def byItselfOrImported():
    if __name__ == "__main__":
        print("this is being run by itself")
    else:
        print("This module is being imported")

byItselfOrImported()