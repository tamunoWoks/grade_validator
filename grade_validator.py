def valid(name, grade):
    """Prints the validated student name and grade."""
    print(f'Hello {name}, your score is {grade}')

def main():
    try:
        # Get user input
        name = input('Enter student name >: ')
        grade = int(input('Enter grade (0-100) >: '))

        # Validate name (cannot be empty or just spaces)
        if not name.strip():
            raise Exception('Name cannot be empty.')
        
        # Validate grade range
        if grade < 0 or grade > 100:
            raise Exception('Grade must be between 0 and 100.')
        
        # Assertion: ensure grade is an integer
        assert isinstance(grade, int), "Grade must be an integer!"

        # If all validations pass, call valid()
        valid(name, grade)
        
    except Exception as err:
        # Catch any exception and print a clean error message
        print(f"Error: {err}")

if __name__ == '__main__':
    main()
