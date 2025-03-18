import reflex as rx
from Python_link_bio.components.title import title
from Python_link_bio.components.link_sponsor import link_sponsor
import Python_link_bio.constants as const
from Python_link_bio.styles.styles import Size

def sponsors() -> rx.Component:
    return rx.vstack(
        title("Coloboran"),
        rx.grid(
            link_sponsor(
                "gato-1024-x-768.jpg",
                const.ELGATO_URL,
                "logotipo del gato"
            ),
            link_sponsor(
                "gato-1024-x-768.jpg",
                const.MVP_URL,
                "logotivo del gatoooo"
            ),
            spacing=Size.DEFAULT.value,
            columns=rx.breakpoints(initial="1", xs="1", sm="2")#los acomoda segun el tamaño pantalla
        ),
        width="100%",
        align_items="start"
    )
