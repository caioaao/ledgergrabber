LINE_FMT = "P %(as_of)s %(symbol)s %(base)s %(quote)s"


def to_lines(quotes):
    return [LINE_FMT % {'as_of': as_of.strftime("%Y/%m/%d %H:%M:%S"),
                        'base': base,
                        'symbol': symbol,
                        'quote': quote}
            for symbol, base, quote, as_of in quotes]


def to_file(quotes, path):
    with open(path, 'w') as f:
        for line in to_lines(quotes):
            print(line, file=f)
