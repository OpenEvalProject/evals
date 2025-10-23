# Peer review - Round 1

Editors:
- Marcel P Goldschen-Ohm, University of Texas at Austin United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.74306.sa0](https://doi.org/10.7554/eLife.74306.sa0)

The authors use a combination of photolabeling and mass spectrometry to probe polyunsaturated fatty acid (PUFA) binding site locations in the pentameric ligand-gated ion channel (pLGIC) ELIC. The data strongly support the idea that DHA, but not PA, bind in the transmembrane domains of ELIC in two locations that overlap with that previously shown for the homolog GLIC. They also show that coarse-grained simulations can recapitulate the observation that DHA and not PA bind in this region, supporting the idea that such simulations can be useful for studying PUFA interactions with pLGICs. Strikingly, the authors provide evidence that DHA binding depends on the occupancy of the agonist site, which is an important observation that informs on molecular motions in the transmembrane domains in response to agonist binding. This work contributes to understanding the molecular underpinnings of PUFA modulation in pLGICs.


---

# Peer review - Round 1

Editors:
- Marcel P Goldschen-Ohm, University of Texas at Austin United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.74306.sa1](https://doi.org/10.7554/eLife.74306.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for submitting your article "Polyunsaturated fatty acids inhibit a pentameric ligand-gated ion channel through one of two binding sites" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Marcel P Goldschen-Ohm as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Richard Aldrich as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Pierre-Jean Corringer (Reviewer #2); Michaela Jansen (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) For all plots with mean +/- SEM including dose-response relations and bar plots, please show all of the individual data points. Also report all statistical tests used in the figure legends.

2) Regarding KK-242, similar chemistry and compounds have been described previously (for review see Chemical Reviews 2013 113 (10), 7880-7929). It should be clarified whether the compound described herein is a new chemical entity or whether it has been generated previously (Beilstein search?).

3) Given that ultimately the authors suggest that the DHA site in ELIC is similar to that in GLIC, a figure that compares the observed binding site in the GLIC structural model and the proposed binding site(s) in ELIC would be very helpful to orient readers.

4) The observation that DHA inhibition depends on agonist site occupancy is very interesting. However, please address the following concerns regarding this data: i) At the concentrations used the authors are looking for a reduction in a signal that is already only ~1%. If these concentrations were necessary to observe the effect, please comment on why that is. ii) It is not clear that there is any reason to normalize the data shown in Figure 4C to the 0 PUFA conditions (in any event, it is not clear how they were normalized as the data don't seem to be from paired experiments). Unless there is a compelling reason otherwise, the data in Figure 4C should be plotted as raw labeling efficiencies (no normalization) and all data points in the absence of PUFA should be shown. iii) Given the variation in labeling efficiency reported in Figure 4-S3, n=3 data points is on the low side. If feasible, another couple of data points would likely help greatly to solidify this dataset, although we appreciate that these may be difficult experiments. iv) How were the data in Figure 4C analyzed? ANOVA?

5) The suggestion of two possible docking sites based on observed photolabeling at Q264 in M3 and C313 in M4 seems entirely dependent on the choice of docked conformations. However, it is not clear how representative the docked poses shown in Figure 4A and B are to the collection of docked poses obtained. Do the vast majority of docked poses cluster tightly around these two poses, or not? A figure illustrating this would be very useful. Also, it is difficult to judge how close the two docked orientations are as they are presented in separate images with different viewpoints. A single image showing both proposed sites on either side of M4 would be very helpful for visualizing what is being proposed in a larger context (e.g. something along the lines of how DHA and PLC are shown in Basak et al. Figure 3A).

6) Were peak responses of R117C-M before and after DTT incubation obtained from the same liposomes? If not, there is no control for expression, and controls to see whether DTT itself increases peak responses in control or in R123C-M are needed.

7) The logic by which the authors conclude that DHA modulates via a single site needs to be spelled out much more clearly. Presumably, because R117C-M has a PUFA like effect, this must be the site? But then why does DHA still modulate R117C-M to a similar extend as control and all other mutants? Also, why would the R118A substitution abolish DHA modification but not the methylester? Both remove essentially a single charge in this interacting pair that seems to be in salt bridge distance?

