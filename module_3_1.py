def count_calls():
    global calls_
    calls_ += 1
    return calls_


def string_info(string):
    count_string = str(string)
    count_calls()
    return len(count_string), count_string.upper(), count_string.lower()


def is_contains(string, *list_to_search):
    count_calls()
    same_words = []
    for i in list_to_search:
        if i.lower() in string.lower():
            same_words.append(i)
        elif string.lower() in i.lower():
            same_words.append(i)
    if len(same_words) > 0:
        c = True
    else:
        c = False
    return c



calls_ = 0
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', 'ban', 'BaNaN', 'urBAN')) # Urban ~ urBAN
print(is_contains('cycle', 'recycling', 'cyclic')) # No matches
print(calls_)

