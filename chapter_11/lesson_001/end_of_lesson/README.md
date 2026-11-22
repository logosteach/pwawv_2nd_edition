# End of Lesson 1

This folder holds a finished copy of the prayer journal as it stands at the end of Chapter 11, Lesson 1, after the walkthrough and before the Exit Challenges.

Use it to compare your own `project_2` files with these. The files are inside [project_2](project_2/). Each file you typed in the lesson starts with a path comment, such as `# project_2/journal/views.py`, so you can tell which file you're looking at.

This copy does not include a database, a virtual environment, or a real `SECRET_KEY`. The `settings.py` file uses a placeholder key. Keep the key Django created in your own project.

## How to run this copy

1. Copy the `project_2` folder to your computer, or download it from this repository.
2. Open that folder in VS Code and create a virtual environment inside it. On Windows 11, macOS, or Linux, follow the [virtual environment setup guide](../../../setup/virtual_environments.md). If PowerShell says running scripts is disabled, follow the [Windows guide for enabling PowerShell scripts](../../../setup/windows_enable_scripts.md).
3. With `(.venv)` showing at the start of your prompt, install the same Django version used in the lesson:

   `pip install django==6.1.3`
4. Build the database:

   `python manage.py migrate`
5. Create an admin account:

   `python manage.py createsuperuser`
6. Start the server:

   `python manage.py runserver`

   Then open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser. Log in at [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) and add a topic, such as "Django Project," plus an entry or two, so the topics page and each topic page have something to show.

The Exit Challenges are separate. Their solutions are in [../exit_challenges](../exit_challenges/).
