# Peer review - Round 1

Editors:
- Armita Nourmohammad, University of Washington United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.55308.sa1](https://doi.org/10.7554/eLife.55308.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

The manuscript presents a new approach, Reg-Seq, to study regulatory logic in hundreds of promoters at a time. To do so, the authors use massively parallel reporter assays and mass spectroscopy and build an information theoretical model to characterize binding energies in regulatory promoters at the base-pair resolution level. This approach can significantly advance our understanding of gene regulation in microbes and opens new avenues towards genome-wide quantification of regulatory logic and discovery of new transcription factors.

Decision letter after peer review:

Thank you for submitting your article "Deciphering the regulatory genome of Escherichia coli, one hundred promoters at a time" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Naama Barkai as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Tamar Friedlander (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Comments:

This manuscript introduces a new method "Reg-Seq" for identifying regulatory sites in promoters using RNA sequencing for cell sorting. The method generates impressive quantitative data for many genes in E. coli, which corroborates many previous results and starts to give us hints about the overall trends of regulatory architectures in E. coli. Although the experimental set up is very compelling and potentially promising, there are still some major concerns regarding presentation of the data and the underlying methods and analyses, which we would like to see addressed.

The main concerns about the manuscript can be summarized as: 1) Experimental method should be better discussed in the main text, its limitations should be explicitly pointed out and its advantages should be compared more clearly against previous techniques. 2) Statistical methods (including inference based on mutual information profiles) should be described more clearly and with more quantitative details throughout the text and the significance of the conclusions should be more explicitly expressed. 3) Analysis of E. coli data, comparison with previously identified regulatory regions and binding sites and the significance of these findings should be better discussed.

The reviewers strongly believe that the manuscript should be reworked to focus less on cherry-picked examples and more on presenting the method. The manuscript needs a significant rearrangement to better explain the procedures applied and fill in various missing points as detailed below.

Essential revisions:

1) The approach based on the mutual information profile to identify the binding sites within a promoter and to classify them as activator or repressors should be better explained:

1.1) Since this is such a key step, the authors need to provide more details about how the manual choice of activator/ repressors works. Overall, it is unclear how one goes from mutual information profiles to deciding whether known sites are or are not identified, how to decide which regions are putative sites, whether they fit known motifs, whether they are RNAP sites, and how to construct an energy matrix for each putative site.

1.2) It is mentioned (subsection “Analysis of sequencing results”, first paragraph) that, to confirm these manual choices, authors computationally identify regions of activators / repressors by assessing the fold change in gene expression due to mutations. It is unclear how the authors are assessing the significance of the changes, i.e., what the underlying null model is. If this computational approach is statistically sound, why the need for the manual approach? These manual choices are worrisome and raise concerns about the feasibility to scale-up this method, as intended by the authors.

2) It is difficult to assess the false positive/negative rate of identifying binding sites: This is partly due to the lack of clarity about the authors' approach in deciding whether a known site was identified or not, partly because the annotation of known sites is unclear and incomplete, and partly because the statistics are not transparently reported in the manuscript. It is therefore important that the authors present an objective method for assessing what fraction of known sites is not recovered, for what fraction of predicted novel sites a motif can be made, and for what fraction of those the mass-spec successfully recovers a binding TF.

As a suggestion: The authors should start from a unambiguously defined set of sites (e.g. from RegulonDB and EcoCyc) and then have an unambiguous procedure for:

i) Calling segments where a site exists (for example based on the summed mutual information within the segment).

ii) Calling the motif by comparing the profile with PSWMs or energy matrices for known motifs.

After that, they should clearly report what fractions of sites are recovered and for what fraction of sites the correct motif is predicted.

3) Energy matrices:

3.1) How are the energy matrices constructed? Details are missing from the manuscript.

3.2) How are the p-values estimated to assign significance to energy parameters? It appears that the authors have used MCMC to sample from a likelihood function but the details are very vague. To define an energy, it is assumed that the average expression can be written as the negative exponential of some effective energy to parametrize the average effects of mutations on expression- this should be better justified in the text. However, it seems that instead of 4 different energy parameters at each position, the model only assumes a “mutant” and a “wild type” energy. This may not be a good approximation given that we know nucleotides within TF binding sites have highly varying degeneracies. Moreover, the likelihood function for the observed DNA and RNA reads should be expressed as a function of the energy parameters at all positions. However, this is not the approach taken by the authors and instead, equations (8) and (9) only look at single positions. So, it is not clear what kind of likelihood function the MCMC is sampling from, or how p-values and confidence intervals are determined. Also, if the authors are indeed using MCMC with some likelihood function to sample the space of possible parameter values, the resulting variation in the energy parameters should correspond to posterior probability intervals and not confidence intervals.

3.3) Could the authors present the accuracy of the inferred energy matrices as a function of the number of genomic variants used? A particular example is currently given in Appendix 3. Can the authors use a simulation for that purpose? This is required to understand the validity of the results and the ability to scale-up such an experiment (if for example a lower resolution is sufficient, can larger regulatory regions be analyzed in future experiments?)

4) The step for assigning regulatory logic to promoters is unclear. Do authors always assume OR-gate-like interactions between the TFs, which is what Equation 14 suggests? If so, what is the justification for that assumption? Is it just the most basic statistical mechanical assumption, or is there strong empirical support?

5) The description of the method and analysis is hard to follow and unclear about many assumptions and limitations. To give a few examples:

