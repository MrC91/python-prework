# Question 1:
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function

def hello_name(user_name):
    print("hello_ " +  user_name)
user_name = input('Enter USERNAME:')
hello_name(user_name)
    # your code here 

# Question 2 
# write a pythin function, first_odds that prints the odd numbers from 1-100 and returns nothing 
def first_odd():
    for i in range(1,101):
        if i % 2!=0:
            print(i)
first_odd()
#your code here
   

# Question 3
def max_num_in_list(a_list):
    maximum= a_list[0]
    for i in range(len(a_list)):
        if a_list[i]>maximum:
            maximum=a_list[i]
        return maximum
a_list=[10,20,30,40,50]
print(max_num_in_list(a_list))

# Question 4
def is_leap_year(a_year):
    if(a_year % 400==0):
        return True
    elif a_year % 100 == 0:
        return False
    elif a_year % 4 == 0:
        return True
    else:
        return False
a_year = int(input())
print(is_leap_year(a_year))

# Question 5
def is_consecutive(a_list):
    return sorted(a_list) == list(range(min(a_list)+1))
a_list = [2,3,4,5,6,7]
print(is_consecutive(a_list))
a_list = [1,2,4,5]
print(is_consecutive(a_list))