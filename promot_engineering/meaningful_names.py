import requests

def fetchData(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error: {response.status_code}")
    except Exception as e:
        print(f"Failed to fetch data: {e}")
        return None

# Usage example
data = fetchData("https://api.example.com/data")









# import requests
#
# def fetchUserDataFromAPI(api_url):
#     """Fetch user-related data from a given API."""
#     try:
#         response = requests.get(api_url)
#         if response.status_code == 200:
#             return response.json()
#         else:
#             raise Exception(f"Failed to fetch user data: {response.status_code}")
#     except Exception as error:
#         print(f"Error fetching user data: {error}")
#         return None
#
# # Usage example
# user_data = fetchUserDataFromAPI("https://api.example.com/users")