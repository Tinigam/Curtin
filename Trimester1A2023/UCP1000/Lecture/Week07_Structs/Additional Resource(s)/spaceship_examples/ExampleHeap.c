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

int main(int argc, char* argv[])
{
	//create two spaceships
	spaceship_t* milleniumEagle = (spaceship_t*)malloc(sizeof(spaceship_t));
	strncpy(milleniumEagle->name, "Milenium Eagle", 255);
	milleniumEagle->velocity = 300;
	
	spaceship_t* enterprise = (spaceship_t*)malloc(sizeof(spaceship_t));;
	strncpy(enterprise->name, "Enterprise", 255);
	enterprise->velocity = 1000;
	
	//print them on the screen
	printSpaceShip(milleniumEagle);
	printSpaceShip(enterprise);
	free(enterprise);
	
	//change the velocity and then print it again
	milleniumEagle->velocity = -10000;
	printSpaceShip(milleniumEagle);
	free(milleniemEagle);
	return 0;
}

