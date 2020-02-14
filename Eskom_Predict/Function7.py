def stop_words_remover(df):
    """
    Return a modified dataframe with english stop words removed from a tokenised tweet.

    Args:
        df (dataframe): Dataframe containing atleast a "Date" column and "Tweets"
        column.

    Returns:
        (dataframe): Modified dataframe containing a column with english stop
        words removed from a tokenised tweet.

    Examples:
        >>> number_of_tweets_per_day(Twitter_dataframe)

        Tweets	                             Date	                Without Stop Words
    0	@BongaDlulane Please send...	     2019-11-29 12:50:54	[@bongadlulane, send, email, ...
    1	@saucy_mamiie Pls log...	         2019-11-29 12:46:53	[@saucy_mamiie, pls, log, ...
    2	@BongaDlulane Query...	             2019-11-29 12:46:10	[@bongadlulane, query, ...
    3	Before leaving the office...	     2019-11-29 12:33:36	[leaving, office, ...
    4	#ESKOMFREESTATE #MEDIASTATEMENT...	 2019-11-29 12:17:43	[#eskomfreestate, #mediastatement, ...

    """

    df['Without Stop Words'] = df['Tweets'].str.lower().str.split()
    df['Without Stop Words'] = list(map(lambda x: [s for s in x if s not in stop_words_dict['stopwords']], df['Without Stop Words']))
    return df
