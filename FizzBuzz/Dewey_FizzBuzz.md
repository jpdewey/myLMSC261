# Initial Markdown for FizzBuzz homework

## Pseudocode (created in class 10-25):
Counter counting every integer from 1 to 100
  Counter will need to have a limit, to stop at 100
  while count something
Every integer that is divisible by 3 prints Fizz
Every integer that is divisible by 5 prints Buzz
Every integer that is divisible by both prints FizzBuzz
  If/else statements for these functions:
    If {variable} % 3 == 0, print "Fizz"
    If {variable} % 5 == 0, print "buzz"
    If {variable} % 3 == 0 and {variable} % 5 == 0, print "FizzBuzz"
    Else: print() (?)

## Trial and error
The first code tried resulted in stack overflow:

``` def func(count):
	for i in range(count + 1):
		while count >= 1 and count <= 100:
			if count >= 1 and count <= 100:
				print(count)
			elif count % 3 == 0:
				print("fizz")
			elif count % 5 == 0:
				print("buzz")
			elif count % 3 == 0 and count % 5 == 0:
				print("fizzbuzz")
			else: print(count)
///
func(1)
```
This is what I believe resulted in stack overflow


``` def func(count):
	for i in range(count + 1):
		while count >= 1 and count <= 100:
			if count >= 1 and count <= 100:
				print(count)
			elif count % 3 == 0:
				print("fizz")
			elif count % 5 == 0:
				print("buzz")
			elif count % 3 == 0 and count % 5 == 0:
				print("fizzbuzz")
			else: print(count)
///
func(count)
```
This also didn't work since the counter is not running


Then, I tried to create a code by first establishing a counter, then defining the if/else statements required to run the fizzbuzz:

``` def func(count):
	count = 0
	for i in range(count + 1):
		while count >= 1 and count <= 100:
			if count >= 1 and count <= 100:
				print(f"{count + 1}")
			elif count % 3 == 0:
				print("fizz")
			elif count % 5 == 0:
				print("buzz")
			elif count % 3 == 0 and count % 5 == 0:
				print("fizzbuzz")
			else:
				print(count)
///
func(count)
```

This also failed since the count had not been defined. So, I established the count first, then defined the function:

``` count = 1
def func(count):
	for i in range(count + 1):
		while count >= 1 and count <= 100:
			if count >= 1 and count <= 100:
				print(f"{count + 1}")
			elif count % 3 == 0:
				print("fizz")
			elif count % 5 == 0:
				print("buzz")
			elif count % 3 == 0 and count % 5 == 0:
				print("fizzbuzz")
			else:
				print(count)
///
func(count)
```

This also resulted in stack overflow of the number 2. So, I backtracked and established a working counter.

``` def func(count):
 for i in range(count + 1):
   print(f"{count + 1}")
```

This counter only printed the number 2 twice.

``` def func(count):
	for i in range(0,100):
		print(f"{count + 1}")
```

This counter printed 100 2's.

``` def fizzbuzz(count):
	for i in range(count + 1):
		print(f"{i}")
///
fizzbuzz(count)
```

This code just counted to 1, leading me to think I was ready to move forward and define the range of the Counter

``` def fizzbuzz(count):
	for i in range(count + 1):
		while count >= 1 and count <= 100:
			print(f"{i}")
///
fizzbuzz(count)
```
Python pranked me and this resulted in stack overflow

I tried redefining what was being counted by switching it to i, which also resulted in stack overflow:

``` def fizzbuzz(count):
	for i in range(count + 1):
		while i >= 1 and i <= 100:
			print(f"{i}")
///
fizzbuzz(count)
```

I then revisited previous code and came up with the idea to switch back to defining the range as (0,100), but then by adding within the print funcion section of the code:

``` def fizzbuzz(count):
	for i in range(0,100):
		print(f"{count} + 1")
///
fizzbuzz(count)
```

This resulted in an error I don't fully understand.

After a dialog with Rachel where I determined that I need to incorporate the fizz buzz earlier in the code, I tried this:
``` def fizzbuzz(count):
	while count >= 1 and count >= 100:
		for i in range(0,100):
			print(f"{count - i}")
///
fizzbuzz(count)
```

This did nothing.

I then realized I wrote contradicting statements, so I tried this:
``` def fizzbuzz(count):
	while count >= 1 and count <= 100:
		for i in range(0,100):
			print(f"{count - i}")
///
fizzbuzz(count)
```

This started counting(yay!) but added a - sign and was endless

``` def fizzbuzz(count):
	while count >= 1 and count <= 100:
		if count >= 1 and count <= 100:
			count + 1
		elif count % 3 == 0:
			print("fizz")
		elif count % 5 == 0:
			print("buzz")
		elif count % 3 == 0 and count % 5 == 0:
			print("fizzbuzz")
		else:		
			for i in range(0,100):
				print(f"{count - i}")
///
fizzbuzz(count)
```

Nothing was happening, since I failed to illustrate a print function in the counter, so I had to manually stop the invisible code from running and doing nothing

``` def fizzbuzz(count):
	while count >= 1 and count <= 100:
		if count >= 1 and count <= 100:
			print(f"{count + 1}")
		elif count % 3 == 0:
			print("fizz")
		elif count % 5 == 0:
			print("buzz")
		elif count % 3 == 0 and count % 5 == 0:
			print("fizzbuzz")
		else:		
			for i in range(0,100):
				print(f"{count - i}")
///
fizzbuzz(count)
```

