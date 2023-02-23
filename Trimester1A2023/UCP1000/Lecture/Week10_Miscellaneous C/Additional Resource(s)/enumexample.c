#include <stdio.h>

typedef enum
{
	NEW_GAME = 1, LOAD_GAME = 2, SETTINGS = 3
} menu_option_t;



int main()
{
	printf("this is a menu\n");
	printf("1. new game\n");
	printf("2. load game\n");
	printf("3. settings\n");	
	
	int choice;
	
	scanf("%d", &choice);
	
	
	switch((menu_option_t)choice)
	{
		case NEW_GAME:
			printf ("this is a new game\n");
			break;
		case LOAD_GAME:
			printf("loading a game\n");
			break;
		case SETTINGS: 
			printf("settings\n");
			break;
		default:
			printf("Unknown Option.\n");
	}
	
	return 0;
}
