# Instagram Follow/Unfollow Checker

This Python script analyzes your Instagram data to determine which users you follow but don't follow back, and vice versa.

## Description

The script reads your Instagram JSON data files (`followers.json` and `following.json`) to identify:
- Users who follow you but you don't follow back
- Users you follow but don't follow you back

## Prerequisites

- Python 3.x
- Instagram data files (`followers.json` and `following.json`) from your Instagram data export

## Installation

1. Ensure you have Python 3.x installed on your system.
2. Place the `insta_follow_unfollow.py` script in the same directory as your Instagram data files.

## Usage

1. Export your Instagram data from [Instagram's Data Download](https://accountscenter.instagram.com/info_and_permissions/).
2. Extract the downloaded ZIP file to get `followers.json` and `following.json`.
3. Place these files in the same directory as the script.
4. Run the script using Python:

   ```bash
   python insta_follow_unfollow.py
   ```

## Output

The script will display:
- Total number of followers
- Total number of people you are following
- A list of users who follow you but you don't follow back (with Instagram URLs)
- A list of users you follow but don't follow you back (with Instagram URLs)

## Files

- `insta_follow_unfollow.py`: Main script to analyze Instagram follow data
- `followers.json`: Instagram data file containing your followers list (from your data export)
- `following.json`: Instagram data file containing your following list (from your data export)

## Note

This script is designed to work with Instagram's JSON data exports. It expects the files to be in the correct format as provided by Instagram's data download feature.
