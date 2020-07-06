# Définition de l'image de base pour la génération de l'image Docker
FROM django:latest

# Définition du mainteneur
LABEL maintainer="eric.ghoubiguian@imerir.com"

# Copie de tous les fichiers et répertoires dans le répertoire nouvellement créé anovfabmanager
COPY . /anovfabmanager

# Changement du répertoire courant pour celui nouvellement créé intitulé anovfabmanager
WORKDIR /anovfabmanager

# Mise à jour du système et de tous ses composants
RUN apt upgrade -y && apt update -y

# Exposer le port d'écoute du container
EXPOSE 8000

# Point d'entrée du container: 'python3 manage.py runserver'
ENTRYPOINT ["python3", "manage.py", "runserver"]
