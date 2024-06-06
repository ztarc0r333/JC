import flet as ft
from flet import LinearGradient
from database.login_control import login_control


def login_view(page: ft.Page):
    """
    Generates the login view for the application.

    Parameters:
    - page (ft.Page): The page object representing the current page.

    Returns:
    - ft.View: The login view containing the username and password text fields, and the login button.
    """
    page.update()

    username = ft.TextField(
        label="Usuario",
        hint_text="Ingresa tu usuario",
        hint_style=ft.TextStyle(color="white"),
        label_style=ft.TextStyle(
            color="white",
            decoration_color="white",
        ),
        width=400,
        height=50,
        icon=ft.icons.PERSON,
        color="white",
        border_color="white",
        border_radius=10,
    )
    password = ft.TextField(
        label="Contraseña",
        hint_text="Ingresa tu contraseña",
        label_style=ft.TextStyle(
            color="white",
            decoration_color="white",
        ),
        hint_style=ft.TextStyle(color="white"),
        password=True,
        can_reveal_password=True,
        color="white",
        width=400,
        height=50,
        icon=ft.icons.LOCK,
        border_color="white",
        border_radius=10,
    )
    login_buton = ft.ElevatedButton(
        "Iniciar Sesion",
        width=400,
        height=50,
        on_click=lambda e: login_button_clicked(username, password),
    )

    def login_button_clicked(username, password):
        if login_control(username, password):
            return page.go("/home")
        else:
            page.snack_bar = ft.SnackBar(ft.Text("Usuario o contraseña incorrectos"))
            page.snack_bar.open = True
            page.update()

    return ft.View(
        "/login",
        controls=[
            ft.Row(
                controls=[
                    ft.Container(
                        alignment=ft.alignment.center,
                        bgcolor="WHITE",
                        content=ft.Column(
                            [
                                ft.Row(
                                    controls=[
                                        ft.Image(
                                            src="assets/images/logo_corah.png",
                                            width=600,
                                            height=300,
                                        )
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    expand=True,
                                ),
                                ft.Row(
                                    controls=[
                                        ft.Image(
                                            src="assets/images/logo_dam.png",
                                            width=300,
                                            height=300,
                                        ),
                                        ft.Image(
                                            src="assets/images/logo_berel.png",
                                            width=300,
                                            height=300,
                                        ),
                                    ],
                                    expand=True,
                                    alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                                ),
                                ft.Row(
                                    controls=[
                                        ft.Image(
                                            src="assets/images/logo_argentum.png",
                                            width=300,
                                            height=300,
                                        ),
                                        ft.Image(
                                            src="assets/images/logo_vvi.png",
                                            width=300,
                                            height=300,
                                        ),
                                        ft.Image(
                                            src="assets/images/logo_herr_2.png",
                                            width=300,
                                            height=300,
                                        ),
                                    ],
                                    expand=True,
                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        expand=True,
                    ),
                    ft.Container(
                        alignment=ft.alignment.center,
                        width=450,
                        gradient=LinearGradient(
                            begin=ft.alignment.top_center,
                            end=ft.alignment.bottom_center,
                            colors=["BLACK", "#1b263b", "#415a77"],
                        ),
                        border_radius=10,
                        content=ft.Column(
                            [
                                ft.Column(
                                    controls=[
                                        ft.Text(
                                            "Control de Auditoria",
                                            color="white",
                                            size=40,
                                            theme_style=ft.TextThemeStyle.TITLE_MEDIUM,
                                            text_align=ft.TextAlign.START,
                                        ),
                                        ft.Text(
                                            "Inicio de Sesion",
                                            color="white",
                                            size=40,
                                            theme_style=ft.TextThemeStyle.TITLE_MEDIUM,
                                            text_align=ft.TextAlign.START,
                                        ),
                                    ],
                                    # alignment=ft.MainAxisAlignment.CENTER,
                                    expand=True,
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                ),
                                ft.Column(
                                    controls=[username, password, login_buton],
                                    alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                    expand=True,
                                ),
                                ft.Column(
                                    controls=[
                                        ft.Text(
                                            "¿Olvidaste tu contraseña?",
                                            color="white",
                                            size=12,
                                            text_align=ft.TextAlign.END,
                                            style=ft.TextStyle(decoration="underline"),
                                        )
                                    ],
                                    alignment=ft.MainAxisAlignment.END,
                                    horizontal_alignment="end",
                                ),
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        expand=False,
                    ),
                ],
                expand=True,
            ),
        ],
    )
