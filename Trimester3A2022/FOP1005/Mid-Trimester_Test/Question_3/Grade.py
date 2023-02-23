def Grade(name, Marks):
  name = name.upper()
  if int(Marks) < 50:
    grade = "F"
  else:
    grade = "P"

  return f"{name}: {grade}"