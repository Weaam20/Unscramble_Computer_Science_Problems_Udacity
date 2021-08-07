"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv


# Start method unique(texts ,calls)
def unique(texts_, calls_):
    """
    :param texts_:  this list contains sending telephone number (string), receiving telephone number (string)
    , timestamp of text message (string).
    :param calls_: this list contains calling telephone number (string), receiving telephone number (string)
    , start timestamp of telephone call (string), duration of telephone call in seconds (string).
    :return: list with different telephone numbers.
    """
    total_unique = []
    for text in texts_:
        if text[0] not in total_unique:
            total_unique.append(text[0])

    for call in calls_:
        if call[0] not in total_unique:
            total_unique.append(call[0])

    for text in texts_:
        if text[1] not in total_unique:
            total_unique.append(text[1])

    for call in calls_:
        if call[1] not in total_unique:
            total_unique.append(call[1])

    return total_unique
# End method unique(texts ,calls)


# Read from excel file (texts.csv).
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

# Read from excel file (calls.csv).
with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 1:
How many different telephone numbers are there in the records?
"""

# Number of telephone numbers in the records.
unique_list = unique(texts, calls)
print("There are", len(unique_list), "different telephone numbers in the records.")


"""
TASK 1:
How many different telephone numbers are there in the records?
Print a message:
"There are <count> different telephone numbers in the records."
"""
