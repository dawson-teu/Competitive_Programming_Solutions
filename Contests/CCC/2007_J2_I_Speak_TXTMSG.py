translation_dict = {
    'CU': 'see you',
    ':-)': 'I\'m happy',
    ':-(': 'I\'m unhappy',
    ';-)': 'wink',
    ':-P': 'stick out my tongue',
    '(~.~)': 'sleepy',
    'TA': 'totally awesome',
    'CCC': 'Canadian Computing Competition',
    'CUZ': 'because',
    'TY': 'thank-you',
    'YW': 'you\'re welcome',
    'TTYL': 'talk to you later',
}

message = input()
while not message == "TTYL":
    if message in translation_dict:
        print(translation_dict[message])
    else:
        print(message)
    message = input()
print(translation_dict[message])
