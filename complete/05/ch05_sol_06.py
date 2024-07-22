weight = float(input('몸무게(kg): '))
height = float(input('신장(m): '))
bmi = weight / (height*height)
print('BMI : ', round(bmi,2))