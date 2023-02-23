CC=gcc
CFLAGS=-Wall
OBJ=main.o hello.o numbers.o
EXEC=program

program: $(OBJ)
	$(CC) $(OBJ) -o $(EXEC)

main.o: main.c hello.h numbers.h
	$(CC) $(CFLAGS) main.c -c

hello.o: hello.c
	$(CC) $(CFLAGS) hello.c -c

numbers.o: numbers.c
	$(CC) $(CFLAGS) numbers.c -c

clean:
	rm -f $(OBJ) $(EXEC)
