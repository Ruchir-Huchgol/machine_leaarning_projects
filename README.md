🚀 Machine Learning Projects
A structured collection of Python modules and experiments showcasing core machine learning techniques—ideal for interview bulk‑up.

📂 Project Structure
/                  # Root folder
├── vector.py      # Custom Vector class – implementation 1
├── vector2.py     # Custom Vector class – implementation 2
├── data/          # Sample datasets (if any)
├── notebooks/     # Jupyter notebooks for demonstration
└── README.md      # This file


🎯 Objective
Build and compare two independent implementations of a Vector class in Python.

Demonstrate understanding of core OOP concepts like operator overloading, immutability, and computational efficiency.

Showcase ability to analyze trade‑offs and strengthen code quality—valuable skills for placement interviews.

🧪 Comparative Study: vector.py vs vector2.py
| Feature                        | **vector.py**                         | **vector2.py**                           | ✅ Strength for Placements            |
| ------------------------------ | ------------------------------------- | ---------------------------------------- | ------------------------------------ |
| **Class Structure**            | Mutable `Vector` with in-place ops    | Immutable `Vector` (returns new objects) | Understand mutability vs purity      |
| **Operator Overloading**       | Implements `+`, `-`, `*`, `==`        | Also adds `@` (dot product), `norm()`    | Advanced operator usage              |
| **Error Handling**             | Basic type/length checks via `assert` | Raises custom exceptions for mismatch    | Emphasis on robust APIs              |
| **Performance Considerations** | Simple loops for operations           | Uses list comprehensions & `zip()`       | Efficient Pythonic code              |
| **Immutability Benefits**      | Simplicity, but risk of side‑effects  | Safer, easier to test/debug              | Highlights software design awareness |
| **Testing & Validation**       | Limited manual test cases             | Included unit tests using `pytest`       | Shows TDD familiarity                |
| **Documentation**              | Basic docstrings                      | Detailed docstrings + usage examples     | Demonstrates communication skills    |


💡 Key Takeaways
Mutability vs Immutability: vector.py is simple and intuitive, but vector2.py enforces better data integrity—great talking point for interviews.
Readability & Pythonic Style: vector2.py aligns with Pythonic best practices, using comprehensions and raising exceptions—shows production readiness.
Test‑Driven Approach: Inclusion of unit tests in vector2.py proves your discipline in writing reliable code.
Completeness: vector2.py offers extra utilities (norm(), dot product, angle calculation), demonstrating design foresight and extensibility.
