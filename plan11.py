
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
'''
#file=open('F:\django-5\plan 11\plan111.txt','r') #read
#file=open('F:\django-5\plan 11\plan111.txt','w') #write
file=open('F:\django-5\plan 11\plan111.txt','a') # append

file.write('\n welcom2')

file.close()

# '''
# with open ('F:\django-5\plan 11\plan111.txt','a') as file:
#     file.write('\n welcome to python ')
import schedule
import time

def job():
    print("I'm working...")

schedule.every(3).seconds.do(job)
# schedule.every().hour.do(job)
# schedule.every().day.at("10:30").do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)
# schedule.every().day.at("12:42", "Europe/Amsterdam").do(job)
# schedule.every().minute.at(":17").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
