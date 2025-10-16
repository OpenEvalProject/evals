# Peer review - Round 1

Editors:
- Thomas R Gingeras, Cold Spring Harbor Laboratory United States

Reviewers:
- Charles Y Lin, Baylor College of Medicine United States

## Review text

DOI: [10.7554/eLife.40760.031](https://doi.org/10.7554/eLife.40760.031)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Mismatch-repair signature mutations activate gene enhancers across colorectal cancer epigenomes" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Aviv Regev as the Senior Editor. The following individual involved in review of your submission has agreed to reveal his identity: Charles Y Lin (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

Studies of mutations in regulatory regions in cancer have lagged substantially behind those of coding mutations, due to both limited ability to interpret them, and lack of consensus in the field regarding their importance ("driver" vs. "passenger"). The manuscript describes new computational and experimental methods for the analysis of mutation at cis-regulatory regions, including analytical tools and the generation of engineered cell lines for the investigation of MMR on establishing enhancer indels. Combined, these resources are valuable tools to understand the role of non-coding region mutations on oncogenesis.

In application to colorectal cancer, the authors show that microsatellite instable (MSI) tumors have a higher rate of enhancer indels leading to gain of enhancer function and that gained enhancers undergo positive selection. The authors’ schema to identify gained enhancers using allelic imbalance and presence only in CRC specific gained enhancers validates well by sanger sequencing. They present an overall model where defects in mismatch repair (MMR) lead to widespread indels at both open and closed regions of chromatin. Gained enhancers show evidence of positive selection as indicated by maintained allelic imbalance, increased expression of putative target genes. The authors conclude with a thought provoking finding that "in CRC, deficiencies in mismatch repair lead to the appearance of indels that are recognized by FOX factors, which turn these sites into functional-regulatory elements".

Essential revisions:

The study claims are provocative and interesting, and the methods are important resources for studying regulatory mutations. However, as explained in these major comments, the authors did not provide definitive evidence for these claims, and several analyses and explanations are required in the revision to assess enhancer activity, gene regulation and TF binding prior to publication at eLife.

1) Strengthening of the oncogenic role of the phenomenon.

It is logical to assume that any enhancer activating the expression of an oncogene will undergo positive selection and also be considered an oncogenic event. Although the authors clearly demonstrate the positive selection aspect, we would like them to consider ways to bolster the oncogenic part of the argument.

• Do recurrent indels actually confer an oncogenic advantage? Is there any evidence of recurrent indels at the pathway level (indels at different loci, but converging on the same pathways)?

• Are genes associated with recurrent indels more likely to be tumor dependencies than non-recurrent genes? For example, in the Dependency Map data, USP8 seems to be a good dependency, but MSX2 is not.

• If data is available, is there any evidence of recurrent indels undergoing clonal selection?

• If most indels are potentially regulated by FOX TFs, would it be reasonable to hypothesize that MSI CRCs are more susceptible to KD of FOX TFs than MSS CRCs? Such a result would go a long way to supporting the claim that "While some of the enhancer indel targets could be oncogenes, most are genes with cancer-related functions that likely provide a selective growth advantage."

We appreciate that some of these queries would be more straightforward to address than others, but expect the authors to address at least some, which can be answered with existing data.

2) More comprehensive demonstration of the statistical associations.

In two key places the authors make statements about association (or lack thereof) to chromatin state, but either do not show the data or choose a partial view:

• The authors mentioned that enhancer regions overlapped with a large percentage of H3K4me1 ChIP-seq, but the data has not been shown. The authors should add the data supporting for this claim.

• On Figure 2A, the authors claimed that there were no associations between mutation rate and H3K27ac regions in MSI samples. Given that the image on Figure 2A shows the distribution of H3K27ac peaks and mutations specific to chromosome 14, the authors' conclusion would be better supported with a genome-wide association analysis of H3K27ac levels and indels. This should be readily rectified.

3) Explanation of the analysis of tumors from mice from different locations.

In Figure 6, the authors injected CRISPR-Cas9 induced MMR CRC cells, and control parental lines, into the portal vein of mice to allow for tumor development and downstream epigenomic/genomic analysis. The authors described that CRISPR-Cas9 induced MMR CRC tumors were harvested from liver, while control parental tumors were harvested from peritoneum. However the authors did not justify why tumors at different locations were chosen for the analysis. In addition, the authors did not investigate possible changes on liver tumor development or tumor histology that could indicate changes to oncogenesis induced by increased enhance activity or mutations. A more in depth analysis of these points could provide further support to the authors final hypothesis.
