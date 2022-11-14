import streamlit as st
from nltk.sentiment import SentimentIntensityAnalyzer
import glob
import plotly.express as px

files = glob.glob('diary/*.txt')

entries = []
for file in files:
    with open(file, 'r', encoding='utf-8') as entry:
        entry = entry.read()
        entries.append(entry)

analyzer = SentimentIntensityAnalyzer()

pos = []
neg = []

for entry in entries:
    score = analyzer.polarity_scores(entry)
    pos.append(score['pos'])
    neg.append(score['neg'])


dates = [date.split('\\')[1].split('.')[0] for date in files]

st.header('Diary Mood')
pos_figure = px.line(x=dates, y=pos, labels={'x': 'Dates', 'y': 'Positivity'})
st.subheader('Positivity')
st.plotly_chart(pos_figure)
neg_figure = px.line(x=dates, y=neg, labels={'x': 'Dates', 'y': 'Negativity'})
st.subheader('Negativity')
st.plotly_chart(neg_figure)


