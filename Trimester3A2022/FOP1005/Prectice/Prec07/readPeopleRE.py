import re
from people import *

# Lets create a pattern and extract some information with it
reg = re.compile(r'''(
                    (\d+[a-zA-Z]?) # (2) house number
                    (\s+)
                    (\w+\s\w+) # (4) street name and type
                    (,\s+)
                    (\w+) # (6) suburb
                    (,\s+)
                    (\d{4}) # (8) postcode
                    )''', re.VERBOSE)
try:
    with open('/home/tinigam/FOP1005/Prectice/Prec07/people.csv', 'r') as f:
        lines = f.readlines()

    person = []
    id_conter = 1

    for line in lines:
        splitline = line.strip().split(':')
        myclass = splitline[0]
        name = splitline[1]
        dob = splitline[2]
        inaddress = splitline[3]
        result = reg.match(inaddress) # returns the matching groups
        if result:
            num = result.group(2)
            street = result.group(4)
            suburb = result.group(6)
            postcode = result.group(8)
            print(myclass,'|',name,'|',dob,'|',num,'|',street, '|',suburb,'|',postcode)
            address = Address(num, street, suburb, postcode)
            if myclass == "Staff":
                record = Staff(name, dob, address, id_conter)
            elif myclass == "Undergrad":
                record = Undergrad(name, dob, address, id_conter)
            elif myclass == "Postgrad":
                record = Postgrad(name, dob, address, id_conter)
            id_conter += 1
            person.append(record)
        else:
            print('Address not matched: ', inaddress)

except OSError as err:
    print('Error with file open: ', err)
