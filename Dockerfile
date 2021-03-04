# Définition de l'image de base pour la génération de l'image Docker
FROM python:latest

# Définition du mainteneur
LABEL maintainer="ericghoubiguian@live.fr"

#  Pour permettre aux messages des logs d'être immédiatement vidés dans le flux au lieu d'être mis en mémoire tampon
ENV PYTHONUNBUFFERED 1

# Migration de tous les fichiers de anovmanager vers le répertoire nouvellement créé anovmanager
COPY . /anovmanager

# Changement du répertoire courant pour celui nouvellement créé intitulé anovmanager
WORKDIR /anovmanager

# Installation de tous les composants
RUN pip install -r /anovmanager/requirements.txt

# Listening on the 8000 port
EXPOSE 8000

# Exécution de la commande "python3 manage py réserver' pour lancer fabmanager
ENTRYPOINT ["python3", "manage.py", "runserver", "0.0.0.0:8000"]