Reviewer #1:

The authors use photolabeling in combination with mass spectrometry to identify a binding site for the polyunsaturated fatty acid (PUFA) DHA in the pentameric ligand-gated ion channel ELIC. The identified site is similar to a structure of DHA bound to the homolog GLIC. Most strikingly, the authors show that DHA binding in ELIC is dependent on the agonist-bound state of the channel, which is an important observation that informs on molecular motions in the transmembrane domains in response to agonist binding. However, the data for the state-dependence of DHA binding, although suggestive, could benefit from either a clearer presentation or some additional investigation.

The authors use a powerful combination of photolabeling and MS to probe polyunsaturated fatty acid (PUFA) binding site locations in the pentameric ligand-gated ion channel (pLGIC) ELIC. The data strongly support the idea that DHA, but not PA, bind in the transmembrane domains of ELIC in a similar location to that previously shown for the homolog GLIC. They also show that coarse-grained simulations can recapitulate the observation that DHA and not PA bind in this region, supporting the idea that such simulations can be useful for studying PUFA interactions with pLGICs. Most strikingly, the authors provide evidence that DHA binding depends on the occupancy of the agonist site, which is an important observation that informs on molecular motions in the transmembrane domains in response to agonist binding. For me, this was the most interesting aspect of the paper. However, I also have some concerns about the evidence that is provided for this which need addressing (see below).

1. For all plots with mean +/- SEM including dose-response relations and bar plots, please show all of the individual data points. Also report all statistical tests used in the figure legends.

2. Given that ultimately the authors suggest that the DHA site in ELIC is similar to that in GLIC, a figure that shows this is a glaring omission. Please show a figure that compares the observed binding site in the GLIC structural model and the proposed binding site(s) in ELIC for comparison. In GLIC, DHA appears to not really extend much into the transmembrane domain. Thus, the similarity to KK-242 whose tail does extend down between M4 and M3 is not completely clear. This should be discussed.

3. The most striking advance for me is the observation that DHA binding depends on occupancy of the agonist site. Although the data presented for this are suggestive, I have some concerns:

i) Why was 10uM KK-242 used for DHA competition experiments? At this low concentration the labeling efficiency is really low to begin with. I am concerned about the reliability of measuring a reduction of a signal that is already only 1-2%, and that furthermore displays a fairly large range of deviation (Figure 4-S3). Does a higher K-242 concentration outcompete DHA?

ii) Perhaps I am misunderstanding the experiment, but I don't understand why the data in Figure 4C are normalized. I think they should simply be plotted as the observed labeling efficiencies in each condition and all data points in the absence of PUFA need to be shown. After the MS it's not like you can take that same sample and test it on another PUFA condition.

iii) Given the variation in labeling efficiency reported in Figure 4-S3, I am not completely convinced that 10uM DHA has much effect on labeling. Even though the effect at 30uM DHA looks fairly clear, I am still a bit concerned about having only three data points given such variability and low initial signals. I suggest obtaining at least another couple of data points as this is a crucial experiment regarding the state-dependent action of DHA.

iv) What is the statistical test indicated in Figure 4C? Probably should be ANOVA with some posthoc test.

4. The suggestion of two possible docking sites based on observed photolabeling at Q264 in M3 and C313 in M4 seems entirely dependent on the choice of docked conformations. However, it is not clear how representative the docked poses shown in Figure 4A and B are to the collection of docked poses obtained. Do the vast majority of docked poses cluster tightly around these two poses, or not? A figure illustrating this would be useful. In GLIC, DHA falls between two arginines that are similarly oriented to R117 and R123, so how unlikely is such an orientation in ELIC? Also, it is difficult to judge how close the two docked orientations are as they are presented in separate images with different viewpoints. A single image showing both proposed sites on either side of M4 would be very helpful for visualizing what is being proposed in a larger context (e.g. something along the lines of how DHA and PLC are shown in Basak et al. Figure 3A). Along these same lines, it is unclear to me that the photolabeling is not consistent with some flexibility in the tail position at a single site given that the photolabeled positions are quite close. If the photolabeling is truly strong evidence for two distinct sites, this needs to be explained further. Otherwise, I suggest presenting the data as consistent with two possible sites on either side of M4 analogous to DHA and PLC as observed in GLIC rather than direct evidence for two sites.

