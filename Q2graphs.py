
class Course:
    # Course entity class
    def __init__(self, courseCode, courseName, creditHours, level):
        self.courseCode = courseCode
        self.courseName = courseName
        self.creditHours = creditHours
        self.level = level

    def __str__(self):
        return (
            f"Course Code: {self.courseCode}\n"
            f"Course Name: {self.courseName}\n"
            f"Credit Hours: {self.creditHours}\n"
            f"Level: {self.level}"
        )


class Graph:
    # Generic directed graph using adjacency list
    def __init__(self):
        self.adjacencyList = {}

    # Add a new vertex
    def addVertex(self, vertex):
        if vertex not in self.adjacencyList:
            self.adjacencyList[vertex] = []

    # Connect one vertex to another
    def addEdge(self, fromVertex, toVertex):
        if fromVertex not in self.adjacencyList:
            self.addVertex(fromVertex)

        if toVertex not in self.adjacencyList:
            self.addVertex(toVertex)

        if toVertex not in self.adjacencyList[fromVertex]:
            self.adjacencyList[fromVertex].append(toVertex)

    # List all incoming adjacent vertices
    def listIncomingAdjacentVertex(self, vertex):
        incomingVertices = []

        if vertex not in self.adjacencyList:
            return incomingVertices

        for currentVertex in self.adjacencyList:
            if vertex in self.adjacencyList[currentVertex]:
                incomingVertices.append(currentVertex)

        return incomingVertices

    # List all outgoing adjacent vertices
    def listOutgoingAdjacentVertex(self, vertex):
        if vertex not in self.adjacencyList:
            return []

        return self.adjacencyList[vertex]


# Course Objects
course1 = Course(
    "CS101",
    "Introduction to Programming",
    3,
    "Core"
)

course2 = Course(
    "CS102",
    "Object-Oriented Programming",
    3,
    "Core"
)

course3 = Course(
    "CS103",
    "Data Structures",
    4,
    "Core"
)

course4 = Course(
    "CS104",
    "Database Systems",
    3,
    "Core"
)

course5 = Course(
    "CS105",
    "Web Development",
    3,
    "Elective"
)

course6 = Course(
    "CS106",
    "Advanced Algorithms",
    4,
    "Elective"
)

# Store all courses in a list
courses = [
    course1,
    course2,
    course3,
    course4,
    course5,
    course6
]

# Create course prerequisite path
graph = Graph()

# Add all courses as vertices
for course in courses:
    graph.addVertex(course)

# Add prerequisite relationships
# fromVertex -> toVertex
# Means fromVertex is a prerequisite of toVertex

graph.addEdge(course1, course2)
graph.addEdge(course2, course3)
graph.addEdge(course1, course4)
graph.addEdge(course2, course5)
graph.addEdge(course3, course6)
graph.addEdge(course4, course6)


# Display all courses
def displayCourses():
    print("\n========== COURSE LIST ==========")

    for i, course in enumerate(courses, start=1):
        print(f"{i}. {course.courseName} ({course.courseCode})")


# Find course using course code
def findCourse(courseCode):
    for course in courses:
        if course.courseCode.lower() == courseCode.lower():
            return course

    return None


# View course details
def viewCourseDetails():
    print("\n========== VIEW COURSE DETAILS ==========")

    courseCode = input("Enter course code: ")

    course = findCourse(courseCode)

    if course is not None:
        print("\n========== COURSE DETAILS ==========")
        print(course)
    else:
        print("Course not found!")


# View prerequisite courses
def viewPrerequisites():
    print("\n========== VIEW PREREQUISITES ==========")

    courseCode = input("Enter course code: ")

    course = findCourse(courseCode)

    if course is None:
        print("Course not found!")
        return

    prerequisites = graph.listIncomingAdjacentVertex(course)

    print(f"\nPrerequisites for {course.courseName}:")

    if len(prerequisites) == 0:
        print("No prerequisite courses.")
    else:
        for prerequisite in prerequisites:
            print(
                f"- {prerequisite.courseName} "
                f"({prerequisite.courseCode})"
            )


# View unlocked courses
def viewUnlockedCourses():
    print("\n========== VIEW UNLOCKED COURSES ==========")

    courseCode = input("Enter course code: ")

    course = findCourse(courseCode)

    if course is None:
        print("Course not found!")
        return

    unlockedCourses = graph.listOutgoingAdjacentVertex(course)

    print(f"\nCourses unlocked by {course.courseName}:")

    if len(unlockedCourses) == 0:
        print("This course does not unlock any other courses.")
    else:
        for unlocked in unlockedCourses:
            print(
                f"- {unlocked.courseName} "
                f"({unlocked.courseCode})"
            )


# Main Menu
def main():
    while True:
        print("\n==========================================")
        print("       UNIVERSITY COURSE SYSTEM")
        print("==========================================")
        print("1. Display all courses")
        print("2. View course details")
        print("3. View prerequisite courses")
        print("4. View unlocked courses")
        print("5. Exit")
        print("==========================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            displayCourses()

        elif choice == "2":
            viewCourseDetails()

        elif choice == "3":
            viewPrerequisites()

        elif choice == "4":
            viewUnlockedCourses()

        elif choice == "5":
            print("\nThank you for using the University Course System!")
            break

        else:
            print("\nInvalid choice! Please enter 1 to 5.")

if __name__ == "__main__":
    main()
