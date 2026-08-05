# This is a small school system for grading Student
#  I hava a big program in java this school system

name = input("Enter student name :")
math = float(input("Enter Math score :"))
english = float(input("Enter English score :"))
programming = float(input("Enter Promgramming score :"))

average = (math + english + programming) / 3
result = average
print(average)
print(f"Name: {name}")
print(f"Math: {math}")
print(f"English: {english}")



if result >= 90:
    print(f"Excellent : {average}")
elif result >= 70:
    print(f"Good : {average}")
elif result >= 50:
    print(f"Passed : {average}")
else:
    print(f"Failed : {average}")


