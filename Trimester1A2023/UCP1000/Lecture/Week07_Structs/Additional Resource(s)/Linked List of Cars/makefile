CC=gcc
CFLAGS=-Wall
OBJ=main.o list.o
EXEC=ListProgram

$(EXEC): $(OBJ)
	$(CC) $(OBJ) -o $(EXEC)

main.o: list.h main.c
	$(CC) $(CFLAGS) -c main.c


list.o: list.h list.c
	$(CC) $(CFLAGS) -c list.c

clean:
	rm -f $(EXEC) $(OBJ)
