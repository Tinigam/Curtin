from people import *
print('#### People Test Program ###')
testAdd = Address('10', 'Downing St', 'Carlisle', '6101')
testPerson = Person('Winston Churchill', '30/11/1874', testAdd)
testPerson.displayPerson()
print()

testAdd2 = Address('1', 'Infinite Loop', 'Hillarys', '6025')
testPerson2 = Staff('Professor Awesome', '1/6/61', testAdd2, '12345J')
testPerson2.displayPerson()
print()

testAdd3 = Address("3", "Student road", "student camp", "3333")
student = Student("Peter", "1/2/2000", testAdd3, "333")
student.displayPerson()
print()

testAdd4 = Address("4", "Post Grad road", "Post Grad camp", "4444")
postGrad = Postgrad("John", "1/2/1999", testAdd4, "444")
postGrad.displayPerson()
print()

testAdd5 = Address("5", "Under Grad road", "Under Grad camp", "5555")
underGrad = Undergrad("Bob", "1/2/2011", testAdd5, "555")
underGrad.displayPerson()
print()