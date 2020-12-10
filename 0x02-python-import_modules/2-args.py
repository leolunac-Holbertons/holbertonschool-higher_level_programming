#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if len(argv) == 1:
        print('0 arguments.')
    else:
        index = 1
        if len(argv) == 2:
            print('1 argument:')
        else:
            print('{} arguments:'.format(len(argv) - 1))
        for i in argv[1:]:
            print('{}: {}'.format(index, i))
            index += 1
