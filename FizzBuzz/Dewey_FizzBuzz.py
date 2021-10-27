def fizzbuzz(count):
	if count >= 1 and count <= 100:
		for i in range(0,100):
			if ((i + 1) % 3 == 0) and ((i + 1) % 5 == 0):
				print("fizzbuzz")
			elif ((i + 1) % 3 == 0):
				print("fizz")
			elif ((i + 1) % 5 == 0):
				print("buzz")
			else:
				print(f"{count + i}")
fizzbuzz(1)
