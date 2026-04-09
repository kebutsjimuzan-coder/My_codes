# ==========================================
# Python Mathematical Logic Exercises
# تمارين المنطق الحسابي في بايثون
# ==========================================

# --- Task 1: Multiplication Table (2s) | التمرين الأول: جدول ضرب الرقم 2 ---
# Using range with step or multiplication to print multiples of 2
# استخدام المدى لطباعة مضاعفات الرقم 2
print("--- Multiples of 2 ---")
for i in range(1, 11):
    print(i * 2)

print("\n" + "="*30 + "\n")

# --- Task 2: Logical Filtering (Not 3 or 5) | التمرين الثاني: التصفية المنطقية ---
# Printing numbers not divisible by 3 AND not divisible by 5
# طباعة الأرقام التي لا تقبل القسمة على 3 و لا تقبل القسمة على 5
print("--- Numbers NOT divisible by 3 or 5 ---")
i = 1
while i <= 50:
    if i % 3 != 0 and i % 5 != 0:
        print(i)
    i = i + 1

print("\n" + "="*30 + "\n")

# --- Task 3: Selective Summation | التمرين الثالث: الجمع الانتقائي ---
# Calculating the total sum of numbers from 1 to 50, excluding multiples of 3
# حساب المجموع الكلي للأرقام من 1 إلى 50 مع استثناء مضاعفات الرقم 3
print("--- Sum of numbers (excluding multiples of 3) ---")
i = 1
total_sum = 0 # Replaced 'm' for clarity | استبدال الحرف لزيادة الوضوح
while i <= 50:
    if i % 3 != 0:
        total_sum = total_sum + i
    i = i + 1
print("Total Sum:", total_sum)

print("\n" + "="*30 + "\n")

# --- Task 4: Countdown Logic | التمرين الرابع: منطق العد التنازلي ---
# Implementing a countdown from 10 down to 1 using a loop
# تنفيذ عد تنازلي من 10 إلى 1 باستخدام حلقة تكرارية
print("--- Countdown (10 to 1) ---")
n = 10
for i in range(0, 10, 1):
    result = n - i 
    print(result)


