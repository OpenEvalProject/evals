# Peer review - Round 1

Editors:
- Daniel R Matute, https://ror.org/0130frc33 University of North Carolina, Chapel Hill United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.76383.sa0](https://doi.org/10.7554/eLife.76383.sa0)

The paper reports a method to study deviations from Mendelian inheritance in genomic data from gametes. The authors use this method to study the existence of the phenomenon in human sperm data but do not find it. The method will be useful for future studies on segregation distortion, and the findings are an important step for the systematic study of segregation distortion in humans and other organisms.


---

# Peer review - Round 1

Editors:
- Daniel R Matute, https://ror.org/0130frc33 University of North Carolina, Chapel Hill United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.76383.sa1](https://doi.org/10.7554/eLife.76383.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting the paper "Strict adherence to Mendel's First Law across a large sample of human sperm genomes" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by a Senior Editor. The reviewers have opted to remain anonymous.

Comments to the Authors:

Your manuscript was reviewed by three experts in the field and they concurred that the research is important and valuable. In particular, the development of the rhapsodi will be important for future studies. We also appreciated the application to human gamete data. The conclusions of the study largely confirm the results from previous studies and for that reason, we have decided to decline the manuscript. The work will not be considered further for publication by eLife. We hope the extensive comments from the reviewers will be useful.

Reviewer #1 (Recommendations for the authors):

The manuscript reports a new method (rhapsodi) to impute haplotypes in the sequencing of human gametes. The method performs well in simulated data and the authors explore parameter spaces relevant to the research. In particular, the authors evaluate how well the method performs at different genotyping depths and number of gametes. Even with relatively low coverage (~0.1X), the method phases the haplotypes effectively. Next, the authors evaluate the performance of rhapsodi to mis-specification of recombination and genotype error rate. Some simulations show a non-monotonic relationship with coverage which means the method is currently hard-coded for an unidentified source of variation. The authors acknowledge this caveat.

The second part of the manuscript compares the results from rhapsodi with those Hapi, another tool to phase haplotypes in gamete sequencing data and show that rhapsodi method seems superior in terms of computational time, completeness, and accuracy.

The next, and final, part of the manuscript is to analyze the data from the SpermSeq dataset (Bell et al. 2020; ~41K sperm haploid genomes). The authors do several steps of filtering and use the reduced dataset to infer crossover location along the genome (and the results are consistent with those of previous reports). Most importantly, the authors also use the method to infer Transmission Distortion (TD). There are a few sites (e.g., seven linked SNPs in chromosome 2) that show some deviations, but after using a multiple hit correction, there is no single SNP that shows a strong signal of TD. In general the manuscript concludes there is no significant deviations from random segregation along the whole human genome. This is a rigorous study that provides a novel tool for the study of gamete genomes. Nonetheless, the conclusion is not particularly novel. Perhaps if the authors provide more context on how the findings are contextualized in our current understanding of TD in humans, the manuscript would be more appealing. As it stands, the discussion is almost entirely about the method performance. An example of this lack of context comes in paragraphs 1 and 2 of the discussion. I would elaborate on the studies that are 'limited in statistical power'. Paragraph 2 suggest that previous studies were problematic but the authors do not describe the specifics. This segment of the discussion could be expanded for the benefit of the reader.

Reviewer #2 (Recommendations for the authors):

As mentioned briefly in the public review, the method developed in this work is well-motivated, high performing, and clearly explained. The descriptions of both simulations and application of the method to real data are very thorough, and the authors have taken care to reduce potential confounding effects of genotyping error and other data artifacts. The highlighted results regarding human TD are challenging to interpret in the context of various limitations, including an absence of discussion of how the method might perform under strong TD, as well as missing or unclear information about the TD simulations and the source of the samples. While some limitations of the TD analysis are discussed, other important ones are missing. Overall, the paper may be stronger if it focuses on the method rather than the TD analysis and/or incorporates or suggests an additional use case beyond searching for TD.

Major suggestions for improvement:

– Expand simulations of TD beyond 70% overtransmission of one allele, to identify an upper bound for TD beyond which allelic dropout substantially reduces power.

