from __future__ import print_function
import time
import tbaapiv3client
from tbaapiv3client.rest import ApiException
from pprint import pprint
import os
from dotenv import load_dotenv

load_dotenv()

configuration = tbaapiv3client.Configuration(
    api_key = {
        'X-TBA-Auth-Key': os.environ.get('TBA_API_KEY')
    }
)

with tbaapiv3client.ApiClient(configuration) as api_client:
    api_instance = tbaapiv3client.TeamApi(api_client)
    if_modified_since = 'if_modified_since_example'

    try:
        # In groups of 500, so 500 * 25 teams = 12,500, which is fine for now because teams only go to 10714
        pages = 25

        for page in range(pages):
            team_page = api_instance.get_teams(page_num=page, if_modified_since=if_modified_since)

            for team in team_page:
                try:
                    api_response = api_instance.get_team_social_media(team_key=team.key, if_modified_since=if_modified_since)
                except ValueError:
                    continue
        
                for item in api_response:
                    if item.type == "github-profile":
                        with open("github_profiles.txt", "a") as file:
                            file.write(f"https://github.com/{item.foreign_key}\n")

    except ApiException as e:
        print(f"Exception when calling API: {e}")
