# Avery Mitchell
#Prog Assign_4_BugCollector
# COSC 1010_500
# Collects the number of bugs found each day for 5 days and keeps a running total

total_bugs = 0

for day in range(1, 6):  # Loops for day 1 through day 5
    bugs_today = int(input(f"Enter the number of bugs collected on day {day}: "))
    total_bugs += bugs_today  # Add today's bugs to the running total

print(f"\nTotal bugs collected over the 5 days: {total_bugs}")
