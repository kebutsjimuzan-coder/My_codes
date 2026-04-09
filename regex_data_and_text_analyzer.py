import re 

# --- Part 1: Numerical Data Extraction (Function) | الجزء 1: استخراج البيانات الرقمية ---
def extract_numeric_data(text_input):
    """Extracts and prints numeric values (like prices) from a string."""
    print("--- Extracting Numeric Values ---")
    # Finding all digits in the text
    numbers = re.findall('[0-9]+', text_input)
    count = 0
    for num in numbers:
        count += 1
        print(f"{count}. Value found: {num}")
    return numbers

# --- Part 2: File Text Analysis | الجزء 2: تحليل نصوص الملفات ---
def analyze_file_content():
    print("\n" + "="*30)
    file_name = input('Enter a file name for text analysis: ')
    
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            content = file.read()
    except FileNotFoundError:
        print('Error: This file does not exist.')
        return

    # Cleaning and splitting logic
    word_registry = {}
    lines = content.strip().splitlines()
    
    for line in lines:
        words = line.strip().split()
        for word in words:
            # Step 1: Normalize (Lowercase)
            word = word.lower()
            # Step 2: Clean symbols using Regex
            clean_word = re.sub(r'[^\w\s]', '', word).strip()
            
            # Step 3: Logic Filter (Ignore 'info' or empty strings)
            # تم وضع التنظيف قبل الفحص لضمان دقة التصفية
            if clean_word == 'info' or not clean_word:
                continue 
            
            # Step 4: Map frequency
            word_registry[clean_word] = word_registry.get(clean_word, 0) + 1

    # Sorting and Outputting Top Results
    print(f'Unique relevant words: {len(word_registry)}')
    
    # Converting dictionary to list of tuples for sorting
    frequency_list = sorted([(v, k) for k, v in word_registry.items()], reverse=True)

    print("\nTop 6 most frequent words:")
    for val, key in frequency_list[:6]:
        print(f"- {key}: {val} times")

# --- Execution | تنفيذ البرنامج ---
# Example text for the first function
sample_text = "Samsung: 700$, iPhone: 1100$, Nokia: 150$"
extract_numeric_data(sample_text)

# Running the file analyzer
analyze_file_content()

