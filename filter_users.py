"""Module to filter the users in the database by name, age and email."""
import json

def get_user_data() -> list[dict[str, int|str]]:
    """Open and loads the data of the JSON File."""
    with open("users.json", "r", encoding="utf-8") as file:
        user_data = json.load(file)
    return user_data


def filter_users_by_name(name: str, users: list[dict[str, int|str]]) -> None:
    """Print the user with the matching name in the database."""
    filtered_users = [user for user in users if user["name"].lower() == name.lower()]

    for user in filtered_users:
        print(user)


def filter_users_by_age(age: int, users: list[dict[str, int|str]]) -> None:
    """Print the user with the matching age in the database."""
    filtered_users = [user for user in users if user["age"] == age]

    for user in filtered_users:
        print(user)


def filter_users_by_email(email: str, users: list[dict[str, int|str]]) -> None:
    """Print the user with the matching email in the database."""
    filtered_users = [user for user in users if user["email"] == email.lower()]

    for user in filtered_users:
        print(user)


if __name__ == "__main__":
    filter_option = input(
        "What would you like to filter by? ('name', 'age' or 'email'): "
    ).strip().lower()

    user_database = get_user_data()

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(name_to_search, user_database)

    elif filter_option == "age":
        while True:
            try:
                age_to_search = input("Enter a age to filter users: ").strip()
                age_to_search = int(age_to_search)
                break
            except ValueError:
                print("Please enter one integer for the age.")
        filter_users_by_age(age_to_search, user_database)

    elif filter_option == "email":
        email_to_search = input("Enter an email to filter users: ").strip()
        filter_users_by_email(email_to_search, user_database)

    else:
        print("Filtering by that option is not yet supported.")
