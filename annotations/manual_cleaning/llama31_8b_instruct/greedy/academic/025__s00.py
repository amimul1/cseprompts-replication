# ================= CSEPrompts manual cleaning =================
# task: academic/025 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   It turns out that (most) YouTube videos can be embedded in other websites, just like the above.
#   For instance, if you visit https://youtu.be/xvFZjo5PgG0 on a laptop or desktop, click Share, and
#   then click Embed, you’ll see HTML (the language in which web pages are written) like the below,
#   which you could then copy into your own website’s source code, wherein iframe is an HTML
#   “element,” and src is one of several HTML “attributes” therein, the value of which, between
#   quotes, is https://www.youtube.com/embed/xvFZjo5PgG0.
#   
#   <iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube
#   video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media;
#   gyroscope; picture-in-picture" allowfullscreen></iframe>
#   Because some HTML attributes are optional, you could instead minimally embed just the below.
#   
#   <iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>
#   Suppose that you’d like to extract the URLs of YouTube videos that are embedded in pages (e.g.,
#   https://www.youtube.com/embed/xvFZjo5PgG0), converting them back to shorter, shareable youtu.be
#   URLs (e.g., https://youtu.be/xvFZjo5PgG0) where they can be watched on YouTube itself.
# ---- model response below: edit from here ----
import requests
from bs4 import BeautifulSoup
import re

def extract_youtube_urls(html):
    """
    Extracts YouTube video URLs from the given HTML.

    Args:
        html (str): The HTML string to parse.

    Returns:
        list: A list of extracted YouTube video URLs.
    """
    soup = BeautifulSoup(html, 'html.parser')
    iframe_tags = soup.find_all('iframe')
    youtube_urls = []

    for tag in iframe_tags:
        src = tag.get('src')
        if src and 'youtube.com/embed/' in src:
            youtube_urls.append(src)

    return youtube_urls

def convert_to_short_url(url):
    """
    Converts a YouTube video URL to a shorter, shareable youtu.be URL.

    Args:
        url (str): The YouTube video URL to convert.

    Returns:
        str: The shorter, shareable youtu.be URL.
    """
    match = re.search(r'/embed/([^/]+)$', url)
    if match:
        video_id = match.group(1)
        return f'https://youtu.be/{video_id}'
    return None

def main():
    url = 'https://www.example.com'  # Replace with the URL of the webpage containing the YouTube video
    response = requests.get(url)
    html = response.text
    youtube_urls = extract_youtube_urls(html)

    for url in youtube_urls:
        short_url = convert_to_short_url(url)
        if short_url:
            print(f'Original URL: {url}')
            print(f'Short URL: {short_url}')
            print('---')

if __name__ == '__main__':
    main()