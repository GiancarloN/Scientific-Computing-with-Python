def verify_input(problems):
    '''Verifies if the user supplied the correct format of problems.'''
    if len(problems) > 5:
        return "Error: Too many problems."
    else:
        for problem in problems:
            tmp = problem.split()
            if len(tmp[0]) > 4 or len(tmp[2]) > 4:
                return "Error: Numbers cannot be more than four digits."
                break
            if tmp[0].isdigit() == False or tmp[2].isdigit() == False:
                return "Error: Numbers must only contain digits."
                break
            if tmp[1] not in "+-":
                return "Error: Operator must be '+' or '-'."
                break

def find_lenght(list):
    '''Finds the lenght of the biggest number in each problem and returns the
    amout of space each problem will occupy accounting for the operator and the space'''
    lenght = 0 
    for element in list: 
        if len(element) > lenght:
            lenght = len(element)

    return lenght + 2
    
def formatted_problems(problems, show_results):
    '''A function that receives a list of strings that are arithmetic problems and returns the 
    problems arranged vertically and side-by-side. The function should optionally take a second argument. 
    When the second argument is set to True, the answers are displayed.'''

    formatted_string = None

    formatted_string = verify_input(problems)

    if formatted_string == None:
        
        #Create a list of lists with each individual list containing the elements of each problem and the space required
        problems_list = list()
        for entry in problems:
            tmp = entry.split()
            tmp.append(find_lenght(tmp))
            problems_list.append(tmp)

        #Creating the string with the formatted problems
        formatted_string = ""
        
        #Creates the first row of numbers
        for element in problems_list:
            formatted_string += " " * (element[3] - len(element[0]))
            formatted_string += element[0]
            if element != problems_list[-1]:
                formatted_string +=  (" " * 4)
        formatted_string += "\n"
        
        #Creates the second row of numbers + the operator
        for element in problems_list:
            formatted_string += element[1] + " " * (element[3] - len(element[2]) - 1)
            formatted_string += element[2]
            if element != problems_list[-1]:
                formatted_string +=  " " * 4
        formatted_string += "\n"

        #Adds dashes at the bottom
        for element in problems_list:
            formatted_string += "-" * (element[3])
            if element != problems_list[-1]:
                formatted_string +=  (" " * 4)
    
        #Add the results if required
        if show_results == True:
            formatted_string += "\n"

            for element in problems_list:
                result = 0
                if element[1] == "+":
                    result = int(element[0]) + int(element[2])
                else:
                    result = int(element[0]) - int(element[2])
                formatted_string += " " * (element[3] - len(str(result))) + str(result)
                if element != problems_list[-1]:
                    formatted_string +=  (" " * 4)

    return formatted_string


def arithmetic_arranger(problems, show_results = False):

    arranged_problems = formatted_problems(problems, show_results)

    return arranged_problems