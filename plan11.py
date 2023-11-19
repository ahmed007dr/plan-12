
# try:
#     age=int(input('enter ur age '))
#     print (100/age)

# # except (ZeroDivisionError,ValueError) as e:
# #     print('please enter number')

# except Exception:
#     print('please enter number')


#file=open('F:\django-5\plan 11\plan11.txt')
# data = file.readlines()

# for d in data:
#     print(d)

#file=open('F:\django-5\plan 11\plan111.txt','r') #read
#file=open('F:\django-5\plan 11\plan111.txt','w') #write
file=open('F:\django-5\plan 11\plan111.txt','a') # append

file.write('\n welcom2')

file.close()


