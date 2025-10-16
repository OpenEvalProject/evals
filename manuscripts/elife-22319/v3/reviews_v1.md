# Peer review - Round 1

Editors:
- Utpal Banerjee, University of California, Los Angeles , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.22319.012](https://doi.org/10.7554/eLife.22319.012)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Dpp from the anterior stripe of cells is crucial for the growth of the Drosophila wing disc" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and K VijayRaghavan as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission. We hope you will be able to submit the revised version within two months.

Summary:

A contentious item that continues to raise interest concerns the relationship between the gradient of the BMP4-like signaling protein Dpp produced in Drosophila wing discs and cell proliferation in the disc. Dpp is both necessary and sufficient for disc growth, and the problem basically boils down to why regions with different levels of Dpp and BMP signaling do not cause different amounts of growth. Evidence and arguments on this point remain of high current interest.

The present manuscript is a partial rebuttal to the 2015 Nature paper from Akiyama and Gibson, which used various types of dpp loss-of-function clones to argue that the BMP Dpp produced by the stripe of cells anterior to the A/P boundary in wing discs was not necessary for the growth of the disc. This argued that models based on reading a gradient of Dpp were likely wrong, and that levels could be greatly reduced without greatly affecting growth, and thus models based on a temporal gradient of increasing BMP signaling were probably wrong as well. Nonetheless, that study showed that the Dpp produced by the entire anterior compartment was necessary for growth, at least up until 36 hours before wandering third instar, presumably this was supplied by low-level Dpp produced outside the normal stripe of high level Dpp expression.

The present manuscript argues that stripe Dpp is necessary for growth, using the same conditional dpp allele used by Akiyama, but a different (ptc) Gal4 driver that the authors show covers more of the stripe at earlier stages, especially in the ventral pouch.

Essential revisions:

Reviewer 1:

1) Since Akiyama already showed that removal from the entire anterior compartment reduces growth, the claim in the present study rests entirely on whether ptc-gal4 drives the excision of the conditional dpp allele in the stripe, or whether it drives excision more widely in the disc. This is a real worry, because the endogenous ptc gene is expressed at low levels throughout the anterior compartment. And as the authors (and others previously) show, ptc-gal4 can drive excision of a G-TRACE maker throughout the anterior as well.

Unfortunately, there is no direct way of telling where the dpp allele has been recombined. The conditional allele contains no marker of excision, and loss of dpp itself cannot be detected except where dpp expression is very strong, as Akiyama did.

The authors argue that there are some discs where ptc-gal4-driven G-TRACE is not excised throughout the anterior, and that therefore these discs must also be those where the conditional dpp allele is not recombined throughout the anterior. However, this makes the unwarranted assumption that the dppFO and G-TRACE are identically sensitive to FLPase. In my experience, different flpout constructs show different sensitivities. The authors also seem to be implying that these are disc to disc differences in cell "lineage", but I doubt greatly whether stripe cells ever give rise to far anterior cells. Rather, the variation likely to be due to slight differences in Gal4 or FLPase expression, or simply a level of randomness in the excision events. In my hands, G-TRACE from Bloomington and ptc-Gal4 can even give rise to expression in the far posterior compartment, cells that have certainly not descended from anterior compartment stripe cells.

I cannot think of a way around this problem, short of building a new excision allele with a marker in the excised DNA. I am open to counter-arguments, but without something I cannot accept the authors' interpretation.

2) One difficulty is that Akiyama show that their dpp-gal4 technique removes most or all stripe Dpp from the dorsal wing pouch and hinge, and also greatly reduces pMad there, as early as 72 hours AEL (their Figure 3). Nonetheless, the dorsal pouch reaches a pretty normal-looking size by late third (although they did not measure pouch size alone, so it is possible there was a slight defect). If this is correct, then loss of the gradient and stripe do not affect growth from 72 hours on.

Either the authors need to disprove this, or they have to incorporate it into their discussion. Does the Akiyama allele version of the experiment lead to loss of Dpp and the pMad gradient in parts of the disc at 72 hours, and is growth in those regions affected or unaffected?

If Akiyama is correct, this should be mentioned. One possible explanation is that the authors might investigate is that the early pMad loss was not enough to increase brinker expression at early time points, as Akiyama only examined brinker at late third. Since the authors have Akiyama's allele, could they look? My thinking here is that the different results might not be due to whether stripe Dpp is lost, per se, but how much residual Dpp signaling is left from Dpp elsewhere in the disc, and whether that residual signaling is enough to suppress brinker expression during the growth phase.

3) In the Gal80ts experiment, the authors also need to show a control wing that is homozygous for the dppFO allele, but reared continuously at 18°C.

Reviewer 2:

1) Figure 2 is a single addition to the GAL4 drivers explored in Extended Data 6 by Akiyama & Gibson, 2015; Figure 3 is an extension of Extended Data 4e of Akiyama & Gibson, 2015; Figure 4 is an extension of Extended Data 7 and lacks the temporal resolution for the Gal80ts experiment as well. There are no experiments to independently substantiate their claim of requirement of central stripe of Dpp for growth.

2) Usage of mCherry: NLS as a probe to study the activity of GAL4 domains: It has been demonstrated that GFP matures in about 5-20 mins, while mCherry matures in about 40-80 mins at 37°C. Slow maturation of mCherry is a property used in design of fluorescent timers (Khmelinskii et al., 2012). Maturation of mcherry is further slower at lower temperatures (~20-25°C). The kinetics of the marker (production/degradation) is crucial for marking the boundaries of GAL4s. Therefore, another probe should be used to confidently determine the boundaries of dpp-GAL4/ ptc-GAL4 domain. Ideally as Dpp is a secretory protein, the domain comparison should be studied with respect to Dpp mRNA and not protein.

3) Evans et al., 2009 using GTRACE show that the ptc-GAL4 marks the entire anterior compartment while dpp-GAL4 only marks a portion of anterior compartment although both show a similar real-time expression profile along the A/P boundary. It is important to "quantify" the variation observed in GTRACE to confidently negate the following possibility: Is dpp from the set of cells excluded by dpp-GAL4 lineage but included in ptc-GAL4 lineage (and ci GAL4) in the anterior compartment important for growth?

Reviewer 3:

The requirement of Dpp signaling for growth of the Drosophila wing has been a subject of much debate recently. Despite a large amount of evidence showing that Dpp is required for wing growth, and that it acts by repressing the growth-repressor Brinker, recent work has suggested that Dpp is only required for growth early in wing development, and not later on (as of mid-third instar). The manuscript here by Matsuda and Affolter revisits this issue. They show that Dpp is indeed required for wing disc growth, providing a technical explanation for the lack of a growth effect seen in Akiyama and Gibson 2015. In terms of temporal requirements, they show that Dpp is required as of early L3 for disc growth (although this was not really debated). In terms of spatial requirement, they find that discs where Dpp was removed only from the medial expression stripe display growth defects, indicating that the medial expression domain of Dpp is needed to support wing growth. Overall, the data quality are good. The manuscript analyzes the issue less in depth than the two other manuscripts that were co-submitted.

From Akiyama and Gibson, there is little debate whether Dpp is needed for growth at early 3rd instar. The debate is whether it is needed later on, as of 96h AEL (mid 3rd instar) (see Figure 2m of Akiyama and Gibson, where the reduction in size at 72h is by 50% and statistically significant, whereas the reduction in size at 96h is not significant). Hence Figure 4 presented here is not very novel, but instead should be repeated at 96h AEL.
