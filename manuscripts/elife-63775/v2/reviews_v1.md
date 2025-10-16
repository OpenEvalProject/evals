# Peer review - Round 1

Editors:
- Peter Turnbaugh, University of California, San Francisco United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.63775.sa1](https://doi.org/10.7554/eLife.63775.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Huss et al. have developed a novel tool (ORACLE) for generating libraries of phage variants. They go on to apply this tool to study the residues important for T7 host specificity, providing a rich dataset for in-depth functional studies. They validate a subset of hits and use this information to engineer T7 variants that may be able to overcome bacterial resistance against a urinary tract infection associated strain, consistent with their in vitro results. Their approach provides both a valuable new tool and intriguing biological insights prompting future studies.

Decision letter after peer review:

Thank you for submitting your article "Mapping the Functional Landscape of the Receptor Binding Domain of T7 Bacteriophage by Deep Mutational Scanning" for consideration by eLife. Your article has been reviewed by four peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Gisela Storz as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Laurent Debarbieux (Reviewer #2); Breck A Duerkop (Reviewer #3); James S Fraser (Reviewer #4).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below only address clarity and presentation.

Summary:

Huss et al. describe a phage genome engineering technology that they call ORACLE. This technique uses recombineering of a phage target gene with a variant library to identify both gain and loss of function mutations. The beauty of this method and what makes it superior to other techniques is that it dramatically limits loss of mutants that are less fit during the initial round of library generation. Thus, the pool of variants is vast and is reduced in bias toward more fit species based on the host used for initial library amplification. They use the model coliphage T7 as a proof of principal and show that several previously unidentified residues of in the T7 tail fiber play critical roles in both loss and gain of function for phage infectivity and they also identify residues that are major drivers of altered host tropism. Lastly, they apply this library to a pathogenic UTI associated strain of E. coli which is normally resistant to wild type T7 infection and identify tail variants of T7 that can now infect this strain, highlighting the applicability of this method toward the discovery of engineered phages that could be used therapeutically. Altogether this is an important advancement in phage engineering that shows potential promise for future phage therapies.

Essential revisions:

1) Claims about generalizability should either be removed, qualified with the various caveats, or supported by additional data. This study focused on a single phage gene and a single host bacterial species. As such, it is not clear if ORACLE will work well in other contexts. More concerningly, the lack of reproducibility across technical replicates in some of the experiments (e.g., subsection “Discovery of gain-of-function variants against resistant hosts”) may indicate that this method will not work for other T7 genes or phenotypes of interests.

The authors state that ORACLE overcomes three major hurdles that make it better than existing methods, one of which is "generalizability for virtually any phage", while denouncing other systems for being applicable for highly transformable hosts only. This is highly exaggerated since ORACLE requires transformation of two plasmids (helper and donor) including one with tunable gene expression, which is clearly not possible in many bacteria. Furthermore, the enrichment step requires a strain with a functional CRISPR/Cas9 system, which again is not so obvious in the bacterial world.

T7 and its E. coli hosts are domesticated strains where phage engineering is considered easier than less well studied phages and their hosts. Considering the authors indicate that the ORACLE method could be applied to any phage-bacteria pair, I would like to see just how feasible it is to generate a highly diverse library on a phage-host pair that are not as well studied as T7-E. coli. This is the situation that would likely occur therapeutically.

2) The description and reasoning behind the use of the helper plasmid carrying the wild type tail fiber is not clear as described. This is really what reduces the bias in the first round of library generation and is critical to the technology. I had to re-read this section several times to fully understand the purpose of this. It would be nice to illustrate this in more detail in Figure 1A, showing that the first round of phage packaging of variants is in to particles that most likely have WT tail fibers, thus all phages generated regardless of the variant DNA packaged should in theory have an equal chance of infecting a host and being propagated in the accumulation stage.
