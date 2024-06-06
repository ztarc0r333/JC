import flet as ft
from flet import *


def store_view(page: ft.Page):

    add_product_container = ft.View(
        "/home/store",
        controls=[
            ft.Column(
                controls=[
                    ft.Text("Portal punto de venta", size=20, color="BLACK"),
                    ft.Column(
                        controls=[
                            ft.Row(
                                controls=[
                                    _create_card(
                                        "Nueva Venta",
                                        "Ventas de mostrador",
                                        ft.icons.POINT_OF_SALE,
                                    ),
                                    _create_card(
                                        "Historial de ventas",
                                        "Datos historicos",
                                        ft.icons.STORAGE,
                                    ),
                                    _create_card(
                                        "Corte de caja",
                                        "cierre",
                                        ft.icons.BOOK_ONLINE_OUTLINED,
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                expand=True,
                            ),
                            ft.Row(
                                controls=[
                                    ft.FilledButton(
                                        "Volver", on_click=lambda e: page.go("/home")
                                    ),
                                    ft.FilledButton(
                                        "Logout", on_click=lambda e: page.go("/login")
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                # expand=True,
                            ),
                        ],
                        expand=True,
                    ),
                ],
                expand=True,
            ),
        ],
    )

    return add_product_container


def _create_card(title, subtitle, icon):
    return ft.Card(
        content=ft.Container(
            content=ft.Column(
                controls=[
                    ft.ListTile(
                        leading=ft.Icon(icon),
                        title=ft.Text(title),
                        subtitle=ft.Text(subtitle),
                        on_click="click",
                    ),
                ]
            ),
            width=300,
            height=200,
            padding=25,
            border_radius=10,
            bgcolor="#4d5377",
            alignment=ft.alignment.center,
        )
    )
