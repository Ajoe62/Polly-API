import requests

def register_user(base_url, username, password):
    """
    Register a new user with the Polly API.
    
    Args:
        base_url (str): The base URL of the API (e.g., 'http://localhost:8000')
        username (str): The desired username for registration
        password (str): The password for the new account
        
    Returns:
        dict: The user data on successful registration with 'id' and 'username'
        
    Raises:
        requests.exceptions.HTTPError: If the API returns an error (e.g., username already registered)
        requests.exceptions.RequestException: For network-related errors
    """
    # Construct the full URL for the registration endpoint
    url = f"{base_url}/register"
    
    # Prepare the request payload according to the API specification
    payload = {
        "username": username,
        "password": password
    }
    
    # Set headers for JSON content
    headers = {
        "Content-Type": "application/json"
    }
    
    # Send the POST request to the API
    response = requests.post(url, json=payload, headers=headers)
    
    # Raise an exception for HTTP errors (4xx and 5xx responses)
    response.raise_for_status()
    
    # Return the parsed JSON response
    return response.json()


def get_polls(base_url, skip=0, limit=10):
    """
    Fetch paginated poll data from the /polls endpoint.

    Args:
        base_url (str): The base URL of the API (e.g., 'http://localhost:8000')
        skip (int): Number of items to skip (pagination)
        limit (int): Maximum number of items to return (pagination)

    Returns:
        list: List of poll objects, each with keys:
            - id (int)
            - question (str)
            - created_at (str)
            - owner_id (int)
            - options (list of dicts with keys: id, text, poll_id)
    """
    url = f"{base_url}/polls"
    params = {"skip": skip, "limit": limit}
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()


# Example usage
if __name__ == "__main__":
    base_url = "http://localhost:8000"
    
    # Example: Register a new user
    try:
        new_user = register_user(base_url, "new_user", "secure_password")
        print(f"User registered successfully: {new_user}")
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 400:
            print("Error: Username already registered")
        else:
            print(f"HTTP Error: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Request Error: {e}")
    
    # Example: Get paginated polls
    try:
        polls = get_polls(base_url, skip=0, limit=10)
        print(f"Retrieved {len(polls)} polls")
        for poll in polls:
            print(f"Poll #{poll['id']}: {poll['question']} (Options: {len(poll['options'])})")
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching polls: {e}")
