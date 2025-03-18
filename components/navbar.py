import reflex as rx
from Python_link_bio.styles.styles import Size as Size
from Python_link_bio.styles.colors import Color as Color
import Python_link_bio.styles.styles as styles

def navbar() -> rx.Component:
    return rx.vstack(
        rx.flex(
          rx.text("aldo", color=Color.PRIMARY.value),
            rx.text("minoldo", color=Color.SECONDARY.value),
            style=styles.navbar_title_style
        ),
        position="sticky",
        bg=Color.CONTENT.value,
        padding_x=Size.BIG.value,
        padding_y = Size.BIG.value,
        z_index="999",
        top="0px"#para paso todo por debajo de la barra(navbar)
    )