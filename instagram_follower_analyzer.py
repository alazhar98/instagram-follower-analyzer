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
from typing import Set, Optional
import json
import urllib.request
import urllib.parse

try:
    # Local license configuration with placeholder keys
    from license_config import is_license_valid
except Exception:
    # Fallback if file missing; treat as invalid until provided
    def is_license_valid(key: str) -> bool:  # type: ignore
        return False

def extract_usernames_from_html(file_path: str) -> Set[str]:
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
    # License check with optional Gumroad verification
    license_key = os.getenv("LICENSE_KEY", "").strip()
    if not license_key:
        # Optional fallback to file-based key for convenience
        key_file_path = "LICENSE_KEY.txt"
        if os.path.exists(key_file_path):
            try:
                with open(key_file_path, "r", encoding="utf-8") as key_file:
                    license_key = key_file.read().strip()
            except Exception:
                license_key = ""

    def verify_with_gumroad(product_id: Optional[str], key: str) -> bool:
        if not product_id:
            return False
        try:
            verify_url = os.getenv(
                "GUMROAD_VERIFY_URL",
                "https://api.gumroad.com/v2/licenses/verify",
            )
            payload = {
                "product_id": product_id,
                "license_key": key,
                # Optional: increment uses count
                "increment_uses_count": True,
            }
            data = urllib.parse.urlencode(payload).encode("utf-8")
            req = urllib.request.Request(verify_url, data=data, method="POST")
            with urllib.request.urlopen(req, timeout=10) as resp:
                body = resp.read().decode("utf-8", errors="ignore")
                parsed = json.loads(body)
                return bool(parsed.get("success"))
        except Exception:
            return False

    product_id = os.getenv("GUMROAD_PRODUCT_ID", "").strip()
    gumroad_ok = False
    if license_key and product_id:
        gumroad_ok = verify_with_gumroad(product_id, license_key)

    local_ok = is_license_valid(license_key) if license_key else False

    if not license_key or not (gumroad_ok or local_ok):
        print("License error: A valid license key is required to run Instagram Follower Analyzer Pro.")
        print("- Set environment variable LICENSE_KEY or create a LICENSE_KEY.txt file with your key.")
        print("- For Gumroad, also set GUMROAD_PRODUCT_ID to enable online verification.")
        print("- If you purchased a license and still see this message, contact support.")
        sys.exit(1)
    
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
