# Peer review - Round 1

Editors:
- Yukiko M Yamashita, University of Michigan United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.38709.022](https://doi.org/10.7554/eLife.38709.022)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "An expanded toolkit for gene tagging based on MiMIC and scarless CRISPR tagging in Drosophila" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Yukiko M Yamashita as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by K VijayRaghavan as the Senior Editor.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

This is yet another set of useful tools by the Bellen lab allowing the fly community to move on and fully profit from the new CRISPR technologies in full, and the reviewers are quite positive about this work. Reviewer #3 pointed out that the image quality can be better, and if it is something that can be easily addressed, better images should be used. We recognize that it is possible that the authors already tried to optimize imaging quality but the Materials and methods section does not provide sufficient information whether the image can be further improved or not. Thus, we would like to see 1) better images and 2) more information about the imaging in the Materials and methods section.

Reviewer #1:

This is a report on yet another useful gene trap/protein trap methodology that utilizes MiMIC in Drosophila.

This new resource is named 'Double Header' (DH), which results in protein trap OR gene trap (gal4) depending on which direction insertion happens, making any insertion events 'productive'. DH construct can be provided either as a plasmid to be injected to the fly embryos, or as Cre-mediated circularized DNA from the genomic transgene. The latter only requires genetic crosses. They provide a few 'proof of principle' examples and confirm that DH behaves as expected (e.g. reporting the expression pattern). DH and characterized a few DH insertions on known genes. Then they turned their attention to a method that can target genes that do not contain introns at all (which are about ~50% of Drosophila genes, but can never be targeted by MiMIC strategy). They used CRISPR/Cas9 strategy to replace a gene of interest with visible, dominant marker (they chose y gene expressed in wing) to facilitate visual screening. Then this will be next used to be replaced with any donor gene (as an example, they generated point mutations in Nmnat gene).

There is no doubt that DH is another extremely useful reagent developed by Bellen lab, and I do not have further comments. But it was not too clear to me whether the second method (two-step replacement of the gene) is significantly faster or more convenient than other already-applied CRISPR methods to generate endogenous tag. This method involves 1) generation of a gene specific construct to generate knock-out flies, and 2) generation of a construct that can tag or point-mutate the gene of interest, therefore need to be conducted at gene-by-gene basis. But I do see a point that DH and CRISPR methods are two complementary methods that are intended to cover all protein coding genes in the Drosophila genome, so it makes sense to report in a single paper. They have already done their best to explain the advantages of their CRISPR method, so I don't have additional suggestions, but I am just noting that I was a bit puzzled when they moved onto CRISPR method because two methods are very different.

Reviewer #2:

This is yet another set of useful tools by the Bellen lab allowing the fly community to move on and fully profit from the new CRISPR technologies in full. As for all the other recently developed tools and resources, these novel methods will be used by many to perform precise gene manipulation and to facilitate the monitoring of gene expression, protein localisation, as well as providing the reagents for many other protein-based manipulations. I do not see any need for further work or editing.

Reviewer #3:

Li-Kroeger and colleagues describe two very useful extensions to widely used current approaches to genome engineering of individual Drosophila genes.

The first one is an incremental (but still productive) improvement to the widely used MiMIC system. The authors design a single insertional fragment that can insert either as an in-frame fusion (in any reading frame) or a GAL4 transcriptional fusion, in a single experiment, and show that this can work reasonably efficiently when injected, and more efficiently when supplied from an existing transgenic construct. While the advance is an incremental one rather than a new concept, it is likely to be widely used, since it can potentially generate pairs of very useful stocks, for the same effort currently used to generate either a single GFP or GAL4 insertion, it can be applied using thousands of existing MiMIC insertion stocks that are already available from stock centres, and only a few additional transgenic stocks described in this paper – which the authors have a good track record of sharing with the community.

The second reported advance is more substantial, both conceptually and practically. It provides a CRISPR-based approach to overcome some of the limitations of the MiMIC system and other CRISPR approaches. They describe a two-step process, in which CRISPR is first used to integrate a yellow+ cassette at a gene of interest, and the then locus with the inserted cassette is again targeted by CRISPR to integrate an engineered fusion and/or mutant allele of interest. The advantages are:

- use of a convenient body color marker to score each of the two steps, and identify low-frequency events more conveniently than by molecular screening;

- the ability to target any gene, independent of whether existing insertional mutations are available;

- design of the insertional cassette sequences which makes the insertion or swap steps irreversible;

- the ease of introducing any mutations or fusions constructed in vitro;

- extensive supporting evidence from several genes, and a different mutations or fusions with a gene of interest, that it works and is likely to be easily applicable.

The levels of GFP signal are disappointingly low for many genes, and not much information is provided on how they were imaged – only using a 20x objective in an LSM 880 confocal. If the authors could improve the brightness (or signal/noise ratio, which will have the same outcome), they would significantly improve the utility of their system and the insertions that are already available, e.g.:

- Presumably they are already using the maximum level of laser power that doesn't bleach their signal?

- Most 20x objectives are low NA – although they do not actually state the NA in their Materials and methods. Since fluorescence intensity in confocal or epifluorescence microscopy varies with the 4th power of NA, even small increases in NA can greatly improve S/N ratio or brightness, and oil or water objectives are far superior to air objectives for this. Even allowing for the 4-fold dimmer intensity of 40x compared to 20x, the higher NA of most 40x objectives also makes these images usually brighter, even if there is no scope to improve sensitivity with an available 20x objective.

- Using a larger pinhole setting will greatly improve brightness or S/N ratio of a weak signal since it increases the photon flux without a proportional increase in noise (albeit at the cost of z-resolution).

- Does lowering the laser scan speed, i.e. increasing pixel dwell time, increase the photons enough to improve the signal, if laser power cannot be increased further?

In conclusion I'm not convinced from their Materials and methods section that they've pushed sensitivity or S/N ratio to the limit. If not, I would like them to re-image their GFP-trap panels in Figure 3 and Figure 3—figure supplement 1 with acquisition settings that improve sensitivity and S/N ratio; if they have done this already, they need to document their efforts better and provide more details on the microscope acquisition settings.
