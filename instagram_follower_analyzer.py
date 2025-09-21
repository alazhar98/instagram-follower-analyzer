#!/usr/bin/env python3
"""
Instagram Follower Analyzer

This script analyzes Instagram followers and following data to find accounts
that you follow but who don't follow you back.

Requirements:
- BeautifulSoup4 (pip install beautifulsoup4)
- followers.html and following.html files in the same directory as this script
"""

from bs4 import BeautifulSoup
import os
import sys

def extract_usernames_from_html(file_path):
    """
    Extract usernames from Instagram HTML file.
    
    Args:
        file_path (str): Path to the HTML file
        
    Returns:
        set: Set of usernames found in the file
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return set()
    except Exception as e:
        print(f"Error reading file '{file_path}': {e}")
        return set()
    
    soup = BeautifulSoup(content, 'html.parser')
    usernames = set()
    
    # Find all anchor tags with Instagram URLs
    links = soup.find_all('a', href=True)
    
    for link in links:
        href = link.get('href', '')
        if 'instagram.com/' in href:
            # Extract username from URL
            username = href.split('instagram.com/')[-1]
            # Remove any query parameters or fragments
            username = username.split('?')[0].split('#')[0]
            # Only add if it's not empty and doesn't contain special characters that aren't part of usernames
            if username and not username.startswith('http'):
                usernames.add(username)
    
    return usernames

def main():
    """Main function to analyze followers and following."""
    
    # Check if required files exist
    followers_file = 'connections/followers_and_following/followers_1.html'
    following_file = 'connections/followers_and_following/following.html'
    
    if not os.path.exists(followers_file):
        print(f"Error: {followers_file} not found in current directory.")
        print("Please make sure the file is in the same directory as this script.")
        sys.exit(1)
    
    if not os.path.exists(following_file):
        print(f"Error: {following_file} not found in current directory.")
        print("Please make sure the file is in the same directory as this script.")
        sys.exit(1)
    
    print("Analyzing Instagram followers and following data...")
    print("=" * 50)
    
    # Extract usernames from both files
    print(f"Reading {followers_file}...")
    followers = extract_usernames_from_html(followers_file)
    print(f"Found {len(followers)} followers")
    
    print(f"Reading {following_file}...")
    following = extract_usernames_from_html(following_file)
    print(f"Found {len(following)} accounts you follow")
    
    # Find accounts you follow who don't follow you back
    not_following_back = following - followers
    
    print("=" * 50)
    print(f"Analysis Results:")
    print(f"Total followers: {len(followers)}")
    print(f"Total following: {len(following)}")
    print(f"Accounts you follow who don't follow you back: {len(not_following_back)}")
    print("=" * 50)
    
    if not_following_back:
        print("\nAccounts that don't follow you back:")
        print("-" * 40)
        
        # Sort the list for better readability
        sorted_not_following = sorted(not_following_back)
        
        for i, username in enumerate(sorted_not_following, 1):
            print(f"{i:3d}. @{username}")
        
        # Save to file
        output_file = 'not_following_back.txt'
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write("Accounts that don't follow you back:\n")
                f.write("=" * 40 + "\n\n")
                for i, username in enumerate(sorted_not_following, 1):
                    f.write(f"{i:3d}. @{username}\n")
                f.write(f"\nTotal: {len(not_following_back)} accounts\n")
            
            print(f"\nResults saved to '{output_file}'")
        except Exception as e:
            print(f"Error saving to file: {e}")
    else:
        print("\nGreat! All accounts you follow also follow you back.")
        print("No accounts to save to file.")

if __name__ == "__main__":
    main()
