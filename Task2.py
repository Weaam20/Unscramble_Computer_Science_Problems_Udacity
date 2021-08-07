import csv


# Start method longest_time(calls)
def longest_time(calls_):
    """
    :param calls_: this list contains calling telephone number (string), receiving telephone number (string)
    , start timestamp of telephone call (string), duration of telephone call in seconds (string).
    :return: list that contains telephone number spent the longest time on the phone and max.
    """
    total_unique = {}

    for call in calls_:
        if call[0] not in total_unique:
            total_unique[call[0]] = 0

    for call in calls_:
        if call[1] not in total_unique:
            total_unique[call[1]] = 0

    # Now we find all unique numbers.

    for call in calls_:
        total_unique[call[0]] += int(call[3])

    for call in calls_:
        total_unique[call[1]] += int(call[3])

    # calculate time on the phone during the period for each telephone number.

    # here we try to find telephone number spent the longest time on the phone during the period.
    max_ = 0
    longest_ = []
    for j in total_unique:
        if total_unique[j] > max_:
            max_ = total_unique[j]
            longest_.append(j)
            longest_.append(max_)

    return longest_
# End method longest_time(calls)


# Read from excel file (texts.csv).
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

# Read from excel file (calls.csv).
with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period?
"""
longest = longest_time(calls)
print(longest[0], "spent the longest time,", longest[1], " seconds, on the phone during")


"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
