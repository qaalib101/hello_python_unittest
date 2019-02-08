import unittest
from phone_manager import Phone, Employee, PhoneAssignments, PhoneError

class TestPhoneManager(unittest.TestCase):

    def test_create_and_add_new_phone(self):

        testPhone1 = Phone(1, 'Apple', 'iPhone 6')
        testPhone2 = Phone(2, 'Apple', 'iPhone 5')

        testPhones = [ testPhone1, testPhone2 ]

        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_phone(testPhone1)
        testAssignmentMgr.add_phone(testPhone2)

        # assertCountEqual checks if two lists have the same items, in any order.
        # (Despite what the name implies)
        self.assertCountEqual(testPhones, testAssignmentMgr.phones)


    def test_create_and_add_phone_with_duplicate_id(self):
        # TODO add a phone, add another phone with the same id, and verify an PhoneError exception is thrown
        # TODO you'll need to modify PhoneAssignments.add_phone() to make this test pass
        testPhone1 = Phone(1, 'Apple', 'iPhone 6')
        testPhone2 = Phone(1, 'Apple', 'iPhone 5')

        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_phone(testPhone1)

        with self.assertRaises(PhoneError):
            testAssignmentMgr.add_phone(testPhone2)


    def test_create_and_add_new_employee(self):
        # TODO write this test and then remove the self.fail() statement
        # Add some employees and verify they are present in the PhoneAssignments.employees list
        employee1 = Employee(1, 'Qaalib')
        employee2 = Employee(2, 'Snoop Dog')

        testAssignmentmgr = PhoneAssignments()
        testAssignmentmgr.add_employee(employee1)
        testAssignmentmgr.add_employee(employee2)
        self.assertIs(0, testAssignmentmgr.employees.index(employee1))
        self.assertIs(1, testAssignmentmgr.employees.index(employee2))



    def test_create_and_add_employee_with_duplicate_id(self):
        # TODO write this test and then remove the self.fail() statement
        # TODO you'll need to fix the add_employee method in PhoneAssignments to make this test PhoneAssignments
        # This method will be similar to test_create_and_add_phone_with_duplicate_id
        employee1 = Employee(1, 'Qaalib')
        employee2 = Employee(1, 'Keanu Reeves')
        testAssignmentMgr = PhoneAssignments()
        testAssignmentMgr.add_employee(employee1)
        with self.assertRaises(PhoneError):
            testAssignmentMgr.add_employee(employee2)


    def test_assign_phone_to_employee(self):
        # TODO write this test and remove the self.fail() statement
        # TODO you'll need to fix the assign method in PhoneAssignments
        testEmployee = Employee(1, 'Qaalib')
        testPhone = Phone(1, 'Apple', 'IPhone 10')
        testPhone2 = Phone(2, 'Apple', 'IPhone X')
        testManager = PhoneAssignments()
        testManager.add_phone(testPhone2)
        testManager.add_phone(testPhone)
        testManager.add_employee(testEmployee)
        self.assertEqual(testPhone, testManager.assign(testPhone.id, testEmployee))




    def test_assign_phone_that_has_already_been_assigned_to_employee(self):
        # If a phone is already assigned to an employee, it is an error to assign it to a different employee. A PhoneError should be raised.
        # TODO write this test and remove the self.fail() statement
        # TODO you'll need to fix the assign method in PhoneAssignments so it throws an exception if the phone is alreaady assigned.

        testEmployee = Employee(1, 'Qaalib')
        testEmployee2 = Employee(2, 'Snoopy')
        testPhone = Phone(1, 'Apple', 'IPhone 10')
        testManager = PhoneAssignments()
        testManager.add_phone(testPhone)
        testManager.add_employee(testEmployee)
        testManager.add_employee(testEmployee2)
        testManager.assign(testPhone.id, testEmployee)
        with self.assertRaises(Exception):
            testManager.assign(testPhone.id, testEmployee2)


    def test_assign_phone_to_employee_who_already_has_a_phone(self):
        # TODO write this test and remove the self.fail() statement
        # TODO you'll need to fix the assign method in PhoneAssignments so it raises a PhoneError if the phone is alreaady assigned.

        testEmployee = Employee(1, 'Qaalib')
        testPhone = Phone(1, 'Apple', 'IPhone 10')
        testPhone2 = Phone(2, 'Apple', 'IPhone X')
        testManager = PhoneAssignments()
        testManager.add_phone(testPhone)
        testManager.add_phone(testPhone2)
        testManager.add_employee(testEmployee)
        testManager.assign(testPhone.id, testEmployee)
        with self.assertRaises(Exception):
            testManager.assign(testPhone2.id, testEmployee)


    def test_assign_phone_to_the_employee_who_already_has_this_phone(self):
        # TODO The method should not make any changes but NOT raise a PhoneError if a phone
        # is assigned to the same user it is currenly assigned to.
        testEmployee = Employee(1, 'Qaalib')
        testPhone = Phone(1, 'Apple', 'IPhone 10')
        testManager = PhoneAssignments()
        testManager.add_phone(testPhone)
        testManager.add_employee(testEmployee)
        self.assertEqual(testPhone, testManager.assign(testPhone.id, testEmployee))


    def test_un_assign_phone(self):
        # TODO write this test and remove the self.fail() statement
        # Assign a phone, unasign the phone, verify the employee_id is None
        testEmployee = Employee(1, 'Qaalib')
        testPhone = Phone(1, 'Apple', 'IPhone 10')
        testManager = PhoneAssignments()
        testManager.add_phone(testPhone)
        testManager.add_employee(testEmployee)
        testManager.assign(testPhone.id, testEmployee)
        testManager.un_assign(testPhone.id)
        self.assertIsNone(testPhone.employee_id)


    def test_get_phone_info_for_employee(self):
        # TODO write this test and remove the self.fail() statement
        # Create some phones, and employees, assign a phone,
        # call phone_info and verify correct phone info is returned

        # TODO check that the method returns None if the employee does not have a phone
        # TODO check that the method raises an PhoneError if the employee does not exist
        testEmployee = Employee(1, 'Qaalib')
        testEmployee2 = Employee(2, 'Snoopy')
        testPhone = Phone(1, 'Apple', 'IPhone 10')
        testPhone2 = Phone(2, 'Apple', 'IPhone X')
        testManager = PhoneAssignments()
        testManager.add_employee(testEmployee)
        testManager.add_phone(testPhone2)
        testManager.add_phone(testPhone)

        self.assertIsNone(testManager.phone_info(testEmployee))

        with self.assertRaises(PhoneError):
            testManager.phone_info(testEmployee2)
