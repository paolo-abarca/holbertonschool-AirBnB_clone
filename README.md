![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
<h1 align="center"> AirBnB Clone </h1>

![](https://images.adsttc.com/media/images/5967/cc6d/b22e/38bb/9b00/0094/original/Airbnb_Exported.gif?1499974762)

- Name of the project : ``0x00. AirBnB clone - The console``
- Authors : <br>
	- [Fernando Gonzales Pradinett](https://github.com/gpradinett) <br>
	- [Paolo Abarca Garcia](https://github.com/paolo-abarca)

<h2 align="center">🤩We create a shell to manage our AirBnB objects🤩</h2>

<img align="right" src="https://media4.giphy.com/media/jO2ZYyQ44uuamn8yYO/giphy.gif?cid=790b7611b13e0aa2b32eec1f0797f9efdc46c7c8adad0c38&rid=giphy.gif&ct=s" width="320px" height="320px">

This is the first step of our first full web application: the AirBnB clone. Our console is able to work in interactive mode but also in non-interactive mode. It main goal is to manage the AirBnB objects. It is capable of creating new objects, retrieving an object from a file, doing operations on objects like counting and computing stats, updating attributes of an object and destroying them.

# 🤔What’s a command interpreter (shell)?🤔

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

## 2 - all

### Usage 1
````c
all <class>
````

### Usage 2

````
<nombre de clase>.all()
````

### Output
````c

(hbnb) User.all()
["[User] (1aa89e6c-d6f0-4be5-96e8-05636eb60122) {'id': '1aa89e6c-d6f0-4be5-96e8-05636eb60122', 'created_at': datetime.datetime(2022, 7, 2, 23, 4, 16, 460854), 'updated_at': datetime.datetime(2022, 7, 2, 23, 4, 16, 460854), 'first_name': 'Zenkaiser', 'age': '89'}"]
(hbnb)

````

## 3 Show a class instances
muestra una instancia especifica


````c
================ Usage 1 ==============
(hbnb) show City 07062be7-fd57-4791-88a6-6a78806398c9

================ Usage 2 ==============

City.show(07062be7-fd57-4791-88a6-6a78806398c9)

========================Output======================================
[City] (07062be7-fd57-4791-88a6-6a78806398c9) {'id': '07062be7-fd57-4791-88a6-6a78806398c9', 'created_at': datetime.datetime(2022, 7, 1, 16, 6, 54, 356353), 'updated_at': datetime.datetime(2022, 7, 1, 16, 6, 54, 356365)}
(hbnb)

````

## 4 Destroy a instance of the storage( file.json )

````c

==================== Usage 1 ==================
destroy User 38f22813-2753-4d42-b37c-57a17f1e4f88

==================== Usage 2 ===================
destroy.User("38f22813-2753-4d42-b37c-57a17f1e4f88")

========================Output======================================

(hbnb) User.all()
["[User] (1aa89e6c-d6f0-4be5-96e8-05636eb60122) {'id': '1aa89e6c-d6f0-4be5-96e8-05636eb60122', 'created_at': datetime.datetime(2022, 7, 2, 23, 4, 16, 460854), 'updated_at': datetime.datetime(2022, 7, 2, 23, 4, 16, 460854), 'first_name': 'Zenkaiser', 'age': '89'}"]
(hbnb)

````

## 5 Update attribute, of instance to the storage

````c

(hbnb) User.all()

["[User] (1aa89e6c-d6f0-4be5-96e8-05636eb60122) {'id': '1aa89e6c-d6f0-4be5-96e8-05636eb60122', 'created_at': datetime.datetime(2022, 7, 2, 23, 4, 16, 460854), 'updated_at': datetime.datetime(2022, 7, 2, 23, 4, 16, 460854), 'first_name': 'Zenkaiser', 'age': '89'}"]
(hbnb)

================= Usage 1 ======================
update User 49faff9a-6318-451f-87b6-910505c55907 first_name "Zenkaiser"

================= Usage 2 =======================
update.User(49faff9a-6318-451f-87b6-910505c55907, first_name, "Zenkaiser")

========================Output======================================
["[User] (1aa89e6c-d6f0-4be5-96e8-05636eb60122) {'id': '1aa89e6c-d6f0-4be5-96e8-05636eb60122', 'created_at': datetime.datetime(2022, 7, 2, 23, 4, 16, 460854), 'updated_at': datetime.datetime(2022, 7, 2, 23, 4, 16, 460854), 'first_name': 'Zenkaiser', 'age': '89'}"]
(hbnb)

````

# Unittest for classes and console

## run unittest

````
python3 -m unittest discover tests


=============Output================
.............................................................
----------------------------------------------------------------------
Ran 32 tests in 0.231s

OK

````

## test the console capturing the output

````
with patch('sys.stdout', new=StringIO()) as f:
    HBNBCommand().onecmd("help show")
````

# Authors contact

[Fernando J. Gonzales Pradinett - linkedin](https://www.linkedin.com/in/fernando-gonzales-pradinett-2879129b/) <br>
[Paolo Abarca - linkedin](https://www.linkedin.com/in/paolo-abarca/)
