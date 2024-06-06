import flet as ft
from flet import *


def home_view(page: ft.Page):
    page.title = "Control de Inventarios"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = "#4d5377"

    home_container = ft.View(
        "/home",
        controls=[
            ft.Column(
                controls=[
                    ft.Row(
                        controls=[
                            ft.Text(
                                "Control de Inventarios",
                                size=40,
                                color="BLACK",
                                weight="bold",
                                italic=True,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        expand=False,
                        height=200,
                    ),
                    ft.Row(
                        controls=[
                            _create_card(
                                "Auditoria de tiendas",
                                "Espacio para la auditoria de inventarios en tienda",
                                "assets/images/auditoria.png",
                                lambda e: page.go("/home/store"),
                            ),
                            _create_card(
                                "Modificacion de Codigos",
                                "Espacio para realizar modificaciones a los codigos de productos",
                                "assets/images/mod_code.png",
                                lambda e: page.go("/home/stock"),
                            ),
                            _create_card(
                                "Nuevos Codigos",
                                "Captura y asignacion de nuevos codigos a los productos",
                                "assets/images/new_code.png",
                                lambda e: page.go("/home/stock"),
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_AROUND,
                        expand=True,
                    ),
                    ft.Row(
                        controls=[
                            ft.FilledButton(
                                "Cerrar Sesion", on_click=lambda e: page.go("/login")
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                        expand=False,
                    ),
                ],
                expand=True,
            )
        ],
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )
    return home_container


def _create_card(tittle, description, image, click):
    return ft.Card(
        content=ft.Column(
            [
                ft.Container(
                    content=ft.Text(tittle, size=18, weight="bold"),
                    padding=10,
                    alignment=ft.alignment.center,
                ),
                ft.Container(
                    content=ft.Text(
                        description,
                        size=12,
                    ),
                    padding=10,
                ),
                ft.Container(
                    content=ft.Image(src=image, width=200, height=200),
                    padding=10,
                    alignment=ft.alignment.center,
                    on_click=click,
                ),
            ],
            spacing=10,
        ),
        elevation=4,  # Elevation defines the shadow depth
        margin=20,  # Margin around the card
        width=300,  # Width of the card
        height=400,  # Height of the card
    )
