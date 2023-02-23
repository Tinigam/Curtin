#include "SpaceshipTypdef.h"
#include <string.h>
#include <stdio.h>

int main(int argc, char* argv[])
{
	spaceship_t milleniumEagle = {"Milenium Eagle", 300};
	spaceship_t enterprise;
	
	strncpy(enterprise.name, "Enterprise", 255);
	enterprise.velocity = 1000;
	
	printf("My spaceship is the %s and can do the kessel run in %f parsecs\n",
											milleniumEagle.name,
											milleniumEagle.velocity);
											
	printf("The %s can do the kessel run in %f parsecs\n",
											enterprise.name,
											enterprise.velocity);
	milleniumEagle.velocity = -10000;
	
	printf("now the velocity is %f\n", milleniumEagle.velocity);
	
	return 0;
}

