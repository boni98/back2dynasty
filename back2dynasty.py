"""

Author: Boni Zhang
Date created: February 26, 2020
Computer Science Lecture A
Lab section: 066
Project: Back to the Dynasty

"""

#global imports
import time
import random
import sys

#global variable
user_star = 0

'''
intro
- introduction to game
- greets user
'''

def intro():
    print('Hello!')
    time.sleep(1)
    print('Welcome to Back to the Dynasty.')
    time.sleep(1)
    user_name = input('Please tell me your name:\n')
    print('\nHi,', user_name, end='!\n')
    time.sleep(1)
    print('I’m so excited for the journey ahead of you!')
    print('Now, we will time travel back to one of the dynasty.')
    print()

'''
chooseDoor
- prompts user to choose a door 
- randomize door chosen
'''

def chooseDoor():
    time.sleep(1)
    print('You will be assigned to an identify card ranging from 1 star class to 5 star class randomly.')
    door = ''
    while door != '1' and door != '2' and door != '3' and door != '4' and door != '5':
        door = input('Please pick a door(1-5) and let you journey to start:\n')
    door = random.randint(1, 5)  # randomize choosen door
    return door

'''
rank
- gives user background story about themselves based on the door number they chose
'''

def rank(chooseDoor):  # FIXME: add more to stories
    time.sleep(1)
    global user_star
    user_star = chooseDoor
    if user_star == 1:
        print('\nYou are born into a very poor class. You are in rank 1. Your family is banned from the mainland. You live in a deserted plain, outside the borders of territory. People in your town does not have much education. Luckily, you were offer a pass to the mainland due to helping a injuired General. As you just got to mainland, you were recognized for your intelligence gave you the opportunity to go the palace to serve the emperor.')
    elif user_star == 2:
        print('\nYou are born into a poor class. You are in rank 2. Your family are beggars. You and your family have traveled all over the mainland begging for food and money. You were sold to a brothel to earn money for your family.')
    elif user_star == 3:
        print('\nYou are born into a middle class. You are in rank 3. Your family have a low-paying job. You work 5 part-time jobs a day from dawn to dusk. You were spotted for your ability to multitask.')
    elif user_star == 4:
        print('\nYou are born into a rich class. You are in rank 4. Your family is one of the honored general\'s family. You grew up learning how to self-defend yourself. You were acknowledged for your combat skills.')
    elif user_star == 5:
        print('\nYou are born into a very rich class. You are in rank 5. Your family is one royal families. You grew up visiting and playing the emperor and other royal families in the royal palace. You can get anything you want just by telling your parents. You were known for being rich as hell. ')
    print()

'''
welcome
- welcome user to palace
'''

def welcome():
    time.sleep(1)
    print('Welcome to the palace!')
    print('You all have been chosen to serve the emperor due to your distinct abilities.')
    print()


'''
rankUp
- increase rank
'''

def rankUp():
    global user_star
    rank = user_star
    rank = rank + 1
    print('Congratulations! The emperor raised your rank!')
    print('You are in rank ' + str(rank))
    if rank == 5:
        win()
        response = input(
            "Do you want to play again? (yes or y to continue playing): ")
        if response == "yes" or response == "y":
            reset()
        else:
            sys.exit()
    user_star = rank
    return rank

'''
rankDown
- decrease rank
'''

def rankDown():
    global user_star
    rank = user_star
    rank = rank - 1
    print('Oh no! You lost your rank position!')
    print('You are in rank ' + str(rank))
    if rank == 0:
        lose()
        response = input(
            "Do you want to play again? (yes or y to continue playing): ")
        if response == "yes" or response == "y":
            reset()
        else:
            sys.exit()
    user_star = rank
    return rank

'''
win
- win game
'''

def win():
    print('CONGRATULATIONS!')
    print('You have successfully secured your Empress position. You Won!')

'''
lose
- lose game
'''

def lose():
    print('GAME OVER!')
    print('You have failed secured your rank position. You Lost!')

'''
question1
- first question of journey
- implements rank up and down
- inform user of rank
'''

def question1():
    time.sleep(1)
    rank = user_star
    q1_answers = ['a', 'b', 'c']
    user_answer1 = ''
    while user_answer1 not in q1_answers:
        print('You have just entered the palace. You saw a group of maid-in-waiting girls starting problems by torturing another girl. What will you do?')
        print('(a) Help the poor girl out')
        print('(b) Ignore them')
        print('(c) Join them and bully her\n')
        user_answer1 = input('Enter an answer: \n')

    if user_answer1 == q1_answers[0]:
        rankUp()
    else:
        rankDown()

