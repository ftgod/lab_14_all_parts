"""
cake.py
=====
Write a program that asks for cake and handles a yes, no, or anything other than yes or no.  It will say different things depending on the user's answer.  Here's an example:

Do you want cake?
> yes
Here, have some cake.

Do you want cake?
> no
No cake for you.

Do you want cake?
> blearghhh
I do not understand.
"""


cake = raw_input('Do you want cake?\n> ')
if cake == 'yes' or cake == 'yeah':
	print('Here, have some cake.')
elif cake == 'no':
	print('NO LAZER FOR YOU (but I meant cake)')
elif cake == 'maybe':
	print('MAKE UP YOUR MIND (Star Trek reference: He\'s dead Jim)')
else:
    print('I do not understand.')