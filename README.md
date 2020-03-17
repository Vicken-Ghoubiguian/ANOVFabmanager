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
