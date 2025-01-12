# Django Framework #

##### About the project

This repository was created to learn about Django Framework in high school class in the IT technician course.  
The idea of this project is return a shorter URL from user-supplied input.  

##### Requirements
* [Python](https://www.python.org/downloads/)
* [Django](https://www.djangoproject.com/download/)

##### Running the project

You need to create a Admin user to manage the URLs, with interface. So, in a powershell run: 

`python manage.py createsuperuser`

The script will ask you an user name, an e-mail and a password. This information will be used to access the admin panel. 
Now, run the server with: 

`python manage.py runserver`

The service can then be accessed in the browser through the address <http://localhost:8000>. The admin panel can be accessed in <http://localhost:8000/admin/>. 
The URL must be registered in the admin panel for the request to be made successfully. You can make some requests in the Python Shell too. 

`python manage.py shell`

With the Python Shell open, you need to import the URL class: 
`>>> from encurtador.models import URL`

Now, you can make requests: 
`>>> URL.objects.all()` >> list all URLs

`>>> obj = URL.objects.create()` >> create an empty object

```
>>> obj.url = 'http://example.com' 
>>> obj.shortcode = 'example'
>>> obj.save() 
```

`>>> obj = URL.objects.create(url = 'http://example.com', shortcode = 'example')` 

If you need to update the database, run: 
`python manage.py migrate`
