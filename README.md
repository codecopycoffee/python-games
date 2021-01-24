# Python-Games
Python games
Sound effects courtesy of: https://opengameart.org/users/dklon

Pong - Created following Christian Thompson's (https://www.youtube.com/channel/UC2vm-0XX5RkWCXWwtBZGOXg) tutorial.  
Challenges:
* Thompson uses Python3 and states in the tutorial he doesn't think there are any differences between the versions for this project. I used Python 2 to test that claim, and found that onkeypress() only works in Python 3, while onkey() works in both Python 2 and Python 3.
* Initially I was unable to get my paddles to work properly - the ball passed right through them. I thought at first that I had written the code incorrectly, but quickly realized I had reversed the left and right paddle code. This taught me to be more careful about the order I'm working in and making sure to maintain consistent order throughout my code.

Connect4 - Created following Keith Galli's (https://www.youtube.com/channel/UC4JX40jDee_tINbkjycV4Sg) tutorial.  
Challenges:
* This was my first time using numpy. I used Homebrew to install it, but when I attempted to run my file I got an error message saying that numpy was not found. I did some research and learned how to modify PYTHONPATH so Python could locate numpy.

<img src="https://github.com/codecopycoffee/python-games/blob/master/pong_preview.png" alt="pong game screenshot" width="500px" height="auto">
