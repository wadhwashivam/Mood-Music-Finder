# Mood Music Finder

## Overview

The Mood Music Finder is a Python script that allows users to find instrumental music on YouTube based on their mood preferences. Users can select a mood from a predefined list, and the script will perform a Google search to find a relevant instrumental music video on YouTube.

## How to Use

1. Run the script by executing the following command in your terminal or command prompt: python mood_music_finder.py

2. Enter the number corresponding to your desired mood from the provided list.

3. The script will perform a Google search and provide a link to a relevant instrumental music video on YouTube.

## Note

- **Search Speed:** This script currently uses the `googlesearch` library for search functionality, which may result in slower search speeds. This is due to the limitations of the library and the pause introduced after each search.

- **Result Limitation:** The script is designed to provide only one link at a time, limiting the number of results returned for simplicity.

## Improvement Suggestions

For improved search speed and more advanced features, consider using the YouTube Data API with the `google-api-python-client` library. This alternative approach allows for faster and more efficient searches, providing more control over the search results.

To set up the YouTube Data API, follow the instructions in the script comments or refer to the official API documentation.

## Author

[Shivam Wadhwa](http://wadhwashivam.github.io/Resume/)



