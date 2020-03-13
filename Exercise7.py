number = 0
total = 0.0
numbers = list()
while True:
  user = input("Enter number:")

  try:
    user = int(user)
    numbers.append(user)
    total = total + user
    number = number + 1
    maximum = max(numbers)
    minimum = min(numbers)

  except:
    if user == "done":
      break
    else:
      print ("Invalid Input")

print("Total:", total)
print("Number:", number)
print("Maximum:", maximum)
print("Minimum:", minimum)
