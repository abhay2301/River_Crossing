# River Crossing Game

A Django-based web application implementing the classic River Crossing puzzle, where a farmer must transport a goat, a wolf, and a cabbage across a river without leaving the goat alone with the cabbage or the wolf alone with the goat. The game features a responsive interface with Bootstrap styling, animated boat movement, and session-based state management.

## Features
- Interactive game board with left and right river banks.
- Animated boat movement using CSS transitions.
- Emoji-based icons for the farmer (👨‍🌾), goat (🐐), wolf (🐺), and cabbage (🥬).
- Win/lose conditions with alert messages.
- Restart functionality to reset the game state.
- Responsive design using Bootstrap 5.

## Prerequisites
- Python 3.13.3 (or compatible version)
- Django 5.2.4
- Virtual environment (recommended)

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/river-crossing-game.git
   cd river-crossing-game
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # On Windows
   ```

3. **Install Dependencies**:
   ```bash
   pip install django==5.2.4
   ```

4. **Apply Migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Collect Static Files**:
   - Clear any existing static files:
     ```powershell
     Remove-Item -Recurse -Force C:\Users\inmai\OneDrive\Desktop\Game\river_crossing\staticfiles
     ```
   - Run the collectstatic command:
     ```bash
     python manage.py collectstatic
     ```
   - Type `yes` when prompted to overwrite existing files.

6. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```

7. **Access the Game**:
   - Open your browser and go to `http://localhost:8000`.
   - Click "Start Game" to begin playing.

## Usage
- **Objective**: Move the farmer, goat, wolf, and cabbage from the left bank to the right bank using the boat, which can carry the farmer and one item at a time.
- **Rules**:
  - The farmer must be present to operate the boat.
  - If left alone, the goat will eat the cabbage, and the wolf will eat the goat.
  - The game ends with a win if all items are safely on the right bank, or a loss if the rules are violated.
- **Controls**:
  - Select a move option (e.g., "Farmer alone" or "Farmer with Goat") and click "Make Move".
  - Click "Restart Game" to reset after winning or losing.

## Project Structure
```
river_crossing/
├── river_crossing/           # Project configuration
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py                 # Django management script
└── game/                     # Main app
    ├── __init__.py
    ├── models.py
    ├── views.py
    ├── urls.py
    ├── static/              # Static files
    │   └── game/
    │       └── css/
    │           └── style.css
    ├── templates/           # HTML templates
    │   ├── base.html
    │   ├── landing.html
    │   └── game_board.html
    └── templatetags/        # Custom template tags
        ├── __init__.py
        └── game_tags.py
```

## Contributing
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m "Description of changes"`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## Issues
- If you encounter the `TemplateSyntaxError: Invalid block tag on line 104: 'endblock'`, ensure `game/templates/game_board.html` matches the provided version and restart the server after updates.
- Report bugs or suggest features by opening an issue on the repository.

## Last Updated
- 03:03 AM IST on Saturday, July 26, 2025

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Built with Django 5.2.4 and Bootstrap 5.3.0.
- Inspired by the classic River Crossing puzzle.