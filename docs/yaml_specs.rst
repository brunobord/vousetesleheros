==========
YAML specs
==========

Step files are written in a YAML format. If you want extensive details on how to
write YAML files, you might want to browse `the official YAML page <http://yaml.org/>`_

More specifically, the "Vous êtes le héros" generator is using specific keys to
define the different content parts of the page.

e.g.

.. code-block:: yaml

    title: Let's start an adventure...
    subtitle: will you be ready for this?
    intro:

        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec a diam
        lectus. Sed sit amet ipsum mauris. Maecenas congue ligula ac quam viverra
        nec consectetur ante hendrerit. Donec et mollis dolor. Praesent et diam eget
        libero egestas mattis sit amet vitae augue. Nam tincidunt congue enim, ut
        porta lorem lacinia consectetur. **Donec ut libero sed arcu vehicula**
        ultricies a non tortor. Lorem ipsum dolor sit amet, consectetur adipiscing
        elit. Aenean ut gravida lorem. Ut turpis felis, pulvinar a semper sed,
        adipiscing id dolor. Pellentesque auctor nisi id magna consequat sagittis.

        Curabitur dapibus enim sit amet elit pharetra tincidunt feugiat nisl
        imperdiet. Ut convallis libero in urna ultrices accumsan. Donec sed odio
        eros. Donec viverra mi quis quam pulvinar at malesuada arcu rhoncus. Cum
        sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus
        mus. In rutrum accumsan ultricies. Mauris vitae nisi at sem facilisis semper
        ac in est.

    choices:
        -
            text: Now I wanna go to this step
            next: next_step
        -
            text: I'd rather go to this one
            next: other_step

Available keys
==============

* ``title``: Title of the page.
* ``subtitle``: Sub-title. To be a little more specific.
* ``intro``: Free text to tell the players more about their situation, before
  they could make their choice.
* ``choices``: a list of options the players should pick... It's a bit more
  complex, please read further if you need some help.
* ``image``: a path to the image that will be displayed on the left side of your
  intro text. Please note that the path should be relative to the :file:`assets`
  directory

``intro``
---------

The "intro" text will be parsed using the markdown format and generated. This
means for example that \*\*my text\*\* will be displayed in bold, like this:
**my text**.

``choices``
-----------

Each choice is a list item. Each list item is preceeded by a (indented) "-"
character. And each list item is built with two keys:

* ``text``: the text of the link
* ``next``: the target of the link. that is to say, the name of the next web page
  the players would reach if they make this choice.
* ``notes`` : adding notes. These notes will be displayed as a pop-in, When
  you'll click on the "OK" button, the players will be redirected to the ``next``
  page.

.. note::

    Please note that the "next" content is the name of the page, without the
    ".html" or  ".yaml" file extension.


Alternate templating
--------------------

By default, the template used by the generator is :file:`step.html`. If you need
a specific template for one or more pages, you'll just have to:

* add your new template in the :file:`template` directory, let's say it's called :file:`special.html`.
* in your :file:`step.yaml` file, set a value for the key ``template``, like this:

.. code-block:: yaml

    title: Look, my special page!
    template: special.html
