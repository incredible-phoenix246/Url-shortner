
# URL Shortener

A simple URL shortening web application built using Django.

## Description

The URL Shortener is a web application that allows users to convert long URLs into shorter, more manageable links. This project is built using Django, providing a straightforward interface to input long URLs and generate shortened versions.

## Features

- Shorten long URLs to more concise forms.
- Redirection from shortened URLs to their original destinations.
- User-friendly interface for URL input and copy functionality.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/breezeconcept/URL-Shortner.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd url-shortener
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the server:**

    ```bash
    python manage.py runserver
    ```

5. **Access the application:**

    Open your web browser and go to `http://localhost:8000/`.

## Usage

1. Access the home page at `http://localhost:8000/`.
2. Enter a long URL into the input field.
3. Click the "Shorten URL" button to generate a shortened link.
4. Copy the shortened URL by clicking the "Copy" button.
5. Paste the shortened URL where needed.

## Folder Structure

The project's folder structure is as follows:

- **`url_shortener/`**: Django app directory containing application files.
- **`manage.py`**: Django's command-line utility for administrative tasks.
- **`requirements.txt`**: List of Python dependencies.

## Technologies Used

- Python
- Django
- HTML
- CSS
- JavaScript

## Contributing

Contributions are welcome! Please fork the repository, make changes, and create a pull request. For major changes, please open an issue first to discuss the proposed changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- This project is based on the Django web framework.
- Inspired by the need for a simple URL shortener.

