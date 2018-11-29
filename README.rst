=====================
django-transitive-dag
=====================


.. image:: https://travis-ci.com/Maxbot100/django-transitive-dag.svg?branch=master
   :target: https://travis-ci.com/Maxbot100/django-transitive-dag


.. image:: https://codecov.io/gh/Maxbot100/django-transitive-dag/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/Maxbot100/django-transitive-dag


SQL Directed Acyclic Graph models for Django

Usage Notes
-----------
Just subclass from EdgeModel & NodeModel and pass your model names as strings like this:

.. code-block:: python

   class MyNode(NodeModel("MyEdge")):
       pass

   class MyEdge(EdgeModel("MyNode")):
       pass


Known Issues / Todo
-------------------
- Updating the ``src`` or ``dst`` of an edge completely breaks the integrity of the graph. Updates to ``src`` and
  ``dst`` are silently prevented, but other fields go through to the database. This leaves the python object in a broken
  state, which is extremely confusing. Instead, you should save a copy of the edge with your changes (e.g. by setting
  ``pk=None``) and then delete the original (or delete first if performance is an issue)
- Batch inserts/updates of edges don't call custom save methods, which means the transitive closure is never generated
