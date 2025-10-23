# Peer review - Round 1

Editors:
- Kang Shen, Stanford University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.31535.022](https://doi.org/10.7554/eLife.31535.022)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "A postsynaptic Pi3K-CII dependent signaling controller for presynaptic homeostatic plasticity" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by Kang Shen as the Reviewing Editor and Eve Marder as the Senior Editor. The following individual involved in review of your submission has agreed to reveal his identity: Joshua M Kaplan (Reviewer #1).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

All three reviewers recognized that this paper is the first comprehensive characterization of the postsynaptic mechanisms of PHP and found it appropriate for publication in eLife. They did raise a number of questions which I will list below. Through discussion with each other, we have come to the conclusion that you can address the issues by revising the text and including new discussions. If you have additional data that speak to some of the questions such as mutant allele analysis of vps34 or rab11, you are also welcome to add them. In particular, the reviewers would like to see some discussions about the steady state GluR levels in the endocytic mutants and how that could potentially affect PHP.

We expect a quick turn around after you resubmit your manuscript since the reviewers did not demand specific experiments to be added. We look forward to receiving a revised version of this manuscript.

Summary:

The manuscript by Hauswrith et al. describes the results of an RNAi screen of the Drosophila kinase and phosphatase proteome to identify components of homeostatic plasticity at the fly NMJ. The authors identified several hits in the late endosomal pathway, and focus on the characterization of one of those hits in detail – PI3K-c11. The authors provide compelling evidence that a postsynaptic late endosomal pathway is essential for homeostatic plasticity, and show that PI3K-c11 mutants disrupt the formation of this compartment. They find an interesting effect on extracellular calcium levels as a regulator of the mechanism, indicating that the pathway is required to support homeostatic at low calcium levels, but not high. They provide some interesting speculation on how this might arise, but sorting it out will require more experimentation. Overall, it's a nice study with some compelling data. I especially liked the individual recordings shown in Figures 1 and 2 that really highlight how robust this form of plasticity is. The characterization of the PI3K-c11 mutant is robust and provides a strong argument for this pathway regulating late endosomal compartments and the homeostatic response to both acute and long-term blockage of postsynaptic glutamate receptors.

Essential revisions:

Please discuss if the steady state GluR levels is affected the endocytic mutants and how that could potentially affect PHP.

Minor points:

1) In Figure 2D, the QC scatter plot for Pi3K68D mutants seem substantially shifted to lower values than the predicted curve for WT controls. Does this suggest that QC is reduced at baseline in these mutants?

2) The conclusions concerning Rab11 and VPS34 would be strengthened if analysis of mutant alleles (or mosaic animals) were provided. I agree that the strength of the Pi3K86D data offset this concern somewhat; however, analysis of mutant alleles would strengthen the authors' conclusions. Perhaps you already have such data?

3) Could the authors speculate about the identity of the EE/RE cargo that requires Pi3K68D?

4) Do the endosomal mutations and RNAi alter RE/EE cargo flux? This could be measured with a fluorescent tracer (e.g. Transferrin).

5) Wouldn't you expect changes in GluR abundance if RE trafficking is perturbed? The data shown in Figure 4B suggest that mEPSP amplitudes are decreased with Pi3K68D over-expression. Was the GluR staining also decreased in these animals?

6) What is the Muscle O/E genotype shown in Figure 4B? I thought that this UAS was lethal when expressed by the BG57 GAL4 driver.

7) The Discussion has an elaborate section involving speculation about PHD. Does Pi3K86D regulate PHD? If not, this aspect of the discussion seems weakly connected to the main findings reported here and should be minimized.

8) Is it fair to normalize EPSCs to mEPSPs for QC calculations?

9) The authors should discuss/speculate about why PHP in Pi3K mutants is sensitive to external calcium levels? Is PHP sensitive to EGTA-AM?

10) Does Pi3K68D mutation alter RMP? (over-expressing Tgene does, subsection “Pi3K68D is required postsynaptically for PHP”, first paragraph).

11) Is FYVE-GFP or Rab11 staining altered when PHP is induced? This would suggest that post-synaptic Endosomes signaling are involved in PHP induction.

12) At several points in the text, you refer to a post-synaptic endosomal "platform" for PHP (e.g. when discussing the model in Figure 9). Please explain what you mean by this term.

13) Pi3K68D-MB is apparently the Minos insertion MB08286 (Materials and methods). I am surprised this has a mutant phenotype, as the splice trap in the Minos is in the wrong orientation for Pi3K68D. This mutation would be more likely to block expression of CG14131, a gene within the Pi3K68D intron that goes in the opposite direction. The MB is in its intron. They should look at the MiMIC insertion nearby (MI15179, also available from Bloomington), as that is in the right orientation to trap splicing of Pi3K68D. Of course, their CRISPR allele appears to show that the phenotype can be produced by only perturbing expression of Pi3I68D, so this should not call any of their results into question. However, the MiMIC allele would be useful for another experiment they should do (although not necessarily for this paper), which I will describe below.

