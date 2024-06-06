import flet as ft
from flet import *


def stock_view(page: ft.Page):
    from items.items import display_items

    return ft.View(
        "/home/stock",
        controls=[
            ft.Text("Stock"),
            ft.Row(
                [
                    display_items(
                        ft.CrossAxisAlignment.START,
                        "Agregar Nuevos Productos",
                        lambda e: page.go("/home/stock/new_barcode"),
                    ),
                    display_items(
                        ft.CrossAxisAlignment.CENTER,
                        "Modificar productos",
                        lambda e: page.go("/home/stock/new_barcode"),
                    ),
                    display_items(
                        ft.CrossAxisAlignment.END,
                        "Baja de productos",
                        lambda e: page.go("/home/stock/new_barcode"),
                    ),
                ],
                spacing=100,
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
            ),
            ft.Row(
                controls=[
                    ft.ElevatedButton("Volver", on_click=lambda e: page.go("/home")),
                    ft.ElevatedButton("Logout", on_click=lambda e: page.go("/login")),
                ],
                alignment=ft.MainAxisAlignment.SPACE_EVENLY,
            ),
        ],
    )
