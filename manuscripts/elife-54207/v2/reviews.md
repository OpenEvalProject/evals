# Peer review - Round 1

Editors:
- Pimchai Chaiyen, Vidyasirimedhi Institute of Science and Technology (VISTEC) Thailand

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.54207.sa1](https://doi.org/10.7554/eLife.54207.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This work has expanded the understanding of isoleucine biosynthesis. It highlights flexibility and interconnectivity of main and alternative metabolic pathways. The knowledge should be useful for further development in the fields of systems biology and metabolic engineering.

Decision letter after peer review:

Thank you for submitting your article "Underground isoleucine biosynthesis pathways in E. coli" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Michael Marletta as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Yew Wen Shan (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The manuscript by Cotton et al. presents mechanisms underlying microbial adaptation to evolve alternative rescue pathways when the main Isoleucine biosynthesis pathway in E. coli is disrupted. Cells in which threonine deaminases have been deleted are still able to grow, implying that another source of 2-ketobutyrate for synthesis of isoleucine must be available. The authors demonstrated that within the proto-typical microbe, Escherichia coli, isoleucine auxotrophy can be complemented/compensated by multiple pathways. As the disruption was carried out at the step of 2-ketobutyrate production, the cell uses other enzymes, MetB mainly under aerobic where the provision of the critical metabolite is done by succinyl-homoserine cleavage, and pyruvate format lyase (PflB/TdcE) to provide 2KB under anaerobic conditions by the condensation of propionyl-CoA.

Overall, the work is well written and the results are quite interesting. The authors make a good case that the enzymes responsible for rescuing growth differ when the cells are grown under aerobic vs anaerobic conditions. The suggestion that a significant amount of 2-ketobutyrate may be produced from propionate in the anaerobic conditions in the mammalian gut is particularly intriguing. The work contributes an elaboration of "underground metabolism" where latent metabolic pathways catalyzed by promiscuous enzymes can be activated given the right metabolic/physiological conditions.

However, there are many issues need to be addressed clearly (especially the issues mentioned in the first two comments). Otherwise, the manuscript would not be accepted for publication in eLife.

Essential revisions:

1) The authors report that replicate cultures of ∆ilvA∆tdcBE. coli, which lack both threonine deaminases, begin to grow at different times, yet genome sequencing reveals no mutations. The authors claim that the is due to "stochastic adaptation of cellular metabolism". This doesn't make sense; typically this kind of result is seen when mutations are required, and they occur at different times in different tubes. Transcriptional changes in response to growth conditions typically happen very quickly, and within the same time frame for replicate cultures. Further, the methionine synthesis genes should be turned on already in minimal medium, so it is not clear what other changes would be contributing. This is a major problem with either the data or the interpretation that needs to be rectified.

2) According to Ecocyc, MetC is an essential gene and strains lacking MetC cannot grow on glucose as a sole carbon source. Thus, the observation that the ∆5 ∆metC strain can grow without addition of methionine is puzzling. Did the authors confirm that metC is really absent? Either there is an interesting and non-obvious mechanistic explanation, or the work was not done properly.

3) It is odd that cells grown under aerobic conditions can recruit MetB to synthesize 2-ketobutyrate, while cells grown under anaerobic conditions apparently do not. MetB should be expressed under both conditions. A good explanation for this counter-intuitive finding is necessary.

4) The text in several places says that enzyme x can catalyze reaction y. For example, subsection “2-ketobutyrate biosynthesis from succinyl-homoserine” says MetB catalyzes both condensation of o-succinylhomoserine and cysteine and cleavage of o-succinylhomoserine to succinate and 2-ketobutyrate. In every case where such statements are made, it is important to provide values for kcat and Km, either from the literature or from experiments carried out in the course of this work.

5) Actual values of Ki for the inhibition of o-succinylhomoserine cleavage by MetB in the presence of cysteine and homocysteine should be determined. These values should be compared to the actual concentrations of cysteine and homocysteine in cells. The single concentrations used in the experiments shown in Supplementary Figure 1B are far above the concentrations that I would expect to be present in cells.

6) Subsection “A latent aerobic isoleucine biosynthesis pathway” paragraph four: Is it ok to ignore flux through the pentose phosphate pathway when considering labeling patterns after growth on 13C-labelled glucose? Considerable flux goes through it.

7) The postulated propionate formate lyase activity of pyruvate formate lyase should be quantified in vitro.

8) Results section and Figure 3, in order to establish that the lack of 2-ketobutyrate is a major cause for the phenotype observed in Figure 3. A simple experiment such as adding 2-ketobutyrate, not isoleucine, into the growth medium to identify if adding 2-ketobutyrate gives the same effect as adding isoleucine would be helpful to confirm the role of 2-ketobutyrate in the mutants.

