🧠 Vector Algebra RAG Application (Local ML Utility)
A locally executable Python-based application designed to implement and experiment with core vector algebra operations from scratch—useful in machine learning pipelines and retrieval-augmented generation (RAG) architectures, where embedding vectors and similarity math play a vital role.
This project builds reusable, lightweight vector functionality without relying on external libraries, ideal for educational, research, or prototype-level systems where full ML libraries may be overkill or unavailable.

🚀 Key Features
🧮 Custom Vector Class: Create and manipulate mathematical vectors natively in Python
🧠 RAG Utility Ready: Supports core operations like dot product and norm—essential for vector similarity and scoring
⚙️ No External Dependencies: Fully native Python; easy to integrate, run, and extend
💡 Designed for Learning and Prototyping: Great for ML students, interview prep, and low-resource scenarios

🛠️ How to Use
# Clone the repo
git clone https://github.com/Ruchir-Huchgol/machine_leaarning_projects.git
cd machine_leaarning_projects

# Run a test script or open interactive shell
python3
>>> from vector2 import Vector
>>> v1 = Vector([1, 2, 3])
>>> v2 = Vector([4, 5, 6])
>>> print(v1 + v2)  # Output: Vector([5, 7, 9])
To run with unit tests (if available in vector2.py):
pip install pytest
pytest


🔍 Comparative Design Study: vector.py vs vector2.py
| Aspect                   | `vector.py`                   | `vector2.py`                                  |
| ------------------------ | ----------------------------- | --------------------------------------------- |
| **Design Style**         | Mutable objects, in-place ops | Immutable, functional design                  |
| **Operator Overloading** | Basic: `+`, `-`, `*`          | Extended: `@` (dot), `norm()`, comparison ops |
| **Error Handling**       | `assert`-based checks         | Proper exceptions and validation              |
| **Performance**          | Manual loops                  | Pythonic with `zip()` and comprehensions      |
| **Testing**              | Minimal                       | Includes `pytest`-based tests                 |
| **Documentation**        | Basic docstrings              | Rich docstrings and usage examples            |



📌 Takeaway:
The comparison highlights design trade-offs around performance, reliability, and code quality. These implementations demonstrate engineering depth, making this project a solid talking point for interviews and placements.
