#Import the requests library to handle HTTP requests
import requests
import json

#Define a function that take a string input
def sentiment_analyzer(text_to_analyse):
    if text_to_analyse == "":
        return {'label':'empty', 'score':'empty'}
        
    # URL of the sentiment analysis servide
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'

    #Constructing the request payload in the expected format
    myobj = {"raw_document": {"text":text_to_analyse}}

    #Custom header specifying the model ID for the sentiment analysis service
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}

    #Sending a POST request to the sentiment analysis API
    response = requests.post(url, json=myobj, headers=header)

    #Parsing the JSON response from the API
    formatted_response = json.loads(response.text)

    #Extracting sentiment label and score from the response
    if response.status_code == 200:
        label = formatted_response['documentSentiment']['label']
        score = formatted_response['documentSentiment']['score']
    else:
        label = None
        score = None

    #returning a dictionary containing sentiment analysis results
    return {'label':label, 'score':score}    