9) Subsection “2-ketobutyrate biosynthesis from succinyl-homoserine”: Why did the authors not construct the mutant in which MetB was deleted to confirm the conclusion made about MetB?

10) Subsection “Enzyme assays”: MetB assay needs clearer description about product measurement. The ability of MetB to generate 2-ketobutyrate should be measured by HPLC/MS (which the authors did with the inhibition experiments). For MetB kinetic assays, the authors described the measurement by monitoring NADH consumption. It is not clear how the assay is linked to 2-ketobutyrate formation.

11) Subsection “Enzyme assays” describes the assay used for MetB activity. The MetB elimination reaction they are considering produces 2-ketobutyrate, which is apparently being detected with lactate dehydrogenase, which normally uses pyruvate as a substrate. Does lactate dehydrogenase turn over 2-ketobutyrate? Did the authors ensure that the amount of lactate dehydrogenase was sufficient so that they were actually assaying MetB activity? Paragraph five says that "succinate, pyruvate and 2-ketobutyrate in the enzymatic assays were quantitatively determined by LC/MS/MS.” This statement is not consistent with the described use of lactate dehydrogenase.

12) In the presence of substantial genetic, growth and complementation assays, the work should benefit from the in vitro enzymatic demonstration of activity of TdcE and PflB.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Underground isoleucine biosynthesis pathways in E. coli" for further consideration by eLife. Your revised article has been evaluated by Michael Marletta (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

All reviewers think that the manuscript is very much improved and presents convincing evidence for the existence of alternative pathways for synthesis of 2KB. However, one of the reviewers note that a solid explanation for how the mutations increase flux through alternative pathways for 2KB synthesis should be provided because this is an important missing piece of the puzzle.

Essential revisions:

1) The mechanism by which the mutation in CysE improves synthesis of 2KB is puzzling. It seems logical that decreasing the concentration of cysteine would increase the rate of cleavage of O-succinyl-L-homoserine to 2KB and succinate. However, the mutation appears to decrease the cysteine concentration by only 44%. (There is enough variability in the data that this is not a totally convincing finding; the p value for the difference between the ∆5 and the ∆5 cysE* strains is 0.16.) In other data, the authors show that, in the presence of cysteine, O-succinyl-L-homoserine is converted entirely to cystathionine and succinate (the normal intermediates in the methionine synthesis pathway). Therefore, it would not be expected that O-succinyl-L-homoserine is cleaved to 2KB and succinate in vivo in the presence of a substantial amount of cysteine. Can the authors come up with a good explanation? For example, is it possible that both the CysE mutation and the metC deletion lower methionine levels, which then would lead to increased transcription of metB? Decreasing MetC activity might also lead to an increase in the concentration of O-succinyl-L-homoserine, which could help push material toward 2KB synthesis. It would be nice if this could be verified by metabolomics.

2) Gels showing the purity of isolated enzymes should be included in the supplementary material.

3) Subsection “2-ketobutyrate biosynthesis from succinyl-homoserine” final paragraph and legend to Figure 5—figure supplement 1 – it is not correct to say that cysteine inhibits MetB. Cysteine is a substrate for MetB. It doesn't really inhibit cleavage of O-succinyl-L-homoserine to 2KB and succinate. It's just that the intermediate formed by reaction of O-succinyl-L-homoserine with the PLP cofactor at the active site of the enzyme is directed toward a different fate in the absence of cysteine.

4) In subsection “Disruption of MetC or a mutation in serine acetyltransferase enable steady 2-ketobutyrate production from succinyl-homoserine” – the text reports an apparent kcat for CysE and A33T CysE. According to the Materials and methods section, these enzymes were assayed with only a single concentration of substrates (20 mM serine and 0.2 mM acetyl CoA). In the absence of information about the Km for each substrate for the wild-type and mutant enzymes, it is not obvious that the values measured are truly kcat, particularly if the Ala33Thr change has a significant effect on a Km. (This is mostly a concern for acetyl CoA, since the concentration of serine was quite high.) Also, for the purpose of interpreting the effect of the mutation, it is necessary to determine whether the enzyme is saturated in vivo (i.e. whether it is kcat or kcat / Km that is the physiologically relevant parameter),

5) Subsection “Anaerobic 2KB biosynthesis from a reversible 2KB formate-lyase activity”: – activity should be given in terms of kcat rather than specific activity.

6) The KBFL pathway appears to be a major pathway for production of 2KB under anaerobic conditions. Therefore, it isn't really an underground pathway. Maybe it should be called an auxiliary pathway?

7) Proper terminology for the chemical intermediates should be used (e.g. succinyl homoserine should be O-succinyl-L-homoserine).

8) Subsection “Enzyme assays for MetB, MetC, and CysE” paragraph four: – a reference should be provided for the statement that lactate dehydrogenase can reduce 2KB.

9) Table 2 – ∆ilvA ∆tdcB should be threonine deaminase deletion strain.
