import pandas as pd 
import matplotlib.pyplot as plt 

def main():
    name = input("What is your name? ")
    course = input("What course: ")
    
    try:
        num_subject = int(input("How many subjects? "))
    except ValueError:
        print("You are supposed to input a number!")
        return
    
    subjects = []
    for i in range(num_subject):
        subject = input(f"Subject {i + 1} name: ")
        subjects.append(subject)
        
    def score_value():
        scores = []
        for i in range(num_subject):
            try:
                score = int(input(f"Your score for {subjects[i]}: "))
            except ValueError:
                print("Invalid input, defaulting to 0.")
                score = 0
            scores.append(score)
        return scores

    def grade(score):
        if score >= 80:
            return "Grade A"
        elif score >= 70:
            return "Grade B"
        elif score >= 60:
            return "Grade C"
        else:
            return "Grade F"

    def gpa(score):
        if score >= 80:
            return 4.0
        elif score >= 70: 
            return 3.0
        elif score >= 60:
            return 2.0
        else:
            return 1.0

    def remarks(score):
        if score >= 80:
            return "Excellent work!"
        elif score >= 70:
            return "Good job!"
        elif score >= 60:
            return "Satisfactory."
        else:
            return "Needs improvement"
    
    # collect all scores
    scores = score_value()
    
    # store results in DataFrame
    data = {
        "Subject": subjects,
        "Score": scores,
        "Grade": [grade(s) for s in scores],
        "GPA": [gpa(s) for s in scores],
        "Remarks": [remarks(s) for s in scores]
    }
    df = pd.DataFrame(data)
    
    print("\n=== Student Report ===")
    print(f"Name: {name}")
    print(f"Course: {course}\n")
    print(df.to_string(index=False))

    # Plot GPA vs Subjects
    plt.plot(df["Subject"], df["GPA"], marker="o",alpha = 0.6)
    plt.scatter(df["Subject"], df["GPA"],color = "skyblue",alpha=0.8)
    plt.title(f"{name}'s GPA Performance")
    plt.xlabel("Subjects")
    plt.ylabel("GPA")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()

