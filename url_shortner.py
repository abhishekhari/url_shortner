from flask import Flask, request, redirect, render_template_string, url_for
import string
import random

app = Flask(__name__)

# In-memory database to store the URL mappings
url_mapping = {}

# Function to generate a short code
def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits
    short_code = ''.join(random.choice(characters) for _ in range(length))
    return short_code

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        original_url = request.form['original_url']
        short_code = generate_short_code()

        # Ensure the short code is unique
        while short_code in url_mapping:
            short_code = generate_short_code()

        # Store the short code and original URL
        url_mapping[short_code] = original_url

        short_url = request.host_url + short_code
        return render_template_string(TEMPLATE, short_url=short_url)

    return render_template_string(TEMPLATE)

@app.route('/<short_code>')
def redirect_to_url(short_code):
    original_url = url_mapping.get(short_code)

    if original_url:
        return redirect(original_url)
    else:
        return render_template_string(ERROR_TEMPLATE, short_code=short_code)

TEMPLATE = '''
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>URL Shortener</title>
</head>
<body>
    <h1>URL Shortener</h1>
    <form method="post">
        <label for="original_url">Enter the URL to shorten:</label><br>
        <input type="text" id="original_url" name="original_url" required><br><br>
        <input type="submit" value="Shorten URL">
    </form>
    {% if short_url %}
    <h2>Your shortened URL:</h2>
    <a href="{{ short_url }}" target="_blank">{{ short_url }}</a>
    {% endif %}
</body>
</html>
'''

ERROR_TEMPLATE = '''
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>URL Shortener - Error</title>
</head>
<body>
    <h1>Error: Invalid URL</h1>
    <p>The short URL code "{{ short_code }}" does not exist.</p>
    <a href="{{ url_for('index') }}">Go back to the home page</a>
</body>
</html>
'''

if __name__ == '__main__':
    app.run(debug=True)
