# Author response - Round 1

Authors:
- David Li-Kroeger ([ORCID: 0000-0001-6473-7691](https://orcid.org/0000-0001-6473-7691))
- Oguz Kanca
- Pei-Tseng Lee ([ORCID: 0000-0002-7501-7881](https://orcid.org/0000-0002-7501-7881))
- Sierra Cowan ([ORCID: 0000-0003-3530-9326](https://orcid.org/0000-0003-3530-9326))
- Michael T Lee
- Manish Jaiswal
- Jose Luis Salazar
- Yuchun He
- Zhongyuan Zuo
- Hugo J Bellen ([ORCID: 0000-0001-5992-5989](https://orcid.org/0000-0001-5992-5989))

## Response text

DOI: [10.7554/eLife.38709.023](https://doi.org/10.7554/eLife.38709.023)

Reviewer #1:

[…] There is no doubt that DH is another extremely useful reagent developed by Bellen lab, and I do not have further comments. But it was not too clear to me whether the second method (two-step replacement of the gene) is significantly faster or more convenient than other already-applied CRISPR methods to generate endogenous tag. This method involves 1) generation of a gene specific construct to generate knock-out flies, and 2) generation of a construct that can tag or point-mutate the gene of interest, therefore need to be conducted at gene-by-gene basis. But I do see a point that DH and CRISPR methods are two complementary methods that are intended to cover all protein coding genes in the Drosophila genome, so it makes sense to report in a single paper. They have already done their best to explain the advantages of their CRISPR method, so I don't have additional suggestions, but I am just noting that I was a bit puzzled when they moved onto CRISPR method because two methods are very different.

We agree that the two methods are very different. However, the methods complement each other and facilitate manipulation of virtually all genes in the Drosophila genome. Also, the use of the yellow wing SIC, while not faster, is precise and reliable. The dominant marker is also more convenient than other CRISPR-based methods.

Reviewer #3:

[…] The levels of GFP signal are disappointingly low for many genes, and not much information is provided on how they were imaged – only using a 20x objective in an LSM 880 confocal. If the authors could improve the brightness (or signal/noise ratio, which will have the same outcome), they would significantly improve the utility of their system and the insertions that are already available, e.g.:

- Presumably they are already using the maximum level of laser power that doesn't bleach their signal?

- Most 20x objectives are low NA – although they do not actually state the NA in their Materials and methods. Since fluorescence intensity in confocal or epifluorescence microscopy varies with the 4th power of NA, even small increases in NA can greatly improve S/N ratio or brightness, and oil or water objectives are far superior to air objectives for this. Even allowing for the 4-fold dimmer intensity of 40x compared to 20x, the higher NA of most 40x objectives also makes these images usually brighter, even if there is no scope to improve sensitivity with an available 20x objective.

- Using a larger pinhole setting will greatly improve brightness or S/N ratio of a weak signal since it increases the photon flux without a proportional increase in noise (albeit at the cost of z-resolution).

- Does lowering the laser scan speed, i.e. increasing pixel dwell time, increase the photons enough to improve the signal, if laser power cannot be increased further?

We agree that the GFP signal of the endogenously-tagged proteins is sometimes low, especially in the nervous system. We already reported this before. Note the expression in third instar larvae is still significantly stronger than in the adult brains. The noise ratio is difficult to optimize and often affects the quality of imaging (Diao et al., 2015; Lee et al., 2018). To address this issue we invested additional effort in optimizing the signal to noise ratio.In the previous version all the samples were imaged using rabbit anti-GFP directly fused to Alexa488 fluorophore. In this version we re-stained all the samples using rabbit anti-GFP and stained with a secondary antibody to amplify the signal. During the imaging we used many of the suggestions proposed by the reviewer and we were able to improve images for some. We therefore replaced images of larval brains for MI06872-CG34383, MI08614-Dgk and MI15073-CG9132 in Figure 3.

To document the usefulness of DH tagging with GFP we decided to dissect ovaries and image ovarioles. We focused on stage 9 and 10 egg chambers where different cells can easily be identified and it is relatively easy to assess subcellular protein distribution. We inserted a whole new figure (Figure 4) showing that it is pretty straightforward to stain and image with high resolution in ovarioles using similar settings that we used in the brain. We hope we have appeased the reviewer’s concern with these new data. Specifically, we added the following paragraph:

“As the GFP protein traps should be able to report the subcellular localization of the tagged protein we turned to tissues were subcellular localization and specific cell expression is easily assessed. […] In summary, GFP protein tagging with DH can be used to determine the cellular and subcellular localization of tagged proteins.”

To further highlight the usefulness of the GFP-tagged proteins, we also added the following text to the Discussion:

“for most genes the corresponding GFP-tagged protein signal in adult brains is often weak, consistent with previous results (Lee et al., 2018a; Diao et al., 2015). However, all the lines tested in the brain allow us to rapidly and reliably determine the cellular and subcellular localization of the GFP tagged proteins in egg chambers.”

We also included additional information in the Materials and methods section to describe our imaging settings with confocal microscopy:

“To increase signal, some samples used anti-GFP antibody (Invitrogen, A11122) followed by incubation with secondary antibody (Alexa Fluor 488-conjugated goat anti-rabbit IgG). […] Laser intensity and detector gains were adjusted as needed to increase signal-to-noise ratio and prevent signal saturation.”
