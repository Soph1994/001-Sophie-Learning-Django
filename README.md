# Sophie is learning Django

## 1. Créer un PROJET Django

1.1. S'assurer que l'on a le programme pour créer un environnement virtuel 
</br>
`virtualenv--version`

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


## X. Points importants à connaître

X.1. Arrêter le serveur Django en serveur local
</br>
Cliquer sur le terminal et faire Ctrl+C

X.2. Initialiser un dossier Git
</br>
`git init`

X.3. Ajouter un fichier pour ignaurer les fichiers que l'on ne doit pas suivre:
</br>
`.gitignore`

X.4. Activer l'environnement virtuel
<br/>
`.\venv\Scripts\activate`





