"""
go_for_gold.py
=====
Translate an athlete's finishing placement (1st, 2nd and 3rd) into its Olympic medal value: 1 for gold, 2 for silver, 3 for bronze and anything else means no medal.  Do this by asking for user input.  For example:

What number should I translate into a medal?
>1
gold

What number should I translate into a medal?
>3
bronze

What number should I translate into a medal?
>23
no medal for you!

"""

"""Translate place number into Olympic medal.  FTW!"""


medal = raw_input('What number should I translate into a medal?\n>')
if int(medal) < 1 or int(medal) > 3:
    print('Not a valid placement, but try harder next year (AT LEAST FOR THE KNICKS HAHAHA!)')
elif int(medal) == 1:
    print('Gold')
elif int(medal) == 2:
    print('Silver')
elif int(medal) == 3:
	print('Bronze')
else:
    print("no medal for you!")