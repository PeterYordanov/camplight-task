#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    This file provides utility functionality for stablishing and managing a database connection
"""
import os

from sqlalchemy import create_engine


class ConnectionContext:
    """
    A context manager class for handling database connections.

    This class uses a context management protocol to establish and close database
    connections automatically using the connection details from the environment variables.

    Attributes:
        engine (Engine): A SQLAlchemy engine instance created from the database URL.
        connection (Connection): A connection object to interact with the database.
    """

    def __init__(self):
        """
        Initializes the ConnectionContext with a SQLAlchemy engine.
        """
        self.engine = create_engine(os.getenv("DATABASE_URL"))
        self.connection = None

    def __enter__(self):
        """
        Opens a new database connection when entering the context.

        Returns:
            Connection: A SQLAlchemy connection object.
        """
        self.connection = self.engine.connect()
        return self.connection

    def __exit__(self, type, value, traceback):
        """
        Closes the database connection when exiting the context.

        Args:
            type (Type): The type of exception raised (if any).
            value (Exception): The exception instance raised (if any).
            traceback (Traceback): The traceback object of the exception (if any).
        """
        self.connection.close()


def get_connection():
    """
    Generator function to yield a database connection.

    Yields:
        Connection: A connection object from a database, ensuring the connection
        is closed after use.

    Usage:
        with get_connection() as connection:
            # perform database operations
    """
    with ConnectionContext() as connection:
        yield connection
