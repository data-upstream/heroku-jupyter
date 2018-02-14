try:
    import os
    import json
    import traceback
    import IPython.lib
    #import pgcontents

    c = get_config()

    ### Password protection ###
    passwd = os.environ['JUPYTER_NOTEBOOK_PASSWORD']
    c.NotebookApp.password = IPython.lib.passwd(passwd)

except Exception:
    traceback.print_exc()
    # if an exception occues, notebook normally would get started
    # without password set. For security reasons, execution is stopped.
    exit(-1)
