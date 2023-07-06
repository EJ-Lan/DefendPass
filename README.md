# DefendPass
Defend Pass is a Python scripting project which uses a password API to help inform users if their password has been breached before

## Password API

I used the password API from (https://haveibeenpwned.com), you can find more details about the API and its functionalities at (https://haveibeenpwned.com/API/v3)

## Usage
* Make sure you have requests installed if not then in your terminal type `pip install requests`
* In the command line call the password_checker.py file followed by as many password arguments as you would like
* Example) `python password_checker.py arg1 arg2 arg3 etc`
* Your output will be recieved in a text file which will either inform you how many times your password has been found and whether you should keep the password or not
* Example) `mypassword123 was found 10473 times... you should probably change your password!` or `mypassword123 was NOT found. Carry on!`
