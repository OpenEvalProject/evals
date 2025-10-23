# Peer review - Round 1

Editors:
- Stephen C Ekker, Mayo Clinic United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.59683.sa1](https://doi.org/10.7554/eLife.59683.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Your method is a nice next step in using gene editing technology for exploring functional genomics. Your application of this approach in the areas of behavioural science is especially noteworthy, especially for the adult zebrafish as a model system.

Decision letter after peer review:

Thank you for submitting your article "A simple and effective F0 knockout method for rapid screening of behaviour and other complex phenotypes" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Didier Stainier as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Darius Balciunas (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

As the editors have judged that your manuscript is of interest, but as described below that additional experiments are required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Summary

Kroll and colleagues describe a new efficient strategy to reliably generate F0 zebrafish embryos with (multiple) genes knocked out using CRISPR/Cas9 RNPs. They showed that in addition to target single genes, this method could be successfully used to create double knockouts of slc24a5 and tbx5a gene pair, or tyr and ta gene pair, in F0 embryos. Strikingly, they also demonstrated direct generation of triple gene knockouts of mitfa, mpv17 and slc45a2 in F0 larvae, which fully recapitulated the pigmentation defects of the crystal mutant. As the authors point out, their methodology is extremely likely to be adapted for candidate genes for traits which display a range of phenotypes among wild type embryos or larvae.

The manuscript points out a rather obvious but somehow underreported feature of NHEJ-based mutagenesis: assuming random size of indels, when 100% of DNA is mutated fewer than 50% (.67x.67) of cells in an embryo will contain frameshift mutations in both alleles. Thus, successful recapitulation of a mutant phenotype in an F0 embryo relies on mutagenesis of an essential part of the protein (not always as straightforward as it seems), utilization of other repair pathways such as MMEJ (not always reliable), or fortuitous help from largely unknown factors which skew the distribution of indel sizes (multiple guide would RNAs need to be tested without guarantee of success). Simultaneously designing several guide RNAs against the gene and co-injecting them, as the authors propose, seems to be an excellent and straightforward strategy.

They established a rapid sequencing-free method to evaluate the activity of Cas9 RNP by using headloop PCR, facilitating the selection of target sites. This is a new tool for the zebrafish community.

Despite the presented data on several loci, it is not clear whether and how this method is better compared to a series of prior related F0 approaches. This question is the crux of this method manuscript.

Essential revisions

1) The authors need a specific direct comparison with prior reports, notably Wu et al. in 2018. Several genes were tested in both work, such as slc24a5, tyr, tbx16, and tbx5a, did you use or compare the same target sites in these genes as reported by Wu et al.?

2) The second major consideration in the field is validating F0 somatic mosaic results with non-mosaic outcomes in prospective loci. Replicating known prior phenotypes is an important first step. But clearly validating new loci where the outcome is unknown is the key challenge in the field and the bar by which these methods will be judged. N=1 locus data has many questions – was this gambler's luck (i.e. they were fortunate the first locus they tried worked)? Did they try others and not have them work?

Additional points

1) Successful multiplex targeting has already been achieved in zebrafish, including the Figure 6 in Jao et al., 2013 reference. This needs to be acknowledged and elaborated upon (different efficiencies, etc.).

2) The statement that "The common strategy is to inject ... RNP..." excludes a significant number of laboratories which prefer to inject Cas9 RNA. The proposed three-guide method should work just as well with Cas9 RNA.

3) The data in Figure 1—figure supplement 1 seems to show that relative concentration of functional Cas9 protein is rate-limiting, perhaps even at the highest 1:1 ratio. Statement that 1:1 ratio is "optimal" (page 7) implies that reduction in the amount of guide RNAs would lead to reduced penetrance of the phenotype, which may or may not be the case.

4) The observation that 41/41 adult slc24a5 fish displayed golden phenotype suggests that only pigmentation-negative embryos (perhaps the 63/67) were raised to adulthood. Please clarify.

5) I am not convinced that headloop PCR is sufficiently quantitative for assessment of guide RNAs for an F0 assay. What is the minimum mutagenesis rate needed to obtain a "positive" PCR result and does it vary between loci? For example, if a specific gRNA produces 30% indels, would it score as positive in Headloop PCR? Assuming 67% frameshift probability, such guide RNA would only produce about 4% (0.3 x 0.67 x 0.3 x 0.67) of biallelically mutated cells and be therefore quite useless in an F0 assay. This analysis can be performed by mixing wild type and mutant DNA in different ratios.

6) Is the dosage/amount of Cas9 or RNP used in this study different or comparable with Wu et al.? Does it account for the improvement of the method described in the study?

7) The authors propose to design the three target sites in distinct exon within each gene. Is it really important and/or necessary to achieve high efficient biallelic knockouts? Any evidence?

8) According to the section of 'Materials and methods', the synthetic gRNA was made of two components, i.e., crRNA and tracrRNA. Synthesis of gRNA as a single molecule by in vitro transcription is usually more popular and economic, is it really necessary to use crRNA and tracrRNA to achieve high efficient biallelic knockouts? Any evidence?

9) Could headloop PCR be used for the quantification of mutagenesis efficiency (indel-producing mutation rate) of Cas9/gRNA? How sensitive is this method? Could small indels (such as 1-bp insertion or deletion) be detected by the headloop PCR?

10) In addition to indels, deletions between two double strand breaks induced by two gRNAs are also important for the generation of biallelic knockouts of the target gene. The authors showed the analysis of mutations in each site (such as in Figure 2A), is it possible to quantify the distribution and contribution of all the different deletions?

11) Figure 1C and 1D: The authors compared the effects of the injection of 1, 2, 3, and 4 loci. How were the 1, 2, and 3 loci selected from the four target sites? Will each of the four loci give the same or different phenotypic ratio if tested individually? Will different combinations of 2 loci or 3 loci give the same or different phenotypic ratio? Or which combination of 2 loci or 3 loci will give the highest mutagenic effect? For example, in Figure 1C, the 3-loci showed comparable effect with 4-loci, while the 2-loci is less effective; is it possible to find other 2-loci combinations which could show higher mutagenic efficiency than the current 2-loci, such that the effect of the new 2-loci combination is as good as the 3-loci or 4-loci combination? Conversely, in Figure 1D, the 2-loci already showed the highest mutagenic effect, is it because of this particular 2-loci combination, or any 2-loci combination will show the same efficiency?

12) Figure 6: The phenotypes of scn1lab F0 knockouts are more severe than those of scn1lab-/- mutant. Any explanation?

13) Please provide the academic name of zebrafish in its first appearance.
