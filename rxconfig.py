import reflex as rx

config = rx.Config(
    app_name="Python_link_bio",
    api_url="https://pruebareflex-production.up.railway.app:8000",
    cors_allowed_origins=[
        "http://localhost:3000",
        "https://aldominoldopruebareflex.vercel.app/"
    ]
)