# Football CLI

A Python script that fetches and displays real time football standings on the command line.
The football data is retrieved from the FREE football data API [football-data.org](https://www.football-data.org/).

## Installation

### 1. Create a free football data API account

This script uses [football-data.org](https://www.football-data.org/) to fetch up-to-date football data. When running the script, the X-Auth token from your football-data.org account is required. On the free tier, your API key will allow up to 50 API calls per minute.

### 2. Copy your X-Auth token into the <code>.env</code> file

Paste your X-Auth token into the <code>.env</code> file after <code>X_AUTH_TOKEN=</code>

### 3. Install pip dependencies

The requests, json and datetime packages are required, to install these run:

```bash
pip install -r requirements.txt
```

## Usage

#### Standings

```bash
python3 football.py standings
```

**Flags**

- <code>compact</code> or <code>c</code> - displays the compact version of the standings table.
