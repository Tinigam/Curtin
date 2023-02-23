typedef struct SpaceShip
{
	char name[256];
	double velocity;
} spaceship_t;

typedef struct SpaceShipNode
{
	spaceship_t* data;
	struct SpaceShipNode* next;
}spaceship_node_t;

typedef struct SpaceShipList
{
	spaceship_node_t* head;
}spaceship_list_t;


spaceship_list_t* createList();
void insertToList(spaceship_list_t*, spaceship_t* newShip);