5.1) Appendix 3 outlines how to calculate the mutual information footprint from the read count data but a more explicit discussion would be helpful: For example, how should the quantities in Equation 5 (p(m, 𝜇), p(m), p(𝜇)) be calculate from the preceding example data (subsection “Information footprints”)?

5.2) The methods rely on both DNA and RNA sequencing of the same sample and using ratios of RNA/DNA reads from the same reporter to estimate expression. The description of the sequencing protocol is insufficient. Importantly, the DNA sequencing is not even mentioned in the methods and it is not explained how precisely this expression quantification is done.

5.3) The methods mention correcting for correlated mutations, MCMC to assign p-values, and energy matrix reconstruction, but it is completely unclear how either of these are done.

6) The discussion of the methods in the main text is mostly qualitative and crucial details are scattered throughout the manuscript, in the appendices and in Materials and methods.

6.1) For example, it requires digging into the appendices to understand that the authors study a region of 160 bp mostly upstream TSS, and so, is this method inadequate if the regulatory region is larger or if its location is unknown? A clear and concise explanation of the crucial details (e.g. size of the region, number of variants per promoter, etc) should be given in the main text.

6.2) To further clarify the methods, it would be helpful to include a picture of the reporter construct, which based on the descriptions includes:

-promoter including 45 bp downstream of annotated TSS.

-then 64bp with primers for plasmid construction

-then 11bp with stop codons in 3 frames.

-then barcodes?

-then a RBS

-then GFP mRNA

7) Authors used TSS information to decide which promoters to pursue. How limiting is this for scaling up the procedure? It would be helpful to discuss briefly what fraction of promoters in E. coli have good TSS information and how valid is to assume that at the genome-wide level, each operon is dominated by a single TSS?

8) The authors rely on expression from plasmids and use mRNA/DNA ratio to handle the effect of variability in plasmid copy number between cells. However, if the plasmid copy number is of a similar order of magnitude as the transcription factor copy number, then the expression level measured (to calculate the energy matrices) is determined not only by the binding energy, but also by the TF availability leading to under-estimation of the binding energies. The authors should comment on this in the manuscript, and if they have the data available, show the measurements for plasmid and TF copy numbers to address this point. At this point we do not see a necessity for additional experiments.

9) The limitations of the method should be more concisely explained. Currently, limitations are scattered throughout the text.

Revisions required for Figures and Tables:

Figure 1: This figure is hard to read. It is difficult to distinguish the individual tick marks around the genome, because there are too many, they are too densely packed, and the colors are too mixed. Also, the caption describes the color of some ticks as "red," but in the printed figure they look more brown (They appeared closer to red on the screen.)

Figure 2: You might want to clarify that the blue region likely corresponds to the σ factor binding site.

Figure 3: The number of (0,0) promoters should be shown as well. Moreover, it seems that the counts in Figure 3 add up to about 50 and the text mentions that there are 32 promoters with no sites found, i.e. type (0,0). Adding this in the sum still seems much less than 113 (i.e., the total number of promoters as indicated in the manuscript). Related to this, it seems that Table 2 has clearly less than 113 promoters in it. Where are the remaining ones?

Figure 4: The authors state about the results in Figure 4: "In each of the cases shown in the figure, prior to the work presented here, these promoters had no regulatory information in relevant databases such as EcoCyc (Keseler et al., 2016) and RegulonDB (Santos- 318 Zavaleta et al., 2019)."

This is simply not true. If you check EcoCyc for these genes you find:

i) idnK regulated by CRP, IdnR and GtnR.

ii) leuABCD regulated by LeuO, slyA, LrhA, and RcsB-BgU.

iii) maoP regulated by hdfR.

iv) rspA regulated by CRP and YdfH.

Only for yjjJ, aphA, and ybjX nothing was previously reported. It should also be noted that except for the rspA promoter, the previously reported regulatory interactions were generally not identified by the method.

Finally, it seems that there is no mass-spec data for yjjJ. Is the identification of marA as the regulator based on motif matching then?

Table 2: This table is unclear. Does the "architecture" of a promoter (first column) correspond to what is inferred in this study, to what is known in the literature, or to a combination of both? For the newly found sites it should be listed whether the binding TF was identified and (if so) what it is. For the fourth column, “literature binding sites”, it is not clear whether this is the total number of known literature sites or only the number of known sites that were successfully identified here – both should be listed. It is not clear what the fifth column “identified binding sites” refers to. The evidence column is also unclear. Is this evidence for the newly found sites or the literature sites?

Just to illustrate the confusion: consider the well-known lac operon. In Table 2 the lac operon (called lac as opposed to lacZYA, which is used elsewhere in the manuscript) is reported to have only 1 known literature site, whereas it is well established that it has a site for CRP and multiple sites for LacI. In the final column it is claimed that there is mass-spec evidence for LacI binding. However, on the website, the lac operon does not occur at all and in Appendix 2—figure 1 only the CRP site is reported. What makes this all even more confusing is that none of the experimental conditions included lactose or another inducer of the operon. As such, the lac operon should be highly repressed and so we expect very little effect of mutating the CRP site, and strong effects of abolishing the LacI site.

In multiple cases in the table, less literature information is reported than it actually exists: e.g. tar is a reported target of FNR, uvrD is a reported target of lexA, cra is a reported target of PhoB, and so on. The authors should make clear what literature information is shown here.

The authors should clear up this information so as to make it unambiguous and consistent across tables, figures, and website.
