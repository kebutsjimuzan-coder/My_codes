import re 

# 1. دالة تنظيف النص واستخراج الكلمات
def clean_word(text):
    text = text.lower().strip()
    # [a-z]+ : اقتناص الكلمات المكونة من حروف فقط
    text_clean = re.findall('[a-z]+', text)
    return text_clean
	
# 2. دالة البحث عن الكلمة/الكلمات الأطول
def find_longest_words(text_clean):
    max_len = 0
    list_long_words = []
    
    for word in text_clean: 
        # إذا وجدنا كلمة أطول من الطول الحالي الأقصى
        if len(word) > max_len:
            max_len = len(word)
            # إعادة ضبط القائمة لتبدأ بالكلمة الجديدة الأطول
            list_long_words = [word]
        # إذا كانت الكلمة مساوية لأقصى طول وصلنا له
        elif len(word) == max_len and max_len > 0:
            if word not in list_long_words: # منع التكرار داخل القائمة قبل العد
                list_long_words.append(word)
    
    return list_long_words

# 3. دالة حساب تكرار الكلمات الأطول وطباعتها
def print_word_stats(longest_list, full_text_list):
    # نعد تكرار الكلمات الأطول داخل النص الأصلي المنظف
    counts = {}
    for word in longest_list:
        counts[word] = full_text_list.count(word)

    print("\n" + "="*40)
    print("--- Longest Words Analysis ---")
    if not counts:
        print("No words found.")
    else:
        for word, frequency in counts.items():
            print(f"Word: '{word}'")
            print(f"Length: {len(word)} characters")
            print(f"Frequency in file: {frequency} times")
            print("-" * 20)
    print("="*40)

# 4. الدالة الرئيسية
def main():
    file_name = input("Enter a file name: ")
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            content = file.read()
            
        # تنفيذ العمليات
        cleaned_data = clean_word(content)
        longest_ones = find_longest_words(cleaned_data)
        
        # نرسل القائمة المنظفة بالكامل لنحسب تكرار الكلمات الأطول فيها
        print_word_stats(longest_ones, cleaned_data)
	
    except FileNotFoundError: 
        print("Error: This file does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
  
