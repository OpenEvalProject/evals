# Author response - Round 1

Authors:
- Joshua C Cofsky ([ORCID: 0000-0001-5403-8555](https://orcid.org/0000-0001-5403-8555))
- Deepti Karandur
- Carolyn J Huang
- Isaac P Witte ([ORCID: 0000-0002-3879-0306](https://orcid.org/0000-0002-3879-0306))
- John Kuriyan ([ORCID: 0000-0002-4414-5477](https://orcid.org/0000-0002-4414-5477))
- Jennifer A Doudna ([ORCID: 0000-0001-9161-999X](https://orcid.org/0000-0001-9161-999X))

## Response text

DOI: [10.7554/eLife.55143.sa2](https://doi.org/10.7554/eLife.55143.sa2)

[…] Overall, this study reveals significant differences in the stability of R-loop:DNA junctions, irrespective of protein. On the one hand, this is a very interesting observation that could have widespread implications in nucleic acid biology. On the other, it remains unproven that the fundamental stability differences observed here have strong implications for the mechanism of Cas12a, as the data shown correlation but not necessarily a causative link between DNA junction stability and target strand cleavage. After all, nucleases such as Cas12a are quite capable of using binding energy to manipulate nucleic acid substrates to a remarkable degree, and the Cas12a second strand cleavage reaction requires considerable more than merely fraying of the R-loop junction.

We agree that protein binding energy is probably mechanistically important, and we agree that our data have not definitively established a causative link between DNA junction stability and target-strand cleavage. Instead, our data identify an interesting structural feature of CRISPR interference complexes that sets them apart from other nucleases that only have protein binding energy at their disposal. To catalyze target-strand cleavage, Cas12a likely relies on a combination of protein:DNA interactions and the native conformational dynamics of the nucleic acids themselves. We have made a minor adjustment to the final paragraph of the Concluding Remarks to clarify this point.

That said, this is an interesting manuscript presenting a number of carefully designed experiments that yield some important new data with potentially wide relevance. The significance of the work is discussed in a thoughtful way and the paper will represent an impactful contribution to the field. We propose an essential revision that does not require new experiments.

Essential revision:

Section about "difference in interhelical stacking energy may underlie asymmetric R-loop flank stability": Here the authors "hypothesize that the asymmetry may emerge from energetic differences in the coaxial stacking of a DNA homoduplex on either end of an RNA:DNA hybrid", which got me lost. The authors refers to crystal structures of the Cas12a/R-loop structure in the 2019 Swarts and Jinek paper (PDB 6I1K and 6I1L). 6I1K best depicts the Cas12a/R-loop, however, the PAM-distal DNA duplex is not coaxially stacked underneath the DNA/RNA hybrid in the structure, it is rotated 180° to the side. I am not sure whether the discussion in this section and the molecular dynamics simulations in Figure 5 can directly explain the fraying propensity in PAM-distal DNA. Perhaps the authors should consider the possibility that the twisting of the backbone at the R-loop junction drives the DNA unwinding, which involves base-flipping in a sequential fashion from the junction of the R-loop. This rotation may be easier from the 3'-end of the R-loop because the backbone has a higher degree of rotation freedom, which means lower energetic barrier.

We respond to these points individually here:

References to the crystal structures:

– We agree that this line of discussion is confusing, as the crystal structures do not serve as direct evidence for or against the mechanism that we discuss here. To clarify the main point of this section, we have removed the discussion of the crystal structures flagged by the reviewer. We have also removed some of the more detailed discussion at the end of this section that, retrospectively, seems extraneous to the main point. We thank the reviewer for identifying the weaknesses in this section, and we hope our changes have clarified our point.

Relationship of fraying propensity and stacking energy:

– Fraying is expected to occur more readily from a duplex terminus that is not stacked on top of another duplex (Häse and Zacharias, 2016). Therefore, interhelical junctions that spend less time in a stacked conformation (i.e., those with weaker stacking energy) are likely to exhibit a greater degree of fraying from each constituent duplex.

Alternative explanations for the observed DNA fraying behavior:

– There could be several explanations for the difference in fraying propensity at the two boundary types, and the “stacking energy hypothesis” presented in this manuscript is just one hypothesis that is supported by our experiments and simulations. We have added a sentence to the end of this section to indicate to the reader the level of certainty that we can currently attribute to our hypothesis.
