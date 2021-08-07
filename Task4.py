"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv


# Start find_all_telemarketers()
def find_all_telemarketers(calls_, texts_):
    """
    :param calls_: this list contains calling telephone number (string), receiving telephone number (string)
    , start timestamp of telephone call (string), duration of telephone call in seconds (string).
    :param texts_: this list contains sending telephone number (string), receiving telephone number (string)
    , timestamp of text message (string).
    :return: list contains all possible telemarketers.
    """
    telephone = []

    # find all receiving telephone number (in calls.csv)
    call_receivers = []
    for call in calls_:
        if call[1] not in call_receivers:
            call_receivers.append(call[1])

    # find all sending telephone number (in texts.csv)
    sending_telephone_number = []
    for text in texts_:
        if text[0] not in sending_telephone_number:
            sending_telephone_number.append(text[0])

    # find all receiving telephone number (in texts.csv)
    receiving_telephone_number = []
    for text in texts_:
        if text[1] not in receiving_telephone_number:
            receiving_telephone_number.append(text[1])

    for call in calls_:
        # if the number have telemarketers code and never send texts, texts or receive incoming calls.
        if (call[0] not in sending_telephone_number) and (call[0] not in receiving_telephone_number) and \
                (call[0] not in call_receivers):
            # to avoid duplicates in telemarketers
            if call[0] not in telephone:
                telephone.append(call[0])  # -->O(n^3)

    return telephone
# End find_all_telemarketers()


# Read from excel file (texts.csv).
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

# Read from excel file (calls.csv).
with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing.
"""

print("These numbers could be telemarketers: ")
telemarketers = find_all_telemarketers(calls, texts)
telemarketers.sort()
for i in telemarketers:  # print all telemarketers
    print(i)


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
