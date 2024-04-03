#### Game description
The game is a two-dimensional basketball simulation in which the player controls a basketball that must be shot into a hoop. The game consists of a fixed basket, a moving basketball and a static backdrop. The challenge of the game lies in the accuracy of the throw to score points. The game is designed to be simple and intuitive, offering an enjoyable playing experience.

#### Main features

##### 1. Graphic display
- Use of the Pygame library to manage 2D graphics.
- Displays the playing field, basket, basketball and background scenery.

##### 2. User controls
- Use mouse to adjust direction and power of throw.
- Left-click to throw the ball.

##### 3. Ball trajectory
- Calculate ball trajectory according to direction and power of throw.
- Use projectile physics concepts to simulate ball movement.

##### 4. Collision detection
- Detect collisions between the ball and the basket to determine whether the shot is successful.
- Use collision between simple shapes to simplify the detection process.

##### 5. Level management
- After each successful shot, the ball changes position relative to the basket, increasing the difficulty of the game.
- Increase distance or defense level to make subsequent shots more difficult.

##### 6. User interface
- Displays relevant information such as the current score and instructions on how to play.
- Display buttons to allow the player to restart or advance to the next level.

##### 7. Scoring system
- Keeps a tally of the number of successful baskets for each game session.
- On-screen display of the current score so players can track their progress.

#### Required modules
- Pygame: A Python library for creating 2D games.
- Math: To perform the mathematical calculations required to simulate the ball's trajectory.
- `Random`: To generate random positions for the ball during level changes.

#### Code structure
1. **Main.py**: Program entry point, containing the game's main loop and initializing the necessary elements.
2. **BasketballGame.py**: Main game class containing game logic and functionality.
3. **constants.py**: File containing constants such as screen size, colors, etc.
4. **assets/**: Directory containing images, sounds and other resources required by the game.
