import re

# --- Step 1: File Access | الخطوة 1: الوصول للملف ---
file_path = input('Enter a file name: ')

try:
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
except FileNotFoundError:
    print('Error: This file does not exist.')
    quit()

# --- Step 2: Data Cleaning & Processing | الخطوة 2: تنظيف ومعالجة البيانات ---
# Converting to lowercase and splitting into words
raw_words = content.lower().split()

word_registry = {} # Dictionary to store frequencies
longest_word = ''  # Variable to track the longest word

# Common stop words to ignore | كلمات شائعة يتم تجاهلها
stop_words = {'info', 'is', 'the', 'a', 'and', 'to', 'in', 'of'}

for word in raw_words:
    # Using Regex to remove any character that is NOT a letter or number
    # [^\w\s] means: replace anything that is not a word character or space
    clean_word = re.sub(r'[^\w\s]', '', word)
    
    # Skip if the word is a stop word or empty
    if clean_word in stop_words or not clean_word:
        continue
    
    # Track the longest word
    if len(clean_word) > len(longest_word):
        longest_word = clean_word
    
    # Count frequency using dictionary
    word_registry[clean_word] = word_registry.get(clean_word, 0) + 1

# --- Step 3: Statistical Output | الخطوة 3: المخرجات الإحصائية ---
print("\n" + "="*30)
print(f'Longest word found: "{longest_word}" ({len(longest_word)} characters)')
print(f'Unique relevant words: {len(word_registry)}')
print(f'Total words processed: {sum(word_registry.values())}')

# --- Step 4: Advanced Sorting | الخطوة 4: فرز متقدم ---
# Sorting words by frequency in descending order
# ترتيب الكلمات حسب التكرار من الأكثر للأقل
top_words = sorted([(v, k) for k, v in word_registry.items()], reverse=True)

print('\

