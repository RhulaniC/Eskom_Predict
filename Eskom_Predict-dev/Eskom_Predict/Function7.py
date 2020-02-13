def stop_words_remover(df):
    '''docstring'''
    
    df['Without Stop Words'] = df['Tweets'].str.lower().str.split()
    df['Without Stop Words'] = list(map(lambda x: [s for s in x if s not in stop_words_dict['stopwords']], df['Without Stop Words']))
    return df
