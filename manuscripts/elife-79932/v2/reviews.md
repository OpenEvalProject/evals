# Peer review - Round 1

Editors:
- José D Faraldo-Gómez, https://ror.org/01cwqze88 National Institutes of Health United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.79932.sa0](https://doi.org/10.7554/eLife.79932.sa0)

This article seeks to address a key question in protein biophysics: are the amino acid positions involved in allosteric mechanisms conserved across homologs of a protein family? Or do these mechanisms involve distinct amino acid patterns that vary amongst homologs? To address this question, the authors follow an innovative multidisciplinary approach that combines deep mutational scanning with machine learning; the findings of this study will be highly relevant to protein engineers and biophysicists.


---

# Peer review - Round 1

Editors:
- José D Faraldo-Gómez, https://ror.org/01cwqze88 National Institutes of Health United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.79932.sa1](https://doi.org/10.7554/eLife.79932.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Deep mutational scanning and machine learning reveal structural and molecular rules governing allosteric hotspots in homologous proteins" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by José Faraldo-Gómez as the Senior Editor. All reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another and with the Senior Editor, and the consensus is to invite you to submit a revised version of your manuscript that addresses the concerns enumerated below – particularly but not exclusively those put forward by Reviewer #3.

Reviewer #1 (Recommendations for the authors):

The paper is well written, the experiments are appropriately performed. I would like to encourage the authors to make the raw data available. I don't have any suggestions for changes to the manuscript and think that it makes a valuable contribution to the literature while noting that it leaves a few questions open-ended and that some of the speculation regarding the molecular basis could be tested experimentally. Obviously, this reflects my biases and interests as somebody interested also in structure and dynamics. Overall it's a very nice paper, congratulations.

Reviewer #2 (Recommendations for the authors):

In the Public Review I provided my overall comments. Below my aim is to make the concept and method clearer to the community.

With this aim in mind, there is one thing that I am missing. That is, how the authors define 'hotspots' via DMS. I think that it is important to clarify. This will help the readers.

I would also suggest to consider a figure comparing the hotspots in this paper to the hotspots as defined by the propagation pathways from the allosteric binding site to the distal active site. Would mapping these on a structure (e.g. using some server?) work? This could help the reader in visualizing the difference between the new concept suggested here and the 'traditional' definition.

Reviewer #3 (Recommendations for the authors):

Figure 1 supplement 1 sets the dynamic range of the assay and seems critical to the interpretation of the experiment. From these data, it would seem that the RolR assay lacks discriminating power across mutations. Consider promoting this figure to the main text.

We found the selection of the top 25% scoring residues as "allosteric hotspots" somewhat arbitrary – is it possible to instead select a cutoff based on the resolution (error) of the assay? Surely the top 25% of allosteric hotspots for RolR (which has a limited dynamic range) and TetR (which has a more extensive dynamic range) have very different biophysical effect sizes, and so this is not an apples-to-apples comparison?

Consider describing the behavior of previously well-characterized aTF mutations in your assay. This would help build confidence that the assay is truly reporting on allosterically dead mutations.

Consider using Fisher's exact test to assign a p-value describing the significance of enrichment/depletion of particular residue types in figure 3A

Figure 3C does not have a legend. Also, the figure seems to show K193Y while the main text refers to an inactive Y198 mutation.

In the methods section, it was unclear how the library was broken up. It seems like it was sequenced in two parts (to cover the entire open reading frame), but was this sequencing two regions of the same cultured and sorted sample? Or was the library broken into sublibraries that were cultured and sorted in smaller batches and then sequenced?

We understand that mutations at ligand-contacting positions were not considered, since these mutations are not allosteric (they instead directly affect ligand binding). How was ligand contacting defined?

Many times, plausible explanations/ideas seemed to be asserted as fact. We feel that these claims either need a citation, more expression of their uncertainty (explaining their lack of evidence in data and the literature), or a more careful explanation:

1. Abstract, page 2: "We found hotspots to be distributed protein-wide rather than being restricted to "pathways" linking allosteric and active sites as is commonly assumed" It is to our knowledge that it has never been asserted that allosteric hotspots themselves form pathways. Rather it is the assertion (in the prior literature cited by the authors) that allosteric hotspots preferentially contact coevolving networks of residues. In many cases, these co-evolving networks don't just link allosteric to the active site, but often connect other distal surfaces (with no known allosteric function) to the active site – going beyond the idea of a single pathway that the authors seem to imply.

