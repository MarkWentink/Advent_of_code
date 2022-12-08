# Input is a .txt file. Each row represents a calorie count for a snack. 
# Groups of snacks per elf are separated by empty rows.


def day_1():

    data = load_data()
    # Sum the calorie counts for each elf so that we have a list of total counts per elf
    # Sort the list in descending order, and revert back from iterable to list
    calorie_list = list(reversed(sorted([sum(x) for x in data])))
    
    # Part 1
    # Biggest total calorie count
    print(f"Solution to part 1: {calorie_list[0]}")

    # Part 2
    # Total of top 3 biggest calorie counts
    print(f"Solution to part 2: {sum(calorie_list[0:3])}")
 
    return


def load_data():
    '''
    load_data() parses a .txt file line by line, grouping the calorie counts per elf. 
    If an empty line is found, we move on to the next elf. 
    
    input: .txt file of one integer per line, with empty lines separating groups.
    
    output: a list of lists of calorie counts grouped by elf.
    '''
    data = []
    with open('./data/day1.txt') as f:
        elf = []
        for line in f.readlines():
            if line.strip() != '':
                elf.append(int(line.strip()))
            else:
                data.append(elf)
                elf = []
    return data



if __name__ == '__main__':
    day_1()


