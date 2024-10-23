# Function to calculate the average grade
def calculate_average(math, english, science):
    total = math + english + science
    average = total / 3
    return average

# Input grades for each subject
math = float(input("Enter Math grade: "))
english = float(input("Enter English grade: "))
science = float(input("Enter Science grade: "))

# Calculate average grade
average_grade = calculate_average(math, english, science)

# Output the average grade
print(f"The average grade is: {average_grade:.2f}")
