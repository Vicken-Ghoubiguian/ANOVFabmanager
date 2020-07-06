# Définition de l'image de base pour la génération de l'image Docker
FROM python:latest

# Définition du mainteneur
LABEL maintainer="eric.ghoubiguian@imerir.com"

#
ENV PYTHONUNBUFFERED 1

# Copie de tous les fichiers et répertoires dans le répertoire nouvellement créé anovfabmanager
RUN mkdir anovfabmanager

# Changement du répertoire courant pour celui nouvellement créé intitulé anovfabmanager
WORKDIR /anovfabmanager

#
ADD requirements.txt /anovfabmanager

# Mise à jour du système et de tous ses composants
RUN pip3 install -r /anovfabmanager/requirements.txt

#
ADD . /anovfabmanager

# 
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
