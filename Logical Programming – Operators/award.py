# award.py

# =========================
# Triathlon Award Program
# =========================

print(" Triathlon Award Calculator")
print("-" * 35)

# Get user input
swimming = int(input("Enter swimming time (minutes): "))
cycling = int(input("Enter cycling time (minutes): "))
running = int(input("Enter running time (minutes): "))

# Calculate total time
total_time = swimming + cycling + running

# Display total time
print(f"\nTotal time taken for the triathlon: {total_time} minutes")

# Determine award
if total_time <= 100:
    award = "Provincial Colours"

elif 101 <= total_time <= 105:
    award = "Provincial Half Colours"

elif 106 <= total_time <= 110:
    award = "Provincial Scroll"

else:
    award = "No Award"

# Display result
print(f"Award: {award}")