month = int(input("Enter the number of the month: "))

if month >= 4 and month <= 6:
	print("Boston is in Spring.")
elif month >= 7 and month <= 9:
	print("Boston is in Summer.")
elif month >= 10 and month <= 11:
	print("Boston is in Autum.")
elif month == 12 or month <= 3:
	print("Boston is in Winter.")
else:
	print("There are only 12 months in a year.")

