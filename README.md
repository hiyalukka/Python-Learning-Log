# Python Learning Log

Notes from learning Python for machine learning. One concept per file, every output comment checked by a script.

## Inside the repo

- **A gotcha library.** Every surprise gets a `GOTCHA:` tag, and one script collects them all into a cheatsheet of the mistakes I actually made.
- **Notes that check themselves.** A checker runs each file and confirms what the comments claim it prints.
- **Self-tests with hidden answers.** Every file ends with questions I should still be able to answer a week later.
- **Predictions on the record.** I write down what I expect before running the code, and log what I got wrong.
- **Mini projects.** Every few topics, one small build using only what I've learned so far.

## What a note looks like

```python
a = [1, 2, 3]
b = a                        # NOT a copy, same list with two names
b.append(4)
print(a)                     # Output: [1, 2, 3, 4]
# GOTCHA: `b = a` does not copy. Use a.copy() for a real copy.
# WHY: a variable points to the list, it doesn't hold it.
```

Tags: `Output` `KEY` `GOTCHA` `WHY` `PREDICT` `TRY` `RECALL`. Every file also ends with a self-test and hidden answers.

## The checker

Output comments go stale when code changes. `tools/check_outputs.py` runs a file and compares each `# Output:` comment with what it really prints.

```console
$ python tools/check_outputs.py 01-basics/1_syntax_and_indentation.py
[OK ] 01-basics/1_syntax_and_indentation.py  (16 output comments checked, 0 wrong)
```

Standard library only.

## Roadmap

Follows the Udemy data science and ML bootcamp. Full subtopic checklist: [CHECKLIST.md](CHECKLIST.md).

- [ ] **1. Python basics** (in progress): syntax, variables, data types, operators
- [ ] **2. Control flow**: conditionals, loops
- [ ] **3. Data structures**: lists, tuples, sets, dictionaries
- [ ] **4. Functions**: parameters, lambda, map, filter
- [ ] **5. Modules**: imports, packages, standard library
- [ ] **6. File handling**: reading, writing, paths
- [ ] **7. Exception handling**
- [ ] **8. Classes and objects**: inheritance, polymorphism, magic methods
- [ ] **9. Advanced Python**: iterators, generators, decorators
- [ ] **10. Data analysis**: NumPy, pandas, matplotlib, seaborn
- [ ] **11. Databases**: SQLite
- [ ] **12. Logging**
- [ ] **13. Flask**
- [ ] **14. Streamlit**
- [ ] **15. Memory management**
- [ ] **16. Multithreading and multiprocessing**

Then machine learning.

## How I study each topic

Write the example myself, predict the output before running it, break it on purpose, then rewrite from a blank file the next day and re-test myself a week later. Mistakes stay in the history.

## Use it for your own course

Click **Use this template**, copy `_templates/concept_template.py` for each concept, and run the checker before each commit.

## About

Hiya, second-year B.Tech student (AI/ML).Course materials belong to their authors; this repo holds only my own notes and code.

[GitHub](https://github.com/hiyalukka) · [LinkedIn](https://www.linkedin.com/in/hiya-lukka/) · [Substack](https://substack.com/@hiyaepochs)
