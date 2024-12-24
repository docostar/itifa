
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








