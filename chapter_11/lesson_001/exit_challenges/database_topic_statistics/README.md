# Database Challenge: Topic Statistics

This solution shows how many entries each topic has, and the total number of topics and entries on the home page.

## Files changed or added

- `journal/views.py` — imports `Entry` and adds `topic_count` and `entry_count` to the home page context.
- `journal/templates/journal/topics.html` — shows `{{ topic.entry_set.count }}` next to each topic.
- `journal/templates/journal/index.html` — shows the totals on the home page.

## Steps

1. Copy these files into your `project_2` folder, replacing the files that already exist.
2. Save your files, start the server if it isn't running, and refresh the home page and the topics page.

No new migrations are needed for this challenge.

## What you should see

- The home page includes a line like "Topics: 1. Entries: 2." The numbers match what you have added in the admin site.
- On the topics page, each topic shows its entry count in parentheses, for example `Django Project (2)`.
