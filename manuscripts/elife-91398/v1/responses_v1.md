# Author response - Round 1

Authors:
- Harshvardhan Gazula
- Henry FJ Tregidgo ([ORCID: 0000-0002-3509-8154](https://orcid.org/0000-0002-3509-8154))
- Benjamin Billot
- Yael Balbastre
- Jonathan Williams-Ramirez
- Rogeny Herisse
- Lucas J Deden-Binder
- Adria Casamitjana
- Erica J Melief
- Caitlin S Latimer
- Mitchell D Kilgore ([ORCID: 0000-0003-1101-6924](https://orcid.org/0000-0003-1101-6924))
- Mark Montine
- Eleanor Robinson
- Emily Blackburn
- Michael S Marshall
- Theresa R Connors
- Derek H Oakley
- Matthew P Frosch
- Sean I Young
- Koen Van Leemput
- Adrian V Dalca
- Bruce Fischl
- Christine L MacDonald
- C Dirk Keene ([ORCID: 0000-0002-5291-1469](https://orcid.org/0000-0002-5291-1469))
- Bradley T Hyman ([ORCID: 0000-0002-7959-9401](https://orcid.org/0000-0002-7959-9401))
- Juan E Iglesias ([ORCID: 0000-0001-7569-173X](https://orcid.org/0000-0001-7569-173X))

## Response text

DOI: [10.7554/eLife.91398.4.sa3](https://doi.org/10.7554/eLife.91398.4.sa3)

The following is the authors’ response to the previous reviews.

Is the coronal slice in Figure 2 the corresponding mid-coronal plane to compute Dice scores? If so, the authors could mention it so that readers have an idea where the selected slice is.

This is indeed a good point. The coronal slice in Figure 2 is not part of the set of slices that we used to compute Dice scores. Showing such a slice is important, so we have added a small figure to the appendix with one of these slices, along with the corresponding automated segmentations.

SIFT descriptors were adopted to detect fiducials only. Maybe it could also be applied to align stacked photographs of brain slices.

While SIFT is robust against changes in pose (e.g., object rotation), perspective, and lightning, it is not robust against changes in the object itself – such as changes between one slice to the next, as is the case in our work. We have added a sentence to the methods section clarifying this issue.
