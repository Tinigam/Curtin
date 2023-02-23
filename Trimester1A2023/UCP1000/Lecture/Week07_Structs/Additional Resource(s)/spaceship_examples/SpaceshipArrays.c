#include "Spaceship.h"
#include <string.h>
#include <stdio.h>
#include <stdlib.h>

void printSpaceShip(const spaceship_t* ship)
{
	printf("The spaceship is the %s and can do the kessel run in %f parsecs\n",
											ship->name,
											ship->velocity);
}

spaceship_t* readSpaceShip()
{
	spaceship_t* ship = (spaceship_t*)malloc(sizeof(spaceship_t));
	printf("Please enter a ship name\n");
	fgets(ship->name, 256, stdin);
	ship->name[strlen(ship->name)-1] = '\0';
	printf("Please enter a ship velocity\n");
	char number[10];
	fgets(number, 10, stdin);
	ship->velocity = atof(number);
	
	return ship;
}

int main(int argc, char* argv[])
{
	//create a shipyard of 5 spaceships
	spaceship_t* shipyard[5];
	
	//add two spaceships
	shipyard[0] = (spaceship_t*)malloc(sizeof(spaceship_t));
	strncpy(shipyard[0]->name, "Milenium Eagle", 255);
	shipyard[0]->velocity = 300;
	
	shipyard[1] = (spaceship_t*)malloc(sizeof(spaceship_t));
	strncpy(shipyard[1]->name, "Enterprise", 255);
	shipyard[1]->velocity = 1000;
	
	//read the next 3 ships from the keyboard
	int i;
	for(i = 2; i < 5; i++)
	{
		shipyard[i] = readSpaceShip();
	}
	
	//print them on the screen
	for(i = 0; i < 5; i++)
	{
		printSpaceShip(shipyard[i]);
	}
	
	for(i = 0; i < 5; i++)
	{
		free(shipyard[i]);
	}
	return 0;
}

