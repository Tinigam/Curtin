//include anything you need
#include <stdio.h>

//declare any functions
int getInput();

//main
int main()
{
	printf("Hi There!\n");
	printf("programming is pretty fun\n");
	int numberOne;
	int numberTwo;
	numberOne = getInput();
	numberTwo = getInput();
	int answer = numberOne * numberTwo;
	
	printf("the answer is: %d\n", answer);
		
	printf("when it works... :)\n");
	return 0;
}

//functions
int getInput()
{
	int input;
	printf("Please enter a number: ");
	scanf("%d", &input);
	return input; 
}

