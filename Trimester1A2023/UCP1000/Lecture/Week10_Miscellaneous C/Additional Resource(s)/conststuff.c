#include <stdio.h>



void printName(const char* name);


int main()
{
	char name[10] = "Rob";

	printName(name);
	printName(name);

	return 0;
}


void printName(const char* name)
{
	printf("the name is %s\n", name);

}
