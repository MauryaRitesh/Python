import speech_recognition as sr
import time

print ("Input a Number to get it's Factorial.")
choice = input("A. Give input by writing.\nB. Give input by Speech.\n")
choice = choice.upper()

if choice == 'A':
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Speak any number: ')
        audio = r.listen(source)
        print ('Done!')
    num = r.recognize_google(audio)
    print (num)
    n = int(num)

if choice == 'B':
    n = int(input("Enter a desired number"))
else:
    print ("Incorrect input.\nExiting...")
    time.sleep(2)
    exit()

def factorial(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    print ('Factorial of {} is: {}'.format(n,f))

factorial(n)



