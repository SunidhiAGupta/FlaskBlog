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


