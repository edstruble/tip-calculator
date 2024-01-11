#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator!")
bill = input("What is the total bill?\n")
desired_tip = input("How much tip would you like to give?\n")
people = input("How many people are splitting the bill?\n")
tip_percentage = int(desired_tip) / 100
bill_tip = int(bill) * tip_percentage
total = int(bill) + bill_tip
split = total / int(people)
print(f"Your total bill is ${total:.2f}. You decided to tip ${bill_tip:.2f} on top of that, so each person must pay ${split:.2f}, however Karen ordered an extra bottle of wine, so she actually owes all of the bill becuase she is a freeloading asshole who tried to get off light by evenly splitting the bill.")


# print(f"Each person should pay ${pay}")