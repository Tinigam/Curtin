CC=gcc
CFLAGS=-Wall
OBJ=powers.o bounds.o
EXEC=program

program: $(OBJ)
	$(CC) $(OBJ) -o $(EXEC)

bounds.o: bounds.c powers.h
	$(CC) $(CFLAGS) bounds.c -c

powers.o: powers.c
	$(CC) $(CFLAGS) powers.c -c

clean:
	rm -f $(OBJ) $(EXEC)