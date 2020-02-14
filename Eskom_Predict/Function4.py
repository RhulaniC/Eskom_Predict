def extract_municipality_hashtags(df):

"""
Takes a tweet on electricity and returns the municipality mentioned and any hashtags in that tweet.

A function which takes in a pandas dataframe and returns a modified dataframe that includes two new columns that contain information about the municipality and hashtag of the tweet, using the municipality dictionary.

Args:
    df (dataframe): pandas dataframe with tweets

Returns:
    dataframe: returns a modified dataframe that includes two new columns that contain information about the municipality and hashtag of the tweet.

"""

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
