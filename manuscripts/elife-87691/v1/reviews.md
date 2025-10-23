# Peer review - Round 1

Editors:
- Inna Slutsky

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.87691.2.sa0](https://doi.org/10.7554/eLife.87691.2.sa0)

This valuable study combines chronic widefield calcium imaging of dorsal cortex activity at the mesoscale level with electrical recording of single neurons in specific cortical and subcortical locations. This work provides compelling evidence for recording neuronal activity at multiple temporal and spatial scales by combination of optical and electrophysiological methods. This work will be of broad interest to system neuroscientists studying neural circuits.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.87691.2.sa1](https://doi.org/10.7554/eLife.87691.2.sa1)

The paper by Dongsheng Xiao, Yuhao Yan and Timothy H Murphy presents a timely approach to record neuronal activity at multiple temporal and spatial scales. Such approaches are at the forefront of system neuroscience and a few examples include, among others, fMRI alongside electrophysiology (Logothetis et al, 2021. Nature) or widefield calcium imaging (Lake et al, 2020. Nat Meth) , or functional ultrasound imaging and multi unit recording (Claron et al, 2023 Cell Reports), The method presented here combines "low resolution" (i.e. cortical regions) widefield calcium imaging across most of the dorsal portions of the murine cortex combined with electrical recording of single neurons in specific cortical and subcortical locations (as a matter of fact, this later components can be used everywhere in the murine brain).

The method presented here is straightforward to implement and very well documented. Examples of novel insights that this approach can generate are well presented and demonstrate the strength of the presented approach, some aspects of the analysis require clarification.

For example, the author reveal Spike-Triggered average cortical activation Maps (STMs) linked to the activity of single neurons (Figs 4 and 5) This allows to directly asses the functional connectivity between cortical and sub-cortical areas. It nevertheless unclear what is the stability of the established relationships. The nature of the "recordings" in Fig 4. is unclear. It looks like these are imaging sessions on the same day, the length of these recordings as well as the interval between them is not stated. It will be fundamental to build a metric to compare STMs variability across sessions/recordings/days; a root-mean-square from an average map across all recordings could provide a starting point.

Also with respect to the STMs analysis, the data-driven choice of 10 clusters might need a bit more explorations. While the silhouette clustering accuracy peaks at 10 (Fig 5A), this metrics comes without a confidence intervals making it difficult to know if a difference of less than 10% (i.e. 11 or 13 clusters) should be deemed different. Maybe a bootstrapping approach could be used here to build such confidence intervals. Another approach to reach the number of cluster to use could be based on "consensus" between different partitioning algorithms (e.g. Strehl, A. & Ghosh, J. itions. J. Mach. Learn. Res. 3, 583-617 [2001]). A much stronger argument should be provided to use the 0.3 correlation cutoff value which seems to be arbitrarily low. The main point here is that the authors should show that their conclusions hold within a range of parameter values (number of clusters and correlation threshold).


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.87691.2.sa2](https://doi.org/10.7554/eLife.87691.2.sa2)

The article presents 'Mesotrode,' a technique that integrates chronic widefield calcium imaging and electrophysiology recordings using tetrodes in head-fixed mice. This approach allows recording the activity of a few single neurons in multiple cortical/subcortical structures, in which the tetrodes are implanted, in combination with widefield imaging of dorsal cortex activity on the mesoscale level, albeit without cellular resolution. The authors claim that Mesotrode can be used to sample different combinations of cortico-subcortical networks over prolonged periods of time, up to 60 days post-implantation. The results demonstrate that the activity of neurons recorded from distinct cortical and subcortical structures are coupled to diverse but segregated cortical functional maps, suggesting that neurons of different origins participate in distinct cortico-subcortical pathways. The study also extends the capability of Mesotrode by conducting electrophysiological recordings from the facial motor nerve. It demonstrates that facial nerve spiking is functionally associated with several cortical areas( PTA, RSP, and M2), and optogenetic inhibition of the PTA area significantly reduced the facial movement of the mice.

Studying the relationship between widefield cortical activity patterns and the activity of individual neurons in cortical and subcortical areas is very important, and Murphy's lab has been a pioneer in the field. However, the choice of low-yield recording methods (tetrode) instead of more high-yield recording techniques, such as silicon probes, makes the approach presented in this study somewhat less appealing. Also, the authors claim that a tetrode-based approach can allow chronic recordings of single neural activity over days - a topic that is very controversial. In terms of results, I was under the impression that most of the conclusions presented in the bulk of the paper ( Figures 1-5) are very similar to what previous work from Murphy's lab and other labs has shown using acute preparation. In this respect, the paper can benefit from a more in-depth analysis of the heterogeneity of single-neuron functional coupling. The last part of the facial nerve recording is interesting (Figure 6), but I think it can be integrated better into the rest of the paper.
