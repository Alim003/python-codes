year = int(input("Which year do you want to check? "))

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")
  
 #leap year condition: on ovory year that ovonly divisÅbIo by 4
 #exeope every year that Ig evenly divågible
 #unless the year also evenly cilvågible by 400
