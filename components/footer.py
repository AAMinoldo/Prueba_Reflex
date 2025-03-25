import reflex as rx
import datetime

from Python_link_bio.styles.colors import TextColor
from Python_link_bio.styles.styles import Size
import Python_link_bio.constants as const


def footer() -> rx.Component:
    return rx.vstack(
        rx.image(src="/favicon.jpeg",
                 height=Size.VERY_BIG.value,
                 weight=Size.VERY_BIG.value,
                 alt="Logotipo de AldoM. Una \'eme\' entre llaves."
                 ),
        rx.text(f"2024 - {datetime.date.today().year}",
                margin_bottom=Size.ZERO.value
                ),  # python para actualizar el año

        rx.link("Aldo link", href="https://mouredev.com",
                is_external=True, align_items="center",
                font_size=Size.MEDIUM.value,
                margin_bottom=Size.SMALL.value,
                margin_top=Size.ZERO.value,
                ),
        rx.link(
            rx.hstack(
                rx.image(
                    src="/icons/github.svg",
                    height=Size.LARGE.value,
                    width=Size.LARGE.value
                ),

                rx.text("Software de creación novedosas desde Cordoba para el mundo",
                        font_size=Size.MEDIUM.value,
                        margin_bottom="50px",  # separo el fondo de la pagina
                ),
                padding_top=Size.ZERO.value
            ),
            href=const.REPO_URL,
            is_external=True
        ),

        padding_x=Size.BIG.value,
        margin_top="80px",  # separa los botones de footer
        color=TextColor.FOOTER.value,
        spacing=Size.ZERO.value#redujo el espacio entre Aldo link y Software..

    )