14) I question their interpretation of the deltaN overexpression phenotype (subsection “Pi3K68D is required postsynaptically for PHP”, last paragraph). If the N terminus interacts with clathrin, and they overexpress a mutant lacking this region in a wt background, this protein (if it is active) should still have activity but be incorrectly localized. In their model, it should not interfere with binding of the wt protein (which is still expressed) to clathrin, since deltaN lacks the clathrin binding site. If clathrin does indeed bind to the N terminus, and they wish to test whether this is important, they would need to instead ectopically express only the N-terminal region, without the kinase. This should then act as a dominant negative, occupying all the sites on clathrin and thus preventing correct localization of the wt protein. Actually, the fact that overexpression of the kinase-dead mutant blocks PHP already makes this point (second paragraph of aforementioned subsection), although not as cleanly as expression of only the N terminus would. The KD mutant should act as a DN, unlike the deltaN mutant, because it would bind to clathrin, occupying the binding sites for the wt kinase, but would not itself have kinase activity.

15) In this regard, it is interesting that there are two forms of the Pi3K68D mRNA (RE and RB) that would encode truncated proteins (PE and PB) encoding only the N terminus. Perhaps these are natural regulators of the kinase whose expression determines whether or not the kinase can find a clathrin binding site? It would be interesting to see where these isoforms are expressed, and to express RE or RB cDNAs and see if they act as DNs.

16) I don't understand the section on the effects of changing Ca concentration. The results are intriguing but seem difficult to interpret in any mechanistic way given the information that exists at present. The Discussion is very hard to read. Perhaps this is inevitable given the confusing nature of the results.

17) Related to point 16), they seem to be saying that since PHP works normally in the mutant at physiological (1.5 uM) Ca++ concentrations (subsection “Loss of Pi3K68D renders the expression of PHP sensitive to changes in extracellular calcium”, second paragraph), these mutants must have been normal with respect to this phenomenon during their development in vivo. It is only when they are filleted and incubated at low Ca++ that a phenotype is observed. It would be very informative about what is going on if they could determine whether the development of the larva in the absence of Pi3K68D renders fillets from these animals abnormal with regard to PHP at low Ca++, or if the activity of Pi3K68D during the experiment is required for normal PHP at low Ca++. It seems like this should be addressable in their system, because there are many Pi3K inhibitors that have been described. They could fillet wt embryos, or embryos lacking one copy of the gene, and then incubate them with the inhibitors and see if this affects PHP. But, perhaps the available inhibitors are not specific enough for this form of Pi3K, or perhaps they don't work in Drosophila? It seems like the investigators probably know the answer to this question already, since it is an obvious experiment. If so, they should inform us in the paper. If not, they should do the experiment.

18) If inhibitors don't work or are not specific enough, there is another approach that could address this question. This experiment would require more time than is normally given for revisions, and the paper is already strong, so I would not require it for publication. The Bellen lab (Nagarkar-Jaiswal et al. eLife 2015) has shown that the DeGradGFP method can transiently inhibit gene function by degrading a GFP fusion of the protein. There is a MiMIC in an appropriate position to allow replacement of the MiMIC by GFP using their methods, to create a "protein trap". In the Bellen paper, they show that such protein traps often retain function. Thus, if they were to make a protein trap and found that this allele behaved like the wt protein, they could then turn off Pi3K68D activity using the temperature-sensitive DeGradGFP mechanism in larvae that had developed with normal activity. In the Bellen paper, they show that they can rapidly shut off Dunce and turn it back on by temperature shifts.

19) From the images, it’s clear there are robust changes in postsynaptic endosomal compartments. However, it is less clear if there is any change going on presynaptically. Clearly they demonstrate the effect on homeostatic plasticity is postsynaptic, but it would be interesting to know if the same changes in subcellular markers is occurring in the presynaptic bouton. I assume PI(3)P would be required in both compartments to properly generate that endosomal compartment – if not it would be interesting, but very surprising. I assume the authors already have that data from their images, so would be nice to comment on it in the text.

20) The authors nicely show postsynaptic rescue of the Pi3K mutant phenotype. However, it wasn't clear why they didn't also show postsynaptic RNAi knockdown blocks PHP. Did I miss that somewhere – if not, why not show that as well to complement the rescue?

21) The last minor comment deals with the Pi3K68D structure function part. They infer the clathrin binding domain and kinase activity are important by overexpressing constructs missing these elements and observing a block in PHP. I would have preferred to see this being done as a rescue of the null mutant – seems a far easier result to interpret. Why was the overexpression used instead of rescue?

22) Not sure how the EM was quantified, or if it was.
