
try:
    age=int(input('enter ur age '))
    print (age/100)

except ValueError as e:
    print('please enter number')
    print(e)



