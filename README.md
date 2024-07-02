# College Searching Tool

## Overview
The **College Searching Tool** is a Python-based tool designed to help students and parents find colleges in a specific city offering courses like BCA or BTech. The application scrapes data from **Collegedunia** and displays the college names along with their respective fees.

## Features
- **Scrape Data**: Fetches college information from Collegedunia based on the specified city and course.
- **Display Results**: Outputs a formatted list of colleges along with their fees.
- **Save Links**: Optionally saves the list of college links to a file for later reference.
- **Colored Output**: Enhances the terminal output with colorful separators for better readability.

## Prerequisites
- Python 3.x
- Required Python packages:
  - `requests`
  - `beautifulsoup4`
  - `colorama`

You can install the necessary packages using pip:
```sh
pip install requests beautifulsoup4 colorama
```

## Usage

  - Run the script:

    ```sh
    python3 college_search.py
    ```

  - Input Details:
        City: Enter the city where you want to search for colleges.
        Course: Enter the course name (BCA or BTech).

  - View Results:
        The script will display the list of colleges and their fees in a formatted manner with colorful separators.

  - Save Links (Optional):
        After displaying the results, you will be prompted to save the links to a file. Enter 'y' to save the links or 'N' to skip.

## Project Structure

  `college_search.py` : The main script containing the CollegeSearch class and logic for fetching, parsing, and displaying college information.

## Code Walkthrough

   - Initialization:
        The `CollegeSearch` class initializes with empty lists to store URLs, positions, college names, and fees.

   - Search:
        The `search` method constructs the URL based on user input and fetches the HTML content from Collegedunia.

   - Parser:
        The `parser` method uses BeautifulSoup to parse the fetched HTML content.

   - Extract Links:
        The `clglinks` method extracts college URLs and positions from the parsed data.

   - Extract Names:
        The `clgname` method extracts and cleans college names from the URLs.

   - Extract Fees:
        The `clgfees` method fetches college fees from the parsed HTML content.

   - Save Links:
        The `savelinks` method prompts the user to save the fetched college URLs to a file.

   - Colored Output:
        The `colourline` method generates a colorful line separator for the terminal output.

   - Run Application:
        The `run` method handles user inputs and coordinates the execution of all other methods to display the results.

## Conclusion

The **College Searching Tool** provides a simple yet effective way to search for colleges based on city and course. The colorful output and optional link-saving feature enhance user experience, making it a handy tool for prospective students.

Feel free to contribute or suggest improvements by opening an issue or submitting a pull request. Enjoy exploring colleges with this tool!

