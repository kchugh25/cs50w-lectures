def announce(f):
    def wrapper():
        print("Function is about to start")
        f()
        print("done with the function")
    return wrapper

@announce
def hello():
    print("function")

hello()