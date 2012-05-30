===================
Utilisation de base
===================

Installation
============

Il vous faut un environnement dans lequel les paquets suivants sont disponibles :

* Jinja2
* Markdown
* PyYAML

Si vous utilisez pip et virtualenv, vous savez qu'il faut faire ça :

.. code-block:: sh

    pip install -r requirements.pip

Créer ses étapes
================

Dans le dossier :file:`steps`, vous pouvez créer vos fichiers YAML en utilisant les
:doc:`specs_yaml` propres au projet.

À partir de là, votre imagination est la limite. Il est recommandé de démarrer
à partir d'un :file:`index.yaml`, mais rien d'obligatoire.

Quand vous pensez être prêt...

Générer votre site
==================

.. code-block:: sh

    python generator.py

Normalement, c'est bon.
