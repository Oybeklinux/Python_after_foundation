# Mavzu 1: Vazifalarni avtomatlashtirish
 
## Reja:
1. [Bilim](#1-bilim)
   - [1.1 Terminlar](#11-terminlar)
   - [1.2 O'qish uchun materiallar](#12-oqish-uchun-materiallar)
2. [Amaliyot. O'qituvchi](#2-amaliyot-oqituvchi)
3. [Amaliyot. O'quvchi](#3-amaliyot-oquvchi)

## 1. Bilim

### 1.1 Terminlar
```
pyinputplus - foydalanuvchi kiritgan ma'lumotni tekshirib olib beradigan funksiyalar moduli
```
### 1.2 O'qish uchun materiallar
- [1.1 pyinputplus moduli]()

## 2. Amaliyot. O'qituvchi

**Reja:**
- [2.1 pyinputplus]()
- [2.2 os va shutil]()

### 2.1 pyinputplus
[pyinputplus](https://github.com/asweigart/pyinputplus) - foydalanuvchi tarafidan kiritilgan qiymatni xatolikka tekshirib, to'g'ri qiymatni qaytaradigan funksiyalar moduli
1. inputNum funksiyasiga misol. Ikki son yig'indisini hisoblash dasturi

```python
import pyinputplus as plus

a = plus.inputNum("a = ")
b = plus.inputNum("b = ")
print(f"a + b = {a + b}")
```
```text
a = d
'd' is not a number.
a = 2.2
b = 3
a + b = 5.2
```

2. inputInt funksiyasiga misol. Ikki son yig'indisini hisoblash dasturi

```python
import pyinputplus as plus

a = plus.inputInt("a = ")
b = plus.inputInt("b = ")
print(f"a + b = {a + b}")
```
```text
a = w
'w' is not an integer.
a = 2.2
'2.2' is not an integer.
a = 3
b = 5
a + b = 8
```
3. inputDate funksiyasiga misol
```python
import pyinputplus as plus

sana = plus.inputDate("Sanani kiriting (kun/oy/yil): ")
print(type(sana), sana)
```
```text
Sanani kiriting (kun/oy/yil): 12.2.2022
'12.2.2022' is not a valid date.
Sanani kiriting (kun/oy/yil): 12/2/2022
<class 'datetime.date'> 2022-12-02
```
4. inputEmail funkisyasi:
```python
import pyinputplus as plus

email = plus.inputEmail("Elektron manzilni kiriting: ")
print(type(email), email)
```
Natija

```text
Elektron manzilni kiriting: 23
'23' is not a valid email address.
Elektron manzilni kiriting: wew
'wew' is not a valid email address.
Elektron manzilni kiriting: oybek@gmail
'oybek@gmail' is not a valid email address.
Elektron manzilni kiriting: oybek@gmail.com
<class 'str'> oybek@gmail.com
```
5. inputYesNo funskiyasi:
```python
import pyinputplus as plus

ha_yoq = plus.inputYesNo("Amerika poytaxti New York shundaymi? (Ha/Yoq): ", yesVal="Ha", noVal="Yoq")
print(type(ha_yoq), ha_yoq)
```
Natija
```text
Amerika poytaxti New York shundaymi? (Ha/Yoq): yes
'yes' is not a valid Ha/Yoq response.
Amerika poytaxti New York shundaymi? (Ha/Yoq): yoq
<class 'str'> Yoq
```
6. inputTime funksiyasi:
```python
import pyinputplus as plus

time = plus.inputTime("Uchadigan vaqtni kiriting (soat:minut): ")
print(type(time), time)
```
Natija
```text
Uchadigan vaqtni kiriting (soat:minut): 23:59
<class 'datetime.time'> 23:59:00
```
7. inputMenu, inputNum, inputDate funksiyasiga misol. 

```python
import pyinputplus as plus
print("== Mahsulot kiritish ==")
mevalar = {}
meva = plus.inputMenu(["olma", "anor", "banan", "bodring"], prompt="Mahsulotlardan birini tanlang\n")
narxi = plus.inputNum(f"{meva}ning narxi: ")
sanasi = plus.inputDate(prompt="Do'konga qachon keldi (10/31/2022): ", formats=["%d-%m-%y"],limit=2)
mevalar[meva] = {
    "narxi": narxi,
    "sanasi": sanasi
}
print(mevalar)
```
```text
Meva nomini kiriting
* olma
* anor
* banan
* bodring
2
'2' is not a valid choice.
Meva nomini kiriting
* olma
* anor
* banan
* bodring
olma
Tanlangan meva: olma
```

### 2.2 os va shutil
os va shutil operatsion tizim va uning fayllar strukturasiga bog'liq bo'lgan funksiyalar mavjud 

8. os.chdir, os.getcwd, os.listdir funksiylariga misol

```python
import os

# dastur ishga tushirilgan papka yo'li 
print(os.getcwd())
# usha papkadagi fayl va papkalar ro'yxati
print(os.listdir())
# bitta tepadagi papkaga o'tish
os.chdir("..")
print(os.getcwd())
print(os.listdir())
os.chdir("..")
print(os.getcwd())
```
9. shutil.copy(), shutil.move()
```python
import os
import shutil
# yangi papka och
os.mkdir("test")
# yangi fayl yoz
with open("test.txt", "x"): pass
# ko'rsatilgan faylni boshqa papkaga ko'chrish
shutil.copy("test.txt", "test")
```
### 2.2 Request
9. Veb sahifa kodini olib, faylga yozib olish
```python
import requests

url = "https://maxway.uz/"
response = requests.get(url)

with open("tmp","w", encoding="utf-8") as file:
    file.write(response.text)
```

10. Sahifadan faqat rasm havolasini olish
```python
import requests
import re

url = "https://maxway.uz/"
response = requests.get(url)
images = []
for link in re.findall('<img\s*src="([^"]*)"', response.text):
    images.append(link)

with open("tmp","w", encoding="utf-8") as file:
    file.write("\n".join(images))
```

11. Sahifadan rasmlarni yuklab olish
```python
import requests
import shutil

images = [
'https://cdn.delever.uz/delever/a261e78b-7717-4df3-94f7-5347e8342cc8',
'https://cdn.delever.uz/delever/2c9fa151-c14e-483d-bbab-1ea7e36a92b0',
'https://cdn.delever.uz/delever/56838918-0f05-45ad-b23d-685e5e5a1099',
'https://cdn.delever.uz/delever/210650ec-fc8a-4d14-b1c3-aa9ac31e1f9f',
'https://cdn.delever.uz/delever/937fa7ef-2def-4c4a-8ff8-7cf3a36dd720',
'https://cdn.delever.uz/delever/8f7bdd9b-808b-46dd-bec0-f2c0efb217f4',
'https://cdn.delever.uz/delever/81e32413-70dd-47d2-ba0d-b30f5bbdcd06',
'https://cdn.delever.uz/delever/1fb3d07b-4afb-4505-86da-abbf0804f8fd',
]
i = 0
for image_link in images:
    response = requests.get(image_link, stream=True)
    i += 1
    extension = response.headers.get('Content-Type').replace('image/','')
    with open(f"{i}.{extension}", "wb") as file:
        shutil.copyfileobj(response.raw, file)
    del response
```
12. 'https://kudapizza.herokuapp.com/pizzas/' API berilgan. Shu APIdan name_ru, price_ru ni ekraga chiqaramiz
```python
import requests
import json

url = 'https://kudapizza.herokuapp.com/pizzas/'
html = requests.get(url)

obj = json.loads(html.content)
for product in obj:
    print(f"\n\nNomi: {product['name_ru']}\nNarxi: {product['price']}")
```
13. Mavjud Excelda faylni ochib ikki qatorga yozuv kiriting
<br>
![](images/img.png)
<br>

```commandline
pip install openpyxl
```

```python
import openpyxl

hujjat = openpyxl.load_workbook("telefonlar.xlsx")
sahifa = hujjat['telefonlar']
sahifa["C2"] = "3000"
sahifa["C3"] = "4000"
sahifa["C4"] = "5000"
hujjat.save("telefonlar.xlsx")
```
Natija
![](images/img_1.png)

14. Excelda yozilgan havolalarni browserda oching
```python
import webbrowser
import openpyxl
hujjat = openpyxl.load_workbook("havolalar.xlsx")
# Sheet1 sahifasi
lines = hujjat['Sheet1']

for line in lines:
    # qator
    for cell in line:
        # yacheyka
        link = cell.value
        if "https" in link:
            webbrowser.open(link)            
hujjat.close()
```
Natija

![](images/img_2.png)


## 2. Amaliyot. O'quvchi
1. inputMenu, inputNum, inputDate, inputTime, inputYesNo, inputEmail funksiyalaridan foydalanib o'zingiz dastur yozing. Ijod qiling
2. Quyidagicha menyu bo'lsin, so'ng menyu mos funksiyalar yozib chiqing
```text
1. Ko'rish
2. Ko'chirish
3. O'chirish
4. Yangi papkani ochish
5. Yangi fayl ochish
```
3. Sahifadan hamma rasmlarni yuklab olish
4. 'https://kudapizza.herokuapp.com/pizzas/' APIdan mahsulot nomi, narxi, rasmini yuklab, faylda JSON formatda saqlang. Faylda rasm havolasi saqlanadi, yuklangan rasmlar alohida images degan papkada bo'lsin.
5. 'https://kudapizza.herokuapp.com/pizzas/' APIdan mahsulot nomi ,sanasi, rasm havolasi, kategoruyasini yuklab, excelda saqlang. <br>Agar excel fayl ochiq bo'lsa, dasturda xatolik bo'ladi, shuni oldini oling
6. 5-masalada bajarilgandan hosil bo'lgan faylni ochib, ichidagi har bir rasmni borwserda ochsin