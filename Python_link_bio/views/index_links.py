import reflex as rx
from Python_link_bio.components.link_button import link_button
from Python_link_bio.components.title import title
from Python_link_bio.styles.styles import Size
import Python_link_bio.constants as const
from Python_link_bio.routes import Route


def index_links()-> rx.Component:
    return rx.vstack(
        title("Comunidad"),

            link_button("Cursos Gratis",
                    "Consulta de tutoriales***********************************",
                    "/icons/twitch-brands.svg",
                    Route.COURSES.value,
                        is_external=False,
                        ),

            link_button("Twitch******************************************",
                        "Directos de lunes a viernes***********************************",
                        "/icons/twitch-brands.svg",
                        const.TWITCH_URL),
            link_button("YouTube",
                        "Tutoriales semanales",
                        "/icons/twitch-brands.svg",
                        const.YOUTUBE_URL),
            link_button("YouTube" "(canal secundario)",
                        "Tutoriales semanales",
                        "/icons/twitch-brands.svg",
                        const.YOUTUBE_SECONDARY_URL),
            link_button("Discord",
                        "El chat de la comunidad",
                        "/icons/twitch-brands.svg",
                        const.DISCORD_URL),

        title("Recursos y mas"),
        link_button("Twitch",
                    "Directos de lunes a viernes",
                    "/icons/twitch-brands.svg",
                    "https://youtube.com/@mouredev"),
        link_button("YouTube",
                    "Tutoriales semanales",
                    "/icons/twitch-brands.svg",
                    "https://youtube.com/@mouredev"),
        link_button("YouTube" "(canal secundario)",
                    "Tutoriales semanales",
                    "/icons/twitch-brands.svg",
                    "https://youtube.com/@mouredevtv"),
        link_button("Discord",
                    "El chat de la comunidad",
                    "/icons/twitch-brands.svg",
                    "https://discord.gg/mouredev"),
        # width="100%",

            width="100%",
            spacing=Size.MEDIUM.value
            # align_items="center",
            # justify_content="center"


    )

