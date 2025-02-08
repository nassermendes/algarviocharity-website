# Algarvio Charity Website

This is the official website for Algarvio Charity, serving the Algarve community.

## About

Algarvio Charity is dedicated to making a positive impact in the Algarve region through various community initiatives and support programs.

## Project Structure

```
algarviocharity-website/
├── app/                    # Flask application package
│   ├── __init__.py        # Application factory
│   └── routes.py          # Route definitions
├── static/                # Static files
│   ├── css/              # Stylesheets
│   ├── js/               # JavaScript files
│   └── images/           # Image assets
├── templates/            # Jinja2 templates
│   ├── base.html        # Base template
│   └── index.html       # Home page template
├── config.py            # Configuration settings
├── requirements.txt     # Python dependencies
└── run.py              # Application entry point
```

## Setup and Development

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   Create a `.env` file with:
   ```
   SECRET_KEY=your-secret-key
   MAIL_USERNAME=your-email@gmail.com
   MAIL_PASSWORD=your-email-password
   ```

4. Run the development server:
   ```bash
   python run.py
   ```

## Deployment

1. Purchase domain (algarviocharity.org)
2. Set up hosting (e.g., DigitalOcean, Heroku, or PythonAnywhere)
3. Configure DNS records
4. Set up SSL certificate

## Technologies Used

- Python 3.9+
- Flask (Web Framework)
- SQLAlchemy (Database ORM)
- Flask-Mail (Email Support)
- HTML5 & CSS3
- JavaScript
- Gunicorn (Production Server)

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Development

This website is built with HTML, CSS, and JavaScript, hosted on GitHub Pages.

## Contact

For more information, visit [algarviocharity.org](https://algarviocharity.org) or email us at info@algarviocharity.org.
