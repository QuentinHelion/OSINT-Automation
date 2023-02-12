import requests

def GoogleDorks():    
    api_key = "AIzaSyBHgyOZIi3QMgWb90G-awiWPg_NrBFT_Z4"
    cse_id = "f7d833c394e914ee6"
    query = "inurl:example.com"
    
    max_results_per_page = 10
    
    start = 1
    total_results = 0
    
    while True:
        #API request
        response = requests.get(
            "https://www.googleapis.com/customsearch/v1",
            params={
                "key": api_key,
                "cx": cse_id,
                "q": query,
                "start": start,
                "num": max_results_per_page,
            },
        )
    
        # Check if the request was successful
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as error:
            print("All searches")
            break
        else:
            search_results = response.json()["items"]
    
            total_results += len(search_results)
    
            # Print the search results
            for result in search_results:
                print(result["link"])
    
            # Check if all results have been retrieved
            if len(search_results) < max_results_per_page:
                break
    
            # Update the starting result number for the next API request
            start += max_results_per_page