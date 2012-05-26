===========
Basic usage
===========

Install
=======

Setup your environment, by installing the following packages / make sure they're
available on your system:

* Jinja2
* Markdown
* PyYAML

if you are using pip and virtualenv, you know you can do this:

.. code-block:: sh

    pip install -r requirements.pip

Create your steps
=================

In the :file:`steps` directory, create your YAML files using the :doc:`yaml_specs`.
Your imagination is the limit. It's recommended to start with a :file:`index.yaml`,
but you are not bound to.

When you think your're ready...

Generate your website
=====================

.. code-block:: sh

    python generator.py

And you're done.
