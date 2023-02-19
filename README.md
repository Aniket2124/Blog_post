# Blog_post
1. Clone project in to the system
2. open in IDE
3. Create a virtual environment
      python3 -m venv venv
4. Activate virtual environment
      source venv/bin/activate
5. Install requirements.txt
      pip install -r requirements.txt
6. Make Migrations for project
      python manage.py makemigrations
7. Make Migrate
      python manage.py migrate
8. Createsuperuser
      python manage.py createsuperuser
9. Runserver
      python manage.py runserver
10. Login using superadmin or can signup a new user to creat post
      note: login with username not with emailid
11. Once you sign in click on create blog to create a Blog Post
12. You can save to draft or can directly post a Blog, if you save the post it will be shown in saved post tab
13. click on Blog Post on Navbar to return to home page.
14. If you want to post saved blog go to saved post tab and click on read more then on update and you can post a Blog.
