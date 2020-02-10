def date_parser(list_dates):
    """
    doctrings
    """

    dates_only = map(lambda x : x[:10] ,list_dates)
    return list(dates_only)
