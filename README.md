# Football CLI

A Python script that fetches and displays real time football standings on the command line.
The football data is retrieved from the FREE football data API [football-data.org](https://www.football-data.org/).

## Getting Started

### 1. Create a free API account

To run the script, the X-Auth token from your [football-data.org](https://www.football-data.org/) account is required. Your free-tier API key will allow up to 50 API calls per minute.

### 2. Copy your X-Auth token into the <code>.env</code> file

Paste your X-Auth token into the <code>.env</code> file after <code>X_AUTH_TOKEN=</code>

### 3. Install pip dependencies

The requests, json and datetime packages are required, to install these run:

```bash
pip install -r requirements.txt
```

### 4. Run <code>football.py</code>

#### Standings

```bash
py football.py standings
```

**Flags**

- <code>compact</code> or <code>c</code> - displays the compact version of the standings table.
