from professor import *

def testConstructor():
    p1 = Professor()
    print(f"Testing constructor with default values.  Expect default values. {p1}")
    p2 = Professor('123456789', 'Brendan', 'Blandy', 'CS')
    print(f"Testing constructor with parameters.  Expect professor Brendan. {p2}")


def testPropertyGetters():
    p = Professor('123456789', 'Brendan', 'Blandy', 'CS')
    print(f"Testing property getters.  Expect individual attributes for professor p.")
    print(f"email: {p.lnumber}, FIRST: {p.firstName}, LAST: {p.lastName}, DEPT: {p.department}")

def testPropertySetters():
    p = Professor('123456789', 'John', 'Smith', 'CS')
    p.lnumber = '987654321'
    p.firstName = 'Brendan'
    p.lastName = 'Blandy'
    p.department = 'PHIL'
    print(f"Testing property setters.  Expect individual attributes for professor to change to Brendan. {p}")

def testPropertySettersWithValidation():
    p = Professor('123456789', 'Brendan', 'Blandy', 'CS')
    try:
        p.lnumber = '12345'
    except ValueError as vErr:
        print("An exception was thrown, less than nine")
        print(vErr)
    try:
        p.firstName = 102
    except ValueError as vErr:
        print("An exception was thrown setting First Name to an int")
        print(vErr)
    try:
        p.lastName = 100
    except ValueError as vErr:
        print ("An exception was thrown setting Last Name to an int")
        print(vErr)
    try:
        p.department = 100
    except ValueError as vErr:
        print ("An exception was thrown setting Last Name to an int")
        print(vErr)

def testEncapsulation():
    p = Professor('123456789', 'Brendan', 'Blandy', 'CS')
    try:
        print(p.lnumber)
        p.lnumber = '987654321'
        print(p.lnumber)
        print (p.__lnumber)
        p.__lnumber = '987654321'
        print (p.__lnumber)
    except AttributeError as attErr:
        print("An attribute error was throws in test Encapsulation")
        print(attErr)

    try:
        print(p.firstName)
        p.firstName = 'Brendan'
        print(p.firstName)
        print (p.__firstName)
        p.__firstName = 'Brendan'
        print (p.__firstName)
    except AttributeError as attErr:
        print("An attribute error was throws in test Encapsulation")
        print(attErr)

    try:
        print(p.lastName)
        p.lastName = 'Blandy'
        print(p.lastName)
        print (p.__lastName)
        p.__firstName = 'Blandy'
        print (p.__lastName)
    except AttributeError as attErr:
        print("An attribute error was throws in test Encapsulation")
        print(attErr)

    try:
        print(p.department)
        p.department = 'CS'
        print(p.department)
        print (p.__department)
        p.__firstName = 'CS'
        print (p.__department)
    except AttributeError as attErr:
        print("An attribute error was throws in test Encapsulation")
        print(attErr)