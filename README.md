<center> <h1> DjangoTest </h1> </center>

<h5> About the project </h5>

This repository was created to learn about Django Framework in high school class in the IT technician course.  
The idea of this project is return a shorter URL from the input given away the user. 

<h5>Requirements</h5>
* [Python](https://www.python.org/downloads/)
* [Django](https://www.djangoproject.com/download/)

<h5>Running the project</h5>

You need to create a Admin user to manage the URLs, with interface. So, in a powershell run: 

`python manage.py createsuperuser`

The script will ask you an user name, an e-mail and a password. This information will be used to access the admin panel. 
Now, run the server with: 

`python manage.py runserver`

The service can then be accessed in the browser through the address <http://localhost:8000>. The admin panel can be accessed in <http://localhost:8000/admin/>. 
The URL must be registered in the admin panel for the request to be made successfully. You can do some requests in the Python Shell too. 

`python manage.py shell`

With the Python Shell open, you need to import the URL class: 
`>>> from encurtador.models import URL`

Now, you can do requests: 
`>>> URL.objects.all()` >> list all URLs

`>>> obj = URL.objects.create()` >> create a empty object

```
>>> obj.url = 'http://example.com' 
>>> obj.shortcode = 'example'
>>> obj.save() 
```

`>>> obj = URL.objects.create(url = 'http://example.com', shortcode = 'example')` 

If you need update the database, run: 
`python manage.py migrate`
