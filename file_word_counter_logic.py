# --- Step 1: Secure File Opening | الخطوة 1: فتح الملف بأمان ---
user_input = input('Enter a file name: ')
try:
    file_handle = open(user_input)
except FileNotFoundError:
    print('Error: This file does not exist.')
    quit()

# --- Step 2: Content Processing | الخطوة 2: معالجة المحتوى ---
full_text = file_handle.read()
# Stripping whitespace and splitting into lines
lines = full_text.strip().splitlines()

word_master_list = []
for line in lines: 
    line_words = line.split()
    word_master_list.append(line_words)
    
# --- Step 3: Frequency Mapping | الخطوة 3: رسم خريطة التكرار ---
word_counts = {} # Professional name for 'muzan' dictionary
    
for group in word_master_list:
    for word in group:
        # Standardizing words to lowercase for better accuracy
        word = word.lower().strip('.,!?') 
        word_counts[word] = word_counts.get(word, 0) + 1

# --- Step 4: Extracting Final Stats | الخطوة 4: استخراج الإحصائيات ---
print(f'The number of unique words is: {len(word_counts)}')

most_frequent_value = None
most_frequent_word = None 
total_words_sum = 0

for word, value in word_counts.items():
    if most_frequent_value is None or value > most_frequent_value:
        most_frequent_value = value
        most_frequent_word = word
    total_words_sum += value  

# --- Final Results Output | مخرجات النتائج النهائية ---
print(f'The number of total words in this file is: {total_words_sum}')
print(f'The most common word is: "{most_frequent_word}"') 
print(f'Frequency of this word: {most_frequent_value}')

# Closing the file is a good practice
file_handle.close()

