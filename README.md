# RelationshipHierarchy-Portal
An Interactive website  that  displays different downloadable hierarchy levels

### Installation

```sh
$ pip3 install django
$ pip3 install --upgrade django-crispy-forms
```

Make migrations and start the server.
```sh
$ python3 manage.py makemigrations
$ python3 manage.py migrate
$ python3 manage.py runserver
```

## Tree visualization procedure

### Default

The tree is displayed in collapsible mode so that the user can click on a node of his choice
and view it's immediate children

### Steps to expand/collapse tree

1)If the user wants to expand or collapse a node completely,he/she will first need to expand the node by clicking if it is in collapsed form or collapse it and then  expand it  again if it is in expanded form.(Warning:Ignoring step 1) could lead to erroneous functionalities)

2)Click on the desired button(Expand/Collapse)

3)Collapse the node  and expand it again.You will be able to view the changes.
