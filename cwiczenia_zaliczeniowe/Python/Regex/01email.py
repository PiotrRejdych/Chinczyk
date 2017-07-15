'''
>>> check_email_edu()
True
>>> check_email_regular()
True
>>> check_email_negative()
False
'''

import re

def check_email_edu():
    email = "student.studencki@uj.edu.pl"
    pattern = "^[A-Za-z][A-Za-z0-9.\-_]*[A-Za-z0-9_\-]@([A-Za-z]+\.)*edu\.([A-Za-z]+\.)*[A-Za-z]+$"
    regexp = re.compile(pattern)
    return regexp.search(email) != None

def check_email_regular():
    email = "student1234@gmail.com"
    pattern = "^[A-Za-z0-9_\-][A-Za-z0-9_\-.]*[A-Za-z0-9_\-]@([A-Za-z]+\.)+[A-Za-z]+$"
    regexp = re.compile(pattern)
    return regexp.search(email) != None

def check_email_negative():
    email = "#-*&12@com"
    pattern = "^[A-Za-z0-9_\-][A-Za-z0-9_\-.]*[A-Za-z0-9_\-]@([A-Za-z]+\.)+[A-Za-z]+$"
    regexp = re.compile(pattern)
    return regexp.search(email) != None

if __name__ == '__main__':
    import doctest
    doctest.testmod()

print check_email_negative()