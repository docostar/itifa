import random

def get_marks_based_on_grade(grade):
    # Define grade-to-range mapping
    grade_ranges = {
        'A': (81, 90),
        'B': (76, 80),
        'C': (71, 75),
        'D': (65, 69),
        'E': (61, 65),
    }
    
    # Check if the grade is valid
    if grade not in grade_ranges:
        raise ValueError("Invalid grade. Valid grades are: A, B, C, D, E.")
    
    # Get the range for the given grade
    low, high = grade_ranges[grade]
    
    # Generate random marks within the range
    marks = random.randint(low, high)
    return marks

