# What Is `__name__`?

*Why we write `if __name__ == "__main__": unittest.main()`*

**UNIT: TESTING CODE IN PYTHON  •  MINI-LESSON**

- **Course:** Intro to Python
- **Teacher:** John Partridge (Mr. P)
- **Grade Level:** 9–12
- **Unit:** Testing Code in Python

In every `unittest` file you have seen so far, this short block appears at the bottom:

```python
if __name__ == "__main__":
    unittest.main()
```

It looks mysterious at first. This mini-lesson explains exactly what it does and why Python programmers write it so often.

## The Special Variable `__name__`

Every Python file (called a **module**) has a special built-in variable named `__name__`. Python sets its value automatically in one of two ways:

| How the file is used | Value of `__name__` | Example |
|---|---|---|
| You run the file **directly** (`python test_calculator.py`) | `"__main__"` | The file is the main program |
| Another file **imports** it (`import test_calculator`) | The module’s own name (e.g. `"test_calculator"`) | The file is being used as a library |

You can see this yourself. Create a tiny file called `name_demo.py`:

```python
print("The value of __name__ is:", __name__)
```

**Run it directly:**

```terminal
$ python name_demo.py
The value of __name__ is: __main__
```

**Import it from another file or the interactive shell:**

```python
>>> import name_demo
The value of __name__ is: name_demo
```

(The print statement still runs because it is not protected by an `if`.)

## The `if __name__ == "__main__":` Idiom

The line

```python
if __name__ == "__main__":
```

is a very common Python pattern. It means:

> “Only run the code indented under this `if` when someone executes this file as the main program. Do **not** run it when the file is imported.”

This lets one file serve two purposes:

1. **As a script** — run it and something useful happens (tests run, a program starts, a demo prints results).
2. **As a module** — other files can `import` its functions, classes, or test cases without triggering side effects.

## Why We Use It with `unittest.main()`

`unittest.main()` is the function that finds every method whose name starts with `test_`, runs those tests, and prints the familiar `.` / `F` / `E` report.

When you place it under the `if`:

```python
if __name__ == "__main__":
    unittest.main()
```

- Running `python test_calculator.py` executes the tests (because `__name__` is `"__main__"`).
- Importing the file (`import test_calculator` or `from test_calculator import TestCalculator`) does **not** automatically run the tests. You can reuse the test class or individual tests from another file if you ever need to.

Without the `if`, simply importing the test file would start the test runner every time—usually not what you want.

> **Teacher tip:** The block is optional. You can also run tests with the command  
> `python -m unittest`  
> (or `python -m unittest -v test_calculator`). That approach never needs the `if __name__` line. Many students like having both options.

## Try It Yourself

1. Open any of the earlier test files (for example `test_calculator.py`).
2. Run it directly: `python test_calculator.py`. You should see the test results.
3. Temporarily comment out the `if __name__` block, then try to import the file from the Python shell. Notice that the tests no longer start automatically.
4. Uncomment the block again.

## Quick Check

1. What value does `__name__` have when you run a file with `python filename.py`?
2. What value does it have when another file does `import filename`?
3. Why is it useful to put `unittest.main()` inside the `if __name__ == "__main__":` block instead of at the top level of the file?
4. Name one other way to run the tests that does **not** require this block.

## Key Takeaway

`if __name__ == "__main__":` is Python’s standard way of saying “This code is for when the file is the main program.” Combined with `unittest.main()`, it gives you a convenient one-command way to run your tests while still keeping the test file importable as a normal module.