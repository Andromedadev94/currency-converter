import sys
rows = [[], [], [], []] #top, second, dash, result

def arithmetic_arranger(problems, show_answers=False):
    for problem in problems:
        n1 = problem.split()[0]
        operator = problem.split()[1]
        n2= problem.split()[2]
        if not n1.isdigit() or not n2.isdigit():
            print('Error: Numbers must only contain digits.')
            sys.exit()
        result = eval(problem)

        if len(n1) >= 5 or len(n2) >= 5:
            raise ValueError('Error: Numbers cannot be more than four digits.')
  
        if operator not in ["+" , "-"]:
            print("Error: Operator must be '+' or '-'.")
            sys.exit()

        width = max(len(str(n1)), len(str(n2)), len(str(result))-1) + 2

        row1 = str(n1).rjust(width)
        row2 = operator + str(n2).rjust(width-1)
        row3 = "-" * (width)
        if show_answers:
            row4 = str(result).rjust(width)
            rows[3].append(row4)

        rows[0].append(row1)
        rows[1].append(row2)
        rows[2].append(row3)
    output = ""
    for row in rows:
        output += "    ".join(row) + "\n"
    return output.rstrip()


    
print(arithmetic_arranger(["32 + 698", "3801 + 2", "45 + 43", "123 + 49"], True))

