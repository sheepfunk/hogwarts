import re

def clean(message):
    """Standardize spacing and capitalization"""
    return ' '.join(m.lower() for m in message.split() if m)

def pluralized_points(num_points):
    if num_points == 1 or num_points == -1:
        return "%d newton" % num_points
    return "%d newtons" % num_points

def detect_points(message):
    amounts = [amount for amount in clean(message).split()
               if amount.isdigit()]
    if len(amounts) == 0 and 'one' in clean(message):
        amounts = [1]
    if len(amounts) == 1:
        return int(amounts[0]) * detect_point_polarity(message)
    else:
        return 0

def detect_point_polarity(message):
    """Discern whether this is a point awarding or deduction"""
    message = clean(message)
    if any(x in message for x in ["newtons to", "newton to", "newtons for", "newton for"]):
        return 1
    elif any(x in message for x in ["newtons from", "newton from"]):
        return -1
    else:
        return 0

def proper_name_for(house):
    """Forgive house misspelling"""
    if "dark" in house:
        return "Dark"
    if "light" in house:
        return "Light"

def get_houses_from(message):
    return list(set(proper_name_for(w) for w in clean(message).split() if proper_name_for(w)))
