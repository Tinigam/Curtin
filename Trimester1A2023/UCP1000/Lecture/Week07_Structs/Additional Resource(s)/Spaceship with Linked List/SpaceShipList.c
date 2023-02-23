#include "SpaceshipList.h"
#include <stdlib.h>

spaceship_list_t* createList()
{
	spaceship_list_t* newList = calloc(1, sizeof(spaceship_list_t));
	
	return newList;
}

void insertToList(spaceship_list_t* list, spaceship_t* newShip)
{
	spaceship_node_t* newNode = calloc(1, sizeof(spaceship_node_t));
	newNode->next = list->head;
	list->head = newNode;
	newNode->data = newShip;
}
