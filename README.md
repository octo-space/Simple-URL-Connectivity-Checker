# Simple URL Connectivity Checker

This Python script is a simple tool for checking the connectivity of a given URL.

## How it Works:

### 1. Importing `urllib.request`

The script starts by importing the `urllib.request` module. This module provides functionalities for opening and reading URLs, making it essential for checking website connectivity.

```python
import urllib.request as urlre
```

### 2. User Input

The script then prompts the user to enter a URL.

```python
url = input("Enter Url : ")
```

### 3. `urlCheck` Function

The core functionality is encapsulated within the `urlCheck` function. 

- **`try...except` Block:** The function uses a `try...except` block to handle potential errors that might occur when attempting to open the URL. 
    - **`urlre.urlopen(url)`:** Inside the `try` block, the `urlopen` function from the `urllib.request` module is used to open the provided URL. This function returns a response object if the URL is reachable.
    - **`res.getcode()`:** The response object contains various information about the request. The `getcode()` method retrieves the HTTP status code, indicating the server's response.
- **Error Handling:** The `except` block catches any exceptions raised during the `urlopen` process. This ensures the script doesn't crash if the URL is invalid or unreachable. 

```python
def urlCheck():
    try:
        res = urlre.urlopen(url)
        print(f'Status Code: {res.getcode()}')
    except Exception as e:
        print(f'Error occurred: {e}')
```

### 4. Execution

Finally, the `urlCheck` function is called, triggering the URL connectivity check.

```python
urlCheck()
```

## Usage:

1. Save the code as a Python file (e.g., `url_checker.py`).
2. Run the script from your terminal: `python url_checker.py`.
3. Enter the URL you want to check when prompted.
4. The script will display the HTTP status code or an error message if the URL is unreachable.

## Example:

```
Enter Url : https://www.google.com
Status Code: 200
```

This indicates that the Google website is reachable and the server responded successfully (status code 200).

