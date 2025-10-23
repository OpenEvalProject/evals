# Peer review - Round 1

Editors:
- Kristin Tessmar-Raible, University of Vienna Austria

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.60176.sa1](https://doi.org/10.7554/eLife.60176.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This work addresses the mechanism underlying kleptoplasty in sea slugs, undoubtedly, a fascinating phenomenon. In the process of kleptoplasty animals transfer food algal chloroplasts into their digestive gland cells and benefit from the continued photosynthesis for up to several months. Previous studies suggested that the incorporation of photosynthesis-related genes from the algal nucleus into the host (sea slug) genomic DNA is a pre-requirement for kleptoplasty to occur. This study shows that such gene transfer is not necessary. The work suggests that also other mechanisms can be in place to establish and maintain the plastid-sea slug relationship. It in turn also implies that the establishment of such connections is likely easier than previously assumed, which should be considered in the context of adaptation mechanisms.

Decision letter after peer review:

Thank you for submitting your article "Chloroplast acquisition without the gene transfer in kleptoplastic sea slugs, Plakobranchus ocellatus" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Christian Hardtke as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Eugene V Koonin (Reviewer #1); Jia-Xing Yue (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional experimental data, even if they feel that they would make the manuscript stronger. However, there are several issues raised by the reviewers that we ask you to clarify, before we can take a final decision on your work.

Summary:

The manuscript addresses interesting evolutionary questions and hints at possible mechanisms about the phenomenon that certain sea slugs can take advantage of algal photosynthesis by maintaining their chloroplasts long after having ingested algae. The authors present high-quality genome assemblies and address the question of whether algal to slug HGT may have facilitated sequestration of algal chloroplasts and find no evidence to support this. There appear to be other genomic changes in the slug genome that could support retention of the chloroplasts.

Essential revisions:

1. The candidate kleptoplasty-related molluscan (KRM) genes that the authors identified in this study serve as an important stepping stone for direct assessment of their kleptoplasty-related function in future. That being said, their functional involvement is far from being proven. The authors demonstrate significant up-regulation of the expression of a set of nearly 200 genes in kleptoplast-harboring slugs. There are some functional trends among these genes, in particular, the enrichment of proteases and carbohydrate metabolism proteins, but it is unclear how this could possibly solve the enigma of the long-term persistence of the functioning kleptoplast given the short life time of the photosynthetic proteins. It is fine to present the data on gene expression up-regulation and the complementary evolutionary analysis, but the authors should be far more circumspect in their conclusions on the direct relevance of the respective genes and rather admit that the puzzle remains.

2. We think that naming the phenomenon of the slugs retaining chloroplasts "DNA/RNA-independent transformation" is problematic, because of the fixed definition of the word "transformation" in (molecular) biology, where transformation is defined as a genetic alteration, which it is not. It does not appear to be plausible that the phenotype and organelle "have moved beyond the species" – they are not inherited in the new species and it is a dead-end for these chloroplasts that are eaten and die a few months later than the rest of the algae. There is likely selective pressure for the slug to hold on to its "food" for a while longer due to the chemical activity of the chloroplast, but there is no selective pressure on the chloroplast to be consumed in this way that would constitute reciprocal evolutionary changes. We do not see this as anything beyond animal adaptations that facilitate utilization of a food source.

3. "Taken together, the data for the three photosynthetic indexes indicate that kleptoplast photosynthesis increases resistance to starvation in PoB." – This isn't directly shown here. There are no plastid-free control slugs. Light exposed slugs live longer – but how do we know it is photosynthesis? Light can affect other cellular processes – ROS, etc.

4. In the photosynthesis experiments (Figure 2), the authors compare the kleptoplast activity to the plastid in the algae H. borneensis. However, genome sequencing revealed two distinct plastid genomes (kRhip and kPoro) which corresponded with plastids from Rhipidosiphon lewmanomontiae and Poropsis spp., neither of which were included in genomic comparisons, and were not used in the comparison for photosynthetic rate.

5. Have the authors considered that the slugs may have acquired photosynthesis related genes from non-algal origins that could potentially support the kleptoplasts? There are other examples of symbioses with many partners where HGTs not from any of the original lineages support the relationship (Husnik, 2013, Cell). Line 170 mentions 6 Chloroplast-related genes in PoB but there is no follow up on what these are, only that they do not look like algae. Could these support the photosynthetic abilities of the kleoptoplasts?

6. In general, the manuscript's readability needs improvement. This is particularly severe for the referral to the figures and a lack of clarity for the RNA seq analyses.

- Different panels of main figures (e.g. Figure 1A-1F, Figure 2B) are not well-referred in the current manuscript, which compromised the readability of the current manuscript.

- Figure 5C is too complex and busy. We recommend to simplify this panel. Here are some suggestions regarding its current form: The authors could consider further subdividing it into multiple panels. Also, the "domain structure" key boxes should belong to the left side of this panel , whereas an additional key box should be provided for explaining colors used in the gene position graph (on the right side of this panel). Otherwise, the readers could easily get confused. Finally, the authors might want to consider changing the color scheme used for FDR to make it more different from the color schemes used for denoting domain structure and gene position.

- Some of the RNASeq analyses are difficult to follow. For instance trying to match Figure S22 with the text is difficult. The methods states that 5 slugs were used for whole-transcriptome sequencing, but 15 libraries were constructed, and there are only 13 library IDs in Figure S22. There are 15 libraries in the heat maps in the main text. What model was used in DESeq2 to call differential expression? What level of coverage was achieved in the RNA-Seq libraries? It seems there is no biological replication for some of the samples?

7. It is interesting that the genes that are expanded in copy number also look to be upregulated. However, it is unclear whether or not multiple mappings are accounted for, and how. If multiple mappings of closely related genes are not properly accounted for then it may appear as up-regulation. Similarly, how close in sequence are the paralougs of these genes, ie, would the reads map to each other?

8. During genome assembly, were the removed "bacterial scaffolds" also present at different coverage levels? Did the authors screen for fungal contaminants also? They mention in the RNA-Seq analyses how other food/biofilms can be present, so there it is likely that other contaminants could be in the assembly.

9. Figure 3C: According to the authors, "the vertical bar chart indicates the number of genes conserved among the species", but if so, why do rare genes seem to be more conserved than core genes according to this bar chart? This needs to be clarified.

10. To test if duplicated genes in PoB are under diversifying selection (a.k.a positive selection) or relaxed purifying selection during neofunctionalization, the authors could use tools such as PAML for a formal test.
