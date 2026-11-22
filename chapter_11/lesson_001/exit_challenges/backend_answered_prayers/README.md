# Backend Challenge: Answered Prayers

This solution adds a `status` field to `Entry` and a page at `/answered/` that lists prayers marked Answered.

## Files changed or added

- `journal/models.py` — adds `status` to `Entry` (`ANS` or `ONG`, default `ONG`). The `date_modified` field from the lesson is still here.
- `journal/admin.py` — registers `Topic` and `Entry` so you can edit status in the admin site.
- `journal/urls.py` — adds the `/answered/` path.
- `journal/views.py` — imports `Entry` and adds the `answered` view, which filters `status='ANS'`.
- `journal/templates/journal/answered.html` — new template for the answered list.
- `journal/templates/journal/base.html` — adds an Answered Prayers link.

## Steps

1. Copy these files into your `project_2` folder, replacing the files that already exist.
2. In the terminal, from `project_2` with `(.venv)` showing, run:

   `python manage.py makemigrations`

   then

   `python manage.py migrate`
3. Start the server, open the admin site, and set at least one entry's status to **Answered**.
4. Visit [http://127.0.0.1:8000/answered/](http://127.0.0.1:8000/answered/).

## What you should see

- An **Answered Prayers** link next to **Prayer Topics** on every page.
- The `/answered/` page lists only entries whose status is Answered, with the topic name and the date. If none are answered yet, it says "No answered prayers have been recorded yet."
