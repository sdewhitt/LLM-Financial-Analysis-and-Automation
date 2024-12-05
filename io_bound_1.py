import time
import requests
from concurrent.futures import ThreadPoolExecutor
from typing import List, Tuple

def fetch_slow_api() -> Tuple[int, str]:
    """
    Make a request to the slow API and return status code
    """

    try:
        print('Starting Request...')
        response = requests.get('http://localhost:5001/')
        response.raise_for_status()
        try:
            result = response.json()
            print(f'Request completed: {result}')
            return response.status_code, result['message']
        except ValueError as e:
            print(f'JSON decode error. Response: {response.text}')
            return -1, f'Invalid JSON response: {str(e)}'
    except requests.RequestException as e:
        print(f'Request Error: {str(e)}')
        return -1, str(e)
    except Exception as e:
        print(f'Unexpected Error: {str(e)}')
        return -1, str(e)
    

if __name__ == '__main__':
    num_requests = 5

    # Single threaded execution
    print(f'\nMaking {num_requests} sequential requests to slow API...')
    start = time.time()
    single_results = fetch_slow_api()
    end = time.time() - start
    print(f'Single threaded execution time: {end:.2f} seconds')