'''
question2
- second question of journey
- implements rank up and down
- inform user of rank
'''

def question2():
    time.sleep(1)
    rank = user_star
    q2_answers = ['a', 'b', 'c']
    user_answer2 = ''
    while user_answer2 not in q2_answers:
        print('\nThe head girl of the maid-in-waiting  group push her work of helping the noble consort measure her clothing measurement to you. You will:')
        print('(a) Take it')
        print('(b) Not take it')
        print('(c) Give it to your friend to do')
        user_answer2 = input('Enter an answer: \n')

    if user_answer2 == q2_answers[0]:
        rankUp()
    else:
        rankDown()

'''
question3
- third question of journey
- implements rank up and down
- inform user of rank
'''

def question3():
    time.sleep(1)
    rank = user_star
    q3_answers = ['a', 'b']
    user_answer3 = ''
    while user_answer3 not in q3_answers:
        print('\nThe noble consort has not been getting much attention from the emperor, so she has been losing weight. Do you tell her her real measurements?')
        print('(a) Yes')
        print('(b) No')
        user_answer3 = input('Enter an answer: \n')

    if user_answer3 == q3_answers[1]:
        rankUp()
    else:
        rankDown()

'''
question4
- fourth question of journey
- implements rank up and down
- inform user of rank
'''

def question4():
    time.sleep(1)
    rank = user_star
    q4_answers = ['a', 'b']
    user_answer4 = ''
    while user_answer4 not in q4_answers:
        print('\nAfter getting her measurements, you will make her clothes:')
        print('(a) More small')
        print('(b) More big')
        user_answer4 = input('Enter an answer: \n')

    if user_answer4 == q4_answers[0]:
        rankUp()
    else:
        rankDown()

'''
question5
- fifth question of journey
- implements rank up and down
- inform user of rank
'''

def question5():
    time.sleep(1)
    rank = user_star
    q5_answers = ['a', 'b']
    user_answer5 = ''
    while user_answer5 not in q5_answers:
        print('\nThe noble consort got many compliments on her clothes that you made for her. The imperial noble consort also wants you to make her one. You got a very rare fabric, what style clothing will you make?')
        print('(a) Fancy and extravagant')
        print('(b) Simple and elegant')
        user_answer5 = input('Enter an answer: \n')

    if user_answer5 == q5_answers[1]:
        rankUp()
    else:
        rankDown()

'''
question6
- sixth question of journey
- implements rank up and down
- inform user of rank
'''

def question6():
    time.sleep(1)
    rank = user_star
    q6_answers = ['a', 'b', 'c']
    user_answer6 = ''
    while user_answer6 not in q6_answers:
        print('\nWhile you were sleeping, the evil maid-in-waiting took some of your fabric. You woke up to find half of it gone, you will:')
        print('(a) Request the manager for more fabric')
        print('(b) Tell the manager that someone stole your fabric')
        print('(c) Wait and see')
        user_answer6 = input('Enter an answer: \n')

    if user_answer6 == q6_answers[2]:
        rankUp()
    else:
        rankDown()

'''
question7
- seventh question of journey
- implements rank up and down
- inform user of rank
'''

def question7():
    time.sleep(1)
    rank = user_star
    q7_answers = ['a', 'b']
    user_answer7 = ''
    while user_answer7 not in q7_answers:
        print(
            '\nThe servant of the imperial noble consort came to get the clothes, you will:')
        print('(a) Tell the servant your design')
        print('(b) Go to imperial noble consort to receive punishment')
        user_answer7 = input('Enter an answer: \n')

    if user_answer7 == q7_answers[1]:
        rankUp()
    else:
        rankDown()

'''
question8
- eighth question of journey
- implements rank up and down
- inform user of rank
'''

def question8():
    time.sleep(1)
    rank = user_star
    q8_answers = ['a', 'b']
    user_answer8 = ''
    while user_answer8 not in q8_answers:
        print('\nThe noble consort was visiting the Imperial noble consort when you got there. You not having the clothes ready for her was told by the servant. When asked why, you:')
        print('(a) Said that you had too many ideas')
        print('(b) Asked imperial noble consort to help you find the robber')
        user_answer8 = input('Enter an answer: \n')

    if user_answer8 == q8_answers[0]:
        rankUp()
    else:
        rankDown()

'''
question9
- nineth question of journey
- implements rank up and down
- inform user of rank
'''

