#taking inputs from user
weight = input("Enter your weight in KG: ")
height = input("Enter your height in m: ")
#converting data for suitable data type
weight_int = int(weight)
height_float = float(height)
#appying foumula
bmi = weight_int / (height_float * height_float)
bmi_int = int(bmi)
#getting final result
print(bmi_int)

