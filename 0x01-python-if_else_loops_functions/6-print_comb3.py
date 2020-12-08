#!/usr/bin/python3
for i in range(10):
        for j in range(10):
                if j > i:
                        print('{}'.format(i), end='')
                        if i != 8 or j != 9:
                                print('{}'.format(j), end=', ')
                        else:
                                print('{}'.format(j))
