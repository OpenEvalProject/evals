# Peer review - Round 1

Editors:
- Naama Barkai, Weizmann Institute of Science Israel

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.32472.033](https://doi.org/10.7554/eLife.32472.033)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "The genetic landscape of a physical interaction" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by Naama Barkai as the Senior and Reviewing Editor. The following individual involved in review of your submission has agreed to reveal their identity: Jesse D Bloom (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As you will see below, the reviewers greatly appreciated the approach, but were worried about technical details. Please address all of the concerns that were raised. Most important are the concerns regarding sequencing errors, controls, and the use of the same thermodynamic model to two different aspects of the problem.

Here are the comments that I drew out of the reviews that I think should be noted. I also agree with many of the other listed points, but these are the ones that most stand out to me:

1) I agree with reviewer #1 that the authors should justify the cutoff of >10 reads. I don't really have a problem with this cutoff, but some justification would be nice. I strongly agree with #1 that the filtering to require >0 counts in selected library doesn't make any sense. A deleterious mutation would be expected to go to zero. So as #1 says, the authors should either remove this filter or come up with a really good reason why it is justified.

2) Reviewers 2 and 3 both think that it doesn't make sense to apply the same thermodynamic model to cis interactions (which presumably relates to protein stability) and trans interactions (which presumably related to binding affinity).

3) Several noted that the availability of the computer code is clearly inadequate.

4) Several noted any clear description of how they dealt with sequencing error, and the lack of controls to quantify this.

5) I agree with reviewer #2's point that the correlations should be reported in terms of the actual quantity on which inferences are based, which is PPI.

6) I agree with reviewers #1 and #2 that they need to justify the 0.64 / 0.96 / 1.04 cutoffs.

Reviewer #1:

The manuscript "The genetic landscape of a physical interaction by Lehner and Diss presents methods for detecting genetic interactions between combinations of point mutations in two genes encoding physically interacting proteins. The combination of Deep Mutational Scanning (DMS) with a Protein Fragment Complementation assay is innovative. They first define interactions in the usual multiplicative way, and then (most interestingly) present a thermodynamic model which explains a large fraction of the observed interactions (stemming from the idea that function depends non-linearly on folding energy). They then essentially redefine genetic interaction to look for combinatorial effects that are not explained by this null model. The combinatorial library construction method that directly establishes a genetic link between the interacting variants is an elegant experimental design. The paper is well written and provides novel insights into physical underpinnings of genetic interactions.

Despite overall enthusiasm, there are some points that should be addressed:

- The sequencing results were filtered to only consider clones with > 10 reads in the input library. How was this cutoff chosen? A plot of #reads vs. variance of technical replicates might be helpful to show demonstrate the effect of this cutoff. The rule of thumb for counts data is that the standard deviation is the square root of the count, so that a 10-count measurement will have a CV of at least 33%. Is this acceptable?

- The results were also filtered to only consider clones with >0 counts in the selected library. This was a bad idea. The mutational combinations that cause interactions to disappear altogether might correspond to some of the strongest and most interesting negative genetic interactions. Fixing this mistake may or may not have much impact on the results, but this analysis error should be corrected.

- R2 can be a misleading indicator of data quality. In measuring agreement between thermodynamic model and results, it would be useful to examine RMSD for held-out data not used in fitting the model.

- The expression "positive (compensatory)" is used, as though these were synonyms. In genetic interaction studies with sufficient resolution to capture different subtypes of positive interactions (see St Onge et al., Nat Genetics 2007), the bulk of positive interactions have been "masking" or "diminishing returns" interactions, where the first mutation disrupted a process, and the second disruptive mutation could do no further harm because the damage was already done. To be suppressive or compensatory means that not only must the combination of mutations be above multiplicative (or thermodynamic?) expectation, but the combination must cause less harm to the phenotypes than the most harmful of the two mutations. Adding specific separate analyses of masking and suppressive/compensatory positive interactions could greatly improve the impact of this study, and this would not be hard to do.

- It is said that two mutations within Fos are more likely to increase the strength of the PPI than one mutation in Fos combined with a second mutation in Jun. To complete the argument, the authors should also examine whether two mutations within Jun are more likely to increase the strength of the PPI than one mutation in Jun combined with a second mutation in Fos.

