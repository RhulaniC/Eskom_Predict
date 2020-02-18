import numpy as np
def dictionary_of_metrics(items):

    # caltulating the mean
    average= round(sum(items)/len(items),2)
    # calculating maximum value
    maximum = max(items)
    # calculating minimun value
    minimum =min(items)


    n = len(items)
    s = sorted(items)
    #calculating variance and std dev
    var =round(sum([((x - average) ** 2) for x in items]) /(n-1),2)
    #var1=np.var(items)
    stddev=round(var**0.5,2)
    #calculating median
    if (n%2)==0:
        lower=int(n/2)-1
        upper =lower +1
        median = round((s[lower]+s[upper])/2,2)

    else:
        median = s[int(n/2)]

    # returning the results as a dictionary
    results =  {'mean': average,
                'median': median,
                'var': var ,
                'std': stddev,
                'min':  minimum,
                'max': maximum}

    return results



def five_num_summary(items):

    #sort list into ascending order
    s = sorted(items)

    #calculate 5 number summary rounded to 2 decimal places
    a = round(np.max(s),2)
    b = round(np.min(s),2)
    c = round(np.median(s),2)
    q1 = round(np.percentile(s,25),2)
    q3 = round(np.percentile(s,75),2)

    #return function as a dictionary
    result = {'max':a,
              'median':c,
              'min':b,
              'q1':q1,
              'q3':q3 }

    return result



def date_parser(list_dates):

    #Remove the dates in the format 'yyyy-mm-dd' from the given list
    dates_only = list(map(lambda x : x[:10] ,list_dates))
    #Return the list containing only the dates
    return dates_only



def extract_municipality_hashtags(df):

    mun_dict = { '@CityofCTAlerts' : 'Cape Town',
                 '@CityPowerJhb' : 'Johannesburg',
                 '@eThekwiniM' : 'eThekwini' ,
                 '@EMMInfo' : 'Ekurhuleni',
                 '@centlecutility' : 'Mangaung',
                 '@NMBmunicipality' : 'Nelson Mandela Bay',
                 '@CityTshwane' : 'Tshwane' }

    #Create two new columns and input default values "NaN"
    df['municipality'] = np.nan
    df['hashtags'] = np.nan

    #Create intermediate dataframe omitting colons from df
    df1 = df['Tweets'].str.replace(':', '')

    for keys,values in mun_dict.items():
        for i in range(200):
            #if key (from dictionary) is found in the tweet, then:
            if keys in df1.str.split()[i]:
                #output corresponding value (from dictionary) into 'municipality' column
                df['municipality'][i] = values

    #extracting all hashtags from tweets and displaying them in 'hashtags' column as lowercase
    df['hashtags'] = list(map(lambda token: [x for x in token if x.startswith('#')], df['Tweets'].str.lower().str.split()))
    for i in range(200):
        #if tweet has no hashtag, then:
        if df['hashtags'][i] == []:
            #output 'NaN'
            df['hashtags'][i] = np.nan
    #return dataframe with new columns
    return df



def number_of_tweets_per_day(df):

    #Extract the 'Date' column from the input twitter dataframe
    twitter_df['Date'] = twitter_df['Date'].str[:10]
    #Group by date and count the number of tweets per date
    df_out = twitter_df.groupby('Date').count()
    #Return dataframe containing the date and number of tweets per day
    return df_out



def word_splitter(df):

    #Tokenize lowercase tweets
    df['Split Tweets'] = df['Tweets'].str.lower().str.split()
    #Return modified dataframe
    return df



