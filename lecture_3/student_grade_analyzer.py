class StudentGradeAnalyzer:
    def __init__(self):
        self.students = []

    def display_menu(self):

        print("\n" + "=" * 40)
        print("      Student Grade Analyzer")
        print("=" * 40)
        print("1. Add a new student")
        print("2. Add grades for a student")
        print("3. Show report (all students)")
        print("4. Find top performer")
        print("5. Exit")
        print("=" * 40)

    def add_student(self):

        try:
            name = input("Enter student name: ").strip()

            if not name:
                print("Error: Student name cannot be empty!")
                return

            for student in self.students:
                if student["name"].lower() == name.lower():
                    print(f"Error: Student '{name}' already exists!")
                    return

            new_student = {
                "name": name,
                "grades": []
            }
            self.students.append(new_student)
            print(f"Student '{name}' added successfully!")

        except Exception as e:
            print(f"An error occurred while adding student: {e}")

    def add_grades(self):

        try:
            if not self.students:
                print("No students available. Please add students first.")
                return

            name = input("Enter student name: ").strip()

            student_found = None
            for student in self.students:
                if student["name"].lower() == name.lower():
                    student_found = student
                    break

            if not student_found:
                print(f"Error: Student '{name}' not found!")
                return

            print(f"Adding grades for {student_found['name']}. Enter grades (0-100) or 'done' to finish:")

            while True:
                grade_input = input("Enter a grade (or 'done' to finish): ").strip().lower()

                if grade_input == 'done':
                    break

                try:
                    grade = float(grade_input)

                    if grade < 0 or grade > 100:
                        print("Error: Grade must be between 0 and 100!")
                        continue

                    student_found["grades"].append(grade)
                    print(f"Grade {grade} added successfully!")

                except ValueError:
                    print("Invalid input. Please enter a number or 'done'.")

            print(f"Grades entry completed for {student_found['name']}.")

        except Exception as e:
            print(f"An error occurred while adding grades: {e}")

    def calculate_average(self, grades):

        try:
            if not grades:
                return None
            return sum(grades) / len(grades)
        except ZeroDivisionError:
            return None
        except Exception:
            return None

    def show_report(self):

        try:
            if not self.students:
                print("No students available.")
                return

            print("\n" + "-" * 20)
            print("   Student Report")
            print("-" * 20)

            averages = []
            valid_averages = []

            for student in self.students:
                avg = self.calculate_average(student["grades"])
                averages.append(avg)

                if avg is not None:
                    valid_averages.append(avg)
                    print(f"{student['name']}'s average grade is {avg:.2f}.")
                else:
                    print(f"{student['name']}'s average grade is N/A.")

            if valid_averages:
                max_avg = max(valid_averages)
                min_avg = min(valid_averages)
                overall_avg = sum(valid_averages) / len(valid_averages)

                print("-" * 30)
                print(f"Max Average: {max_avg:.2f}")
                print(f"Min Average: {min_avg:.2f}")
                print(f"Overall Average: {overall_avg:.2f}")
            else:
                print("-" * 30)
                print("No valid grades available for statistics.")

        except Exception as e:
            print(f"An error occurred while generating report: {e}")

    def find_top_performer(self):

        try:
            if not self.students:
                print("No students available.")
                return

            students_with_grades = []
            for student in self.students:
                avg = self.calculate_average(student["grades"])
                if avg is not None:
                    students_with_grades.append((student, avg))

            if not students_with_grades:
                print("No students with valid grades available.")
                return

            top_student, top_avg = max(students_with_grades, key=lambda x: x[1])
            print(f"The student with the highest average is {top_student['name']} with a grade of {top_avg:.2f}.")

        except Exception as e:
            print(f"An error occurred while finding top performer: {e}")

    def run(self):

        print("Welcome to Student Grade Analyzer!")

        while True:
            try:
                self.display_menu()
                choice = input("Enter your choice (1-5): ").strip()

                if choice == '1':
                    self.add_student()
                elif choice == '2':
                    self.add_grades()
                elif choice == '3':
                    self.show_report()
                elif choice == '4':
                    self.find_top_performer()
                elif choice == '5':
                    print("Exiting program. Goodbye!")
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and 5.")

            except KeyboardInterrupt:
                print("\n\nProgram interrupted by user. Exiting...")
                break
            except Exception as e:
                print(f"An unexpected error occurred: {e}")



if __name__ == "__main__":
    analyzer = StudentGradeAnalyzer()
    analyzer.run()
