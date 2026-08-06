# this is a program for age catagory checker 
# We have this project (if , elif)
age = int(input("Enter your age :"))

if age < 0 or age > 100:
    print('Please enter a realistec age.')
elif age <= 12:
    print('chlid')
elif age  <= 19:
    print('Teenager')
elif age <= 35:
    print('Youg adult')
elif age  <= 60:
    print('Adult')
else:
    print('senior')

if age >= 18:
    print('You can vote')