5. The logic of the final Results section on hMTS was a bit hard for me to follow. Firstly, hMTS mimics the PA tail (line 449), but PA does not bind here specifically? Second, no differences in peak current were observed between control and unmodified or modified cysteine mutants as assayed by ANOVA. Although I do agree that modification of R117C-M does seem like it exhibits smaller peak currents, I am a bit shaky on the idea of falling back to t-Test when ANOVA does not indicate a difference. More importantly, were peak responses of R117C-M before and after DTT incubation obtained from the same liposomes? If not, there is no control for expression, and DTT itself was not checked to see if it increases peak responses in control or in R123C-M. Thus, the evidence that hMTS inhibits ELIC currents analogous to a PUFA, although suggestive, is lacking controls. Regardless, the logic that DHA modulates via a single site is not spelled out sufficiently for me. Presumably, because R117C-M has a PUFA like effect, this must be the site? But then why does DHA still modulate R117C-M to a similar extend as control and all other mutants?

Reviewer #2:

This is a very compelling study identifying a fatty acid binding site mediating allosteric inhibition of ELIC. The study implements several complementary techniques that are all relevant to the demonstration:

1. Purification of ELIC and reconstitution in giant liposomes for excised patch voltage-clamp, showing that DHA inhibits ELIC channel function.

2. Design and synthesis of a new photolabeling reagent, KK-242, with optimal photochemistry with a structure resembling a fatty acid. Middle-down mass spectrometry show that KK-242 photolabels two distinct sites on both sides of the outer portion of M4, one at the interface with M3 (M3Q264 and M4R318), and one at the interface with M1 (M4C313). Importantly, KK-242 labelling is inhibited by DHA in a dose-dependent manner and only in the presence of the agonist. Thus, DHA preferentially binds to both KK-242 photolabeled sites when ELIC is in the agonist-bound state.

3. Using coarse-grained molecular dynamics (CGMD) simulations, authors determine two fatty acid binding sites in the outer TMD of ELIC that are specific for DHA over PA when agonist is bound to the channel, and that are overlapping with the one identified by photolabelling.

4. To investigate the functional significance of the M1 and M3 DHA binding sites, each site was covalently modified with hexadecyl-methanethiosulfonate (hMTS), mimicking the binding of a fatty acid, using the accessible arginines above the M1M4 and M3M4 groves. Electrophysiological analysis of ELIC cysteine mutants clearly show that the M3M4 site specifically mediates inhibition.

Overall, the study is carefully designed and conducted, very clearly presented and discussed, and the demonstration complete. It is a beautiful piece of work.

Reviewer #3:

Dietzen et al. investigated the interaction site/s and mechanism of the polyunsaturated fatty acid (PUFA) docosahexaenoic acid (DHA) with the prokaryotic pentameric ion channel ELIC using a novel fatty acid photolabeling reagent with broad amino acid reactivity coupled with mass spectrometry, coarse-grained molecular dynamics (CGMD) calculations, as well as covalent modification using a methane thiosulfonate (MTS) reagent with a lipid-like tail of engineered Cys at identified sites. The results are further probed using a DHA methylester derivative (DHA-ME), using competition photolabeling with palmitic acid (PA), and current simulations based on a previously published gating model.

The authors show that DHA or DHA-ME preapplication for 3 minutes reduces the peak current obtained with the agonist cysteamine. The cysteamine EC50 is unaltered. PA has a significant but much smaller effect. CGMD was used to calculate lipid diffusion, and identified localized areas of high enrichment for DHA in two intrasubunit groves between M4 and M1 or M3, respectively, mostly in the outer membrane leaflet. The distribution of PA was also calculated with the same method and found to be more diffuse, indicating that PA's functional effect is associated with unspecific rather than specific interactions.

