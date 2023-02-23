#ifndef LIST_H
#define LIST_H

//a struct for storing a car
typedef struct Car
{
    int numberOfWheels;
    char name[64];
    double topSpeed;
}car_t;

//a struct for each node of a linked list
//to make it generic, change car_t to void*
typedef struct ListNode
{
    car_t value;
    struct ListNode* next;
}list_node_t;

//a struct for the linked list itself that keeps track of the 
//first car node (head), last car node(tail) and count
typedef struct List
{
    list_node_t* head;
    list_node_t* tail;
    int size;
}list_t;


list_t* createList();
void printList(list_t* list);
void addToList(list_t* list, car_t car);
void freeList(list_t* list);

#endif
