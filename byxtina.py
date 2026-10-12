import flet as ft
import os
from datetime import datetime
from abc import ABC, abstractmethod
class Currency(ABC):
    def __init__(self,code,name,rate):
        self._code=code
        self._name=name
        self._rate=rate
    @property
    def code(self):
        return self._code
    @code.setter
    def code(self,value):
        self._code=value
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,value):
        self._name=value
    @property
    def rate(self):
        return self._rate
    @rate.setter
    def rate(self,value):
        self._rate=value
    def get_info(self):
        pass
    def __eq__(self,other):
        return self._code==other._code
    def __repr__(self):
        return "Currency: "+self._code
    def __str__(self):
        return self._name
class Usd(Currency):
    def get_info(self):
        return self._name
    def __lt__(self,other):
        return self._rate<other._rate
    def __gt__(self,other):
        return self._rate>other._rate
class Session(ABC):
    def __init__(self,user):
        self._user=user
        self._time_in=datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        self._time_out=None
    @property
    def user(self):
        return self._user
    @user.setter
    def user(self,value):
        self._user=value
    @property
    def time_in(self):
        return self._time_in
    @time_in.setter
    def time_in(self,value):
        self._time_in=value
    @property
    def time_out(self):
        return self._time_out
    @time_out.setter
    def time_out(self,value):
        self._time_out=value
    def get_info(self):
        pass
    def close(self):
        self._time_out=datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    def __eq__(self,other):
        return self._user==other._user
    def __repr__(self):
        return "Session: "+self._user
    def __str__(self):
        return self._user
class UserSession(Session):
    def get_info(self):
        return self._user
    def __lt__(self,other):
        return self._user<other._user
    def __gt__(self,other):
        return self._user>other._user
class Mapper:
    def __init__(self):
        self.keys=[]
        self.values=[]
    def set(self,key,value):
        if key in self.keys:
            i=self.keys.index(key)
            self.values[i]=value
        else:
            self.keys.append(key)
            self.values.append(value)
    def get(self,key):
        if key in self.keys:
            i=self.keys.index(key)
            return self.values[i]
        else:
            return None
    def __eq__(self,other):
        return self.keys==other.keys
    def __repr__(self):
        return "Mapper"
    def __str__(self):
        return "Mapper"
class MyText(ft.Text):
    pass
class MyButton(ft.Button):
    pass
class MyTextField(ft.TextField):
    pass
class MyColumn(ft.Column):
    pass
class MyRow(ft.Row):
    pass
class MyContainer(ft.Container):
    pass
class MyDropdown(ft.Dropdown):
    pass
class MyDivider(ft.Divider):
    pass
class MyIcon(ft.Icon):
    pass
class MyCard(ft.Card):
    pass
class Convert:
    @staticmethod
    def perevesti(summa,rate_from,rate_to):
        if rate_from<=0:
            return 0
        return summa/rate_from*rate_to
cveta=Mapper()
cveta.set("green",ft.Colors.GREEN)
cveta.set("red",ft.Colors.RED)
valuti=[Usd("USD","Доллар",1.0),Usd("EUR","Евро",0.92),Usd("RUB","Рубль",92.5),Usd("GBP","Фунт",0.79),Usd("JPY","Йена",149.8),Usd("CNY","Юань",7.24),Usd("KZT","Тенге",450.0),Usd("TRY","Лира",27.5),Usd("BYN","Бел.рубль",3.25),Usd("UAH","Гривна",37.8)]
def sohranit_otchet(sessions):
    put="otchet.txt"
    f=open(put,"w",encoding="utf-8")
    f.write("+  | login | time_in | time_out |\n")
    f.write("|---|\n")
    for s in sessions:
        if s.time_out==None:
            t_out="---"
        else:
            t_out=s.time_out
        f.write("|---|\n")
        f.write("| "+s.user+" | "+s.time_in+" | "+t_out+" |\n")
    f.write("+\n")
    f.close()
def main(page:ft.Page):
    page.title="Обменник"
    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    page.bgcolor=ft.Colors.WHITE
    session=UserSession("student")
    label_result=MyText(value="",size=24,color=ft.Colors.GREEN,text_align=ft.TextAlign.CENTER)
    spisok1=[]
    spisok2=[]
    for v in valuti:
        spisok1.append(ft.DropdownOption(key=v.code,text=v.code))
        spisok2.append(ft.DropdownOption(key=v.code,text=v.code))
    dropdown_from=MyDropdown(width=120,options=spisok1,value="USD")
    dropdown_to=MyDropdown(width=120,options=spisok2,value="EUR")
    pole_from=MyTextField(label="Сумма",width=180)
    pole_to=MyTextField(label="Результат",width=180)
    def poschitat(e=None):
        if pole_from.value=="":
            label_result.value=""
            pole_to.value=""
            page.update()
            return
        try:
            summa=float(pole_from.value)
        except:
            label_result.value="Введи число"
            label_result.color=ft.Colors.RED
            page.update()
            return
        if summa<=0:
            label_result.value="Сумма должна быть больше 0"
            label_result.color=ft.Colors.RED
            page.update()
            return
        rate_from=1.0
        rate_to=1.0
        for v in valuti:
            if v.code==dropdown_from.value:
                rate_from=v.rate
            if v.code==dropdown_to.value:
                rate_to=v.rate
        result=Convert.perevesti(summa,rate_from,rate_to)
        pole_to.value=str(round(result,2))
        label_result.value=str(round(summa,2))+" "+dropdown_from.value+" = "+str(round(result,2))+" "+dropdown_to.value
        label_result.color=ft.Colors.GREEN
        page.update()
    pole_from.on_change=poschitat
    dropdown_from.on_change=poschitat
    dropdown_to.on_change=poschitat
    stroka1=MyRow(controls=[dropdown_from,pole_from],alignment=ft.MainAxisAlignment.CENTER,spacing=10)
    stroka2=MyRow(controls=[dropdown_to,pole_to],alignment=ft.MainAxisAlignment.CENTER,spacing=10)
    page.add(MyContainer(content=MyColumn(controls=[stroka1,stroka2,label_result],alignment=ft.MainAxisAlignment.CENTER,horizontal_alignment=ft.CrossAxisAlignment.CENTER,spacing=15),padding=30,alignment=ft.Alignment.CENTER))
    def on_close(e):
        session.close()
        sohranit_otchet([session])
    page.on_close=on_close
ft.run(main)