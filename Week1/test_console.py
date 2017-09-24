'''Python - Test How Debugging Works

Created: 09/24/2017
Author: Frank J Genova

'''

def get_guess():
    '''Get user input as guess'''

    print('Enter your guess:')
    guess = raw_input('>')
    return guess

def print_guess(guess):
    '''Print guess'''

    print('Here is the guess:')
    print('{}'.format(guess))
    return True

def main():
    '''Do main program to get guess and print it'''

    guess = get_guess()
    print_guess(guess)
    exit()

if __name__ == '__main__':
    main()
