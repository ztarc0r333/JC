import flet as ft
from flet import *
from controller.scanner_control import read_barcode


def new_barcode_view(page: Page):

    page.title = "New Barcode"

    return ft.View(
        "/home/stock/new_barcode",
        controls=[
            ft.Column(
                controls=[
                    ft.Text(
                        "Control de Codigos - Nuevo Producto",
                        size=20,
                        color="BLACK",
                    ),
                    ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Row(
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    controls=[
                                        ft.TextField(
                                            label="Nombre del producto",
                                            border="underline",
                                            width=300,
                                            read_only=False,
                                        ),
                                        ft.Icon(
                                            name=ft.icons.DRAW_OUTLINED,
                                            color="BLACK",
                                            tooltip="Campo Requerido",
                                        ),
                                    ],
                                ),
                                ft.Row(
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    controls=[
                                        ft.TextField(
                                            label="Clave del producto",
                                            border="underline",
                                            width=300,
                                            read_only=False,
                                        ),
                                        ft.Icon(
                                            name=ft.icons.DRAW_OUTLINED,
                                            color="BLACK",
                                            tooltip="Campo Requerido",
                                        ),
                                    ],
                                ),
                                ft.Row(
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    controls=[
                                        ft.TextField(
                                            label="Descripcion del producto",
                                            multiline=True,
                                            min_lines=1,
                                            max_lines=5,
                                            border="underline",
                                            width=300,
                                            read_only=False,
                                        ),
                                        ft.Icon(
                                            name=ft.icons.DRAW_OUTLINED,
                                            color="BLACK",
                                            tooltip="Campo Requerido",
                                        ),
                                    ],
                                ),
                                ft.Row(
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    controls=[
                                        ft.TextField(
                                            label="Codigo de producto",
                                            hint_text="Escanea el Codigo",
                                            border="underline",
                                            width=300,
                                            read_only=True,
                                        ),
                                        ft.IconButton(
                                            ft.icons.QR_CODE,
                                            icon_color="BLACK",
                                            tooltip="Escanear nuevo Codigo",
                                            on_click=lambda e: read_barcode(),
                                        ),
                                    ],
                                ),
                                ft.Row(
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    controls=[
                                        ft.Dropdown(
                                            label="Selecciona una categoria",
                                            width=350,
                                            options=[
                                                ft.dropdown.Option("CATEGORIA 1"),
                                                ft.dropdown.Option("CATEGORIA 2"),
                                                ft.dropdown.Option("CATEGORIA 3"),
                                                ft.dropdown.Option("CATEGORIA 4"),
                                                ft.dropdown.Option("CATEGORIA 5"),
                                                ft.dropdown.Option("CATEGORIA 6"),
                                                ft.dropdown.Option("CATEGORIA 7"),
                                                ft.dropdown.Option("CATEGORIA 8"),
                                                ft.dropdown.Option("CATEGORIA 9"),
                                                ft.dropdown.Option("CATEGORIA 10"),
                                            ],
                                        )
                                    ],
                                ),
                                ft.Row(
                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                    controls=[
                                        ft.IconButton(
                                            ft.icons.CHEVRON_LEFT,
                                            icon_color="BLACK",
                                            tooltip="Regresar",
                                            on_click=lambda e: page.go("/home/stock"),
                                        ),
                                        ft.IconButton(
                                            ft.icons.HOME,
                                            icon_color="BLACK",
                                            tooltip="Ir al Inicio",
                                            on_click=lambda e: page.go("/home"),
                                        ),
                                        ft.IconButton(
                                            ft.icons.LOGOUT,
                                            icon_color="BLACK",
                                            tooltip="Cerrar Sesion",
                                            on_click=lambda e: page.go("/login"),
                                        ),
                                    ],
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                        ),
                        # width=1200,
                        # height=800,
                        alignment=ft.alignment.center,
                        bgcolor="#EDF2F4",
                        expand=True,
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                expand=True,
            ),
        ],
    )
