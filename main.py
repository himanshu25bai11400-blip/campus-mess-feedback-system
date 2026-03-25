from feedback import Feedback, save_feedback, generate_report
import datetime

def main():
    print("Welcome to MessMate - Campus Mess Feedback System")
    while True:
        print("\n1. Submit Feedback")
        print("2. View Report (for mess committee)")
        print("3. Exit")
        choice = input("Enter choice: ")
        
        if choice == "1":
            student_id = input("Enter your Student ID (or 'anonymous'): ")
            date = datetime.date.today().isoformat()
            meal_type = input("Meal type (Breakfast/Lunch/Dinner): ")
            while True:
                try:
                    rating = int(input("Rating (1-5): "))
                    if 1 <= rating <= 5:
                        break
                    print("Rating must be 1-5")
                except ValueError:
                    print("Invalid input")
            comments = input("Comments (optional): ")
            
            fb = Feedback(student_id, date, meal_type, rating, comments)
            save_feedback(fb)
            print("Thank you! Feedback submitted.")
            
        elif choice == "2":
            generate_report()
        elif choice == "3":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
