points = 174 # Enter input

result = {'wooden rabbit': 1-50, 'no prize':51-150, 'wafer-thin mint':151-180, 'penguin':181-200}

# Conditional statement
if points >= 151 <= 180:
  print("Congratulations! You won a wafer-thin mint")
elif points >= 181 <= 200:
  print("Congratulations! You won a penguin")
elif points >= 51 <= 150:
  print("oh dear, you won no prize")
elif points >= 1 <= 50:
  print("Congratulations! You won a wooden rabbit")
else: 
  print("oh dear,no prize this time")

#output 
print(result)