– The methods and Figure 4 – —figure supplement 4 provide only the number of gametes and not the sequencing coverage used for simulations of TD. Include information about coverage for these simulations, and highlight in the figure the range of parameters/conditions represented in the real dataset.

– The authors claim that they have ">80% power to detect even subtle TD." However, the results from the analysis with multiple test correction shown in Figure 4 – —figure supplement 4B show 80% power for a sample size of ~1000 gametes (the smallest sample size in the sperm dataset) at roughly a 0.58 transmission rate (it is challenging to see precisely from the colors in the figure). It would be helpful to provide an exact lower bound for the detection of TD under realistic conditions. A transmission rate of 0.58 is arguably not subtle and is comparable to the rate at which pedigree studies would also be reasonably well powered.

– In several places the authors state that a true positive signature of TD would not be eliminated through stringent filtering due to the persistence of strong LD. One effective way to demonstrate this would be to show that their filtering has not masked large regions of the genome in some donors. What are the longest stretches in which all SNPs have been eliminated through filtering?

– Repetitive regions, particularly centromeres and telomeres, are often involved in TD in other species, yet these would be filtered out as "challenging regions" in this analysis. Is it possible to infer how well these regions might be captured through LD with included SNPs? The section of the Discussion describing cases of TD that might not be captured in this analysis should include this limitation.

– Relatedly, if the marginal signal of TD on chromosome 2 shown in Figure 4 and described in brief on pp. 5 – 6 is at the end of the genotype-able portion of the chromosome, it could represent stronger TD involving telomeric repeats in LD with this region. This possibility could be excluded or discussed.

– It would be helpful for interpreting the results to include more details about the source of the sperm samples, particularly the donors' ancestry and whether the donors were known to have any fertility issues. This would provide useful context for the possibility of population-specific TD in the Discussion, as well as any comparisons to results of earlier studies using other methods.

– The Conclusion could be substantially strengthened by suggesting other potential uses for this method, including but not limited to detection of TD. Which samples would be most interesting to use for subsequent scans of TD? What other uses might this method have in non-TD-related genetic or evolutionary studies?

Reviewer #3 (Recommendations for the authors):

This method for phasing and imputing gamete genotypes requires substantially more benchmarking. Although accuracy is of interest and reasonably well evaluated through simulations, nothing is presented about the computational performance. In particular, given that much larger Sperm-seq datasets must already be in production, it is important to determine if this approach will scale sufficiently for those applications. Runtimes and memory requirements should be reported.

The code is reasonably well documented. However, I am not certain I could reproduce the haplotype phasing approach nor the HMM-based on the description provided in the text. The description should be expanded substantially possibly in a supplemental text section. For instance, in the state transition diagram in Figure 1C, as shown it indicates that the HMM does not transition back from error states. Is that right or am I misunderstanding?

The section, "Power analysis for detecting TD" states that the power across simulations is 80%. Does this account for a multiple testing correction? Both corrected and uncorrected values should be reported.

Two biological factors might be worth some additional clarification. First, what do we know about the ancestry of the donors? E.g., are some individuals admixed? Admixture might be expected to "unmask" cryptic distorter/suppressor pairs. Second, it should be clearly stated in the discussion that this study does not exclude the possibility of rare strong distorters at modest or low frequencies in human populations.

To me, figure 4-S3 is somewhat misleading. Note that this might actually be figure 4-s4 given the caption and references in the text, but on the pdf that page is labelled figure 4-s3. None of the donors considered had more than about 3300 total sperm sampled. After QC, I assume it is less. Yet the X-axis proceeds to 10k. I'd like to see the X-axis pruned back to a reasonable range for these analyses and a line plotted with points for each donor where the experiment would have power to detect TD. I suggest plotting the line at 80% power by convention, but 50% would allow for a more direct comparison to Meyer et al. (2012). This really should be a main text figure, too, since all of the major biological claims in the paper hinge on these analyses it is necessary to explore power in much greater depth.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Adherence to Mendel's First Law across a large sample of human sperm genomes" for further consideration by eLife. Your revised article has been evaluated by Molly Przeworski (Senior Editor) and a Reviewing Editor.

