import sys
print('Hello. This is a BMI calculator. If you want to know your BMI value I need to know some information about you. Do you want to check your BMI value? ')
while True:
    answear = input()
    if answear == 'yes':
        print('OK, now tell me what is your name.')
        break
    if answear != 'yes' and answear != 'no':
            print('You need to write "yes"  or "no" dummy!')
            continue
    if answear == 'no':
        print('OK. Have a nice day!')
        sys.exit()
        
name = input()
print('Great! ' + (name) + '.' + (' Now tell me how much you weight. Do not be ashamed.'))



while True:
    weight = int(input())
    if weight > 35 and weight < 250:
        print('Ok, and what about your height? How many cm?')
        break
    if weight <= 35 or weight > 250:
        print('Do not play with me, kiddo. Tell me your REAL weight. I will not judge you.')
        continue



while True:
    height = int(input())
    BMI = round((weight) / ((height/100) * (height/100)),2)
    if height > 100 and height < 250:
        print('Thank you, your BMI is: ' + str((BMI)) + '.')
        break
    if height <= 100 or height > 250:
        print('Gosh, ' + (name) +'! ' + ('I know that you are lying. I will ask once again. How tall are you [cm]?'))
        continue


print('Now.. Do you want to know if your BMI value is correct?')

while True:
    answear1= input()
    if answear1 == 'yes':
        print('Write your BMI value now:')
        break
    if answear1 != 'yes' and answear1 != 'no':
            print('You need to write "yes"  or "no".')
            continue
    if answear1 == 'no':
        print('OK. Your lost. Have a nice day!')
        sys.exit()


answear2 = float(input())
while True:
    if answear2 >= 18.5 and answear2 <= 24.9:
        print('Yes, it is correct. You do not have to worry. See you again!')
        sys.exit()
    if answear2 <18.4:
        print('Your BMI value is quite to low. You need to eat more. Enjoy!')
        sys.exit()
    if answear2 > 25.0:
        print('Dude! I am afraid about you! You weight way to much! Contact with your dietician and take care of yourself! Unless you are a body-builder. In that case, have fun.')
        sys.exit()

