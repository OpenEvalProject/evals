# Peer review - Round 1

Editors:
- Lipi Thukral, CSIR-Institute of Genomics and Integrative Biology India

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.105111.3.sa0](https://doi.org/10.7554/eLife.105111.3.sa0)

This important study provides information on the TMEM16 family of membrane proteins, which play roles in lipid scrambling and ion transport. By simulating 27 structures representing five distinct family members, the authors captured hundreds of lipid scrambling events, offering insights into the mechanisms of lipid translocation and the specific protein regions involved in these processes. While the data on comparison of scrambling competence is compelling, the evidence for outside-the-groove scramblase activity without experimental validation is missing and is based on a limited set of observed events.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.105111.3.sa1](https://doi.org/10.7554/eLife.105111.3.sa1)

Summary:

The manuscript investigates lipid scrambling mechanisms across TMEM16 family members using coarse-grained molecular dynamics (MD) simulations. While the study presents a statistically rigorous analysis of lipid scrambling events across multiple structures and conformations, several critical issues undermine its novelty, impact, and alignment with experimental observations.

Review on revised version:

The referee notes that the authors, in their response letter, have concurred with most of the concerns originally raised. Specifically, the authors acknowledge the referee's view that the manuscript primarily confirms previously reported findings and does not present a significantly novel advance, particularly regarding the central observation of groove-mediated lipid scrambling in the open Ca²⁺-bound TMEM16 structures. The authors have also acknowledged the potential discrepancies with existing experimental studies and have addressed this point candidly through additional discussion. Furthermore, the referee appreciates that the authors have echoed the concern regarding the limited statistical robustness of the observed scrambling events.

Given that the authors have essentially affirmed the key points raised in the initial review, the referee believes that these acknowledgements reinforce the basis of the original assessment. Therefore, the referee maintains the original opinion that, despite its technical merits and useful discussion made in the revised version, the manuscript does not offer sufficient novelty or mechanistic depth.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.105111.3.sa2](https://doi.org/10.7554/eLife.105111.3.sa2)

Summary:

Stephens et al. present a comprehensive study of TMEM16-members via coarse-grained MD simulations (CGMD). They particularly focus on the scramblase ability of these proteins and aim to characterize the "energetics of scrambling". Through their simulations, the authors interestingly relate protein conformational states to membrane's thickness and link those to the scrambling ability of TMEM members, measured as the trespassing tendency of lipids across leaflets. They validate their simulation with a direct qualitative comparison with Cryo-EM maps.

Strengths:

The study demonstrates an efficient use of CGMD simulations to explore lipid scrambling across various TMEM16 family members. By leveraging this approach, the authors are able to bypass some of the sampling limitations inherent in all-atom simulations, providing a more comprehensive and high-throughput analysis of lipid scrambling. Their comparison of different protein conformations, including open and closed groove states, presents a detailed exploration of how structural features influence scrambling activity, adding significant value to the field. A key contribution of this study is the finding that groove dilation plays a central role in lipid scrambling. The authors observe that for scrambling-competent TMEM16 structures, there is substantial membrane thinning and groove widening. The open Ca2+-bound nhTMEM16 structure (PDB ID 4WIS) was identified as the fastest scrambler in their simulations, with scrambling rates as high as 24.4 {plus minus} 5.2 events per μs. This structure also shows significant membrane thinning (up to 18 Å), which supports the hypothesis that groove dilation lowers the energetic barrier for lipid translocation, facilitating scrambling.

The study also establishes a correlation between structural features and scrambling competence, though analyses often lack statistical robustness and quantitative comparisons. The simulations differentiate between open and closed conformations of TMEM16 structures, with open-groove structures exhibiting increased scrambling activity, while closed-groove structures do not. This finding aligns with previous research suggesting that the structural dynamics of the groove are critical for scrambling. Furthermore, the authors explore how the physical dimensions of the groove qualitatively correlate with observed scrambling rates. For example, TMEM16K induces increased membrane thinning in its open form, suggesting that membrane properties, along with structural features, play a role in modulating scrambling activity.

Another significant finding is the concept of "out-of-the-groove" scrambling, where lipid translocation occurs outside the protein's groove. This observation introduces the possibility of alternate scrambling mechanisms that do not follow the traditional "credit-card model" of groove-mediated lipid scrambling. In their simulations, the authors note that these out-of-the-groove events predominantly occur at the dimer interface between TM3 and TM10, especially in mammalian TMEM16 structures. While these events were not observed in fungal TMEM16s, they may provide insight into Ca2+-independent scrambling mechanisms, as they do not require groove opening.

Weaknesses:

A significant challenge of the study is the discrepancy between the scrambling rates observed in CGMD simulations and those reported experimentally. Despite the authors' claim that the rates are in line experimentally, the observed differences can mean large energetic discrepancies in describing scrambling (larger than 1kT barrier in reality). For instance, the authors report scrambling rates of 10.7 events per μs for TMEM16F and 24.4 events per μs for nhTMEM16, which are several orders of magnitude faster than experimental rates. While the authors suggest that this discrepancy could be due to the Martini 3 force field's faster diffusion dynamics, this explanation does not fully account for the large difference in rates. A more thorough discussion on how the choice of force field and simulation parameters influence the results, and how these discrepancies can be reconciled with experimental data, would strengthen the conclusions. Likewise, rate calculations in the study are based on 10 μs simulations, while experimental scrambling rates occur over seconds. This timescale discrepancy limits the study's accuracy, as the simulations may not capture rare or slow scrambling events that are observed experimentally and therefore might underestimate the kinetics of scrambling. It's however, important to recognize that it's hard (borderline unachievable) to pinpoint reasonable kinetics for systems like this using the currently available computational power and force field accuracy. The faster diffusion in simulations may lead to overestimated scrambling rates, making the simulation results less comparable to real-world observations. Thus, I would therefore read the findings qualitatively rather than quantitatively. An interesting observation is the asymmetry observed in the scrambling rates of the two monomers. Since MARTINI is known to be limited in correctly sampling protein dynamics, the authors, in order to preserve the fold, have applied a strong (500 kJ mol-1 nm-2) elastic network. However, I am wondering how the ENM applies across the dimer and if any asymmetry can be noticed in the application of restraints for each monomer and at the dimer interface. How can this have potentially biased the asymmetry in the scrambling rates observed between the monomers? Is this artificially obtained from restraining the initial structure, or is the asymmetry somehow gatekeeping the scrambling mechanism to occur majorly across a single monomer? Answering this question would have far-reaching implications to better describe the mechanism of scrambling.

Notably, the manuscript does not explore the impact of membrane composition on scrambling rates. While the authors use a specific lipid composition (DOPC) in their simulations, they acknowledge that membrane composition can influence scrambling activity. However, the study does not explore how different lipids or membrane environments or varying membrane curvature and tension, could alter scrambling behaviour. I appreciate that this might have been beyond the scope of this particular paper and the authors plan to further chase these questions, as this work sets a strong protocol for this study. Contextualizing scrambling in the context of membrane composition is particularly relevant since the authors note that TMEM16K's scrambling rate increases tenfold in thinner membranes, suggesting that lipid-specific or membrane-thickness-dependent effects could play a role.

Comments on revisions:

I have carefully reviewed the replies of the author, which address the points I raised and improved the manuscript by making the changes outlined in their response. Particularly, I am pleased to see that the authors report ensemble averages in Figure 1-supplement 1 and add relevant information in a newly created table. I welcome the refinement of the discussion towards a cautionary approach in describing quantitatively the findings of experiments and computations for what concerns scrambling rates. I still feel that proper statistical analysis to compare the distributions in Figure 3-figure supplement 6 would have made the points claimed even stronger, but - at the same time - I do see the points of the authors in commenting the differences between these distributions more qualitatively. Overall, I support the publication of this manuscript, it has been a pleasure to read it.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.105111.3.sa3](https://doi.org/10.7554/eLife.105111.3.sa3)

Summary:

The paper investigates the TMEM16 family of membrane proteins, which play roles in lipid scrambling and ion transport. A total of 27 experimental structures from five TMEM16 family members were analyzed, including mammalian and fungal homologs (e.g., TMEM16A, TMEM16F, TMEM16K, nhTMEM16, afTMEM16). The identified structures were in both Ca²⁺-bound (open) and Ca²⁺-free (closed) states to compare conformations and were preprocessed (e.g., modeling missing loops) and equilibrated. Coarse-grain simulations were performed in DOPC membranes for 10 microseconds to capture the scrambling events. These events were identified by tracking lipids transitioning between the two membrane leaflets and they analysed correlation between scrambling rates, in addition, structural properties such as groove dilation and membrane thinning were calculated. They report 700 scrambling events across structures and the figure 2 elaborates on how open structures show higher activity, also as expected. The authors also address how structures may require open groove, this and other mechanisms around scrambling is a bit controversial in the field.

Strengths:

The strength of this study emerges from comparative analysis of multiple structural starting points and understand global/local motions of the protein with respect to lipid movement. Although the protein is well-studied, both experimentally and computationally, the understanding of conformational events in different family members, especially membrane thickness less compared to fungal scramblases offers good insights.

Weaknesses:

The weakness of the work is to fully reconcile with experimental evidence of Ca²⁺-independent scrambling rates observed in prior studies, but this part is also challenging using coarse-grain molecular simulations. Previous reports have identified lipid crossing, packing defects and other associated events, so it is difficult to place this paper in that context. However, the absence of validation leaves certain claims, like alternative scrambling pathways, speculative.
