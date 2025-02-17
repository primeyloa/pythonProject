def createDictionary():
    '''Returns a tiny Spanish dictionary'''
    spanish = dict() # creates an empty dictionary
    spanish['hello'] = 'hola'
    spanish['yes'] = 'si'
    spanish['one'] = 'uno'
    spanish['two'] = 'dos'
    spanish['three'] = 'tres'
    spanish['red'] = 'rojo'
    spanish['black'] = 'negro'
    spanish['green'] = 'verde'
    spanish['blue'] = 'azul'
    print(spanish)
    return spanish


def main():
    '''Apparently "spanish" is lost in context since it
    was declared in a local scope, hence the function
    is initialized with a new variable to hold the data returned from the fnxn
    so that it can be used and referred to on another local scope'''
    dictionary = createDictionary()
    print(dictionary['two'])
    print(dictionary['red'])

createDictionary()
main()
print(createDictionary())