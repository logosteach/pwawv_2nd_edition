# Set Up a Python Virtual Environment

Think of a virtual environment as a *bubble* around one project. Software you install inside the bubble only affects that project, not the rest of your computer. That means one project can use Django 6.1.3 while another uses a different version, and the two will not conflict.

This page shows you how to create a virtual environment named `.venv` on your own machine, activate it, install a pinned package, and turn it off when you are done. Work in your project folder the whole time (for Chapter 11, that folder is `project_2`). In VS Code, open the project folder first, then open a terminal with **Terminal > New Terminal**.

## How the Create Command Works

You will type a short command like `py -m venv .venv` or `python3 -m venv .venv`. Here is what the pieces mean:

- `-m` tells Python to run a *module* (a packaged set of tools).
- `venv` is the module that creates virtual environments.
- `.venv` is the name of the folder it creates. The leading dot makes it a hidden folder. You will still see it in VS Code. In File Explorer or Finder, you may need to turn on "show hidden files" to see it.

## Check That Python Is Installed, Then Create and Activate

Go to the section for your operating system. You need Python 3.12 or newer for the projects in this course.

## Windows 11

In PowerShell, check that Python is installed:

```powershell
py --version
```

If that command does not work, try:

```powershell
python --version
```

You should see a version number, such as:

```terminal
Python 3.13.5
```

If neither command works, install Python 3.12 or newer from [python.org](https://www.python.org/downloads/) and try again, or ask your instructor for help.

From your project folder, create the virtual environment. Use the same Python command that worked above:

```powershell
py -m venv .venv
```

If that does not work, use:

```powershell
python -m venv .venv
```

Then activate it:

```powershell
.venv\Scripts\activate
```

**Note:** If PowerShell says running scripts is disabled on this system, follow the [Windows guide for enabling PowerShell scripts](windows_enable_scripts.md), then activate again.

When it works, your prompt starts with `(.venv)`:

```terminal
(.venv) PS C:\Users\YourName\project_2>
```

## macOS

In Terminal, check that Python is installed:

```bash
python3 --version
```

You should see a version number, such as:

```terminal
Python 3.13.5
```

If the command does not work, install Python 3.12 or newer from [python.org](https://www.python.org/downloads/) and try again, or ask your instructor for help.

From your project folder, create the virtual environment:

```bash
python3 -m venv .venv
```

Then activate it:

```bash
source .venv/bin/activate
```

When it works, your prompt starts with `(.venv)`:

```terminal
(.venv) yourname@computer project_2 %
```

## Linux (Debian/Ubuntu)

In the terminal, check that Python is installed:

```bash
python3 --version
```

You should see a version number, such as:

```terminal
Python 3.13.5
```

If the command does not work, install Python 3.12 or newer with your package manager, or ask your instructor for help.

From your project folder, create the virtual environment:

```bash
python3 -m venv .venv
```

If you get an error that `venv` or `ensurepip` is not available, install the missing package and try the create command again:

```bash
sudo apt install python3-venv
python3 -m venv .venv
```

Then activate it:

```bash
source .venv/bin/activate
```

When it works, your prompt starts with `(.venv)`:

```terminal
(.venv) yourname@computer:~/project_2$
```

## After You Activate

Once the virtual environment is active, `python` and `pip` work the same way on Windows, macOS, and Linux. You no longer need `py` or `python3` for the rest of these steps.

Upgrade `pip`, Python's package installer:

```
python -m pip install --upgrade pip
```

Install a package at a specific version with `==`. For the Chapter 11 prayer journal, that looks like this:

```
pip install django==6.1.3
```

Check what is installed:

```
pip list
```

You should see `Django` at version `6.1.3`, along with a few packages Django depends on. Your other version numbers may be a little different. That is normal.

## Deactivate the Virtual Environment

When you are finished working, leave the bubble with:

```
deactivate
```

The `(.venv)` prefix disappears from your prompt. Your project files stay on your computer. The next time you work on the project, activate the environment again with the same activate command for your operating system.

## Select the Interpreter in VS Code

VS Code needs to know it should use the Python inside `.venv`. Open the Command Palette with `Ctrl+Shift+P` (Windows or Linux) or `Cmd+Shift+P` (macOS), then choose **Python: Select Interpreter**. Pick the interpreter that points at your project's `.venv` folder.

You can also click the Python version in the Status Bar at the bottom of the VS Code window and choose `.venv` from the list.

## Don't Commit `.venv` to Git

A virtual environment is disposable, and it should not be checked into Git. Add `.venv/` to a `.gitignore` file in your project folder so the environment is not committed. You can always delete it and create it again.

## If Your Virtual Environment Breaks

If the environment stops working, delete the `.venv` folder in File Explorer, Finder, or your file manager (you may need to show hidden files first). Then go back to your project folder and create the environment again with the same create command for your operating system. Your project files, such as `spec.md`, are not inside `.venv`, so they will still be there.

For more detail, see Python's [venv documentation](https://docs.python.org/3/library/venv.html) and the [VS Code Python environments guide](https://code.visualstudio.com/docs/python/environments).
