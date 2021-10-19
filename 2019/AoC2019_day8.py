def parse_data(data, width, height):
    
    data = data[0]
    nr_layers = len(data)//(width * height)
    layer_pop = width * height
    parsed_data = []
    for i in range(nr_layers):
        layer = []
        for j in range(height):
            row = []
            for k in range(width):
                row.append(data[(i * layer_pop) + (j * width) + k])
            layer.append(row)
        parsed_data.append(layer)
        
    
    return parsed_data


def count_digits_in_layer(layer, digit):
    tmp = []
    for row in layer:
        tmp.extend(row)
    
    return tmp.count(digit)


def count_digits_per_layer(image, digit):
    
    digits_in_layers = []

    for layer in image:
        tmp = []
        for row in layer:
            tmp.extend(row)
        digits_in_layers.append(tmp.count(str(digit)))
    
    return digits_in_layers


def find_fewest_zeroes(image):

    zeroes = count_digits_per_layer(image, '0')
    
    return zeroes.index(min(zeroes))


def star_one(image):
    
    layer_nr = find_fewest_zeroes(image)
    
    return count_digits_in_layer(image[layer_nr], '1') * count_digits_in_layer(image[layer_nr], '2')


def determine_pixel(image, x,y):
    layer = 0
    if image[layer][x][y] != '2':
        return image[layer][x][y]
    else:
        while image[layer][x][y] == '2':
            layer += 1
        return image[layer][x][y]
    

def merge_image(image):
    merged_image = []
    height = len(image[0])
    width = len(image[0][0])

    for x in range(height):
        row = []
        for y in range(width):
            pixel = determine_pixel(image, x, y)
            row.append(pixel)
        merged_image.append(row)

    return merged_image

def star_two(image):
    
    merged = merge_image(image)

    for line in merged:
        row = ''
        for digit in line:
            if digit == '0':
                row += ' '
            else:
                row += digit
        print(row)

    return



def read_input():
    
    data = []
    
    with open('Data/AoC2019_8.txt') as f:
        for line in f.readlines():
            data.append(line.strip())
    
    return data


def Day_8():
    print("\n Day 8 solutions: \n")
    data = read_input()
    image = parse_data(data, 25, 6)
    print("Star one: ", star_one(image))
    print("Star two: ") 
    star_two(image)
    print('\n------------------')

    return





if __name__ == '__main__':

    Day_8()