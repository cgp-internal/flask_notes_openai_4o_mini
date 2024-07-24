# Note Taking Application

This project is a simple note-taking application built using Flask. It allows users to create, read, update, and delete notes. 

## Project Structure

- `app.py`: Main entry point for the Flask application.
- `routes/note.py`: Defines RESTful routes for CRUD operations for notes.
- `models/note.py`: Defines the Note model and handles CSV interactions.
- `data/notes.csv`: Stores the notes data with initial example notes.
- `README.md`: Basic documentation and project overview.
- `.gitignore`: Excludes unnecessary files from version control.
- `run.sh`: Bash script for setup and running the application.
- `requirements.txt`: Lists necessary Python packages.

## Getting Started

### Prerequisites

Ensure you have Python and pip installed. It is recommended to use a virtual environment.

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Run the setup script:
   ```bash
   bash run.sh
   ```
   This will set up the virtual environment and install dependencies.

### Running the Application

To start the application, run the following command:
```bash
python app.py
```

The application will be accessible at `http://127.0.0.1:5000/`.

## Usage

Once the application is running, you can use the following endpoints for various operations:

- **Create a Note**: `POST /notes`
- **Read all Notes**: `GET /notes`
- **Read a Note by ID**: `GET /notes/<id>`
- **Update a Note**: `PUT /notes/<id>`
- **Delete a Note**: `DELETE /notes/<id>`

## Contributing

Contributions are welcome! Please feel free to submit a pull request.

## License

This project is open source and available under the MIT License.