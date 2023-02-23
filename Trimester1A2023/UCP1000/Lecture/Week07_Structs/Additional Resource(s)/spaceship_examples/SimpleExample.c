#include "SimpleSpaceship.h"
#include <stdio.h>

int main(int argc, char* argv[])
{
	struct SpaceShip milleniumEagle = {"Milenium Eagle", 300};
	
	printf("My spaceship is the %s and can do the kessel run in %f parsecs\n",
											milleniumEagle.name,
											milleniumEagle.velocity);
											
	milleniumEagle.velocity = -10000;
	
	printf("now the velocity is %f\n", milleniumEagle.velocity);
	
	return 0;
}

