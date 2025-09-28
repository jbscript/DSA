# Python Time Complexity Reference

Quick reference guide for time complexities of common Python operations and methods.

## Lists

### Basic Operations
| Operation | Average Case | Worst Case |
|-----------|--------------|------------|
| `list[i]` (access) | O(1) | O(1) |
| `list[i] = x` (assignment) | O(1) | O(1) |
| `len(list)` | O(1) | O(1) |

### Modification
| Operation | Average Case | Worst Case |
|-----------|--------------|------------|
| `list.append(x)` | O(1) | O(n) |
| `list.insert(i, x)` | O(n) | O(n) |
| `list.pop()` | O(1) | O(1) |
| `list.pop(i)` | O(n) | O(n) |
| `list.remove(x)` | O(n) | O(n) |

### Search & Sort
| Operation | Time Complexity |
|-----------|-----------------|
| `x in list` | O(n) |
| `list.index(x)` | O(n) |
| `list.count(x)` | O(n) |
| `list.sort()` | O(n log n) |
| `sorted(list)` | O(n log n) |

## Dictionaries

| Operation | Average Case | Worst Case |
|-----------|--------------|------------|
| `dict[key]` | O(1) | O(n) |
| `dict[key] = value` | O(1) | O(n) |
| `key in dict` | O(1) | O(n) |
| `del dict[key]` | O(1) | O(n) |
| `dict.get(key)` | O(1) | O(n) |
| `dict.keys()` | O(1) | O(1) |
| `dict.values()` | O(1) | O(1) |
| `dict.items()` | O(1) | O(1) |

## Sets

| Operation | Average Case | Worst Case |
|-----------|--------------|------------|
| `x in set` | O(1) | O(n) |
| `set.add(x)` | O(1) | O(n) |
| `set.remove(x)` | O(1) | O(n) |
| `set.discard(x)` | O(1) | O(n) |
| `set1 & set2` (intersection) | O(min(len(set1), len(set2))) | O(len(set1) × len(set2)) |
| `set1 | set2` (union) | O(len(set1) + len(set2)) | O(len(set1) × len(set2)) |

## Strings

| Operation | Time Complexity |
|-----------|-----------------|
| `len(string)` | O(1) |
| `string[i]` | O(1) |
| `x in string` | O(n) |
| `string.find(x)` | O(n) |
| `string.replace(old, new)` | O(n) |
| `string.split()` | O(n) |
| `''.join(list)` | O(n) |

## Tuples

| Operation | Time Complexity |
|-----------|-----------------|
| `len(tuple)` | O(1) |
| `tuple[i]` | O(1) |
| `x in tuple` | O(n) |

## Common Algorithms

| Algorithm | Time Complexity | Space Complexity |
|-----------|-----------------|------------------|
| Binary Search | O(log n) | O(1) |
| Linear Search | O(n) | O(1) |
| Bubble Sort | O(n²) | O(1) |
| Merge Sort | O(n log n) | O(n) |
| Quick Sort | O(n log n) avg, O(n²) worst | O(log n) |
| Heap Sort | O(n log n) | O(1) |

## Built-in Functions

| Function | Time Complexity |
|----------|-----------------|
| `min(iterable)` | O(n) |
| `max(iterable)` | O(n) |
| `sum(iterable)` | O(n) |
| `sorted(iterable)` | O(n log n) |
| `reversed(iterable)` | O(n) |

## Tips for Optimization

1. **Use sets for membership testing** instead of lists when order doesn't matter
2. **Use dict.get()** instead of checking `if key in dict` then accessing
3. **Use list comprehensions** instead of loops when possible
4. **Use deque** from collections for frequent operations at both ends
5. **Use bisect** module for maintaining sorted lists efficiently

## Key Takeaways

- **Lists**: Great for indexed access, expensive for insertion/deletion in middle
- **Dictionaries**: Excellent for key-based lookups, O(1) average case
- **Sets**: Best for membership testing and set operations
- **Choose the right data structure** based on your most frequent operations