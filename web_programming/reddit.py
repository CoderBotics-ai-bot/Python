from __future__ import annotations

import requests
from typing import List
from requests import exceptions

valid_terms = set(
    """approved_at_utc approved_by author_flair_background_color
author_flair_css_class author_flair_richtext author_flair_template_id author_fullname
author_premium can_mod_post category clicked content_categories created_utc downs
edited gilded gildings hidden hide_score is_created_from_ads_ui is_meta
is_original_content is_reddit_media_domain is_video link_flair_css_class
link_flair_richtext link_flair_text link_flair_text_color media_embed mod_reason_title
name permalink pwls quarantine saved score secure_media secure_media_embed selftext
subreddit subreddit_name_prefixed subreddit_type thumbnail title top_awarded_type
total_awards_received ups upvote_ratio url user_reports""".split()
)

def get_subreddit_data(
    subreddit: str, limit: int = 1, age: str = "new", wanted_data: list | None = None
) -> dict:
    """
    Fetch data from a specified subreddit.

    Parameters
    ----------
    subreddit : str
        Name of the subreddit to gather data from.
    limit : int, optional (default=1)
        The number of posts to fetch from the subreddit.
    age : str, optional (default="new")
       The posts to fetch based on their age. Can be either "new", "top", or "hot".
    wanted_data : list, optional
        List of fields of the data to fetch from each posts. If None, all fields will be fetched.

    Returns
    -------
    data_dict : dict
        Dictionary containing the data fetched from each posts.

    Raises
    ------
    ValueError
        If one or more of the fields provided in wanted_data list are not valid.
    requests.exceptions.HTTPError
        If the status of the response from the API is 429, meaning API rate limit has been exhausted.
    """
    # Ensure wanted_data is a list
    wanted_data = wanted_data or []

    # Validate search terms
    invalid_search_terms = ", ".join(sorted(set(wanted_data) - valid_terms))
    if invalid_search_terms:
        raise ValueError(f"Invalid search terms: {invalid_search_terms}")

    # Perform API request
    response = requests.get(
        f"https://reddit.com/r/{subreddit}/{age}.json?limit={limit}",
        headers={"User-agent": "Some random string"},
    )
    if response.status_code == 429:
        raise requests.exceptions.HTTPError("API rate limit has been exhausted")

    # Parse response data
    data = response.json()["data"]["children"]

    # Extract requested data
    data_dict = {}
    for i, child in enumerate(data):
        if not wanted_data:  # If no specific data requested, return full data
            data_dict[i] = child
        else:
            data_dict[i] = {item: child["data"][item] for item in wanted_data}
    return data_dict


if __name__ == "__main__":
    # If you get Error 429, that means you are rate limited.Try after some time
    print(get_subreddit_data("learnpython", wanted_data=["title", "url", "selftext"]))
