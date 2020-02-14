def dictionary_of_metrics(items):
    ## caltulating the mean
    average= round(sum(items)/len(items),2)
    ## calculating maximum value
    maximum = max(items)
    ## calculating minimun value
    minimum =min(items)


    n = len(items)
    s = sorted(items)
    ##calculating variance and std dev
    var =round(sum([((x - average) ** 2) for x in items]) /(n-1),2)
    ##var1=np.var(items)
    stddev=round(var**0.5,2)
    ##calculating median
    if (n%2)==0:
                lower=int(n/2)-1
                upper =lower +1
                median = round((s[lower]+s[upper])/2,2)

    else:
        median = s[int(n/2)]
      ## returning the results as a dictionary

    results =  {'mean': average,
              'median': median,
             'var': var ,
              'std': stddev,
              'min':  minimum,
              'max': maximum}

    return results
