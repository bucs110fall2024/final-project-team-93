
:warning: Everything between << >> needs to be replaced (remove << >> after replacing)

# << Project Title >>
## CS110 Final Project  << Semester, Year >>

## Team Members

<< List team member names >>

***

## Project Description

<< Give an overview of your project >>

***    

## GUI Design

### Initial Design

![initial gui](assets/gui.jpg)

### Final Design

![final gui](assets/finalgui.jpg)

## Program Design

### Features

1. << Feature 1 >>
2. << Feature 2 >>
3. << Feature 3 >>
4. << Feature 4 >>
5. << Feature 5 >>

### Classes

- Player: The character the person playing the game will control. Has 3 attacks (slash, overhead, stab) to use to counter an enemy attack. 
- Knight: An enemy the player will have to face, has the ability to throw all different attack types and feint but throws slashes more often. The knight has a higher liklihood of countering the players counter. 
- Brute: An enemy the player will have to face, has the ability to throw all different attack types and feint but throws overheads more often. His counter window is longer however he is more prone to throwing feints. This enemy has a normal liklihood of countering the players counter. 
- Assassin: An enemy the player will have to face, has the ablity to throw all different attack types and feint but throws stabs more often. His counter window is shorter, but rarely feints. This enemy has a normal liklihood of countering the players counter
- King: The last enemy the player will have to face. This enemy is a mix of all the enemies above, and will take the characteristsics of one random enemy during each attack phase. For example, the king may attack the player as a Knight, where the counter window is normal and a normal liklihood of feinting. After the attack phase once both characters are done countering, will randomly switch to behave as a different class or the same class.  

## ATP

| Step                 |Procedure             |Expected Results                   |
|----------------------|:--------------------:|----------------------------------:|
|  1                   | Run Counter Program  |GUI window appears with count = 0  |
|  2                   | click count button   | display changes to count = 1      |
etc...
