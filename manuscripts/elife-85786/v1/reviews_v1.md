# Peer review - Round 1

Editors:
- Caleb Kemere, Rice University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.85786.3.sa0](https://doi.org/10.7554/eLife.85786.3.sa0)

This paper introduces the python software package Pynapple and a separate package of more advanced routines (Pynacollada) to the Neuroscience/Neural Engineering community. Pynapple provides a set of data objects and methods that have the potential to simplify data analysis for neural and behavioral data types. This represents a valuable contribution to the field. With more examples and as a live coding notebook, the evidence was judged to be compelling.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.85786.3.sa1](https://doi.org/10.7554/eLife.85786.3.sa1)

A typical path from preprocessed data to findings in systems neuroscience often includes set of analyses that often share common components. For example, an investigator might want to generate plots that relating one time series (e.g., a set of spike times) to another (measurements of a behavioral parameter such as pupil diameter or running speed). In most cases, each individual scientist writes their own code to carry out these analyses, and thus the same basic analysis is coded repeatedly. This is problematic for several reasons, including the inefficiency of different people writing the same code over and over again.

This paper presents Pynapple, a python package that aims to address those problems.

Strengths:

The authors have identified a key need in the community - well written analysis routines that carry out a core set of functions and can import data from multiple formats. In addition, they recognized that there are some common elements of many analyses, particularly those involving timeseries, and their object-oriented architecture takes advantage of those commonalities to simplify the overall analysis process.

The package is separated into a core set of applications and another with more advanced applications, with the goal of both providing a streamlined base for analyses and allowing for implementations/inclusion of more experimental approaches.

Weaknesses:

The revised version of the paper does a very good job of addressing previous concerns. It would be slightly more accurate in the Highlights section to say "A lightweight and standalone package facilitating long-term backward compatibility" but this is a very minor issue.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.85786.3.sa2](https://doi.org/10.7554/eLife.85786.3.sa2)

The manuscript by G. Viejo et al. describes a new open-source toolbox called Pynapple, for data analysis of electrophysiological recordings, calcium imaging, and behavioral data. It is an object-oriented python package, consisting of 5 main object types: timestamps (Ts), timestamped data (Tsd), TsGroup, TsdFrame, and IntervalSet. Each object has a set of built-in core methods and import tools for common data acquisition systems and pipelines.

Pynapple is a low-level package that uses NWB as a file format, and further allows for other more advanced toolsets to build upon it. One of these is called Pynacollada which is a toolset for data analysis of electrophysiological, imaging, and behavioral data.

Pynapple and Pynacollada have the potential to become very valuable and foundational tools for the analysis of neurophysiological data. NWB still has a steep learning curve and Pynapple offers a user-friendly toolset that can also serve as a wrapper for NWB.
