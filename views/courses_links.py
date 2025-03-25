import reflex as rx
from Python_link_bio.components.link_button import link_button
from Python_link_bio.components.title import title
from Python_link_bio.styles.styles import Size
import Python_link_bio.constants as const
from Python_link_bio.routes import Route


def courses_links() -> rx.Component:
    return rx.vstack(
        title("Cursos Gratis",
              ),
        
        link_button("Retos de programacion",
                    "Ruta de estudio semanal para practicar logica de programacion",
                    "/icons/twitch-brands.svg",
                    const.CODE_CHALLENGES_URL
                    ),
        link_button("Python desde cero",
                    "Cursos de 37 horas",
                    "/icons/twitch-brands.svg",
                    const.PYTHON_COURSE_URL
                    ),
        link_button("Sql y Bases de datos",
                    "Sql y mucho mas",
                    "/icons/twitch-brands.svg",
                    const.SQL_COURSE_URL
                    ),
        link_button("Un dia un lenguaje",
                    "Primeros pasos en los 11 lenguajes mas usados",
                    "/icons/twitch-brands.svg",
                    const.LANGUAGES_COURSE_URL
                    ),

        title("Muchos mas en:"),

        link_button("Retos de programacion",
                    "Ruta de estudio semanal para practicar logica de programacion",
                    "/icons/twitch-brands.svg",
                    const.CODE_CHALLENGES_URL
                    ),
        link_button("Python desde cero",
                    "Cursos de 37 horas",
                    "/icons/twitch-brands.svg",
                    const.PYTHON_COURSE_URL
                    ),
        width="100%",
        spacing=Size.MEDIUM.value
    )
