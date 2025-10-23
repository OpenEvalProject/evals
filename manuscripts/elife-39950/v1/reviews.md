# Peer review - Round 1

Editors:
- Eduardo Franco, McGill University Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.39950.020](https://doi.org/10.7554/eLife.39950.020)

In the interests of transparency, eLife includes the editorial decision letter, peer reviews, and accompanying author responses.

[Editorial note: This article has been through an editorial process in which the authors decide how to respond to the issues raised during peer review. The Reviewing Editor's assessment is that all the issues have been addressed.]

Thank you for submitting your article "A generalized theory of somatic evolution" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by Eduardo Franco as Reviewing Editor and Aviv Regev as the Senior Editor. The reviewers have opted to remain anonymous.

The Reviewing Editor has highlighted the concerns that require revision and/or responses, and we have included the separate reviews below for your consideration. In the interest of providing you with constructive feedback we have edited the reviewers' critiques while keeping the substantive points in need of revision. If you have any questions, please do not hesitate to contact us.

Your modelling work advances our understanding of multi-stage carcinogenesis by accommodating the effects of ageing and other potential drivers of biological variability. However, reviewers have raised significant major concerns. In brief, they challenged many of your assumptions regarding biological mechanisms and were disappointed with the lack of details on the methodology and with the sanguine interpretation of model outputs without firm support on tenable assumptions.

We strongly encourage you to take the critiques below very seriously. The value of your paper to eLife readers will substantially increase if you are able to accommodate the many concerns that are transcribed below.

When resubmitting, please revise the title of your paper to reflect its focus on carcinogenesis or prediction of age-specific cancer incidence.

Separate reviews (please respond to each point and revise accordingly):

Reviewer #1:

I worry that many of the statements or presentations in this submission are imprecise or technically sloppy. These statements must be amended and backed by logic, a detailed explanation of the methods, and/or references to prior work.

In subsection “Quick guide to model”, this is written: "We simulate the assumed fixed fitness effects following the assumptions made in many modeling studies and by modern MMC theorists (Bozic et al., 2010; Tomasetti et al., 2015; Vogelstein et al., 2013)." Even if that point is clarified elsewhere in the paper, that statement is much too vague there to be acceptable.

In Figure 2A, the following is written: "Cells divide stochastically based on the last time a specific cell divided and the age-dependent cell division rate" and "Cell's relative chances of staying in the self-renewing pool over time depend on the niche space available, the number of competing cells and the cell's relative somatic fitness." Those statements in that figure are mathematically imprecise and unacceptable. They don't allow anything to be independently reproduced. Please revise to permit independent verification.

The Matlab code dump in Supplementary file 1 lacks details. The authors must provide enough explanatory text to explain their programming code. As it stands the presentation of the modeling procedures is rather cryptic. The discussions in the main text must be based on clear and detailed annotations to the code. The authors must create a dedicated section in Supplementary file 1 that is carefully and pedagogically written to explain the simulation steps.

Are the vertical axis scales in Figure 3 linear or logarithmic? Are the vertical axis scales in Figure 4 linear or logarithmic? In Figure 5, what is the numbering on the horizontal axes?

Reviewer #2:

This is a well-written and reasoned paper that develops and tests a mathematical model for understanding the observed rates of cancer incidence across diverse tissues/organs & species. Whilst I am not a mathematical modeller and am only superficially familiar with Matlab, I find the approaches used sensible and the assumptions underlying them valid overall. In my view the most important contribution of this manuscript is to highlight the non-cell-autonomous effect of ageing on somatic evolution and demonstrate how taking this into account can help better explain the observed cancer incidence. However, some of the assumptions made and inferences drawn will be open to criticism and also some known variables are not tested in the proposed models. Below I make some suggestions about how this could be addressed and also some other comments.

Major comments:

The assumption that the fitness advantage imparted by a mutation is constant is likely to be untrue in some instances. As HSCs are used as the model here, clonal haematopoiesis (CH) is a pertinent example. In CH, clonal expansions do not inexorably lead to clonal growth over time and in many instances clones that expand initially, stop expanding or even shrink later (e.g. Young et al., Nat Comms, 2016 and Abelson et al., Nature, 2018). It would be worth modelling the impact of this: i.e. will clonal behaviour differ if the fitness advantage fluctuates between 1.0 and 1.1 at different times, whilst averaging 1.05 (vs a constant advantage of 1.05).

Similarly, HSC or other stem cell divisions may be driven by intermittent life events (such as intercurrent illnesses /infections). Would such a fluctuating behaviour alter predictions or influence effects of drift in the author's models?

The concept of molecular synergy between mutations is not explored and this is also true of the concept of cellular transformation (often a consequence of powerful synergy). These are both well-established concepts operating in the evolution to CH to acute leukaemia. The most significant way in which these phenomena could influence the proposed models, is by achieving extremes of fitness advantage that go beyond the ranges explored here. These phenomena have been invoked to explain observations such as the peak in ALL incidence in early childhood in association with activated mutational processes (e.g. Swaminathan et al., Nat Immunol, 2015). These phenomena should at least be discussed if not modelled.

Minor comments:

The term "life history traits" should be explained/discussed early in the manuscript and in the context of life history theory. e.g. list some of these traits and mention that they are seen as determinants (through natural selection) of diverse organismal characteristics of a species.

The interaction between ageing and clonal expansion has been previously reported for clonal haematopoiesis in association with particular mutations (e.g. McKerrell et al., 2015) and a brief mention of this in Introduction would be helpful to readers.

The authors discuss the impact of ageing on clonal selection solely form the point of you of the ageing environment or niche. The potential impact of cell-intrinsic ageing of tissue stem cells should also be mentioned even if this does not affect modelling.

Estimates of the number of HSCs are controversial. The authors explain in Materials and methods that the specific number used here would not affect their model. In the relevant Results section, it would be worth referring readers to methods for this explanation. Similarly, the fact that the authors do take into account mutations other than nucleotide substitutions and also heritable epigenetic change should also be mentioned or alluded to before Materials and methods.

In the Introduction and Quick guide to model sections the authors discuss that "~50% of mutations accumulate before maturity". This is reportedly not the case in HSCs, which appear to harbour very few somatic variants in the first two decades of life (Welch et al., 2012). There is also evidence that in some individuals, mutational processes driven by DNA editing enzymes may augment the number of mutations. As HSCs are used as the model here, the authors should discuss this and mention whether/how it affects their calculations. Are they suggesting that purifying selection removes some/most of the more mutated HSCs If so, this would be controversial and thus requires more explanation or rethinking.

In the Introduction the phrase "… approximately the same age of incidence increase" is not clear and should be made clearer – e.g. "… approximately the same fractional increases in incidence with age".

In subsection “Quick guide to model” paragraph two, the statement "… always increase cellular somatic fitness" appears redundant when a driver mutation's driving potential is constant.

Figure 2A: legend should make it clear that the model refers to fate choices for a single cell.

Figure 2B: readers will notice that at age 0 the number of cells is very small (~1 cell). This is probably because age 0 refers to the fertilised zygote. This should be explained to avoid confusion.

Figure 3B: light and dark blue lines appear to have been switched in legend.
