#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    The user repository defines the basic interactions between our backend and database
"""
from database.tables import User
from services.profile_photo import fetch_profile_photo
from sqlalchemy import delete, func, insert, select, update


class UserRepository:
    """
    A repository for managing CRUD operations on user data in the database.

    This class encapsulates the logic required to access and modify user records, providing a clean
    and easy interface for interactions with the database related to user entities.

    Attributes:
        connection (Connection): The database connection to execute database operations.
    """

    def __init__(self, connection):
        """
        Initialize the UserRepository with a database connection.

        Args:
            connection (Connection): A database connection object.
        """
        self.connection = connection

    def create(self, user_data):
        """
        Create a new user in the database using the provided user data.

        Args:
            user_data (dict): A dictionary containing details of the user to be created.

        Returns:
            None: Indicates the user was created successfully in the database.
        """
        query = insert(User).values(
            first_name=user_data["first_name"],
            last_name=user_data["last_name"],
            email=user_data["email"],
            phone_number=user_data["phone_number"],
            profile_photo=fetch_profile_photo(),
        )
        self.connection.execute(query)
        self.connection.commit()

    def update(self, user_id, user_data):
        """
        Update an existing user's details in the database.

        Args:
            user_id (int): The ID of the user to update.
            user_data (dict): A dictionary containing updated details for the user.

        Returns:
            User: The updated user object, reflecting the changes made.
        """
        query = (
            update(User)
            .where(User.id == user_id)
            .values(
                first_name=user_data.get("first_name"),
                last_name=user_data.get("last_name"),
                email=user_data.get("email"),
                phone_number=user_data.get("phone_number"),
            )
            .execution_options(synchronize_session="fetch")
        )
        self.connection.execute(query)
        self.connection.commit()

        return self.get_by_id(user_id)

    def delete(self, user_id):
        """
        Delete a user from the database based on their user ID.

        Args:
            user_id (int): The ID of the user to delete.

        Returns:
            None: Indicates the user was deleted successfully from the database.
        """
        query = delete(User).where(User.id == user_id)
        self.connection.execute(query)
        self.connection.commit()

    def get_all(self, page=1, page_size=10):
        """
        Retrieve all users from the database with pagination.

        Args:
            page (int): The current page number.
            page_size (int): The number of users to return per page.

        Returns:
            list: A list of user objects corresponding to the current page.
        """
        offset = (page - 1) * page_size
        query = select(User).offset(offset).limit(page_size)
        result = self.connection.execute(query)
        users = result.mappings().all()
        return users

    def get_total_count(self):
        """
        Get the total count of users in the database.

        Returns:
            int: The total number of users in the database.
        """
        query = select(func.count()).select_from(User)
        result = self.connection.execute(query)
        total_count = result.scalar()
        return total_count

    def get_by_id(self, user_id):
        """
        Retrieve a single user by their ID from the database.

        Args:
            user_id (int): The ID of the user to retrieve.

        Returns:
            User: The retrieved user object if found, otherwise None.
        """
        query = select(User).where(User.id == user_id)
        result = self.connection.execute(query)
        user = result.mappings().first()
        return user if user else None
