def menu(*args):
    while True:
        s = input('Choose: ').strip()

        if s in args:
            return s

        print(f'{s} is not a valid option; try again')
