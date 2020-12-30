"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
text_sent= []
text_received=[]
call_placed=[]
call_received=[]
for val in texts:
    text_sent.append(val[0])
    text_received.append(val[1])
for val in calls:
    call_placed.append(val[0])
    call_received.append(val[1])

unique_list= list(set(text_sent+text_received+call_placed+call_received))
print("There are {} different telephone numbers in the records.".format(len(unique_list)))