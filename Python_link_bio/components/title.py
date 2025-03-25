import reflex as rx
import Python_link_bio.styles.styles as styles
from Python_link_bio.styles.styles import title_style


def title(text: str) -> rx.Component:
    return rx.heading(
        text,
        style=styles.title_style
    )