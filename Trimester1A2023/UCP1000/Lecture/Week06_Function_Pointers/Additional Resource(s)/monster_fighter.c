#include <stdio.h>

//define a data type called "Attack" that stores a function
typedef void (*Attack) (void);

//Function declarations
void FightMonster(Attack attackFunction);
void AttackWithSword();
void AttackWithMagic();

//main function for fighting monsters
int main()
{
	//fight the monster and give it the AttackWithSword callback function
	FightMonster(&AttackWithSword);
	//fight the monster and give it the AttackWithMagic callback function
	FightMonster(&AttackWithMagic);
	//fight the monster and give it the AttackWithSword callback function
	FightMonster(&AttackWithSword);
	
	return 0;
}

//function for fighting a monster takes an "Attack" variable as an argument
//The attack variable contains a callback function to decide how to attack
void FightMonster(Attack attackFunction)
{
	printf("fighting the monster\n");
	//run the callback
	attackFunction();
	printf("The monster is dead\n");
}

//callback function for attacking with a sword
void AttackWithSword()
{
	printf("the monster has been attacked with a sword!\n");
}

//callback function for attacking with magic
void AttackWithMagic()
{
	printf("the monster has been attacked with a fireball!\n");
}