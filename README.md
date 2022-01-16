# Sentiment analysis in financial news

This service performes sentiment analysis in financial news using the FINBERT 
pre-trained model provided by ProsusAI and Hugging Face 
(https://huggingface.co/ProsusAI/finbert). 

FinBERT is a pre-trained NLP model to analyze sentiment of financial text. 
It is built by further training the BERT language model in the finance domain, 
using a large financial corpus and thereby fine-tuning it for financial sentiment 
classification.
## Installation
### Local
Install the dependencies by creating the Conda environment sentiment from the given environment.yml file and activating it:

conda env create -f environment.yml
conda activate sentiment

In terminal run:

python main.py

The application listens to localhost:5000/sentiment where you can post json data for sentiment prediction.
#### Example:

curl -X POST -H "Content-Type: application/json" -d '{"headline": "Nasdaq ekes out a higher close to end a volatile week, while Dow drops 200 points, or 0.56%"}' http://0.0.0.0:5000/sentiment/

Response:

{
  "Headline": "Nasdaq ekes out a higher close to end a volatile week, while Dow drops 200 points, or 0.56%", 
  "Positive": 0.06724409013986588, 
  "Negative": 0.9106093645095825, 
  "Neutral": 0.02214655466377735
}

### Docker
Clone the repository, navigate through terminal to the source file sentiment-analysis-for-financial-news and run:

docker build -t sentiment-analysis-for-financial-news .
docker run -d -p 5000:5000 sentiment-analysis-for-financial-news 
Now the app waits for post requests.


This service was developed in the scope of H2020 INFINITECH project.
https://marketplace.infinitech-h2020.eu