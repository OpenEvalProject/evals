# Peer review - Round 1

Editors:
- Anne-Florence Bitbol, https://ror.org/02s376052 Ecole Polytechnique Federale de Lausanne (EPFL) Switzerland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.84878.sa0](https://doi.org/10.7554/eLife.84878.sa0)

This valuable study provides a synthesis of sector models for cellular resource partitioning in microbes and shows how a simple flux balance model can quantitatively explain growth phenomena from numerous published experimental data sets. The evidence is convincing, and the study should be of interest to the microbial physiology community.


---

# Peer review - Round 1

Editors:
- Anne-Florence Bitbol, https://ror.org/02s376052 Ecole Polytechnique Federale de Lausanne (EPFL) Switzerland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.84878.sa1](https://doi.org/10.7554/eLife.84878.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "An Optimal Regulation of Fluxes Dictates Microbial Growth In and Out of Steady-State" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Aleksandra Walczak as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) Please streamline the presentation of the model and the underlying assumptions, and clearly mention parameter values, and whether they are adjusted or fixed, in the main text. It would also be useful to provide units and typical values in E. coli when parameters are introduced, as well as to comment on the realism of parameter values for those that are varied. All this is important, especially for the reader to gain intuition on the model (see reviewer 3's detailed comments).

2) Please briefly discuss additional mechanisms that could be of interest, such as ppGpp binding RNAP and ternary complexes (see reviewer 3's detailed comments).

3) Please address the reviewers' suggestions, esp. regarding clarifying the manuscript, and comparing to previous results in the literature.

Reviewer #1 (Recommendations for the authors):

– I find the notations for the allocation parameters (ϕ in the text) misleading. It seems to me that this symbol is often reserved in the literature for mass fractions. Although these two quantities are the same at the steady state (in the framework presented), the authors should at least write a sentence to make the reader aware of that.

– On page 5 the authors discuss the presence of γmax in scenario I. I might miss something, but the authors could also comment somewhere about the presence of a γmin (slow growth seems not to be accessible in this regime).

– For the sake of clarity, it could be better to write the equations in Figure 1B in terms of the allocation parameters (not mass fraction).

– Page 6, 'reate' > 'rate'.

– Beginning of the section "Optimal allocation results from…". Here it should be clearly stated that now the authors explore a different model, in which v is different from νmax (as before).

– In Figure 2B, ribosome allocation and transcription rate could be highlighted as they 'constitute' the flux-parity regulator (if my interpretation is correct). They could have a red box.

– In my opinion, the comparison with scenario III on page 8 after Equation (2) is misleading. I would probably put Fig2D-E as a supplementary figure and just plot ϕRb∗ (flux parity). Also, I do not understand the colormap of Fig2D and the fact that the values are multiplied by ϕRb(III) in the plot.– The order of Table S1 and Table S2 should be changed.

Reviewer #2 (Recommendations for the authors):

In its current form, the presentation of the model and the underlying assumptions is convoluted. The reader has to do a lot of work to figure out parameter values, which assumptions have been made in which section, and so forth; a revised narrative which is easy to follow would help a lot. Throughout the supplemental material and appendix, references to Figures and Tables are missing (they appear as double question marks) and there are a number of typos; please check those issues.

Some specific comments follow:

– Please explain the proteome constraint ϕRb+ϕMb+ϕO=1 for the benefit of the reader, even though this constraint has been used in prior work.

– Inclusion of ribosome activity later in the paper is confusing after the discussion of how ribosome inactivity is a "puzzle".

– Bottom panel of Appendix 1, Figure 2 – the model behaves very differently near the origin; are there data to confirm this behavior?

– In Figure 1(A), it would help to add units alongside descriptions, e.g. does cpc have dimensions of charged tRNAs per unit volume, and does vmax have units of nucleotides/sec?

– Please check that notation is consistent, e.g. at bottom of p. 4, ϕR is used instead of ϕRb, and similarly for ϕM.

– Relevant references are missing: In the main text on p. 11 (last line), add Metzl-Raz et al. eLife 2017 along with Karpinets et al. 2006; on p. 6 in the discussion regarding S. cerevisiae in the penultimate paragraph, add Kostinski and Reuveni Phys. Rev. Res. 2021, and also their 2020 PRL work analyzing the rRNA bound on bacterial growth rates in Methods on p. 15, last paragraph of “Synthesis of Proteins”; in the discussion of a non-zero ribosomal protein fraction in the limit that growth rate goes to zero, include Koch’s hypothesis that this is advantageous for fluctuating growth conditions [A.L. Koch, Adv. Microb. Physiol. 1971].

– Appendix 1, Figure 6: Could a mathematical expression for the 'absolute difference from optimal allocation' be spelled out?

– Proteome sectors in supplemental Figure S1(B) are not to scale: 'other proteins' fraction should be much larger (~55% from authors' numbers) and r-protein fraction (~7% to 25% by mass in E. coli) is smaller than represented.

How do the results of this manuscript compare to prior observations of tRNA charging? For example, consider this quote from Bremer and Dennis below:

"There are about nine tRNA molecules per ribosome in exponentially growing E. coli, and this ratio shows little variation for growth rates above 0.6 doubling/h. Since the peptide chain elongation rate approaches 22 amino acids per second, each tRNA is required to cycle through the ribosome on average about two times per second. Ikemura [T. Ikemura, 1981, J Mol Biol 146:1-21] has quantitated over 70% of the total tRNA population into 26 separate species, at least one for each amino acid except for proline and cysteine. For each of these 18 different amino acids, there is at least one major tRNA isoacceptor, which is present at a molar ratio of 0.15 to 0.60 copy per ribosome. The aminoacyl-tRNA synthetases are present at about 0.1 copy per ribosome; each synthetase molecule is therefore required to aminoacylate about 10 molecules of its cognate tRNA every second ( = 1 cognate tRNA per second per ribosome) to sustain protein synthesis at a rate of about 20 amino acids per second per ribosome."
