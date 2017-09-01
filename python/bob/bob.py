def hey(string):
    msg = 'Whatever.'
    if string.isupper():
        msg = 'Whoa, chill out!'
    elif string.rstrip().endswith('?'):
        msg = 'Sure.'
    elif string.isspace() or not string:
        msg = 'Fine. Be that way!'
    return msg
