# ANOVFabmanager

Développement un système de gestion des clients, de contrôle des espaces et des machines, pour le futur atelier numérique Orles Valley.

##### Table des matières

1. [Présentation du projet](#presentation_du_projet)

2. [Technologies utilisées](#technologies_utilisées)

3. [Prérequis](#prerequis)

4. [Commandes de base](#commandes_de_base)

5. [Installation de ANOVFabmanager en version de développement ou de test](#installation_de_ANOVFabmanager_en_version_de_developpement_ou_de_test)

<a name="#prerequis"></a>
## Prérequis

Pour faire fonctionner ANOVFabmanager en version de développement ou de test, il est nécessaire d'installer le framework Django.

Pour cela, lancez la commande suivante:

```bash
sudo pip3 install django
```

Si l'utilitaire pip n'est pas installé, lancez la commande suivante:

```bash
sudo apt install python3-pip
```

Pour mettre à jour Django, vous avez le choix entre les 2 commandes suivantes:

```bash
pip3 install django --upgrade
```

ou

```bash
pip3 install --upgrade django=(numéro de la nouvelle version; ex: 3.0.4)
```

Pour le thème jquery UI ThemeRoller, voici le lien bref de celui utilisé: https://jqueryui.com/themeroller/#!zThemeParams=5d00000100d805000000000000003d8888d844329a8dfe02723de3e5700bbb34ecf36cdef1e1654faa0015427bdb9eb45ebe89aaede0ec5f0d92417fcc6551ce804ff46bf543167700d2cf4e583f2515147aacb86ffa11c0e588dae72a13c98dc37478199f7eea536e99702e8babee264319b6fedc74243113955cb55c0a1f9a7c71478699d65953b77021eb6065294f9943cf01581477003638b2648a14140bd1364b8e574f4cbc4379b66b19ed3ca38a09d4d41cc5d47881ce86e441dbec79fc7e939a1dd6a718741b7a1c175423193b8b6b9df4ea3e248684b6e81b6c1d1f07593f4d884035cf3765453b971b41435eb448b3c44f5766aa0c97ae3cd31fd2f6373e6681c8a76476442a7f5b468583f684ce07cae1e36f845a51dd8908a0ea104852be2ea69bc1fb128173fea2ef429073f878b1eee2a442df26aeac6e85d0a784490072e15669e922a2ec3dcb38bd88a2dc97c16c8e0e615006af4faf8eccc5148c4978a2cd5acc0c22359967c3f3d290590fd208197456fd53f44e8cf62ce33821227876c3ebedaac7716382aca97ec04d8679ff990c6166

<a name="#commandes_de_base"></a>
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

<a name="#installation_de_ANOVFabmanager_en_version_de_developpement_ou_de_test"></a>
## Installation de ANOVFabmanager en version de développement ou de test

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
