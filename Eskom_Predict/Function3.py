def date_parser(list_dates):
    """
    From datetime strings, return only the date in 'yyyy-mm-dd' format.

    Args:
        list_dates (list): List of datetime strings

    Returns:
        (list) : Extract only the date of each item in the input list
        and return in 'yyyy-mm-dd' format

    Examples:
        >>> date_parser(
                        ['2019-11-29 12:50:54',
                        '2019-11-29 12:46:53',
                        '2019-11-29 12:46:10'])

        ['2019-11-29',
         '2019-11-29',
         '2019-11-29']
        
    """

    dates_only = map(lambda x : x[:10] ,list_dates)
    return list(dates_only)
