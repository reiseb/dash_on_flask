# Dash on flask with flask_login
An example of a seamless integration of a Dash app into an existing Flask app based on the application factory pattern.

For details and how to use, please read: [How to embed a Dash app into an existing Flask app](https://medium.com/@olegkomarov_77860/how-to-embed-a-dash-app-into-an-existing-flask-app-ea05d7a2210b)

## Modifications from the original blogpost
* added separate subfolder for dashapps, multiple apps can be developed separately and added via git submodules
* added further abstraction to dashapp registration
* revised forms and login logic so that only admins can register new users
* added css style sheets
* updated environment

## Deploy on Heroku (free)
First, edit the app.json and replace the value of the `repository`:
```
"repository": "https://github.com/okomarov/dash_on_flask"
```
with the URL to the forked repository.

Then click on the button:

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)
