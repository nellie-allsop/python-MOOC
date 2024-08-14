print("hello world")
# testing commenting
print("hiya")

# function with no parameter
def say_hello():
    print("Hiya love")

# calling the function
say_hello()

#function with parameter (name in this case)
def say_goodbye(name):
    print("Goodbye" + name)

say_goodbye("Claire")
# parameter is replaced by the argument "Claire"

#global scope
name = "Clover"

def say_name():
    name = "George" #local scope
    print("Hello " + name)

say_name()
print(name)

def square(num):
    return num * num

two_squared = square(2)

print(two_squared + 5)

numbers = [1,2,3,4,5]
# use lambda to double each number in last

double = list(map(lambda x: x * 2, numbers))

print(double)