weight = int(input ("Weight: "))
unit_choice = input ("Kgs or lbs? ")
if unit_choice.upper() == "L":
    converted = weight * 0.45
    print (f"You are {converted} kilograms")
elif unit_choice.upper() == "K":
    converted = weight * 2.2
    print(f"You are {converted} pounds")
else:
    print ("Please use 'K' or 'L' to enter your chosen unit")

