print("welcome to tip calculator")
bill = float(input("what was the total bill? $"))
tip = int(input("how much tip would you like to give? 10 , 12 or 15? "))
people = int(input("how many people to split the bill?"))
bill_with_tip = tip / 100 * bill + bill
bill_per_person = bill_with_tip / people
final_amount = round(bill_per_person , 2)
print(f"each person should pay: ${final_amount}")
