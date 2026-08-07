# 🧠 Social Media NLP Analysis
*An exploratory Natural Language Processing case study using NLTK and TextBlob.*

## 📌 Project Overview
This project explores how Natural Language Processing can be used to analyse unstructured social-media text for linguistic and contextual indicators associated with planned public gatherings.

A fictional social-media post was processed using NLTK and TextBlob. The analysis included tokenisation, stopword removal, stemming, lemmatisation, part-of-speech tagging, named-entity recognition, syntactic parsing and sentiment analysis.

The purpose of the project was not to make an automated enforcement decision, but to investigate how NLP tools can convert informal, noisy text into structured information that may support human-led risk assessment and further investigation.

## 🎯 Objectives
- Examine the characteristics of unstructured social-media text.
- Apply a standard NLP preprocessing pipeline.
- Identify references to time, location, mobilisation and physical objects.
- Compare NLTK and TextBlob outputs.
- Evaluate sentiment and grammatical structure.
- Discuss the limitations of rule-based NLP techniques.
- Consider how more advanced tools could improve contextual accuracy.

## 📝 Text Sample
The analysis used a fictional social-media post containing informal language, hashtags, emojis, a time reference, a location and mobilisation-related phrases.

The example was designed to demonstrate the challenges involved in analysing short, noisy and context-dependent social-media text.

## 🔄 NLP Pipeline
The workflow included:

1. Sentence segmentation
2. Tokenisation
3. Stopword removal
4. Stemming
5. Part-of-speech tagging
6. Lemmatisation
7. Named-entity recognition
8. Syntactic parsing
9. Sentiment analysis

## 💻 Python Scripts

The project is organised into two scripts:

- **nltk_analysis.py** – performs text preprocessing, POS tagging, named-entity recognition, parsing and sentiment analysis using NLTK.

- **textblob_analysis.py** – analyses the same text using TextBlob to compare tokenisation, sentiment analysis, parsing and lemmatisation outputs.

## 📊 Results
The analysis identified references to time, location, mobilisation and physical objects within the text.

NLTK produced a sentiment score indicating a mainly neutral and moderately positive tone, while TextBlob also identified slightly positive polarity and moderate subjectivity. These findings suggest excitement or anticipation rather than explicit hostility.

The outputs also demonstrated several limitations, including incorrect named-entity classifications and difficulties interpreting hashtags, slang, emojis and context-dependent language.

## ⚖️ Limitations and Ethical Considerations
The analysis was based on a single fictional post and should not be interpreted as a reliable public-safety classification system.

Rule-based and lexicon-based NLP tools may misinterpret slang, sarcasm, emojis, coded language and local context. Automated outputs should therefore support, rather than replace, human judgement.

Any real-world application would also require careful consideration of privacy, proportionality, bias, transparency and the risk of incorrectly classifying harmless communication.

## 🧠 Skills Demonstrated
- Natural Language Processing
- Text preprocessing
- Tokenisation
- Stopword removal
- Stemming and lemmatisation
- Part-of-speech tagging
- Named-entity recognition
- Sentiment analysis
- Syntactic parsing
- Critical evaluation of NLP limitations

## 🚀 Future Improvements
Potential enhancements include:

- Analysing a larger, labelled dataset.
- Using spaCy for improved entity recognition and processing efficiency.
- Building a supervised text-classification model with scikit-learn.
- Comparing rule-based methods with transformer-based language models.
- Evaluating performance using precision, recall and F1-score.
- Introducing bias, fairness and explainability testing.

## 📄 Report
[View the full NLP analysis report](reports/Social_Media_NLP_Analysis_Report.pdf)

## 🌍 About the Author
