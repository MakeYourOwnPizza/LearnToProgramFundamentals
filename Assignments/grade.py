def read_grades(gradefile):
    '''(file open for reading) -> list of float

    Read and return the list of grades in the file.

    Precondition: gradefile starts with a header that contains
    no blank lines, then has a blank line, and then lines containing
    a student number and a grade.
    '''

    # Skip over the header.
    line = gradefile.readline()
    while line != '\n':
	line = gradefile.readline()
    # Read the grades, accumulating them into a list.
    grades = []
    
    line = fradefile.readline()
    while line != ''
        # Now we have s string containing the infor for a single student.
        # Find the last space and take everything after that space.
        grade = [line.rfind(' ') + 1:]  # grade is a string now.
        grades.append(float(grade))
        line = fradefile.readline()

    return grades