2. Results page 5: "An aTF mutant that increases the thermodynamic gap between inactive and active states by stabilizing the inactive state will constitutively lock the protein in the inactive allosteric state. We term these "dead" variants. The dead variants are well-folded proteins that can bind to DNA and repress transcription but cannot be induced with ligand." The authors have made no measurements of protein stability. The only measurements made are cellular GFP levels in the presence and absence of the ligand. This needs a citation or some moderation of language.

3. Results page 6: "The evolution of aTFs has occurred through a series of gene duplication events resulting in mixing and matching LBDs and DBDs. " Citation needed.

4. Results page 6: "Thus, the DBDs likely exist as stand-alone domains that are not allosterically "wired" to the rest of the protein at the residue level but instead respond to large thermodynamic changes (e.g., inducer binding)." The data does not support this conclusion. The data suggests that the DBD is qualitatively depleted for mutations that abolish ligand-based activation while maintaining apo repression.

5. Results page 6: "Taken together, these observations show that although the hotspots are not superimposable across aTFs, the TetR-family likely share a conserved structural mechanism where the allosteric signal travels from the LBD through the dimer interface and a4 to the DBD, while the DBD itself acts as an internally rigid module that docks on DNA." This is speculation that seems more appropriate to the discussion (rather than results) section.

6. Results page 7: "These results also show that although allosteric hotspots may not be superimposable across distant homologs, local clusters of LRIs share similar patterns between homologs. As homologs get closer in sequence, regional similarities in allosteric signaling may give way to the superimposability of individual hotspots. " This again seems more appropriate to the discussion (rather than results) section.

7. Results page 8: "We concluded that the interaction energy of the large hydrophobic sidechains provides an enthalpic gain that stabilizes the allosteric OFF state of the protein." The thermodynamic mechanism of the mutations was not investigated in this study. We feel that it would be a stretch to form conclusions about enthalpy.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Deep mutational scanning and machine learning reveal structural and molecular rules governing allosteric hotspots in homologous proteins" for further consideration by eLife. Your revised article has been evaluated by the 3 original referees. I am glad to be able to inform the reviewers have decided to recommend that this work be published in eLife, pending revisions. As you will see below, one of the reviewers requires some additional clarifications in regard to the methodology, which might also help future readers to better appreciate the value of the work. Therefore we would like to offer you the opportunity to clarify these issues – which in my view would require editing of the manuscript and possibly moving Figure 1 S1 to the main text.

Reviewer #1 (Recommendations for the authors):

All the comments have been addressed satisfactorily in my opinion.

Reviewer #2 (Recommendations for the authors):

The revised manuscript addresses my comments/suggestions, and I think of the other reviewers as well. The paper is an excellent contribution to the literature in an important area and can be accepted as is. It is also an additional highly innovative and original work by the authors.

Reviewer #3 (Recommendations for the authors):

Thank you to the authors for a substantial revision. I very much appreciated the additions to the flow and NGS preparation/analysis methods sections, the clarifications on chip-based library construction, the more complete analysis of replicates, and the specification of the equation used to score allosterically dead variants. I also found the comparison to the ohm server predictions an interesting addition. As stated in my first review, the questions the authors seek to address – both (1) how allostery is implemented across homologs and (2)what physicochemical factors distinguish allosteric hotspots – are timely and fundamental open problems in protein biophysics. The paper contributes an enormous amount of experimental data, and the strategy of using machine learning to identify relevant features that distinguish hotspots is creative and leads to interesting results.

However, I still have substantial reservations about two aspects of the data analysis that persist from my earlier review. These are considerable enough that in parts of the manuscript I do not feel that the data support the authors' conclusions, but rather suggest something different. The first is that the strategy for deciding which mutations are allosterically dead still just doesn't make sense to me. I really might be missing something here; maybe the authors can explain. The second lies in the usage of quartiles to assign allosteric hotspots, and how this impacts the two constructs with a more limited allosteric dynamic range (RolR and TtgR).

Major concerns:

