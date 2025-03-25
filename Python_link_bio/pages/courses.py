import reflex as rx
from Python_link_bio.components.navbar import navbar
from Python_link_bio.components.footer import footer
from Python_link_bio.views.header import header
from Python_link_bio.views.index_links import index_links
import Python_link_bio.styles.styles as styles
from Python_link_bio.styles.styles import Size as Size
from Python_link_bio.views.sponsors import sponsors
import Python_link_bio.utils as utils
from Python_link_bio.routes import Route
from Python_link_bio.views.courses_links import courses_links


@rx.page(
    route=Route.COURSES.value,
    title=utils.courses_title,
    description=utils.courses_description,
    image=utils.preview,
    meta=utils.courses_meta
)
def courses()-> rx.Component:
    return rx.box(
        utils.lang(),
        navbar(),
        rx.center(
            rx.vstack(
            header(details=False),
            courses_links(),
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

