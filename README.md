# CS110 Final Project Proposal
# Mario Bomber
## CS 110 Final Project
### Fall 2022
### [Assignment Description](https://docs.google.com/document/d/1H4R6yLL7som1lglyXWZ04RvTp_RvRFCCBn6sqv-82ps/edit?usp=sharing)

[Link to Replit](https://replit.com/join/lpjkntmecg-alexeskenazi)

<< [link to demo presentation slides](#) >>

### Team: Alex and Vishil
#### Team Members
 * Alex Eskenazi
 
 * Vishil Patel


## Project Description

A game where bombs and other items rain down from the sky and the character has to avoid the harmful ones and collect the reward items such as extra lives, money bags, and point amplifiers. The longer the character stays alive the more points it gets. The longer the user plays the harder it gets.

### Requirements:

#### Must Have
* Character moves horizontally with keyboad :white_check_mark:
* At least one type of item rains down. :white_check_mark:
* Item kills character on collision. :white_check_mark:
* Game restart :white_check_mark:
* Game quit :white_check_mark:

#### Nice to Have
* Lives are counted :white_check_mark:
* Game over on loosing all lives :white_check_mark:
* Scoring sytem :white_check_mark:
* Prize items :white_check_mark:
* Sound effects :white_check_mark:
* Background soundtrack :white_check_mark:

#### Dream
Different Levels
* Character choice.
* Score board :white_check_mark:
* Variety of power ups with different effects
* Boss fight - skill challenge to pass on levels
* Multiplayer

#### Additional Requirements
Requirements added after proposal
* Welcome screen  :white_check_mark:
* Game over screen :white_check_mark:
* Max score :white_check_mark:

:white_check_mark: Represents  fullfilled requirements

***    

## User Interface Design

- **Initial Concept**

  - [Welcome Screen](https://replit.com/@AlexEskenazi/final-project-alex-and-vishil#etc/alexvishil_welcome_screen.png)
  - [Game Screen](https://replit.com/@AlexEskenazi/final-project-alex-and-vishil#etc/alexvishil_game_screen.png)
  - [Game Over Screen](https://replit.com/@AlexEskenazi/final-project-alex-and-vishil#etc/alexvishil_gameover_screen.png)
    
    
- **Final GUI**
  - << You should also have a screenshot of each screen for your final GUI >>

***        

## Program Design

* Non-Standard libraries
    * << You should have a list of any additional libraries or modules used (pygame, request) beyond non-standard python. 
         For each additional module you should include
         - url for the module documentation
         - a short description of the module >>
   - Pygame - provides the graphing and event framework for the game.
* Class Interface Design (will provide this at the end of the project - see Class List below)
    * << A simple drawing that shows the class relationships in your code (see below for an example). This does not need to be overly detailed, but should show how your code fits into the Model/View/Controller paradigm. >>
        * ![class diagram](assets/class_diagram.jpg) 
* **Classes**
    * **Charater** - Screen object representing the main game character.
    * **Bomb** - Screen object representing a lethal bomb that reduced the number of character lifes and has a score value that corresponds to the score increase when the character avoids it.
    * **Powerup** - Screen object representing a powerup, that is, an object that provides
    extra powers like more lives or ghost-mode to become transparent to bombs.
    * **Scoreboard** - Scoreboard represents the model for the information displayd regarding the state of the game, including the score, lives, powerups, level, and high score
    * **GameController** Controlls the game flow

## Project Structure and File List

The Project is broken down into the following file structure:

* main.py
* src
    * << all of your python files should go here >>
* assets
    * << all of your media, i.e. images, font files, etc, should go here) >>
* etc
    * << This is a catch all folder for things that are not part of your project, but you want to keep with your project >>

***

## Tasks and Responsibilities 

   * Outline the team member roles and who was responsible for each class/method, both individual and collaborative.

## Testing

* << Describe your testing strategy for your project. >>

## ATP - Aceptance Test Procedure 

| Step | Procedure                                                           | Expected Result                                                                                        |
| ---- | ------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| 1    | Run the program                                                     | Application opens and welcome screen appears                                                           |
| 2    | Welcome screen - no action needed                                   | Welcome screen Space background displays                                                               |
| 3    | Welcome screen - no action needed                                   | Welcome screen shows static character image partially overlapping the title                            |
| 4    | Welcome screen - no action needed                                   | Game name, credits, and basic instructions are displayed                                               |
| 5    | Welcome screen - no action needed                                   | Background music is playing (locally not on Replit)                                                    |
| 6    | Welcome screen - Press s key while music is off                     | Music starts (note - music does not work on Replit, only on local                                      |
| 7    | Welcome screen - Press s while music is on                          | Music stops (note - music does not work on Replit, only on local                                       |
| 8    | Welcome screen - Press q                                            | Applicaiton cleanly exits                                                                              |
| 9    | Run the program to display the welcome screen                       | Application opens and welcome screen appears                                                           |
| 10   | Welcome screen - Press Space bar                                    | Game starts, the game screen shows and object start falling from the top to the bottom                 |
| 11   | Game - no actions needed                                            | Bombs come down on every lane at different (random) speeds                                             |
| 12   | Game - no actions needed                                            | Two 'lives' (mushrooms) come down along with the bombs                                                 |
| 13   | Game - no actions needed                                            | Character (Mario) displays at the bottom                                                               |
| 14   | Game - no actions needed                                            | Space background remains                                                                               |
| 15   | Game - Press Arrow Left                                             | Character moves to the left                                                                            |
| 16   | Game - Press Arrow Right                                            | Character moves to the right                                                                           |
| 17   | Game - Press Arrow Left multiple times                              | When character reaches the left border it reapears on the right side                                   |
| 18   | Game - Press Arrow Right multiple times                             | When character reaches the Right border it reapears on the left side                                   |
| 19   | Game - Falling Items                                                | When falling items reach the bottom they reappear at the top with new random speed                     |
| 20   | Game - Falling mushrooms                                            | When falling mushrooms reach the bottom they reapear at the top in random lanes with new random speeds |
| 21   | Game - character hits bomb                                          | Character loose one live - hearts in the scoreboard indicating the number of lives decrease            |
| 22   | Game - character hits bomb                                          | A sound is played and the word "BOOM!" appears in place of the bomb                                    |
| 23   | Game - toggle background music (press s key)                        | Sound of the character hitting a Bomb or a Mushroom still plays regardless of the music playing        |
| 24   | Game - hit multiple bombs for number of lives to reach zero         | Lifes indicator on the scoreboard shows zero lives                                                     |
| 25   | Game - character looses all lives                                   | Game over screen is displayed                                                                          |
| 26   | Game - character hits Life (mushroom)                               | A sound is played and the word "Life!" appears in place of the bomb                                    |
| 27   | Game - bomb reaches bottom                                          | The bomb score is displayed instead of the bomb                                                        |
| 28   | Game - bomb reaches bottom                                          | The game score is increased by the value of the bomb                                                   |
| 29   | Game - bomb reaches bottom                                          | The bomb reapears at the top of the screen with the same speed                                         |
| 30   | Game - mushroom reaches bottom                                      | Mushroom reapears at the top in a new lane                                                             |
| 31   | Game - Score Board - no action needed                               | Score board shows while game is on                                                                     |
| 32   | Game - Score Board - Lives - game start                             | Score board shows 3 lives at the begining                                                              |
| 33   | Game - Score Board - Lives - lives reach zero                       | Game ends and game over screen is displayed                                                            |
| 34   | Game - Score Board - Play game                                      | Score updates in score board as unexploded bombs reach the bottom of the screen                        |
| 35   | Game - Score Board - During first game                              | After intial run scoreboard Max Score shows 0                                                          |
| 36   | Game - Score Board - Second and subsequent times the game is played | As new games are played while the app is runnin the max score is updated accordingly                   |
| 37   | Game - Score Board - Close the app and re-run the game              | The max score is reset to zero when the application is re-started                                      |
| 38   | Game - Press S when music is off                                    | Music starts (note - music does not work on Replit, only on local                                      |
| 39   | Game - Press S when music is on                                     | Music stops (note - music does not work on Replit, only on local                                       |
| 40   | Game - Press Q                                                      | Application exits                                                                                      |
| 41   | Game - Press O                                                      | Game over screen is displayed                                                                          |
| 42   | Game - Press O                                                      | Partial score does not count towards maximum score                                                     |
| 43   | Game Over screen - no action needed                                 | Space background remains                                                                               |
| 44   | Game Over screen - no action needed                                 | Game over text and key instructions are displayed                                                      |
| 45   | Game Over - Press Space                                             | Restarts the game - Max score is updated acordingly                                                    |
| 46   | Game Over - Press Q                                                 | Application exits                                                                                      |
| 47   | Game Over screen - Press S when music is off                        | Music starts (note - music does not work on Replit, only on local                                      |
| 48   | Game Over screen - Press S when music is on                         | Music stops (note - music does not work on Replit, only on local                                       |

