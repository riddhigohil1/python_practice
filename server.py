''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import Flask, render_template, request from the flask pramework package
# Import the sentiment_analyzer function from the package created
from flask import Flask, render_template,request
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

#Initiate the flask app
app = Flask('Sentiment Analyzer')

@app.route("/sentimentAnalyzer")
def sent_analyzer():
    ''' This code receives the text from the HTML interface and 
        runs sentiment analysis over it using sentiment_analysis()
        function. The output returned shows the label and its confidence 
        score for the provided text.
    '''

    #Retrieve the text from request arguments to analyze
    text_to_analyze = request.args.get('textToAnalyze')

    #Pass text ro function and store response
    response = sentiment_analyzer(text_to_analyze)

    #Extract label and score from the response
    label = response['label']
    score = response['score']

    #return a fromatted string with label and score
    if label is None:
        return 'Invalid input! Try again.'

    if label == 'empty':
        return 'Please Enter Text!'
    label_print = label.split('_')[1]
    return f"The given text has been identified as {label_print} with a score of {score} ."

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    #This functions executes the flask app and deploys it on localhost:5000
    app.run(host='0.0.0.0', port=5000)
