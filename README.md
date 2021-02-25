# Attack on Typing!


## Group Members Bio's:

- [Anthony Beaver](https://github.com/PyDrummer)
    - Anthony Beaver is a full stack software developer from Seattle Washington. Passionate about problem solving and playing the drums! Looking to change the world one syntax error at a time.
- [Logan Jones](https://github.com/okayjones)
    - Logan Jones is a former product manager and current software engineer. She is a skilled problem solver who loves cats, taco bell, and world of warcraft.
- [Nick Dorkins](https://github.com/NickDorkins)
    - Software Developer with a background in Specialized Industrial Safety, and fabrication. Enjoy's traveling and spending time with family and puppies. Favorite things to do outside quarantine are going to Disney parks and playing Magic the Gathering.
- [Nebiyu Kifle ](https://github.com/neba9)
    - I am a professional and highly motivated software engineer. I have a background in marketing and logistics management for about 6 years back home in Ethiopia. I used to also have my own business. I have worked on multiple projects and have a broad experience in software development at Code Fellows. I am passionate to learn new things in the tech industry. I would love the opportunity to put my experience at tech company I am currently looking for a new role that will utilize my skills and experience and take my career to the next level.

---

## Summary of Ideas:

**Have you or a loved one ever wanted to type a bit faster? Not sure how to level up your typing skills? You should try Attack on Typing! Our app provides an easy to use interface, and challenges that progressively get harder as you play. This educational app will make you a faster typer, and it’s free!**

---

## How to get started:

- Clone [Attack on Typing](https://github.com/PySnooper/AttackOnTyping.git) repository to your local machine
    ```
    $ git clone https://github.com/PySnooper/AttackOnTyping.git
    ```

- In your CLI change directories into the AttackOnTyping directory
    ```
     $ cd AttackOnTyping
    ```
- Once inside run a "poetry install" to install dependencies 
    ```
    $ poetry install
    ```
- After dependencies install you are going to change to the attackontyping directory
     ```
     $ cd attackontyping
    ```
- Once inside the attackontyping directory you are going to start the application
    ```
    $ python attackontyping.py
    ```
- Once the application loads, follow the prompts on the screen and enjoy!



---

## User Stories

| User Story: | Developer Expectations: | Acceptance Tests: |
| --- | --- | --- |
| Have an easy to use menu to navigate the program.| Have a welcoming message and clear directions on how to navigate the menu before playing the game.| User has multiple options upon loading the program such as Play game, Rules, About us, Exit. |
| I want to see how quickly I typed my answer. | A timer feature to calculate how long it took for the user to enter their answer. | A class and time keeping functions built to accurately calculate time spent typing the user input. |
| I want to know how high I scored while playing the game. | Add score keeping functionality that displays the users score as they play. | Program keeps track of the user's score based on their typing performance. Shows the user how many points they got. |
| I want a different sentence to type out as my challenge. | Utilize Faker python library to import randomly generated sentences as the challenges. | Faker works and we parse the data, then present this as the sentence to have the user type out. |
| I want a challenge, give me a limited amount of tries before I "lose" the game and have to retry. | Add failure conditions and keep track of the amount of fails vs tries given to the user. | The user gets a limited amount of tries based on the amount of time they took to type the message. If they cant type it within the time the tries count goes down. After there are no more tries they get a "Game Over, Try Again" message. |

---

## Domain Modeling

[Attack On Typing - Domain Modeling](https://drive.google.com/file/d/1Vr_-2xkZiBMW9oE7Kbs9MtxRmSpgqeuR/view?usp=sharing
)

---

## Wireframe

[Attack On Typing - Wireframe](https://docs.google.com/document/d/1ffrMg_Xb_HBKk_IqghCmqEzixe2cI_Sh0IOmtYf2H_Q/edit?usp=sharing)

---

## Resources:

- [Faker Documentation](https://faker.readthedocs.io/en/master/)
- [StackOverflow: Write unit test for console print](https://stackoverflow.com/questions/33767627/python-write-unittest-for-console-print)
- [Colorama](https://pypi.org/project/colorama/)
- [Accessible Colors](https://accessible-colors.com/) (ADA Color Compliance)
- [Color Safe](http://colorsafe.co/) (ADA Color Compliance)
- [ASCII Art Archive](https://asciiart.website/index.php)
- [Print Colors in Python terminal - GeeksforGeeks](https://www.geeksforgeeks.org/print-colors-python-terminal/)
- [How to create a Countdown Timer using Python? - GeeksForGeeks](https://www.geeksforgeeks.org/how-to-create-a-countdown-timer-using-python/)
- [Pyfiglet: Github](https://github.com/pwaller/pyfiglet)
- [Pyfiglet Documentation](https://pypi.org/project/pyfiglet/0.7/)

