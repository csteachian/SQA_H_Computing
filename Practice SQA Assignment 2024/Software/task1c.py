import csv
filePath = 'Practice SQA Assignment 2024/Software/'

def read_from_file_into_parallel_arrays():
    company = []
    numEmployees = []
    ceoSalary = []
    with open(filePath+'companies.csv','r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            company.append(row[0])
            numEmployees.append(int(row[1]))
            ceoSalary.append(int(row[2]))
    return company, numEmployees, ceoSalary

def findMaxPos(thisArray):
    #     Set max to the value of thisArray[0]
    max = thisArray[0]
    #     Set position to 0
    position = 0
    #     Loop for all remaining items in thisArray (1 to length of thisArray)
    for index in range(1,len(thisArray)):
    #         If thisArray[index] > max then
        if thisArray[index] > max:
    #             Set max to thisArray[index]
            max = thisArray[index]
    #             Set position to the index
            position = index
    #         End If
    #     End loop
    #     RETURN position
    return position
    # END FUNCTION


def find_and_display_salary_difference(company, ceoSalary):
    # Ask user to enter the name of chosen company
    companyName = input("Enter the name of the chosen company: ")
    # Set found to False
    found = False
    # Call findMaxPos function to return the position of the highest CEO salary
    highestSalaryPos = findMaxPos(ceoSalary)
    # Loop for company array
    for index in range(0,len(company)):
    #    If current company is the chosen company
         if company[index] == companyName:
    #        Set found to True
             found = True
    #        Set position to current index
             position = index
    #    End if
    # End loop
    # If chosen company name is in list
    if found == True:
    #    Subtract and store chosen company's CEO salary from highest CEO salary
         salaryDifference = ceoSalary[highestSalaryPos] - ceoSalary[position]
    #    Display message containing the name of company with the highest CEO salary, name of chosen company and difference in salaries
         print(company[highestSalaryPos]+" company has the highest paid CEO.")
         print("The "+companyName+" CEO earns £"+ str(salaryDifference)+" less than the highest paid CEO.")
    # Else
    else:
    #    Display "Company not found"
         print("Company not found")
    # End if

def find_and_display_companies(numEmployees):
    # Call findMaxPos function to reutrn position of highest number of employees
    highestEmployeesPosition = findMaxPos(numEmployees)
    # Set count to 0
    count = 0
    # Loop for numEmployees array
    for index in range(0, len(numEmployees)):
    #     If current employees is greater than or equal to maximum employees * 0.9
        if numEmployees[index] >= numEmployees[highestEmployeesPosition] * 0.9:
    #         Set count to count + 1
            count = count + 1
    #     End if
    # End loop
    # Display message showing number of companies that employ within 10% of the highest number of employees
    print("The highest number of employees employed by a single company is "+str(numEmployees[highestEmployeesPosition]))
    print(str(count)+" companies employ within 10% of "+str(numEmployees[highestEmployeesPosition]))

# main program
company, numEmployees, ceoSalary = read_from_file_into_parallel_arrays()
find_and_display_salary_difference(company, ceoSalary)
find_and_display_companies(numEmployees)