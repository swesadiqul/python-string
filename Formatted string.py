#Programmer Sadiq
#By@Sadiqul Islam
#Formatted String



#formatted string
a = 34
b = 57
print(f'{a} + {b} = {a+b}')

#Example
c = 12
d = 10
print(' Value of c is = {}, Value of d is = {}'.format(c,d))

#Example
p = 67
q = 98

print(f' Value of p is = {p}  \n Value of q is = {q} \n Summation is = {p+q}')

#string concatenation from the user input
m = input('Enter the value of m: ')
n = input('Enter the value of n: ')

print(f'Value of m is = {m}, Value of n is = {n}, Concatenation is= {m+n}')

#you can formate any variable using by string formating method
name = 'Jubayer Ahmed'
print('My name is {}.'.format(name))

#we can print any list using by string formating method
mylist = [1,2,3,4,5]
print('The list is {}'.format(mylist))

#you can format any string to store in a variable
x = 4
y = 7
z = 'Value of x is = {}, Value of y is = {}'
print(z.format(x,y))

#you can replace or substitute into a string argument using by format method
msg = 'My score on C = {1}, Python = {0}, Java = {1}' .format(8,9.0,2)
print(msg)