This yet again resulted in stack overload, but I shall carry on with more trial and error
I tried adding an addition feature to line four of the print function:

``` def fizzbuzz(count):
	while count >= 1 and count <= 100:
		if count >= 1 and count <= 100:
			print(f"{count}", {count} + 1)
		elif count % 3 == 0:
			print("fizz")
		elif count % 5 == 0:
			print("buzz")
		elif count % 3 == 0 and count % 5 == 0:
			print("fizzbuzz")
		else:		
			for i in range(0,100):
				print(f"{count - i}")
///
fizzbuzz(count)
```

This resulted in an error

I revisited the original "Lovely" counter from class, but by adding the (0,100) range:

``` def fizzbuzz(count):
	for i in range(0,100):
		print(f"{count - i} Lovely!")
///
fizzbuzz(1)
```

This resulted in a count that went 1,0,-1,-2,etc. to -98

I changed the - to a + and I got a counter. I am relieved hahaha

``` def fizzbuzz(count):
	for i in range(0,100):
		print(f"{count + i} Lovely!")

///
fizzbuzz(1)
```
This was my counter.

``` def fizzbuzz(count):
	for i in range(0,100):
		while count >= 1 and count <= 100:
			if count % 3 == 0:
				print("fizz")
			elif count % 5 == 0:
				print("buzz")
			elif count % 3 == 0 and count % 5 == 0:
				print("fizzbuzz")
			else:
				print(f"{count + i}")
		print(f"{count + i}")
```
Another attempt:

``` def fizzbuzz(count):
	for i in range(0,100):
		print(f"{count + i}")
		while count >= 1 and count <= 100:
			if count % 3 == 0:
				print("fizz")
			elif count % 5 == 0:
				print("buzz")
			elif count % 3 == 0 and count % 5 == 0:
				print("fizzbuzz")
///
fizzbuzz(1)
```

This resulted in printing the number one, and then running invisible code that I had to terminate

``` def fizzbuzz(count):
	while count >= 1 and count <= 100:
		for i in range(0,100):
			print(f"{count + i}")
		if count % 3 == 0:
			print("fizz")
		elif count % 5 == 0:
			print("buzz")
		elif count % 3 == 0 and count % 5 == 0:
			print("fizzbuzz")
///
fizzbuzz(1)
```

This resulted in an endless stream of repeated counting from 1 to 100

My next attempt involved moving some things around to hopefully add the fizzes and buzzes in, but to no avail:
``` def fizzbuzz(count):
	while count >= 1 and count <= 100:
		for i in range(0,100):
			if count % 3 == 0:
				print("fizz")
			elif count % 5 == 0:
				print("buzz")
			elif count % 3 == 0 and count % 5 == 0:
				print("fizzbuzz")
			else:
				print(f"{count + i}")
///
fizzbuzz(1)
```

My next thought was to try changing the phrase "if count % 3 == 0" to "if i % 3 == 0" since I was getting a perfect counter without any fizz or buzz replacements. I thought this because I realized the variable count did not actually pertain to the numbers (I think), whereas i actually references the numbers. I also added parentheses to ensure that they were each being read as separate equations. Here is the code I came up with:

``` def fizzbuzz(count):
	if count >= 1 and count <= 100:
		for i in range(0,100):
			if (i % 3 == 0):
				print("fizz")
			elif (i % 5 == 0):
				print("buzz")
			elif (i % 3 == 0) and (i % 5 == 0):
				print("fizzbuzz")
			else:
				print(f"{count + i}")
///
fizzbuzz(1)
```

This resulted in the fizzes and buzzes being printed after the number they are pertaining to, without any fizzbuzzes

Next, I changed the order of the if/else statements in order to narrow it down in a more efficient manner. This resulted in fizzes, buzzes and fizzbuzzes, but they were still 1 ahead of where they should be:

``` def fizzbuzz(count):
	if count >= 1 and count <= 100:
		for i in range(0,100):
			if (i % 3 == 0) and (i % 5 == 0):
				print("fizzbuzz")
			elif (i % 3 == 0):
				print("fizz")
			elif (i % 5 == 0):
				print("buzz")
			else:
				print(f"{count + i}")
///
fizzbuzz(1)
```

I tried changing the order of the print and the if statement (which I was pretty sure wasn't going to work, but I had to give it a shot), and ended up with a syntax error:

``` def fizzbuzz(count):
	if count >= 1 and count <= 100:
		for i in range(0,100):
			print("fizzbuzz") if (i % 3 == 0) and (i % 5 == 0)
```

I tried changing the if/else statement to a while statement (which I also didn't think would work, but tried anyway), which resulted in endless fizzbuzzes:

``` def fizzbuzz(count):
	if count >= 1 and count <= 100:
		for i in range(0,100):
			while (i % 3 == 0) and (i % 5 == 0):
				print("fizzbuzz")
			while (i % 3 == 0):
				print("fizz")
			while (i % 5 == 0):
				print("buzz")
///
fizzbuzz(1)
```

Then, I added another formula within each if/else statement so that it prints the fizzes and buzzes on the numbers they are supposed to be replacing:

``` def fizzbuzz(count):
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
///
fizzbuzz(1)
```

This was successful!!!!

I then transferred this from the testing shell to a new .py file and tested it in terminal, which resulted in success!

### Other Troubleshooting

In addition to all of the above troubleshooting, there were additional issues regarding syntax: small typos, forgetting colons, etc.

Luckily, the more I practice, the fewer syntax errors I find myself making!