def question9():
    time.sleep(1)
    rank = user_star
    q9_answers = ['a', 'b']
    user_answer9 = ''
    while user_answer9 not in q9_answers:
        print('\nThe imperial noble consort had a good impression on you, but the noble consort was talking bad about you. You:')
        print('(a) Compliment the imperial noble consort more')
        print('(b) Confront the noble consort')
        user_answer9 = input('Enter an answer: \n')

    if user_answer9 == q9_answers[0]:
        rankUp()
    else:
        rankDown()

'''  
question10
- tenth question of journey
- implements rank up and down
- inform user of rank
'''

def question10():
    time.sleep(1)
    rank = user_star
    q10_answers = ['a', 'b']
    user_answer10 = ''
    while user_answer10 not in q10_answers:
        print('\nAfter the noble consort left, will you tell the imperial consort that someone rob your fabric?')
        print('(a) Yes')
        print('(b) No')
        user_answer10 = input('Enter an answer: \n')

    if user_answer10 == q10_answers[0]:
        rankUp()
    else:
        rankDown()

'''  
question11
- eleventh question of journey
- implements rank up and down
- inform user of rank
'''

def question11():
    time.sleep(1)
    rank = user_star
    q11_answers = ['a', 'b']
    user_answer11 = ''
    while user_answer11 not in q11_answers:
        print('\nThe imperial noble consort gave you a small punishment and order people to find the robber. During this time, what will you do:')
        print('(a) Watch your stuff more carefully')
        print('(b) Follow the evil girl during her daily activities')
        user_answer11 = input('Enter an answer: \n')

    if user_answer11 == q11_answers[1]:
        rankUp()
    else:
        rankDown()

'''  
question12
- twelveth question of journey
- implements rank up and down
- inform user of rank
'''

def question12():
    time.sleep(1)
    rank = user_star
    q12_answers = ['a', 'b']
    user_answer12 = ''
    while user_answer12 not in q12_answers:
        print('\nYou found out that the evil girl is trying to get your friend on her side, you think she will probably give her sin to her. You will:')
        print('(a) Report to the manager')
        print('(b) Wait and see')
        user_answer12 = input('Enter an answer: \n')

    if user_answer12 == q12_answers[1]:
        rankUp()
    else:
        rankDown()

'''  
question13
- thirdteenth question of journey
- implements rank up and down
- inform user of rank
'''

def question13():
    time.sleep(1)
    rank = user_star
    q13_answers = ['a', 'b', 'c']
    user_answer13 = ''
    while user_answer13 not in q13_answers:
        print('\nMany palace consort are in need of people. Where will you go?')
        print('(a) Imperial noble consort')
        print('(b) Noble consort palace')
        print('(c) Other palace')
        user_answer13 = input('Enter an answer: \n')

    if user_answer13 == q13_answers[0]:
        rankUp()
    else:
        rankDown()

'''  
question14
- fourteenth question of journey
- implements rank up and down
- inform user of rank
'''

def question14():
    time.sleep(1)
    rank = user_star
    q14_answers = ['a', 'b']
    user_answer14 = ''
    while user_answer14 not in q14_answers:
        print('\nThe emperor came to visit the imperial noble consort. Emperor asked you, “Do you have any opinion on the illness that is going on throughout the country?”')
        print('(a) To send people out to help different part of the country')
        print('(b) As the emperor’s wife, I’m not allowed to talk about stuff outside the palace. ')
        user_answer14 = input('Enter an answer: \n')

    if user_answer14 == q14_answers[1]:
        rankUp()
    else:
        rankDown()


'''  
question15
- fifteenth question of journey
- implements rank up and down
- inform user of rank
'''

def question15():
    time.sleep(1)
    rank = user_star
    q15_answers = ['a', 'b', 'c', 'd']
    user_answer15 = ''
    while user_answer15 not in q15_answers:
        print('\nIt is Empress Dowager’s Birthday. What color will you wear to the birthday party?')
        print('(a) Blue')
        print('(b) Red')
        print('(c) Green')
        print('(d) White')
        user_answer15 = input('Enter an answer: \n')

    if user_answer15 == q15_answers[0] or user_answer15 == q15_answers[2]:
        rankUp()
    else:
        rankDown()

'''  
reset
- rest game
- run through game by calling other function in loop
'''

def reset():
    reset = "yes"
    while reset == "yes" or reset == "y":
        intro()
        choice = chooseDoor()
        rank(choice)
        welcome()
        question1()
        question2()
        question3()
        question4()
        question5()
        question6()
        question7()
        question8()
        question9()
        question10()
        question11()
        question12()
        question13()
        question14()
        question15()
        
'''
main
- run through game
'''

if __name__ == "__main__":
    reset()
