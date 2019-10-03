# Solitaire
Solitaire Simulator for KP Engineering Application

Download the code and run python solitaire.py to play!

To briefly explain my design choices, I decided to create a Card Object and a Pile object to more easily simulate the behavior of adding and removing cards, rather than using lists to represent each of the different piles. Creating these objects makes it easier to simulate the difference ways you can interact with a pile. My game does not test for user error, in the sense that the user can play the game with disregard for the actual rules of solitare- they can put whatever cards they want on top of one another in whichever order they want. I decided to do this in order to give players more fun- if they want to play solitaire according to the rules then they can, but they can also mess around with the game however they choose.

I decided to use python for a couple of reasons. First, I hadn't coded a real project in python in a while, so I wanted to practice with the language. Python is also my preferred language when dealing with lists, and since I knew Solitaire contained multiple lists I thought it would be the easiest language for the project.


