hours = input("Enter hours:")

try:
  hours = float(hours)

except:
  print("Error, please enter numeric input")
  exit()

rate = input("Enter rate:")

try:
  rate = float(rate)
  if hours <= 40:
    pay = hours * rate
  else:
    pay = ((hours - 40) * (1.5 * rate)) + (40 * rate)
  print (pay)

except:
  print("Error, please enter numeric input")
