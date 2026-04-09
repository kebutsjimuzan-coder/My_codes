# ==========================================
# Advanced Logic & Statistical Operations
# العمليات المنطقية المتقدمة والإحصاء
# ==========================================

# --- Task 1: Drawing Patterns (Pyramid) | التمرين الأول: رسم الأشكال (المثلث) ---
# Using nested while loops to create a star pattern
# استخدام حلقات متداخلة لإنشاء مثلث من النجوم
print("--- Increasing Star Pattern ---")
row_limit = 1
while row_limit <= 5:
    column_count = 1
    while column_count <= row_limit:
        print("*", end=" ")
        column_count += 1
    print()
    row_limit += 1

print("\n" + "="*30 + "\n")

# --- Task 2: Live Average Calculator | التمرين الثاني: حاسبة المتوسط المباشر ---
# Calculating running average from user input with error handling
# حساب المتوسط الحسابي من مدخلات المستخدم مع معالجة الأخطاء
print("--- Interactive Average Calculator ---")
entry_count = 0
running_total = 0
while True:
    user_input = input('Enter a number (or "Done" to finish): ')
    if user_input == 'Done':
        break 
    try:
        numeric_value = int(user_input)
        running_total += numeric_value
        entry_count += 1
    except:
        print('Error: Invalid input, please enter a number')

if entry_count > 0:
    calculated_average = running_total / entry_count
    print(f"Results -> Average: {calculated_average}, Count: {entry_count}, Total: {running_total}")
else:
    print('No numbers were entered.')

print("\n" + "="*30 + "\n")

# --- Task 3: Min/Max/Avg Stats | التمرين الثالث: إحصائيات شاملة ---
# A refined script to find Smallest, Largest, and Average from a list
# كود مطور لإيجاد الأصغر، الأكبر، والمتوسط من قائمة
print("--- List Statistics ---")
data_list = [] # Changed from 'Muzan' to 'data_list' for professional naming
while True:
    raw_val = input('Enter a float (or "exit" to finish): ')
    if raw_val == 'exit':
        break 
    try:
        float_val = float(raw_val)
        data_list.append(float_val)
    except:
        print('Invalid input')
        continue

if data_list:
    min_val = None # Changed from 'small'
    max_val = None # Changed from 'large'
    sum_total = 0
    for value in data_list:
        sum_total += value
        if max_val is None or value > max_val:
            max_val = value
        if min_val is None or value < min_val:
            min_val = value
    
    print(f"Stats -> Min: {min_val}, Max: {max_val}, Avg: {sum_total/len(data_list)}")
else:
    print("List is empty.")

print("\n" + "="*30 + "\n")

# --- Task 4: Inverted Pyramid | التمرين الرابع: المثلث المقلوب ---
# Using nested 'for' loops with range steps to reverse the pattern
# استخدام حلقات for المتداخلة مع الخطوات العكسية لقلب المثلث
print("--- Decreasing Star Pattern ---")
for i in range(5, 0, -1):
    for star in range(i):
        print("*", end=" ")
    print()


