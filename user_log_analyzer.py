import re

# معجم لتخزين بيانات كل مستخدم
users = {}

# طلب إدخال اسم الملف
inp = input('Enter a file name: ') 

# فتح الملف وقراءة الأسطر
try:
    with open(inp, 'r', encoding='utf-8') as log_file:
        # قراءة النص بالكامل وتقسيمه لأسطر
        lines = log_file.read().strip().splitlines()
except FileNotFoundError:
    print('Error: This file does not exist.')
    quit()

for line in lines:
    line = line.strip()
    if not line: continue # تخطي الأسطر الفارغة
    
    # 1. استخراج اسم المستخدم (يفترض أنه بعد النقطتين الأخيرتين)
    # النمط: يبحث عن كلمة بعد آخر نقطتين في السطر
    user_match = re.findall(r':([a-z0-9]+)$', line)
    
    # 2. استخراج حالة العملية (الرقم المكون من 3 خانات مثل 404 أو 200)
    status_match = re.findall(r' ([0-9]{3}) ', line)
    
    if user_match and status_match:
        user = user_match[0]
        status = int(status_match[0])
        
        # إذا المستخدم غير موجود، أنشئ له سجل
        if user not in users:
            users[user] = {'total': 0, 'failed': 0}
        
        # تحديث السجلات
        users[user]['total'] += 1
        
        # إذا كانت الحالة 400 أو أكثر تعتبر فشلاً (مثل أخطاء HTTP)
        if status >= 400:
            users[user]['failed'] += 1

# طباعة النتائج لكل مستخدم
print("\n--- User Activity Report ---")
for user, data in users.items():
    total = data['total']
    failed = data['failed']
    # حساب نسبة الفشل
    failure_rate = (failed / total) * 100
    print(f"User: {user:10} | Total: {total:3} | Failed: {failed:3} | Failure Rate: {failure_rate:5.1f}%")
  
