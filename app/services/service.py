from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from config import (
    DELEGATED_ACCOUNT,
    SERVICE_ACCOUNT_KEY_FILE,
    SCOPES
)


class Service:
    """Service builder"""

    def __init__(self, service_name, version, discovery_url=None):
        self.service_name = service_name
        self.version = version
        self.discovery_url = discovery_url

        self.root_delegated_user = DELEGATED_ACCOUNT
        self.current_delegated_user = DELEGATED_ACCOUNT

        self.credentials = Credentials.from_service_account_file(
            SERVICE_ACCOUNT_KEY_FILE,
            scopes=SCOPES,
            subject=DELEGATED_ACCOUNT
        )

        self.service = self.build(self.service_name, self.version)

    def build(self, service, version):
        """build the service from name, version and credentials"""
        return build(
            service,
            version,
            credentials=self.credentials,
            cache_discovery=False,
            discoveryServiceUrl=self.discovery_url
        )
