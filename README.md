Проект на Django
____________________________________________________
    после того как проект склонирован
    pip install -r requiremets.txt для того чтобы установились все библиотеки
____________________________________________________
1. python -m venv venv
2. venv\scripts\activate
3. pip freeze > requiremets.txt
4. pip install django
5. django-admin startproject shop -> cd shop -> manage.py startapp product
6. settigs.py -> INSTALLED_APPS add 'product.apps.ProductConfig'
7. manage.py migrate

_______________________________________________________
Начало работы с общим проектом на гит

    git remote add origin https://github.com/FullstakCommand/название_проекта.git
    git branch -M main
    git push -u origin main

Username for 'https://github.com': ******** Password for ******: *********


