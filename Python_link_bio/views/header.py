import reflex as rx

from Python_link_bio.components.link_icon import link_icon
from Python_link_bio.components.info_text import info_text
from Python_link_bio.styles.styles import Size
from Python_link_bio.styles.colors import TextColor
from Python_link_bio.styles.colors import Color
import Python_link_bio.constants as const


def header(details=True) -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(fallback="AM",
                      size=Size.BIG.value,
                      src="/236.jpg",
                      radius="full",
                      bg=Color.CONTENT.value,
                      color=TextColor.BODY.value,
                      padding="2px",
                      border="4px",
                      border_color=Color.PRIMARY.value
                      ),
            rx.vstack(
                rx.heading(
                    "Aldo A Minoldo", size=Size.MEDIUM.value,
                    direction="column", spacing="3",
                    width="100%",
                    color=TextColor.HEADER.value
                ),
                rx.text(
                    "@minoldoaldo",
                    margin_top="0px",
                    color=TextColor.BODY.value
                ),
                rx.hstack(
                    link_icon(
                        "/icons/twitch.svg",  # no muestra la imagen
                        const.MOUREDEV_URL,
                        "Twithc"
                    ),
                    link_icon(
                        "/icons/instagram.svg",
                        const.YOUTUBE_URL,
                        "Youtube"
                    ),
                    link_icon(
                        "/icons/x.svg",
                        const.YOUTUBE_URL,
                        "Youtube Secundario"
                    ),
                ),
                align_items="start"
            ),
            spacing=Size.DEFAULT.value
        ),
        rx.cond(
            details,
            rx.vstack(
                rx.flex(
                    info_text("+13", "años de experiencia"),
                    rx.spacer(),
                    info_text("+13", "años de experiencia"),
                    rx.spacer(),
                    # info_text("+13", "años de experiencia"),
                    width="100%"
                ),

                rx.text(f"""
        Desarrollador de software del Instituto Politecnico Cordoba""",
                        color=TextColor.BODY.value,
                        font_size=Size.MEDIUM.value
                        ),
                width="100%",
                spacing=Size.BIG.value
            ),
        ),
        spacing=Size.BIG.value,
        align_items="start"
        # justify_content="center"
    )
