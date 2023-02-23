#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main()
{
	//seed the rng ONCE ONLY at the start of the program
	srand(time(NULL));

	//pick a random number from 5 to 14 (Range of 10 numbers starting at 5)
	int x = rand() % 10 + 5;
	//pick a different random number that could be anything
	int y = rand();

	printf("%d is a random number! :)\n", x);
	printf("%d is a random number! :)\n", y);

	//decision making based on randomness
	if(x == 10)
	{
		printf("The first random number was exactly 10!\n");
	}
	else if (x<10)
	{
		printf("The first random number was less than 10\n");
	}
	else
	{
		printf("The first random number was more than 10\n");
	}
	

	return 0;
}
