import reflex as rx
from Python_link_bio.components.navbar import navbar
from Python_link_bio.components.footer import footer
from Python_link_bio.views.header.header import header
from Python_link_bio.views.links.links import links
import Python_link_bio.styles.styles as styles
from Python_link_bio.styles.styles import Size as Size
from Python_link_bio.views.sponsors.sponsors import sponsors

#para backend es State
# class State(rx.State):
#     pass


def index()-> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
            header(),
            links(),
            sponsors(),
            max_width=styles.MAX_WIDTH,
            width="100%",
            # align_items="center",
            # justify_content="center",
            # height="100vh",
            margin_y=Size.BIG.value
            )
        ),
        rx.center(
            footer())
    )


app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE
)
app.add_page(
    index,
    title="Aldo Minoldo | aprendiendo",
    description="Hola mi nombre es Aldo",
    image="236.jpg"
)

