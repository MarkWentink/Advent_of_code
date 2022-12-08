

def day_3():

    data = load_data()
    
    # Part 1
    # Challenge is to identify which character features in both the first half and the second half of a string.
    # Characters are given a score 1-52, which must be summed across all strings. 
    total = 0
    for rucksack in data:
        # Split rucksack into its two compartments (halves of each string)...
        # and find the intersection between the sets of unique characters. This returns the only characters the two sets have in common. 
        duplicate = list(set(rucksack[:len(rucksack)//2]).intersection(set(rucksack[len(rucksack)//2:])))[0]
        # Keep a running total of the scores
        total += score(duplicate)

    print(f"Solution to part 1: {total}")
        

    
    # Part 2
    # Three consecutive lines in the .txt are in a group. Find the only character in common between all three lines. 
    
    # Make batches of three elves
    batches = []
    for i in range(len(data)//3):
        batches.append(data[3*i:3*i+3])

    # For each batch, find the item in common between all three rucksacks using the intersection of three sets
    # Then calculate its score and return the total sum.
    total = 0
    for batch in batches:
        duplicate = list(set(batch[0]).intersection(batch[1]).intersection(batch[2]))[0]
        total += score(duplicate)

    print(f"Solution to part 2: {total}")

    return


def score(item):
    """
    Takes in a single character, and returns its score leveraging its ASCII value. 
    """
    if ord(item) in range(65,91):
        value = ord(item)-38
    else:
        value = ord(item)-96
    return value


def load_data():
    """
    load_data() parses a .txt file, and appends each line as an entry to a list. 

    Input: .txt file 
    Output: list of lines
    """
    with open('./data/day3.txt') as f:
        data = [line.strip() for line in f.readlines()]
    
    return data



if __name__ == '__main__':
    day_3()


