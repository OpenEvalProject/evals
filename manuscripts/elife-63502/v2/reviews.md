# Peer review - Round 1

Editors:
- Sandeep Krishna, National Centre for Biological Sciences‐Tata Institute of Fundamental Research India

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.63502.sa1](https://doi.org/10.7554/eLife.63502.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This paper uses high throughput longitudinal TCR sequencing to understand the TCR dynamics in two persons infected with SARS-CoV-2. In particular, they find two peaks of T cell clonal expansion at 15 and 37 days post infection. The authors also identify TCR sequence motifs that are likely to be specific to SARS-CoV-2 and thereby show that some T cell clones are present pre-infection suggesting the existence of cross-reactive memory T cells prior to the infection.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting your work entitled "Longitudinal TCR repertoire profiling reveals the dynamics of T cell memory formation after mild COVID-19" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Phil Bradley (Reviewer #2).

Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife.

While we found the questions raised in this study interesting, we concluded that the manuscript would not be suitable for eLife without substantially more evidence that the clonotypes have TCR specificity for SARS-CoV-2. The individual reviews are appended below.

Reviewer #1:

This work investigates the T cell receptor (TCR) repertoires of 2 individuals diagnosed with mild COVID-19 infection. The authors use high-throughput sequencing of 2 biological replicate samples obtained at each of multiple pre-infection and post-infection timepoints to identify TCRalpha and TCRbeta clonotypes that contract or expand post-infection and to investigate potential reactivation of pre-existing memory cells. This is a potentially interesting work that may provide novel insights into T cell responses to SARS-CoV-2. However, some of the specific details of the various analyses reported are not clear and I have several major concerns about the reported work.

1) The primary concern is the TCR specificity of the clonotypes that were determined to be contracting or expanding post-SARS-CoV-2-infection and therefore identified as responding to or reactive to SARS-CoV-2. There is no verification that these expanding or contracting clonotypes have TCR specificity for SARS-CoV-2. One alternative possibility is that some, maybe even many, of these expanding or contracting clonotypes are bystander-activated T cells with TCRs that are not specific for SARS-CoV-2. Similarly, the clonotypes that were identified as contracting or expanding post-SARS-CoV-2 infection and also detected in the memory pool prior to SARS-CoV-2 infection may not be cross-reactive (i.e. specificity for another infection + SARS-CoV-2), as suggested by the authors, but rather non-SARS-CoV-2-specific bystander-activated memory T cells.

While the dynamics of the T cell populations following SARS-CoV-2 infection may be informative regardless of the mode of activation of the T cells (i.e. TCR-mediated vs. bystander activated), the reported TCR clonotype motifs are only informative if these TCRs have SARS-CoV-2 specificity.

2) Another concern is the substantial variation between the various approaches used to identify the contracting and expanding clonotypes post-infection that are associated with COVID-19 infection. The manuscript text states that the EdgeR and NoiseET approaches for identifying expanding and contracting clonotypes yielded similar results. Figure 1—figure supplement 4A, D suggest that the two approaches yield similar trajectories for the identified expanding and contracting clonotype subsets (i.e. fraction of reactive clonotypes). However, the Venn diagrams in Figure 1—figure supplement 4B, C, E, F show that the two approaches are, in some cases, identifying substantially different subsets of expanding or contracting clonotypes. For example, for Donor M in Figure 1—figure supplement 4F, of the 1044 expanded clonotypes identified by NoiseET, only 478 were also identified by EdgeR.

The text also states that the contracting and expanding clonotypes identified using EdgeR largely overlap/correspond to the clusters 2 and 3 of clonal trajectories yielded using PCA (Figure 1B-E) but no quantitative evidence is provided to support this. Venn diagrams, similar to those in Figure 1—figure supplement 4, could be provided that compare the expanding and contracting clonotypes identified using the three different approaches (i.e. EdgeR, NoiseET, and PCA) as applied to TCRα as well as TCRβ clonotypes.

While these differences between methods may not have significant consequences for some of the reported results (eg. temporal clonal trajectories), these differences raise concerns about the results that depend on specific clonotype sequences (eg. Figure 2D-G, Figure 3—figure supplement 2 and Figure S5D-G that report amino acid motifs for contracting and expanding clonotypes).

Reviewer #2:

This manuscript describes a longitudinal study of TCR repertoires in two individuals with mild COVID-19. TCRα and β repertoires at 4 time points post-infection are used to identify T cell clonotypes likely responding to COVID-19. These responding clones fall into two groups, a set of monotonically contracting clones and a set of clones whose frequencies peak (at day ~37) and then contract. Sequencing of memory populations at two time points and availability of TCR repertoire data from both individuals prior to infection allow the authors to map clonotypes to memory phenotypes and to identify a handful of responding clones that existed in the memory compartment prior to infection. Clusters of sequence-similar clonotypes are identified that suggest focused responses to immunodominant epitopes. This is a succinct and timely study and I have no major concerns, just a few questions/suggestions/typos detailed below.

How unexpected is the TCR clustering evident in Figure 2D-G? For example if the same number of equally high Pgen sequences were selected at random? I wonder whether the authors could run ALICE on just the responding clones (not the full dataset) to assess which neighborhoods are very unlikely to occur by chance.

Could the "computational chain pairing" method of Minervina et al. be applied to this data? If only to try to connect some of the sequence motifs between the α and β chains?

Reviewer #3:

This is a case report analysing TCR repertoire on two individuals with suspected COVID-19 infection. The report shows that a set of TCR sequences expands between days 15 and day 30/37 and another set contract. The amount of expansion/contraction is not clearly shown. Most of these sequences are found in the memory phenotype. A few (especially CD4) are found before immunisation. As the authors point out, the evidence that the TCRs recognise COVID-19 is purely circumstantial. Even if they do, I do not see that this study contributes significantly to understanding either the protective or the pathological immune response to COVID-19.

1) The Abstract is full of unsubstantiated claims. For example "T cell response is a critical part of both individual and herd immunity to SARS-CoV-2 and the eﬃcacy of developed vaccines. " Or "In both donors we identiﬁed SARS-CoV-2-responding CD4+ and CD8+ T cell clones. We describe characteristic motifs in TCR sequences of COVID- 19-reactive clones, suggesting the existence of immunodominant epitopes." The authors do not identify COVID-19 responding clones; nor do they show any evidence that there are immunodominant epitopes.

2) Figure 1 What does "normalized trajectory of TCR clones in each cluster" mean ? It would be interesting to see the magnitude of the responses. Similarly, I don't really understand the y axis in panels d and e.

3) Figure 3. I don't understand panels a and b. Is this the proportion of contracting TCR sequences which are memory phenotype? If so, what are the rest ? Or are they simply not captured. The figure legend is obscure.
