import logging

from app.services.service import Service


class LumappsService(Service):
    """Lumapps Service"""

    def __init__(self):
        discovery_url = ('https://lumsites.appspot.com/'
                         '_ah/api/discovery/v1/apis/lumsites/v1/rest')
        Service.__init__(self, 'lumsites', 'v1', discovery_url)

    def get_user(self, user_email):
        try:
            user = self.service.user().get(
                email=user_email
            ).execute()
            return user
        except Exception as e:
            logging.error(f'Error getting user {user_email}: {str(e)}')

    def save_user(self, body):
        try:
            user = self.service.user().save(
                body
            ).execute()
            return user
        except Exception as e:
            logging.error(f'Error saving user: {str(e)}')

    def list_users(self, maxResults=500):
        try:
            users = []
            cursor = None

            while True:
                res = self.service.user().list(
                    maxResults,
                    cursor
                ).execute()

                items = res.get('items', [])
                cursor = res.get('cursor', None)

                for user in items:
                    users.append(user)

                if not res.get('more', False):
                    break
            return users
        except Exception as e:
            logging.error(f'Error listing users: {str(e)}')

    def get_user_directory(self, user_email, content_id):
        try:
            user = self.service.user().directory().get(
                email=user_email,
                contentId=content_id
            ).execute()
            return user
        except Exception as e:
            logging.error(f'Error getting user {user_email} directory: {str(e)}')

    def save_user_directory(self, body):
        try:
            self.service.user().directory().save(
                body
            ).execute()
            return 200
        except Exception as e:
            logging.error(f'Error saving user directory: {str(e)}')

    def delete_multi_users(self, uids):
        try:
            self.service.user().deleteMulti(
                uid=uids
            ).execute()
            return 200
        except Exception as e:
            logging.error(f'Error deleteMulti users: {str(e)}')

    def get_metadata(self, metadata_uid):
        try:
            metadata = self.service.metadata().get(
                uid=metadata_uid
            ).execute()
            return metadata
        except Exception as e:
            logging.error(f'Error get metadata {metadata_uid}: {str(e)}')

    def save_metadata(self, body):
        try:
            self.service.metadata().save(
                body
            ).execute()
            return 200
        except Exception as e:
            logging.error(f'Error saving metadata: {str(e)}')

    def list_metadata(self, maxResults=500):
        try:
            metadatas = []
            cursor = None

            while True:
                res = self.service.metadata().list(
                    maxResults,
                    cursor
                ).execute()

                mds = res.get('items', [])
                cursor = res.get('cursor', None)

                for md in mds:
                    metadatas.append(md)

                if not res.get('more', False):
                    break
            return metadatas
        except Exception as e:
            logging.error(f'Error listing metadatas: {str(e)}')
