import pickle

example_dict = {
    "client_id" :"143443373358-kok70q3su8jc4qo8uhrr4d6dhdp6gaqp.apps.googleusercontent.com",
    "client_secret" : "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",
    "refresh_token" : "1//0gjKKAQijzHNPCgYIARAAGBASNwF-L9IrQmoyLNxwURme1-_d739S_o67owFxg2yeLwo9zpd8_n09ATe-CQF-wVyH77QSAS4vxKA",
}

pickle_out = open('token.pickle',"wb")
pickle.dump(example_dict, pickle_out)
pickle_out.close()
