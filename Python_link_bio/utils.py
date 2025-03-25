import reflex as rx

# Comun

def lang()-> rx.Component:
    return rx.script("document.documentElement.lang='es'")

preview = "https://moure.dev/preview.jpg"

_meta = [
    {"name": "og:type", "content": "website"},
    {"name": "og:image", "content": preview},
    {"name": "twitter:card", "content": "summary_large_image"},
    {"name": "twitter:site", "content": "@mouredev"}
]
# Index

index_title = "AldoMinoldo | aprendido reflex"
index_description = "HOla, mi nombre es Aldo"

index_meta = [
    {"name": "og:title", "content": index_title},
    {"name": "og:description", "content": index_description},
]
index_meta.extend(_meta)

# Cursos
courses_title = "AldoMinoldo | Cursos Gratis"
courses_description = "Este es un listado con algunos cursos gratis de python"

courses_meta = [
    {"name": "og:title", "content": courses_title},
    {"name": "og:description", "content": courses_description},
]
courses_meta.extend(_meta)
