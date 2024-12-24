import random

def distribute_marks(total_marks, sections):
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

# Input: Total marks and section-wise highest marks
total_marks = 85
sections = [
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

print(distribute_marks(total_marks, sections))