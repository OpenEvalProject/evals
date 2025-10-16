# Peer review - Round 1

Editors:
- Joshua T Schiffer, https://ror.org/007ps6h72 Fred Hutchinson Cancer Research Center United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.76487.sa0](https://doi.org/10.7554/eLife.76487.sa0)

Congratulations on this impressive paper which combines clinical biomarker data, patient specific data and viral genetics data to estimate the proportion of HIV infections occurring within key subgroups of the population in Amsterdam. The work is methodologically impressive and also may be of high utility for understanding the spread of HIV and other viral infections through the population.


---

# Peer review - Round 1

Editors:
- Joshua T Schiffer, https://ror.org/007ps6h72 Fred Hutchinson Cancer Research Center United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.76487.sa1](https://doi.org/10.7554/eLife.76487.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for submitting your article "Estimating the potential to prevent locally acquired HIV infections in a UNAIDS Fast–Track City, Amsterdam" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and David Serwadda as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: David A Rasmussen (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

Please clarify certain assumptions about the model regarding the source of local infections, as described mostly by reviewer 2 and a bit by the other 2 reviewers

Reviewer #1 (Recommendations for the authors):

This manuscript describes an analysis of the transmission dynamics of HIV–1 in Amsterdam in the context of a rapid scale–up of prevention measures. Rather than relying on a single source of information, it integrates both virus sequence diversity (by phylogenetic analysis) and statistical modelling to derive estimates of the numbers of unsampled infections and to use clinical biomarkers to estimate dates of infection.

Specifically, the authors reconstructed phylogenetic trees relating large numbers of HIV–1 sequences collected in Amsterdam, outside Amsterdam, and from around the world. The distribution of risk groups and locations was extrapolated by maximum parsimony from the observed sequences at the tips of the tree down towards their common ancestors, and clusters associated with local transmission within Amsterdam were extracted. This process was repeated for 100 replicate trees, which is an important step for accommodating the uncertainty in reconstructing phylogenetic trees.

The authors used a Bayesian method to fit a hierarchical model of the time elapsed between HIV infection and diagnosis ("age" of infection), as predicted by viral load and CD4 measurements, and stratify the model by risk group and location. The resulting estimated dates of infection provide an important context to interpreting the transmission clusters extracted from the phylogenetic trees – many studies have endeavoured to obtain similar information.

The presence of undiagnosed infections that are epidemiologically related to clusters in the study was estimated by fitting a branching process model to the clusters augmented with estimated infection dates. This is a very noteworthy aspect of the analysis, especially because the failure to observe undiagnosed infections is a significant issue that makes it difficult to interpret HIV–1 clusters derived from the comparative analysis of sequence variation. In this case, clusters of recently diagnosed individuals who were infected for a long period of time, as indicated by clinical biomarkers, implies a larger number of unsampled infections related to that particular group.

The authors report that, despite the success of scaling up prevention measures in Amsterdam at limiting the onward transmission of HIV–1, there remains a substantial undiagnosed population associated with a disproportionately greater number of recent infections, and that this largely affects foreign–born men who have sex with men. These methodological advances and unique data resources distinguish this study from an abundant literature on HIV–1 transmission clusters. Most of my comments, provided as recommendations for the authors, about the manuscript concern language and the presentation of results.

– Page 2, "(HIV) is concentrated in metropolitan areas, […] representing 26% of the global HIV burden" – minor point, it would be easier to interpret this statistic if it were accompanied with a rough estimate of what share of the global population is contained in metropolitan areas

– Page 2, is there a URL or reference for the UNAIDS fast–track Cities initiative?

– Page 3, "among infections that are estimated to have occurred since 2014" – is the significance of this cutoff year associated with the fast track initiative? It would be helpful to spell this out for the reader.

– Page 4, I have heard of the Weibull distribution but not the Weibull likelihood – please clarify.

– Page 4, "we used the first available partial HIV–1 polymerase (pol) sequence" – please provide HXB2 nucleotide coordinates

