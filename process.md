# For virtual environment

-> py -m venv project-name
-> project-name\Scripts\activate.bat

-> `django-admin` - to see possible subcommands

-> in src `django-admin startproject project-name(here trydjango)`  - to creage two files trydjango and manage.py

-> run manage.py as - `python manage.py runserver` - will give some warnings but don't care


# set editor
-> in sublime text in project `open project` and `save project as`

# django settings in settings.py in src

-> every django project has a secret key

middleware - requests and handle requests

root_urlconf - how to route

templates - html pages rendered in django

wsgi_application - server uses

databases - maps to database, where is located, engine

auth_password - validates password

international stuff

static_url - where do you store some stuff

-> `python manage.py migrate` - for database - syncs database with our settings and apps 

-> in settings change name to db2 and run `python manage.py migrate` it will create another db (only works with sqlite)

# django components (apps)

-> add /admin in url to see `admin app` or component
-> run python manage.py migrate in another terminal to have app running
 -- its to confirm db is ready to use

-> `python manage.py createsuperuser` - create user which has access to admin
-> log in with created user in admin

-> to to user - now we are in `auth app`

# create custom app

-> `python manage.py startapp app-name` - to create app with name app-name
the new app will be included in src with some files

-> add 'products' in apps in settings
-> `python manage.py makemigrations` - to create modal Product
-> `python manage.py migrate` 

after adding a new field in models and makemigrations it will ask to add default

-> whenever make changes in models.py run makemigrations and migrate

-> got an error while saving new product - upgraded to django-2.1.5 and it solved

# create product object 

-> `python manage.py shell` - opens python interpretor - to create object in interpretor
Product.objects.all()
Product.objects.create(title="jdf"...)



-> to add view - add function in urls.py as given


-> add the template folder from templates in settings.py in DIRS
-> add the path of templates in dirs as /python-flask/.../templates or use os.path.join with BASE_DIR

-> see built-in templates and filters in documentation



-> obj = Product.objects.get(id=1)
-> dir(obj) - gives available functions


-> ** dict passes dict as arguments












