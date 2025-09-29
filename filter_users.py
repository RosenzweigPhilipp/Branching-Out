"""User filtering application with multiple search criteria.

This module provides functionality to filter users from a JSON file based on
different criteria such as name, age, and email address.
"""

import json
from typing import List, Dict, Any, Optional


def load_users(filename: str = "users.json") -> List[Dict[str, Any]]:
    """Load users from a JSON file.
    
    Args:
        filename: The name of the JSON file containing user data.
        
    Returns:
        A list of dictionaries containing user information.
        
    Raises:
        FileNotFoundError: If the specified JSON file doesn't exist.
        json.JSONDecodeError: If the JSON file is malformed.
    """
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return []
    except json.JSONDecodeError:
        print(f"Error: The file '{filename}' contains invalid JSON.")
        return []


def display_users(users: List[Dict[str, Any]]) -> None:
    """Display a list of users in a formatted way.
    
    Args:
        users: A list of user dictionaries to display.
    """
    if users:
        for user in users:
            print(user)
    else:
        print("No users found matching the criteria.")


def filter_users_by_name(name: str, users: Optional[List[Dict[str, Any]]] = None) -> None:
    """Filter users by name (case-insensitive).
    
    Args:
        name: The name to search for.
        users: Optional list of users. If None, users will be loaded from file.
    """
    if users is None:
        users = load_users()
    
    if not users:
        return
    
    filtered_users = [
        user for user in users 
        if user.get("name", "").lower() == name.lower()
    ]
    
    display_users(filtered_users)


def filter_users_by_age(age_input: str, users: Optional[List[Dict[str, Any]]] = None) -> None:
    """Filter users by age.
    
    Args:
        age_input: The age to search for as a string.
        users: Optional list of users. If None, users will be loaded from file.
    """
    if users is None:
        users = load_users()
    
    if not users:
        return
    
    try:
        age = int(age_input)
        filtered_users = [
            user for user in users 
            if user.get("age") == age
        ]
        
        if filtered_users:
            display_users(filtered_users)
        else:
            print(f"No users found with age {age}")
    except ValueError:
        print("Please enter a valid age (number).")


def filter_users_by_email(email: str, users: Optional[List[Dict[str, Any]]] = None) -> None:
    """Filter users by email address (case-insensitive).
    
    Args:
        email: The email address to search for.
        users: Optional list of users. If None, users will be loaded from file.
    """
    if users is None:
        users = load_users()
    
    if not users:
        return
    
    filtered_users = [
        user for user in users 
        if user.get("email", "").lower() == email.lower()
    ]
    
    if filtered_users:
        display_users(filtered_users)
    else:
        print(f"No users found with email {email}")


def get_user_input() -> tuple[str, str]:
    """Get filter criteria and search value from user input.
    
    Returns:
        A tuple containing the filter option and search value.
    """
    filter_option = input(
        "What would you like to filter by? (name/age/email): "
    ).strip().lower()
    
    if filter_option == "name":
        search_value = input("Enter a name to filter users: ").strip()
    elif filter_option == "age":
        search_value = input("Enter an age to filter users: ").strip()
    elif filter_option == "email":
        search_value = input("Enter an email to filter users: ").strip()
    else:
        return filter_option, ""
    
    return filter_option, search_value


def main() -> None:
    """Main function to run the user filtering application."""
    filter_option, search_value = get_user_input()
    
    if filter_option == "name":
        filter_users_by_name(search_value)
    elif filter_option == "age":
        filter_users_by_age(search_value)
    elif filter_option == "email":
        filter_users_by_email(search_value)
    else:
        print("Filtering by that option is not yet supported.")


if __name__ == "__main__":
    main()
