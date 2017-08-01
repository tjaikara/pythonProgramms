
print("Python data types")

#Number variable
number = 500
#print that number
print (number)

#print memory location of number
print(id(number))

#array values
arry = [1,2,3,4]
#add 5 to array
arry.append(5)
#print array values
print (arry)
#print array values within range
print (arry[:2])
print(arry[1:4])
print (arry[1:])



x = {'one':1, 'two':2}
print (type(x), x)

#integer
a = 50
print(type(a), a)

#double
b = 50.2
print (type(b), b)

#castng
b = int(50.2)
print (type(b), b)

#Sting
z = "this is a  string"
print (type(z), z)

z = '''
    This 
    is 
    a string'''
print (z)


#dictionary
dictionary = dict(one = 1, two = 'two')
print (type(dictionary), dictionary)


#String manipulation
b = 'hello'
a = 'this %s is a string '%b
c = 'this {} is a string'.format(b)
print (a)
print (c)

#Boolean
boolean = True
print(type(boolean), boolean)
