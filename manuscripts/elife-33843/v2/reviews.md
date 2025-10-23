# Peer review - Round 1

Editors:
- Tanya T. Whitfield, University of Sheffield United Kingdom

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.33843.042](https://doi.org/10.7554/eLife.33843.042)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Segmentation of the zebrafish axial skeleton relies on notochord sheath cells and not on the segmentation clock" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor (Tanya Whitfield) and Didier Stainier as the Senior Editor. The following individual involved in review of your submission has agreed to reveal his identity: Matthew Harris (Reviewer #1).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission

Summary:

Lieras-Forero et al. detail quite novel and important findings on the independent patterning role of the notochord in segmentation of the zebrafish vertebral column in a process that is independent of somite formation. The wavefront model has been accepted as the conserved mechanism by which segmentation in vertebrate organisms occurs. It is/was generally assumed, however, that in fishes the meristic patterning is determined by a wavefront model as shown in beginning mutants in regulators of this patterning mechanism. The authors clearly, and elegantly, demonstrate underlying capacity of the zebrafish notochord to form ordered, meristic array of vertebral bodies even in the case of dysfunctioning segmental patterning in the sclerotome. These data build on classic comparative anatomy and recent genetic data that point to patterning of the chordacentra and the notochord as a key, and ancestral, step to the formation of vertebrae and patterning of the vertebral column. The authors further develop and test a mathematical model that is sufficient to explain the interaction between the dual patterning systems that can explain a number of characteristics seen in the adult phenotypes caused by different mutant combinations.

Essential revisions:

Both reviewers were positive overall, but each had suggestions for improvement. In particular, there are several concerns over the modelling aspect of the paper. Please address the following as essential revisions:

1) Please address all issues raised by both reviewers concerning the mathematical model.

2) Please address the issues concerning the genetic analysis and nomenclature raised by reviewer 1.

3) Please use the Discussion section to set your work in a broader context (see comments and suggestions from reviewer 1).

Reviewer #1:

The findings detailed by this paper are quite interesting and are important for developmental biologists broadly. The paper is very well written, and beyond some small (but essential) comments/critiques that I hope will be taken under consideration to increase the accuracy and impact of the manuscript, I believe it will be a landmark paper.

Genetics:

– Do new alleles generated/described in this manuscript fail to complement the previous described alleles? How do the authors know that these are nulls or severe loss-of-function? The position in of the TALEN alleles would support potential gene fragments to be produced. Similarly, what genetic characterization has been done on the Tilling alleles of her1 and her7 to see if these are true loss-of-function. Some discussion/exploration of characterization of these alleles in the paper would be helpful, however as the phenotype is what is critical in this manuscript, no extensive genetic analysis is necessary to be undertaken to address these questions.

– Giving triple mutants different mutant names is not commonly accepted by the field, nor is it helpful. Gollum, or bachau are not a single locus as the names would suggest. This is quite confusing and severely complicates conceptual understanding of comparisons between the compound mutants. This detracts from an otherwise exceptional and elegantly performed study.

Modeling

– The generation of the reaction diffusion model to integrate the notochordal and somatic patterning events is quite helpful and at least supplemental figure 14 should be in the paper. This is critical.

– The model shows only resting states. Please comment in the text if the model can reproduce the ontological sequence of patterning as shown in this paper (e.g. does it replicate a rostral bias?). Also, does the model cause fill-in responses to perturbations as seen in the mutant phenotypes.

– Subsection “Disruption of the segmentation clock in double and triple mutants” The authors may want to integrate the fact that the reaction diffusion mechanism provides plasticity by the feedback characteristics of the interactions.

Phylogenetic character analysis of notochord induction/association of the chordacentrum.

– At several points the authors detail current thinking of chordacentrum involvement in patterning of the vertebra column and formation of the centra. It would be important, and clarifying, if the authors discuss classical work in basal teleosts such as Amia and Gar suggesting that notochord induction/association of a chordacentrum is ancestral in teleosts (Schultze and Arratia papers in the 1980s) and addressed in Laern, (1976). How much of the discordance between models/species that the authors mention represents different mechanisms or, alternatively, similar mechanisms studied at different levels of analysis?

Reviewer #2:

In this study Forero et al., investigate the role of the segmentation clock in patterning chordacentra in zebrafish. Using a family of segmentation clock mutants, they disrupt segmentation to varying degrees and measure the chordacentra pattering. They propose a model in which the periodic patterning of chordacentra arises from a pattering process that can function independently from the segmentation clock. However, the somite patterns can modify the chordacentra patterning mechanism.

My major issue is that the model ought to generate periodic patterning of chordacentra in the absence of somitogenesis clock input. If the proposed model can do this robustly then some elementary exploration of this case is necessary (i.e. a minimum requirement is to provide enough detail so the results are reproducible and verify that there is a robust patterning mechanism in the case of no sinks). This validation is crucial as later the authors use the model to explain the location of activator peaks relative to sinks.

1) The authors claim that 'in the absence of any sinks, the notochord would in our model segment without any defects with a periodicity determined entirely by the internal dynamics.'

The key figure supporting this statement (Figure 14E) indicates that the mathematical model produces spatially periodic patterns at steady state in the absence of dermatome signal (i.e. s(x)=0 for all x).

It is not adequately explained in the text how the proposed model does this. What is the patterning mechanism?

A standard way to analyse the model is to consider behavior without diffusion. What are the steady states and what is their linear stability?

