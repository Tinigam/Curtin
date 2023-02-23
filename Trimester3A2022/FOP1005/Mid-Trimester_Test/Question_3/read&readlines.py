# read() is used to read the entire contents of a file as a single string. 
with open("/home/tinigam/FOP1005/Mid-Trimester_Test/linux_command.txt", "r") as f:
  contents = f.read()
  print(contents)
  print()
# readlines() is used to read the contents of a file line by line, and returns a list of strings where each element is a line from the file.
with open("/home/tinigam/FOP1005/Mid-Trimester_Test/linux_command.txt", "r") as f:
  lines = f.readlines()
  print(lines)