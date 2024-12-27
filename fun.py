
from openpyxl.styles import Font, Fill, Border, Alignment, Protection, PatternFill
def get_practical_number(sheet_name,lo_no):
    min_row = 2
    max_row = sheet_name.max_row

    for temp in range(min_row, max_row + 1):
        if lo_no == sheet_name["A" + str(temp)].value:
            found_row = temp
            break

    start_practical = sheet_name["B" + str(found_row)].value
    end_practical = sheet_name["C" + str(found_row)].value
    return start_practical,end_practical



import random

def get_marks_based_on_grade(grade):
    # Define grade-to-range mapping
    grade_ranges = {
        'A': (85, 90),
        'B': (78, 84),
        'C': (71, 77),
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

def get_practical_wise_marks(avg_marks, num_practicals):
    if not (60 <= avg_marks <= 90):
        raise ValueError("Average marks must be between 60 and 90.")

    total_marks = avg_marks * num_practicals
    marks = []

    for _ in range(num_practicals):
        remaining_practicals = num_practicals - len(marks)
        if remaining_practicals > 1:
            if avg_marks>=67:
            # Randomly distribute marks close to the average, if avg marks >66
                mark = random.randint(max(60, avg_marks - 6), min(90, avg_marks + 6))
            else:
                mark = random.randint(max(60, avg_marks - 3), min(90, avg_marks + 3))
        else:
            # Ensure the last mark adjusts to meet the total
            mark = total_marks - sum(marks)
            mark = max(60, min(90, mark))
        marks.append(mark)
    
    return marks

sections_max_marks = [
    [2, 5, 8],  # Section 1
    [3, 2, 5],  # Section 2
    [3, 3, 4],  # Section 3
    [1, 2, 2],  # Section 4
    [4, 3, 3],  # Section 5
    [4, 3, 3],  # Section 6
    [3, 5, 2],  # Section 7
    [7, 3, 5],  # Section 8
    [7, 5, 3],  # Section 9
]



#version 1 of marks_distribution
def get_section_marks(total_marks, sections=sections_max_marks):
    # Ensure total marks are valid
    max_total = sum(sum(section) for section in sections)
    min_total = len(sections)  # Minimum 1 mark per sub-section

    if not (min_total <= total_marks <= max_total):
        raise ValueError("Total marks must be between the minimum and maximum possible marks.")

    # Initialize the distribution with minimum marks (1 mark for each sub-section)
    distributed_marks = [[1 for _ in section] for section in sections]
    remaining_marks = total_marks - sum(sum(section) for section in distributed_marks)

    while remaining_marks > 0:
        for section_idx, section in enumerate(sections):
            for sub_idx, max_mark in enumerate(section):
                if remaining_marks == 0:
                    break
                # Current mark for the sub-section
                current_mark = distributed_marks[section_idx][sub_idx]
                # Add 1 mark if it doesn't exceed the max limit
                if current_mark < max_mark:
                    distributed_marks[section_idx][sub_idx] += 1
                    remaining_marks -= 1

    return distributed_marks

def increment_column(col):
    """
    Increment an Excel column letter.
    For example, 'A' -> 'B', 'Z' -> 'AA', 'AZ' -> 'BA'.
    """
    # Convert the column string to an integer based on Excel column system
    num = 0
    for char in col:
        num = num * 26 + (ord(char) - ord('A') + 1)
    
    # Increment the number
    num += 1
    
    # Convert the number back to a column string
    result = ''
    while num > 0:
        num -= 1  # Adjust for 1-based index
        result = chr(num % 26 + ord('A')) + result
        num //= 26
    
    return result


#version 2 of marks_distribution
def distribute_marks(total_marks, sections=sections_max_marks):
    # Calculate the total of all highest marks
    max_total = sum(sum(section) for section in sections)

    if total_marks < len(sections) or total_marks > max_total:
        raise ValueError("Total marks must be between the minimum required marks and the sum of all max marks.")
    
    # Store the distributed marks
    distributed_marks = []
    
    # Randomly distribute marks for each subsection
    for section in sections:
        section_marks = []
        remaining_marks = total_marks // len(sections)  # Start with an even distribution
        
        for max_mark in section:
            # Ensure there's enough remaining marks to distribute, avoiding zero range
            if remaining_marks < 1:
                mark = 1
            else:
                mark = random.randint(1, min(remaining_marks, max_mark))
            
            section_marks.append(mark)
            remaining_marks -= mark

        distributed_marks.append(section_marks)

    # Adjust remaining marks to match total marks
    remaining_marks = total_marks - sum(sum(section) for section in distributed_marks)
    
    # Randomly distribute remaining marks across sections
    while remaining_marks != 0:
        for section_marks in distributed_marks:
            for i in range(len(section_marks)):
                if remaining_marks == 0:
                    break
                # If we still need marks and can increase this section
                if remaining_marks > 0 and section_marks[i] < sections[distributed_marks.index(section_marks)][i]:
                    section_marks[i] += 1
                    remaining_marks -= 1
                # If we need to decrease marks, but can't go below 1
                elif remaining_marks < 0 and section_marks[i] > 1:
                    section_marks[i] -= 1
                    remaining_marks += 1

    return distributed_marks