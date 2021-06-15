#!/usr/bin/env python3
'''
Program that recreates the example multiplication quiz without importing the
PyInputPlus module. Program will prompt user with 10 multiplication questions,
ranging from 0x0 to 9x9.
- If user enters correct answer, program displays 'Correct!' for 1 second and
  moves on to next question.
- User gets three tries to enter correct answer before program moves on to next
  question.
- Eight seconds after displaying question, question is marked as incorrect even
  if user enters the correct answer.
'''
import random, time

numberOfQuestions = 10
correctAnswers = 0

for questionNumber in range(numberOfQuestions):
    # Pick two random numbers:
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)
    # Prompt showing which random numbers to multiply
    prompt = '#%s: %s x %s = ' % (questionNumber + 1, num1, num2)
    attempts = 0
    start = time.time()

    while True:
        response = input(prompt)    # Input
        try:
            response = int(response)
            stop = time.time()  # Stop time used to compare between start time
        except ValueError: # If non-decimal is inputted
            print('ERROR: USE NUMERIC DIGITS')

        # Move to next question if user takes 8+ seconds to answer question
        if stop - start > 8:
            print('OUT OF TIME')
            break

        # Handle answers with custom message, add to score if correct
        if response == num1 * num2:
            print('CORRECT!')
            correctAnswers += 1
            break
        else:
            print('INCORRECT!')

        # Move to next question if too many attempts
        attempts += 1
        if attempts == 3:
            print('OUT OF ATTEMPTS')
            break

    time.sleep(1)   # Brief pause to let user see the result

print('Score: %s / %s' % (correctAnswers, numberOfQuestions))
