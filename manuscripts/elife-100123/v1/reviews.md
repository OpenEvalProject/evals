# Peer review - Round 1

Editors:
- Saad Jbabdi, University of Oxford United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.100123.3.sa0](https://doi.org/10.7554/eLife.100123.3.sa0)

This fundamental work has the potential to advance our understanding of brain activity using electrophysiological data, by proposing a completely new approach to reconstructing EEG data that challenges the assumptions typically made in the solutions to Maxwell’s equations. Convincing evidence for the superior spatio-temporal resolution of this method is provided through a number of experiments, including simultaneous FMRI/EEG acquisitions. This work will be of broad interest to neuroscientists and neuroimaging.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.100123.3.sa1](https://doi.org/10.7554/eLife.100123.3.sa1)

I want to reiterate my comment from the first round of reviews: that I am insufficiently familiar with the intricacies of Maxwell's equations to assess the validity of the assumptions and the equations being used by WETCOW. The work ideally needs assessing by someone more versed in that area, especially given the potential impact of this method if valid.

Effort has been made in these revisions to improve explanations of the proposed approach (a lot of new text has been added) and to add new simulations.

However, the authors have still not compared their method on real data with existing standard approaches for reconstructing data from sensor to physical space. Refusing to do so because existing approaches are deemed inappropriate (i.e. they "are solving a different problem") is illogical.

Similarly, refusing to compare their method with existing standard approaches for spatio-temporally describing brain activity, just because existing approaches are deemed inappropriate, is illogical.

For example, the authors say that "it's not even clear what one would compare [between the new method and standard approaches]". How about:

(1) Qualitatively: compare EEG activation maps. I.e. compare what you would report to a researcher about the brain activity found in a standard experimental task dataset (e.g. their gambling task). People simply want to be able to judge, at least qualitatively on the same data, what the most equivalent output would be from the two approaches. Note, both approaches do not need to be done at the same spatial resolution if there are constraints on this for the comparison to be useful.

and

(2) Quantitatively: compare the correlation scores between EEG activation maps and fMRI activation maps

The abstract claims that there is a "direct comparison with standard state-of-the-art EEG analysis in a well-established attention paradigm", but no actual comparison appears to have been completed in the paper.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.100123.3.sa2](https://doi.org/10.7554/eLife.100123.3.sa2)

Summary:

The manuscript claims to present a novel method for direct imaging of electric field networks from EEG data with higher spatiotemporal resolution than even fMRI. Validation of the EEG reconstructions with EEG/FMRI, EEG, and iEEG datasets are presented. Subsequently, reconstructions from a large EEG datasets of subjects performing a gambling task are presented.

Strengths:

If true and convincing, the proposed theoretical framework and reconstruction algorithm can revolutionise the use of EEG source reconstructions.

Weaknesses:

There is very little actual information in the paper about either the forward model or the novel method of reconstruction. Only citations to prior work by the authors are given with absolutely no benchmark comparisons, making the manuscript difficult to read and interpret in isolation to their prior body of work.

Comments on revisions:

This is a major rewrite of the paper. The authors have improved the discourse vastly. There is now a lot of didactics included but they are not always relevant to the paper. The section on Maxwell's equation does a disservice to the literature in prior work in bioelectromagnetism and does not even address the issues raised in classic text books by Plonsey et al. There is no logical "backwardness" in the literature. They are based on the relative values of constants in biological tissues. Several sections of the appendix discuss in terms of weather predictions and could just be written specifically for the problem here. There are reinventions of many standard ideas in terms of physics discourses, like Bayesian theory or PCA etc. I think that the paper remains quite opaque and many of the original criticisms remain, especially as they relate to multimodal datasets. The overall algorithm still remains poorly described. The comparisons to benchmark remain unaddressed and the authors state that they couldn't get Loreta to work and so aborted that. The figures are largely unaltered, although they have added a few more, and do not clearly depict the ideas. Again, no benchmark comparisons are provided to evaluate the results and the performance in comparison to other benchmarks.
