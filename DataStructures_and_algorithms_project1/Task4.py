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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

text_sent= []
text_received=[]
call_placed=[]
call_received=[]

for call in calls:
    call_placed.append(call[0])
    call_received.append(call[1])

for text in texts:
    text_sent.append(text[0])
    text_received.append(text[1])
    
call_placed_unique= set(call_placed)   

all_others= set(call_received + text_sent + text_received)

call_suspects=[]

for call in call_placed_unique:
    if call not in all_others:
        call_suspects.append(call)
        

     
call_suspects= sorted(call_suspects)

print ("These numbers could be telemarketers: ")
for suspect in call_suspects:
    print(suspect)