""" This code cleans a csv-text dataset. Removing stopwords etc.
Finally it will export the clean dataset as a csv-file.
"""
# Import libraries
import pandas as pd
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

def clean_data(csv_file):
    """ Loads data and prepares data (feature transformation)
        Input: csv-file with messages and class
         (spam = 1 or not spam = 0 )
        Output: pd-DataFrame-object
    """
    # load csv file
    data = pd.read_csv(csv_file)

    data['text'] = data['text'].str.strip('fw :')
    data['text'] = data['text'].str.strip(' re : ')

    stop_words = set(stopwords.words('english'))
    tokenizer = RegexpTokenizer(r'\w+')
    ps = PorterStemmer()

    numb_mails = len(data.text)

    # Loops through each message (email)
    for message in range(numb_mails):
        # make message lower case
        text = data.text[message]

        # Substitute special tokens with descriptive strings
        text = text.replace('$', 'DOLLAR')
        text = text.replace('@', 'EMAILADRESS')
        text = text.replace('https', 'URL')
        text = text.replace('www', 'URL')

        # Remove unescessary information
        text = text.replace('Subject', '')
        text = text.replace('cc', '')

        # Make text lower case
        text = text.lower()

        # Tokenize + remove punctuation
        tokens1 = tokenizer.tokenize(text)

        # Remove stop-words
        tokens2 = [w for w in tokens1 if not w in stop_words]

        # Stemming tokens
        numb_tokens = len(tokens2)

        for token in range(numb_tokens):
            tokens2[token] = ps.stem(tokens2[token])

        # Sustitute number (special token) with 'NUMBER'
        #(numbers can be split by with space)
        for token in range(numb_tokens):
             try:
                 int(tokens2[token])
                 tokens2[token] = "NUMBER"
             except:
                 pass

        last_token = ""
        for token in reversed(range(numb_tokens)):
            if (last_token == tokens2[token]) and (last_token=='NUMBER'):
                del tokens2[token+1]

            last_token = tokens2[token]

        # Collect tokens to string and assign to dataframe
        prepared_string = " ".join(tokens2)

        data.at[message,'text'] = prepared_string

    return data

result = clean_data('emails.csv')
result.to_csv('processedEmails.csv', encoding='utf-8', index = False)

print('Done, number of lines ', len(result))
