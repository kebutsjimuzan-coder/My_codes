# ==========================================
# String Parsing & Data Extraction
# تحليل النصوص واستخراج البيانات
# ==========================================

# --- Task 1: Smart Input Filter | التمرين الأول: مرشح المدخلات الذكي ---
# A loop that ignores comments starting with '#' and stops at 'done'
# حلقة تتجاهل التعليقات التي تبدأ بـ '#' وتتوقف عند كلمة 'done'
print("--- Interactive Input Filter ---")
while True:
    user_line = input('> ')
    
    # Handling empty inputs to avoid errors with index [0]
    # معالجة المدخلات الفارغة لتجنب الأخطاء عند فحص أول حرف
    if len(user_line) == 0:
        continue
        
    if user_line[0] == '#':
        continue
    if user_line == 'done':
        break 
    print(user_line)
print('System Finished.')

print("\n" + "="*30 + "\n")

# --- Task 2: Domain Extractor | التمرين الثاني: مستخرج النطاقات ---
# Extracting and counting specific email domains from a text block
# استخراج وحساب عدد نطاقات بريد إلكتروني محددة من نص
print("--- Email Domain Counter ---")
example_count = 0
email_data = """
From: ali@example.com
From: sara@gmail.com
From: omar@example.com
From: test@yahoo.com
From: admin@example.com
"""

# Splitting the multi-line string into a list of lines
# تقسيم النص متعدد الأسطر إلى قائمة من الأسطر
lines = email_data.strip().split('\n')

for line in lines:
    # Finding the position of the domain start
    # إيجاد موقع بداية النطاق (بعد علامة @)
    at_position = line.find('@') + 1
    domain = line[at_position:].strip()
    
    if domain == 'example.com':
        example_count += 1
    print(f"Extracted Domain: {domain}")

print(f"Total 'example.com' instances: {example_count}")

print("\n" + "="*30 + "\n")

# --- Task 3: Score Reporter | التمرين الثالث: محلل تقرير الدرجات ---
# Parsing a string of subjects and scores to calculate the average
# تحليل نص يحتوي على مواد ودرجات لحساب المتوسط الحسابي
print("--- Academic Report Parser ---")
total_score = 0
report_string = "Math=78, Physics=88, Chemistry=91"

# Splitting by comma to separate subjects
# التقسيم باستخدام الفاصلة لفصل المواد عن بعضها
subject_entries = report_string.split(',')

for entry in subject_entries:
    # Locating the score after the '=' sign
    # تحديد موقع الدرجة بعد علامة '='
    equal_sign_pos = entry.find('=') + 1
    score = int(entry[equal_sign_pos:])
    print(f"Subject Score: {score}")
    total_score += score 

subject_count = len(subject_entries)
average_score = total_score / subject_count
print(f"Average: {average_score:.2f} | Total: {total_score}")

