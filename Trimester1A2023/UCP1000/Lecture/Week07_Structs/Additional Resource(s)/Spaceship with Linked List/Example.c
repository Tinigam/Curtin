#include "SpaceshipList.h"
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
	//create a list of spaceships
	spaceship_list_t* shipyard = createList();
	
	//read the spaceships from the keyboard
	char exit[64];
	do
	{
		insertToList(shipyard, readSpaceShip());
		
		printf("Do you want to create another ship?\n");
		fgets(exit, 256, stdin);
	}while(strcmp(exit, "yes\n") == 0);
	
	
	//print them on the screen
	spaceship_node_t* current = shipyard->head;
	while(current != NULL)
	{
		printSpaceShip(current->data);
		current = current->next;
	}
	
	//free the spaceships
	current = shipyard->head;
	while(current != NULL)
	{
		//store the next node so that we don't lose it
		//when the current is freed
		spaceship_node_t* next = current->next;
		//free the spaceship
		free(current->data);
		//free the node
		free(current);
		//move to the next node
		current = next;
	}
	//free the list itself
	free(shipyard);
	
	return 0;
}

