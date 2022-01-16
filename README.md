# Sentiment analysis in financial news

This service performs sentiment analysis in financial news using the FinBERT 
pre-trained model provided by 
[ProsusAI and Hugging Face](https://huggingface.co/ProsusAI/finbert). 

FinBERT is a pre-trained NLP model to analyze sentiment of financial text. 
It is built by further training the BERT language model in the finance domain, 
using a large financial corpus and thereby fine-tuning it for financial sentiment 
classification.
## Installation
### Local
Install the dependencies by creating the Conda environment sentiment from the given environment.yml file and activating it:
```
conda env create -f environment.yml
conda activate sentiment
```

In terminal run:
`python main.py`

The application will listen to `localhost:5000/sentiment` where you can post json data for sentiment prediction.

### Docker
Clone the repository, navigate through terminal to the source file sentiment-analysis-for-financial-news and run:
```
docker build -t sentiment-analysis-for-financial-news .
docker run -d -p 5000:5000 sentiment-analysis-for-financial-news
```
Now the app waits for post requests.
### Example
` curl -X POST -H "Content-Type: application/json" -d '{"headline": "Nasdaq ekes out a higher close to end a volatile week, while Dow drops 200 points, or 0.56%"}' http://0.0.0.0:5000/sentiment/`

Response:
```
{
  "Headline": "Nasdaq ekes out a higher close
  to end a volatile week, 
  while Dow drops 200 points, or 0.56%", 
  "Positive": 0.06724409013986588, 
  "Negative": 0.9106093645095825, 
  "Neutral": 0.02214655466377735
}
```
## Deploy in Tutorial Notebook Mode
Experimentation with this model is also available through a 
Jupyter Notebook included in this repository. 
The notebook includes code for:
1. Connect to Twitter API and query tweets
2. Tweets' preprocessing
3. Sentiment analysis in the downloaded tweets using the FinBERT model
4. Visualization of sentiment predictions

To run the tutorial on your local machine, you will need to have 
a Python Jupyter server running locally. You can download and
install [Jupyter](https://jupyter.org). Once running, 
you can download the notebook version of the model from 
the [GitHub link](https://github.com/giorgosfatouros/sentiment-analysis-for-financial-news/blob/main/Twiter-Sentiment-Analysis-with-FinBERT%20.ipynb)
and save it on your computer (right-click on the file and select ‘Save Link As..’), 
then open it with your Jupyter server. You should make sure to save the notebook in a directory that the Jupyter server can access.


> This service was developed in the scope of 
> [H2020 INFINITECH project](https://marketplace.infinitech-h2020.eu).