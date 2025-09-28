| Feature                                 | `pop()`                           | `del`                                           |
| --------------------------------------- | --------------------------------- | ----------------------------------------------- |
| **Returns removed value?**              | ✅ Yes                            | ❌ No                                           |
| **Can remove by index?**                | ✅ Yes → `pop(index)`             | ✅ Yes → `del list[index]`                      |
| **Can remove last item?**               | ✅ Yes → `pop()` (default)        | ❌ No (must specify index or slice)             |
| **Supports slices (range)?**            | ❌ No                             | ✅ Yes → `del list[start:end]`                  |
| **Raises error if index out of range?** | ✅ Yes                            | ✅ Yes                                          |
| **Common use case**                     | When you _need the removed value_ | When you just _want to delete_ without using it |
