# إنشاء دالة للبحث عن كلمة 
def search_word(lines, target):
    # إنشاء قاموس لإدخال الأسطر و الأرقام فيه
    result_dict = {}
    # إنشاء قائمة لرقم السطور الكلمة 
    line_numbers = []
    # إنشاء قائمة للسطور التي تحتوي الكلمة 
    line_contents = []
    
    count = 0
    for line in lines:
        count += 1	
        # التأكد من وجود الكلمة في السطر 
        if target in line:
            line_numbers.append(count)
            line_contents.append(line)
            
    # دمج القائمتين في قاموس 
    # تم تصحيح طريقة إنشاء القاموس لتعمل برمجياً بشكل سليم
    for i in range(len(line_numbers)):
        result_dict[line_numbers[i]] = line_contents[i].strip()

    return result_dict

# الطلب من المستخدم أن يدخل ملفاً 
file_name = input("Enter a file name: ")

try:
    # فتح الملف عبر try لتجنب الخطأ 
    with open(file_name, 'r', encoding='utf-8') as file:
        # استخدام readlines للحصول على قائمة أسطر جاهزة
        lines = file.readlines()
        
    word = input("Enter a word for searching about it: ")

    # استدعاء الدالة 
    search_result = search_word(lines, word)
    
    # طباعة النتائج
    if search_result:
        print(search_result)
    else:
        print("Word not found.")
			
except FileNotFoundError:
    print("This file does not exist")
    
except Exception as e:
    print(f"An error occurred: {e}")
  
