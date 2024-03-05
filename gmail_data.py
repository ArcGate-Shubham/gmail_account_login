def test_data():
    import requests
    import json
    import pickle

    pickle_in = open("token.pickle", "rb")
    example_dict = pickle.load(pickle_in)

    client_id = example_dict["client_id"]
    client_secret = example_dict["client_secret"]
    refresh_token = example_dict["refresh_token"]
    
    url = f"https://oauth2.googleapis.com/token?client_id={client_id}&client_secret={client_secret}&grant_type=refresh_token&refresh_token={refresh_token}"
    payload = {}
    headers = {}
    response = requests.request("POST", url, headers=headers, data=payload)
    response_json = response.json()
    print(json.dumps(response_json, indent=2))
    with open("token.json", "w") as file:
        json.dump(response_json, file)
    print("Token data has been saved to token.json.")