My analysis suggests that in the absence of diffusion and with s0<1-d (i.e. small influence from the dermatome) there is a unique steady state (0,0) that is stable.

When s0>1-d the origin becomes unstable and there are two non-zero steady states (i.e. presumably the model becomes bistable in this regime).

This analysis is consistent with the authors numerical results; the spatially homogeneous steady state is destabilized in simulations where the sink strength is greater than 0.5. Outside of this region the spatially homogeneous steady state is monostable.

Given the case where s0=0 is stable, the question then is whether the introduction of diffusion could cause an instability (e.g. Turing) and hence periodic patterning. If this is the case the authors should show it. However, even if this were true the wavefront behavior presented by the authors is nontrivial.

I have tried to reproduce Figure 14E with my own code and as many of the details provided but cannot.

2) The PDE model has a parameter that is discontinuous in space. The authors ought to provide details of their discretisation scheme so that the reader can assess how they have dealt with this discontinuity.

I suggest the following improvement: define the sinks independently of the numerical mesh and then approximate the steep switches with a continuous function such as tanh. In this way the sink strength parameter can be guaranteed to be continuous.

3) Stability analysis – is the pattering mechanism robust to small perturbations? It is worrying that the authors initialise on an unstable steady state of the homogeneous problem. Hence an infinitesimally small perturbation from these initial conditions could result in completely different model behaviour.

Could the authors add some small amplitude noise to the initial conditions and present some numerical results. Is the proposed wavefront solution stable?

4) The use of Fitzhugh Nagumo ought to be justified. I am not suggesting that the model needs to be linked to a molecular detail but some insight into the various terms would be helpful. The authors should describe the model assumptions and how they might be relevant to this system.

5) “In the simulations of fss, guu, and fum this strict correspondence between sink and activator is lost (Figure 7B and C); activator peaks occur both together with sinks and in between them.”

Can the authors use the model to provide insight into how this can happen? Is this observation a generic feature of activator-inhibitors models? If it is generic, then showing results from other reaction-diffusion models would help. If it is not generic, then the properties of the proposed model that yield the interesting behaviour ought to be defined and investigated more thoroughly.

6) Given the mathematical model takes up almost two pages of the results then I suggest that a figure exploring the relevant features of the model is appropriate.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Segmentation of the zebrafish axial skeleton relies on notochord sheath cells and not on the segmentation clock" for further consideration at eLife. Your revised article has been evaluated by Didier Stainier (Senior editor), Tanya Whitfield (Reviewing editor), and two reviewers.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance. Reviewer 1 only has minor concerns that will be quick to address. Reviewer 2 has some more substantial concerns regarding robustness of the system to small perturbations. The reviewer has given comments together with two video files. Please address the comments from both reviewers.

Reviewer #1:

In the text the authors often list fss, her1;her7, and tbx6;her1;her7 mutant combinations. I assume the fss allele of tbx6 is the one being used (unless another has been generated). If this is the case the text should reflect this as tbx6-/-. her1; her7, tbx6;her1;her7 mutants. The authors have correctly labeled this in the figures, but not the figure legends nor text.

Somewhere in the text the authors should address whether these alleles are thought to be null or strong loss-of-function. Data is not needed, rather citation of previous genetic analysis on available alleles and a statement in the text is just helpful.

Results section “A reaction-diffusion model of axial patterning in the zebrafish”: “intrinsic segmentation mechanism, likely sheath cells" Sheath cells is not a mechanism. Do the authors mean within sheath cells?

Reviewer #2:

1) Whilst the theory section has been improved, now that it is explicit that the authors are proposing the Turing mechanism as the underlying patterning mechanism, can they provide a fuller analysis of the unstable wavenumbers for the parameter values presented in the simulations? It is important to characterize how the unstable wavenumbers (and corresponding wavelengths) relate to the typical inter-sink distance (e.g. presumably the model parameters have been chosen to give a wavenumber that is approximately of the same order as the inter-sink distance).

2) As the authors did not present the results with arbitrarily small noise in the initial data as I requested, I have solved the equations myself.

In Noise.mp4 I solve the model as it is presented in the paper. Note that the key qualitative behaviour is that independent of somite signal, a propagating wavefront leaves a periodic pattern in its wake. This is the behavior observed experimentally that any reasonable model ought to replicate.

In NoNoise.mp4 I have added very low amplitude noise to the initial conditions. Note that the noise destabilises the wavefront solution and the domain patterns simultaneously rather than sequentially.

These numerical results indicate that even the addition of infinitesimally small noise throughout the domain results in the wavefront solution being lost. Given the presence of noise in biological systems, this robustness issue is a fundamental limitation that, by not addressing in the main text of the manuscript, the authors seem to have neglected.

I suggest the following:

i) The authors build a convincing case, with reference to the pattern formation literature, that deals with the robustness issue. i.e. are there other published examples of wavefront propagation mediated spatial patterning with a similar lack or robustness?

or

ii) The authors build on their proposal that robustness could be mediated by a maturation gradient. This could be incorporated into the model by considering a competency domain where the authors solve the reaction diffusion equations on some domain [0, s(t)] where s(t) is a suitably chosen function of time.

Such a model would have a fundamentally different behaviour in that the imposed wavefront would determine the speed of segmentation rather than the Turing instability. Moreover, it would be robust to infinitesimally small noise.

For the suggested approach the authors could see, for example, Madzvamuse et al., 2005 or Crampin et al., 2002.
