# Peer review - Round 1

Reviewers:
- Jan Willem Veening, University of Groningen , The Netherlands

## Review text

DOI: [10.7554/eLife.20640.021](https://doi.org/10.7554/eLife.20640.021)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Modularity and determinants of a (bi-)polarization control system from free-living and obligate intracellular bacteria" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Vivek Malhotra as the Senior Editor. The following individual involved in review of your submission has agreed to reveal his identity: Grant Bowman (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission

Summary:

The reviewers find that the identification and characterization of ZitP are highly interesting and contribute to our understanding of cell polarity in bacteria. The experiments are, in general, well-designed and the paper is clearly written. The very data rich paper demonstrates that ZitP is a factor that contributes to the positioning of PopZ. However, the conclusions on its role in origin segregation are less well supported and the authors make a few overinterpretations of their results, and these should be corrected before the manuscript is ready for publication. Some of these interpretations would be strengthened by additional supporting experiments, and others would be best left out of the manuscript.

Central conclusions:

1) The Zn-finger domain of ZitP is sufficient for interaction with PopZ, whereas its association with the membrane is critical for its function.

2) ZitP is found to associate, directly or indirectly, with sites flanking the PopZ/ParB-associated centromeric parS sites.

3) Deletion of ZitP or overexpression leads to defects in PopZ and ParB localization.

4) ZitP is able to mediate the redistribution of PopZ to both cell poles upon co-overexpression with PopZ in C. crescentus and in a heterologous E. coli system.

5) Similar properties are observed for ZitP homologues from various α-proteobacterial species, suggesting that the function of the protein is widely conserved in this lineage.

Essential revisions:

The reviewers raise a number of concerns that must be adequately addressed before the paper can be accepted. Some of the required revisions will likely require further experimentation.

In general we propose to remove some of the data concerning the claim that ZitP affects chromosome segregation as the current data does not fully supports this. The manuscript says important things about PopZ and cell polarity, including issues related to chromosome segregation. Focusing the paper on the ZitP-PopZ part will also make the paper more accessible to non Caulobacter readers.

Thus, instead of doing the proposed experiments listed below, some of the points listed can be solved by either downplaying the claims made and/or removing the data.

1) The conclusion that ZitP has a role in origin segregation that goes beyond controlling PopZ localization is not supported by the data:

A) The ChIP-seq results may be explained by the fact that ZipP is associated with the membrane-proximal surface of the PopZ complex and, therefore, located in the vicinity of the DNA regions flanking the PopZ-associated ParB-parS complex. The results obtained for PopZ may reflect a similar situation: crosslinking to the parS region itself may be less efficient because it requires the isolation of a tripartite complex consisting of PopZ, ParB and parS DNA, whereas crosslinking to the flanking regions that are not covered by ParB but still in the immediate proximity of PopZ may be more effective. The experiment using the mCherry-PopZ strain and an anti-RFP antibody (Figure 4A, bottom row) should be performed in a strain lacking ZitP.

B) The synthetic effects caused by the deletion of zitP in the different popZ mutant backgrounds do not necessarily indicate a direct role of ZitP in ParAB regulation. All the defects in ParB localization observed are likely explained by the aberrant formation and localization of PopZ clusters, which in turn may affect the positioning of ParB-parS complexes or the localization/function of ParA and, thus, the control of cell division by the MipZ system. As shown by Ptacin et al. (2014), the mutant forms of PopZ are not fully defective in ParA/ParB binding but still show some affinity for the two proteins. Thus, the deletion of ZitP and the consequent changes in the efficiency/reliability of PopZ localization may simply aggravate the defects caused by the mutation of PopZ and thus enhance the segregation defects of the mutant strains. In agreement with this notion, the severity of the phenotype in all cases corresponds to the severity of the defect in PopZ localization (Figure 4—figure supplement 1). Similarly, the effects of zitP overexpression (stalling of ParB movement, displacement of monomeric ParA) may all be explained by the strongly aberrant PopZ localization patterns induced in this condition and their effects on ParB localization and ParA function. In my eyes, there is no evidence for the statement that "ZitP controls ParAB through a new mechanism that does not involved the known ParAB interaction sites in PopZ but unknown regions flanking the centromere".

