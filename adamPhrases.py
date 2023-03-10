import random
# A storage of generic phrases adam can say

# acknowledgement phrases
ack_phrases = ['of course', 'Sure thing sir', 
                'Of course sir', 'Understandable', 
                'Always sir', 'Sure thing', 'Yes', 'Spendid']
yes_phrases = ['yes', 'yeah', 'ok', 'okay', 'k', 'sure', 'yes please', 
                'please', 'alright', 'why not', 'do that', 'yeah sure']
no_phrases = ['no', 'nah', 'not right now', 'stop', 'i can do it', 
            'i got it', 'that is not necessary', 'i can get it', 'not really']

def acknowledge():  
    return ack_phrases[random.randint(0, 7)].lower()

# Generic Yes responses that prompt Adam to do something
def checkYes(statement):
    for phrase in yes_phrases:
        if phrase in statement:
            return True
    return False
def checkNo(statement):
    for phrase in no_phrases:
        if phrase in statement:
            return True
    return False