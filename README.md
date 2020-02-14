# Eskom_Predict Package
Python functions used to analyse and calctulate data from Eskom. These functions process both numerical and text data.

## What you will need
This project runs on the latest version of Python. Before you can start, ensure that the latest version of python is intalled.  

## Intalling the project package from GitHub
 issue this command to install from GitHub:
 `pip install git+https://github.com/Xenaschke/Eskom_Predict.git`
 
 if you need to install the latest version of this package, use:
 `pip install --upgrade git+https://github.com/Xenaschke/Eskom_Predict.git`
 
## Running the codes
Once the package is installed into python the following fucntions can be used to get the metrics:

### Fuction 1

### Fuction 2
For this function, you have to first import numpy. The function five_num_summary(items) takes in a list of integers and returns a dictionary of the five number summary. 
#### Example
An argument items = [3,5,6,78,8,9,9,6,4,6.8,7,8,9,1] will return {'max': 78.0, 'median': 6.9, 'min': 1.0, 'q1': 5.25, 'q3': 8.75}

### Function 3
This function date_parser(list_dates) takes in a list of datetime strings, extracts the dates of each item in the list, and returns the date in 'yyyy-mm-dd' format.

#### Example 
An argument list_dates = ['2019-11-29 12:50:54','2019-11-29 12:46:53''2019-11-29 12:46:10'] will return ['2019-11-29', '2019-11-29', '2019-11-29'].

### Function 4
This function extract_municipality_hashtags(df) takes in pandas dataframe with tweets and returns a modified dataframe that includes two new columns containing information about the municipality and  the tweet hashtag (in lowercase).

#### Example 
An argument twitter_df.copy() = 	  Tweets                                               Date
                                 0	@BongaDlulane Please send an email to mediades...	 2019-11-29 12:50:54
                                 1	@saucy_mamiie Pls log a call on 0860037566	        2019-11-29 12:46:53
                                 2	@BongaDlulane Query escalated to media desk.	      2019-11-29 12:46:10
                                 3	Before leaving the office this afternoon, head... 	2019-11-29 12:33:36
                                 4	#ESKOMFREESTATE #MEDIASTATEMENT : ESKOM SUSPEN...	 2019-11-29 12:17:43
  Tweets	                                            Date         	        municipality     	hashtags
0	@BongaDlulane Please send an email to mediades...	  2019-11-29 12:50:54	 NaN	               NaN
1	@saucy_mamiie Pls log a call on 0860037566	         2019-11-29 12:46:53	 NaN               	NaN
2	@BongaDlulane Query escalated to media desk.	       2019-11-29 12:46:10	 NaN               	NaN
3	Before leaving the office this afternoon, head...	  2019-11-29 12:33:36 	NaN	               NaN
4	#ESKOMFREESTATE #MEDIASTATEMENT : ESKOM SUSPEN...	  2019-11-29 12:17:43	 NaN	               [#eskomfreestate, #mediastatement]
...	...	...	...	...
195	Eskom's Visitors Centresâ€™ facilities include i  2019-11-20 10:29:07	 NaN	               NaN
196	#Eskom connected 400 houses and in the process...	2019-11-20 10:25:20	 NaN	               [#eskom, #eskom, #poweringyourworld]
197	@ArthurGodbeer Is the power restored as yet?	     2019-11-20 10:07:59	 NaN	               NaN
198	@MuthambiPaulina @SABCNewsOnline @IOL @eNCA @e...	2019-11-20 10:07:41	 NaN               	NaN
199	RT @GP_DHS: The @GautengProvince made a commit...	2019-11-20 10:00:09	 NaN	               NaN

### Function 5
This function takes in Dataframe containing atleast a "Date" column and "Tweets" column and returns a Dataframe grouped by day, with the number of tweets for that day.

