# ==========================================
# Python Loop Control & Logic Markers
# تمارين التحكم في الحلقات والعلامات المنطقية
# ==========================================

# --- Task 1: Replacing Multiples with Markers | التمرين الأول: استبدال المضاعفات بعلامات ---
# Goal: Replace every 4th number with "X" using a while loop
# الهدف: استبدال كل رابع رقم بالحرف "X" باستخدام حلقة while
print("--- Number Pattern with 'X' Marker ---")
i = 0 
while i <= 29:
    i = i + 1
    if i % 4 == 0:
        # Print "X" instead of the number if divisible by 4
        # طباعة "X" بدلاً من الرقم إذا كان يقبل القسمة على 4
        print("X")
    else:
        print(i)

print("\n" + "="*30 + "\n")

# --- Task 2: Skipping Multiples of 3 | التمرين الثاني: استثناء مضاعفات الرقم 3 ---
# Goal: Print numbers from 2 to 20, skipping those divisible by 3
# الهدف: طباعة الأرقام من 2 إلى 20 مع استثناء الأرقام التي تقبل القسمة على 3
print("--- Skipping Multiples of 3 (Range 2-20) ---")
for i in range(2, 21):
    if i % 3 != 0:
        print(i)

print("\n" + "="*30 + "\n")

# --- Task 3: Loop Interruption (Break Logic) | التمرين الثالث: إيقاف الحلقة (منطق الـ Break) ---
# Goal: Stop the loop when reaching a specific number (8)
# الهدف: إيقاف الحلقة عند الوصول لرقم معين (8)
print("--- Stop Loop at 7 (Corrected from 'stop' to 'break') ---")
i = 1
while i <= 10:
    print(i)
    i = i + 1
    if i == 8:
        # 'break' is the correct keyword to stop a loop in Python
        # كلمة 'break'  لإيقاف الحلقة في بايثون
        break 

print("\n" + "="*30 + "\n")

# --- Task 4: Extended Break Logic | التمرين الرابع: منطق الإيقاف الممتد ---
# Goal: Stop a long loop (up to 50) at a specific point (37)
# الهدف: إيقاف حلقة طويلة (تصل لـ 50) عند نقطة محددة (37)
print("--- Early Break at 36 ---")
i = 1
while i <= 50:
    print(i)
    i = i + 1
    if i == 37:
        break
      
