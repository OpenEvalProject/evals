# Peer review - Round 1

Editors:
- Arvind Murugan, University of Chicago United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.65498.sa1](https://doi.org/10.7554/eLife.65498.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This paper extends classical models of molecular cooperativity to higher order cooperativity, where the binding of ligand by a protein is affected by other already bound ligands. The work quantifies effective higher order cooperativity between 3 or more ligands that interact indirectly by biasing the underlying (equilibrium) molecular ensemble. The work should be of broad interest to protein scientists since it suggests a new way of quantifying empirical observations of cooperativity.

Decision letter after peer review:

Thank you for submitting your article "Allosteric conformational ensembles have unlimited capacity for integrating information" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by Arvind Murugan as Reviewing Editor and Aleksandra Walczak as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Hernan G Garcia (Reviewer #1).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

The reviewers had mixed opinions, primarily with respect to clarity of the paper and presenting a clear relationship to prior work. In particular, reviewer #2 has concerns about the way cooperativity is quantified here, the benefits of this approach and its relationship to prior work. Below, I summarize a few areas where the paper must be improved prior to being acceptable for publication. Please also refer to the reviewer's detailed reports for constructive criticism that will make this paper more readable and impactful.

1. Flavor of results in the main paper: The work relies on significant mathematical work that is entirely confined to the appendices. The main paper is too superficial as a result and the reader should have more meat to sink their teeth into. See reviewer's comments for suggestions – e.g., some equations (or intuition behind equations) can be moved from the appendix to the main paper. I present one suggestion re: Figure 4 below. Feel free to address this important issue in other ways instead.

Figure 4 is the only figure that presents some sense of the results and is much too brief. Perhaps Figure 4 can be unpacked, possibly into an additional figure, offering intuition into the remarkable binding curves shown (e.g., with positive and negative cooperativity in different regimes). For example, you could show the kinetic network needed to get one or two of the most interesting binding curves shown in Figure 4. The current visualization in Figure 4 in terms of heatmaps is hard to interpret.

The mathematical content in Materials and methods needs to be better integrated with the argument in the main text. One way to do this would be to add notes in the Methods that point to concepts discussed in the main text. See reviewer comments re: the same.

2. Relationship to prior work: Your work seeks to do two distinct things: (a) demonstrate that equilibrium conformational ensembles can implement any pattern of HOCs, (b) introduce a new way to quantify higher order cooperativity that's distinct from binding curve shape.

As one of the reviewers points out, the presentation of (b), relationship to prior work and benefits of the new measure over prior work should be better clarified. See reviewer comments for more. Could you spell out an example or two where the binding curve is an unwieldy or misleading characterization of cooperativity while your HOC coefficient performs better?

3. Concrete biological example – theory can and should precede experiments. But the paper will have more impact if the authors can lay out how to use the framework here to perform or interpret experiments. Ideally this would be done with a concrete example of a protein or protein complex where these ideas might potentially have relevance, how what is known about its conformations predicts HOCs and binding curves, what experimental signatures one might look for and so on – even if there is currently no data.

See review comments for other suggestions.

Reviewer #1:

Often in biology, in phenomena ranging from the binding of oxygen to hemoglobin to the binding of transcription factors to DNA, it is observed that the binding of a second ligand to its substrate is more likely than the binding of the first ligand. This so-called cooperativity is usually associated with direct ligand-ligand interactions. However, an increasing body of theoretical work rooted on the Monod-Wymand-Changeux and Koshland-Némethy-Filmer models has shown that, if the substrate can adopt two conformations, cooperativity can arise in the absence of direct interactions between ligands.

Despite the widespread adoption of these models, they have presented limitations when confronted with real data. For example, quantitatively recapitulating gene expression input-output functions in eukaryotes often calls for more than the pairwise interactions that lead to classic cooperativity. Instead, in order to reconcile theory and experiment it is necessary to invoke higher-order cooperativity. Here, multiple bound ligands act in a collective fashion to influence the binding (or unbinding) of additional ligands.

Biddle et al. propose an intriguing theoretical model for realizing higher-order cooperativity between binding sites in a single substrate in the absence of energy dissipation, which means that they must adhere to the strict constraints of microscopic reversibility imposed by thermodynamic equilibrium. They demonstrate that, by extending previous models and allowing the substrate to fluctuate between multiple distinct conformational states, systems may achieve arbitrary higher-order cooperativitive (HOC) behaviors, even at thermodynamic equilibrium. Their graph-based method extends the idea of allosteric regulation to apply to systems with many distinct conformational degrees of freedom and, as such, should, in principle, provide a useful conceptual tool for interrogating the wide range of biological processes in which allostery is thought to play some role.

The paper is extremely well-written, with ample room for the introduction of concepts-including their historical background-and for the discussion. However, we worry that the difficulty of their mathematical notation, as well as their choice to relegate key details about both the derivation and the application of their method to the SI will limit the impact and pedagogical value of this creative and timely work.

Likewise, the considerable import of their finding that sufficiently complex allosteric systems can realize any regulatory logic that is achievable at thermodynamic equilibrium is somewhat obscured by the absence of a clear, detailed application to a concrete biological system. All the same, we view this work as an exciting step towards developing theoretical models that adequately attend to the richness and complexity of real biological systems.

Strengths:

– The paper offers a new framework for thinking about how complex allosteric systems with multiple distinct conformations function to integrate information from ligand binding.

– The authors show that allostery, when sufficiently complex, can provide a physical basis for the emergence of higher-order cooperativities of an arbitrary nature.

– The authors provide an intuitive method for coarse-graining systems with many conformations into a single, tractable ligand-binding graph, which can then be used to quantify higher-order cooperativities between binding sites. This method should prove a useful tool for navigating the complexities present in many real biological systems.

– The authors show that their framework is consistent with (and therefore subsumes) previously used MWC models.

Weaknesses:

– Due to the strong results and implications of the paper, the mathematical proofs in the Materials and methods section must be easy to follow and accessible to the reader. The abundance of indices and references back and forth from the main text make it difficult to follow and evaluate the author's claims throughout this work. The derivations of the authors' coarse-graining procedure and their expression for effective higher-order-cooperativity, as well as their proof that sufficiently complex allosteric systems can achieve any regulatory logic, are nowhere to be found in the main text. While it may not be practical to include these pieces in full, the authors often could at least provide qualitative intuition for the origins and implications of the expressions they present.

– The lemmas and proofs in the Materials and methods are stated mostly in the form of equations, with few explanation on how the proof connects to the concept explained in the main text.

– It is worth noting that the authors limit themselves to considering systems at thermodynamic equilibrium. This is perfectly understandable given the considerable scope of the work already undertaken, but it will be interesting to see what new behaviors might emerge from systems operating away from equilibrium in future work.

– Given that this paper considers only the equilibrium situation, it would be interesting to explicitly state the advantage of adopting the linear framework as opposed to a thermodynamic description in terms of, for example, Boltzmann weights.

– The absence of a thorough, well-illustrated application to a concrete biological system somewhat dampens the paper's impact.

– The authors use the phrase "information integration" multiple times throughout, but they never provide a precise definition of what they mean. Typically a treatment of information transmission would be expected to deal with noise, as well as mean behavior, but that is not done here. They need to clearly define this term early on. While the authors provide an example that does give some intuition in lines 126-136, it might be helpful to move this discussion earlier to provide more context for the rest of the discussion in the introduction.

– In line 41, the authors point out that previous studies investigating effective cooperative effects in MWC models do not "quantitatively determine" the effective cooperativity, but instead infer it indirectly from the shape of the binding curve. However, they do not tell us why this matters. What can we expect to gain by quantifying effective cooperativity directly?

– What is the benefit of having more than 2 conformations? Can the authors show, quantitatively, how performance scales with the number of conformations? The discussion in lines 340-344 provides some basis for this, but the point seems worthy of further discussion and illustration. Is there a graphical way to illustrate the space of achievable integrative behaviors, and how this expands with increasing N (for some given n)?

– This work would be significantly strengthened by including a concrete example that demonstrates both how the framework could be employed to analyze a biological system and what it tells us about how conformational flexibility impacts integrative behaviors. For instance, the authors could revisit their earlier work on the hunchback gene in fruit flies (Estrada et al., Cell, 2016; Park et al., eLife, 2019), and show how the space of achievable GRFs expands with the number of conformational degrees of freedom.

Reviewer #2:

In this paper, the authors argue correctly that quantification of higher-order coupling (HOC) is crucial for the understanding of biological systems at many different levels of description. I found the paper hard to read. This is due, in part, to the lack of connection with previous descriptions of HOC. The most basic description of pairwise coupling is usually through linkage analysis developed by Wyman. Such coupling is often described by cycles, e.g. a double-mutant cycle or a cycle that describes binding of some ligand X in the absence and presence of a second ligand Y. Pairwise coupling is usually considered to have a dimension of 2 (and not 1 as in the work here). A natural extension to HOC coupling is then done via higher-order dimensional constructs, e.g. triple-mutant boxes for the 3-way coupling between 3 residues (JMB 1990 Aug 5;214(3):613-7; PNAS 2004 Jan 6;101(1):111-6; Annu Rev Biophys. 2017 May 22;46:433-453). Consequently, a key question for me about the current work is the relationship between the previously used measure for HOC and the one described here.

Also, is there an advantage to using the measure proposed in the current work? It seems to me that the description here bypasses intermediate orders of coupling. In other words, nth order coupling is not described in terms of all the lower orders of coupling. Is that a good thing?

In addition, the authors ignore (lines 48-50) the existence of the Hill constant which provides a measure of cooperativity despite having some shortcomings and (line 83) the many previous papers about HOC as mentioned above.

Other comments:

1. Line 308 and elsewhere -it seems that statistical corrections for the binding constants were not introduced. This is OK if stated and not misinterpreted.

2. Line 321 – HOC usually diminishes with factorial decomposition. Why not here?

3. Lines 328, 401-402 – site-heterogeneity leads to apparent negative cooperativity but it is apparent since it can involve no coupling or 'communication' between sites. It should not, therefore, be presented as a possible source for HOC and is not true negative cooperativity.

4. Line 338 – I thought that intrinsic HOC can arise only when the sites are not identical so what am I missing unless it's the statistical factor.

5. Figure 4 – why can binding decrease with increasing substrate concentration?

6 Lines 385-392 – for hemoglobin affinity increases but cooperativity actually decreases at high substrate concentrations because most of the molecules are 'locked' in the R state. Is this captured by the current formalism?

7. Line 699 – fix typo: i to k; I don't understand Equation 15. If each term in the product is a ratio of the terms for forward and reverse directions so should the result on the rhs. Thermodynamically, a product of equilibrium constants is an equilibrium constant but the result on the rhs is not.

8. The analogy with TF binding is potentially problematic because of confusion between different levels of cooperativity. For example, IPTG binding to the lac repressor dimer occurs without cooperativity but 2 IPTG molecules need to be bound for transcription to occur. Hence, measuring transcription as a function of IPTG concentration appears to be very cooperative but the fraction bound as a function of IPTG concentration is not.
