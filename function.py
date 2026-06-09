def addition (a,b):
    return  a+b
    

sum= addition(10,5)
print(sum)

def calc_average (a,b,c):
    sum = a+b+c
    avg = sum/3
    print(avg)
    return(avg)

calc_average(34,56,78)

numbers = [1,2,3,4,5,6,7]
tuple = (1,2,3,4,5,6,7,8)

def print_len(numbers):
    print (len(numbers))
    
print_len(numbers)
print_len(tuple)

cities = ["Mumbai", "Delhi", "BBSR", "Bhopal", "Indore"]
Animals = ["Lion", "Tiger", "Cow", "crow", "dog"]

def print_values(list):
    for item in list:
        print(item, end=" ")

print_values(cities)
print_values(Animals)