2) Figure 2—figure supplement 1B: The elution profile for ZitP needs to be shown to allow a definitive conclusion on the interaction between PopZ and ZitP.

3) The main function of ZitP appears to be the attachment of PopZ to the membrane, which in turn helps to establish the bipolar PopZ localization pattern. Is PopZ in the C. crescentus ΔzitP mutant no longer membrane-associated (even though its subcellular distribution is largely unchanged)? This could be clarified by PALM analysis of suitable C. crescentus strains. Similarly, it would be interesting to see that in E. coli, PopZ clusters are cytoplasmic and no longer membrane-associated (as suggested in the subsection “ZitP imparts bipolarity upon PopZ in E. coli”, first paragraph).

4) The results shown for RpZitP and RpPopZ in Figure 6E are not as clear as for those obtained for the C. crescentus proteins. The data obtained for the rickettsial proteins should be quantified.

5) From the evidence presented in this manuscript, it is clear that PopZ directs the localization of ZitP. However, the authors also strive to prove the reverse – that ZitP directs PopZ localization. They succeed in showing this under two circumstances – co-expression of proteins in E. coli and in the context of overproduction of ZitP1-133 in Caulobacter. At times, the authors seem to be drawing too strong of a conclusion from these results, as the same might be expected of any protein that binds to PopZ. Thus, ZitP's role in directing PopZ may not be unique, especially if PopZ has many binding partners. The possibility of many binding partners may be inferred from the fact that nearly all ST proteins (in addition to the chromosome centromere and ParA/B are delocalized in a popZ knockout background (Bowman et al. 2010). To support the claim that ZitP has a physiological role in directing PopZ localization, they also show that zitP knockouts enhance the cell division phenotype in PopZ mutant backgrounds where PopZ cannot interact with ParA/B. This is a critical result that bears further exploration. First, the authors should determine whether interaction with PopZ is needed for rescue by testing the effects of rescuing the PopZKE/KEP mutant with the W35I mutant of ZitP. Additionally, the authors should ask which parts of ZitP are critical for the rescuing effect by adding back different sections of ZitP into the PopZKE and/or KEP background. If ZitP1-133is sufficient to rescue the phenotype and ZitP1-43 is not, this suggests that membrane anchoring and not just interaction with PopZ is important for proper polar localization of PopZ. If full length ZitP is required, it suggests an important functional role for the C-terminal domain. If ZitP1-43 is sufficient, the model that ZitP directs PopZ localization will likely require some adjustment.

6) Chromatin-IP starts with formaldehyde x-linking, which binds any near neighbors to DNA. Thus, interaction between ZitP and DNA may not be direct or even indirect in the formal sense. It is likely that indirect binding to DNA was observed for PopZ, as sequence-dependent association with DNA probably occurs through ParB/ParA. However, we also know that centromeres reside near poles in Caulobacter cells, and that the poles also have PopZ. Thus, some of the binding observed by ChIP-seq may have occurred merely because PopZ and the centromere are in proximity – not from a direct or even an indirect connection between protein and DNA. Similarly, it seems possible that ZitP is merely in the vicinity of centromere by virtue of its interaction with PopZ, and not indirectly binding to DNA. The conclusions would be strengthened if the authors could provide more compelling evidence that ZitP isn't interacting with sites near centromeric DNA because it is at the poles and happens to be near DNA that is not otherwise occluded by ParA/ParB/PopZ. If this is not possible, several of the authors' conclusions should be reworded, the issue should be raised in the main text of the manuscript, and mechanisms outside of ZitP-DNA interactions should be discussed.
