def BMI(height, weight):
    #formual is weight by height square
    bmi = weight/(height**2)
    return bmi
 
#height and weight in meters and kgs
height = 1.79832
weight = 70
 

bmi = BMI(height, weight)
print("The BMI is", format(bmi), "so ", end='')
 

if (bmi < 18.5):
    print("underweight")
 
elif ( bmi >= 18.5 and bmi < 24.9):
    print("Healthy")
 
elif ( bmi >= 24.9 and bmi < 30):
    print("overweight")
 
elif ( bmi >=30):
    print("Suffering from Obesity")