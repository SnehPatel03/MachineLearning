# Behind the Scenes of Loops in Python

## 1. Iteration Tools
- **For loops**
- **Comprehensions**
- **Map**
- Other constructs that can be used on **iterable objects** like:
  - List
  - String
  - File *(special case, explained below)*

---

## 2. Internal Method: `iter()`
- The `iter()` function is used to obtain an iterator object.  
- It points to the **first element** and prepares for iteration.

---

## 3. The `__next__()` Method
- The `__next__()` method retrieves the **next element** from the iterator.
- If the boundary is reached, Python raises an exception:
  - **`StopIteration`**

---

## 4. File Iteration (Unique Case)
- Files are **special iterables** in Python.  
- Direct method: `readline()` can be used to read line by line.  
- Internally, file iteration also uses the **`__next__()`** method.  
- When you open a file, it is **already iterable by default**, so there is no need to explicitly call `iter()`.

⚠️ In contrast:
- Lists and similar objects require `iter()` to get an iterator.

---

## 5. Example: `range()`
- `range(10)` is also an iterable.  
- It behaves similarly to lists and is handled by the iteration protocol.

---

**Key Takeaway**  
Iteration in Python is powered by:
- `iter()` → gets
