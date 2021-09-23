from config import DELEGATED_ACCOUNT
from app.services.lumapps import LumappsService


def main():
    lumapps_service = LumappsService()

    # Examples
    # Get a user
    user = lumapps_service.get_user(DELEGATED_ACCOUNT)
    print(user)

    # List users
    users = lumapps_service.list_users(maxResults=2)
    print(users)


if __name__ == '__main__':
    main()
