# Sophie is learning Django

## 1. Créer un PROJET Django

1.1. S'assurer que l'on a le programme pour créer un environnement virtuel 
</br>
`virtualenv --version`

1.2. Créer l'environnement virtuel
</br>
`virtualenv venv`

1.3. Installer Django (librairie Python)
</br>
`pip install django`

1.4. Créer un projet Django avec le nom core
</br>
`django-admin startproject core .`

1.5. Démarrer le serveur Django en local
</br>
`python manage.py runserver`


## 2. Créer une APPLICATION Django

2.1. Créer une application dans le projet avec le nom blogs
</br>
`python manage.py startapp blogs`

2.2. Créer le fichier urls.py dans le dossier de l'application créée

2.3. Enregistrer l'application blogs dans le fichier settings 

2.4. Inclure les urls blogs dans l'application core


## 3. Créer une page web

3.1. Créer une url pour diriger vers la vue

3.2. Créer une vue qui sera appelée par l'url pour diriger vers le template

3.3. Préparer le template

## 4. Intégrer Bootstrap au projet

4.1. Ajouter BASE_DIR / "templates" au fichier settings

4.2. Ajouter à settings le STATIC_URL</br>
`STATIC_URL = '/static/'`

4.3. Ajouter à settings le STATIC_ROOT</br>
`STATIC_ROOT = BASE_DIR / 'staticfiles'`

4.4. Ajouter à settings le STATICFILES_DIRS et importer la librairie os
`STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)`
`import os`

4.6. Créer le dossier templates à la racine du projets

4.7. Créer la base html dans le dossier templates

4.8. Ajouter le templates html appelant le bootstrap, voir [Bootstrap CDN](https://www.bootstrapcdn.com/)

4.9. Etendre le ficher de base dans les templates</br>
`{% extends 'base.html' %}`

4.10. Ajouter le contenu dans la page dans les balises</br>
`{% block content %}`</br>
`{% endblock %}`

## Points importants à connaître

1. Arrêter le serveur Django en serveur local
Cliquer sur le terminal et faire Ctrl+C

2. Initialiser un dossier Git
</br>
`git init`

3. Ajouter un fichier pour ignaurer les fichiers que l'on ne doit pas suivre:
</br>
`.gitignore`

4. Activer l'environnement virtuel
</br>
`.\venv\Scripts\activate`

5. Figer les librairies installés dans le fichier requirements.txt</br>
`pip freeze > requirements.txt`

6. Installer les librairies téléchargés du projet</br>
`pip install -r requirements.txt`