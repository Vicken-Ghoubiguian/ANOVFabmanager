# ANOVFabmanager

##### Table des matières

1. [Présentation du projet](#presentation_du_projet)

2. [Technologies utilisées](#technologies_utilisées)

3. [Prérequis](#prerequis)

	* [Django](https://www.djangoproject.com),

	* [Docker](https://www.docker.com),

	* [Docker compose](https://docs.docker.com/compose/),

	* [pip](https://pip.pypa.io/en/stable/),

	* [virtualenv](https://python-guide-pt-br.readthedocs.io/fr/latest/dev/virtualenvs.html),

	* [jQuery](https://jquery.com),

	* [jQuery UI](https://jqueryui.com),
	 
	* [git](https://git-scm.com),
 
	* [Bootstrap](https://getbootstrap.com).

4. [Commandes de base](#commandes_de_base)

5. [Installation de ANOVFabmanager sur une machine quelconque](#installation_de_ANOVFabmanager_sur_une_machine_quelconque)

6. [Installation de ANOVFabmanager grâce à Docker compose](#installation_de_ANOVFabmanager_grace_a_docker_compose)

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



```

<!-- Pour installer ANOVFabmanager en version de développement ou de test, il suffit de suivre la procédure suivante.

Tout d'abord si ce n'est pas déjà fait, clonez le dépôt git du projet à l'aide de la commande suivante:

```bash
git clone https://gitlab.imerir.com/orles-valley/anovfabmanager
```

Ensuite, rendez-vous dans le répertoire du projet cloné à l'aide de la commande suivante:

```bash
cd anovfabmanager
```

Pour finir, lancez la commande suivante pour lancer l'application web:

```bash
python3 manage.py runserver
```

-->

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

Une fois que tout est installé, exécutez la commande `docker-compose up`. Cette commande va construire et faire marcher les containers Docker de l'application web.

Une fois cette commande exécutée, l'application fonctionne et est accessible [ici](http://127.0.0.1:8000).

Toutes mes félicitations...

<!-- Pour faire fonctionner ANOVFabmanager en version de développement ou de test, il est nécessaire d'installer le framework Django.

Avant toutes choses, il est nécessaire de vérifier que l'utilitaire pip3 est installé, grâce à la commande suivante:

```bash
sudo pip3 --version
```
ou encore celle-ci:

```bash
sudo pip3 -V
```
Si celui-ci n'est pas installé, lancez la commande suivante:

```bash
sudo apt install python3-pip
```
Il est maintenant temps de passer aux choses sérieuses.

Tout d'abord, vous devez créer votre environnement virtuel dans le répertoire du projet.

Positionnez-vous dans le répertoire du projet à l'aide de la commande suivante:

```bash
cd anovfabmanager
```
Ensuite, créez votre environement virtuel à l'aide de la commande suivante:

```bash
python3 -m venv votre_environement_virtuel
```
Si l'utilitaire `venv` n'est pas installé, installez-le à l'aide de la commande suivante:

```bash
sudo apt install python3-venv
```
Maintenant il ne reste plus qu'à l'activer à l'aide de cette dernière commande:

```bash
source votre_environement_virtuel/bin/activate
```
Il est maintenant temps d'installer Django, pour cela lancez la commande suivante:

```bash
pip3 install django
```
__petite précision__: la commande `sudo` n'est plus nécessaire une fois l'environement virtuel activé.

Pour mettre à jour Django, vous avez le choix entre les 2 commandes suivantes:

```bash
pip3 install django --upgrade
```
ou

```bash
pip3 install --upgrade django=(numéro de la nouvelle version; ex: 3.0.4)
```
Pour le thème jquery UI ThemeRoller, voici le lien bref de celui utilisé: [Ici](https://jqueryui.com/themeroller/#!zThemeParams=5d00000100d805000000000000003d8888d844329a8dfe02723de3e5700bbb34ecf36cdef1e1654faa0015427bdb9eb45ebe89aaede0ec5f0d92417fcc6551ce804ff46bf543167700d2cf4e583f2515147aacb86ffa11c0e588dae72a13c98dc37478199f7eea536e99702e8babee264319b6fedc74243113955cb55c0a1f9a7c71478699d65953b77021eb6065294f9943cf01581477003638b2648a14140bd1364b8e574f4cbc4379b66b19ed3ca38a09d4d41cc5d47881ce86e441dbec79fc7e939a1dd6a718741b7a1c175423193b8b6b9df4ea3e248684b6e81b6c1d1f07593f4d884035cf3765453b971b41435eb448b3c44f5766aa0c97ae3cd31fd2f6373e6681c8a76476442a7f5b468583f684ce07cae1e36f845a51dd8908a0ea104852be2ea69bc1fb128173fea2ef429073f878b1eee2a442df26aeac6e85d0a784490072e15669e922a2ec3dcb38bd88a2dc97c16c8e0e615006af4faf8eccc5148c4978a2cd5acc0c22359967c3f3d290590fd208197456fd53f44e8cf62ce33821227876c3ebedaac7716382aca97ec04d8679ff990c6166)

-->

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
