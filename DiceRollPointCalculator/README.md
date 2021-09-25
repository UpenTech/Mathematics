# 2D Dice Grid Scoring Calculator

This is a simple dice rolling game (whatsoever you bascially can call it a point calculator).

## What does it do? 

A set of dices consisting of **4 dices** are rolled **4 times** i.e. alltogether 16 dices are rolled. 
The outcome of dices are then represented by **4x4 matrix** were each row denotes a set.
Points are then calculated based on the outcomes.

## Representation in 4*4 Matrix

| Dice Outcome | Dice Outcome | Dice Outcome | Dice Outcome |
|------------------|------------------|------------------|------------------|
| 1st Dice Outcome | 2nd Dice Outcome | 3rd Dice Outcome | 4th Dice Outcome |
| 5th Dice Outcome | 6th Dice Outcome | 7th Dice Outcome | 8th Dice Outcome |
| 9th Dice Outcome | 10th Dice Outcome | 11th Dice Outcome | 12th Dice Outcome |
| 13th Dice Outcome | 14th Dice Outcome | 15th Dice Outcome | 16th Dice Outcome |

## **Rules for points calculation**
------------------------------------
 
*	If all four corner's outcome are either all even or all odd, 20 points are added.
*	If a row's outcome are either all even or all odd, 20 points are added.
*	If a column's outcome are either all even or  all odd, 20 points are added.
*	If a diagonal's outcome are either all even or  all odd, 20 points are added.

## An Example

Following are the outcomes of rolling, represnted by 4x4 matrix

|Outcomes|Outcomes|Outcomes|Outcomes|
|:------:|:------:|:------:|:------:|
|6|2|3|1|
|2|6|5|1|
|2|3|4|6|
|4|4|5|6|

	Here, 1st Column's Dices outcome are all even and so are one of the diagonal's.
	Ergo, our points will be 40.

_______________

I'm trying to keep my hands dirty with `python` and this is another one of my creepy program.
The code is open to any amemdment ( though I hardly dought someone is going to).
So, yea I would love to implement additional features if someone has some good ideas.
 
