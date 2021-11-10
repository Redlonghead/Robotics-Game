# yesOrNo()
given a yes or no question, this function returns a True for yes and a False for no with editable lists for yes's and no's and any combination of capital and lowercase numbers

# printWait()
easy printer - wait for enter or print - wait for time function and it can clear after

by the way you can run this with only one argument (text) and it will default to waiting for Enter to be pressed, or pass a second argument of the time, in seconds, to wait until continuing and you can put c=True to clear after or leave it out to not clear

so all these work...

printWait("hi")

\>\>print hi the wait to enter, does not clear

printWait("hi", t=3)

\>\>prints hi, waits 3 seconds, does not clear

printWait("hi", True)

\>\>prints hi, waits for enter, and clears

printWait("hi", True, 4)

\>\>prints hi, waits 4 seconds, clears

printWait("hi", t=3, c=True)

\>\>prints hi, waits 3 seconds, does clear

# getCoords()
takes two numbers in num1, num2 format and returns a list of integer equivalents

it is a little lenient, so 1 , 1 works for example