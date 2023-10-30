""" Regular Expression in Python """

import re
if re.search("Elon Musk", "Elon Musk is the owner of Tesla, Starlink and Twitter"):
    print("Elon musk was found")

Owners = re.findall("Elon Musk", "Elon Musk is the owner of Tesla, Starlink and Twitter - Elon Musk" )
for x in Owners:
    print(x)


##############################
Animal_str = "Cat pat rat bat"
all_animal = re.findall("[cprb]at", Animal_str)
for x in all_animal:
    print(x)

some_animal = re.findall("[^Cb]at", Animal_str)
for x in some_animal:
    print(x)


random_str = "get some of the \\stuff"
print("find the \\stuff : ", re.search("\\stuff", random_str))

another_str = "F.B.I C.I.A C.I.D"
print("Matches : ", len(re.findall(".\..\..\.", another_str)))

integer_str = "12345"
print("Matches : ", len(re.findall("\d", integer_str)))

another_int = "1234 12345 123456 1234567"
print("Matches : ", len(re.findall("\d{5,7}", another_int)))

# Example 1 "Creating a matching email lists"
email_list = "db@hh.com me@.com @apple.com db@.com"
print("Email matches : ", len(re.findall("[\w._%+-]{1,20}@[-w.-]{2,20}.[A-Za-z]{2,3}", email_list)))