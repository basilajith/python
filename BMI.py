# A simple programme to find a person's BMI and identify the weight category in which he is classified
print "What is your name?"
name = raw_input ('> ')

print "Okay %s, how much do you weigh? Say it in kilograms." % name
weight = float (raw_input ('> '))

print "What is your height %s? Say it in metres." % name
height = float (raw_input ('> '))

bmi = float (weight / (height * height))
print "\n"
print "In that case, your BMI is %s." % bmi

if bmi <  18.5:
	print "Which means, you are underweight %s.\n" % name
else:

	if bmi > 18.5 and bmi < 24.9:
		print "Which means, your weight is normal %s.\n" % name
	else:

		if bmi > 24.9 and bmi < 29.9:
			print "Which means, you are overweight %s.\n" % name
		else:
		
			if bmi > 29.9 and bmi < 34.9:
				print "Which means, you are obese of the first degree %s.\n" % name
			else:
			
				if bmi > 34.9 and bmi < 39.9:
					print "Which means, you are obese of the second degree %s.\n" % name
				else:
				
					if bmi > 39.9:
						print "Oh my! You have extreme obesity!\n"
