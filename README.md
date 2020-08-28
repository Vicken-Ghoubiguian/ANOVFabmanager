# ANOVFabmanager

##### Table des matières

1. [Présentation du projet](#presentation_du_projet)

2. [Technologies utilisées](#technologies_utilisées)

3. [Prérequis](#prerequis)

	* [Django](https://www.djangoproject.com),

	* [Docker](https://www.docker.com),

	* [Docker compose](https://docs.docker.com/compose/),

	* [pip](https://pip.pypa.io/en/stable/),

	* [MySQL](https://www.mysql.com/fr/),

	* [virtualenv](https://python-guide-pt-br.readthedocs.io/fr/latest/dev/virtualenvs.html),

	* [jQuery](https://jquery.com),

	* [jQuery UI](https://jqueryui.com),
	 
	* [git](https://git-scm.com),
 
	* [Bootstrap](https://getbootstrap.com).

4. [Installation de ANOVFabmanager sur une machine quelconque](#installation_de_ANOVFabmanager_sur_une_machine_quelconque)

5. [ANOVFabmanager déjà installé ? Comment le développer ?](#ANOVFabmanager_deja_installe_comment_le_developper)

6. [Installation de ANOVFabmanager grâce à Docker compose](#installation_de_ANOVFabmanager_grace_a_docker_compose)

7. [Commandes de base](#commandes_de_base)

<a name="presentation_du_projet"></a>
## Présentation du projet

Ce projet consiste à développer un systéme de gestion des clients, des abonnements, de contrôle des espaces et des machines pour le futur atelier numérique Orles Valley.
D'autres fonctionnalités peuvent être ajoutées à ce système logiciel à condition de faire le tour des spécificités techniques et de l'architecture de ce dernier.

<a name="prerequis"></a>
## Prérequis

Pour faire fonctionner ANOVFabmanager sur une machine quelconque (physique ou virtuelle), l'application repose sur les composants suivants:

<a name="django"></a>
* Django: `Django` est un framework open source écrit en Python pour vous permettre de développer des applications web,

<a name="docker"></a>
* Docker: `Docker` est un moteur logiciel permettant la génération, le déploiement et la gestion d'applications dans des conteneurs logiciels,

<a name="docker_compose"></a>
* Docker compose: `Docker compose` est un outil logiciel permettant la génération, le déploiement et la gestion d'applications multi-containers avec Docker,

<a name="mysql"></a>
* MySQL: `MySQL` est un moteur de gestion de bases de données permettant le stockage et la gestion des données relatives au bon fonctionnement du fablab,

<a name="pip"></a>
* pip: `pip` est un utilitaire pour l'installation et la gestion de packages python,

<a name="virtualenv"></a>
* virtualenv: `virtualenv` est un utilitaire pour créer des environnements virtuels python isolés,

<a name="jquery"></a>
* jQuery: `jQuery` est une bibliothèque JavaScript permettant la mise au point d'effets dans les pages web,

<a name="jqueryui"></a>
* jQuery UI: `jQuery UI` est une extension du framework `jQuery` présenté précédemment, permettant la mise au point d'effets pour les widgets de la page web,

<a name="git"></a> 
* git: `git` est l'utilitaire de gestion de versions utilisé par le projet de développement de l'application `ANOVFabmanager`,

<a name="bootstrap"></a>
* Bootstrap: `Bootstrap` est une collection d'outils pour la mise en place du design des pages web composant l'application `ANOVFabmanager`.

Pour la bonne configuration de l'environnement de déploiement, il est nécessaire d'installer `Django`, `Git`, `Docker`, `Docker compose`, `virtualenv` et `pip`.

Tout est expliqué en détail dans les parties [Installation de ANOVFabmanager sur une machine quelconque](#installation_de_ANOVFabmanager_sur_une_machine_quelconque) et [Installation de ANOVFabmanager grâce à Docker compose](#installation_de_ANOVFabmanager_grace_a_docker_compose) ci-dessous.

<a name="installation_de_ANOVFabmanager_sur_une_machine_quelconque"></a>
## Installation de ANOVFabmanager sur une machine quelconque

Pour faire fonctionner ANOVFabmanager, il est d'abord important d'installer les composants suivants: `Django`, `Git`, `virtualenv` et `pip`.

Il est d'abord important de cloner le projet depuis le dépôt officiel. Pour cela, exécutez les commandes suivantes dans l'ordre:

```bash

sudo apt install git # Installe l'utilitaire git sur la machine

git clone https://gitlab.imerir.com/orles-valley/anovfabmanager # Clone le projet ANOVFabmanager sur la machine

cd anovfabmanager # Change le répertoire courant pour celui du projet cloné anovfabmanager

```
Il faut ensuite également créer puis configurer l'environnement virtuel Python et y installer `Django` grâce aux commandes suivantes à exécuter dans l'ordre:

```bash

sudo apt install python3-pip # Installation de l'utilitaire pip3 (utilitaire pip pour la version 3 de python) pour installer tous les packages python nécessaires

sudo apt install python3-venv # Installation de l'utilitaire python3-venv pour créer et configurer votre environement virtuel

python3 -m venv votre_environnement_virtuel # Création de l'environnement virtuel

source votre_environnement_virtuel/bin/activate # Activation de votre environement virtuel

pip3 install -r requirements.txt # Installation de tous les packages python contenus dans le fichier requirements.txt

```
Maintenant que tout est en place, il est maintenant temps de démarrer l'application web. Pour cela, exécutez la commande suivante:

```bash
python3 manage.py runserver
```
Toutes mes félicitations: une fois cette commande exécutée, l'application fonctionne et est accessible [ici](http://127.0.0.1:8000).

<a name="ANOVFabmanager_deja_installe_comment_le_developper"></a>
## ANOVFabmanager déjà installé ? Comment le développer ?

Dans le cas où ANOVFabmanager a été correctement installé et configuré selon les instructions données dans la section précédente (voir [ici](#installation_de_ANOVFabmanager_sur_une_machine_quelconque)), il vous faudra réactiver votre environnement virtuel Python pour développer l'application web.

Pour cela, suivez les commandes suivantes dans cet ordre:

```bash

cd anovfabmanager # Change le répertoire courant pour celui du projet cloné anovfabmanager

source votre_environnement_virtuel/bin/activate # Activation de votre environement virtuel
```
Le prompt de votre terminal passera immédiatement de `$` à `(votre_environnement_virtuel)`.

Finalement pour activer l'application web, exécutez cette commande:

```bash
python3 manage.py runserver
```

Toutes mes félicitations, c'est maintenant à vous de jouer.

<a name="installation_de_ANOVFabmanager_grace_a_docker_compose"></a>
## Installation de ANOVFabmanager grâce à Docker compose

Comme précédemment, clonez le projet depuis le dépôt officiel puis vous rendre dans le répertoire correspondant à l'aide des commandes suivantes à exécuter dans l'ordre:

```bash

sudo apt install git # Installe l'utilitaire git sur la machine

git clone https://gitlab.imerir.com/orles-valley/anovfabmanager # Clone le projet ANOVFabmanager sur la machine

cd anovfabmanager # Change le répertoire courant pour celui du projet cloné anovfabmanager

```
Le déployement de ANOVFabmanager en production se fera grâce à `Docker` et `Docker compose`. Il est donc nécessaire de les installer d'abord avant toutes choses.
Si vous voulez faire ça rapidement, exécutez les commandes suivantes:

```bash
sudo apt install docker.io # Installe Docker sur la machine

sudo apt install docker-compose # Installe Docker compose sur la machine
```
Si vous voulez les installer proprement, rendez-vous sur [Installer Docker](https://docs.docker.com/engine/install/ubuntu/) et [Installer Docker compose](https://docs.docker.com/compose/install/).

Une fois que tout est installé, exécutez la commande `sudo docker-compose up`. Cette commande va construire et faire marcher les containers Docker de l'application web.

Une fois cette commande exécutée, l'application fonctionne et est accessible [ici](http://127.0.0.1:8000).

Toutes mes félicitations...

<a name="commandes_de_base"></a>
## Commandes de base

Voici une liste des commandes de base pour l'administration de fabmanager:

* Pour démarrer l'application web:

```bash
python3 manage.py runserver
```
* Pour démarrer l'application web en mode non sécurisé (dans le cas où le mode débug est désactivé):

```bash
python3 manage.py runserver --insecure
```
__Petite note__: pour lancer cette commande, il est nécessaire d'être dans le même répertoire que le projet.
