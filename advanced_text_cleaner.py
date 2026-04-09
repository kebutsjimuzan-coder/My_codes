import re 

# 1. دالة تنظيف النص واستخراج الكلمات المكونة من حروف فقط
def get_clean_words(text):
    text = text.lower().strip()     
    # [a-z]+ : يضمن التقاط الكلمات المكونة من حروف فقط ويتجاهل الأرقام والرموز
    clean_list = re.findall(r'[a-z]+', text)
    return clean_list

# 2. دالة تصفية الكلمات حسب الطول (أكثر من 3 أحرف)
def filter_long_words(word_list):
    # استخدام List Comprehension يجعل الكود أسرع وأكثر أناقة في بايثون
    return [word for word in word_list if len(word) > 3]

# 3. دالة حساب الإحصائيات (الكلمات الفريدة والإجمالي)
def calculate_stats(word_list):
    counts = {}
    for word in word_list:
        counts[word] = counts.get(word, 0) + 1
    
    print("-" * 30)
    print(f"Unique words (>3 chars): {len(counts)}")
    print(f"Total words processed:   {sum(counts.values())}")
    print("-" * 30)
    return counts  
	
# 4. دالة عرض الكلمات العشر الأكثر شيوعاً
def report_top_frequencies(counts_dict):
    # ترتيب تنازلي بناءً على التكرار
    top_list = sorted([(v, k) for (k, v) in counts_dict.items()], reverse=True)
    
    print("\n__ Top 10 Most Frequent Words __")
    for count, word in top_list[:10]:
        print(f"{word:15} | Frequency: {count}")
			
def main():
    file_name = input("Enter the file name: ")
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            raw_text = file.read()
            
        # تنفيذ العمليات بالتسلسل (Pipeline)
        words = get_clean_words(raw_text)
        filtered_words = filter_long_words(words)
        word_counts = calculate_stats(filtered_words)
        
        if word_counts:
            report_top_frequencies(word_counts)
        else:
            print("No words longer than 3 characters were found.")
			
    except FileNotFoundError:
        print("Error: This file does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
  
