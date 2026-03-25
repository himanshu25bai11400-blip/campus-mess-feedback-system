import csv
import datetime
import os
from collections import Counter

class Feedback:
    def __init__(self, student_id, date, meal_type, rating, comments):
        self.student_id = student_id
        self.date = date
        self.meal_type = meal_type 
        self.rating = rating        
        self.comments = comments

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "date": self.date,
            "meal_type": self.meal_type,
            "rating": self.rating,
            "comments": self.comments
        }

def save_feedback(feedback):
    file_path = "data/feedback.csv"
    os.makedirs("data", exist_ok=True)
    fieldnames = ["student_id", "date", "meal_type", "rating", "comments"]
    
    file_exists = os.path.isfile(file_path)
    with open(file_path, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow(feedback.to_dict())

def load_all_feedback():
    feedbacks = []
    try:
        with open("data/feedback.csv", "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                feedbacks.append(Feedback(
                    row["student_id"],
                    row["date"],
                    row["meal_type"],
                    int(row["rating"]),
                    row["comments"]
                ))
    except FileNotFoundError:
        pass
    return feedbacks

def generate_report():
    feedbacks = load_all_feedback()
    if not feedbacks:
        print("No feedback yet!")
        return
    
    ratings = [f.rating for f in feedbacks]
    avg_rating = sum(ratings) / len(ratings)
    meal_ratings = {}
    common_complaints = Counter()
    
    for f in feedbacks:
        if f.meal_type not in meal_ratings:
            meal_ratings[f.meal_type] = []
        meal_ratings[f.meal_type].append(f.rating)
        if f.comments.strip():
            common_complaints[f.comments.lower()] += 1
    
    print("\n=== Mess Feedback Report ===")
    print(f"Total feedbacks: {len(feedbacks)}")
    print(f"Overall Average Rating: {avg_rating:.2f}/5")
    print("\nMeal-wise Average:")
    for meal, rts in meal_ratings.items():
        print(f"  {meal}: {sum(rts)/len(rts):.2f}/5")
    
    print("\nTop 3 Common Comments:")
    for comment, count in common_complaints.most_common(3):
        print(f"  - {comment} ({count} times)")
    
   
    os.makedirs("reports", exist_ok=True)
    with open("reports/latest_report.txt", "w") as f:
        f.write("Campus Mess Feedback Report\n")
        f.write(f"Generated on: {datetime.date.today()}\n\n")
        f.write(f"Overall Average: {avg_rating:.2f}/5\n")
       
