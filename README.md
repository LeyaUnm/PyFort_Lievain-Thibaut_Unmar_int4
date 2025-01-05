# Programming in Python's project : Fort Boyard Simulation 

# 1.General presentation :
	
 ## Contributors :
		
  - Lola Lievain-Thibaut : Logical Challenge , Chance Challanges , Main Program
  - Emeline Unmar : Math challenge , Père Fouras Challenge  , Utility functions , Final Challenge

 ##  Description : 

  This project simulates an interactive experience inspired by the famous TV show Fort Boyard. Players form a team, participate in various challenges, and earn keys to unlock the treasure room. The goal is to collect three keys by solving riddles, mathematical puzzles, or other games of logic and chance.
  
  ## Key Features :

  * Team Creation: Add players with roles and assign a team leader.
  
  * Diverse Challenges: Includes math puzzles, logic games, chance-based challenges, and Père Fouras’s riddles.
  
  * Attempt Management: Players have a limited number of attempts to complete challenges.
  
  * Progress Tracking: Players collect keys to unlock new stages.
  
  ## Technologies used : 

  * Programming Language: Python
  
  * Libraries:
  	json: Manages data for riddles and configuration.
	random: Used for challenge and riddle selection.
 
  * Development Tools: PyCharm
  
  ## Installation : 

  1. Clone the git repository in your IDE :
     - Copy the link : https://github.com/LeyaUnm/projet_python_Lievain-Thibaut_Unmar.git
     - Open your IDE, here VSCode.
     - Select " Clone Git Repository..." :
    
       ![Screenshot 2025-01-05 100204](https://github.com/user-attachments/assets/6436b80d-6563-432b-92ad-26c12cb10271)
       
     - Paste the URL in the entrance bar :
     
![Screenshot 2025-01-05 100248](https://github.com/user-attachments/assets/2fc20593-5d38-4b8a-b1f2-c197aa56553e)
     - Select the location of the file in your computer
     - Opend the Clone repository.
    
  2. Modification of the JSON file's path in the program :

     - Open the 2 JSON file
     - Right click on their name and select "copy path"
	![Screenshot 2025-01-05 101556](https://github.com/user-attachments/assets/f4d24d4e-c1ad-42cc-8210-c28c20c12d40)

     - Open the final_challenge's file and paste the path of the TRClues.json at line 8
     - Open the pere_fouras_challenge's file and paste the path of the PFRiddles.json at line 24
     

  
  ## How to use :
   - Open the main.py file and run it.
   - Enter your answer in the terminal
   - Your game is settle, you can now play.

# 2. Technical documentation :

* Game algorithm : 

The game algorithm follows these steps:

1.The game begins with an introduction to its rules and objectives.
2.Players form a team and designate one leader. Each player has a defined role.
3.The team selects and completes various challenges, each offering the opportunity to earn a key upon success.
4.Once the team has collected three keys, they gain access to the treasure room.
5.The game ends when the players enter the treasure room, symbolizing victory.

* Functions: 

## Chance challenges : 

### shell_game() :
* This function is the entire chance shell game. When you call this function, you are able to play the game. 
 * The game consists in choosing one of three shells, and one has a key under it. If the chosen shell doesn't have a key, we start again. 
 * If after two attempts the player does not find the key, they lose. Otherwise, they win the key.
 * It returns a boolean, True if the player succeeds, and False if he failed

### dice_game() :
* This function is the entire dice shell game. When you call this function, you are able to play the game. 
 * The game consists of rolling two dice. If one of them is a 6, the player wins. Otherwise, the master takes his turn doing the same. If he doesn't roll a 6, then we start over. This process repeats three times in total. If after three times no one has rolled a 6, then the game is a draw, and no one wins anything.
 * It returns a boolean, True if the player succeeds, and False if he failed

### chance_game():
* This function choses a game randomly between both games.
 * It uses the randint function to choose between 1 and 2, like a heads or tails, which picks and calls upon the chosen game. It also keeps in a variable the result of the game.
 * It returns a boolean, the result of whatever game the player played. 
  * This function is called in the Main function to avoid calling each game one at a time.


## Logic challenge :  Battleship  (advanced)

### next_player(player): 
* This function is used to change the current player.
 * When you call this function, it switches the active player between 0 and 1.
 * It returns the next player (1 if the input is 0, and 0 if the input is 1).
 * The parameter is the tuple that represents the previous player

### empty_grid():
* This function initializes the entire grid for the game.
 * When you call this function, it creates a blank 3x3 grid with empty spaces.
 * It returns the initialized grid.

### display_grid_ship(grid, message):
* This function is used to display a grid along with a message.
 * It takes in parameters the grid created with empty_grid() and a message created with a later function.
 * When you call this function, it prints the grid's current state and a custom message.
 * It does not return anything.

### ask_position(): 
* This function is used to ask the player for a position on the grid.
 * When you call this function, it prompts the player to input coordinates (line, column).
 * If the input is incorrect, it asks again until a valid position is entered.
 * It returns the coordinates as a tuple of integers.

### initialize():
* This function is used to place the player's boats on the grid.
 * When you call this function, the player can choose positions to place two boats.
 * If the chosen position is invalid or already occupied, the player is asked again.
 * It returns the grid with the boats placed.

### has_won(grid): 
* This function checks if a player has won the game.
 * When you call this function, it verifies if two “X” marks are present on the grid.
 * It returns True if there are two “X” marks, and False otherwise.

### turn(player, player_grid, player_shots_grid, opponent_grid): 
* This function handles one turn of the game for either the player or the master.
 * When you call this function:
 * If it's the master's turn, it chooses a random position to shoot. If it's the player's turn, they input a position to shoot.
 * Hits are marked with “X” , and misses are marked with “.” on the relevant grids. It does not return anything but updates the grids.
 * It takes into parameters which player is playing, the player grid containing all the information, as well as the shots the players have done. The opponent’s grid as well of course to keep track of the master’s grid if he wins or not.

### master_initialize(): 
* This function is used to initialize the master's grid by placing two boats randomly.
 * When you call this function, two boats are placed on random positions in the grid.
 * It returns the master's grid with the boats placed. It has no parameters

### battleship_game(): 
* This function calls upon turn() to run the game.
 * The game consists of sinking the opponent's two boats first.
 * When you call this function, it initializes the grids, alternates turns between the player and the master, and determines the winner.
 * It returns True if the player wins and False if the master wins.

## Math Challenges : 

### factorial(n):
* This function calculates the factorial of a number.
 * When you call this function, it multiplies all integers from 1 to n.
 * If n is 0, the function returns 1 as the factorial of 0 is defined to be 1.
 * It takes a single parameter n (int), which is the random number whose factorial is to be calculated.
 * It returns the factorial of n.

### math_challenge_factorial():
* This function challenges the player to find the factorial of a random number between 0 and 10.
 * When you call this function, it generates a random number n and prompts the player to input the factorial of n.
 * It compares the player's input with the correct factorial, and returns True if the player is correct, and False otherwise.

### is_prime(n):
* This function checks if a number is prime.
 * When you call this function, it verifies if the input n is divisible only by 1 and itself.
 * It returns True if n is prime and False otherwise.
 * The parameter is n (int), the number to be checked.

### nearest_prime(n):
* This function finds the closest prime numbers to n.
 * When you call this function, it checks if n is prime. If it is, the function returns [n]. Otherwise, it searches for the nearest lower and higher prime numbers to n.
 * It returns a list containing the closest prime numbers to n.
 * The parameter is n (int), the number for which nearest primes are calculated.

### math_challenge_prime():
* This function challenges the player to find the prime number closest to a random number between 10 and 20.
 * When you call this function, it generates a random number n and asks the player to input the closest prime number.
 * It checks if the player's input matches one of the nearest primes. It returns True if the player's input is correct, and False otherwise.

### math_roulette_challenge():
* This function challenges the player to solve a random mathematical operation (addition, subtraction, or multiplication).
 * When you call this function, it generates a list of 5 random numbers and a random operation (+, -, or *).
 * The player is prompted to solve the operation and input their answer.
 * It compares the player's input to the correct result. It returns True if the player's input is correct, and False otherwise.

## Json file reading

### load_riddles(file):
* This function loads the riddles from a JSON file.
 * When you call this function, it opens the specified file and reads its content using the json module.
 * It extracts the "question" and "answer" from each riddle in the file and stores them in a list of dictionaries.
 * It takes a single parameter, file (str), which is the path to the JSON file containing the riddles.
 * It returns a list of dictionaries, each containing a "question" and its corresponding "answer".

## Pere fouras riddle

### pere_fouras_riddle():
* This function runs a riddle challenge where the player has 3 attempts to answer correctly.
 * When you call this function, it loads the riddles from the PFRiddles.json file and randomly selects one riddle.
 * The player is given three attempts to answer the riddle correctly. If the answer is correct, the function prints "Correct!" and returns True.
 * If the answer is incorrect, the function substract 1 from the number of attempts left and notifies the player of the remaining attempts.
 * If the player fails to answer correctly after 3 attempts, the correct answer is displayed, and the function returns False.

## Final Challenge : 

### treasure_room():
* This function handles the treasure room challenge, where the player must guess the correct code word based on a series of clues.
 * When you call this function, it loads the clues and the code word from a JSON file, selects a random year and show, and displays the first 
 * three clues. The player then has three attempts to guess the code word.
 * If the guess is correct, the player wins and the game ends. If not, additional clues are provided, and the player has two more attempts.
 * The function prints the outcome of the game, whether the player wins or loses.
 * It does not return anything, but prints messages to indicate the result.

## Utility functions : 

### introduction():
* This function prints the introduction to the game, including the rules.
 * When you call this function, it outputs a welcome message and explains the objective of the game: collecting three keys through various 
challenges to unlock the treasure room.

### compose_equipe():
* This function creates a team of players by asking for their details.
 * When you call this function, it asks the user to enter the number of players (between 1 and 3). Then, for each player, it prompts for their name, profession, and whether they are the team leader.
 * The function ensures that at least one player is designated as the leader.
 * It returns a list of dictionaries, each containing details of a player, including their name, profession, whether they are the leader, and the number of keys they've won (initialized to 0).

### challenges_menu():
* This function displays a menu of challenges and prompts the user to choose one.
 * When you call this function, it presents the user with a list of challenge options (Mathematics, Logic, Chance, and Père Fouras's Riddles) and asks them to select a challenge by entering a number.
 * It ensures that the input is valid (between 1 and 4).
 * It returns the selected choice as an integer.

### choose_player(team):
* This function allows you to select a player from the team.
 * It takes in parameter the team created with the compose_equipe function above
 * When you call this function, it lists the players and their roles (Leader or Member), then prompts the user to choose a player by entering a number.
 * It ensures that the chosen number is valid and corresponds to one of the players in the team.
 * It returns the selected player as a dictionary containing the player's details.

## The main : 

### game():
* This is the main function that controls and starts the entire game.
 * When you call this function, it initiates the game, starting with the introduction and the composition of the team.
 * The player.s must then complete challenges to earn keys, which are tracked by the variable key. The goal is to collect three keys to access the final challenge.
 * The function loops until the player.s has.ve earned three keys. During each loop iteration, a player is chosen, and they must participate in one of four challenges (Math, Logic, Chance, or Pere Fouras's Riddle).
 * If the player.s succeeds in a challenge, they gain a key. If they fail, they can try again in the next round.
 * After collecting three keys, the player.s accesses the final challenge (treasure room) where they must guess a code word based on clues. The player.s has three attempts, and each attempt provides additional clues.
 * At the end, it tells the player.s if they have succeeded or not


## Input and error management : 

### Input Validation:
- Ensures players provide valid inputs (e.g., choosing between 1 and 4 in menus).
- Displays error messages for invalid entries.
### Error Handling:
- Loops until a valid input is provided.

# 3. Logbook

Friday, December 6th: Initial commit, task planning session, and getting familiar with how Git and GitHub work. Lola started working on the battleship program.

Friday, December 20th: Emeline worked on and completed her maths challenges, while Lola continued working on the battleship program. We had some issues with GitHub but managed to solve them.

Tuesday, December 24th: Solo session for Lola, finished the battleship game, and completed the chance challenges.

Thursday, December 26th: Emeline started working on the Père Fouras riddle and the treasure room.

Thursday, January 2nd: Lola started working on the Readme part 2. She tried to implement a history feature but kept encountering errors. Unable to fix it, she focused on helping Emeline and improving the battleship game. Meanwhile, Emeline finished the Père Fouras riddle and the final challenge for the treasure room.

Friday, January 3rd: We had a big panic because we didn’t check each other’s functions before. When we tried to check them, we realized that after every commit, the functions didn’t work. We tried to fix it but failed, so we created a new repository. Lola worked on the game() function, and Emeline worked on the utility functions. Then we copied and pasted everything from our computers into GitHub.

Saturday, January 4th: Final checks and full testing day. Finished the Readme file.

# 4. Testing and Validation

## Test strategies : 

### Specific Test Cases and Results:

Test Case: Verifying that the factorial function returns correct results for inputs ranging from 0 to 11.

![image](https://github.com/user-attachments/assets/8a27481b-c8a5-4f62-aea6-fd363acdabfc)

Result: The function passed all cases.


Test Case: Checking the identification of the nearest prime number when multiple prime numbers are equidistant.

![Screenshot 2025-01-04 230921](https://github.com/user-attachments/assets/3e02ee22-a417-46ef-87fe-4915c05b1377)

Issue Found: The initial algorithm did not handle cases with two equidistant prime numbers because it didn't search for prime number below the given number (e.g., 12, where both 11 and 13 are valid).

Resolution: The code was updated to return both primes, and the test confirmed the fix.


Test Case: Testing team composition with valid and invalid player inputs.

![Screenshot 2025-01-04 231200](https://github.com/user-attachments/assets/a5174645-2370-4253-a1ce-97a4a792b075)

Result: The application correctly handled errors, such as invalid player counts or missing leader assignments.

Test Case: Simulating a "battleship" challenge.

![Screenshot 2025-01-04 231634](https://github.com/user-attachments/assets/3204e235-7b47-42ff-9665-3dd856b90aee)

Result: The challenge ran as expected, with correct handling of player inputs and outputs.



  

