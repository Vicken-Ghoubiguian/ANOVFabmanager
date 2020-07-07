# Définition de l'image de base pour la génération de l'image Docker
FROM python:latest

# Définition du mainteneur
LABEL maintainer="eric.ghoubiguian@imerir.com"

#  Pour permettre aux messages des logs d'être immédiatement vidés dans le flux au lieu d'être mis en mémoire tampon
ENV PYTHONUNBUFFERED 1

# Copie de tous les fichiers et répertoires dans le répertoire nouvellement créé anovfabmanager
RUN mkdir anovfabmanager

# Changement du répertoire courant pour celui nouvellement créé intitulé anovfabmanager
WORKDIR /anovfabmanager

# Migration de tous les fichiers de anovfabmanager vers le répertoire nouvellement créé anovfabmanager
ADD . /anovfabmanager

# Mise à jour du système et de tous ses composants
RUN pip3 install -r /anovfabmanager/requirements.txt

# Exécution de la commande "python3 manage py réserver' pour lancer fabmanager
#CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