In the next set of experiments the goal was to use photoaffinity labeling with suitable fatty acids and subsequent mass spectrometric identification to characterize PUFA binding sites. Initially, a commercially available bifunctional photoreactive reagent (pacFA) with an aliphatic diazirine was used. The authors find that PacFA did not label ELIC, likely because the hydrophobic transmembrane environment does not contain nucleophilic amino acid sidechains like glutamate or aspartate that are reactive towards the aliphatic diazirine. The authors subsequently design and synthesize the novel trifluoromethylphenyl diazirine compound, KK-242, that is expected to be more broadly reactive towards different amino acid side chains. KK-242 has a similar alkyl chain length compared to PA. In photolabeling experiments with KK-242 this compound labeled a single position in M3 (Q264), and two positions in M4 (C313 and R318). Docked in chemically meaningful poses KK-242 seems to bind to two distinct sites on either side of the outer portion of M4. The KK-242 carboxylate reaches to R117 when docked to Q264, and to R123 when docked to C313.

Previously, a co-crystal structure of GLIC with DHA was published (Basak et al., eLife 2017). Both GLIC and ELIC contain an Arg at the position corresponding to ELIC-R117. GLIC contains an additional Arg, R118, whereas ELIC contains an Arg at position 123, R123. Interestingly, the GLIC structure had the DHA carboxylate in close proximity to R118. The prior GLIC study showed that a R118A mutation is not inhibited by DHA, indicating that the R118, and consequently potentially a salt bridge between the DHA carboxylate and the R118 positive charge was required for DHA inhibition. On the contrary, the present study indicates that the methyl ester of DHA, DHA-ME, is able to inhibit ELIC. In this case, there would be no salt bridge between DHA-ME and Arg. The photolabeling was further interrogated with competition experiments with DHA and PA. These showed that photolabeling efficiency by KK-242 was dose dependently reduced for the M4 site with DHA but only insignificantly reduced with PA. CGMD simulation data confirms specific binding at M3/M4 intrasubunit grove for DHA, same site as R117, Q264. Additional binding with the M1/C313 is also identified. In summary, the photolabeling results are supported by the CGMD simulations.

In a separate set of experiments, in a Cys-less background R117C and R123C were modified with a MTS reagent with a lipid-like tail for investigation of the functional significance of sites. R117C modification with MTS reagent inhibited peak currents and the effect was reversed with reducing agent application (dithiothreitol, DTT) which will remove the covalently linked disulfide introduced by the MTS reagent. There was no effect of the covalent modification of R123C with the same reagent. Mass spectrometry for both positions indicated that both R117C and R123C were indeed modified at a comparable high level. This leads to the conclusion that while both positions are modified, only the R117C modification has a functional impact that can be observed with the electrophysiological experiments described here.

The authors further show that photolabeling was specific for the agonist bound state.

Simulations previously published by others and the present study also indicate that fatty acids in the presence of agonist may stabilize a pre-active or desensitized state of the channel.

In summary, the present study uses complementary approaches that identify two binding sites for the PUFA DHA within the extracellular leaflet on either side of the M4 transmembrane segment, with only a single site per subunit being responsible for the inhibitory effect.

Overall, the results recapitulate what has been described and published in eLife in 2017 with regard to DHA modulation of the closely related pentameric channel homologue GLIC using X-ray co crystallography, EPR and electrophysiology. The present paper uses a different set of approaches that are elegantly complementary to one another and overall corroborate the same findings. Of note, the GLIC co-crystal structure did show two lipid binding sites as well, one was occupied by DHA, the other by "PLC", a lipid carried with the purification. The newly-synthesized compound KK-242 is a promising tool likely attractive for the study of additional transmembrane proteins that are modulated by PUFAs.

Comments for the authors:

Similar chemistry and compounds have been described previously (for review see Chemical Reviews 2013 113 (10), 7880-7929), it should be clarified whether the compound described herein is a new chemical entity or whether it has been generated previously (Beilstein search?).

Statistics: the detailed results should be provided.

Why would the R118A substitution abolish DHA modification but not the methylester? Both remove essentially a single charge in this interacting pair that seems to be in salt bridge distance?
