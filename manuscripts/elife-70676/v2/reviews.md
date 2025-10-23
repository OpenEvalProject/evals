# Peer review - Round 1

Editors:
- María Mercedes Zambrano, CorpoGen Colombia

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.70676.sa1](https://doi.org/10.7554/eLife.70676.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Acceptance summary:

This work uses an elegant and well-designed experimental evolution strategy to investigate the roles of history, chance, and selection on the evolution of antibiotic resistance in the clinical pathogen Acinetobacter baumannii. The authors show that while history impacts the evolution of antimicrobial resistance, this effect decreases with increasing drug selection strength and indicates that natural selection is a dominant driver. The work presents clear, unambiguous data on the importance of antibiotic exposure on the evolution of resistance.

Decision letter after peer review:

Thank you for submitting your article "The roles of history, chance, and natural selection in the evolution of antibiotic resistance" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Dominique Soldati-Favre as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Alan McNally (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

While the work addresses a very relevant and interesting question, the reviewers raised some concerns that need to be addressed in order to improve the manuscript. Additional experimental details should be included, and clarification is needed regarding some of the concepts used. More importantly, the limitations of the approach need to be specifically addressed and some of the claims and interpretations should be toned down, particularly given the absence of a drug-free control.

1) A main concern is in the interpretation of populations having the same genetics but different phenotypes (eg lines 300-310) – this conclusion is wrong given the experimental design. The authors provide several explanations but leave out a high likelihood alternative which is that different experiments consist of mixed populations with diverse genetic makeups. Alternatively, if the authors meant instead to focus on specific mutations (ie same mutations/localized mutations) regardless of the background, then this conclusion is trivial – it is known that pleiotropy exists.

2) I agree with the author's definitions of change due to history vs change due to selection given the evolution they designed – and I found this quite innovative and overall strong. However, the definition and calculations of evolution due to chance here are shaky given the three replicates only. There are plenty of extremely rigorous estimates of genetic drift during bacterial evolution (see all of Lenski's work) – three populations is quite small to make that claim and run the statistics. Including chance as a possible contributor didn't add much to the story, and it raised more questions than answers given the extremely diverse genetics that were observed, and that data of the mixed populations below 75% was not included.

3) Experiments are flawed without a no drug control. Was the reversion of CIP resistance specific to the new drug selection, or is it simply the lack of CIP pressure? This is important as the authors make claims about drug-specific evolutionary tradeoffs and collateral sensitivity. The methods in line 428: "We froze 1 mL of the control populations on days…" but this is the only place a control population is mentioned.

4) Much of the data was difficult to follow, such as the fold changes for MICs – for example, following the discussion of CIP resistance, maintenance, and reversion was nearly impossible with the reference to figure 4 fold changes only. Also going back and forth between IMI and CAZ, which is discussed in parallel near the beginning, but then broken down later on, is another example.

5) Key experimental details are missing. What volume were the populations propagated in? Population experiments were not well described – how were replicate MICs initiated? How much volume was used for sequencing? So on and so forth. These are particularly important to interpret the results.

6) Why was a 75% threshold used to determine alleles if the populations were sequenced to a level of 5%?

7) Despite being described in great detail in the methods, it doesn't come across to non-modeler such as myself exactly how selection, history, and chance were quantified in the phenotypic experiments shown in figure 2. I am a bit clearer as to how these were quantified for the genomic data. However, I think a broad readership may benefit from a layman's description of how these were differentiated. It is vital to the science and data shown and I would certainly have appreciated a clarification, especially for the phenotypic data in figure 2.

8) In line 307. In the absence of bacterial genetic experiments to confirm that these historical infections are actually driving the 4 fold differences in phenotype, I think this inference needs to be toned down.

9) Line 343: Is there a benefit to be had of fitness experiments in antibiotic-free medium to confirm the supposition made here?

10) In some cases, I found the framing of the results in terms of history, chance, and selection to be a bit overly general, which sometimes obscured the specific results being reported. The paper could be improved by using more specific language-perhaps restricted in scope- in describing and interpreting the results, both because 1) it's not obvious to me that the results would apply generally to antibiotic resistance beyond the very nice, but potentially system-specific, results presented here; and 2) the terms themselves (history, chance, selection) could conceivably have different meanings in different contexts (more on this below).

11) The study design has been used in numerous previous studies; it is well established, elegant, and has given rise to many new insights. However, as I understand it, there are some inherent assumptions of the approach that should be briefly discussed. Most notably, does the approach inherently assume that the effects of history, chance, and selection are additive (or perhaps linear) in some sense (in terms of phenotypic variance measurements or the Manhattan-based genotype metric)? While this simplifying assumption seems critical to the power of the approach, it is not clear to me that this assumption holds in general. When I try to think of this in terms of, say, a simple population dynamics model, the terms history, chance and selection are themselves somewhat nebulous, and it's not clear to me that they could be unambiguously and uniquely defined even in simplified theoretical models (or more directly, that the variance-based phenotype measures correspond to well-defined features or parameters of population dynamics models). I say this not to criticize the approach-again, its power lies in the simplicity of the design and the intuitive value of separating these three evolutionary features and attempting to quantify their contributions. But I think the article could be strengthened by briefly discussing the underlying assumptions-ideally by pointing to previous work (if it exists) that establishes that the features are additive and measurable in the sense required by the experimental design. If not, I think it would be worth discussing that limitation briefly, as I worry the inherently nonlinear nature of these very complicated, evolving systems could lead us to misinterpret the results. Given the general success of similar approaches in past work, I suspect the authors have thought through these issues in detail; discussing those points might open the paper to a broader audience not intimately familiar with all the previous studies.

12) One example related (but not identical to) the point above: in the current experiment, the role of history is defined in terms of previous selection conditions (drug and growth phase). But the new evolution experiment itself has multiple time points, and even qualitatively distinct epochs (sub- and super-MIC drug). So one might argue that history is playing a role continuously throughout the experiment-history not merely of the previous selection in fluoroquinolones, but also history of the previous time points / epochs of the new evolution (β-lactams). My point is that it is important to clearly define the terms at all stages and discuss, at least briefly, the limitations of the definitions that are chosen.

13) While history, chance, and selection are quantified at both the genetic and phenotype level, it's not clear to me that these numbers can be directly compared to one another (though it's tempting to do so!). Could the authors briefly comment on the connection between these measures-that is, when (and to what extent) one would expect correlations between them (e.g. high levels of historical influence at the genetic level leads to high levels of historical influence at the phenotype (MIC) level….assuming the definitions used here).

14) Do the authors have any thoughts on how the results might be affected by the fact that the new evolution experiments take place in planktonic (rather than biofilm) conditions? How might the results differ if they had been performed in biofilm, and what could you learn from the fully symmetric experiment (P/ B initial strains evolved in both P and B new selection conditions). The authors may wish to discuss this avenue for future work.
