from database.dependency.repository import user_repository
from database.services.user_service import UserService

user_service = UserService(user_repository=user_repository)