The manuscript was reviewed by two of the original reviewers and two additional ones. Overall, the reviewers agree on the merit of the work. The manuscript has been improved but there are some important remaining issues that must be addressed. In summary, we have three requests and one suggestion.

Essential:

– A comparison to hapcut2 seems to be crucial for benchmarking the method. Since your method has a phasing component, it is important to present a comparison that is adequate given the scale of the dataset.

– The criticisms about pedigree-based studies need to be presented in a more nuanced way. Similarly, the broad statement about the absence of strong TD in humans seems poorly supported. The reviewers all suggested a more balanced presentation of these previous efforts and more of a discussion of how rhapsodi can be integrated in current research.

– The manuscript reads as two disjointed pieces, one on method development and the other on applications. We would ask that the manuscript be revised with this issue in mind, as it persists from the previous submission.

Potentially useful but not essential:

The reviewers list some suggestions, including changing the title, modifying the abstract, and reordering the introduction and discussion.

Reviewer #2 (Recommendations for the authors):

I appreciate the extensive further simulations, analyses, and revisions the authors have provided, particularly the additional simulations under strong TD and the clarified details about their samples, metrics, and computing resources. The suggestions for future uses of rhapsodi are also helpful in communicating the significance of this work. These additions substantially strengthen the manuscript and alleviate many of my initial concerns.

I still feel that statements about generalizing a negative finding in the search for TD within this sample to a broader statement about the absence of strong TD in humans (e.g., line 107 "underscores the fidelity of human male meiosis for ensuring balanced transmission of alleles to the gamete pool"), are somewhat too strong, for the following reasons:

1) All power simulations for rhapsodi-based TD detection are conditional on observing a distorter in heterozygous state within the sample, which would require the distorter not to be very rare (roughly >1.4% allele frequency required for 50% probability that at least one of 25 individuals is heterozygous). Observed distortion alleles in other species are often at very low frequency under an equilibrium model where the distortion is balanced by fitness costs in homozygotes (e.g., SD is found at 1 – 5% frequency per ref #9). Unbalanced distorters would fix or be lost rapidly, and would be unlikely to be detected except in the very brief window at which they are locally at intermediate frequency. The authors note these as caveats in the Discussion, but the need for a relatively common distorter is not described as an issue of power (see discussion of comparison to pedigree-based studies below).

2) I may have missed it, but I did not see mention of the possibility of population-specific TD aside from the discussion about fixed distorters uncovered through admixture. While it is true that there are very few alleles with extreme patterns of frequency differentiation across human populations (lines 620 – 621), this is not highly relevant for whether one should expect distorters to be population-specific. As mentioned above, distortion loci are likely to be rare and/or ephemeral, and either would make them very likely to be population-specific.

3) Some TD systems involve epistasis between alleles at distorter and responder loci, which would further require the responder allele to be observed heterozygous in the sample.

I did not notice this before, but there are statements in both the Introduction (line 63) and Discussion (line 505) about pedigree-based TD scans being underpowered due to the small size of human families. This is a bit misleading because such studies typically combine data across multiple families (as noted by the authors in lines 523 – 524), which reduces their power to detect TD present in any one individual but not to detect TD involving an allele at intermediate frequency that is heterozygous in many parents within the sample. Both pedigree-based and sperm sequencing studies have issues of power due to sample size of individuals that are currently discussed primarily in the context of pedigree-based studies; donor sample size concerns are separated from considerations of power when discussing the sperm sequencing study design.

The statement that "single-gamete sequencing studies… provide equal power for detecting TD involving common and rare alleles" is undermined by the following clause "provided that they are heterozygous in the sampled donor individual." The probability that any of the sampled donor individuals are heterozygous for a distorter depends upon that distorter's frequency in the population, so the study's overall power to detect TD is not equal for common and rare alleles (see point 1 above). For example, in the context of Figure 4—figure supplement 4, 200 informative transmissions out of 1518 trios would imply p(heterozygous) = 0.066 (200/3036, MAF = 0.034). In the Sperm-seq sample of 25 individuals, 18% of such cases would be expected to have no heterozygotes in the sample. As this example demonstrates, the power for the present study is substantially higher than for previous pedigree-based studies, but not as much higher as implied by the power simulations.

