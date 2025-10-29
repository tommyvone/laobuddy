# LaoBuddy

A feature-rich social media platform built with Python Flask, designed to connect people and foster meaningful interactions.

## About

LaoBuddy is a modern social networking application that enables users to share content, connect with friends, engage in conversations, and build communities. Built with scalability and user experience in mind, it provides a comprehensive set of social features in a clean, intuitive interface.

## Features

### Core Functionality
- **User Authentication**: Secure signup, login, logout, and password reset
- **User Profiles**: Customizable profiles with avatar and cover photo uploads
- **Posts & Content**: Share text, images, and videos with your network
- **Social Interactions**: Like, comment, and share posts
- **News Feed**: Personalized feed with chronological or ranked content
- **Relationships**: Follow users or send friend requests
- **Direct Messaging**: Private 1:1 and group conversations
- **Notifications**: Real-time updates for interactions and activities
- **Search**: Find users, posts, and content across the platform
- **Moderation Tools**: Admin panel for content moderation and user management

### Security & Privacy
- CSRF protection
- Secure session management
- XSS and SQL injection prevention
- Content security policy
- Password hashing with industry standards
- Privacy controls for profiles and posts

## Tech Stack

### Backend
- **Python 3.10+**
- **Flask**: Web framework
- **SQLAlchemy**: ORM for database operations
- **Alembic**: Database migrations
- **Flask-Login**: User session management
- **Flask-WTF**: Form handling and validation
- **Celery**: Background task processing
- **Redis**: Caching and message queues

### Frontend
- **Jinja2**: Template engine
- **HTML/CSS/JavaScript**
- Responsive design for mobile and desktop

### Database
- **PostgreSQL** or **MySQL**

### Deployment
- **Gunicorn**: WSGI HTTP server
- **Nginx**: Reverse proxy and static file serving

## Installation

### Prerequisites
- Python 3.10 or higher
- PostgreSQL or MySQL
- Redis (for caching and background tasks)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/laobuddy.git
cd laobuddy
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your configuration
```

5. Initialize the database:
```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

6. Run the development server:
```bash
flask run
```

Visit `http://localhost:5000` to see the application.

## Configuration

Create a `.env` file in the root directory with the following variables:

```env
FLASK_APP=app.py
FLASK_ENV=development
SECRET_KEY=your-secret-key-here
DATABASE_URL=postgresql://user:password@localhost/laobuddy
REDIS_URL=redis://localhost:6379/0
```

## Project Structure

```
laobuddy/
├── app/
│   ├── __init__.py
│   ├── models/          # Database models
│   ├── routes/          # Application routes/blueprints
│   ├── templates/       # Jinja2 templates
│   ├── static/          # CSS, JS, images
│   └── utils/           # Helper functions
├── migrations/          # Database migrations
├── tests/              # Test suite
├── config.py           # Configuration settings
├── requirements.txt    # Python dependencies
└── run.py             # Application entry point
```

## Development

### Code Formatting
This project uses Black for code formatting:

```bash
black .
```

### Running Tests
```bash
pytest
```

### Database Migrations
Create a new migration:
```bash
flask db migrate -m "Description of changes"
```

Apply migrations:
```bash
flask db upgrade
```

## Roadmap

- [ ] Enhanced search with full-text indexing
- [ ] Real-time messaging with WebSockets
- [ ] Mobile app (iOS/Android)
- [ ] Advanced analytics dashboard
- [ ] API for third-party integrations
- [ ] Internationalization (i18n) support
- [ ] Stories and ephemeral content
- [ ] Video calling features

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

Please ensure your code:
- Follows PEP 8 style guidelines
- Includes appropriate tests
- Is formatted with Black
- Includes documentation for new features

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

If you encounter any issues or have questions:

- Open an issue on GitHub
- Check the [documentation](docs/)
- Join our community discussions

## Acknowledgments

- Flask community for the excellent framework
- All contributors who help improve LaoBuddy
- Open source libraries that make this project possible

---

Made with ❤️ by Tommy Bountham
