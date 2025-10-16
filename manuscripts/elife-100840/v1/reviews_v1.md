# Peer review - Round 1

Editors:
- Caleb Kemere, Rice University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.100840.3.sa0](https://doi.org/10.7554/eLife.100840.3.sa0)

This paper represents an important contribution to the field. Summarizing results from neural recording experiments in mice across ten labs, the work provides compelling evidence that basic electrophysiology features, single-neuron functional properties, and population-level decoding are fairly reproducible across labs with proper preprocessing. The results and suggestions regarding preprocessing and quality metrics may be of significant interest to investigators carrying out such experiments in their own labs.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.100840.3.sa1](https://doi.org/10.7554/eLife.100840.3.sa1)

The IBL here presents an important paper that aims to assess potential reproducibility issues in rodent electrophysiological recordings across labs and suggests solutions to these. The authors carried out a series of analyses on data collected across 10 laboratories while mice performed the same decision-making task, and provided convincing evidence that basic electrophysiology features, single-neuron functional properties, and population-level decoding were fairly reproducible across labs with proper preprocessing. This well-motivated large-scale collaboration allowed systematic assessment of lab-to-lab reproducibility of electrophysiological data, and the suggestions outlined in the paper for streamlining preprocessing pipelines and quality metrics will provide general guidance for the field, especially with continued effort to benchmark against standard practices (such as manual curation).

The authors have carefully incorporated our suggestions. As a result, the paper now better reflects where reproducibility is affected when using common, simple, and more complex analyses and preprocessing methods, and it is more informative-and more reflective of the field overall. We thank the reviewers for this thorough revision. We have 2 remaining suggestions on text clarification:

(1) Regarding benchmarking the automated metrics to manual curation of units: although we appreciate that a proper comparison may require a lot of effort potentially beyond the scope of the current paper; we do think that explicit discussion regarding this point is needed in the text, to remind the readers (and indeed future generations of electrophysiologists) the pros and cons of different approaches.

In addition to what the authors have currently stated (line 469-470):

"Another significant limitation of the analysis presented here is that we have not been able to assess the extent to which other choices of quality metrics and inclusion criteria might have led to greater or lesser reproducibility."

Maybe also add:

"In particular, a thorough comparison of automated metrics against a careful, large, manually-curated dataset, is an important benchmarking step for future studies.

(2) The authors now include in Figure 3-Figure Supplement 1 that highlight how much probe depth is adjusted by using electrophysiological features such as LFP power to estimate probe and channel depth. This plot is immensely informative for the field, as it implies that there can be substantial variability-sometimes up to 1 mm discrepancy between insertions-in depth estimation based on anatomical DiI track tips alone. Using electrophysiological features in this way for probe depth estimation is currently not standard in the field and has only been made possible with Neuropixels, which span several millimeters. These figures highlight that this should be a critical step in preprocessing pipelines, and the paper provides solid evidence for this.

Currently, this part of the figure is only subtly referenced to in the text. We think it would be helpful to explicitly reference this particular panel with discussions of its implication in the text.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.100840.3.sa2](https://doi.org/10.7554/eLife.100840.3.sa2)

Summary:

The authors sought to evaluate whether analyses of large-scale electrophysiology data obtained from 10 different individual laboratories are reproducible when they use standardized procedures and quality control measures. They were able to reproduce most of their experimental findings across all labs. Despite attempting to target the same brain areas in each recording, variability in electrode targeting was a source of some differences between datasets.

Strengths:

This paper gathered a standardized dataset across 10 labs and performed a host of state-of-the-art analyses on it. Their ability to assess the reproducibility of each analysis across this kind of data is an important contribution to the field.

Comments on revisions:

The authors have addressed almost all of the concerns that I raised in this revised version. The new RIGOR notebook is helpful, as are the new analyses.

This paper attributes much error in probe insertion trajectory planning to the fact that the Allen CCF and standard stereotaxic coordinate systems are not aligned. Consequently, it would be very helpful for the community if this paper could recommend software tools, procedures, or code to do trajectory planning that accounts for this.

I think it would still be helpful for the paper to have some discussion comparing/contrasting the use of the RIGOR framework with existing spike sorting statistics. They mention in their response to reviewers that this is indeed a large space of existing approaches. Most labs performing Neuropixels recordings already do some type of quality control, but these approaches are not standardized. This work is well-positioned to discuss the advantages and disadvantages of these alternative approaches (even briefly) but does not currently do so-it does not need to run any of these competing approaches to helpfully mention ideas for what a reader of the paper should do for quality control with their own data.