– Page 4, "retrieved from the Los Alamos HIV–1 sequence database" – the LANL database requests authors to provide the URL (https://www.hiv.lanl.gov)

– Page 4, "All sequences were subtyped using Comet and Rega." Please provide version numbers and briefly explain how discordant subtype assignments were resolved between these two algorithms. (I found the explanation in the supplementary material and it's not that much longer – why not explain it in main text?)

– Page 4, did you use a double–precision version of FastTree?

– Page 4, I have a problem with the term "phylogenetic subgraphs". A subgraph is a subset of nodes in the network that is not necessarily a single connected component, whereas the authors are presumably referring to either subtrees (all descendants from an internal node), or subset trees (a contiguous subset of descendants from an internal node). In the HIV molecular epidemiology literature, we would refer to these as subtrees.

– Page 4, "Diagnosed Amsterdam patients in the same subgraph are interpreted as belonging to the same transmission chain" – this interpretation is not very accurate – while individuals in a distinct subtree are more epidemiologically related, they are not necessarily in the same "transmission chain" and it is misleading to make this association. The conventional terminology would be "transmission cluster".

– Page 4, "the estimated state of the root of the subgraph is interpreted as the origin of the transmission chain" – this ancestral state reconstruction is going to be quite uncertain in many cases – was this uncertainty propagated from the replicate bootstrap trees? – it would also be good to emphasize that "origin" refers to location and risk group, and not a single individual

– Figure 1, please check this figure for color accessibility – also the use of thin (low weight) font and narrow lines in the tree may make the figure difficult to read for the vision impaired

– Figure 3, I don't understand why there is so much unused space at the top half of the lower plots – I surmise that the authors intend to preserve the y–axis scales between the top and bottom plots for each of A and B columns, but why not truncate the lower plots? I also think the "zoom in" plots have limited utility and could be moved to supplementary material. Otherwise the plots are a rather effective visualization method.

– Page 12, please provide some details on the branching process model, since it plays an important role in this analysis – although it is well described in supplementary material, it would be helpful to give a little more info in the main text

– Figure 4, for what it's worth, these palettes render well in black and white

– Page 15, "the proportion of undiagnosed individual individuals infected with HIV are" – singular or plural?

– Code availability – this GitHub repository appears to be set to private – please make this available for peer review

– Figures S4–S14 – I'm not a fan of radial layouts for displaying phylogenies with node annotations – also, are these trees rooted? this layout method implies that they are, but I did not see any methodological description for rooting trees. Also, these appear to be vectorized images – it's actually more efficient to use a rasterized format like PNG or TIFF for large annotated trees because you're otherwise storing information about an excessive number of objects to draw.

– Figure S4, what's circulating recombinant form A1? do you mean subtype A1?

– Equation S12, please use or something similar to prevent the MSM and HSX superscripts from being rendered in math mode

– Please explain how the pairs plots (Figures S18, S19) were used to assess convergence of the Hamiltonian Monte Carlo chain samples. The figure legends don't provide any information.

Reviewer #2 (Recommendations for the authors):

While Amsterdam has done a tremendous job identifying and treating HIV infections and a large proportion of the HIV infected population is in care, the authors results highlight that there are often still substantial delays in diagnosis and that as many as 20% of individuals infected between 2014–2018 remained undiagnosed by the end of 2018. These results have important implications for HIV prevention strategies and policy: long–term goals aimed at diagnosing or treating a certain fraction of the overall infected population may need to be reconsidered in a more dynamic context focused on the delays between infection and diagnosis/treatment.

Overall, the study design is strong and the statistical methods used to estimate the time to diagnosis and the proportion of undiagnosed infections are sound.

However, it's not clear to me what assumptions are being made to estimate the proportion of new infections arising locally from individuals living in Amsterdam. It seems there may be several latent assumptions here, namely (1) there are no unobserved transmission events in the transmission chains between individuals living in/outside of Amsterdam (2) sampling more extensively outside of Amsterdam would not break apart the observed transmission chains into a larger number of smaller chains (with more external introductions from outside of Amsterdam). It seems to me these assumptions could bias the estimated proportion of new infections arising locally, and therefore the "preventable fraction", upwards. At the very least I think it would be helpful to be more transparent about the assumptions behind the estimator given in eq. 2.

Pg. 5 "predicted actual transmission chains" – not clear what is meant by this.

Pg. 6 "N_C is the estimated number of transmission chains which emerged between 2014–2018" –– is N_C the estimated number of transmission chains or rather the estimated number of individuals in those transmission chains? It seems like it would need to be the later to make N_C directly comparable to N_I.

Reviewer #3 (Recommendations for the authors):

The paper uses various sources of data to identify when and among whom new HIV transmissions are occurring in Amsterdam. The models use multiple data inputs and the conclusions are of high public health importance. The results appear to be largely supported by the analyses. The multidisciplinary approach could be of use for tracking infectious diseases in other settings.

A few areas of the paper could use clarification as described below

– I am a bit confused by the term upwards bias in time to diagnosis estimates. Please be specific in what is meant by this phrase.

– The data in the 2nd and 3rd to last columns in Table 1 would be easier to digest in a histogram.

– Tables 2 and 3 would also be easier to digest in graphical form.

– Please provide 1–2 sentences summarizing the Bayesian methods in Pantazis et al. in the Methods.

– Please justify the assumption that time to diagnosis did not change substantially over 2010–2019. It seems like that with lower true incidence, in theory a higher proportion of diagnoses could occur during later stages of infection.

– Please more precisely define "uninterrupted state label".

– Why were other subtypes or recombinants excluded?

– The blue and turquoise in Figure 3 are difficult to discriminate.

– Discussion: What is the ECDC model? Please specify.
