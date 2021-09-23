## Quickstart Lumapps API

This quickstart can be used as template. It has a few Lumapps API calls as examples

## Requirements

- Have a service account key (name it `key.json` and add it to config/credentials/)

- Activate Google Workspace domain-wide delegation on the service account

- Authorize the following scope on your Workspace platform, with the service account client ID: 
`https://www.googleapis.com/auth/userinfo.email`

- Python3 (https://www.python.org/downloads/windows/)

- Python virtualenv and pip installed

- Update DELEGATED_ACCOUNT in config file. The email must be a Google Workspace admin.

## Setup

```bash
# Create virtualenv
python3 -m venv venv

# Activate venv
source venv/bin/activate

# Install requirements
pip install google-api-python-client
```

## Main

```bash
# Execute examples in main
python main.py
```

## Documentation

Link to the official Lumapps API documentation: https://apiv1.lumapps.com/