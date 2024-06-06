import flet as ft


def create_container(count, text, color):
    items = []
    for i in range(1, count + 1):
        items.append(
            ft.Container(
                content=ft.Text(value=str(text)),
                alignment=ft.alignment.center,
                width=100,
                height=100,
                bgcolor=color,
            )
        )
    return items


def display_items(align: ft.CrossAxisAlignment, text, click):
    return ft.Column(
        [
            ft.Text(
                str(text),
                size=16,
            ),
            ft.Container(
                content=ft.Column(
                    create_container(1, text, "green"),
                    alignment=ft.MainAxisAlignment.START,
                    horizontal_alignment=align,
                ),
                bgcolor=ft.colors.AMBER_100,
                width=200,
                on_click=click,
            ),
        ]
    )
