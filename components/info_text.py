import reflex as rx
import Python_link_bio.styles.styles as styles
from Python_link_bio.styles.colors import TextColor as TextColor
from Python_link_bio.styles.colors import Color as Color

def info_text(title: str, body: str) -> rx.Component:
    return rx.box(
        rx.text(title,
                font_wieght="bold",
                color=Color.PRIMARY.value
                ),
        f"{body}",
        font_size=styles.Size.MEDIUM.value,
        color=TextColor.BODY.value
    )








