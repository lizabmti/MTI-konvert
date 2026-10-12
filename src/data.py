import flet as ft
from models import Mapper, Usd


cveta=Mapper()
cveta.set("green",ft.Colors.GREEN)
cveta.set("red",ft.Colors.RED)

valuti=[Usd("USD","Доллар",1.0),Usd("EUR","Евро",0.92),Usd("RUB","Рубль",92.5),Usd("GBP","Фунт",0.79),Usd("JPY","Йена",149.8),Usd("CNY","Юань",7.24),Usd("KZT","Тенге",450.0),Usd("TRY","Лира",27.5),Usd("BYN","Бел.рубль",3.25),Usd("UAH","Гривна",37.8)]
