# ==========================================
# Python Loops & Control Flow Practice
# تمارين على الحلقات التكرارية والتحكم في التدفق
# ==========================================

# --- Task 1: Filtering Even Numbers | التمرين الأول: تصفية الأرقام الزوجية ---
# Goal: Print even numbers from 1 to 30 using 'continue'
# الهدف: طباعة الأرقام الزوجية من 1 إلى 30 باستخدام أمر الاستمرار
print("--- Even Numbers (1-30) ---")
for i in range(1, 31):
    if i % 2 != 0:
        # Skip odd numbers
        # تجاوز الأرقام الفردية
        continue
    else:
        print(i)

print("\n" + "="*30 + "\n") # Separator | فاصل

# --- Task 2: Number Classifier | التمرين الثاني: مصنف الأرقام ---
# Goal: Label each number as 'even' or 'odd' from 1 to 9
# الهدف: تصنيف كل رقم كزوجي أو فردي من 1 إلى 9
print("--- Even/Odd Classifier ---")
for i in range(1, 10):
    if i % 2 == 0:
        print(i, "even")
    else:
        print(i, "odd")

print("\n" + "="*30 + "\n") # Separator | فاصل

# --- Task 3: Skipping Multiples of 3 | التمرين الثالث: استثناء مضاعفات الرقم 3 ---
# Goal: Use a 'while' loop to print numbers while skipping multiples of 3
# الهدف: استخدام حلقة 'while' لطباعة الأرقام مع استثناء مضاعفات الرقم 3
print("--- Skipping Multiples of 3 ---")
i = 0
while i <= 29:
    i = i + 1
    if i % 3 == 0:
        # Skip numbers divisible by 3
        # تجاوز الأرقام التي تقبل القسمة على 3
        continue 
    else:
        print(i)
      
