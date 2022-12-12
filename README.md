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

## 5. Intégrer les éléments de navigation

5.1 ajouter dans le dossier template à la racine du projet, le fichier navbar.html

5.2. récupérer le modèle de navbar que vous désirez sur [Bootstrap navbar](https://getbootstrap.com/docs/4.3/components/navbar/) coller le modèle dans le fichier navbar.html

5.3. inclure dans le fichier base.html le contenu de la navbar avec la commande suivante:</br>
`{% include 'navbar.html' %}`

## 6. Créer un modèle de donnée

6.1. aller dans le dossier blogs, puis le fichier models.py. Créer le model Post.

6.2. Préparer les scripts du models de données avec la commande suivante:
`python manage.py makemigrations`

6.3. Générer les tables dans la base de donnée
`python manage.py migrate`

## 7. Ajouter des données au modèle de donnée

7.1. importer le model dans le fichier admin.py
`from .models import Post`

7.2. Ajouter le modèle Post au menu admin
`admin.site.register(Post)`

7.3. Créer un superuser dans le terminal et suivez les instructions
`python manage.py createsuperuser`

7.4. Se connecter a l'espace Admin
`localhost:8000/admin`

7.5. Ajouter deux lignes au modèle Post

## 8. Ajouter une ListView

8.1. création d'un url

8.2. création d'une ListView

8.3. création d'un folder template ListView

8.4. Ajouter l'extension de la base.html et les blocks content

8.5. Créer une boucle sur les blogs dans le template blog_list.html

## 9. Mettre dans une table html la ListView

9.1. Mettre le format de table bootstrap. [table bootstrap](https://getbootstrap.com/docs/4.0/content/tables/)

9.2. Intégrer la boucle dans la table html 

## 10. Ajouter une Vue CREER Blog

10.1. Ajouter une url

10.2. Ajouter une vue

10.3 Ajouter un template

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

4. Activer l'environnement virtuel
<br/>
`.\venv\Scripts\activate`

5. Figer les librairies installés dans le fichier requirements.txt</br>
`pip freeze > requirements.txt`

6. Installer les librairies téléchargés du projet</br>
`pip install -r requirements.txt`