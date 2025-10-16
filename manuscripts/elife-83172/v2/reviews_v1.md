# Peer review - Round 1

Editors:
- George H Perry, https://ror.org/04p491231 Pennsylvania State University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.83172.sa0](https://doi.org/10.7554/eLife.83172.sa0)

This paper directly estimates the fitness cost of loss-of-function mutations in almost every gene in the human genome, providing an interpretable measure of the severity of mutations. The authors then compare datasets of presumably healthy individuals and individuals affected by severe complex disorders or genetic disorders, finding enrichment of de novo loss-of-function mutations in highly constrained genes among probands alongside other illuminating results. This important study will be useful to researchers interested in interpreting and prioritizing disease-causing mutations and in the process of human evolution. Overall, the approach is elegant and the results are of high quality and compelling.


---

# Peer review - Round 1

Editors:
- George H Perry, https://ror.org/04p491231 Pennsylvania State University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.83172.sa1](https://doi.org/10.7554/eLife.83172.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Relating pathogenic loss-of-function mutations in humans to their evolutionary fitness costs" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by George Perry as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

All reviewers were overall strongly positive about your manuscript (and I concur!). The reviewers described your method as "elegant" in their non-public assessments of the work. There are only a few points of revision that you must address in order for your paper to be accepted for publication in eLife. These are summarized at a high level immediately below, but please see the full reviews for detailed comments to aid you in your revision. Overall, very well done on this work and paper.

1. Provide some quantification of how robust your analysis is to the choice of parameters including priors, mutation rates, and demographic history.

2. Explicitly expand the discussion of your results in the context of experimental organism-based knowledge of haploinsufficiency and the evolutionary genomics of gene dosage effects.

3. Address the two technical questions from Reviewer #3.

Reviewer #1 (Recommendations for the authors):

1) How robust are the results of the demographic model? The authors modify the Schiffels and Durbin model to better match the frequency spectrum but it still doesn't match perfectly. This model also assumes continuous panmictic populations – i.e. it does not take into account admixture or population structure in the history of the sample. While some of these effects may be taken into account by the changes in Ne, I think (but I do not know) that may not capture all the effects. In general, it would be good to have some sense of how the estimates change. I think that in the case of no change in population size, the point estimate of hs is just mu/f, so even just comparing to this would give some idea of how important the demography is.

2) How robust are the results of the choice of prior? The uniform priors on log(s) and h are quite strong statements about your belief about the distribution of effects. The large credible intervals suggest that many genes do not have much posterior information. Would it not make more sense to use priors based on a previous analysis (for example Weghorn et al. (2019))? In any case, I think it is important to know how robust the results are to the priors.

3) How robust are the results of the mutation rate estimates? I'm not totally clear on how these are generated. If I understand correctly, they are trained in part on another dataset of LoF mutations. Is there some circularity there? In particular, if there is some systematic bias in the mutation rate estimates due to variant calling, mapping, or other artefacts would that affect your results? Otherwise, I assume that the random error has a fairly linear effect on your estimates, but it would be good to have a sense of how large that is for different genes – presumably for small genes that are highly constrained, the error in the estimate of mutation rate is systematically larger for example. I don't think it's necessarily needed, but this uncertainty could easily be built into the inference (that is one of the nice things about this approach).

Reviewer #2 (Recommendations for the authors):

This study models the fitness costs of loss-of-function mutations in a large cohort of a human database of 55,855 individuals. The modeling indicates different values for autosomal genes, X-linked genes, and those present in the pseudo-autosomal regions of the X and Y chromosomes. The study details the frequency of de novo mutations in zygotes and examined the relationship to a few specific genetic diseases. The authors have composed a well-written manuscript, have explicitly detailed their assumptions, and have noted caveats to interpretations. The results are a valuable documentation of the effects of loss-of-function mutations in humans.

It is perhaps a matter of taste, but this reviewer suggests that the results could have an even greater impact if they were cast in relation to results from experimental organisms regarding haploinsufficiency and to evolutionary genomics of gene dosage effects.

For example, one of the first compilations of LOF mutations that produce a recognizable haploinsufficient effect on a single phenotype revealed that they were typically some type of regulatory gene using Drosophila as a model (Birchler et al., 2001, Dev. Biol. 234: 275-288). Experimental studies of LOF heterozygotes in yeast that are haploinsufficient suggest an overrepresentation of genes involved with multicomponent complexes (Papp et al., 2003, Nature 424: 194-197; Deutschbauer et al., 2005, Genetics 169: 1915-1925; Castrillo et al., 2007, J. of Biology 6:4; Yoshikawa et al., 2011, Yeast 28: 349-361; Pir et al., 2012, BMC Systems Biol 6:4). In human, haploinsufficient genes have been associated with those that have strong network connectivity (Huang et al., 2010, PLoS Genetics 6:e1001154; Mottes et al., 2021, PLoS Comput. Biol 17: e1009638) and with connections to human diseases (Makino and McLysaght, 2010, PNAS 107: 9270-9274). Reviews of dosage sensitivity in the context across biology provide examples in other taxa and the role of dosage sensitivity on genomic evolution (Birchler and Veitia, 2012, PNAS 109: 14746-14753; Birchler and Veitia, 2021, Cytogenetics and Genome Research 161:10-11). Is it possible to make these connections?

With regard to the X and Y chromosomes, evidence has been presented that dosage-sensitive regulatory genes were retained between the X and Y chromosomes in the evolution of the heteromorphic state of human sex chromosomes (Bellott et al., 2014, Nature 508: 494-499). It would be of interest to know how the authors' results intersect with that observation. Also, it is of interest how these results fit with the conclusions of Pessia et al. (2012, PNAS 109:5346-5391) regarding how dosage-sensitive genes impacted the evolution of the human sex chromosomes.

The question arises of how the authors' results intersect with findings about dosage sensitivity being preferentially associated with regulatory factors and other multi-component interactions. Do these have a stronger effect? Is there a relationship with the degree of network connectivity? Can the fitness projections help understand their behavior over evolutionary time?

Reviewer #3 (Recommendations for the authors):

The method is presented very clearly. I only have two quick technical questions and one (hopefully helpful) suggestion.

1) It seems from the text that h and s have two separate priors and are estimated independently. For rare variants, there is probably power to only estimate their product. Please explain why h and s are treated independently or clarify the text if they are not.

2) Parameter α (male bias) is of significant importance for the analysis of the X chromosome. How is it determined for individual genes (I assume that it is not expected to be 3.5 for every gene)? Could you please clarify?

3) In the deterministic limit and assuming that selection is acting through a disease, the fraction of de novo PTV mutations in patients (out of all PTVs in patients) should be exactly equal selection coefficient. It would be of great interest to compare the population genetics estimates to de novo fractions in the patient population data.
