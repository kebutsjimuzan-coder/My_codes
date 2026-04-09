import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup 

# الموقع المستهدف (موقع شهير للتدريب على كشط البيانات)
url = "http://books.toscrape.com/"
 
# فتح الرابط وقراءة محتوى HTML
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# استخراج جميع الأوعية التي تحتوي على بيانات الكتب
data_of_books = soup.find_all('article', class_='product_pod')

# طباعة الهيدر (رأس الجدول) بتنسيق منظم
print(f"{'name_of_book':<25} | {'price_of_book':<10} | {'link_of_book'}")
print(f"{'_'*25} | {'_'*10} | {'_'*25}")

# حلقة للمرور على كل كتاب واستخراج تفاصيله
for book in data_of_books:
    # استخراج السعر
    price_of_book = book.find('p', class_='price_color').text
    # استخراج العنوان الكامل من خاصية title
    name_of_book = book.h3.a['title']
    # استخراج الرابط الخاص بالكتاب
    link_of_book = book.h3.a['href']
    
    # طباعة البيانات بشكل محاذٍ ومنظم
    # تم قص الاسم الطويل لـ 20 حرفاً لضمان تناسق الجدول
    print(f"{name_of_book[:20]:<25} | {price_of_book:<10} | {link_of_book}")
  
