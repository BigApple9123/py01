#Fizz Buzz
#prints the numbers from 1 to 100 inclusive 
#1)for multiples of 3 print **Fizz** instead of number 
#2)for multiples of 5 print **Buzz** instead of number 
#3)for numbers which are multiples of both 3 & 5 print **FizzBuzz** instead 
i=1
while i <= 100:
    if i%3==0 and i%5==0:
        print('FizzBuzz')
    elif i%3==0:
        print('Fizz')
    elif i%5==0:
        print('Buzz')
    else:
        print(i)
    i+=1

#Number adder
#create a program that prompts the user for 2 numbers. Display the sum back to the user
#prompt the user for the operand
#create an interesting format for the response
num1=input('Enter a number:')
while not num1:
    num1=input('Please enter a number')
num2=input('Enter another number:')
while not num2:
    num2=input('Please enter another number')
mysum=num1+num2
print('The sum of {} and {} is {}'.format(num1, num2, mysum))

#Statistics on lists of numbers
#create a program that allows the user to enter as many numbers as they want until the user types **Q**
#When the user enters **Q**, display some statistics about the list 
#use the **statistics** module into your program and use its methods to calculate statistics
num=input('Enter a number:')
mylist=[]
while num != 'Q':
    if num.isnumeric()==True:
        mylist.append(int(num))
    num=input('Enter a number, enter **Q** to see statistics about the list of numbers you entered:')
mysum=sum(mylist)
print('The sum of the list of numbers you entered is {}'.format(mysum))

#Store data in a dictionary
#create a script that uses the console to capture some required demographic data about a subject(e.g. id, sex, age, race, etc.)
#Store the data in a dictionary. If the user types **print** then print the contents of the dictionary
#add some validation to ensure the input is acceptable(e.g. no strings for age, no missing values for sex)
#take some action if the user fails to reply properly after 3 promts for correct input
demo=input('Enter demographic data about a subject using the format **=** using lowercase, e.g id=10001-0106:')
err=0
mydict={}
while demo != 'print':
    mykey=demo.split('=')[0]
    myvalue=demo.split('=')[1]
    if mykey=='age' and myvalue.isnumeric()==False:
        print('No strings for age!')
        err += 1
        if err==3:
            break
    elif mykey=='sex' and not myvalue:
        print('No missing values for sex!')
        err += 1
        if err==3:
            break
    else:
        mydict[mykey]=myvalue
    demo=input('Enter demographic data about a subject using the format **=** using lowercase, e.g id=10001-0106, enter **print** to see current contents:')
else:
    print(mydict)
    
#Random number guesser
#create a program that
#1)defines a random number-you will need to use the **random** module
#2)continue to ask the user to input an integer until the value is correct
#3)alert the user if the guess if too high or low
#4)if the user guesses the correct answer, print a congratulations message, tell the user how many tries it took, and leave the loop
#5)allow the user to leave the loop anytime by typing **Q**
import random 
rnum=random.randint(0, 100)
num=int(input('Guess the number:'))
time=1
while num != rnum:
    if num < rnum:
        num=int(input('Your guess is too low! Make another guess:'))
        time += 1
    elif num > rnum:
        num=int(input('Your guess is too high! Make another guess:'))
        time += 1
    if num=='Q':
        break
if num==rnum:
    print('Contratulations! Your guess is correct. Your total # of attempted guess is {}'.format(time))