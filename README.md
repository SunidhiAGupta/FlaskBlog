# FlaskBlog
This is a flask blog application.

## Debug
When you make any changes to your app and reload it, app will not show any changes, you have to stop your app and run it again. So to make the changes visible on reload set debug enviornment as given in command below, make changes in your code also.
```bash
 export FLASK_DEBUG=1
```

```bash
 if __name__== '__main__':
        app.run(debug=True)
```
## 'templates' folder
To get rid of writing HTML code within the route funtion, we create a template Folder.
This folder cntains all the HTML files for each of the route functions.

## render_template()
This function is used to render html files from templates folder in your flask app.

