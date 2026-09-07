# 🎧 Mixtape Maker

A desktop GUI application built with Python and `customtkinter` that lets users curate a custom mixtape by selecting favorite genres and artists, generating personalized track recommendations, and emailing the finished playlist to a friend.

## Features

- **Genre Selection** — Browse and select from a list of available genres to shape your mixtape's vibe.
- **Artist Search** — Search for favorite artists by name, view matching results in a formatted table, and add them to your selections.
- **Selection Management** — Store, view, and clear your chosen genres and artists at any point before generating your mixtape.
- **Mixtape Generation** — Generate a list of recommended tracks based on your selected artists and genres.
- **Email Delivery** — Send your generated mixtape as a nicely formatted HTML track list directly to an email address.

## How It Works

The app is structured around a simple main menu that routes to different actions:

| Action | Description |
|---|---|
| **Main Menu** | Displays currently selected genres and artists |
| **Select Genres** | Choose favorite genres from the available list |
| **Select Artists** | Search for and add artists to your mixtape |
| **Make Mixtape!** | Generates track recommendations and offers to email them |
| **Quit** | Closes the application |

User selections are stored in a shared `user_selections` dictionary containing:
```python
{
    'genres': [],
    'artists': {}
}
```

## Tech Stack

- **Python 3**
- **customtkinter** — for the graphical user interface
- **Custom `apis` module**:
  - `audio` — handles genre listing, artist search, and mixtape/track generation
  - `twilio` — handles sending the mixtape via email
  - `gui` — wraps `customtkinter` for simplified window, button, and input handling

## Getting Started

### Prerequisites
- Python 3.x
- `customtkinter` (`pip install customtkinter`)
- Access to the course-provided `apis` module (`audio`, `twilio`, `gui`)

### Running the App
```bash
python mixtape_maker.py
```

This launches the GUI window where you can navigate between menu actions using the on-screen buttons.

## Known Issues / Future Improvements

- Genre selection currently stores raw input as a single string rather than parsing multiple comma-separated genres.
- The "clear" command in `select_genres` is checked *after* the new value has already been appended, so it doesn't currently clear the genre list as intended.
- Input validation could be added for artist selection numbers to avoid crashes on invalid entries.


## Author

Created as part of a coursework assignment on building interactive applications with external API integrations.

