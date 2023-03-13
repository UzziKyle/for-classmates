import security
import compute

security.askUsername()

firstYear = {
    "General Courses" : {
        "EnviSci" : 3,
        "Algebra" : 3,
    },
    "Professional Courses" : {
        "Eng 1": 3,
        "Fil 1" : 3,
        "PE 1" : 3,
    },
    "Core Courses" : {
        "CC1" : 3,
        "CC2" : 3,
    },
    "Misc Fee" : 2000,
}

secondYear = {
    "General Courses" : {
        "Cal 2" : 3,
        "Linear" : 3,
        "Physics1" : 3,
    },
    "Professional Courses" : {
        "Eng 3" : 3,
        "Fil 3" : 3,
        "PE 3" : 3,
    },
    "Core Courses" : {
        "CC4" : 3,
        "CC5" : 3,
    },
    "Misc Fee" : 2500,
}

thirdYear = {
    "General Courses" : {
        "PolSci 1" : 3,
        "Anthro 1" : 3,
        "Psych 1" : 3,
    },
    "Professional Courses" : {
        "Writing 1" : 3,
        "DataSci 1": 3,
    },
    "Core Courses" : {
        "CC6" : 3,
        "CC10" : 3,
        "Thesis 1" : 3,
    },
    "Misc Fee" : 3000,
}

fourthYear = {
    "General Courses" : {
        "Acctg 1" : 3,
        "Rizal" : 3, 
    },
    "Professional Courses" : {
        "Writing 3" : 3,
        "DataSci 3" : 3,
    },
    "Core Courses" : {
        "Elect 1" : 3,
        "Elect 2" : 3,
        "Thesis 2" : 3,
    },
    "Misc Fee" : 3500,
}

subjects = {
    "FIRST YEAR" : firstYear,
    "SECOND YEAR" : secondYear,
    "THIRD YEAR" : thirdYear,
    "FOURTH YEAR" : fourthYear,
}


studentInfoKeys = ["First Name","Middle Initial","Last Name","Course","Year"]
studentInfo = {studentInfoKeys[key] : (input(f"Enter {studentInfoKeys[key]}: ").strip().upper()) for key in range(len(studentInfoKeys))}

generalCourseUnits = subjects[studentInfo["Year"]].get("General Courses")
professionalCourseUnits = subjects[studentInfo["Year"]].get("Professional Courses")
coreCourseUnits = subjects[studentInfo["Year"]].get("Core Courses")

totalUnits = [generalCourseUnits, professionalCourseUnits, coreCourseUnits]


def unitsComputation():

    global subjects
    global totalUnits

    totalUnitsPrice = 0
    for course in totalUnits:
        for units in course.values():
            unitsPrice = units * 1000
            totalUnitsPrice += unitsPrice

    misc = subjects[studentInfo["Year"]].get("Misc Fee")

    paymentScheme = input("\nEnter payment scheme(FULL PAYMENT, INSTALLMENTS, PARTIAL PAYMENT): ").upper().strip()

    if paymentScheme == "FULL PAYMENT":
        outputPrinter(paymentScheme,compute.paymentMode1(totalUnitsPrice, misc))

    elif paymentScheme == "INSTALLMENTS":
        outputPrinter(paymentScheme,compute.paymentMode2(totalUnitsPrice, misc))

    elif paymentScheme == "PARTIAL PAYMENT":
        outputPrinter(paymentScheme,compute.paymentMode3(totalUnitsPrice, misc))


def outputPrinter(paymentScheme,tuition):

    global studentInfo
    global totalUnits

    print("\n\nGeneral Subjects \t{}\nProfessional Subjects \t{}\nCore Courses \t\t{}".format(totalUnits[0],totalUnits[1],totalUnits[2]))
    print("{}, {} {}. - {} {} - Tuition: P {} - {}".format(studentInfo["Last Name"], studentInfo["First Name"], studentInfo["Middle Initial"], studentInfo["Year"],studentInfo["Course"],tuition,paymentScheme))
    
    quit()


unitsComputation()