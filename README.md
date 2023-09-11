## Yarn Сhecker :yarn:

## Overview
Web scraping app for yarn & wool prices comparison with **Django** and **DRF** <br/>
It uses celery beat to scape with current prices twice a day and update the database accordingly.

## Features

- Scrape multiple pages of product listings.
- Gather detailed information for each product.
- Store or update scraped data through a data handler.
- Schedule data scrapings.

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/kaluzhskaia/yarn_checker.git
    ```
  
2. Navigate to the project directory:
    ```bash
    cd yarn_checker
    ```

3. Create a virtual environment (optional):
    ```bash
    virtualenv venv
    ```

    Activate the virtual environment:

    - On Windows:
        ```bash
        .\\venv\\Scripts\\activate
        ```

    - On macOS and Linux:
        ```bash
        source venv/bin/activate
        ```

4. Install the requirements:
    ```bash
    pip install -r requirements.txt
    ```

5. Create and apply the migrations:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

**Starting the app:**

- Navigate to the project folder and execute 
``` python manage.py runserver ```
- Open [localhost:8000/yarn_products](http://localhost:8000/yarn_products/) with any browser to view the scraped results.


## Screenshots
![image](https://github.com/Kaluzhskaia/yarn_checker/assets/16777799/7c0c3c13-7be0-4b3a-8c8b-88752a5a69d9)
