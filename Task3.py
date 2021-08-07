"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv


# Start method find_code(calls)
def find_code(calls_):
    """
  :param calls_: this list contains calling telephone number (string), receiving telephone number (string)
    , start timestamp of telephone call (string), duration of telephone call in seconds (string).
  :return: all of the area codes and mobile prefixes called by people in Bangalore.
  """
    F_code_ = []
    for call in calls_:  # --> O(n)
        if call[0][:5] == '(080)':  # If fixed lines
            if call[1][0] == '(':
                index = call[1].find(")")
                if call[1][:index + 1] not in F_code_:
                    F_code_.append(call[1][:index + 1])  # --> O(n^2)
            elif call[1][:3] == '140':  # If telemarketers
                if call[1][:3] not in F_code_:
                    F_code_.append(call[1][0:3])  # --> O(n^2)
            elif call[1][0] == '7' or '8' or '9':  # If mobile numbers
                if call[1][:4] not in F_code_:
                    F_code_.append(call[1][:4])  # --> O(n^2)

    F_code_.sort()  # --> O(nlogn)
    return F_code_


# End method find_code(calls) --> this method with time complexity O(n^2).


def percentage(calls_):
    """
    :param calls_:this list contains calling telephone number (string), receiving telephone number (string)
    , start timestamp of telephone call (string), duration of telephone call in seconds (string).
    :return: percentage of calls from fixed lines in Bangalore are made to fixed lines also in Bangalore.
    """
    called = 0
    total = 0

    for call in calls_:
        if call[0][:5] == '(080)':
            total += 1
            if call[1][:5] == '(080)':
                called += 1

    return round((called / total) * 100, 2)


# Read from excel file (texts.csv).
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

# Read from excel file (calls.csv).
with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
"""

print("The numbers called by people in Bangalore have codes:")
F_code = find_code(calls)
for i in F_code:
    print(i)

print('__________________________________________')
print(' ')

"""
Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?
"""

percentage = percentage(calls)
print(percentage, "percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
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
