x = 10

y = [10, 20, 30]

def hello(name):
    return f'Hello, {name}!'


# only print goodbye if the program was run, rather than imported
if __name__ == '__main__':
    print(f'Goodbye from {__name__}')
