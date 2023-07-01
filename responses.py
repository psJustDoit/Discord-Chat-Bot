import random


def get_response(message: str) -> str:

    greetings = ['hello', 'yo', 'whats up', 'sup', 'eyo', 'sup sup']

    if message in greetings:
        return 'Howdy partner! I\'m a simple chat bot. I can roll a random number by typing \'roll\' or give simple responses currently. My programmer is not the brightest so be patient with me! :)'
    
    if message == 'roll':
        return str(random.randint(1, 10))
    
    if message == '!font':
        return '`LOOK AT THIS COOL MESSAGE FONT!` :D'
    
    if message == 'i love you':
        return 'Do you really mean that? ^^'
    
    return 'I didn\'t understand what you wrote. Try typing clearly next time -.-'