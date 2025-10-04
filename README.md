# Balloon Loop Heuristic (BLH) for the Traveling Salesman Problem

This repository introduces the **Balloon Loop Heuristic (BLH)**, a novel constructive approach for solving the **Traveling Salesman Problem (TSP)**.

BLH builds a "loop" by identifying the farthest city from the depot, visiting clustered cities on the way there, and collecting remaining cities on the return – similar to tightening a balloon. Combined with a lightweight **2-opt** local optimization, this yields near-optimal tours at low computational cost.

---

## Features
- Constructive TSP heuristic in **O(n log n)**
- Refinement with classical **2-opt**
- Tested on 50+ real cities (Germany + Luxembourg as depot)
- Produces smooth loop-like routes
- Open-source and easy to extend

---

## Example Result
BLH+2opt vs. NN+2opt (50+ cities):

| Method      | Tour length (eff. km) | Gap vs. NN+2opt |
|-------------|-----------------------|-----------------|
| BLH + 2-opt | 4521.7                | +3.7%           |
| NN + 2-opt  | 4360.2                | --              |

---

## Installation
```bash
git clone https://github.com/YOURNAME/blh-tsp.git
cd blh-tsp
pip install -r requirements.txt
```

---

## Usage
Run experiment:
```bash
python src/run_experiment.py
```

---

## License
This project is licensed under the MIT License – free to use and modify.

---

## Citation
If you use BLH in your research, please cite:
```
Fey, S., 2025.
"A Balloon Loop Heuristic for the Traveling Salesman Problem".
arXiv preprint.
```