- In Figure 4E, the last example (bottom right panel) does not seem to make sense biochemically. While the WT and double mutant both can be expected to have a hydrophobic interaction, the individual single mutants would also be expected to be able to fulfill that role.

- "Sequencing data was filtered using homemade Perl scripts" is hardly a reproducible description, especially given that there is no statement about code availability. The code written for this study (e.g. perl scripts for sequence analysis, R scripts for statistical analyses) would ideally be publicly posted (e.g., at Github) and not simply "available on request".

- Some thresholds used for classifying mutant effects seem to come from nowhere. While the 1.04 threshold is justified in terms of its control of FDR at 0.05, no similar justification is provided for 0.64 or 0.96 thresholds.

- Subsection “Comparisons of the proportion of structural epistasis in cis and trans”. It is not at all clear that using the same P-value threshold allows apples-apples comparison between different libraries of different sizes. Would be better to computationally down-sample the larger of the two libraries.

Reviewer #2:

This paper uses deep mutational scanning (DMS) on two proteins to study the genetic determinants of binding across a protein-protein interaction interface; further, it interprets these observations in a structural context. It is the first study to analyze large-scale epistasis across an interface, so it will be of considerable interest to those interested in sequence-structure-function relationships and the determinants of PPIs. I find the conceptual framework and design to be solid. The experiments appear to have been well executed and the data have been carefully analyzed, so I think the paper is a good candidate for eLife.

A few comments follow. I am mostly concerned that better attention to analysis of error and reproducibility is necessary. I expect that it should be possible to address my comments with a handful of additional statistical analyses and more precise description in the text.

1) Stochastic error in inferring growth rate from frequencies has not been adequate attention. The authors use all sequences with >10 input reads and >0 post-selection reads. Estimates of PPI scores (and, in turn, of epistasis) for genotypes with low read numbers will have considerable stochastic error associated with them, particularly if that error is propagated into products or ratios (as they are for epistatic effects). Although reproducibility may be relatively high overall, the authors should incorporate uncertainty caused by stochastic error into their classifications and quantifications of mutational and epistatic effects.

2) The authors claim that reproducibility is high, and refer to a high rank-order correlation coefficient among replicates. The paper's major inferences, however, are not based on rank-order but on PPI score and statistics derived from it. What matters, then, is the reproducibility of the PPI score. The authors should instead report R2 for PPI among reps and between DMS and small-scale experiment. If the R2 is low, discussion of the implications for the authors' claims will be required.

3) Because the library was created using doped degenerate codons rather than targeted synthesis, there are a great variety of genotypes in the library with different numbers of mutations. Paired-end sequencing is used (rather than bar-coding) to identify genotypes. Sequencing error may lead to mis-identification of genotypes, and this error may be biased towards genotypes with certain numbers of mutations. This concern does not appear to have been addressed. Reporting the degree of sequencing error and showing that it does not strongly affect the claims is necessary.

4) I find the PPI score unintuitive. In theory, it might range asymmetrically around the value of 1 (wildtype) from 0 for a totally deleterious genotype to infinity. This alone bothers me (and could be addressed with a log-scale relative to wildtype). The assay itself puts practical limits on how much a mutant genotype might possibly increase the PPI, because there must be saturation point at which occupancy of the complex, given the dose of methotrexate in the assay, no longer improves fitness. The PPI numbers are therefore somewhat hard to interpret. I would prefer a transform that expresses the PPI on a log scale relative to wild type, rescaled so the intervals between the minimum and wild-type and that between wild-type and maximum are the same. I don't view the authors' method as fatally flawed, and I have no reason to think the conclusions would change if my method were used. I'd like the authors to consider the possibility that such an approach might make the numbers in the paper easier for the reader to interpret.

5) I like the authors' efforts to quantitatively distinguish specific structural epistatic interactions from general thermodynamic epistasis caused by the nonlinear relationship between the proteins' affinity for each other and occupancy of the complex. Although the model has a nice theoretical basis and accounts for a substantial amount of epistasis, there may be additional causes of nonspecific epistasis remaining in the system – for example, if there are nonlinearities in the relationship between occupancy of the jun-fos complex and growth rate. I would therefore like to see the authors explore using Sailer and Harms' Genetics 2017 method, which identifies general epistasis in a way that is more agnostic to the specific biochemical causes or quantitative relationships, to determine if this is the case. If general epistasis can be identified using Sailer's approach even after the thermodynamic model is applied, this would be important, because it would further reduce (and probably sharpen) the cases of specific structural epistasis, and it would be an interesting finding, as well.

