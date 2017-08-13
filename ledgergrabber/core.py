LINE_FMT = "P %(as_of)s %(symbol)s %(base)s %(quote)s"


def to_lines(quotes, aliases={}):
    return [LINE_FMT % {'as_of': as_of.strftime("%Y/%m/%d %H:%M:%S"),
                        'base': aliases.get(base, base),
                        'symbol': aliases.get(symbol, symbol),
                        'quote': quote}
            for symbol, base, quote, as_of in quotes]


def to_file(quotes, path, aliases={}):
    with open(path, 'w') as f:
        for line in to_lines(quotes, aliases):
            print(line, file=f)
