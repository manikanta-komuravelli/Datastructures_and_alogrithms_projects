"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
import re

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
code_list=[]
codes= [] 
fixed_line_calls_to_bangalore=0
total_line_calls_from_bangalore=0

for val in calls:
    if re.search('080',val[0]) and re.search('\(0',val[1]):
        codes.append(re.findall(r'\(([0-9]+)\)',val[1])[0])
    elif re.search('140',val[1][:3]):
        codes.append(val[1])
    elif val[1].startswith('7') or val[1].startswith('8') or val[1].startswith('9'):
        codes.append(val[1][0:4])
    if re.search('080',val[0]) and re.search('080',val[1]):
        fixed_line_calls_to_bangalore += 1
    if re.search('080',val[0]):
        total_line_calls_from_bangalore+= 1

       
code_list= sorted(list(set(codes)))

print("The numbers called by people in Bangalore have codes:")
for code in code_list:
    print(code)


percent= round((fixed_line_calls_to_bangalore/total_line_calls_from_bangalore)*100, 2)
print("{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(percent))

