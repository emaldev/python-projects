# this is a class for change (String , float , integer , boolean ) 
#        varaible together .

name = "12.45"
age = 20
gpa = 3.45
is_student = True

#====================================================
# this is printing the type of variable for exam
# there are the type of variable befor the change
#print(type(name)) # String = 'str'
#print(type(age)) # integer = 'int'
#print(type(gpa)) # float = 'float'
#print(type(is_student)) # boolean = 'bool'

#====================================================
# change integer to float 
age = float(age)
print(age)
print(type(age)) # this is after change of the variable
#====================================================
# change float to integer variable.
gpa = int(gpa)
print(gpa)
print(type(gpa))#this is type of after to change
#====================================================
# float to string
gpa = str(gpa)
print(gpa)
print(type(gpa))
#====================================================
#integer to boolean
age = bool(age)
print(age)
print(type(age))
#====================================================
#change boolean to integer
is_student = int(is_student)
print(is_student)
print(type(is_student))
#====================================================
# change string to float 
name = float(name)
print(name)
print(type(name))
#====================================================