6) I have some concern that the thermodynamic correction may affect cis and trans interactions differently. Stated a little too simply, the model is built around the expectation that mutations in trans that additively affect the energy of complex formation will have an exponential effect on occupancy of the complex and therefore on PPI; epistasis not accounted for by this relationship represent specific structural epistasis. It is not apparent to me that the same model appropriately corrects for general thermodynamic nonlinearity among cis- acting mutations. Suppose that two mutations within a protein independently affect the dG of the native structure; they will have an exponential effect on occupancy of the native structure. It is not obvious to me that the model will account for such nonlinear effects on the effective concentration of each molecule. If so, then pairs of cis-mutations that in fact act additively on the protein might be classified as structural specific interactions even after the thermodynamic model is applied. This could contribute to the apparent excess of classified epistasis in cis compared to in trans after removal of thermodynamic epistasis (Figure 5). If I am misinterpreting the model, it would be helpful for the authors to better explain in the main text what the model does and doesn't account for.

7) The authors classify the magnitude of PPI effects as strongly deleterious, weakly deleterious, neutral, and beneficial based on thresholds of 0.64, 0.96, and 1.04. The authors should provide a justification these numbers, which are presented as if they are arbitrary. (They do resemble some relevant numbers from the normal distribution, but the authors should make this explicit and justify their use.)

8) The interface of jun and fos appears as if it might be isologous, such that a mutation in one partner would be expected to have precisely the same structural and functional effect as the same mutation in the other (although this prediction would be compromised by divergence between the paralogs over time). The authors might discuss this, particularly as an explanation for the correlation between the effects of a mutation in one partner and the same mutation in the other. Isology would explain correlation; divergence would explain imperfect correlation.

9) Some bZip proteins, including fos and jun family members, can homodimerize. In the current assay, such events would interfere with growth, assuming that homodimers would compete with the heterodimer for the relevant subunits. Mutations that specifically affect the affinity of homodimerization – including those at the interface – would thus affect PPI, but not through trans-interactions. The authors should consider this possibility and note how it might contribute to their observations.

10) The authors state that combining two mutations that positively affect growth rate leads to positive epistasis and cite Figure 3C. I believe that should be apparent as pies colored mostly green in the upper-right quadrant of the array. I don't see that in the data at all. That quadrant looks mostly yellow, suggesting little epistasis. What I believe is apparent in Figure 3C is that positive epistasis is concentrated in the rows where a weak beneficial mutation plus a deleterious mutation yield an outcome that is less deleterious than expected; this effect goes away when the thermodynamic model is applied (compare 3F). This is worth noting and, I hope, providing an explanation for.

Reviewer #3:

This study uses deep mutational scanning to assess the effects of essentially all single amino-acid mutations to the JUN and FOS proteins. It then uses an interesting strategy to analyze the effects of combinations of mutations to the two.

This is the first deep mutational scanning study to look at both sides of a protein-protein interface. In general, the experiments appear to be well done with adequate replicates – at least I could identify no obvious technical flaws. They also have a nice and detailed Materials and methods section.

The analysis in terms of thermodynamic effects was quite nice, and I like the result about a mix of thermodynamic and structural epistasis.

In general, unless the other reviewers identify significant problems that I have overlooked, I support publication of this paper.

* The only thing that I see lacking experimentally is deep sequencing of the wildtype sequences to estimate the error rate. Right now there is no such estimate of how many of the observed mutations are actually due to library preparation of sequencing errors. This could easily be determined by sequencing wild type.

* The computer code used for the data analysis should be included as a supplementary file and/or a GitHub repository (eLife now allows this).

* In various places (first in the subsection “Determinants of single mutant outcome”), the authors refer to the "identical substitutions" in both proteins. But they never clearly explain what this means. I'm assuming that the proteins are homologous, and they mean the homologous positions? This needs to be described much better.

* Unless I am misunderstanding, the thermodynamic model is in terms of mutational effects on the protein-protein binding. This makes sense for analyzing the trans mutational effects. But for analyzing the cis mutational effects, wouldn't we expect to instead be concerned with ddG values for the stabilities of the individual proteins?
