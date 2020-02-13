def extract_municipality_hashtags(df):

    #Create two new columns and input default values "NaN"
    df['municipality'] = np.nan
    df['hashtags'] = np.nan

    #Create intermediate dataframe omitting colons from df
    df1 = df['Tweets'].str.replace(':', '')

    for keys,values in mun_dict.items():
        for i in range(200):
            if keys in df1.str.split()[i]:            #if key (from dictionary) is found in the tweet, then:
                df['municipality'][i] = values        #output corresponding value (from dictionary) into 'municipality' column

    #extracting all hashtags from tweets and displaying them in 'hashtags' column as lowercase
    df['hashtags'] = list(map(lambda token: [x for x in token if x.startswith('#')], df['Tweets'].str.lower().str.split()))
    for i in range(200):
        if df['hashtags'][i] == []:                   #if tweet has no hashtag, then:
            df['hashtags'][i] = np.nan                #output 'NaN'
    return df                                         #return dataframe with new columns
