# Utilisez une image de base Python
FROM python:3.8-slim

# Copiez les fichiers requis (app.py) dans le conteneur
COPY . .

# Installez les dépendances
RUN pip install Flask
RUN pip install jinja2

# Commande pour exécuter l'application
CMD ["python", "app/app.py"]