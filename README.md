# README.md

## Introduction

This library simplifies the setup of Telethon clients for Telegram bots by handling configuration loading and client creation in a centralized way. It aims to streamline the process of creating Telegram bots, allowing developers to focus on bot logic rather than boilerplate code.

## Installation
```bash
pip install telethon-client-wrapper
```
## Configuration

Create a `config.json` file with the following fields:

```json
{
  "device_model": "YourDeviceModel",
  "system_version": "YourSystemVersion",
  "app_version": "YourAppVersion",
  "lang_code": "en",
  "system_lang_code": "en-US",
  "api_id": "YOUR_API_ID",
  "api_hash": "YOUR_API_HASH"
}
```

## Usage

Import and use the `create_client` function:

```python
from telethon_client_wrapper import create_client

client = create_client('config.json', 'my_session')

```

## Contribution Guidelines

Contributions are welcome

## Support

For support or inquiries, please contact [@Rerowros](https://t.me/Rerowros) or open an issue on GitHub.

## Roadmap

- [ ] Enhance error handling and logging.

## Links

- [Telethon Documentation](https://docs.telethon.dev/)
