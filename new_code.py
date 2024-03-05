def test_data_value():
    import requests
    import json

    url = "https://gmail.googleapis.com/gmail/v1/users/me/messages/send"

    payload = json.dumps({
        "raw": "RnJvbTogc2h1YmhhbXZpamF5dmFyZ2l5YTVAZ21haWwuY29tClRvOiBzaHViaGFtdmlqYXl2YXJnaXlhNTlAZ21haWwuY29tClN1YmplY3Q6IFNheWluZyBIZWxsbwoKVGhpcyBpcyBhIG1lc3NhZ2UganVzdCB0byBzYXkgaGVsbG8uClNvLCAiSGVsbG8iLg=="
    })

    json_in = open("token.json", "rb")
    example_dict = json.load(json_in)
    access_token = example_dict['access_token']

    headers = {
        'Authorization': f'Bearer {access_token}',
        'Cache-Control': 'no-cache',
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
