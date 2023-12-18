import math

print("This is Body-Mass Index calculator\nPlease enter your height as 5 9 if your height is 5 feet 9 inches\nEnter your weight in KGs")
height= input("Height = ").split()
for n in range(0,len(height)):
    height[n] = int(height[n])
weight = int(input("Weight = "))
#input of weight and height is done 
#height which is stored in the list is converted to integer
height_ft = height[0]
height_in = height[1]
#height in feet and height in inches are seprated 
ft_to_in = height_ft * 12
#height in feet is converted to inches 


height_final = ft_to_in + height_in
height_m = height_final * 0.0254

BMI = weight / height_m ** 2
BMI_final = round(BMI,1)
print(f"Your Body-Mass Idex is {BMI_final}")

if BMI_final < 18.5:
    print("You are Underweight")
elif BMI_final < 25:
    print("You have Healthy weight")
elif BMI_final < 30:
    print("You are Overweight")
else:
    print("You are Obese")
input()
