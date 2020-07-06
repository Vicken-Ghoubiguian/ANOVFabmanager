# ANOVFabmanager

Projet de développement d'un systéme de gestion des clients, des abonnements, de contrôle des espaces et des machines pour le futur atelier numérique Orles Valley.

##### Table des matières

1. [Présentation du projet](#presentation_du_projet)

2. [Technologies utilisées](#technologies_utilisées)

3. [Prérequis](#prerequis)

	* [Django](https://www.djangoproject.com),

	* [Docker](https://www.docker.com),

	* [Docker compose](https://docs.docker.com/compose/),

	* [virtualenv](https://python-guide-pt-br.readthedocs.io/fr/latest/dev/virtualenvs.html),

	* [pip](https://pip.pypa.io/en/stable/),

	* [jQuery](https://jquery.com),

	* [jQuery UI](https://jqueryui.com).

4. [Commandes de base](#commandes_de_base)

5. [Installation de ANOVFabmanager sur une machine quelconque](#installation_de_ANOVFabmanager_sur_une_machine_quelconque)

6. [Installation de ANOVFabmanager grâce à Docker compose](#installation_de_ANOVFabmanager_grace_a_docker_compose)

<a name="presentation_du_projet"></a>
## Présentation du projet



<a name="prerequis"></a>
## Prérequis

Pour faire fonctionner ANOVFabmanager sur une machine quelconque (physique ou virtuelle), il faut impérativement installer les composants suivants:

#### Django

![Django logo](https://static.djangoproject.com/img/logos/django-logo-positive.png)

Django est un framework open source écrit en Python pour vous permettre de développer des applications web.

#### Docker

![Docker logo](https://d1.awsstatic.com/acs/characters/Logos/Docker-Logo_Horizontel_279x131.b8a5c41e56b77706656d61080f6a0217a3ba356d.png)

Docker est un moteur logiciel permettant de lancer des applications dans des conteneurs logiciels.

#### Docker compose

![Docker compose logo](https://user.oc-static.com/upload/2019/05/08/15573466889395_1_QVFjsW8gyIXeCUJucmK4XA.png)

#### virtualenv

![Virtualvenv logo](https://www.vincentverloop.nl/wp-content/themes/yootheme/cache/python-virtualenv-e00eb153.jpeg)

#### pip

![Pip logo](https://www.twoscoops.co.uk/wp-content/uploads/2015/08/pip-logo.png)

#### jQuery

![JQuery logo](https://www.igmcentre.fr/wp-content/uploads/2015/06/jquery-logo.jpg)

#### jQuery UI

![JQuery UI logo](data:image/png;base64,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)

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

<a name="installation_de_ANOVFabmanager_sur_une_machine_quelconque"></a>
## Installation de ANOVFabmanager sur une machine quelconque

Pour installer ANOVFabmanager en version de développement ou de test, il suffit de suivre la procédure suivante.

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

<a name="installation_de_ANOVFabmanager_grace_a_docker_compose"></a>
## Installation de ANOVFabmanager grâce à Docker compose
