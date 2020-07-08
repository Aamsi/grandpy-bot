# grandpy-bot

## Présentation du projet

GrandPyBot est un robot qui peut vous donner des informations sur différents lieux.

Posez-lui une question, et il vous donnera l'adresse du lieu et des informations sur l'endroit.

Vous pouvez visiter le projet sur le lien: https://git.heroku.com/p7-app.git

Vous pouvez aussi l'installer en local.

## Installation

**Clôner le repo**

```git clone https://github.com/Aamsi/grandpy-bot.git```

**Créer votre environnemment virtuel**

- ```virtualenv env``` à la racine du projet
- ```source env/bin/activate``` pour activer l'environnement virtuel

**Installer les librairies necessaires**

```pip install -r requirements.txt```

**Fournir une API KEY pour Google Map et MapBox**
- Vous pouvez créer un fichier ```local_settings.py``` et mettre vos variables dedans (voir le fichier patch)
- Avec heroku, créez un fichier ```.env```

**Lancer l'application à la racine du projet**
- Avec python: ``` python flask_app.py```
- Avec heroku en local après avoir créer votre fichier ```.env```

Posez vos questions au bot! :+1:

## Lancer les tests à la racine du projet

- Décommentez les lignes dans le fichier ```local_settings.py```
- run ```python -m unittest discover```
