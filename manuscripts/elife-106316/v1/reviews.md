# Peer review - Round 1

Editors:
- Claude Desplan, https://ror.org/0190ak572 New York University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.106316.2.sa0](https://doi.org/10.7554/eLife.106316.2.sa0)

This valuable manuscript uses mathematical modeling to address the synchrony of the vertebrate segmentation clock with the developmental processes. The authors use convincing arguments to support the idea that this would allow the evolution of flexible body plans and a variable number of segments. This manuscript could be of interest to developmental biologists and systems biologists.

[Editors' note: this paper was reviewed by Review Commons.]


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.106316.2.sa1](https://doi.org/10.7554/eLife.106316.2.sa1)

Summary:

In this manuscript, Hammond et al. study robustness of the vertebrate segmentation clock against morphogenetic processes such as cell ingression, cell movement and cell division to ask whether the segmentation clock and morphogenesis are modular or not. The modularity of these two would be important for evolvability of the segmenting system. The authors adopt a previously proposed 3D model of the presomitic mesoderm (Uriu et al. 2021 eLife) and include new elements; different types of cell ingression, tissue compaction and cell cycles. Based on the results of numerical simulations that synchrony of the segmentation clock is robust, the authors conclude that there is a modularity in the segmentation clock and morphogenetic processes.

The presented results support the conclusion. The manuscript is clearly written.

Major comments from the original round of review:

[Optional] In both the current model and Uriu et al. 2021, coupling delay in phase oscillator model is not considered. Given that several previous studies (e.g. Lewis 2003, Herrgen et al. 2010, Yoshioka-Kobayashi et al. 2020) suggested the presence of coupling delays in Delta-Notch signaling, could the authors analyze the effect of coupling delay on robustness of the segmentation clock against morphogenetic processes?

Significance:

Synchronization of the segmentation clock has been studied by mathematical modeling, but most previous studies considered cells in a static tissue without morphogenesis. In the previous study by Uriu et al. 2021, morphogenetic processes such as cell advection due to tissue elongation, tissue shortening, and cell mobility were considered in synchronization. The current manuscript provides methodological advances in this aspect by newly including cell ingression, tissue compaction and cell cycle. In addition, the authors bring a concept of modularity and evolvability to the field of the vertebrate segmentation clock, which is new. On the other hand, the manuscript confirms that the synchronization of the segmentation clock is robust by careful simulations, but it does not propose or reveal new mechanisms for making it robust or modular. The main targets of the manuscript will be researchers working on somitogenesis and evolutionary biologists who are interested in evolution of developmental systems. The manuscript will also be interested by broader audiences, like developmental biologists, biophysicists, and physicists and computer scientists who are working on dynamical systems.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.106316.2.sa2](https://doi.org/10.7554/eLife.106316.2.sa2)

Summary:

The manuscript from Hammond et al., investigates the modularity of the segmentation clock and morphogenesis in early vertebrate development, focusing on how these processes might independently evolve to influence the diversity of segment numbers across vertebrates.

Methodology: The study uses a previously published computational model, parameterized for zebrafish, to simulate and analyse the interactions between the segmentation clock and the morphogenesis of the pre-somitic mesoderm (PSM). Their model integrates cell advection, motility, compaction, cell division, and the synchronization of the embryo clock. Three alternative scenarios of PSM morphogenesis were modeled to examine how these changes affect the segmentation clock.

Model System: The computational model system combines a representation of cell movements and the phase oscillator dynamics of the segmentation clock within a three-dimensional horseshoe-shaped domain mimicking the geometry of the vertebrate embryo PSM. The parameters used for the mathematical model are mostly estimated from previously published experimental findings.

Key Findings and Conclusions: (1) The segmentation clock was found to be broadly robust against variations in morphogenetic processes such as cell ingression and motility; (2) Changes in the length of the PSM and the strength of phase coupling within the clock significantly influenced the system's robustness; (3) The authors conclude that the segmentation clock and PSM morphogenesis exhibited developmental modularity (i.e. relative independence), allowing these two phenomena to evolve independently, and therefore possibly contributing to the diverse segment numbers observed in vertebrates.

Major comments from the original round of review:

(1) The key conclusion drawn by the authors (that there is robustness, and therefore modularity, between the morphogenetic cellular processes modeled and the embryo clock synchronization) stems directly from the modeling results appropriately presented and discussed in the manuscript.

The model comprises some strong assumptions, however all have been clearly explained and the parameterization choices are supported by experimental findings, providing biological meaning to the model. Estimated parameters are well explained, and seem reasonable assumptions (from the embryology perspective).

(2) This study, as is, achieves its proposed goal of evaluating the potential robustness of the embryo clock to changes in (some) morphogenetic processes. The authors do not claim that the model used is complete, and they properly identify some limitations, including the lack of cell-cell interactions. Given the recognized importance of cellular physical interactions for successful embryo development, including them in the model would be a significant addition in future studies.

(3) The authors have deposited all the code used for analysis in a public GitHub repository that is updated and available for the research community.

(4) In page 6, the authors justify their choice of clock parameters for cells ingressing the PSM: "As ingressing cells do not appear to express segmentation clock genes (Mara et al. (2007)), the position at which cells ingress into the PSM can create challenges for clock patterning, as only in the 'off' phase of the clock will ingressing cells be in-phase with their neighbors."

However, there are several lines of evidence (in chick and mouse), that some oscillatory clock genes are already being expressed as early as in the gastrulation phase (so prior to PSM ingression) (Feitas et al, 2001 [10.1242/dev.128.24.5139]; Jouve et al, 2002 [10.1242/dev.129.5.1107]; Maia-Fernandes at al, 2024 [10.1371/journal.pone.0297853]).

Question: Is this also true in zebrafish? (I.e. is there any recent experimental evidence that the clock genes are not expressed at ingression, since the paper cited to support this assumption is from 2007).

If they are expressed in zebrafish (as they are in mouse and chick), then the cell addition should have random clock gene periods when they enter the PSM and not start all with a constant initial phase of zero. Probably this will not impact the results since the cells will also be out of phase with their neighbors when they "ingress", however, it will model more closely the biological scenario (and avoid such criticism).

Significance:

GENERAL ASSESSMENT

This study uses a previously published model to simulate alternative scenarios of morphogenetic parameters to infer the potential independence (termed here modularity) between the segmentation clock and a set of morphogenetic processes, arguing that such modularity could allow the evolution of more flexible body plans, therefore partially explaining the variability in the number of segments observed in the vertebrates. This question is fundamental and relevant, yet still poorly researched. This work provides a comprehensive simulation with a model that tries to simplify the many morphogenetic processes described in the literature, reducing it to a few core fundamental processes that allow drawing the conclusions sought. It provides theoretical insight to support a conceptual advance in the field of evolutionary vertebrate embryology.

ADVANCE

This study builds on a model recently published by Uriu et al. (eLife, 2021) that incorporates quantitative experimental data within a modeling framework including cell and tissue-level parameters, allowing the study of multiscale phenomena active during zebrafish embryo segmentation. Uriu's publication reports many relevant and often non-intuitive insights uncovered by the model, most notably the description of phase vortices formed by the synchronizing genetic oscillators interfering with the traveling-wave front pattern.

However, this model can be further explored to ask additional questions beyond those described in the original paper. A good example is the present study, which uses this mathematical framework to investigate the potential independence between two of the modeled processes, thereby extracting extra knowledge from it. Accordingly, the present study represents a step forward in the direction of using relevant theoretical frameworks to quantitatively explore the landscape of complex molecular hypotheses in silico, and with it shed some light on fundamental open questions or inform the design of future experiments in the lab.

The study incorporates a wide range of existing literature on the developmental biology of vertebrates. It comprehensively cites prior work, such as the foundational studies by Cooke and Zeeman on the segmentation clock and the role of FGF signaling in PSM development as discussed by Gomez et al. The literature properly covers the breadth of knowledge in this field.

AUDIENCE

Target audience: This study is relevant for fundamental research in developmental biology, specifically targeting researchers who focus on early embryo development and morphogenesis from both experimental and theoretical perspectives. It is also relevant for evolutionary biologists investigating the genetic factors that influence vertebrate evolution, as well as to computational biologists and bioinformatics researchers studying developmental processes and embryology.

Developmental researchers studying the segmentation clock in other vertebrate model organisms (namely mouse and chick), will find this publication especially valuable since it provides insights that can help them formulate new hypotheses to elucidate the molecular mechanisms of the clock (for example finding a set of evolutionarily divergent genes that might interfere with PSM length).

Additionally, this study provides a set of cellular parameters that have yet to be measured in mouse and chick, therefore guiding the design of future experiments to measure them, allowing the simulation of the same model with sets of parameters from different vertebrate model organisms, therefore testing the robustness of the findings reported for zebrafish.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.106316.2.sa3](https://doi.org/10.7554/eLife.106316.2.sa3)

Summary:

In this manuscript, Verd and colleagues explored how various biologically relevant factors influence the robustness of clock dynamics synchronization among neighboring cells within the context of somatogenesis, adapting a mathematical model presented by Urio et. al in 2021 in a similar context. Specifically they show that clock dynamics is robust to different biological mechanisms such as cell infusion, cellular motility, compaction-extension and cell-division. On the other hand , the length of Presomitic Mesoderm (PSM) and density of cells in it has a significant role in the robustness of clock dynamics. While the manuscript is well-written and provides clear descriptions of methods and technical details, it tends to be somewhat lengthy.

Major comments from original round of review:

(1) The authors mention that "...the model is three dimensional and so can quantitatively recapture the rates of cell mixing that we observe in the PSM". I am not convinced with this justification of using a 3D model. None of the effects the authors explore in this manuscript requires a three dimensional model or full physical description of the cellular mechanics such as excluded volume interaction etc. A one-dimensional model characterized by cell position along the arclength of PSM and somatic region and segmentation clock phase θ can incorporate all the physics authors described in this manuscript as well as significantly computationally cheap allowing the authors to explore the effect of different parameters in greater detail.

(2) I am not sure about the justification for limiting the quantification of phase synchrony in a very limited (one cell diameter wide) region at one end of the somatic part (Page 33 below Fig. 9). From my understanding of the manuscript, the segments appear in significant length anterior to this region. Wouldn't an ensemble average of multiple such one cell diameter wide regions in the somatic region be a more accurate metric for quantifying synchrony?

(3) While studying the effect of cellular ingression, the authors study three discrete modes-random, DP and DP+LV and show that in the DP+LV mode the clock synchrony becomes affected. I would like the authors to explore this in a continuous fashion from a pure DP ingression to Pure LV ingression and intermediates.

(4) While studying the effect of length and density of cells in PSM on cellular synchrony, the authors restrict to 3 values of density and 6 values of PSM length keeping the other parameter constant. I would be interested to see a phase diagram similar to Fig. 7 in the two dimensional parameter space of L and ρ0. I am curious if a scaling relation exists for the parameter values that partition the parameter space with and without synchrony.

(5) Both in the abstract and introduction, the authors discuss at a great length about the variability in the number of segments. I am curious how the number and width of the segments observed depend on different parameters related to cellular mechanics and the segmentation clock ?

(6) The authors assume that the phase dynamics of the chemical network may be described by an oscillator with constant frequency. For the completeness of the manuscript, the author should discuss in detail, for which chemical networks this is a good assumption.

(7) Figure 3 and the associated text shows no effect of the cellular motility profile in the synchrony of the segmentation clock. This may be moved to the supplementary considering the length of this manuscript.

Significance:

The manuscript answers some important questions in the synchrony of segmentation clock in the vertebrates utilizing a model published earlier. However, the presented result is incomplete in some aspects (points 2 to 5 of section A) and that could be overcome by a more detailed analysis using a simpler one dimensional (point 1 of section A). I believe this manuscript could be of interest to an intersecting audience of developmental biologists, systems biologists, and physicists/engineers interested in dynamical systems.

[Editors' note: the authors have responded comprehensively to the reviews from Review Commons.]