1. Strategy for assigning allosterically dead mutations. I appreciate that the authors clarified in their revisions that sequencing reads were normalized across replicates, experimental conditions, and proteins. These normalizations make sense to me, and I see that this helps in comparing counts. I also appreciate the authors' statements that "we use cell sorting as a binary classifier" and that by counting the number of dead mutations at a position they safeguard against noise in the data. Their point is well-taken that they seek to categorize mutations as allosterically dead/not dead, rather than using the flow data as a quantitative high-resolution measure. But I am still really stuck on understanding the use of a single threshold of 5 (or 10) to assess if a mutant is present in both the uninduced and induced sorted populations, and therefore assign it as allosterically dead. To illustrate, consider the following scenario. Let's imagine the authors ALSO sequenced the sorted induced fluorescent population (in addition to the induced nonfluorescent population). Now consider two different mutations with the following read distributions:

a. Mutant "A": 10 reads in the uninduced population, 10 reads in the induced non-fluorescent population, and 0 reads in the induced fluorescent population.

b. Mutant "B": 1000 reads in the uninduced population, 10 reads in the induced non-fluorescent population, and 900 reads in the induced fluorescent population.

If I understand correctly, both mutants would be classified as allosterically dead according to the authors' method. This makes sense for Mutant A, but for Mutant B…. it looks like it activates, just not completely, or maybe there is some noise in the sorting data. Is it obvious that if there are five or ten reads present it truly isn't noise? (How often do the authors observe "impossible codons" – meaning codons that are not part of their chip-based library – in the induced non-fluorescent population? This might set the noise threshold?) My impression is that the single threshold approach used by the authors may overestimate the number of "dead" mutations. It seems like it would be more correct to consider the ratio of the number of reads in the induced, sorted, non-fluorescent population relative to the number of reads in the uninduced population. One could then plot the distribution of this ratio (or maybe the log ratio), and apply a threshold to that ratio, rather than to threshold the absolute number of reads.

2. Strategy for assigning allosteric hotspots. Here the authors take the top quartile of residues according to their weighted positional score (that accounts for the number of dead mutations at a position as observed across replicates). By definition, this means that for each homolog, one-quarter of positions (however many were scored) will be called "hotspots". This seems consistent with what the authors report – for a length of 200 protein, you should then get about 50 hotspots. For RolR, which seems to be a bit longer, they get a few more (57 hotspots). So when they write that "changing the threshold (for assessing allosterically dead) has a modest impact on the overall number of hotspots" it is not really evidence of the robustness of the threshold choice – it is just that they are still taking the top quartile. If I understand correctly, they could use pretty much any strategy they like for assigning allosterically dead/not dead mutants and the number of hotspots would be about the same. That seems like an unusual feature of the analysis choice to me.

Now, the challenge is what happens when they consider TtgR and RolR. These are the two mutants with the least dynamic range in the assay (25-fold for TtgR, 15-fold for RolR, vs 49-fold for TetR, and 100-fold for MphR). When looking at the data in figure 1 supplement 2, it is clear that TtgR and RolR seem to have fewer allosterically-dead mutations per position. The matrices are overall less "stripey" in the vertical direction than TetR and MphR. So, when they take the top quartile of positions for TtgR and RolR to define allosteric hotspots, the cutoffs are much lower (~0.25-0.3) than for TetR and MphR (~0.8 or so, based on figure 1 supplement 3). As a consequence, what it means to be a hotspot in RolR or TtgR seems to be different than what it means in TetR and MphR. Indeed, my interpretation of the data (based on the heat maps in figure 1 supplement 3) would have been that RolR and TtgR just have fewer hotspots overall. This quartile-based definition of hotspots may explain a number of unusual features for RolR/TtgR, including the fact that: (1) the hotspot distributions are more diffuse across the sequence and structure (Figure 1) (2) that the F-scores are lower (they are less easily distinguished by physical properties), and (3) that the GA-NN model is less compelling. IMO, the reason that the GA-NN does less well for RolR/TtgR is that the training data is labeled improperly… basically, many of the positions they are calling hotspots are just not really hotspots. I feel like this is a far simpler explanation for differences in behavior for RolR and TtgR, rather than the authors' proposal that "… these differences might suggest a higher level of complexity in the allostery mechanism in TtgR and RolR, in which the hotspot resides may contribute to both intra-domain properties and inter-domain coupling". More generally, I think the choice of top-quartile means that what the authors compare across homologs is not truly apples-to-apples.
