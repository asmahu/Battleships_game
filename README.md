# Battleships Game
**Player vs. CPU**
**About**

Battleship is known worldwide as a pencil and paper game which dates from war I. It was published by various companies as a pad-and-pencil game in the 1930s and was released as a plastic board game. The game has spawned electronic versions, video games, smart devices, apps and film.
This is a command line battleship game which designed to entertain Battleship fans.
This includes Title, Instruction, possibility to select size of board and number of ships, getting player's name, the score board, player score board, CPU score board and after each round there is a possibility to players to choose leave, replay or continue tha game.

![ami](views/Images/ami.PNG)

**Deployment**

This project developed manually from Gitpod command line interface using the CI's mock terminal for Heroku
Steps:
- Creating a Heroku Account/App 
- create/login into a heroku account
- In setting tab set the buildpacks to python and NodeJs 
- Connect to github search for github repository
- Deploy Branch
 
**Existing Features**

The ability to play agains CPU
Get board size and ships as only integer input is allowed
Get Player's name as only alphabet is allowed
The ability to make board for player and system.
Get Player's name as only alphabet is allowed
The ability to make board for player and system.
Coordinate matching functionality that player can't enter the same coordinte.
A score tracking system which can maintain  both cpu and player.
Score Area
Show result 
Game Control Area which player can make decision to leave, continue or replay the game.


**Features left to Implement**
To determine a time limitation for game in each round.

**Data Model**





**Testing PEP8 Online**
no error were found.

**Bugs**

In the first time I thought it was possible to run python code via (python3 -m http.server) whereas it should be run via Terminal.

**Remaining Bugs**

During pushing my code before deploying I forgot to handle this issue cause of time constraints and 
the way of deploying (deploy branch) the issue is just with output not in code I solved the problem in code.
- incorrect one:
'print("Invalid input: row and column \
must be an integer between 0 - {board.size - 1}\n")'
- correct one:
'print(f"Invalid input: row and column \
must be an integer between 0 - {board.size - 1}\n")'



Performance 
lighthouse images
 
Unfixed Errors
No erros.

Credits
I highly appreciate slack community and CI for helping me to solve any problems during this project.

Content
I often look for help in StackOverflow Community when I get stuck.

Media
