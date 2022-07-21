# URL-Shortner

## Design and implement a URL shortener service in Django

● Use case - generate short link:It should take a URL and generate a fixed length, shortened random url.
○ A web page to allow the a user to paste a URL and see the randomly generated shortened URL (note: no authentication required, hence no concept of ‘admin’ is here)
○ This may be done via a POST API to save the details

● Use case - Use short link: When user uses any generated URL they should be redirected to the original URL
○ This may be done via a GET API which will have the redirection logic



## How to install and Run

Git clone repository from https://github.com/PawanRamaMali/URL-Shortner.git 

In the Project directory,  run the below command to install the required packages 

```
pip install -r requirements.txt
``` 

* For windows, open command prompt to load the secret key

```
call env.bat
```

* For Linux, open the terminal and execute the below command to load the secret key
```
source .env
```


```
python manage.py makemigrations

python manage.py migrate

python manage.py runserver
```

