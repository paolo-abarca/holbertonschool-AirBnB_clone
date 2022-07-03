![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
<h1 align="center"> AirBnB Clone </h1>

![](https://images.adsttc.com/media/images/5967/cc6d/b22e/38bb/9b00/0094/original/Airbnb_Exported.gif?1499974762)

- Name of the project : ``0x00. AirBnB clone - The console``
- Authors : <br>
	- [Fernando Gonzales Pradinett](https://github.com/gpradinett) <br>
	- [Paolo Abarca Garcia](https://github.com/paolo-abarca)

<h2 align="center">🤩We create a shell to manage our AirBnB objects🤩</h2>

This is the first step in creating our first full web application: the ``AirBnB clone``

<h2 align="center">🤔What’s a command interpreter (shell)?🤔</h2>

It is a program that receives commands from a user,
our console has the following functions:

``create``  ``update`` ``Destroy``  ``store`` ``persists``  -> Objects

- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object

# Starting

Steps:
### 1 - Install python

````
sudo apt install python3.8
````

### 2 - Clone the repo on your computer
````
git clone https://github.com/paolo-abarca/holbertonschool-AirBnB_clone.git
````

### 3 - Execute the console
````
./console.py
(hbnb)
````
you should see the following prompt waiting for your commands

## Non interactive mode

````c
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
````


## Interactive Mode
````c
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
````


## Learning Objectives

General
- How to create a ``Python package``
- How to create a command interpreter in Python using the ``cmd module``
- What is ``Unit testing`` and how to implement it in a ``large project``
- How to ``serialize`` and ``deserialize`` a Class
- How to ``write`` and ``read`` a JSON file
- How to manage ``datetime``
- What is an ``UUID``
- What is ``*args`` and how to use it
- What is `` **kwargs `` and how to use it
- How to handle ``named arguments`` in a function



# Testing
we must run the tests in interactive and non-interactive mode

| Non interactive mode
````c
echo "python3 -m unittest discover tests" | bash
````

| Interactive mode
````c
python3 -m unittest discover tests"
````

# Ejemplos de uso de **Comandos**

## 1 - Create
```
(hbnb) create <[class]>

######salida######

(hbnb) create User
38f22813-2753-4d42-b37c-57a17f1e4f88
(hbnb)
```

# Authors contact

[Fernando J. Gonzales Pradinett - linkedin](https://www.linkedin.com/in/fernando-gonzales-pradinett-2879129b/) <br>
[Paolo Abarca - linkedin](https://www.linkedin.com/in/paolo-abarca/)
