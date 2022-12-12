# Part 01: Introduction to Python Programming Language

## Python Download and Install

### For Windows Users:

1. Download the installer from the official docuementation.

[Download the installer from here](https://www.python.org/downloads/)

2. Double click the downloaded executable to install Python. 

### For Mac users:

1. For Mac books there is already a pre-installed version of Python. You can check that out using the following command.

```terminal
$ python --version
```

If your Mac has Python3 installed you can check out its version using the following command

```terminal
$ python3 --version
```

[We'll just follow the instructions on this website to have Python installed](https://www.makeuseof.com/how-to-install-python-on-mac/)


### For Linux users:

Linux already comes with a pre-installed version of Python just like the Mac, but its likely python2.7. In this tutorial we want to use python 3.8 and above. Let's update our Python version.

To check the Python 2 version you have installed, run:

```terminal
$ python2 --version
```

To check if you have Python3 installed run:

```terminal
$ python3 --version
```

If you don't have python3 installed, you'll want to install it using the following set of commands:

```terminal
$ sudo apt update

$ sudo apt install software-properties-common

$ sudo add-apt-repository ppa:deadsnakes/ppa

$ sudo apt install python3.10 python3.10-venv python3.10-dev

$ python3 --version

$ python3.10 --version
```

[You can read more about installation from this repository](https://linuxhint.com/update-python-ubuntu/#:~:text=You%20need%20to%20use%20the,system%20for%20new%20Python%20versions.)


## Running your python code

Once we have python installed we can run Python code right in the terminal without having to do anything else. Use the following commands:

```terminal
$ python3
```

This will open up the Python interpretar, you can write Python code in here

```terminal
>>> print("Hello world")
```

To exit use the command below:

```terminal
>>> exit()
```

## Installing An IDE:

### Windows And Mac

An IDE: Integrated development environment

After installing python you can use the IDE Python comes with by default.

In this tutorial we'll learn how to setup our own environment for coding.

We'll install vs code

[Follow this link to install vs code for Windows and Mac](http://code.visualstudio.com/)


### Linux setup

For Linux, we'll use the snap to install it with snap and the ubuntu software store:

```terminal
$ sudo snap install --classic code
```

To use the Ubuntu software store open the application and type in the name `code`. Find the one with the blue vs logo.


Once done we can now open VS code through the terminal using:

```terminal
$ code .
```

```terminal
$ code --version
```

If you do not have the microsoft repo on your machine. Read [here](https://phoenixnap.com/kb/install-vscode-ubuntu)


## Installing Extensions

Now we have to install a couple of extends to ready coding. Open vs code and follow along

- `python` extension
- `prettier` for code formatting
- `autopep8` for formatting code according to the Python standards
- `code runner` provides play button to run your code from vs-code without having to use the terminal

Once done, let's begin to write our programs.

## Writting Your First Program

1. Create a folder on your desktop. Make sure you have navigated to your desktop or where you want to keep your folder.


Run this command to create your folder

```terminal
$ mkdir introToPython
```

Run this command to open up VS-code

```terminal
$ code .
```

Create a folder called `basics` in vs-code. Inside this folder create a file called `part_01.py`

Add the following content:

```python
print("Hello world")
```

Navigate back to your terminal/cmd and run:

```terminal
python3 basics/part_01.py
```

This will run the code.
