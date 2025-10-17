def students_passing(scores):
    passing_failing = {'Passing': [x for x in scores if x >= 50],
                       'failing': [i for i in scores if i < 50]}
    return passing_failing

def main():
    # Ask for class size (must be a positive integer)
    while True:
        try:
            data = int(input('How many people are in the class: '))
            if data <= 0:
                print('Please enter a positive number for class size.')
                continue
            break
        except ValueError:
            print('Please enter a valid integer for class size.')

    # Collect grades and validate each is between 0 and 100
    raw_scores = []
    for num in range(data):
        while True:
            try:
                result = int(input(f"Enter student grade #{num+1}: "))
                if 0 <= result <= 100:
                    raw_scores.append(result)
                    break
                else:
                    print('Grade must be between 0 and 100. Try again.')
            except ValueError:
                print('Please enter a valid integer grade (0-100).')
        groups = students_passing(raw_scores)
        print(f'Passing: {groups["Passing"]}')
        print(f'Failing: {groups["failing"]}')

        #Failing Average
        failing = groups['failing']
        if failing:
            avg_fail = sum(failing) / len(failing)
            print(f'Average failing score: {avg_fail:.2f}')
        else:
            print('No failing students; average failing score: N/A')
        
        #Passing Average
        passing = groups['Passing']
        if passing:
            avg_pass = sum(passing)/len(passing)
            print(f"Average for the passing score: {avg_pass:.2f}")
        else:
            print("No Student Passed; average passing score: N/A")

        #Total Average
        average_class_grade = sum(raw_scores)/len(raw_scores)
        print(f'Here is the class average: {average_class_grade}')

main()
