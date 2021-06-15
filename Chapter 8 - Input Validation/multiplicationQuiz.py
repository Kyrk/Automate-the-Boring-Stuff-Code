#!/usr/bin/env python3
# Example program that uses PyInputPlus to create a timed multiplication quiz.
import pyinputplus as pyip
import random, time
numberOfQuestions = 10
correctAnswers = 0

for questionNumber in range(numberOfQuestions):
    # Pick two random numbers
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)

    prompt = '#%s: %s x %s = ' % (questionNumber + 1, num1, num2)

    try:
        # Right answers are handled by allowRegexes.
        # Wrong answers are handled by blockRegexes, with a custom message.
        pyip.inputStr(prompt, allowRegexes=['^%s$' % (num1 * num2)],
                blockRegexes=[('.*', 'Incorrect!')],
                timeout=8, limit=3)
    except pyip.TimeoutException:
        # If user answers after 8-second timeout expired, raise exception.
        print('Out of time!')
    except pyip.RetryLimitException:
        # If user answers incorrectly more than 3 times, raise exception.
        print('Out of tries!')
    else:
        # This block runs if no exceptions were raised in the try block.
        print('Correct!')
        correctAnswers += 1
        time.sleep(1)   # Brief pause to let user see the result.

print('Score: %s / %s' % (correctAnswers, numberOfQuestions))
