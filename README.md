Backdrop
========

Backdrop is a configuration system that keeps your settings out of source control.

It's curently JSON based. Other formats may be available in the future.

Install
-------

    pip install backdrop

Use
---
Configuration files must be stored in `~/.backdrop/`.

For example, create a new project configuration file:

    touch ~/.backdrop/myproject.json

Open it with your favorite editor:

    vim ~/.backdrop/myproject.json

Save your settings, e.g.:

    {
        "database": {
            "username": "myproject",
            "password": "53cr3tp455w0rd"
        }
    }

In your project, include `backdrop` and load the configuration:

    from backdrop import Backdrop

    config = Backdrop('myproject')
