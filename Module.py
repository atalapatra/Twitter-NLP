
import pandas as pd
import re

## Functions

def tweepyToDataframe (api_data):
    json_data = [i._json for i in api_data]
    df = pd.io.json.json_normalize(json_data)
    return df

def remove_url(txt): # From: https://www.earthdatascience.org/courses/use-data-open-source-python/intro-to-apis/analyze-tweet-sentiment-in-python/
    """Replace URLs found in a text string with nothing 
    (i.e. it will remove the URL from the string).

    Parameters
    ----------
    txt : string
        A text string that you want to parse and remove urls.

    Returns
    -------
    The same txt string with url's removed.
    """
    return " ".join(re.sub("([^0-9A-Za-z \t])|(\w+:\/\/\S+)", "", txt).split())

