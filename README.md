## Yarn checker :yarn:

Web scraping app for yarn & wool prices comparison with **Django** and **DRF** <br/>
It uses celery beat to scape with current prices twice a day and update the database accordingly.


**Requirements:**

beautifulsoup4==4.12.2 <br/>
celery==5.3.1 <br/>
Django==4.2.3 <br/>
djangorestframework==3.14.0 <br/>
redis==4.6.0 <br/>
requests==2.31.0 <br/>
 

**_Starting the app:_**

- Navigate to the project folder and execute 
``` python manage.py runserver ```
- Open [localhost:8000/yarn_products](http://localhost:8000/yarn_products/) with any browser to view the scraped results

![image](https://github.com/Kaluzhskaia/yarn_checker/assets/16777799/7c0c3c13-7be0-4b3a-8c8b-88752a5a69d9)
