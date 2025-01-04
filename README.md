Programming in Python's project : Fort Boyard Simulation 

1.General presentation :
	
 Contributors :
		
  - Lola Lievain-Thibaut : Logical Challenge , Chance Challanges , Main Program
  - Emeline Unmar : Math challenge , Père Fouras Challenge  , Utility functions , Final Challenge

  Description : 

  This project simulates an interactive experience inspired by the famous TV show Fort Boyard. Players form a team, participate in various challenges, and earn keys to unlock the treasure room. The goal is to collect three keys by solving riddles, mathematical puzzles, or other games of logic and chance.
  
  Key Features :

  Team Creation: Add players with roles and assign a team leader.
  
  Diverse Challenges: Includes math puzzles, logic games, chance-based challenges, and Père Fouras’s riddles.
  
  Attempt Management: Players have a limited number of attempts to complete challenges.
  
  Progress Tracking: Players collect keys to unlock new stages.
  
  Technologies used : 

  Programming Language: Python
  
  Libraries:
  	json: Manages data for riddles and configuration.
	random: Used for challenge and riddle selection.
 
  Development Tools: PyCharm
  
  Installation : 
  
  How to use :

2. Technical documentation :

o Game algorithm : 

The game algorithm follows these steps:

1.The game begins with an introduction to its rules and objectives.
2.Players form a team and designate one leader. Each player has a defined role.
3.The team selects and completes various challenges, each offering the opportunity to earn a key upon success.
4.Once the team has collected three keys, they gain access to the treasure room.
5.The game ends when the players enter the treasure room, symbolizing victory.

o Functions: 

§ Provide a list of function prototypes, including brief descriptions of their 
roles and parameter explanations. 

o Input and error management : 

§ Describe how the code handles input values, intervals, and the methods 
used for error management. 

§ Provide a list of known bugs. 

3. Logbook

o A logbook can help keep track of project progress and task allocation: 

Logbook:

Friday, December 6th: Initial commit, task planning session, and getting familiar with how Git and GitHub work. Lola started working on the battleship program.

Friday, December 20th: Emeline worked on and completed her maths challenges, while Lola continued working on the battleship program. We had some issues with GitHub but managed to solve them.

Tuesday, December 24th: Solo session for Lola, finished the battleship game, and completed the chance challenges.

Thursday, December 26th: Emeline started working on the Père Fouras riddle and the treasure room.

Thursday, January 2nd: Lola started working on the Readme part 2. She tried to implement a history feature but kept encountering errors. Unable to fix it, she focused on helping Emeline and improving the battleship game. Meanwhile, Emeline finished the Père Fouras riddle and the final challenge for the treasure room.

Friday, January 3rd: We had a big panic because we didn’t check each other’s functions before. When we tried to check them, we realized that after every commit, the functions didn’t work. We tried to fix it but failed, so we created a new repository. Lola worked on the game() function, and Emeline worked on the utility functions. Then we copied and pasted everything from our computers into GitHub.

Saturday, January 4th: Final checks and full testing day. Finished the Readme file.

4. Testing and Validation

o Test strategies : 

Specific Test Cases and Results:

Test Case: Verifying that the factorial function returns correct results for inputs ranging from 0 to 11.
![image](https://github.com/user-attachments/assets/8a27481b-c8a5-4f62-aea6-fd363acdabfc)
Result: The function passed all cases.

Test Case: Checking the identification of the nearest prime number when multiple prime numbers are equidistant.
![Screenshot 2025-01-04 230921](https://github.com/user-attachments/assets/3e02ee22-a417-46ef-87fe-4915c05b1377)

Issue Found: The initial algorithm did not handle cases with two equidistant prime numbers (e.g., 22, where both 11 and 13 are valid).

Resolution: The code was updated to return both primes, and the test confirmed the fix.
Game Start:

Test Case: Testing team composition with valid and invalid player inputs.

![Screenshot 2025-01-04 231200](https://github.com/user-attachments/assets/a5174645-2370-4253-a1ce-97a4a792b075)

Result: The application correctly handled errors, such as invalid player counts or missing leader assignments.

Test Case: Simulating a "battleship" challenge.

![Screenshot 2025-01-04 231634](https://github.com/user-attachments/assets/3204e235-7b47-42ff-9665-3dd856b90aee)

Result: The challenge ran as expected, with correct handling of player inputs and outputs.



  

