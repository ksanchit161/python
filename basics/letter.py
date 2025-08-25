letter = ''' Dear |NAME|, 
You are selected!
|DATE|'''

letter = letter.replace("|NAME|", "SANCHIT").replace("|DATE|", "01-01-2023")
print(letter)
''