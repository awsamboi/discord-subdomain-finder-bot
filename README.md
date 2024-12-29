# Discord Subdomain Finder Bot

A Discord bot that fetches all subdomains for a given domain using the SecurityTrails API and resolves their IP addresses. The results are displayed in clean, paginated Discord embeds.

## Features

- Fetch subdomains for any domain using the SecurityTrails API.
- Resolve and display the IP address for each subdomain.
- Display results in paginated Discord embeds for better readability.
- Handles large subdomain lists by batching results into groups of 25.

## Prerequisites

Before running the bot, ensure you have the following:

1. **Python 3.8+** installed.
2. A **Discord Bot Token**. You can create one from the [Discord Developer Portal](https://discord.com/developers/applications).
3. A **SecurityTrails API Key**. Sign up and get your API key from the [SecurityTrails website](https://securitytrails.com/).

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/awsamboi/discord-subdomain-finder-bot.git
   cd discord-subdomain-finder-bot
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Replace and add your API keys:

   ```
   DISCORD_BOT_TOKEN=i_think_it_is_google_api_token_but_not_sure
   SECURITYTRAILS_API_KEY=your_securitytrails_api_key
   ```

## Usage

1. Run the bot:

   ```bash
   python main.py
   ```

2. Invite the bot to your Discord server using the OAuth2 URL from the Discord Developer Portal.

3. Use the command `!subdomains <domain>` in a Discord channel to fetch subdomains for the given domain.

   Example:

   ```
   !subdomains example.com
   ```

4. The bot will reply with embeds showing subdomains and their IP addresses.

## Example Output

**Command:**

```
!subdomains example.com
```

**Bot Response:**

- **Embed 1:**
  - `api.example.com` | IP: `192.168.1.1`
  - `blog.example.com` | IP: `192.168.1.2`

- **Embed 2:** (if more than 25 subdomains exist)

## Code Structure

- **`main.py`**: Main script for the Discord bot.
- **`requirements.txt`**: List of dependencies.

## Dependencies

- `discord.py` for interacting with the Discord API.
- `requests` for making API calls to SecurityTrails.
- `socket` for DNS resolution.
