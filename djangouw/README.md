# 👋 Hello developer!

This project serves as an example of what can be achieved. It is not a fully functional product. Feel free to use the source code and ideas as a starting point for your own projects.

This is one of the many templates available from W3Schools. Check our [tutorials for frontend development](https://www.w3schools.com/where_to_start.asp) to learn the basics of [HTML](https://www.w3schools.com/html/default.asp), [CSS](https://www.w3schools.com/css/default.asp) and [JavaScript](https://www.w3schools.com/js/default.asp). 🦄  
Also check [Python](https://www.w3schools.com/python/) and [Django](https://www.w3schools.com/django/) tutorials to grasp the backend of this template.

## Knowledge requirements

To be able to fully understand and modify this template to your needs, there are several things you should know (or learn):

- [HTML](https://www.w3schools.com/html/default.asp)
- [CSS](https://www.w3schools.com/css/default.asp)
- [JavaScript](https://www.w3schools.com/js/default.asp)
- [Python](https://www.w3schools.com/python/)
- [Django](https://www.w3schools.com/django/)
- [SQLite](https://www.sqlite.org/docs.html)

## Warning - environment variables

Do not change DATABASE_URL and SECRET_KEY, as these are generated. If they are changed the space may not behave as predicted.
**Remember to switch DEBUG to false when going to production**

## 🔨 What's next?

Customize this template to make it your own.  
Remember to make your layout responsive - if you want your site to look good on smaller screens like mobile.  

## 🎨 Where to find everything?

This template is made by using several technologies.  
Below are explanations about where to find specific code.

### HTML

HTML files are stored in a folder called `templates`. Files have `.html` extension.
In `templates/base.html` you can add your external links and scripts, or change other meaningful things that is relevant on every page.
You can find other templates in `templates/`.

### CSS and Static Images

CSS files can be found in `static/css/`.
Icons are stored in `static/`.

### Core files

You can find:
  - views in `form/views.py`.
  - local URL configuration in `form/urls.py`.
  - global URL configuration in `contact-form/urls.py`.
  - models (for tables) in `form/models.py`.
  - static files in `static`.
  - settings in `contact-form/settings.py`.

## Database

Dynamic spaces can use [SQLite](https://www.sqlite.org/docs.html) database.  
The database file is called `database.db`. It is placed inside the `w3s-dynamic-storage` folder.  
SQLite connection path to the database is `sqlite:///w3s-dynamic-storage/database.db` which you can use to connect to the SQLite database programmatically.   
For this template, the database connection path can also be found in the environment.  
You can modify the tables in `models.py` inside `form`. Remember to run the commands for `makemigrations` and `migrate` when you change the models. 

---  
**Do not change the `w3s-dynamic-storage` folder name or `database.db` file name!**  
**By changing the `w3s-dynamic-storage` folder name or `database.db` file name, you risk the space not working properly.**

## What is needed if you want to integrate this template into another project

  - Bring everything under `form/` into your base directory and add 'form' to your `INSTALLED_APPS` in `settings.py`.
  - Check for migrations by running both `python3 manage.py makemigrations` and `python3 manage.py migrate`
  - In your global `urls.py` (in the project settings folder) add the path to the form app. The first argument will determine what all the local app URLs for the form will be under. Make sure it doesn't crash with your other URLs. Example:`path('contact-us', include('form.urls'))`

## Misc: 
  - `python3 manage.py makemigrations`
    - If you change the models you have to run this command and then migrate to commit the changes.
  - `python3 manage.py migrate`
    - Migrate is needed to put the model changes into effect after making migrations. This will create new tables which means you may have conflicts to already stored data. In that case Django will ask in the terminal what you would like to do. This is the message:
      `It is impossible to add a non-nullable field <name> to <model> without specifying a default.` This is because the database needs something to populate existing rows.
      Please select a fix:
      1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
      2) Quit and manually define a default value in models.py.
      Select an option: `
    You avoid this by setting a default when you add the field to the model. E.g. `title = models.CharField(("title"), max_length=250)`

## 🔨 Please note
For now files created/uploaded or edited from within the terminal view will not be backed up or synced. 

## ⛑ Need support?
[Join our Discord community](https://discord.gg/6Z7UaRbUQM) and ask questions in the **#spaces-general** channel to get your space on the next level.  
[Send us a ticket](https://support.w3schools.com/hc/en-gb) if you have any technical issues with Spaces.

Happy learning!