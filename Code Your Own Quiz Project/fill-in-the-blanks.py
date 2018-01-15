easy_quiz = """___1___ is the nickname given to Tardar Sauce, a snowshoe ___2___ that rose to online fame after several pictures of her ___3___ \
facial expressions were posted to ___4___ in late September 2012."""
easy_answers = ['Grumpy Cat', 'cat', 'annoyed', 'Reddit']

medium_quiz = """Dat ___1___ (a colloquial pronunciation of “that boy”) is a nickname given to a 3D character model of a green ___2___ \
riding a unicycle, typically accompanied by catchphrases like “here comes dat boi!” and “o ___3___ waddup,” that went viral on \
social media in early ___4___."""
medium_answers = ['boi', 'frog', 'shit', '2016']

hard_quiz = """Chef Boyardee is a brand of canned ___1___ products sold internationally by Conagra brands. The company was founded by
Hector Boiardi of ___2___ heritage in Cleveland, Ohio, U.S.A., in 1928. As Spongebob would sing,
'Meatball, meatball, ___3___ underneath. Ravioli, ravioli, ___4___!'"""
hard_answers = ['pasta', 'Italian', 'spaghetti', 'Great Barrier Reef']

answers = [easy_answers, medium_answers, hard_answers]
blank_space = ['___1___', '___2___', '___3___', '___4___']

def game_start():
    """
    function greets user and prompts user to enter a difficulty level
    """
    name = input('Please enter your name: ') # name is intentionally ignored
    print('Welcome xxxDookieMonster2017xxx!')
    print('Fill in the blanks with the correct answers to win!')
    print('You have 3 attempts to guess. All answers are CASE SENSITIVE!')
    print('Please select from [easy | medium | hard]: ')
    level = input()
    return difficulty_level(level)

def difficulty_level(difficulty):
    """
    function responds to users difficulty choice
    """
    if difficulty == 'easy':
        print('Wimp.')
        print(easy_quiz)
        quiz,answer = easy_quiz,easy_answers
    elif difficulty == 'medium':
        print('Saucy!')
        print(medium_quiz)
        quiz,answer =  medium_quiz,medium_answers
    elif difficulty == 'hard':
        print('Oooh big boi!')
        print(hard_quiz)
        quiz,answer = hard_quiz,hard_answers
    else:
        print('You illiterate peasant. Select from [easy | medium | hard]: ')
        level = input()
        return difficulty_level(level)
    return prompt(quiz,answer)
        

def prompt(question,answers):
    """
    function prompts user for an answer, and determines whether it is correct or wrong. if wrong, user is prompted to try again. user has 3 chances in total
    """
    answer_index, blank_index, guesses, chance = 0, 0, 0, 2
    while answer_index < len(answers):
        player_answer = input('Enter answer for ' + blank_space[blank_index] + ': ')
        if player_answer == answers[answer_index]:
            question = (question.replace(blank_space[blank_index],answers[answer_index])) #replaces the blank with the correct answer, and reprints the string
            print (question)
            answer_index += 1
            blank_index += 1
            print('Aww yiss!')
        else:
             print('Boo! Try again. You have ' + str(chance) + ' chances left.')
             chance -= 1
             max_guesses = 2
             guesses += 1
             if guesses > max_guesses:
                print('Doot doot (You failed!)')
                break
            
print (game_start())
