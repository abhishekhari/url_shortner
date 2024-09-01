# URL Shortening Service

A simple Python-based web application that allows you to shorten long URLs, similar to services like bit.ly. This project is built using the Flask web framework.

## Features

- Generate short URLs for long links.
- Redirect to the original URL using the short URL.
- Basic error handling for invalid short codes.

## Requirements

- Python 3.x
- Flask (install using `pip`)

## Installation

1. **Clone the repository or download the script:**

    ```bash
    git clone https://github.com/your-username/url-shortener.git
    ```

    Alternatively, you can download the `url_shortener.py` file directly.

2. **Navigate to the project directory:**

    ```bash
    cd url-shortener
    ```

3. **Install Flask:**

    Ensure you have Flask installed. You can install it via pip:

    ```bash
    pip install Flask
    ```

## Usage

1. **Run the Application:**

    Run the `url_shortener.py` script using Python:

    ```bash
    python url_shortener.py
    ```

    This will start the Flask development server on `http://127.0.0.1:5000/`.

2. **Access the Application:**

    Open your web browser and navigate to:

    ```
    http://127.0.0.1:5000/
    ```

3. **Shorten a URL:**

    - Enter the URL you want to shorten in the input field and click the "Shorten URL" button.
    - The shortened URL will be displayed on the page.

4. **Use the Shortened URL:**

    - Copy the shortened URL and paste it into your browser's address bar to be redirected to the original URL.

5. **Error Handling:**

    - If you attempt to access a short code that does not exist, an error message will be displayed.

## Example

1. **Enter URL:**
    - Input: `https://www.example.com/very/long/url/path`
    
2. **Shortened URL:**
    - Output: `http://127.0.0.1:5000/abc123`
    
3. **Redirection:**
    - Visiting `http://127.0.0.1:5000/abc123` redirects to `https://www.example.com/very/long/url/path`.

## File Structure

- `url_shortener.py` - The main Python script for the application.

## Notes

- This is a basic implementation that uses an in-memory dictionary to store URL mappings. All data will be lost when the server is restarted.
- To make this service more robust, consider using a persistent database like SQLite, PostgreSQL, or MongoDB.


## Contributing

If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

