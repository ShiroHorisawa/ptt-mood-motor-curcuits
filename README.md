# Dissociation of Mood and Motor Circuits in the Human Subthalamic Region

This repository contains minimal code used to reproduce the core analyses described in the study:

"Dissociation of Mood and Motor Circuits in the Human Subthalamic Region".

## Overview

The code implements connectome-based lesion–fiber engagement analysis.

Main steps include:

1. Fiber weight estimation
2. Raw and Balance score calculation
3. Permutation testing
4. Bootstrap confidence intervals

## Example workflow

```bash
python scripts/compute_fiber_weights.py
python scripts/compute_prediction_scores.py
python scripts/permutation_test.py
python scripts/bootstrap_ci.py
```
