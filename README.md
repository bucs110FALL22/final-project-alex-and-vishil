:warning: Everything between << >> needs to be replaced (remove << >> after replacing)
# CS110 Project Proposal
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
* Character moves horizontally with keyboad
* At least one type of item rains down.
* Item kills character on collision.
* Game restart
* Game quit

#### Nice to Have
* Lives are counted 
* Game over on loosing all lives
* Scoring sytem
* Prize items
* Sound effects
* Background soundtrack

#### Dream
Different Levels
* Character choice.
* Score board
* Variety of power ups with different effects
* Boss fight - skill challenge to pass on levels
* Multiplayer

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

## ATP

| Step                 |Procedure             |Expected Results                   |
|----------------------|:--------------------:|----------------------------------:|
|  1                   | Run Counter Program  |GUI window appears with count = 0  |
|  2                   | click count button   | display changes to count = 1      |
etc...
