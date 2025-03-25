import reflex as rx
import Python_link_bio.styles.styles as styles
from Python_link_bio.styles.styles import Size as Size

def link_button(title: str, body: str, image:str, url: str, is_external=True)-> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.image(
                    src=image,
                        width=styles.Size.LARGE.value,
                        height=styles.Size.DEFAULT.value,
                        margin=styles.Size.MEDIUM.value,
                        alt=title
                        ),
                rx.vstack(
                    rx.text(title, style=styles.button_title_style),
                    rx.text(body, style=styles.button_body_style),
                ),
                spacing=Size.MEDIUM.value,
                align_items="start",
                text_align="left",
                margin=Size.ZERO.value,
                paddign_y=Size.SMALL.value,
                padding_right=Size.SMALL.value,
                width="100%"
            ),
            width = "100%",  # Ancho fijo para todos los botones
        ),
        align="center",
        href=url,
        is_external=is_external,  # habre una nueva pestaña, para no abondonar nuestra pagina
        width="100%",
    )



