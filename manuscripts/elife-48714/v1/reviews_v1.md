# Peer review - Round 1

Editors:
- Alfonso Valencia, Barcelona Supercomputing Center - BSC Spain

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.48714.sa1](https://doi.org/10.7554/eLife.48714.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The paper represents first a new contribution to the methodology to infer selection coefficients associated of mutations, and, second, the application of the methodology to the comparative study of mutations in normal versus cancer sub-clones. The general findings contribute to our understanding of somatic mutations and tumor evolution, as well as to the ongoing discussion on the role of potential cancer-related mutations in normal tissues.

Decision letter after peer review:

Thank you for submitting your article "Measuring the distribution of fitness effects in somatic evolution by combining clonal dynamics with dN/dS ratios" for consideration by eLife. Your article has been reviewed by Patricia Wittkopp as the Senior Editor, a Reviewing Editor, and three reviewers. The following individuals involved in review of your submission have agreed to reveal their identity: Ferran Muinos (Reviewer #1); Jamie Blundell (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The paper deals with the important issue of understanding how selection of quantifying the selective advantage provided by somatic mutations as a key element to understand tumor evolution.

The proposed method infers selection coefficients associated with mutations that expand in normal tissues as well as subclonal mutations in oesophageal and skin data set (Martincorena et al.,) linking dN/dS and clone size and provides a model of somatic evolution in normal tissues, applying it to the and infer selective advantages for specific genetic loci in normal and cancer tissues, effectively linking SFS and dN/dS ratios..

The paper is timely, since a number of intriguing reports have detected somatic evolution (potential positive selection) in normal tissues that should not be pathogenic. It also aligns well with previous publications; bioRxiv 569566; doi: https://doi.org/10.1101/569566

Essential revisions:

The referees and editors truly appreciate the approach and consider it an important contribution to the field. Still, we find that it is important to validate the main hypothesis on the estimation of the selection coefficient on mutations in normal tissues.

We will also ask you to consider if the section on cancer is essential for the paper, as it is it is problematic in terms reproducibility and seems rather a distraction of the main argument.

During the revision, you will have the opportunity to address following issues related with clarifications and additional information. We find particularly important to address the ones related with the importance of different mutations in the same gene and the influence of history, e.g. influence of germline mutations in clonal evolution and the potentially transient nature of fitness gains.

Limited applicability questioning the application to cancer cases.

- The method for inferring selective advantages in tumors has one important limitation which is made very clear in the text: the method is not ready for the commonly available data sets. Remarkably, it is apparent that even in the case of high-quality histopathologically-normal tissue data the method has still limited resolution. I wonder whether this low resolution may compromise some of the conclusions drawn after the analysis.

- It is very reassuring from the modeling perspective that the model and subsequent fitting approach yields consistent results with the simulations when applied to the normal tissue data. However, the validation in tumors is lacking. Simulation analyses only confirm that the implementation of the fitting method correctly reflects the model, regardless of the validity of the model.

- The method heavily resorts to the estimation of mutation frequencies. However, this estimation may be difficult, particularly from tumor data with complex chromosomal architectures.

- In summary, there is not enough data for cancer. It is unclear if the section of application to cancer adds much, given the clear statement that there is not enough subclonal recurrence to say very much.

Different mutations in the same gene

- Although it may not affect the validity of the method, the conceptualization of driver mutation presented in the manuscript may obfuscate the interpretation of the results. It is very likely that any mutation found in a gene subject to high selective pressure confers a selective advantage itself, but for genes under mild positive selection this may not be true, whence not all mutations may be bound to drive. Moreover, different driver mutations may confer distinct selective advantages.

- A challenge in using the skin / esophagus data is that the lack of large numbers of people sampled means data is rather sparse. Our experience looking at the blood makes clear that there is often a wide spectrum of fitness effects even for non-syn mutations within the same gene. This effect is not discussed here. Can the authors present an analysis of say the bottom few genes in Figure 3A to test whether there is evidence that the Δ are the same or whether some of the wide variation could be attributable to a variation of Δ even within the gene? I appreciate the data might not be there for a thorough analysis of this though.

- To easily track all the assumptions implied by the models it would be very beneficial for the manuscript to include sketches of the proofs that formally derive the two main functional forms adopted for the mutation density g. This would make the line of reasoning much more transparent and spare the reader the time for literature scrapping.

- Although from the text it seems that the variants implied under the term "mutation" are just coding SNVs, the analysis may well be valid for other types of mutations such as small insertions and deletions or splicing affecting SNVs, as the dN/dS method of choice is equipped to handle them. Please, clarify. Moreover, dNdScv is dependent on the choice of a transcript for the genes analyzed: this choice should be pointed out somewhere in the manuscript.

- The method heavily resorts to the availability of a sufficiently robust method to estimate dN/dS at genetic loci from mutational data. Thus, all the caveats of the method of choice may propagate downstream onto the method described, it is good that these limitations are discussed in the text.

- Motivated by (Introduction) "Enumeration of the selective advantage of each driver mutation enables prediction of future evolutionary dynamics". This claim is more difficult to interpret in the light of your own findings, namely, that there are somatic mutations showing a very significant fitness gain in normal tissues. Consider that those mutations may confer a transient fitness gain until a new homeostatic equilibrium is attained.

- How are the step-sizes of the clone size intervals decided? How coarse these bins can be while still rendering a meaningful fit for the selective coefficients?

- The Discussion section is mainly descriptive and methodological. What can be concluded about the role of NOTCH1 and TP53 in aging and/or tumor initiation in the light of the results in normal tissues?

- The methods are essentially the same (e.g. Equation 4 in this work is Equation 1 in Watson et al., except Watson et al., focusses on SFS view whereas Williams et al. focus on the frequency-dependent dN/dS view – though, as the authors know well, these are different ways of viewing exactly the same info!). It should be made very clear that this has been independently developed by Watson et al. This is especially true since the way Watson et al., is cited at the moment is wholly incorrect!

- Internal consistency between syn and non-syn mutations and validating N. The framework presented here, at its heart, analyses the SFS of two classes of mutations (syn vs non-syn) and takes the ratio of these in bins of increasing frequency. However, taking the ratio of the SFS for these classes of mutation throws away important information and means the authors lose the ability to validate N. If instead of taking the ratios they simply plot the SFS for both the syn and nonsyn variants independently then the amplitude of these curves at low frequency will be given by Nμ, which given one can estimate μ enables one to calculate N, which serves as an important validation since you can check agreement with known estimates of 5000/mm2 (as quoted in the text). I would strongly suggest plotting the SFS of each class of mutation independently as outlined in Watson et al., since this does not throw out the N dependence. Furthermore, this inference of N from the amplitude provides an important internal consistency check on characteristic frequency of the clones (what the authors term N(t) in their main text – although as outlined at the end of my review there is a minor error in their equation). The value of N enables one to predict where the synonynous variants should appear as outlined in (Watson et al. bioRxiv 569566; doi: https://doi.org/10.1101/569566). This analysis would greatly strengthen this work as it would challenge the model more substantially.

- Validation of Δ. One major flaw of the work as presented is that the inferences for Δ are not validated or challenged. One approach we found useful is that the Δ make clear predictions for how the SFS should evolve with age. Even though there is no longitudinal sampling, there is a very wide range of ages in the esophagus data and reasonably wide range in the skin data. The authors should check whether the Δ inferred is consistent with how the SFS changes with age. i.e there should be a wider spectrum of frequencies in the older people and a narrower spectrum in younger people. In fact, the characteristic frequency of the clones should increase exponentially with age since the N(t) (characteristic size of the extant non-syn clones) increases exponentially with age so this makes a clear prediction to be checked. Including this analysis would strengthen the manuscript considerably.

- Spatial effects. A challenge with using data from skin and esophagus to check this theoretical framework is that these tissues evolve on a 2D spatially constrained sheet of cells. There was no development or real discussion of how this might affect the theory (which has no explicit spatial effects built in). While a full theoretical treatment of this does seem beyond the scope of this work, it would be nice to see a thorough discussion of it, especially relating to some of the findings in the recent literature e.g. Hall et al., bioRxiv 480756; doi: https://doi.org/10.1101/480756 and Fusco et al., 2016, neither of which were cited.

- High frequency synonymous variants are likely to be genetic hitchhikers. While there was a short discussion of hitchhikers at the end, it was somewhat cursory and not quantitative. Given the theory, the authors can predict what fraction of syn variants are expected to be hitchhikers in the skin / esophagus data and their frequency distribution (this analysis has been performed in Supplementary note 7 of Watson et al., 2019). It would be an important check on the inferences to perform a similar analysis and see if there is agreement with predictions.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Measuring the distribution of fitness effects in somatic evolution by combining clonal dynamics with dN/dS ratios" for further consideration by eLife. Your revised article has been evaluated by Patricia Wittkopp (Senior Editor), a Reviewing Editor, and the original reviewers.

The manuscript has been improved but the two referees still have a number of points that require additional clarification or a better explanation. The one that I find compulsory is a better description of Figure 5, as detailed by the second referee.

Reviewer #1:

- From this reviewer's perspective, the main concerns raised during the first round of reviews have been addressed. The authors have conceded to reshape the paper so as to exclude the cancer part in the interest of applicability and reproducibility.

- The authors have thoroughly addressed all the comments including additional explanations and new figures for the sake of completeness and clarification. In particular, the authors have now conducted a supplementary analysis of the impact of the dN/dS calculation method of choice; have completed the methodological description; have added clarification to the relationship between predictiveness and selective regime; have completed the discussion hypothesizing a temporal dynamics for the expansion of NOTCH1 vs TP53 variants in histopathologically normal oesophageal tissue; have tackled the relevance and limitations of the study regarding the per-site inference of selective advantages; have clarified the impact of bin-sizes at model fitting; and have carried an important new analysis suggested by one of the reviewers to validate Δ.

- The manuscript has clearly improved and feels to have reached a point so that exposure to public scientific debate cannot wait anymore.

Reviewer #2:

Generally I find the manuscript improved relative to the first draft. However there remain a few issues that I believe need to be addressed to really demonstrate whether the numbers inferred using this method are meaningful.

I am glad to see the suggestion made in my first review on ways to challenge the inferred Δ was used by the authors as the basis for the substantial new analysis resulting in Figure 5. I believe the additional analysis strengthens the manuscript. Given that the idea for this analysis comes from an analysis performed in Watson et al., it would be appropriate to clearly acknowledge this in the main text e.g. words to the effect of "Following closely the analysis laid out in Watson et al. we reasoned…" subsection “Site frequency spectra”.

I also have a few questions about this current analysis. First, as mentioned by the authors, the theoretical prediction is that N(t) should increase exponentially with age with the gradient being approximately Δ. In Figure 5D it is not clear to me what data has been used for this plot and how numbers were estimated. If this data is grouped across many genes the predicted increase should not be exponential at all, so it is not clear if this fit is appropriate. The authors need to clarify this. It is more appropriate to perform the analysis on a gene-by-gene basis as shown in Figure 5—figure supplement 1 but this figure highlights that the agreement between the values of Δ using the two methods are not very good (e.g. TP53 is inferred to be ~0.018 on basis of age change vs 0.06 on basis of dN/dS). The log scale on Figure 5—figure supplement 1B obfuscates this. Is the correlation between the methods still significant on a (more standard) linear scale? The y-axis scale on Figure 5C is incorrect: there is a missing factor of rλ (see below too). Generally I think this new analysis is encouraging but would benefit from a more cautionary telling: highlighting how the agreement between inferred values of Δ is far from perfect and might point to more complex dynamics e.g. environmental effects which alter Δ.

There remains an error in Equation. 4. The units are not correct. The density is dimensionless while at present it is proportional to mutation rate (units of 1/time). There is a timescale missing from the expression: which I believe is r \λ and should be in the denominator. The authors should check this.

I am still not convinced the authors have satisfactorily addressed the issue of sites within a gene having different Δ values. While I accept that the current data sets do not have the power to resolve Δ on a site by site basis they can, and in my opinion should, simulate this with some parameterised distribution and test what value of Δ they would infer using their grouped method. Because, if there is a range of Δ for mutations within the same gene, and a single value is inferred, it is not clear that the value inferred represents the average value of Δ across the gene as the authors claim in their rebuttal. This claim should be backed up with simulations if the data do not exist.
