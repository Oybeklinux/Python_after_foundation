# Mavzu 3: Kivy da mobil dastur yozish
 
## Reja:
1. [Bilim](#1-bilim)
   - [1.1 Terminlar](#11-terminlar)
   - [1.2 O'qish uchun materiallar](#12-oqish-uchun-materiallar)
2. [Amaliyot. O'qituvchi](#2-amaliyot-oqituvchi)
3. [Amaliyot. O'quvchi](#3-amaliyot-oquvchi)

## 1. Bilim

### 1.1 Terminlar
```

```
### 1.2 O'qish uchun materiallar

## 2. Amaliyot. O'qituvchi
- [2.1 Kivyga kirish]
   - [2.1.1 Kivyni o'rnatish]
   - [2.1.2 Kivyda sodda dastur]
   - [2.1.3 KV fayl strukturasi]
- [2.2 Molashuvchan interfeys]
    - [2.2.1 BoxLayout]
    - [2.2.1 AnchorLayout]    
     
   - [DP: Density-independent Pixels]

**Reja:**

#### 2.1 Kivyga kirish
#### 2.1.1 Kivyni o'rnatish

```commandline
pip install kivy[base]
```
To'liq versiyasi
```commandline
pip install kivy[full]
```

**Kivy** - bu mobil qurilmalarga dastur yozish uchun kutubhonadir. Kv - bu dizaynni yasash uchun ishlatiladigan html ga o'xashash format
<br>
Ijobiy tarafi:
- Bitta kod bilan android va iPhone ga dastur tuzish mumkin

Salbiy tarafi:
- Dizayn o'zinikidaka bo'lmaydi
- Nativ til emas
- Hujjat yetarli emas
- Qo'llab quvvatlash jamiyati yetarli emas

#### 2.1.2 Kivyda sodda dastur

1. Kivy da eng sodda dastur yozing

```python
from kivy.app import App

class SoddaApp(App):
    pass

app = SoddaApp()
app.run()

```

Natija
<br>
![](images/img_4.png)

### 2.1.3 KV fayl strukturasi

2. Kivyda interfeys yasaymiz. Buning uchun sodda.kv nomli fayl yaratamiz

sodda.kv

``` text
MainWidget:


```

```python
from kivy.app import App
from kivy.uix.widget import Widget

class MainWidget(Widget):
    pass

class SoddaApp(App):
    pass

app = SoddaApp()
app.run()
```

Natija
<br>
![](images/img_4.png)

3. Kv faylga tugma qo'shamiz

sodda.kv
   
```text
MainWidget:

<MainWidget>:
    Button:
        text: "kivy dastur"
```

main.py

```python
from kivy.app import App
from kivy.uix.widget import Widget

class MainWidget(Widget):
    pass

class SoddaApp(App):
    pass

app = SoddaApp()
app.run()
```

Natija
<br>
![](images/img.png)

4. Tugma o'lchami va pozitsiyasini o'zgartiramiz

sodda.kv
```text
MainWidget:

<MainWidget>:
    Button:
        text: "kivy dastur"
        pos: 100, 200
        size: 300, 100
```

Natija
<br>
![](images/img_1.png)

5. px hamma ekranlarda har hil bo'ladi, natijada tugma telefonda boshqa, planshetda boshqa o'lcham bo'lishi mumkin. Shuning uhcun endi hammasida bir hil bo'lishi uchun dp o'lcham birligidan foydalanamiz

```text
MainWidget:

<MainWidget>:
    Button:
        text: "kivy dastur"
        pos: "100dp", "200dp"
        size: "300dp", "100dp"
```

Natija
<br>
![](images/img_2.png)

6. Ikkinchi tugmani qo'shamiz

```text
MainWidget:

<MainWidget>:
    Button:
        text: "kivy dastur"
        pos: "100dp", "200dp"
        size: "300dp", "100dp"

    Button:
        text: "kivy"
        pos: "100dp", "400dp"
        size: "300dp", "100dp"
```

Natija
<br>
![](images/img_3.png)

7. Endi yozuv (label) qo'shamiz

```text
MainWidget:

<MainWidget>:
    Button:
        text: "kivy dastur"
        pos: "100dp", "200dp"
        size: "300dp", "100dp"
    Button:
        text: "kivy"
        pos: "100dp", "400dp"
        size: "300dp", "100dp"
    Label:
        text: "label"
        pos: "100dp", "0dp"
        size: "300dp", "100dp"
        color: 1, 0 , 0, 1
```

Natija
<br>
![](images/img_6.png)



### 2.2 Molashuvchan interfeys
### 2.2.1 BoxLayout


Layout turlari

![](images/img_5.png)

Dastur interfeysi wijet yoki layout bo'ladi

<br>

8. BoxLayout ga misol

```python
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout


class BoxLayoutMisol(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "horizontal"
        b1 = Button(text="Matn 1")
        b2 = Button(text="Matn 2")
        self.add_widget(b1)
        self.add_widget(b2)

class MainWidget(Widget):
    pass

class SoddaApp(App):
    pass

app = SoddaApp()
app.run()

```

sodda.kv 
```text
BoxLayoutMisol:

<MainWidget>:
    Button:
        text: "kivy dastur"
        pos: "100dp", "200dp"
        size: "300dp", "100dp"
    Button:
        text: "kivy"
        pos: "100dp", "400dp"
        size: "300dp", "100dp"
    Label:
        text: "label"
        pos: "100dp", "0dp"
        size: "300dp", "100dp"
        color: 1, 0 , 0, 1
```

Natija
<br>
![](images/img_7.png)

9. Yuqoridagi misolni kv fayl bilan yasaymiz

```python
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout


class BoxLayoutMisol(BoxLayout):
    pass

class MainWidget(Widget):
    pass

class SoddaApp(App):
    pass

app = SoddaApp()
app.run()
```

kv.fayl

```text
BoxLayoutMisol:

<BoxLayoutMisol>:
    orientation: vertical
    Button:
        text: "Matn 1"
    Button:
        text: "Matn 2"       
        
<MainWidget>:
    Button:
        text: "kivy dastur"
        pos: "100dp", "200dp"
        size: "300dp", "100dp"
    Button:
        text: "kivy"
        pos: "100dp", "400dp"
        size: "300dp", "100dp"
    Label:
        text: "label"
        pos: "100dp", "0dp"
        size: "300dp", "100dp"
        color: 1, 0 , 0, 1
```

Natija
<br>
![](images/img_7.png)

Layout o'lcham va pozitsiyalarni o'zi boshqaradi. Shuning uchun ularni yozganda foydasi bo'lmaydi
10. kv faylda layoutda o'lchamlar bilan ishlash

```text
size_hint: 0.5, 0.5
```

10. kv faylda layoutda o'lchamlar bilan ishlash

```text
#size: "100dp", "100dp"
size_hint: None, None
```
11. Bo'yi, enini alohida berish

```text
    #size: "100dp", "100dp"
    size_hint: None, None
    width: "100dp"
    height: "100dp"
```

12. Bo'yini foizda, enini sonda berish

```text
    #size: "100dp", "100dp"
    size_hint: 0.5, None
    #width: "100dp"
    height: "100dp"
```

13. Gorizontal pozitsiyasini o'zgartirish
- Gorizontal hususiyatlar: x, center_x, right
- Vertikal hususiyatlar: y, center_y, left

```text
    #size: "100dp", "100dp"
    size_hint: 0.5, None
    #width: "100dp"
    height: "100dp"
    pos_hint: {"x": 0.5}   
```

14. Vertikal pozitsiyasini o'zgartirish
- Gorizontal hususiyatlar: x, center_x, right
- Vertikal hususiyatlar: y, center_y, left

```text
    #size: "100dp", "100dp"
    size_hint: .5, .5
    #width: "100dp"
    #height: "100dp"
    pos_hint: {"center_y": .5}   
```

15. Layout ichida Layout ishlatish

```text
BoxLayoutMisol:

<BoxLayoutMisol>:
    orientation: "vertical"
    Button:
        text: "Matn 1"
    BoxLayout:
        orientation: "horizontal"
        Button:
            text: "Matn 21"
        Button:
            text: "Matn 22"
        Button:
            text: "Matn 23"
    Button:
        text: "Matn 3"


```

Natija
<br>
![](images/img_8.png)

16. Layout orasida masofa qoldirish

```text
BoxLayoutMisol:

<BoxLayoutMisol>:
    orientation: "vertical"
    Button:
        text: "Matn 1"
    BoxLayout:
        orientation: "horizontal"
        spacing: "5dp"
        Button:
            text: "Matn 21"
        Button:
            text: "Matn 22"
        Button:
            text: "Matn 23"
    Button:
        text: "Matn 3"


```

Natija
<br>
![](images/img_9.png)

### 2.2.1 AnchorLayout

17. AnchorLayout ga misol

sodda.kv
```text
AnchorLayoutMisol:

<AnchorLayoutMisol>:
    Button:
        text: "AnchorLayout"

```
```python
from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout


class AnchorLayoutMisol(AnchorLayout):
    pass

class BoxLayoutMisol(BoxLayout):
    pass

class MainWidget(Widget):
    pass

class SoddaApp(App):
    pass

app = SoddaApp()
app.run()

```

Natija
<br>
![](images/img_10.png)

18. AnchorLayout da o'lchamni o'zgartiramiz

```text
AnchorLayoutMisol:

<AnchorLayoutMisol>:
    Button:
        text: "AnchorLayout"
        size_hint: .2,.1

```

Natija
<br>
![](images/img_11.png)

19. AnchorLayout da pozitsiya
```text
AnchorLayoutMisol:

<AnchorLayoutMisol>:
    #right, left,center
    anchor_x: "right"
    #bottom, top, center
    anchor_y: "top"
    Button:
        text: "AnchorLayout"
        size_hint: .2,.1

```

Natija
<br>
![](images/img_12.png)

### 3. Amaliyot. O'quvchi
Yuqoridagi kutubhonalardan foydalanib o'zingiz ijod qilib dastur yozing
