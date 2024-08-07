calls = 0
str = ''
list_of_str = []


def count_calls():
   global calls
   calls = calls + 1


def string_info(str):
    strbig = str.upper()
    strlow = str.lower()
    leng = len(str)
    result = (leng, strbig, strlow)
    count_calls()
    return result


def is_contains(str, list_of_str):
    count_calls()
    newlist = [i.lower() for i in list_of_str]
    if str.lower() in newlist:
        return True
    else:
        return False

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
