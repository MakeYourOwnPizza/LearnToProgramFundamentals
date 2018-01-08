def read_grades(gradefile):
    '''(file open for reading) -> dict of {float: list of str}

    Read the grades from gradefile and return a dictionary where
    each key is a grade and each value is the list of ids of students
    who earned that grade.

    Precondition: gradefo;e starts wotj a header that contains
    no blank lines, then has a blank line, and then lines containing
    a student number and a grade.
    '''

    # Skip over the header. We read part of the text until we hit the blank line.
    line = gradefile.readline()
    while line != '\n':
        line = gradefile.readline()
    
    # Read the grades, accumulating them into a dict.

    grade_to_ids = {}
    line = gradefile.readline()

    while line != '':
        
        # four-digit student id
        student_id = line[:4]
        # space of white space on both ends, and show them as float
        grade = float(line[4:].strip())

        if grade not in grade_to_ids:
            grade_to_ids[grade] = [student_id]
        else:
            grade_to_ids[grade].append(student_id)

        # Once we finish adding this grade and student ID to the dictionary,
        #we can move onto the next line of the file.
        line = gradefile.readline()

    return grade_to_ids
