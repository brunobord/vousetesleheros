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

Choices
-------

Each choice is a list item. Each list item is preceeded by a (indented) "-"
character. And each list item is built with two keys:

* ``text``: the text of the link
* ``next``: the target of the link. that is to say, the name of the next web page
  the players would reach if they make this choice.

.. note::

    Please note that the "next" content is the name of the page, without the
    ".html" or  ".yaml" file extension.
