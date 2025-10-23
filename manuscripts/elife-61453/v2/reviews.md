# Peer review - Round 1

Editors:
- Hannes Neuweiler, University of Würzburg Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.61453.sa1](https://doi.org/10.7554/eLife.61453.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

Mutation of the superoxide dismutase is implicated in motor neuron disease. The enzyme contains both zinc (Zn) and copper (Cu) as cofactors. The role that either Zn or Cu play in membrane association and disease-causing aggregation of superoxide dismutase is currently unclear. The authors apply site-directed mutagenesis to generate Zn-only and Cu-only binding mutants of the enzyme and untangle the effect that the binding of each cofactor has on membrane association and aggregation. Through application of a large set of complementary techniques, involving statistical mechanical modelling, fluorescence and infra-red spectroscopy, and optical and atomic force microscopy, the authors show that deficiency of Zn uptake, induced by mutation, is a major driving force for toxic aggregation of superoxide dismutase.

Decision letter after peer review:

Thank you for submitting your article "Metal cofactor zinc and interacting membranes modulate SOD1 conformation-aggregation landscape in an in vitro ALS Model" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Olga Boudker as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Erdinc Sezgin (Reviewer #2).

The reviewers have discussed the reviews with one another. They acknowledge the integrated approach taken by you and your co-authors and the amount of data presented and discussed. However, the reviewers raise major concerns regarding both experiments and computer simulations. Not all conclusions are justified by the data presented and additional data are required. We ask you to revise your manuscript in light of the reviewers' concerns.

As the editors have judged that your manuscript is of interest, but as described below that additional experiments are required before it is published, we would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). First, because many researchers have temporarily lost access to the labs, we will give authors as much time as they need to submit revised manuscripts. We are also offering, if you choose, to post the manuscript to bioRxiv (if it is not already there) along with this decision letter and a formal designation that the manuscript is "in revision at eLife". Please let us know if you would like to pursue this option. (If your work is more suitable for medRxiv, you will need to post the preprint yourself, as the mechanisms for us to do so are still in development.)

Reviewer #1:

Sannigrahi et al. report the investigation of structural determinants of membrane insertion and aggregation of Cu-Zn superoxide dismutase (SOD1), an enzyme that is implicated in motor neuron disease. The authors combine mutagenesis experiments with a variety of techniques, involving tryptophan fluorescence, FTIR, AFM, Tht fluorescence, FCS, optical microscopy and computer simulation. They arrive at that conclusion that conformational change and site-specific metal binding modulate membrane insertion and aggregation of SOD1.

Identifying the origins of SOD1 dysfunction and aggregation can have important implications in the development of therapeutic strategies for motor neuron disease. The underlying molecular biology is not well understood. The study by Sannigrahi et al. is an integrated approach involving an impressive number of complementary methods. However, the conclusions put forward are not sufficiently supported by the data presented. The applied methodologies yield data of insufficient resolution to draw the detailed molecular picture presented. Additional experimental work would be required to substantiate or provide evidence for the findings.

1. The statistical mechanical model (WSME) is coarse-grained. It e.g. considers three consecutive amino acid residues as a block. It is therefore of limited suitability to study the effects of single-point mutations and metal-binding or conformation and aggregation.

2. The effect of mutation and Zn/Cu-binding on Trp fluorescence spectral properties of SOD1 is marginal (Figure 2a). Likewise, the far-UV CD spectra shown in supporting information show marginal changes. The broad spectral characteristics of far-UV CD defies an accurate, quantitative deconvolution of secondary structure content. No solid conclusions concerning a conformational change can thus be inferred. FTIR spectra are broad and smooth (i.e. lack significant sub-structure) (Figure 2b, c). Their deconvolution in seven discrete sub-states appears ambitious and error-prone.

3. The authors propose to determine membrane affinities of SOD1 and mutants thereof by applying extrinsic fluorescence modification and by measuring binding to artificial micelles using fluorescence correlation spectroscopy (analysis of diffusion time constants). Extrinsic fluorescence labels are hydrophobic compounds and supposedly tend to strongly interact with membrane lipids. This will provides an artificial bias of conjugates to micelle membranes. Control experiments are required to rule out effects of the labels.

4. The influence of mutation on stability and conformation of SOD1 is unclear. Mutations H72F and H121F, introduced to alter metal binding, may as well have effects on stability and conformation (folding) of the entire domain, irrespective of the metal-bound/unbound state. Mutation itself may lead to unfolding and aggregation. Mutation of a histidine to a phenylalanine, as applied by the authors, may have disruptive effects on protein structure because a small side chain is replaced by a larger one. Thermal and/or chemical denaturation experiments, carried out on isolated protein material and mutants thereof, and their analysis are required to assess the effect of mutations on folding and stability.

Reviewer #2:

In this manuscript, Sannigrahi et al. studied the role of metal binding sites of SOD1 on its aggregation and toxicity. They created a Zn only, Cu only binding mutants as well as Zn/Cu binding-deficient mutant. Zn bearing mutant behaved similarly as wild type protein in terms of membrane binding, aggregate formation and toxicity, while Zn/Cu deficient mutant behaved similarly to Cu bearing (no Zn) mutant. They conclude that Zn binding pocket is crucial to keep the protein in healthy state and in the absence of Zn binding, protein aggregates especially in the presence of membranes. Lastly, they investigated real disease mutations and samples two mutations with different degree of Zn binding, and confirmed the same trend; if the Zn binding pocket is influenced, mutation is more severe.

I am not an expert of this particular biological question (ALS and role of SOD1), but I evaluated the technical aspects of the manuscript.

In general, the manuscript is well written, the messages are clear and the conclusions are supported by data.

Reviewer #3:

This paper looks at the effect of metal cofactor binding on the aggregation and toxicity of SOD1, which natively binds a Cu2+ and a Zn2+ ion. The authors investigate the WT SOD1, the apo SOD1 and two mutants which do not bind Cu2+ (H121F) or Zn2+ (H72F) in order to look at the effects of the metal binding on SOD aggregation and toxicity. They find by a number of assays and a computational study that Zn2+ rather than Cu2+ is the dominant factor in determining susceptibility to aggregation, membrane binding, etc. Based on this they propose that deficient Zn2+ uptake by SOD1 is responsible for the pathogenic behaviour of some mutants.

There is a lot of interesting data in this paper supporting this hypothesis (some more so than others), however there are some points the authors should consider:

1. A potential weakness of the computational estimation of membrane binding affinity is that the WT crystal structure was used for WT, while structure predictions from the I-TASSER server were used for apo and Cu/Zn-deficient mutants. Since one might expect the predicted structure to be of lower quality, it might then have an enhanced propensity for membrane binding via exposed hydrophobic groups? What would be obtained if the I-TASSER server was also used to generate the structure used for WT in this calculation? This point also applies to the computational validation where predicted membrane binding free energies are compared with distance to the Zn2+ or Cu2+ site of the mutants. This again involves a 2-stage prediction – firstly of the mutant structure, then of its binding energy. Maybe the authors can give some intuition as to how this can be sufficiently accurate to be useful?

2. Correlation functions for A488-SOD1 are shown are at the extremes of no SUVs versus a high concentration of SUVs. What happens at intermediate concentrations where there would be more of a mix of bound and unbound populations – can the two components be clearly resolved in the log-linear plots of G(tau)?

3. I may have missed something, but why does the population of membrane-bound protein saturate at much less than 100%? Is there a baseline parameter for the population at high [DPPC SUV] in addition to Ka? One thing that occurred to me is that membrane binding may quench the fluorescence somewhat, so the amplitude of the membrane-bound population may be lower than it should be, hence this effect; and the differences in folding/misfolding of the SOD mutants may lead to different binding to the SUVs which would in turn affect the relative amplitudes of the two components. This wouldn't affect the fit of the sigmoidal curves, but maybe the relative fraction of slowly diffusing component should not be literally interpreted in terms of a bound population. Rather than "population membrane bound" Figure 2f could say "Fraction bound fluorescence" or similar? This interpretation would support the authors' contention that H72F is more apo-like and H121F more holo-like.

4. The differences in the ratio Ksvm/Ksv are basically reflecting differences in Ksv, because the values of Ksvm are all very similar. Thus it may reflect more the differences in non membrane-bound protein than differences in membrane binding, as seems to be the inference in the paper?

5. The finding of change in secondary structure on membrane binding based on IR data, in particular increase in alpha-helical population, for the apo form and the H72F, is very interesting and strongly supports differences in membrane interaction between WT/H121F and apo/H72F – maybe this data should be included in the main text rather than the SI in fact? To me this seems a more noteworthy change than the modest differences in membrane association constants obtained from FCS.

6. Aggregation was studied for the reduced form of the disulfides. The authors should motivate why the aggregation is studies using the reduced form of the protein while the prior work in the paper used the oxidized form (I believe?). My knowledge in this area is limited so I'm not sure which is the form more relevant to observed pathologies.

7. A complicating factor in the perturbation of GUV membranes by the aggregates formed with/without SUVs present is the SUVs themselves. Presumably there is a significant SUV concentration in the aliquots taken from the aggregation reaction – could the SUVs rather than differences in the aggregates be responsible for the difference in the effect on GUVs? A control could be to add just SUVs to the GUV samples.

8. For the validation, a statistical test should be used to demonstrate the significance of the observed correlations.