It might be worth considering for future work whether power may be gained for detecting TD using rhapsodi by combining data across individuals following haplotype inference.

Reviewer #3 (Recommendations for the authors):

Overall, the manuscript has improved and many of my concerns have been well addressed. In particular, emphasizing the power considerations of this specific approach in the main text was an important addition. I appreciate the authors' correcting inaccuracies in my understanding of their previous work.

I respectfully disagree with the authors' dismissal of several considerations.

First, the paper remains a pretty sharp subdivision of methods vs biology. The methods are really about phasing and recombination detection in sperm-seq data, the biology is about TD. I believe it will be hard for a non-specialist to read this manuscript, though the authors are correct that extremely specialized users --- i.e., those with their own sperm-seq datasets --- may benefit from improved software usability.

Second, a comparison to an approach that is suited to the scale of data used is necessary. If hapcut2 is the only option, it should be applied despite being an "off-label" use. Also, yes, it is somewhat outside of typical hapcut2, but linking the reads bioinformatically is pretty straightforward and reasonable. It bears some similarity to read-backed phasing Certainly if one of this studies' co-authors believed this to be a valid use in previous published work it is reasonable to include as a point of comparison here.

On a related note, in "Benchmarking against existing methods", while the description of previous analysis is accurate, the relevant underlying datasets vary so much from previous works that is it not clear that the same results would hold here. Minimally, some acknowledgement should be added that the results described from previous work are based on a dramatically different dataset than was considered here.

Reviewer #4 (Recommendations for the authors):

The authors describe two main things in this paper:

First is the software package called "rhapsodi". Rhapsodi is an R package which is designed to use sparse whole-genome sequencing data from gametes to phase a sperm donor's haplotypes, impute gamete genotypes and identify meiotic crossover breakpoints.

Second, rhapsodi was used with both simulated data and a published dataset of 41,189 individual sperm cells' sequence. The main biological focus of this second part of the paper involved testing for transmission distortion, of any alleles or broader linkage blocks, for which none is detected. Previous publications, referenced in the manuscript, have suggested that transmission distortion can occur in human populations. The possible causes of the discrepancies in results between the study and previous studies is discussed.

Strengths

In the set of variables assessed, rhapsodi appears to outperform Hapi, which the authors present as the benchmark to meet or exceed for a package focused on efficient, accurate, complete and reliable phasing of haplotypes.

Another strength is that the paper also assesses transmission distortion with particularly large datasets for which no signal is detected. This contrasts from previous studies cited in the manuscript. However, the claims relevant to the analysis of this public dataset appears to be convincing. Further, the authors go on to offer good reasoning, particularly in the Discussion, about how they arrived at these conclusions, what any potential limitations of the approach may be, and how the dataset used differs fundamentally from pedigree-based data i.e. this study investigates transmission rates in gametes and does not consider different stages of fertilisation and subsequent aspects embryonic development.

Weaknesses

The approaches in the paper generally are quite strong. However, the study lacks a positive control for transmission distortion, which is not simulated data. This positive control does not exist in published human datasets to the best of my knowledge. However, outside of the scope of this study, one could consider reanalysing published non-human single-gamete sequencing datasets of which there are a number of studies.

The analyses of meiotic crossovers with non-simulated data are quite light – limited to Figure 5 sup 4 and 5 – compared to the two other features of rhapsodi (phasing and imputation), which feature more extensively. Given that a significant portion of the manuscript presents a re-analysis of the data from Bell et al. 2019 Nature, it be helpful to visually demonstrate the variation in crossover numbers, positioning, interference between the 25 donors, and where possible compare these results to published analyses e.g. Bell et al. and other studies. For example, Figure 5—figure supplement 5 suggests that rhapsodi is much more conservative with calling of crossovers/haplotype transitions than Bjarni et al. and I think that this is worthy of discussion. Particularly because false positive rates of double crossovers can have a large effect on particular study types, such as those concerning crossover interference.

