#HW: 1. Encapsulation in Personal Budget Management
'''
Problem Statement: You are required to build a Personal Budget Management application. The application 
will manage budget categories like food, entertainment, utilities, etc., ensuring that budget details 
remain private and are accessed or modified through public methods.


Task 1: Define Budget Category Class
-Create a class BudgetCategory with private attributes for category name and allocated budget.
-Initialize these attributes in the constructor.
-Expected Outcome: A BudgetCategory class capable of storing category details securely.

Task 2: Implement Getters and Setters
-Write getter and setter methods for both the category name and the allocated budget.
-Ensure that the setter methods include validation (e.g., budget should be a positive number).
-Expected Outcome: Methods that allow controlled access and modification of the private attributes, with validation checks in place.

Task 3: Add Budget Functionality
-Implement a method to add expenses to a category and adjust the budget accordingly.
-Validate the expense amount before making deductions from the budget.
-Expected Outcome: Ability to track expenses per category and update the remaining budget safely.

Task 4: Display Budget Details
-Create a method to display the details of a budget category, including the name, allocated budget, and remaining budget after expenses.
-Expected Outcome: Users can view a summary of each budget category, showcasing encapsulation in action.
'''

class BudgetCategory:
    def __init__(self, category_name, allocated_budget):
        self.__category_name = category_name
        self.__allocated_budget = allocated_budget

    def get_category_name(self):
        return self.__category_name
    
    def get_allocated_budget(self):
        return self.__allocated_budget
    
    def set_category_name(self, new_cat_name):
        self.__category_name = new_cat_name
    
    def set_allocated_budget(self, budget):
        if isinstance(budget, int):
            self.__allocated_budget = budget
            print(f"You're budget is {budget}!")
        else:
            print("Invalid budget amount.")

    def add_expense(self, amount):
        if amount > 0:
            self.set_allocated_budget(self.get_allocated_budget() - amount)
            print(f"You have expensed ${amount}!")
        else:
            print("Invalid expenes amount.")

    def display_category_summary(self):
        # Method to display the budget category details
        # ...
        print(f"Category Name: {self.__category_name}")
        print(f"Allocated Budget: {self.__allocated_budget}")

food_category = BudgetCategory("Food", 500)
food_category.add_expense(100)
food_category.display_category_summary()
