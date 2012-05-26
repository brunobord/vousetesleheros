=============================
Spécifications du format YAML
=============================

Les étapes en YAML sont écrites dans le format YAML. Si vous voulez des détails
sur ce format, vous pouvez vous diriger sur le `site officiel de YAML <http://yaml.org/>`_

Le projet "Vous êtes le héros" a bien sûr ses propres clés pour définir les
différentes parties utilisées dans chaque page.

e.g.

.. code-block:: yaml

    title: Commençons l'aventure...
    subtitle: êtes-vous prêt ?
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
            text: je veux aller ici
            next: next_step
        -
            text: je veux aller là
            next: other_step

Clés disponibles
================

* ``title``: Le titre de la page.
* ``subtitle``: Le sous-titre. Pour être plus spécifique.
* ``intro``: Texte libre permettant de renseigner les joueurs sur leur situation,
  pour les aider à faire un choix.
* ``choices``: une liste d'options disponibles pour chaque joueur. C'est un peu
  plus complexe, donc, voir ci-dessous comment les alimenter.

.. note::

    Le texte d'intro sera analysé en markdown et générera du HTML. Ça signifie
    par exemple que \*\*mon texte\*\* s'affichera en gras, comme ceci :
    **mon texte**.


Choices
-------

Chaque choix est un élément de liste. Chaque liste est est préfixée par un "-"
indenté. Et chaque liste a de nouveau deux clés

* ``text``: le texte du lien
* ``next``: la cible du lien. c'est à dire, la page web vers laquelle les
  joueurs iront s'ils choisissent cette option.

.. note::

    Le contenu du "next" est le nom simple de la page, sans l'extension ".html"
    ou ".yaml".
