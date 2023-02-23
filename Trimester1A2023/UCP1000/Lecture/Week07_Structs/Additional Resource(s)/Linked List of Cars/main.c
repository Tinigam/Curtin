#include <stdio.h>
#include <string.h>
#include "list.h"

//this factory function makes a new car by reading the data from stdin
car_t makeCar()
{
    car_t newCar;
    printf("Please type the number of wheels\n");
    scanf("%d", &newCar.numberOfWheels);
    getchar();
    printf("Please type the name of the car\n");
    //could use scanf here but fgets will get the whole line
    //scanf("%63s", newCar.name); 
    fgets(newCar.name, 64, stdin);
    //chomp the <enter> key off the end of the user input
    int size = strlen(newCar.name);
    newCar.name[size-1] = '\0';
    printf("Please type the top speed\n");
    scanf("%lf", &newCar.topSpeed);
    getchar();

    return newCar;
}



int main( int argc, char **argv )
{
    //to make a single car, you can use array style initializer syntax
    //car_t mazda = { 4, "Rx7", 200.0 };
    
    
    int userChoice;
    //make a list
    list_t* list = createList();

    //dispay a menu
    do
    {
        printf("1. Create a car\n");
        printf("2. Exit\n");
        scanf("%d", &userChoice);
        if(userChoice == 1)
        {
            //call makeCar() and add the new car to the list
            addToList(list, makeCar());
        }
        //until the user quits
    } while(userChoice != 2);


    //print all the cars in the list
    printList(list);

    //free all the calloced memory
    freeList(list);

    return 0;
}
