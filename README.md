![GH language](https://img.shields.io/github/languages/top/TangoMan75/python-lab)
[![GH release](https://img.shields.io/github/v/release/TangoMan75/python-lab)](https://github.com/TangoMan75/python-lab/releases)
[![GH license](https://img.shields.io/github/license/TangoMan75/python-lab)]((https://github.com/TangoMan75/python-lab/blob/main/LICENSE))
[![GH stars](https://img.shields.io/github/stars/TangoMan75/python-lab)](https://github.com/TangoMan75/python-lab/stargazers)
[![Python CI](https://github.com/TangoMan75/python-lab/workflows/Python%20CI/badge.svg)](https://github.com/TangoMan75/python-lab/actions/workflows/python.yml)
![Visitors](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgithub.com%2FTangoMan75%2Fpython-lab&labelColor=%23697689&countColor=%2337d67a&style=flat)

🔬 TangoMan Python Lab
======================

#python #vanilla #back-end #training #interview #technical-interview

**🔬 TangoMan Python Lab** is a Python coding project for practicing common interview questions and coding challenges.

There are various Python scripts in the root directory that implement different algorithms and solutions to coding problems:

1. 🔄 **Ackermann**

Implements the Ackermann function, which is a classic example of a recursive function that can be used to test compilers and illustrate the concept of recursion.

2. 🔍 **BinarySearch**

Implements binary search to find an element in a sorted array. Binary search is an efficient algorithm for searching sorted data sets and relies on the divide-and-conquer technique.

3. ➕ **Factorial**

Calculates factorials recursively. Factorials are used in combinatorics and provide good examples of recursive functions.

4. 🔢 **Fibonacci**

Generates Fibonacci numbers recursively. The Fibonacci sequence illustrates recursion and has applications in mathematics and nature.

5. 💬 **FizzBuzz**

Prints numbers 1 to 100, but prints "Fizz" for multiples of 3, "Buzz" for multiples of 5, and "FizzBuzz" for multiples of both. This is a common interview screening question.

6. 👋 **HelloWorld**

Prints "Hello World!" - the traditional first program for beginner programmers.

7. ❄️ **MinTemperature**

Finds minimum temperature value from temperature data. Demonstrates algorithms for finding minimum/maximum values.

8. 🔄 **Palindrome**

Checks if a string is a palindrome. Palindromes illustrate recursion and string manipulation.

9. ✔️ **Perfect**

Checks if a number is a perfect number, where the number equals the sum of its divisors. Interesting math and recursion example.

10. 🃏 **Poker**

Evaluates poker hands. Involves evaluating combinations and ranks of cards.

11. 🥇 **PrimeNumbers**

Checks if a number is prime, where a natural number greater than 1 has no positive divisors other than 1 and itself.

12. 🔄 **Rot13**

Encodes/decodes a string using the ROT13 cipher, a simple letter substitution cipher. Basic encryption example.

13. 🔑 **SimpleJWT**

Implements JSON Web Token (JWT) encoding and decoding.

14. 💹 **Stocks**

Return an array holding the names of the top three stocks with the best average performance given two separate arrays containing stocks names and prices.

15. 🔢 **Syracuse**

Implements the Syracuse algorithm/sequence. Interesting recursion and number theory example.

16. 💸 **Taxes**

Calculates taxes on French incomes based on specified brackets.

17. 🏗️ **TowerOfHanoi**

Implements the Tower of Hanoi algorithm. A classic algorithm that illustrates recursion and dynamic programming.

18. 🔄 **VonNeumann**

Generates Von Neumann ordinal numbers. Illustrates generating recursive sequences.

✅ Unit Tests
-------------

The tests/ directory in each folder contains `unittest` test cases for testing the implementations of each algorithm.

### 📑 unittest Documentation

unittest documentation is available here: [https://docs.python.org/3/library/unittest.html](https://docs.python.org/3/library/unittest.html)

🚀 Github Actions
-----------------

This project uses Github Actions for continuous integration and testing. The `.github/workflows` directory contains YAML workflow definitions for:

- Linting: Runs `pylint` to check code style and quality on every push and pull request.
- Testing: Runs the Python unit tests on Ubuntu, against python versions _3.8_ _3.9_ and _3.10_.

The workflows help maintain code quality and ensure the tests pass on multiple python versions.

🌟 Inspiration
--------------

The following YouTube videos inspired **TangoMan Python Lab** project:

- [Coding Challenge : JS Impot.calculate()](https://www.youtube.com/watch?v=cX-5J_cy8TM)
- [FizzBuzz: One Simple Interview Question](https://www.youtube.com/watch?v=QPZ0pIK_wsc)
- [Solve This Coding Question To Win $200](https://www.youtube.com/watch?v=WDuZ_S_9vLg)
- [The Most Difficult Program to Compute? - Computerphile](https://www.youtube.com/watch?v=i7sm9dzFtEI)

💻 Dependencies
---------------

**TangoMan Python Lab** requires the following dependencies:

- Python3

---

### 🐍 Python3

#### 🐧 Install Python3 (Linux)

On linux machine enter following command

```bash
$ sudo apt-get install --assume-yes python3
```

#### 🏁 Install Python3 (Windows)

Download and install latest version from here [python.org](https://python.org)

#### 🍎 Install Python3 (OSX)

You can install python through the Homebrew package manager. Homebrew will install python-pip as well.

```bash
$ brew install python
```

---

### 🐍 Pylint

install pylint globally with pip

```bash
sudo pip install --upgrade pylint
```

> Pylint documentation https://github.com/pylint-dev/pylint

---

### 🐍 Autopep8

install autopep8 globally with pip

```bash
sudo pip install --upgrade autopep8
```

> Autopep8 documentation https://github.com/hhatto/autopep8

---

🚀 Installation
---------------

### ⚡ Step 1: Simply enter following command in your terminal

```bash
$ sh entrypoint.sh install
```

🔥 Usage
--------

Run `sh entrypoint.sh` to print help

Run tests:

```bash
sh entrypoint.sh unit
```

Lint code:

```bash
sh entrypoint.sh lint
```

Fix lint errors:

```bash
sh entrypoint.sh lint --fix
```

Uninstall:

```bash
sh entrypoint.sh uninstall
```

🤝 Contributing
---------------

Thank you for your interest in contributing to **TangoMan Python Lab**.

Please review the [code of conduct](./CODE_OF_CONDUCT.md) and [contribution guidelines](./CONTRIBUTING.md) before starting to work on any features.

If you want to open an issue, please check first if it was not [reported already](https://github.com/TangoMan75/python-lab/issues) before creating a new one.

📜 License
----------

Copyrights (c) 2024 &quot;Matthias Morin&quot; &lt;mat@tangoman.io&gt;

[![License](https://img.shields.io/badge/Licence-MIT-green.svg)](LICENSE)
Distributed under the MIT license.

If you like **TangoMan Python Lab** please star, follow or tweet about it:

[![GitHub stars](https://img.shields.io/github/stars/TangoMan75/python-lab?style=social)](https://github.com/TangoMan75/python-lab/stargazers)
[![GitHub followers](https://img.shields.io/github/followers/TangoMan75?style=social)](https://github.com/TangoMan75)
[![Twitter](https://img.shields.io/twitter/url?style=social&url=https%3A%2F%2Fgithub.com%2FTangoMan75%2Fpython-lab)](https://twitter.com/intent/tweet?text=Wow:&url=https%3A%2F%2Fgithub.com%2FTangoMan75%2Fpython-lab)

... And check my other cool projects.
