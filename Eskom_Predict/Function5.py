
def number_of_tweets_per_day(df):
    '''docstring'''
    
    twitter_df['Date'] = twitter_df['Date'].str[:10]
    df_out = twitter_df.groupby('Date').count()
    return df_out
