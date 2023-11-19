
try:
    age=int(input('enter ur age '))
    print (100/age)

# except (ZeroDivisionError,ValueError) as e:
#     print('please enter number')

except Exception:
    print('please enter number')




