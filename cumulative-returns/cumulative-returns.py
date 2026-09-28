def cumulative_returns(returns: list) -> list:
    """
    Returns the compounded cumulative return after every period.
    """
    wealth = 1.0
    out = []
    for r in returns:
        wealth *= 1.0 + float(r)
        out.append(wealth - 1.0)
    return out