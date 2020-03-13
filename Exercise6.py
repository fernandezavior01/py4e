number = 0
total = 0.0
while True :
  user = input("Enter a number:")
  if user == "done" :
      break
  try:
      fuser = float(user)
  except:
      print("Invalid input")
      continue
  number = number + 1
  total = total + fuser

print(total, number, total/number)
