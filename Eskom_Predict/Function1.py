def dictionary_of_metrics(items):

    """

    Function that calculates the mean, median, variance, standard deviation,
    minimum and maximum of of list of items.


    The function calculates the mean, median, variance, standard deviation,
    minimum and maximum of of list of items.
    The input is a list of integers and it outputs as a dictionary.

    Args:
        items (list): List of integers

    Returns:
        dictionary: with keys 'mean', 'median', 'std', 'var', 'min', and 'max',
        corresponding to the mean, median, standard deviation, variance, minimum
        and maximum of the input list


    """

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
