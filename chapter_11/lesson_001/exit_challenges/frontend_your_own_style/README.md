# Frontend Challenge: Your Own Style

This solution adds a custom stylesheet and loads it from `base.html`. Your own colors and fonts can be different; this is one simple starting point, including hover effects on links.

## Files changed or added

- `static/css/custom.css` — new stylesheet for the header and pages.
- `journal/templates/journal/base.html` — loads `custom.css` with `{% load static %}` and a link tag. The logo and Prayer Topics link from the lesson are still here.

## Steps

1. Create a `css` folder inside your `project_2/static` folder if it isn't there yet.
2. Copy `custom.css` into `project_2/static/css/`.
3. Copy `base.html` into `project_2/journal/templates/journal/`, replacing the file that already exists.
4. Save your files, start the server if it isn't running, and refresh each page.

## What you should see

- The pages use the fonts and colors from `custom.css`.
- Links in the header change color and show an underline when you hover over them.
- The home, topics, and topic pages still work as they did at the end of the lesson.
