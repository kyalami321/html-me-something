from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return "Hello World"

app.run()

<!DOCTYPE html>
<html>
<head>
<title>Nothing Interests Humans More Than Other Humans</title>
</head>
<header>
Article by Tomas Monzon</header>
<body>
<main>
<article>


