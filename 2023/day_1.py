'''
Advent of Code 2023, Day 1:

We are given a list of alpha-numeric strings.
For part 1, the task is to search each string for the first occuring digit from the left, 
and the first digit from the right, and concatenate those into a two-digit number. 
The solution for part 1 is the sum of all these 'calibration values'.

In part 2, we are advised that whenever a digit is written out as text ('one', 'two'), 
those should be considered valid calibration values as well. 
'''


def day1():

    data = load_data()

    print("\nDAY 1")
    print("-------------\n")
    print(f"Solution for part 1: {part1(data)}")
    print(f"Solution for part 2: {part2(data)}")
    print('\n')

    return


def load_data():
    '''
    Loads in data from the given filepath, reading one line at a time, 
    stripping whitespace, and appending to a list. 
    '''
    data = []
    with open('./data/day1.txt') as f:
        for line in f.readlines():
            data.append(line.strip())

    return data


def part1(data):
    '''
    In part one, we first filter down each entry to digits only using a nested list comprehension.
    The first list comprehension iterates through each entry in the data.
    The second, for each entry, only keeps those characters that are digits 1-9.

    Once filterd, another list comprenhension runs through the data again. 
    In each case, if the entry only consists of a single digit, it uses that digit twice to create a two-digit number.
    Otherwise, it uses the first and last digit. Results are stored in the calibration_values list. 

    Lastly, we return the sum of calibration values. 
    '''
    digitised_entries = [[x for x in row if x in [digit for digit in '123456789']] for row in data]

    calibration_values = [int(row[0] + row[0]) if len(row) == 1 else int(row[0]+row[-1]) for row in digitised_entries]
    
    return sum(calibration_values)


def part2(data):
    '''
    Part 2 requires the conversion of digits as words to digits as characters. We use a dictionary for this. 

    We search for the first and last occurence of a key in the dictionary using .startswith() and .endswith()
    While searching, we consecutively trim characters off the front and end of the string. 
    This feels like a rather slow and clumsy way to go about it, and hopefully something I'll have time to improve in the future. 

    Looking for the second digit from the end requires a caveat in case we had trimmed down our string to only one character. 
    
    '''

    numbers = {
    '1':'1',
    '2':'2',
    '3':'3',
    '4':'4',
    '5':'5',
    '6':'6',
    '7':'7',
    '8':'8',
    '9':'9',
    'one':'1',
    'two':'2',
    'three':'3',
    'four':'4',
    'five':'5',
    'six':'6',
    'seven':'7',
    'eight':'8',
    'nine':'9'
}
    calibration_values = []
    for row in data:
        number1 = 0
        while number1 == 0:
            for x in numbers.keys():
                if row.startswith(x):
                    number1 = numbers[x]
                    break
            row = row[1:]
        number2 = 0
        
        while number2 == 0:
            if len(row) == 0:
                number2 = number1
                break
            for x in numbers.keys():
                if row.endswith(x):
                    number2 = numbers[x]
                    break
            row = row[:-1]
        calibration_values.append(int(number1+number2))


    return sum(calibration_values)




if __name__ == '__main__':
    day1()