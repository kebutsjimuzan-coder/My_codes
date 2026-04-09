# --- Initializing the List | تهيئة القائمة ---
# Creating an empty list to store user input
# إنشاء قائمة فارغة لتخزين الأرقام المدخلة
numbers = []

# --- Data Collection Loop | حلقة جمع البيانات ---
while True:
    num = input(' Enter a number (or type "done" to finish): ')
    
    # Checking for the exit condition
    # التحقق من شرط الخروج من الحلقة
    if num == 'done':
        break 
    else:
        try:
            # Converting input to integer and adding to the list
            # تحويل المدخل إلى رقم صحيح وإضافته للقائمة
            num = int(num)
            numbers.append(num)
        except:
            # Handling non-numeric input errors
            # معالجة أخطاء المدخلات غير الرقمية
            print('Invalid input, please enter a number')
            continue

# Printing the final list of numbers
# طباعة قائمة الأرقام النهائية
print("List of numbers:", numbers)

# --- Data Processing Logic | منطق معالجة البيانات ---
totale = 0 # To store the sum of even numbers | لتخزين مجموع الأرقام الزوجية
count = 0  # To count odd numbers | لحساب عدد الأرقام الفردية

# Iterating through the list to filter even and odd numbers
# المرور على القائمة لفرز الأرقام الزوجية والفردية
for i in numbers:
    if i % 2 == 0:
        # If the number is even, add it to the total
        # إذا كان الرقم زوجياً، أضفه للمجموع
        totale = totale + i
    else:
        # If the number is odd, increment the counter
        # إذا كان الرقم فردياً، زد العداد واحد
        count = count + 1

# Outputting the results
# طباعة النتائج النهائية
print(f"Sum of even numbers: {totale}")
print(f"Count of odd numbers: {count}")

