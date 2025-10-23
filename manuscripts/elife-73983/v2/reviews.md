# Peer review - Round 1

Editors:
- Kevin J Verstrepen, https://ror.org/02bpp8r91 VIB-KU Leuven Center for Microbiology Belgium

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.73983.sa0](https://doi.org/10.7554/eLife.73983.sa0)

This impressive study not only expands the identification of small-effect QTL, but also reveals epistatic interactions at an unprecedented scale. The approach takes advantage of DNA barcodes to increase the scale of genetic mapping studies in yeast by an order of magnitude over previous studies, yielding a more complete and precise view of the QTL landscape and confirming widespread epistatic interactions between the different QTL.


---

# Peer review - Round 1

Editors:
- Kevin J Verstrepen, https://ror.org/02bpp8r91 VIB-KU Leuven Center for Microbiology Belgium

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.73983.sa1](https://doi.org/10.7554/eLife.73983.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for submitting your article "Barcoded Bulk QTL mapping reveals highly polygenic and epistatic architecture of complex traits in yeast" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, including Kevin J Verstrepen as Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Patricia Wittkopp as the Senior Editor.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential Revisions:

1. Try to further expand the analysis of genetic interactions

2. Simulate a wider range of genetic architectures, including highly polygenic ones

3. Discuss the limitations of the lasso model in the discussion.

4. help readers interpret the model similiarity score.

5. Provide a more detailed rationale for the setup and interpretation of the validation experiments

6. Describe the fine-mapping methodology in more detail.

7. Discuss the impact of the limitations of the HMM model near recombination breakpoints.

8. Cite (PMID: 29487138)

Reviewer #1:

Nguyen Ba and coworkers report the development of a clever novel approach for QTL mapping in budding yeast, dubbed "BB-QTL". In brief, they use batches of barcoded yeasts to generated very large barcoded F1 libraries (100,000 cells), followed by a Bar-Seq approach to map the fitness of these individuals and a clever low-coverage whole-genome sequencing coupled to background knowledge of the parental sequences to map their respective genotypes. A custom analysis pipeline then allowed predicting QTLs as well as possible epistatic interactions for a set of 18 phenotypes.

The novel technology expands the precision and power of more traditional approaches. The results mainly confirm previous findings. S. cerevisiae phenotypes are typically influenced by many different QTLs of different nature, including coding and noncoding variation; with coding and rare variants often having a larger effect. Moreover, several QTLs located in a set of specific genes like MKT1 and IRA2, were confirmed to influence multiple phenotypes (pleiotropy). Apart from confirming previous findings, the increased power of BB-QTL does offer the advantage of having lower error rates and higher power to detect specific mutations as drivers of a QTL, including some with only small effect sizes. Together, this yields a more complete and precise view of the QTL landscape and, most importantly, confirms widespread epistatic interactions between the different QTLs. Moreover, now that the barcoded pools have been developed, it becomes relatively easy to test these in other conditions. On the other hand, the power to detect many novel (industrially-relevant) QTLs is likely limited by the inclusion of only two parental strains, one being the lab strain BY4741.

Overall, this is an impressive and interesting piece of work that not only expands the identification of small-effect QTL, but also reveals epistatic interactions at an unprecedented scale.

Still, much of the general biological conclusions are perhaps not completely novel, and I wonder whether more can be done here, to further lift the biological insight that we might gain from this unique dataset?

Specifically, I wonder whether it would also make sense to try and detect epistatic interactions in several different ways (eg simply looking at the effect of pairs of variants)? Do you find particularly strong examples of epistasis (eg complete inter-dependency of 2 mutations, or complete suppression)? Can you look for higher-order epistasis? Also, can you investigate in more detail whether epistasis partly explain the discrepancy between a given QTL's predicted effect size, and the real effect size when it is tested experimentally? Lastly, do you find evidence of selection?

One major hurdle of using QTL data to obtain improved industrial yeasts is that a QTL often seems to work in a specific background, or at least has vastly smaller effects. Similarly, in eQTL studies, it has been found that promoters often harbor several variations that together result in a limited effect on expression, likely because some (secondary) mutations were selected as suppressors of an earlier (primary) mutation. On the other hand, if a phenotype is under strong positive selection, one would expect that this compensation is absent. I wonder whether similar observations can be made in this study? For example, if one compares the fitness of the two parental strains in the different conditions, does one see systematically many more "positive" drivers in the strain with the higher fitness? Or are many "positive" QTL linked to the inferior parent? And what about the predicted epistatic interactions – do you seem more "compensatory" (negative) interactions within one genome compared to between genomes? Do you see evidence that such interacting mutations are genetically linked to (ie located in the same region)? You now validated QTL in the BY background – would their effect be different in the RM background?

Reviewer #2:

Ngyuyen Ba et al., investigated the genetic architecture of complex traits in yeast using a novel bulk QTL mapping approach. Their approach takes advantage of genetic tools to increase the scale of genetic mapping studies in yeast by an order of magnitude over previous studies. Briefly, their approach works by integrating unique sequenceable barcodes into the progeny of a yeast cross. These progeny were then whole genome sequenced, and bulk liquid phenotyping was carried out using the barcodes as an amplicon-based read-out of relative fitness. The authors used their approach to study the genetic architecture of several traits in ~100,000 progeny from the well-studied cross between the strains RM and BY, revealing in greater detail the polygenic, pleiotropic, and epistatic architecture of complex traits in yeast. The authors developed a new cross-validated stepwise forward search methodology to identify QTL and used simulations to show that if a trait is sufficiently polygenic, a study at the scale they perform is not sufficiently powered to accurately identify all the QTL. In the final section of the paper, the authors engineered 6 individual SNPs and 9 pairs of RM SNPs on the BY background, and measured their effects in 11 of the 18 conditions used for QTL discovery. These results highlighted the difficulty of precisely identifying the causal variants using this study design.

The conclusions in this paper are well supported by the data and analyses presented, but some aspects of the statistical mapping procedure and validation experiments deserve further attention.

In their supplementary section A.3-1.5 the authors perform QTL simulations to assess the performance of their analysis methods. Of particular interest is the performance of their cross-validated stepwise forward search methodology, which was used to identify all the QTL. However, a major limitation of their simulations was their choice of genetic architectures. In their simulations, all variants have a mean effect of 1% and a random sign. They also simulated 15, 50, or 150 QTL, which spans a range of sparse architectures, but not highly polygenic ones. It was unclear how the results would change as a function of different trait heritability. The simulations should explore a wider range of genetic architectures, with effect sizes sampled from normal or exponential distributions, as is more commonly done in the field.

In this simulation section, the authors show that the lasso model overestimates the number of causal variants by a factor of 2-10, and that the model underestimates the number of QTL except in the case of a very sparse genetic architecture of 15 QTL and heritability > 0.8. This indicates that the experimental study is underpowered if there are >50 causal variants, and that the detected QTL do not necessarily correspond to real underlying genetic effects, as revealed by the model similarity scores shown in A3-4. This limitation should be factored into the discussion of the ability of the study to break up “composite” QTL, and more generally, detect QTL of small effect.

In section A3-2.3, the authors develop a model similarity score presented in A3-4 for the simulations. The measure is similar to R^2 in that it ranges from 0 to 1, but beyond that it is not clear how to interpret what constitutes a “good” score. The authors should provide some guidance on interpreting this novel metric. It might also be helpful to see the causal and lead QTLs SNPs compared directly on chromosome plots.

The authors performed validation experiments for 6 individual SNPs and 9 pairs of RM SNPs engineered onto the BY background. It was promising that the experiments showed a positive correlation between the predicted and measured fitness effects; however, the authors did not perform power calculations, which makes it hard to evaluate the success of each individual experiment. The main text also does not make clear why these SNPS were chosen over others-was this done according to their effect sizes, or was other prior information incorporated in the choice to validate these particular variants? The authors chose to focus mostly on epistatic interactions in the validation experiments, but given their limited power to detect such interactions, it would probably be more informative to perform validation for a larger number of individual SNPs in order to test the ability of the study to detect causal variants across a range of effect sizes. The authors should perform some power calculations for their validation experiments, and describe in detail the process they employed to select these particular SNPs for validation.

In section A3-1.4, the authors describe their fine-mapping methodology, but as presented is difficult to understand. Was the fine-mapping performed using a model that includes all the other QTL effects, or was the range of the credible set only constrained to fall between the lead SNPs of the nearest QTL or the ends of the chromosome, whichever is closest to the QTL under investigation? The methodology presented on its face looks similar to the approximate Bayes credible interval described in Manichaikul et al., (PMID: 16783000). The authors should cite the relevant literature, and expand this section so that it is easier to understand exactly what was done.

The text explicitly describes an issue with the HMM employed for genotyping: "we find that the genotyping is accurate, with detectable error only very near recombination breakpoints". The genotypes near recombination breakpoints are precisely what is used to localize and fine-map QTL, and it is therefore important to discuss in the text whether the authors think this source of error impacts their results.

The use of a count-based HMM to infer genotypes has been previously described in the literature (PMID: 29487138), and this should be included in the references.
