
try:
    age=int(input('enter ur age '))
    print (100/age)

except ValueError as e:
    print('please enter number')
    print(e)
except ZeroDivisionError as r:
    print(r)
    




