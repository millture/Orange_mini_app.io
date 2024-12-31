import asyncio
import flet as ft


async def main(page: ft.Page):
    page.title = 'Cliker'
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#fcfcfc"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.fonts = {'Fonts': '/assets/fonts/Fonts.ttf'}
    page.theme = ft.Theme(font_family="Fonts")

    async def score_up(event: ft.ContainerTapEvent):
        score.data += 1
        score.value = str(score.data)

        image.scale = 0.7

        score_counter.opacity = 0.9
        score_counter.value = "+1"

        score_counter.visible = True

        score_counter.left = event.local_x
        score_counter.top = event.local_y

        progress_bar.value += (1 / 100)

        if score.data % 50 == 0:
            if score.data % 325 == 0:
                message = 'Ты выиграла все призы 🎆'
            elif score.data % 300 == 0:
                message = 'Твой пятый приз 🎶'
            elif score.data % 250 == 0:
                message = 'Твой четвертый приз 👕'
            elif score.data % 200 == 0:
                message = 'Твой третий приз 👖'
            elif score.data % 150 == 0:
                message = 'Твой второй приз 🍬'
            elif score.data % 100 == 0:
                message = 'Твой первый приз 🧦'
            elif score.data % 25 == 0:
                message = 'Игра началась 🎅'

            snack_bar = ft.SnackBar(
                content=ft.Text(
                    value=message,
                    size=20,
                    color="#ff8b1f",
                    text_align=ft.TextAlign.CENTER
                ),
                bgcolor="#f0f9f7"
            )

            page.overlay.append(snack_bar)
            snack_bar.open = True
            progress_bar.value = 0

        page.update()

        await asyncio.sleep(0.1)
        image.scale = 1
        score_counter.opacity = 0
        score_counter.visible = False

        page.update()
        # page.overlay.clear()

    score = ft.Text(value="0", size=100, data=0, color="#fa8128")
    score_counter = ft.Text(size=50, animate_opacity=ft.Animation(duration=600, curve=ft.AnimationCurve.BOUNCE_IN))

    image = ft.Image(
        src="newphoto.jpg",
        fit=ft.ImageFit.CONTAIN,
        width=250,  # Установите желаемую ширину
        animate_scale=ft.Animation(duration=600, curve=ft.AnimationCurve.EASE)
    )

    progress_bar = ft.ProgressBar(
        value=0,
        width=page.width - 100,
        bar_height=20,
        color="#ff8b1f",
        bgcolor="#bf6524"

    )

    page.add(
        score,
        ft.Container(
            content=ft.Stack(controls=[image, score_counter]),
            on_tap_down=score_up,
            margin=ft.Margin(0, 0, 0, 30)
        ),
        ft.Container(
            content=progress_bar,
            border_radius=ft.BorderRadius(10, 10, 10, 10)
        )
    )


if __name__ == "__main__":
    # ft.app(target=main, view=ft.WEB_BROWSER)
    ft.app(target=main)
