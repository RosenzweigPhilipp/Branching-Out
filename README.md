# User Filter Application

A Python application that allows you to filter users from a JSON file based on different criteria such as name, age, and email address.

## Features

- **Name Filtering**: Search for users by their name (case-insensitive)
- **Age Filtering**: Find users by their exact age with input validation
- **Email Filtering**: Search for users by their email address (case-insensitive)
- **Error Handling**: Robust error handling for file operations and user input
- **Type Safety**: Full type annotations for better code maintainability
- **Clean Architecture**: Well-organized code following PEP 8 guidelines

## Requirements

- Python 3.9 or higher
- A `users.json` file containing user data

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/RosenzweigPhilipp/Branching-Out.git
   cd Branching-Out
   ```

2. Ensure you have a `users.json` file in the same directory as `filter_users.py`

## Usage

### Running the Application

```bash
python filter_users.py
```

The application will prompt you to choose a filtering option and then ask for the search criteria.

### Example Interactions

#### Filter by Name
```
What would you like to filter by? (name/age/email): name
Enter a name to filter users: John
{'name': 'John Doe', 'age': 25, 'email': 'john.doe@example.com'}
```

#### Filter by Age
```
What would you like to filter by? (name/age/email): age
Enter an age to filter users: 30
{'name': 'Jane Smith', 'age': 30, 'email': 'jane.smith@example.com'}
```

#### Filter by Email
```
What would you like to filter by? (name/age/email): email
Enter an email to filter users: admin@company.com
{'name': 'Admin User', 'age': 35, 'email': 'admin@company.com'}
```

## JSON File Format

The `users.json` file should contain an array of user objects with the following structure:

```json
[
    {
        "name": "John Doe",
        "age": 25,
        "email": "john.doe@example.com"
    },
    {
        "name": "Jane Smith",
        "age": 30,
        "email": "jane.smith@example.com"
    }
]
```

## Code Structure

### Functions

- **`load_users(filename)`**: Loads user data from a JSON file with error handling
- **`display_users(users)`**: Displays a list of users in a formatted way
- **`filter_users_by_name(name, users)`**: Filters users by name (case-insensitive)
- **`filter_users_by_age(age_input, users)`**: Filters users by age with input validation
- **`filter_users_by_email(email, users)`**: Filters users by email (case-insensitive)
- **`get_user_input()`**: Handles user input for filter criteria
- **`main()`**: Main application logic

### Key Features

- **Type Annotations**: All functions include comprehensive type hints
- **Google-Style Docstrings**: Complete documentation for all functions
- **Error Handling**: Graceful handling of file errors and invalid input
- **PEP 8 Compliance**: Code follows Python style guidelines
- **Modular Design**: Functions are reusable and testable

## Error Handling

The application handles several types of errors:

- **FileNotFoundError**: When the `users.json` file doesn't exist
- **JSONDecodeError**: When the JSON file is malformed
- **ValueError**: When invalid age input is provided
- **Missing Fields**: Gracefully handles missing user data fields

## Development

### Code Quality

This project follows Python best practices:

- PEP 8 style guidelines
- Comprehensive type annotations
- Google-style docstrings
- Modular function design
- Robust error handling

### Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature-name`)
3. Make your changes following the existing code style
4. Add appropriate tests if needed
5. Commit your changes (`git commit -am 'Add some feature'`)
6. Push to the branch (`git push origin feature-name`)
7. Create a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).

## Version History

- **v1.0.0**: Initial release with basic filtering functionality
- **v1.1.0**: Added age filtering capability
- **v1.2.0**: Added email filtering capability
- **v2.0.0**: Major refactor with type annotations, improved error handling, and PEP 8 compliance

## Author

**Philipp Rosenzweig**
- GitHub: [@RosenzweigPhilipp](https://github.com/RosenzweigPhilipp)

## Acknowledgments

- Built as part of a Git branching and workflow learning exercise
- Demonstrates best practices in Python development and version control