# ==========================================
# File Handling & Content Filtering
# التعامل مع الملفات وتصفية المحتوى
# ==========================================

# --- Task 1: Targeted Keyword Search | التمرين الأول: البحث عن كلمة محددة ---
# Reading a file line by line to save memory and finding a specific name
# قراءة الملف سطراً بسطر لتوفير الذاكرة والبحث عن اسم محدد
print("--- Keyword Search (Ali) ---")
file_name = input('Enter the file name to search for "ali": ')

try:
    # Opening the file in read mode
    # فتح الملف في وضع القراءة
    with open(file_name, 'r') as file_handle:
        for line in file_handle:
            # Checking if the keyword exists in the current line
            # التحقق مما إذا كانت الكلمة المفتاحية موجودة في السطر الحالي
            if 'ali' in line:
                print(line.strip())
except FileNotFoundError:
    print(f"Error: The file '{file_name}' does not exist.")
    # We use return or a flag instead of quit() for better flow
    # نستخدم معالجة الأخطاء بدلاً من الإغلاق المفاجئ للبرنامج

print("\n" + "="*30 + "\n")

# --- Task 2: Python Content Extractor | التمرين الثاني: مستخرج محتوى بايثون ---
# Loading full file content and filtering lines containing 'Python'
# تحميل محتوى الملف بالكامل وتصفية الأسطر التي تحتوي على كلمة 'Python'
print("--- Python Content Filter ---")
try:
    target_file = input('Enter a file name to filter Python-related lines: ')
    
    with open(target_file, 'r') as f_handle:
        # Reading all lines and stripping whitespace
        # قراءة جميع الأسطر وتنظيف المسافات الزائدة
        content_lines = f_handle.read().strip().splitlines()
        
        for line in content_lines:
            if 'Python' in line:
                print(line)
except FileNotFoundError:
    print("Error: The file was not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")


