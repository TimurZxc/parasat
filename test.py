import re

# URL from which we want to extract the video ID
url = "https://www.youtube.com/watch?v=sKPyT2xQuh0&ab_channel=%D0%9A%D0%B0%D0%B7%D1%85%D0%B8%D0%BC%D0%BF%D1%80%D0%BE%D0%BC%D0%9E%D0%AE%D0%9B"

# Define the regex pattern to find the video ID
# We look for '?v=' followed by a series of non-'&' characters
pattern = r'\?v=([^&]+)'

# Search for the pattern in the URL
match = re.search(pattern, url)
if match:
    video_id = match.group(1)  # Extract the video ID
    print("Extracted video ID:", video_id)
else:
    print("No video ID found.")
