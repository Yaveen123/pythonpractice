days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
subjects = ["English", "Software", "Drama", "Science", "Sport"]



def generateTimetable(subjectsInput):
    timetable = []
    for i in range(0,4):
        subjectsToInsert = []
        for j in range(len(subjectsInput)):  # Added missing colon and fixed range()
            subjectsToInsert.append(subjectsInput[j])
        timetable.append(subjectsToInsert)
    print(timetable)


def printTimetable():
    dayCounter = -1
    for day in timetable:
        dayCounter += 1
        print(days[dayCounter])
        
        periodCounter = -1 
        for period in day:
            periodCounter += 1
            print(f"Period {periodCounter}: {period}")

generateTimetable(subjects)
