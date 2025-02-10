# Utilisation de l'image officielle Python
FROM python:3.10-slim

# Définition du répertoire de travail
WORKDIR /app

# Copie des fichiers de l'application
COPY . /app

# Installation des dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Définition des variables d'environnement
ENV PYTHONUNBUFFERED=1

# Exposition du port de l'application
EXPOSE 8000

# Commande pour démarrer l'application
CMD ["fastapi", "prod", "main.py"]
