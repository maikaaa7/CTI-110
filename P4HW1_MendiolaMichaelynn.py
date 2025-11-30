# Michaelynn Mendiola
# 11/28/2025
# P4HW1
# Program stores the scores entered and displays: lowest score, modified list of scores, average, and grade earned.

# Ask how many scores to enter
num_scores = int(input("How many scores do you want to enter? "))

scores = []

# FOR loop to collect valid scores
for i in range(1, num_scores + 1):
    score = float(input(f"Enter score #{i}: "))

    # WHILE loop to validate the scores
    while score < 0 or score > 100:
        print("INVALID Score entered!!!!")
        print("Score should be between 0 and 100")
        score = float(input(f"Enter score #{i} again: "))
    
    
    scores.append(score)

# Process scores
lowest = min(scores)
scores.remove(lowest)
avg = sum(scores) / len(scores)

# Display Results
print("------------Results------------")
print(f"{'Lowest Score:':20}{lowest:,.1f}")
print(f"{'Modified List:':20}{scores}")  
print(f"{'Scores Average:':20}{avg:,.1f}")

# Determine letter grade for average
if avg >= 90:
    print('Your grade is: A')
elif avg >= 80:
    print('Your grade is: B')
elif avg >= 70:
    print("Your grade is: C")
elif avg >= 60:
    print("Your grade is: D")
else:
    print("Your grade is: F")

print("---------------------------------")