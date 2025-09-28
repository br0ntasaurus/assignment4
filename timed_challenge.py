# Pick one question from timed_challenge.txt
# Paste the question as a comment below
# Set a timer for 30 minutes and complete the question!



# First Repeated Value
# Return the first value that repeats in the collection.
# Input: [1, 4, 3, 5, 3, 2, 1]
# Output: 3


def first_repeated_value(values):
    seen = set ()
    for item in values:
        if item in seen:
            return item
        seen.add(item)
    return None