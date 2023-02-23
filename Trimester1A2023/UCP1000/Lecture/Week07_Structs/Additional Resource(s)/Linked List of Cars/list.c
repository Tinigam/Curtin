#include "list.h"
#include <stdlib.h>
#include <stdio.h>

//This function makes a new linked list
list_t* createList()
{
    //calloc will allocate enough memory for the list
    //and set all data there to 0 (NULL)
    list_t* newList = (list_t*)calloc(1, sizeof(list_t));
    return newList;
}
    
//This function loops through the list of cars and prints each one
void printList(list_t* list)
{
    list_node_t* current;
    //start at the head, 
    //continue while not at the end of the list, 
    //go to the next node each loop
    for(current = list->head; current != NULL; current = current->next)
    { 
        printf("I drive a %s that goes at %fkmph\n", current->value.name, current->value.topSpeed);
    }
}

//take a list and add a car to the start of it
void addToList(list_t* list, car_t car)
{
    list_node_t* newNode = malloc(1*sizeof(list_node_t));
    newNode->value = car;
    newNode->next = list->head;
    list->head = newNode;
    //if the list is empty, the new node is both the head, and the tail
    if(list->size == 0)
    {
        list->tail = newNode;
    }
    list->size++;
}

//need to free everything that's been allocated
//That means loop through and free EVERY node.
void freeList(list_t* list)
{
    list_node_t* current, *next;
    while(current != NULL)
    {
        next = current->next;
        free(current);
        current = next;
    }
    free(list);
}



