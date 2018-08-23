n=raw_input()
if((n>='a' and n<='z')or(n>='A' and n>='Z')):
	if n in ('a','e','i','o','u','A','E','I','O','U'):
		print "is a vowel"
	else:
		print "is a consonant"
else:
	print "invalid"
