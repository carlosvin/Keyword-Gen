Simple Python command line tool to extract relevant keywords from an input string.

# Usage

```bash
> python keyword_calc.py -h

usage: keyword_calc.py [-h] [--exclusion_list [EXCLUSION_LIST [EXCLUSION_LIST ...]]] sentence

Extract a list of relevant keywords from an input string

positional arguments:
  sentence

optional arguments:
  -h, --help            show this help message and exit
  --exclusion_list [EXCLUSION_LIST [EXCLUSION_LIST ...]]
```

# Example
```bash
> python keyword_calc.py "En un lugar de la Mancha de cuyo nombre no quiero quiero" --exclusion_list En no de la un

# output
quiero
lugar
Mancha
cuyo
nombre
```
