from flask import Flask, request, render_template_string

app = Flask(__name__)

FLAG = open("/flag.txt").read()

with open("index.html") as f:
    TEMPLATE = f.read()


@app.route("/")
def index():
    name = request.args.get("name", "")
    if name:
        greeting_html = f"<h3>Hello, {name}!</h3>"
        page = TEMPLATE.replace("<!-- greeting -->", greeting_html)
    else:
        page = TEMPLATE
    return render_template_string(page)


if __name__ == "__main__":
    print(f"Flag: {FLAG}")
    app.run(host="0.0.0.0", port=8080)
