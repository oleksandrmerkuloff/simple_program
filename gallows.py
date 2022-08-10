import random
import time


def controlGraphicVERSION(version):

    gallows_graphic =[
'''
    + -------
            |
            |      
            |
            |
            |
        ======              
''',
'''
    + -------
            |
    O       |      
            |
            |
            |
        ======              
''',
'''
    + -------
            |
    O       |      
    |       |
            |
            |
        ======              
''',
'''
    + -------
            |
    O       |      
  / |       |
            |
            |
        ======              
''',
'''
    + -------
            |
    O       |      
  / | \     |
            |
            |
        ======              
''', 
'''
    + -------
            |
    O       |      
  / | \     |
   /        |
            |
        ======              
''',
'''
    + -------
            |
    O       |      
  / | \     |
   / \      |
            |
        ======              
''']
    
    print(gallows_graphic[version])



def greeting(fn):
    print('''
    Hi, this is a gallows game,
    you have to guess the hidden word.
    The subject of the hidden word is animals
    ''')
    
    def wrapper():

        return fn()

    return wrapper

@greeting
def playing_game():

    graphic_version = 0

    def type_question():
        hidden_animals_list = ['Alpaca', 'Alabai', 'Alligator', 'Ant', 'Badger', 'Beagle',
        'Baboon', 'Bee', 'Bird', 'Bison', 'Buffalo', 'Bullfrog', 'Bulldog']
        
        tech_list = ['Computer', 'Telephone', 'CCTV']

        car_list = ['BMW', 'AUDI', 'Mercedes', 'Ford', 'Tesla']

        type_of_game = input("""
    Enter type of word list: 
        1 - Animal
        2 - Tech
        3 - Car
        Answer: """)

        if type_of_game == '1':
            return hidden_animals_list
        elif type_of_game == '2':
            return tech_list
        elif type_of_game == '3':
            return car_list
    # create a hidden word
    

    hidden_word = random.choice(type_question())
    hidden_word = hidden_word.lower()
    
    print('Make a word...\n')

    hidden_char = []

    # Криво но формирую првильный список 
    for i in range(len(hidden_word)):
        hidden_char.append('=')

    wrong_char = []

    time.sleep(2)

    print('Ok, let\'s start!')
    
    controlGraphicVERSION(graphic_version)

    print('Wrongs chars: {}'.format(', '.join(wrong_char)))
    print('Hidden word: {}'.format(''.join(hidden_char)))

    
    while graphic_version < 6:
        
        answer = input('Enter char, please: ').strip().lower()
        if len(answer) > 1:
            print('Please, enter one char!')
        # Если буква есть в слове, то перебираем это слово с аомощью метода find и меняем символ '=' на эту букву 
        elif answer in hidden_word:
            char = -1
            while True:
                char = hidden_word.find(answer, char + 1)
                #перебираем слово на наличие буквы и возвращаем список символов 
                if char != -1:
                    hidden_char[char] = answer
                else:
                    break
        # Если нету, то в список неправильных букв +1 буква         
        else:
            wrong_char.append(answer)
            graphic_version += 1

        hidden_char_like_str = ''.join(hidden_char)

        if hidden_char_like_str == hidden_word:
            print('Greeting you are win!!!')
            print('You quess word it\'s: {}'.format(hidden_word.title()))
            break
        else: 
            controlGraphicVERSION(graphic_version)
            print('Wrongs chars: {}'.format(', '.join(wrong_char)))
            print('Hidden word: {}'.format(''.join(hidden_char)))

    else: 
        print('GAME OVER!!!')

        print('Right word is: {}'.format(hidden_word.title()))

if __name__ == '__main__':
    while True:
        
        playing_game()

        answer = input('Do you want to continue? (y/n)\n').lower()

        if answer == 'n':
            break