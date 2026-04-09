# ==========================================
# Advanced Text Analyzer & Word Counter
# محلل النصوص المتقدم ومعالج الكلمات
# ==========================================

def analyze_text_file(): 
    """Analyzes a text file to count words and find the most frequent word."""
    # Getting the file name from the user
    file_name = input('Enter the file name to analyze: ')

    try:
        # Opening and reading the entire file content
        with open(file_name, 'r', encoding='utf-8') as file_handle:
            raw_text = file_handle.read()
    except FileNotFoundError: 
        print(f"Error: The file '{file_name}' does not exist.")
        return # Use return to exit the function safely

    # --- Data Cleaning & Preparation | تنظيف وتحضير البيانات ---
    # Stripping whitespace and splitting into lines
    lines = raw_text.strip().splitlines()
    
    word_list = []
    for line in lines:
        # Splitting each line into individual words
        words_in_line = line.split()
        word_list.append(words_in_line)
    
    # --- Frequency Analysis | تحليل التكرار باستخدام القاموس ---
    word_frequency = {} # Professional name for 'muzan' dictionary
    total_word_count = 0
    
    for words in word_list: 
        for word in words:
            # Cleaning the word: Lowercase and stripping punctuation
            clean_word = word.lower().strip('.,!?":;()')
            
            # Counting unique words using a dictionary
            # حساب الكلمات الفريدة باستخدام القاموس
            word_frequency[clean_word] = word_frequency.get(clean_word, 0) + 1
            total_word_count += 1
            
    # --- Extracting Statistics | استخراج الإحصائيات 

