# AirBnB Clone
![AirBnB Logo](image/hbnb_logo.png)

## Contents

- [Description](#description)
- [Environment](#environment)
- [Further Information](#further-information)
- [Requirements](#requirements)
- [Repo Contents](#repo-contents)
- [Installation](#installation)
- [Usage](#usage)
  - [Methods](#methods)

## Description 📄

This is the first phase of a four-phase project to create a basic clone of the AirBnB web app. In this first phase, a basic console was created using the Cmd Python module to manage the objects of the whole project, being able to implement the methods create, show, update, all, and destroy to the existing classes and subclasses.

## Environment 💻

The console was developed in Ubuntu 14.04LTS using python3 (version 3.10.8).

## Further Information 📑

For further information on Python version and documentation, visit [python.org](https://www.python.org/).

## Requirements 📝

Knowledge in python3, how to use a command line interpreter, a computer with Ubuntu 20.04, python3, and pep8 style corrector.

## Repo Contents 📋

This repository contains the following files:

| File                | Description                                     |
|---------------------|-------------------------------------------------|
| AUTHORS             | Contains info about authors of the project     |
| base_model.py       | Defines BaseModel class (parent class) and methods |
| user.py             | Defines subclass User                          |
| amenity.py          | Defines subclass Amenity                       |
| city.py             | Defines subclass City                          |
| place.py            | Defines subclass Place                         |
| review.py           | Defines subclass Review                        |
| state.py            | Defines subclass State                         |
| file_storage.py     | Creates new instance of class, serializes and deserializes data |
| console.py          | Creates object, retrieves object from file, does operations on objects, updates attributes of object, and destroys object |
| test_base_model.py  | Unittests for base_model                       |
| test_user.py        | Unittests for user                              |
| test_amenity.py     | Unittests for amenity                           |
| test_city.py        | Unittests for city                              |
| test_place.py       | Unittests for place                             |
| test_review.py      | Unittests for review                            |
| test_state.py       | Unittests for state                             |
| test_file_storage.py| Unittests for file_storage                      |
| test_console.py     | Unittests for console                           |

## Installation 🛠️

Clone the repository and run the console.py

```bash
$ git clone https://github.com/------/AirBnB_clone.git
```

## Usage 🔧

| Method | Description                                       |
|--------|---------------------------------------------------|
| create | Creates an object of a given class                |
| show   | Prints the string representation of an instance based on the class name and id |
| all    | Prints all string representations of all instances based or not on the class name |
| update | Updates an instance based on the class name and id by adding or updating attributes (save the change into the JSON file) |
| destroy| Deletes an instance based on the class name and id (save the change into the JSON file) |
| count  | Retrieve the number of instances of a class       |
| help   | Prints information about a specific command      |
| quit/ EOF | Exit the program                                |