#### Example 
An argument twitter_df.copy() = 	  Tweets                                               Date
                                 0	@BongaDlulane Please send an email to mediades...	 2019-11-29 12:50:54
                                 1	@saucy_mamiie Pls log a call on 0860037566	        2019-11-29 12:46:53
                                 2	@BongaDlulane Query escalated to media desk.	      2019-11-29 12:46:10
                                 3	Before leaving the office this afternoon, head... 	2019-11-29 12:33:36
                                 4	#ESKOMFREESTATE #MEDIASTATEMENT : ESKOM SUSPEN...	 2019-11-29 12:17:43
                                 
                                 
will return: Date	       Tweets
            2019-11-20	  18
            2019-11-21	  11
            2019-11-22	  25
            2019-11-23	  19
            2019-11-24	  14
            2019-11-25	  20
            2019-11-26  	32
            2019-11-27  	13
            2019-11-28  	32
            2019-11-29	  16    
### Function 6
This function word_splitter(df) takes in pandas dataframe with tweets and returns a modified dataframe that includes a new column that contains the tokenized tweets (in lowercase).

#### Example
An argument  df   =                 Tweets                                                  Date
                                 0	@BongaDlulane Please send an email to mediades...	 2019-11-29 12:50:54
                                 1	@saucy_mamiie Pls log a call on 0860037566	        2019-11-29 12:46:53
                                 2	@BongaDlulane Query escalated to media desk.	      2019-11-29 12:46:10
                                 3	Before leaving the office this afternoon, head... 	2019-11-29 12:33:36
                                 4	#ESKOMFREESTATE #MEDIASTATEMENT : ESKOM SUSPEN...	 2019-11-29 12:17:43

      Tweets	                                                Date	        Split Tweets
    0	@BongaDlulane Please send an email to mediades...	    2019-11-29	    [@bongadlulane, please, send, an, email, to, m...
    1	@saucy_mamiie Pls log a call on 0860037566	           2019-11-29	    [@saucy_mamiie, pls, log, a, call, on, 0860037...
    2	@BongaDlulane Query escalated to media desk.	         2019-11-29	    [@bongadlulane, query, escalated, to, media, d...
    3	Before leaving the office this afternoon, head...     2019-11-29    	[before, leaving, the, office, this, afternoon...
    4	#ESKOMFREESTATE #MEDIASTATEMENT : ESKOM SUSPEN...	    2019-11-29	    [#eskomfreestate, #mediastatement, :, eskom, s...

### Function 7 
This function  stop_words_remover(df) takes in Dataframe containing atleast a "Date" column and "Tweets" column and returns a modified dataframe containing a column with english stop words removed from a tokenised tweet.

#### Example

An argument df =                    Tweets                                               Date
                                 0	@BongaDlulane Please send an email to mediades...	 2019-11-29 12:50:54
                                 1	@saucy_mamiie Pls log a call on 0860037566	        2019-11-29 12:46:53
                                 2	@BongaDlulane Query escalated to media desk.	      2019-11-29 12:46:10
                                 3	Before leaving the office this afternoon, head... 	2019-11-29 12:33:36
                                 4	#ESKOMFREESTATE #MEDIASTATEMENT : ESKOM SUSPEN...	 2019-11-29 12:17:43
Returns

     Tweets	                             Date	                Without Stop Words
    0	@BongaDlulane Please send...	     2019-11-29 12:50:54	 [@bongadlulane, send, email, ...
    1	@saucy_mamiie Pls log...	         2019-11-29 12:46:53	 [@saucy_mamiie, pls, log, ...
    2	@BongaDlulane Query...	           2019-11-29 12:46:10	 [@bongadlulane, query, ...
    3	Before leaving the office...	     2019-11-29 12:33:36	 [leaving, office, ...
    4	#ESKOMFREESTATE #MEDIASTATEMENT...2019-11-29 12:17:43	 [#eskomfreestate, #mediastatement, ...
    
## How to contribute to the project
To contribute to this repository, one needs to email the owners of this repository before making any changes. 
For pull request process: Update the README.md with details of changes to the interface
                          You may merge the Pull Request in once you have the sign-off of the developers.
## Authors

Abdullah Shaikh  
Kolobe Rufus Seopa
Tshegofatjo Makhafola
Vahiel Moodley
Xenaschke Croucamp

## Acknowledgements
Damian Vather for his assistance.
    
