class Professor:

    def __init__(self, lnumber='123456789', firstName='firstTest', lastName='lastTest', department='dept'):
        self.__lnumber = lnumber
        self.__firstName = firstName
        self.__lastName = lastName
        self.__department = department

    @property
    def lnumber(self):
        return self.__lnumber

    @property
    def firstName(self):
        return self.__firstName

    @property
    def lastName(self):
        return self.__lastName
    
    @property
    def department(self):
        return self.__department

    @lnumber.setter
    def lnumber(self, lnumber):
        if isinstance(lnumber, str) and len(lnumber) == 9:
            self.__lnumber = lnumber
        else:
            raise ValueError(
                f"Must be nine digits. {type(lnumber)}  {lnumber}")

    @firstName.setter
    def firstName(self, firstName):
        if isinstance(firstName, str):
            self.__firstName = firstName
        else:
            raise ValueError(f"Must be a string {type(firstName)}  {firstName}")

    @lastName.setter
    def lastName(self, lastName):
        if isinstance(lastName, str):
            self.__lastName = lastName
        else:
            raise ValueError(f"Must be a string {type(lastName)}  {lastName}")

    @department.setter
    def department(self, department):
        if isinstance(department, str):
            self.__department = department
        else:
            raise ValueError(f"Must be a string {type(department)}  {department}")

    def __str__(self):
        return f'Professor(lnumber: {self.__lnumber}, FIRST: {self.__firstName}, LAST: {self.__lastName}, DEPT: {self.__department} )'
