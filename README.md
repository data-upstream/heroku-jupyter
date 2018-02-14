# heroku-jupyter

Use this application to deploy [Jupyter Notebook](https://jupyter.org/) to
heroku.

## Quick start

Jupyter will not start, if the environment variable `JUPYTER_NOTEBOOK_PASSWORD`
was not set.

## Installation instructions

### heroku - automatic deployment

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

### heroku - manual deployment

Push this repository to your app or fork this repository on github and link your
repository to your heroku app.

Jupyter notebook will not start until the environment variable
`JUPYTER_NOTEBOOK_PASSWORD` is set. Use a good password:
```
$ heroku config:set JUPYTER_NOTEBOOK_PASSWORD=<your_passwd> -a <your_app>
```

If you are really sure, that you do not want a password protected notebook
server, you can set `JUPYTER_NOTEBOOK_PASSWORD_DISABLED` to `DangerZone!`.

