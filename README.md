# frc-github-url-scraper

A simple script that uses The Blue Alliance's API to find all of the teams' GitHub pages

## Installation
Clone this repository

```bash
https://github.com/FRC-Team3484/frc-github-url-scraper
```

Create a virtual enviroment and activate it using the command for your system (Linux is shown here)
```bash
python3 -m venv .venv
source ./.venv/bin/activate
```

Install the required packages
```bash
pip install -r requirements.txt
```

Run the script
```bash
python main.py
```

The URL's for teams' GitHub's will be placed into the `github_profiles.txt` file. The script takes some time to make it though every team on TBA.