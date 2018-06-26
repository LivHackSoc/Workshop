# Go Programming Language

<img src="https://github.com/LivHackSoc/Workshop/blob/master/go/resource/images/mascot.png" height="400px">

Go is an open source programming language created by Google in 2009. The main team consists of people who was part of the C programming language and Unix development. Positive aspect of Go includes:

* The syntax combines the best of many prpgramming languages e.g. C, Python and JavaScript
* Statically typed (includes memory safety, garbage collection and more)
* Extremely fast to build. Very efficient compiler
* Takes advantages of multiple core, hence it is popular for concurrent programming
* Does not include many boilerplate (looking at you Java)

# Section 

* Installation
* Foundation
* Intermediate 
* Advance

# Foundation

## Main

Always include the package main at the start. The main() function is the entry point of the program. For example you want to call functions inside this. It is similar to Java's main method. 

<img src="https://github.com/LivHackSoc/Workshop/blob/master/go/resource/images/screenshots/f1.png" height="250px">

## Variables 

To declare a variable with a type. There are many types you can choose from.

<img src="https://raw.githubusercontent.com/LivHackSoc/Workshop/master/go/resource/images/screenshots/f2.png" height="250px">

You can also declare variable without type with the operator __:=__, the compiler will automatically guess the type for you.

<img src="https://github.com/LivHackSoc/Workshop/blob/master/go/resource/images/screenshots/f3.png" height="250px">

You can declare costant with **const** keyword.

<img src="https://github.com/LivHackSoc/Workshop/blob/master/go/resource/images/screenshots/f4.png" height="250px">


## Data Structures

**Array** in Go is fixed size (how many element it can hold). You must always declare the size and the type.

<img src="https://github.com/LivHackSoc/Workshop/blob/master/go/resource/images/screenshots/f5.png" height="250px">

However, without the size you will create a **splice**.

<img src="https://github.com/LivHackSoc/Workshop/blob/master/go/resource/images/screenshots/f6.png" height="250px">

The **map** is a data structure which contains a key and a corresponding value. Similar to Python's dictionary.

<img src="https://github.com/LivHackSoc/Workshop/blob/master/go/resource/images/screenshots/f7.png" height="250px">

**Map** operations you can perform.

<img src="https://github.com/LivHackSoc/Workshop/blob/master/go/resource/images/screenshots/f8.png" height="250px">