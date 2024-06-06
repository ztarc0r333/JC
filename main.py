import flet as ft
from views.login import login_view
from views.home import home_view
from views.store import store_view
from views.stock import stock_view
from views.new_barcode import new_barcode_view


def main(page: ft.Page):
    page.title = "JC Portal"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.window_width = 1366
    page.window_height = 960
    page.window_resizable = False

    def route_change(route):
        page.views.clear()
        page.views.append(login_view(page))
        print(f"Actual route: {page.route}")
        if page.route == "/home":
            page.views.append(home_view(page))

        elif page.route == "/home/store":
            page.views.append(store_view(page))
        elif page.route == "/home/stock":
            page.views.append(stock_view(page))
        elif page.route == "/home/stock/new_barcode":
            page.views.append(new_barcode_view(page))

        page.update()

    def view_pop(view):
        page.views.clear()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

    page.add()


if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets")
