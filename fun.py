
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

def get_practical_wise_mark(start_practical,end_practical,marks):
    practical_marks=[]

import random

def distribute_marks(avg_marks, num_practicals):
    if not (60 <= avg_marks <= 90):
        raise ValueError("Average marks must be between 60 and 90.")

    total_marks = avg_marks * num_practicals
    marks = []

    for _ in range(num_practicals):
        remaining_practicals = num_practicals - len(marks)
        if remaining_practicals > 1:
            if avg_marks>=67:
            # Randomly distribute marks close to the average, if avg marks >66
                mark = random.randint(max(60, avg_marks - 7), min(90, avg_marks + 7))
            else:
                mark = random.randint(max(60, avg_marks - 3), min(90, avg_marks + 3))
        else:
            # Ensure the last mark adjusts to meet the total
            mark = total_marks - sum(marks)
            mark = max(60, min(90, mark))
        marks.append(mark)
    
    return marks






