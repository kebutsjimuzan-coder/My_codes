# ==========================================
# User Interaction & Applied Logic
# تفاعل المستخدم والمنطق البرمجي التطبيقي
# ==========================================

# --- Task 1: Grade Stats & High Scorers | التمرين الأول: إحصائيات الدرجات والمتفوقين ---
# Tracking grades with range validation and counting high achievements
# تتبع الدرجات مع التحقق من النطاق وحساب عدد المتفوقين
print("--- Grade Statistics ---")
grade_count = 0
grade_total = 0
high_achievers = 0

while True:
    score_input = input('Enter a grade (0-100) or "done" to finish: ')
    if score_input == 'done':
        break
    try:
        score = int(score_input)
        if score < 0 or score > 100:
            print('Invalid grade! Please enter a value between 0 and 100.')
            continue
        
        grade_total += score
        grade_count += 1
        if score > 90:
            high_achievers += 1
    except ValueError:
        print('Error: This is not a number.')

if grade_count > 0:
    avg_grade = grade_total / grade_count
    print(f"Stats -> Count: {grade_count}, Total: {grade_total}, High Grades: {high_achievers}, Average: {avg_grade}")
else:
    print("No valid grades entered.")

print("\n" + "="*30 + "\n")

# --- Task 2: Greeting & Ideal Weight Calc | التمرين الثاني: التحية وحساب الوزن المثالي ---
# Simple user greeting and a basic formula for ideal weight based on height
# تحية المستخدم ومعادلة بسيطة لحساب الوزن المثالي بناءً على الطول
print("--- User Greeting & Health Tool ---")
user_name = input("Enter your name: ")
print("مرحباً يا " + user_name)

height_input = input('Enter your length (in meters, e.g., 1.75): ')
try:
    height = float(height_input)
    # Formula: Height squared * 22 (Standard BMI constant)
    ideal_weight = (height ** 2) * 22 
    print(f"Your estimated ideal weight is: {ideal_weight:.2f} kg")
except ValueError:
    print("Please enter a valid height in numeric format.")

print("\n" + "="*30 + "\n")

# --- Task 3: Iterative Condition Check | التمرين الثالث: التحقق الشرطي التكراري ---
# Demonstrating how conditions change within a loop
# توضيح كيفية تغير الشروط داخل الحلقة التكرارية
print("--- Sequential Logic Check ---")
current_val = 2
for step in range(0, 8):
    current_val = current_val + step
    if current_val >= 4:
        print(f"Value {current_val}: Good")
    else:
        print(f"Value {current_val}: Bad")
      
