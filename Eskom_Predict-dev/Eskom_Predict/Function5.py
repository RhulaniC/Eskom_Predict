
def number_of_tweets_per_day(df):
    '''docstring'''
<<<<<<< HEAD

=======
    
>>>>>>> 59030df2ed33999d405d5e5f2c7079d79f08c004
    twitter_df['Date'] = twitter_df['Date'].str[:10]
    df_out = twitter_df.groupby('Date').count()
    return df_out
