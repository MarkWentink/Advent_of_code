
import collections

def generate_nrs(puzzle_range):

    numbers = []

    for i0 in range(2, 8):
        for i1 in range(i0, 10):
            for i2 in range(i1, 10):
                for i3 in range(i2, 10):
                    for i4 in range(i3, 10):
                        for i5 in range(i4, 10):
                            numbers.append(100000*i0+10000*i1+1000*i2+100*i3+10*i4+i5)
            
    numbers = list(x for x in numbers if x > puzzle_range[0])
    numbers = list(x for x in numbers if x < puzzle_range[1])

    return numbers



def star_one(puzzle_range):

    numbers = generate_nrs(puzzle_range)
    numbers = list(x for x in numbers if len(set(str(x)))<6)

    return len(numbers)


def star_two(puzzle_range):

    numbers = generate_nrs(puzzle_range)
    numbers = list(x for x in numbers if len(set(str(x)))<6)
    numbers = list(x for x in numbers if 2 in collections.Counter(str(x)).values())

    return len(numbers)

def Day_4(puzzle_range):
    print("\n Day 4 solutions: \n")
    print("Star one: ", star_one(puzzle_range))
    print("Star two: ", star_two(puzzle_range))
    print('\n------------------')

    return





if __name__ == '__main__':

    Day_4((234208, 765869))
   