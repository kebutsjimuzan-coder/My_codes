# دالة لمعرفة أطول سطر 
def find_longest_line(lines):
    longest_line = None
    list_longest_line = []
    
    for line in lines:
        x_line = line.strip().split()
        
        # المقارنة بين طول السطر الحالي وأطول سطر مخزن
        if longest_line == None or len(x_line) > len(longest_line):
            longest_line = x_line
            list_longest_line = []
            list_longest_line.append(line)
            
        elif longest_line != None and len(x_line) == len(longest_line):
            list_longest_line.append(line)
            
    return list_longest_line 
	
# دالة لحساب عدد الكلمات في الأسطر الأطول 
def count_words_in_line(list_longest_line):
    result_dict = {}
    for line in list_longest_line:
        x_line = line.strip().split()
        count_word = len(x_line)
        # السطر هو المفتاح وعدد الكلمات هو القيمة
        result_dict[line] = count_word		
    return result_dict

# بداية البرنامج الأساسي
file_name = input("Enter a file name: ")	

try:
    # فتح الملف (أضفنا utf-8 فقط ليدعم ملفاتك العربية)
    with open(file_name, 'r', encoding='utf-8') as file:
        text = file.read()
        lines = text.splitlines()

    # استدعاء الدوال وتخزين النتائج في متغيرات
    longest_lines = find_longest_line(lines)	
    finally_dict = count_words_in_line(longest_lines)
    
    # التأكد من وجود نتائج وطباعتها
    if len(longest_lines) == 0:
        print("الملف فارغ أو لا يحتوي على كلمات")
    else:
        for content, count in finally_dict.items():
            print("عدد الكلمات:", count, "| السطر:", content)
			
except FileNotFoundError:
    print("Error: this file does not exist")
except Exception as e:
    print("An error occurred:", e)
  
