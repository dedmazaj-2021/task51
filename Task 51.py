from math import sqrt

def simple(number):    #this function checks whether a number is prime
    square_root = int(sqrt(number)) + 1
    if number % 2 == 0:
        return False
    else:
        for i in range(3, square_root, 2):
            if number % i == 0:
                return False
        else:
            return True

def check(input_value):   #this function checks how many variations of a number are prime
    count = 0
    lenght = len(input_value)
    for i in range(0, 10):
        processed_value = int(input_value.replace('*', str(i)))
        if simple(processed_value) and len(str(processed_value)) == lenght:
            count += 1
    return count;

def minimal(value):  #this function finds the minimum number of possible variations
    list = []
    for i in range(0, 10):
        variation = value.replace('*', str(i))
        if simple(int(variation)):
            list.append(variation)
    list.sort()
    return list[0]

break_out_flag = False

for numb in range(100000, 1000000):   #in the main loop we check all six-digit numbers
    number_as_string = str(numb)
    if simple(numb):
        for digit in range(0, 10):
            if number_as_string.count(str(digit)) == 3:
                number_as_string = number_as_string.replace(str(digit), '*')
                if check(number_as_string) > 7:
                    break_out_flag = True
                    print(minimal(number_as_string))
                    break
    if break_out_flag == True:
        break
                    
















    
