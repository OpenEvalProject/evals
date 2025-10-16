# Author response - Round 1

Authors:
- Xiaoxuan Lin ([ORCID: 0000-0001-5356-9135](https://orcid.org/0000-0001-5356-9135))
- Patrick R Haller
- Navid Bavi
- Nabil Faruk
- Eduardo Perozo
- Tobin R Sosnick ([ORCID: 0000-0002-2871-7244](https://orcid.org/0000-0002-2871-7244))

## Response text

DOI: [10.7554/eLife.89635.3.sa4](https://doi.org/10.7554/eLife.89635.3.sa4)

The following is the authors’ response to the original reviews.

We thank the reviewers for their positive remarks. We have addressed the reviewers’ recommendations in the point-by-point response below to improve our revised manuscript.

Reviewer #1 (Recommendations For The Authors):

1. The authors carry out their HDX-MS work on Prestin (and SLC26A9) solubilized in glycol-diosgenin. The authors should carefully rationalize their choice of detergent and discuss how their key findings are also pertinent to the native state of Prestin when residing in an actual phospholipid bilayer. More native membrane mimetic models are available, for instance, nano-discs etc. While I am not insisting that the authors have to repeat their measurements in a more native membrane system, it would be a very nice control experiment, and in any case, a detailed discussion of the limitations of the approach taken and possible caveats should be included - possibly with additional references to other studies.

Response: We have added a paragraph rationalizing the choice of detergent in lines 174-176. We have also added requested HDX data comparing prestin reconstituted in nanodisc to prestin solubilized in micelle (Fig 5). The HDX for prestin under these two membrane mimetics were indistinguishable, including the anion-binding site, suggesting that our major findings are likely pertinent to prestin residing in a lipid bilayer. The only major HDX difference we observed was that a lipid-facing helix TM6 is more dynamic for prestin in nanodisc compared to in micelles. In our previous structural studies, we identified TM6 as the “eletromotile elbow” that is important for prestin’s mechanical expansion (Bavi et al., Nature, 2021). We are currently conducting a more thorough investigation to understand the role of TM6 in prestin’s electromotility.

1. As far as I understand, the HEPES state represents the apo-state and thus assumes that HEPES does not bind to Prestin - the authors should support this assumption or include a discussion of the possible effect of HEPES on Prestin. Also, the HEPES state has fewer time-points - this should also be discussed.

Response: We have included a discussion of the possible effects of HEPES in lines 331-345. In fact, in an attempt to support our assumption that HEPES does not bind to prestin, we set out to determine the structure of prestin in the HEPES-based buffer using single particle cryo-EM. However, we did not find evidence that HEPES binds to prestin. Details are discussed in lines 331-345 and Supporting Information Text 3.

We employed a denser sampling of HDX labeling times for prestin in Cl- because it is critical for fitting and ∆G calculation. The earlier time points are used mainly to evaluate the dynamics of the less stable cytosolic domain. Since the cytosolic domain does not directly participate in prestin’s voltage-sensing mechanism and electromotility, we only measured the HEPES states with longer time points which mainly probe the dynamics of the transmembrane domain.

1. Overall, the HDX-MS data provided and the statistical analysis done is in my view sufficiently detailed and well done - the authors are advised to make reference to and include a HDX Summary table and HDX Data Table according to the HDX-MS community-guidelines (Masson et al. Nature Methods 2019).

Response: An HDX summary table was provided in Table S1 and referred in lines 81 and 388. We have included a reference to Masson et al., Nature Methods, 2019, in line 389.

1. Figure 5 - I like the detailed analysis of the helix folding - but in my experience, one can provide a great fit of many HDX curves to a 4 -term exponential function - I think the authors would need more time-points to provide a more convincing case. But it does provide a compelling theory - even if the data strictly does not prove it. The authors should discuss this in more detail - including limitations etc.

Response: We presented a statistical analysis describing the accuracy of the fitting in Fig 6A. We acknowledge that the values of the exponentials may not be precisely determined, but the fundamental result is robust – TM3 exchanges through fraying from the N-terminal end of the helix while TM6 exchanges much more cooperatively. Collecting additional time points may reduce the error on the rates but would not contribute to additional mechanistic insights.

Reviewer #2 (Recommendations For The Authors):

1. I suggest toning down more speculative/ hypothetical aspects. Specifically, I believe that the following sentence should not be in the abstract in its present form: "This event shortens the TM3-TM10 electrostatic gap, thereby connecting the two helices such that TM3-anion-TM10 is pushed upwards by forces from the electric field, resulting in reduced cross-sectional area."

Response: The sentence has been rephrased.

1. The "nuance" between helix fraying and helix unfolding is an important aspect of the author's hypothesis but this should be explained better. In that regard, have the authors performed HDX-MS analysis of the mutant P136T? That would nicely support their claim regarding the importance of helix fraying as being foundational to allow electromotility.

Response: More explanation for helix fraying and unfolding has been provided in the main text.We have not performed HDX-MS analysis of the mutant P136T. However, we performed molecular dynamics simulations using Upside, and consistently, showed that a P136T mutation in prestin results in a highly stabilized TM3 (Fig. S4B).

1. Why do measurements at two pDs? Did the authors observe any differences?

Response: The purpose of two pDs is to increase the effective dynamic range of the HDX measurement by two orders of magnitude because the intrinsic exchange rate scales with pD & Temp. This allows us to determine the stability of both the highly and minimally stable regions within the protein. We have rephrased lines 83-87 to better rationalize this choice of pDs. With the time points performed in this study, we did not observe noticeable differences for HDX performed under the two pDs when corrected for the changes in the intrinsic rates (Fig. S7A).

1. I can't help but wonder what is the interest in doing HDX-MS measurements after 27h of incubation. Membrane proteins are known for their instability once purified and a few odd HDX profiles at that specific timepoint (especially in the 80-100 residues area) make one question whether local unfolding preceding aggregation could happen. This actually weakens the author's claims about cooperative unfolding and localized and directional helix fraying. Could they provide some evidence (CD, thermostability measurements such as trp fluorescence quenching, or SEC analysis) that the prestin is still folded after 27h in GDN.

Response: We appreciate reviewer’s comments on membrane proteins can be unstable once purified. In our system, we did not observe evidence of unfolding or aggregation caused by long-term incubation after purification. This is mostly supported by the fact that our HDX reactions were initiated and injected to MS in random order, yet are still highly reproducible among biological and technical replicates. A specific example included HDX on freshly purified SLC26A9 gave the same deuteration levels as SLC26A9 purified in GDN after 4 days. For prestin, although we don’t have direct comparison between fresh samples and old samples (24-27h post-purification) due to the lack of samples, 30s HDX in SO42- performed 24h post-purification gave a %D that fell between 10s and 90s of labeling done on fresh sample. Additionally, HDX on prestin in Cl- performed on freshly purified sample gave the sample %D as prestin in the presence of 1M urea labeled after 24~48h of purification, suggesting that prestin is relatively resistant to aggregation at least within 48h after purification even in the presence of 1 M urea (data not shown).

Furthermore, the HDX for prestin in nanodisc are essentially identical to prestin in micelles except for a functionally important helix (TM6), suggesting minimal aggregation or misfolding.

We think the “a few odd HDX profiles” at 27h time points for residues 80-100 are caused by two reasons. Firstly, TM1 unfolds cooperatively and its stability in HEPES falls within the detection range when long labeling time points were employed (within one log unit of 27h). Secondly, we observed two non-interconverting and structurally distinct populations for TM1 (Supporting Information Text 1 & Fig. S8), and in long labeling times, the two isotope distributions merge and sometimes can skew the %D calculations. Nevertheless, the HDX differences we observed comparing across conditions are clear and such %D calculation skewing, if present, should be minimal and does not change our main conclusions.
