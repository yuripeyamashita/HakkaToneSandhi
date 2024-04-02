## Usage
```python
from sandhi import sixian_sandhi as ss
from sandhi import hailu_sandhi as hs

result = ss(["samˊ", "ginˊ", "fanˊ", "teu"])
print(type(result))
print(result)

result = hs(["gonˊ", "liˋ", "zhug", "dungˋ"])
print(type(result))
print(result)
```

```
<class 'list'>
['samˇ', 'ginˇ', 'fanˇ', 'teu']
<class 'list'>
['gon+', 'liˋ', 'zhugˋ', 'dungˋ']
```
