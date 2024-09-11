import time
import requests

def check_response_time(url):
    try:
        start_time = time.time()
        response = requests.get(url)
        end_time = time.time()

        response_time = end_time - start_time
        print(f"Response Time: {response_time:.4f} seconds | Status Code: {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    target_url = 'http://localhost:5000/'

    while True:
        check_response_time(target_url)
        time.sleep(1)
