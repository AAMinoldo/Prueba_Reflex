# FROM python:3.13 as init
#
# WORKDIR /app
# COPY . .
#
# ENV VIRTUAL_ENV=/app/.venv_docker
# ENV PATH="$VIRTUAL_ENV/bin:$PATH"
# RUN python3 -m venv $VIRTUAL_ENV
#
# RUN pip install --upgrade pip
# RUN $uv pip install --no-cache-dir -r requirements.txt
#
# CMD reflex run --env prod --backend-only


FROM python:3.13

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar el contenido del directorio actual al contenedor
COPY . .

# Crear el entorno virtual
ENV VIRTUAL_ENV=/app/.venv_docker
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Crear el entorno virtual
RUN python -m venv $VIRTUAL_ENV

# Instalar pip y cualquier dependencia
RUN pip install --upgrade pip

# Instalar Reflex
RUN pip install reflex

# Instrucción CMD para ejecutar Reflex con los parámetros especificados
CMD ["reflex", "run", "--env", "prod", "--backend-only"]


#arranca el contenedor
#docker run -d -p 8000:8000 --name app aldominoldo-web:latest
#docker ps