The outputs of this work will be very useful for future researchers; both the rhapsodi software, and the finding that there is no strong transmission distortion signal in these 25 male sperm samples. Rhapsodi is one of a very limited number of user-friendly generalised pieces of software – as opposed to a collection of scripts – for the analysis of sparsely sequenced gametes for haplotype phasing, imputation and meiotic crossover breakpoint analysis. The package should attract significant attention from the potential userbase.

The biological findings of this study – failure to identify transmission distortion in these samples – should be of general interest to geneticists and adjacent fields. Despite being a negative finding, it challenges existing literature with a robust analysis and will be sure to stimulate further research directions.

I found the paper very interesting. I also found the paper to be very well written, clear, accessible to a broad readership, and look forward to using rhapsodi.

Reviewer #5 (Recommendations for the authors):

The authors introduce a new method rhapsodi, which accurately infers haplotypes from low-coverage sequence data of large sample sizes of haploid gametes. They demonstrate that rhapsodi performs better than the existing approach Hapi, particularly for larger samples of gametes. They apply rhapsodi to test for evidence of transmission distortion (TD) in a published human Sperm-seq dataset (single cell sequencing of >30k sperm from 25 donors), and report no significant evidence of TD.

rhapsodi is a powerful approach, which will be useful in a variety of contexts. The TD analysis is more rigorous than previous pedigree-based studies, providing convincing evidence for a lack of strong distorters. However, power to detect weak TD remains limited after accounting for multiple testing. The method is a larger contribution, and likely to be of interest to a broader audience. The manuscript would benefit from re-framing to focus on introducing rhapsodi – with human TD results demonstrating its application.

Recommendations for authors:

The authors have thoroughly and carefully addressed the technical concerns of previous reviewers, and better placed the results in context with previous literature.

However, as noted by previous reviewers, the major strength of the manuscript is the method rather than the human TD analysis. Re-framing the manuscript with focus first on the method would better reflect the relative contribution of the aims, and broaden readership. This could be accomplished without extensive re-writing. For example, I suggest:

– Change title: The title refers only to the TD results – including mention of the method in the title will be more accurate and make it less likely to be overlooked by readers interested in applying the method to other questions. e.g. something like:

New method for analyzing haploid gamete sequences applied to a large sample of human sperm shows adherence to Mendel's first law.

– Re-ordering abstract: to first highlight the need for new method/software to analyse SpermSeq data – ie low-coverage sequencing data from large sample size of gametes. Next highlight TD in humans as an example of a question that can be addressed with SpermSeq data better than previous. [summary of findings] Add at the end more explicit mentions of other applications of rhapsodi (outlined in L653-672 of Discussion)

– Re-order Introduction/beginning of Discussion in similar manner.

Other comments:

L402 "even slight deviations from Mendelian expectations, as supported by our simulations of TD across a range of gamete sample sizes and transmission rates"

– I would consider ~50-55% slight deviations – power is low in this range

– Single noted peak on Chr 2 is 56% for 1571 gametes – but doesn't reach genome-wide significance

– This concern has been addressed somewhat by removing "strict" etc in response to previous reviewers, but could

L491 comparison to Zollner – excess of allele sharing among sibs in pedigree – 50.43% -

this is surviving offspring not gametes so reflects additional sources of TD and selection on embryos/offspring

L621-631 discusses other sources of TD but does not mention this may explain the discrepancy with pedigree based approaches

Could add within-ejaculate sperm competition as factor – reviewed in:

https://royalsocietypublishing.org/doi/full/10.1098/rstb.2020.0066#d1e627

L581 this paragraph makes more sense combined with points in L543-550

Filtering of repeat regions and segmental duplications could remove sites with TD (as noted by the previous reviewer) – in L545 point out the benefits of stringent filtering but doesn't point out that some of these regions could be effected by TD

Methods – in beginning, briefly reiterate the differences compared to methods in the sperm-seq paper (Bell et al. 2020) – it's unclear that the method here is similar but formalised into the package

Figure 4 – Figure supp 1 and Figure 2-supp9 – can't distinguish different colors – make points bigger and/or change shape also according to scale
