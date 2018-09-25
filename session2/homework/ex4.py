hcm = int(input('input cm : '))
hm  = float(hcm/100)
kg       = float(input('input kg : '))
BMI      = kg/(hcm*hm)

if BMI < 16:
    print('You are underweight')
elif BMI < 18.5:
    print('Underweight')
elif BMI < 25:
    print('Normal')
elif BMI < 30:
    print('Overweight')
else:
    print('Obese')