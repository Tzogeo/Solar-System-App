# Solar-System

Welcome to Solar-System, a Python program built using Pygame that offers a range of interactive features related to the celestial bodies within our solar system. Some examples are: a simulation of the movement of the planets in scale, information about the planets, an eazy and a not so easy quiz about them and a free-fall simulation on the planets

## Essential libraries:
pygame
sys (pre-installed with python)
random (pre-installed with python)
webbrowser (pre-installed with python)
math (pre-installed with python)
datetime (pre-installed with python)

## How to install the project:

Ensure you have Python installed on your system.
Install Pygame library by using pip install pygame(in Windows).
Clone this repository to your local machine.
Navigate to the directory where the program is saved.
Run the solar_system.py file using Python.

## How to use the project:
From the main menu by prssing the appropriate button the user access the features below:
* Key 1: shows information about the planet
* Key 2: shows a free fall simulation
* Key 3: shows the planets(and their movement) in scale
* Key 4: focuses on the inner planets and shows them in scale
* Key 5: opens a quiz on the planets
* Key 6: opens another quiz with more difficult questions

Specifically the user in each feature will do this:
1: The user will see  images of the 8 planets with their name and a bit of information about them. By pressing the name of a specific planet the user will be able to see more information about this planet. By clicking an image of a planet the wikipedia page of that planet will be opened on the default browser
2: The user will see the planets and a spaceship on each. By pressing the space bar the user will start or pause the simulation. By starting it, the spaceships will "fall" next to each other accordingly to the gravitational pull of their respective planets. By pressing the key "r" the spaceships will reset to their initial position.
3: The user will see the solar system with the distances between each planet in scale. In the beginning the planets will be placed in the position they are the day the program runs. By pressing the space bar the planets will begin to move (pr stop if they are already moving). The time will change accordingly. By pressing the key "n" the user will be able to give as input a certain date(in the dd/mm/yyyy format) and the simulation will show the position of the planets on that day. By pressing the key "r" their position will reset in the current day. By clicking with the mouse in the area near the inner planets the user will be transported in the inner planets.(See 4 for more information)
4: The user will have the same features as 3 but the model will focus on the inner planets(Mercury,Venus,Earth and Mars). This will give the user the ability to better observe their movement, which is very fast and small in the other model.
5: The user will be able to take a quiz to test their knowledge on the planets. In the top there will be questions which will have a planet for an answer and the user will have to click on the image of the right planet.
6: This will also open a quiz. This quiz will have more difficult questions and the user will be able to make three mistakes before losing.

The user will be able to return to the previous screen by pressing the escape button and leave the game by clicking x on the top right side of the window.

## Credits:
This program is developed using Pygame, an open-source library for making multimedia applications. Special thanks to the contributors of Pygame for their dedication to the project. 
The information on the program and most of the images were taken from Wikipedia and Nasa. Special thanks to all the people behind the two organisations.

## Contribution:
Contributions to this project are welcome! Feel free to submit bug reports, feature requests, or even pull requests to help improve Solar-System for everyone.

## License:
This project is licensed under the MIT License - see the LICENSE file for details.

## Future updates:
In the simulation of the movement of the planets the user will be able to see some missions of space exploration that happen(happened or will happen) near the time that appears.

## Feedback:
If you have any feedback, suggestions, or issues, please don't hesitate to reach out. Your input is invaluable in enhancing the user experience of Solar-System.

Thank you for using the app! Happy exploring the wonders of our solar system! 🌌🪐
