# ==========================================
# Functions & Dynamic List Processing
# الدوال ومعالجة القوائم الديناميكية
# ==========================================

# --- Task 1: Boolean Function (Even Check) | التمرين الأول: دالة التحقق المنطقي ---
# A function that returns a string indicating if a number is even or odd
# دالة تعيد نصاً يوضح ما إذا كان الرقم زوجياً أم فردياً
def is_even(number):
    """Checks if a number is even | تتحقق ما إذا كان الرقم زوجياً"""
    if number % 2 == 0:
        return 'True'
    else:
        return 'False'

# Testing the function
# اختبار الدالة
check_result = is_even(7)
print(f"Is 7 even? {check_result}")

print("\n" + "="*30 + "\n")

# --- Task 2: Math Function (Squaring) | التمرين الثاني: دالة الحساب (التربيع) ---
# A function that calculates the square of a number and returns it for further use
# دالة تحسب مربع الرقم وتعيده لاستخدامه في عمليات أخرى
def calculate_square(number):
    """Returns the square of a number | تعيد مربع الرقم"""
    return number ** 2

# Using the function in a mathematical expression
# استخدام الدالة في تعبير رياضي
final_value = calculate_square(4) + 2
print(f"Square of 4 plus 2 is: {final_value}")

print("\n" + "="*30 + "\n")

# --- Task 3: Interactive Max Finder | التمرين الثالث: البحث عن القيمة الكبرى ---
# Collecting numbers into a list and finding the largest value
# جمع الأرقام في قائمة والبحث عن القيمة الكبرى
print("--- Dynamic Max Value Finder ---")
numeric_list = []
while True:
    user_input = input('Enter a number (or "stop" to finish): ')
    
    if user_input == 'stop':
        break
    
    try:
        converted_num = int(user_input)
        numeric_list.append(converted_num)
    except ValueError:
        print('Error: This is not a valid number.')

# Finding the largest number in the collected list
# إيجاد الرقم الأكبر في القائمة المجمعة
if numeric_list:
    max_value = None
    for current_num in numeric_list:
        if max_value is None or current_num > max_value:
            max_value = current_num
    
    print(f"Collected Numbers: {numeric_list}")
    print(f"The largest number is: {max_value}")
else:
    print("No numbers were collected.")


