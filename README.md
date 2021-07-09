## Curlec Biller

The webapp uses ReactJS for it's frontend and Django for it's backend.

To start the server and run the webapp. Go to terminal and run commands:

1. cd **django_react_starter/frontend** (make sure you are in the curlec_work directory first)
2. **npm run dev**
3. cd **..**
4. **py manage.py runserver**

The developement server will start at port 8000 and needs to be refreshed to show changes made in the code. Ctrl + 5 if changes aren't showing even after refresh.

Bootstrap was used to speed up development. The bootstrap css has been imported to django_react_starter\frontend\static\css\main.css so if you need to style anything edit that file (there is no need to edit the actual bootstrap files in the node_modules).

All the things that need to be done/fixed in each react component are added at the bottom of the component's .js files in curlec_work/django_react_starter/frontend/src/components.

The images used in this code are stored in django_react_starter/images. Currently they are sourced from imgur but you can change the src if you want in index.html file at django_react_starter/frontend/templates/frontend/index.html.

Python packages used are in requirements.txt file and all js packages used are in the two node_modules folders.

Feel free to clean up any bad code/bad practices as this webapp was coded by two 17-year-old high school students :)
