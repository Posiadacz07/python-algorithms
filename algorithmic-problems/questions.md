# Questions

1. Is there any smart way of filling the array with values e.g. first 10 numbers set to 0, next 10 to 1 and the rest to 2?

2. Dana jest lista n-elementów, stwórz listę wielkości k list zawierających różne kombinacje elementów n.

```python
list = [ ... ] # n-elementów
final_list = np.zeros(shape=(k, n), dtype=int) # lista k na n
for i in range(k):
    to_choose = list.copy()
    for j in range(n):
        element = random.choice(list(to_choose))
        final_list[i][j] = element
        to_choose.remove(element)
```
Czy jest na to lepszy sposób? 