num = int(input("How many numbers for average?"))
total_sum = 0

for n in range (num):
    numbers = float(input("Enter the number:"))
    total_sum += numbers

avg = total_sum / num

print("Average is : ", avg)
