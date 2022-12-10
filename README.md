# Sophie is learning Django

## 1. Créer un PROJET Django

1.1. S'assurer que l'on a le programme pour créer un environnement virtuel 
</br>
'virtualenv--version'

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


## Points importants à connaître

1. Arrêter le serveur Django en serveur local
Cliquer sur le terminal et faire Ctrl+C

2. Initialiser un dossier Git
</br>
`git init`

3. Ajouter un fichier pour ignaurer les fichiers que l'on ne doit pas suivre:
</br>
`.gitignore`





