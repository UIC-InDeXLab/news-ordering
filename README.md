# Maximizing Neutrality in News Ordering
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7159295.svg)](https://doi.org/10.5281/zenodo.7159295)

Companion repo for "Maximizing Neutrality in News Ordering" paper.

## Installation
- Clone the repo
- Create a virtual environment using e.g., venv or Conda
- Install any missing packages using e.g., pip or Conda
  - main packages are fairly standard (e.g., NetworkX, NumPy, SciPy, Matplotlib)

## Usage
- Run the desired notebook using Jupyter Notebook or JupyterLab

## Notebooks
- `generate_labeling_tasks.ipynb`: Given a set of news headlines, generates pairs of headlines to annotate.
- `labels_to_graph.ipynb`: Reads labeled data and converts it into graph format. Also contains code to fit data to statistical distribution.
- `detection.ipynb`: Given a dataset, determines whether ordering was cherry-picked.
- `maximizing_neutrality.ipynb`: Given synthetic or semi-synthetic dataset, finds orderings that approximately maximize neutrality.

## Authors

* **[Rishi Advani](https://rishi-advani.com/)**
* **[Paolo Papotti](https://www.eurecom.fr/~papotti/)**
* **[Abolfazl Asudeh](https://www.cs.uic.edu/~asudeh/)**

## License

This project is licensed under the MIT License &mdash; see the [LICENSE.md](LICENSE.md) file for details.

<p align="center"><img width="20%" src="https://www.cs.uic.edu/~indexlab/imgs/InDeXLab2.gif"></p>
