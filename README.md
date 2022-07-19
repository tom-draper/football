# Premier-League-Table

A python script that fetches and displays real time Premier League table on the command line.
The football data is retrieved from the football data API football-data.org (https://www.football-data.org/).

## Getting Started

### 1. Create a free football-data.org account

For real time data, this app requires your X-Auth token from your football-data.org account (completely free). Your API key will allow up to 50 calls per minute.

### 2. Copy your X-Auth token into the <code>.env</code> file

Paste your X-Auth token into the <code>.env</code>, after <code>X_AUTH_TOKEN=</code>

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

##### Flags

- <code>compact</code> or <code>c</code> - displays the compact version of the standings table 

#### Match Results

```bash
py football.py results
```
