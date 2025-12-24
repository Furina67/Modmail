# Discord ModMail Bot

A scalable ModMail system for Discord servers built using private threads.

This bot enables users to contact staff via direct messages while keeping conversations organized, private, and easy to manage for moderators.


## Features

- DM-based ModMail system using private threads  
- Staff-only **Claim** and **Close** buttons  
- Claim protection (only the claimer can reply or close)  
- Two-way message and attachment forwarding  
- Ticket logging to a dedicated channel  
- Persistent storage using JSON  
- Designed for clean scalability and maintenance  


## Setup

### Install dependencies
```bash
pip install -r requirements.txt

Update the .env file:

```BOT_TOKEN=your_bot_token_here
SERVER_ID=your_server_id
TICKET_CHANNEL_ID=your_ticket_channel_id
LOG_CHANNEL_ID=your_log_channel_id
STAFF_ROLE_ID=your_staff_role_id
PREFIX=$```

Run the bot:
```python bot.py```