def stop_words_remover(df):

    # dictionary of english stopwords
    stop_words_dict = {'stopwords':[
        'where', 'done', 'if', 'before', 'll', 'very', 'keep', 'something', 'nothing', 'thereupon',
        'may', 'why', 'â€™s', 'therefore', 'you', 'with', 'towards', 'make', 'really', 'few', 'former',
        'during', 'mine', 'do', 'would', 'of', 'off', 'six', 'yourself', 'becoming', 'through',
        'seeming', 'hence', 'us', 'anywhere', 'regarding', 'whole', 'down', 'seem', 'whereas', 'to',
        'their', 'various', 'thereafter', 'â€˜d', 'above', 'put', 'sometime', 'moreover', 'whoever', 'although',
        'at', 'four', 'each', 'among', 'whatever', 'any', 'anyhow', 'herein', 'become', 'last', 'between', 'still',
        'was', 'almost', 'twelve', 'used', 'who', 'go', 'not', 'enough', 'well', 'â€™ve', 'might', 'see', 'whose',
        'everywhere', 'yourselves', 'across', 'myself', 'further', 'did', 'then', 'is', 'except', 'up', 'take',
        'became', 'however', 'many', 'thence', 'onto', 'â€˜m', 'my', 'own', 'must', 'wherein', 'elsewhere', 'behind',
        'becomes', 'alone', 'due', 'being', 'neither', 'a', 'over', 'beside', 'fifteen', 'meanwhile', 'upon', 'next',
        'forty', 'what', 'less', 'and', 'please', 'toward', 'about', 'below', 'hereafter', 'whether', 'yet', 'nor',
        'against', 'whereupon', 'top', 'first', 'three', 'show', 'per', 'five', 'two', 'ourselves', 'whenever',
        'get', 'thereby', 'noone', 'had', 'now', 'everyone', 'everything', 'nowhere', 'ca', 'though', 'least',
        'so', 'both', 'otherwise', 'whereby', 'unless', 'somewhere', 'give', 'formerly', 'â€™d', 'under',
        'while', 'empty', 'doing', 'besides', 'thus', 'this', 'anyone', 'its', 'after', 'bottom', 'call',
        'nâ€™t', 'name', 'even', 'eleven', 'by', 'from', 'when', 'or', 'anyway', 'how', 'the', 'all',
        'much', 'another', 'since', 'hundred', 'serious', 'â€˜ve', 'ever', 'out', 'full', 'themselves',
        'been', 'in', "'d", 'wherever', 'part', 'someone', 'therein', 'can', 'seemed', 'hereby', 'others',
        "'s", "'re", 'most', 'one', "n't", 'into', 'some', 'will', 'these', 'twenty', 'here', 'as', 'nobody',
        'also', 'along', 'than', 'anything', 'he', 'there', 'does', 'we', 'â€™ll', 'latterly', 'are', 'ten',
        'hers', 'should', 'they', 'â€˜s', 'either', 'am', 'be', 'perhaps', 'â€™re', 'only', 'namely', 'sixty',
        'made', "'m", 'always', 'those', 'have', 'again', 'her', 'once', 'ours', 'herself', 'else', 'has', 'nine',
        'more', 'sometimes', 'your', 'yours', 'that', 'around', 'his', 'indeed', 'mostly', 'cannot', 'â€˜ll', 'too',
        'seems', 'â€™m', 'himself', 'latter', 'whither', 'amount', 'other', 'nevertheless', 'whom', 'for', 'somehow',
        'beforehand', 'just', 'an', 'beyond', 'amongst', 'none', "'ve", 'say', 'via', 'but', 'often', 're', 'our',
        'because', 'rather', 'using', 'without', 'throughout', 'on', 'she', 'never', 'eight', 'no', 'hereupon',
        'them', 'whereafter', 'quite', 'which', 'move', 'thru', 'until', 'afterwards', 'fifty', 'i', 'itself', 'nâ€˜t',
        'him', 'could', 'front', 'within', 'â€˜re', 'back', 'such', 'already', 'several', 'side', 'whence', 'me',
        'same', 'were', 'it', 'every', 'third', 'together'
        ]
    }
    #Tokenize lowercase tweets
    df['Without Stop Words'] = df['Tweets'].str.lower().str.split()
    #Remove stopwords
    df['Without Stop Words'] = list(map(lambda x: [s for s in x if s not in stop_words_dict['stopwords']], df['Without Stop Words']))
    #Return modified dataframe
    return df
