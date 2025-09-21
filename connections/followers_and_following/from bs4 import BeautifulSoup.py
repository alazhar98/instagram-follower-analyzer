from bs4 import BeautifulSoup

# Load followers.html
with open("followers.html", "r", encoding="utf-8") as f:
    followers_html = f.read()

# Load following.html
with open("following.html", "r", encoding="utf-8") as f:
    following_html = f.read()

# Parse with BeautifulSoup
followers_soup = BeautifulSoup(followers_html, "html.parser")
following_soup = BeautifulSoup(following_html, "html.parser")

# Extract usernames (Instagram usually puts them inside <a> tags)
followers = {a.get_text() for a in followers_soup.find_all("a")}
following = {a.get_text() for a in following_soup.find_all("a")}

# Clean up (remove empty strings)
followers = {f.strip() for f in followers if f.strip()}
following = {f.strip() for f in following if f.strip()}

# Accounts you follow but don’t follow you back
not_following_back = following - followers

print("People you follow but don’t follow you back:")
for user in sorted(not_following_back):
    print(user)

# Save to file
with open("not_following_back.txt", "w", encoding="utf-8") as f:
    for user in sorted(not_following_back):
        f.write(user + "\n")
