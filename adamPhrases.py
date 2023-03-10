import random
# A storage of generic phrases adam can say

# acknowledgement phrases
ack_phrases = ['of course', 'Sure thing sir', 
                'Of course sir', 'Understandable', 
                'Always sir', 'Sure thing', 'Yes']
yes_phrases = ['yes', 'yeah', 'ok', 'okay', 'k', 'sure', 'yes please', 
                'please', 'alright', 'why not', 'do that', 'yeah sure']

def acknowledge():
    return ack_phrases[random.randint(0, 6)].lower()

# Generic Yes responses that prompt Adam to do something
def checkYes(statement):
    for phrase in yes_phrases:
        if phrase in statement:
            return True
    return False