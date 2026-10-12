import flet as ft
from ui.widgets import (
    MyText, MyButton, MyTextField, MyColumn, MyRow,
    MyContainer, MyDropdown, MyDivider, MyIcon, MyCard
)
from models.session import UserSession
from services.convert import Convert
from services.report import sohranit_otchet
from data.rates import valuti


def main(page: ft.Page):
    page.title = "Обменник"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = ft.Colors.WHITE

    session = UserSession("student")
    label_result = MyText(value="", size=24, color=ft.Colors.GREEN,
                          text_align=ft.TextAlign.CENTER)

    spisok1 = []
    spisok2 = []
    for v in valuti:
        spisok1.append(ft.DropdownOption(key=v.code, text=v.code))
        spisok2.append(ft.DropdownOption(key=v.code, text=v.code))

    dropdown_from = MyDropdown(width=120, options=spisok1, value="USD")
    dropdown_to = MyDropdown(width=120, options=spisok2, value="EUR")
    pole_from = MyTextField(label="Сумма", width=180)
    pole_to = MyTextField(label="Результат", width=180)

    def poschitat(e=None):
        if pole_from.value == "":
            label_result.value = ""
            pole_to.value = ""
            page.update()
            return
        try:
            summa = float(pole_from.value)
        except:
            label_result.value = "Введи число"
            label_result.color = ft.Colors.RED
            page.update()
            return
        if summa <= 0:
            label_result.value = "Сумма должна быть больше 0"
            label_result.color = ft.Colors.RED
            page.update()
            return
        rate_from = 1.0
        rate_to = 1.0
        for v in valuti:
            if v.code == dropdown_from.value:
                rate_from = v.rate
            if v.code == dropdown_to.value:
                rate_to = v.rate
        result = Convert.perevesti(summa, rate_from, rate_to)
        pole_to.value = str(round(result, 2))
        label_result.value = (str(round(summa, 2)) + " " + dropdown_from.value +
                              " = " + str(round(result, 2)) + " " + dropdown_to.value)
        label_result.color = ft.Colors.GREEN
        page.update()

    pole_from.on_change = poschitat
    dropdown_from.on_change = poschitat
    dropdown_to.on_change = poschitat

    stroka1 = MyRow(controls=[dropdown_from, pole_from],
                    alignment=ft.MainAxisAlignment.CENTER, spacing=10)
    stroka2 = MyRow(controls=[dropdown_to, pole_to],
                    alignment=ft.MainAxisAlignment.CENTER, spacing=10)

    page.add(MyContainer(
        content=MyColumn(
            controls=[stroka1, stroka2, label_result],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15),
        padding=30,
        alignment=ft.Alignment.CENTER))

    def on_close(e):
        session.close()
        sohranit_otchet([session])

    page.on_close = on_close


ft.run(main)