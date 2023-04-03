import ipdb
import time

# my_list = ['stuff', 'more stuff', 'even more stuff', 'wow stuff']

# for index, value in enumerate(my_list):
#     print(f'{index} is {value}')

# while True:
#     print('I will always be true')

def countdown(x):

    while x > 0:
        print(f'{x} SECOND(S)!')
        x -= 1

    print('HAPPY NEW YEAR!')

def countdown_with_sleep(i):

    while i > 0:
        print(f'{i} SECOND(S)!')
        i -= 1
        time.sleep(1)

    print('HAPPY NEW YEAR!')

# ipdb.set_trace()