# ledgergrabber

Utils for creating prices files for [Ledger CLI](http://ledger-cli.org/).

## Examples

```python
from ledgergrabber import fiat
from ledgergrabber import crypto
import ledgergrabber.core

# Quotes functions returns lists of tuples with `(symbol, base, quote, as_of)`
fiat_quotes = fiat.from_fixer_io(base='EUR', symbols=['BRL', 'USD'])
crypto_quotes = crypto.from_coinmarketcap(base='EUR')

# saving it
ledgergrabber.core.to_file(fiat_quotes + crypto_quotes, "./prices_db")
```
