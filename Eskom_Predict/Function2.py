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
             'q3':q3}

    return result
