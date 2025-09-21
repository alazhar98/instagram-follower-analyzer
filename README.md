# Instagram Follower Analyzer

A Python script that analyzes your Instagram followers and following data to find accounts that you follow but who don't follow you back. Perfect for cleaning up your following list and identifying one-sided relationships.

## 🚀 Quick Start

1. Export your Instagram data from Settings > Privacy and Security > Download Your Information
2. Clone this repository
3. Place your `followers_1.html` and `following.html` files in the `connections/followers_and_following/` directory
4. Run the script: `python3 instagram_follower_analyzer.py`

## ✨ Features

- 🔍 **Smart Analysis**: Parses Instagram HTML export files using BeautifulSoup
- 📊 **Detailed Reports**: Extracts usernames from both followers and following lists
- 🎯 **One-sided Detection**: Finds accounts that don't follow you back
- 💻 **Console Output**: Displays results with formatted statistics
- 📄 **File Export**: Saves results to `not_following_back.txt` for easy reference
- 🚀 **Easy Setup**: Simple installation and usage

## 📈 What You'll Get

- Total number of followers
- Total number of accounts you follow
- Complete list of accounts that don't follow you back
- Sorted, numbered list for easy review
- Exportable results file

## Requirements

- Python 3.6 or higher
- BeautifulSoup4 library

## Installation

1. Install the required dependency:
   ```bash
   pip install beautifulsoup4
   ```
   
   Or install from requirements.txt:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Make sure you have the following files in the same directory as the script:
   - `connections/followers_and_following/followers_1.html`
   - `connections/followers_and_following/following.html`

2. Run the script:
   ```bash
   python3 instagram_follower_analyzer.py
   ```

## Output

The script will:
- Display analysis results in the console
- Create a `not_following_back.txt` file with the complete list of accounts that don't follow you back

## Sample Output

```
Analyzing Instagram followers and following data...
==================================================
Reading connections/followers_and_following/followers_1.html...
Found 26 followers
Reading connections/followers_and_following/following.html...
Found 196 accounts you follow
==================================================
Analysis Results:
Total followers: 26
Total following: 196
Accounts you follow who don't follow you back: 180
==================================================
```

## 📁 Project Structure

```
instagram-follower-analyzer/
├── instagram_follower_analyzer.py    # Main script
├── requirements.txt                  # Python dependencies
├── README.md                        # This file
├── not_following_back.txt           # Generated results (after running)
└── connections/
    └── followers_and_following/
        ├── followers_1.html         # Your Instagram followers data
        └── following.html           # Your Instagram following data
```

## 🔧 Installation

### Option 1: Using pip
```bash
pip install beautifulsoup4
```

### Option 2: Using requirements.txt
```bash
pip install -r requirements.txt
```

## 🚀 Usage

1. **Export your Instagram data**:
   - Go to Instagram Settings > Privacy and Security > Download Your Information
   - Select "Followers and Following" data
   - Download and extract the ZIP file

2. **Set up the project**:
   ```bash
   git clone https://github.com/yourusername/instagram-follower-analyzer.git
   cd instagram-follower-analyzer
   ```

3. **Add your data**:
   - Place `followers_1.html` and `following.html` in `connections/followers_and_following/`

4. **Run the analysis**:
   ```bash
   python3 instagram_follower_analyzer.py
   ```

## 📊 Sample Output

```
Analyzing Instagram followers and following data...
==================================================
Reading connections/followers_and_following/followers_1.html...
Found 26 followers
Reading connections/followers_and_following/following.html...
Found 196 accounts you follow
==================================================
Analysis Results:
Total followers: 26
Total following: 196
Accounts you follow who don't follow you back: 180
==================================================
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## ⚠️ Important Notes

- The script uses relative paths, so make sure to run it from the main project directory
- The script handles Instagram's HTML structure and extracts usernames from anchor tags
- Results are sorted alphabetically for easy reading
- This tool is for personal use only - respect Instagram's Terms of Service

## 🔒 Privacy & Security

**IMPORTANT**: This repository contains sample data only. When using with your real Instagram data:

1. **Never commit personal data** - Your real Instagram HTML files contain private information
2. **Use .gitignore** - The repository is configured to ignore personal data files
3. **Keep results private** - The `not_following_back.txt` file contains personal follower information
4. **Respect privacy** - Don't share other people's usernames or follow data publicly

### How to Use with Your Real Data:
1. Replace the sample HTML files in `connections/followers_and_following/` with your real Instagram export
2. Run the script locally
3. Keep the results private - don't commit them to version control

