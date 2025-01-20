#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    The users endpoints provide a way to perform CRUD operations on our database for our users table
"""
import base64
from logging import getLogger

from database.connection_context import get_connection
from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from models.pagination_parameters import PaginationParams
from models.user import User
from repositories.user_repository import UserRepository
from sqlalchemy.orm import Session

router = APIRouter()
logger = getLogger(__name__)


@router.post("/")
def create(user_data: User, db: Session = Depends(get_connection)):
    """
    Create a new user in the database.

    Args:
        user_data (User): The user data from the request payload.
        db (Session): Database session dependency.

    Returns:
        JSONResponse: A response object with status code, message, and user data or error details.
    """
    try:
        logger.info("Attempting to create a new user")
        user_repo = UserRepository(db)
        user_repo.create(user_data.model_dump())

        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content={
                "message": "User created successfully",
                "data": user_data.model_dump(),
            },
        )
    except Exception as e:
        logger.exception("Failed to create user")
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"message": str(e)},
        )


@router.get("/")
def read_all(
    pagination: PaginationParams = Depends(),
    db: Session = Depends(get_connection),
):
    """
    Retrieve all users from the database with pagination.

    Args:
        pagination (PaginationParams): Pagination parameters.
        db (Session): Database session dependency.

    Returns:
        JSONResponse: A response object with all users and pagination details.
    """
    try:
        logger.info("Fetching users from database")
        user_repo = UserRepository(db)
        users = user_repo.get_all(page=pagination.page, page_size=pagination.page_size)
        total_users = user_repo.get_total_count()
        total_pages = (total_users + pagination.page_size - 1) // pagination.page_size

        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "message": "Users fetched successfully",
                "data": [
                    {
                        "id": user.id,
                        "first_name": user.first_name,
                        "last_name": user.last_name,
                        "email": user.email,
                        "phone_number": user.phone_number,
                        "profile_photo": (
                            base64.b64encode(user.profile_photo).decode("utf-8")
                            if user.profile_photo
                            else None
                        ),
                    }
                    for user in users
                ],
                "total_pages": total_pages,
                "total_count": total_users,
            },
        )
    except Exception as e:
        logger.exception("Failed to fetch users")
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "message": "An error occurred while fetching users",
                "error": str(e),
            },
        )


@router.put("/{user_id}")
def update(user_id: int, user_data: User, db: Session = Depends(get_connection)):
    """
    Update an existing user in the database.

    Args:
        user_id (int): The ID of the user to update.
        user_data (User): The new data for the user.
        db (Session): Database session dependency.

    Returns:
        JSONResponse: A response object indicating the outcome of the update operation.
    """
    try:
        logger.info(f"Updating user with ID {user_id}")
        user_repo = UserRepository(db)
        updated_user = user_repo.update(user_id, user_data.model_dump())

        if not updated_user:
            logger.error(f"User with ID {user_id} not found")
            return JSONResponse(
                status_code=status.HTTP_404_NOT_FOUND,
                content={"message": "User not found"},
            )

        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "message": "User updated successfully",
                "data": user_data.model_dump(),
            },
        )
    except Exception as e:
        logger.exception(f"Failed to update user with ID {user_id}")
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "message": "An error occurred while updating the user",
                "error": str(e),
            },
        )


@router.delete("/{user_id}")
def delete(user_id: int, db: Session = Depends(get_connection)):
    """
    Delete a user by their ID from the database.

    Args:
        user_id (int): The ID of the user to delete.
        db (Session): Database session dependency.

    Returns:
        JSONResponse: A response object indicating the outcome of the deletion operation.
    """
    try:
        logger.info(f"Attempting to delete user with ID {user_id}")
        user_repo = UserRepository(db)
        user_repo.delete(user_id)

        return JSONResponse(
            status_code=status.HTTP_204_NO_CONTENT,
            content={"message": "User deleted successfully"},
        )
    except Exception as e:
        logger.exception(f"Failed to delete user with ID {user_id}")
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "message": "An error occurred while deleting the user",
                "error": str(e),
            },
        )
