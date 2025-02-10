# Utilisation de l'image officielle Python
FROM python:3.10-slim

# Définition du répertoire de travail
WORKDIR /app

# Copie des fichiers de l'application
COPY . /app

RUN pip install fastapi==0.115.8 \
    peewee==3.17.9 \
    pydantic==2.10.6 \
    PyJWT==2.10.1 \
    python-dotenv==1.0.1 \
    pytz==2025.1 \
    uvicorn==0.34.0

# Définition des variables d'environnement
ENV PYTHONUNBUFFERED=1

# Exposition du port de l'application
EXPOSE 8000

# Commande pour démarrer l'application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
