# إنشاء دالة لمعرفة أطول سطر يحتوي على كلمة محددة
def find_longest_line(lines, word):
    longest_line = None
    # قائمة لتخزين الأسطر التي تحقق الشرط وتكون هي الأطول
    list_longest_line = []
    
    for line in lines:
        x_line = line.strip().split()
        
        # التأكد أولاً من أن الكلمة المطلوبة موجودة في السطر الحالي
        if word in x_line:
            # شرط تعيين أطول سطر (أو تحديثه إذا وجدنا أطول منه)
            if longest_line == None or len(x_line) > len(longest_line):
                longest_line = x_line
                # تفريغ القائمة لأننا وجدنا سطرًا أطول يحقق الشرط
                list_longest_line = []
                list_longest_line.append(line)
                
            # إذا كان السطر مساوياً في الطول لأطول سطر وجدناه سابقاً وكلاهما يحتوي على الكلمة
            elif len(x_line) == len(longest_line):
                list_longest_line.append(line)
                
    return list_longest_line 
	
# إنشاء دالة لحساب عدد الكلمات في الأسطر الناتجة
def count_words_in_line(list_longest_line):
    result_dict = {}
    for line in list_longest_line:
        x_line = line.strip().split()
        count_word = len(x_line)
        # تخزين السطر كمفتاح وعدد كلماته كقيمة
        result_dict[line] = count_word		
    return result_dict

# القسم الرئيسي للبرنامج
file_name = input("Enter a file name: ")	
try:
    # فتح الملف (استخدام utf-8 يضمن دعم اللغة العربية)
    with open(file_name, 'r', encoding='utf-8') as file:
        text = file.read()
        lines = text.splitlines()
        
    word = input("Enter a word for searching about it: ")
    
    # تنفيذ الدوال بالتسلسل
    longest_lines = find_longest_line(lines, word)	
    finally_dict = count_words_in_line(longest_lines)
    
    # التأكد من وجود نتائج
    if not longest_lines:
        print(f"لم يتم العثور على أسطر تحتوي على الكلمة: '{word}'")
    else:
        print("\n--- النتائج (أطول الأسطر التي تحتوي على الكلمة) ---")
        for content, count in finally_dict.items():
            print(f"عدد الكلمات: {count} | السطر: {content}")
			
except FileNotFoundError:
    print("Error: this file does not exist")
except Exception as e:
    print(f"An error occurred: {e}")
  
