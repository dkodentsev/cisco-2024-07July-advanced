def menu(*args):
    while True:
        s = input(f'Choose ({'/'.join(args)}): ').strip()

        if s in args:
            return s

        print(f'{s} is not a valid option; try again')

if __name__ == '__main__':
    choice = menu('x', 'y', 'z')
    print(f'User chose {choice}')
