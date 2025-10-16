# Peer review - Round 1

Editors:
- Frederic Pincet, https://ror.org/05a0dhs15 Ecole Normal Superieure France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.76356.sa0](https://doi.org/10.7554/eLife.76356.sa0)

Using all-atom molecular dynamics simulations to visualize the pre-fusion primed state during synaptic vesicle fusion is very original and this approach will certainly be used by others in the future. This work provides new insights into the protein organization prior to vesicle fusion that will help better understand the mechanisms of vesicle priming and evoked-release.


---

# Peer review - Round 1

Editors:
- Frederic Pincet, https://ror.org/05a0dhs15 Ecole Normal Superieure France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.76356.sa1](https://doi.org/10.7554/eLife.76356.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "All-atom molecular dynamics simulations of synaptic vesicle fusion I: a glimpse at the primed state" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Vivek Malhotra as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Ben O'Shaughnessey (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) Manuscript readability

a. the manuscript should be shortened. This notably applies to the Results section.

b. the manuscript should better focus on the relevant conclusions relative to the SNAREs (degree of zippering, juxtamembrane linker – lipid interactions), synaptotagmin and complexin. These modifications will be an opportunity to discuss the results in view of other simulations, i.e. coarse grain approaches accessing fusion timescales.

2) Limitations of all atom MD simulations

a. At the molecular level, the assumptions regarding the initial arrangement of the proteins and the missing aspects (e.g. Munc13, Munc18, Syt linkers, Cpx-SNARE interactions) must be explicitly stated and discussed in view of the current knowledge in the field.

b. Realistic statements about likely fusion times need to be compared to the all-atom simulation times.

3) "Primed" state

a. The term "primed", used in the title and in the manuscript is misleading because other core synaptic proteins are not included in the simulations.

b. It is difficult to assess whether the vesicle in the proposed molecular arrangement is actually primed. On the contrary, given the narrow intermembrane distance with molecular contacts, it is very likely the membranes will ultimately fuse. All-atom simulations cannot reach the relevant time scales to be conclusive.

c. The Cpx accessory helix looks like a wobbly finger unlikely to support much force.

4) Calcium addition

a. Calcium-phospholipid may play an important part in the molecular arrangement and the fusion process. This is ignored here and should be addressed.

b. How does one reconcile that the aliphatic loops on Synaptotagmin C2B domain do not insert into the membrane upon calcium binding as observed in previous structural/functional studies?

Reviewer #1 (Recommendations for the authors):

1) It is difficult to assess if the results from simulations are a true representative of the biological process or an outcome of the initial condition/constraints chosen. For example, it is puzzling that there is no intra-molecular assembly of the SNAREpins during the simulation even though the coil-coil interactions are expected to occur in the simulation time scales. It appears, in almost all cases, that the SNARE zippering is unaltered at the end of the simulation. Also, it might be possible that the authors' choice to model the juxtamembrane region as a fully unstructured region prevents membrane fusion under the current simulation conditions. While it is not clear if the SNAREs zippering extends through the juxtamembrane (JM) region into the transmembrane region as observed in the crystal structure of full-length SNARE (Stein et al. Nature 2009), it stands to reason the JM region needed to be at least partially structured for effective force transfer to catalyze merging of the bilayers.

2) A major conclusion of the report is that the steric clash between Complexin accessory helix and vesicle serves as the fusion clamp and indeed drives the positioning of the SNARE and Synaptotagmin on the planar bilayer. However, there are a couple of factors that might alleviate or even mitigate this steric clash: (i) the vesicle and bilayer are positioned at ~2.3 nm apart at the beginning of the simulation. However, high-resolution cyroEM analysis in synaptosomes/cultured neurons (Fernandez-Busnadiego, R. J Cell Biol 2013; Radhakrishnan et al. PNAS 2021) show that the inter-bilayer distance of docked/primed vesicle is ~4.5 nm. Thus, it might be imperative to carry out the simulation with the physiological accurate inter-bilayer distance (ii) Complexin molecule has been positioned on SNAREs assuming a fully-zippered SNARE complex. However, there is sufficient evidence that SNAREs are likely only partially-assembled in an RPP vesicle (Hua & Charlton, Nat Neurosci 1999, Prashad & Charlton, PLoS One, 2014), and the positioning of the CPX, esp. the accessory helix is correlated to the extent of SNARE assembly (Choi et al. ELife 2016, Kummel et al. Nat Struct Biol 2011; Zhou et al. Nature 2017). Furthermore, accessory helix has been shown to interact with c-terminal ends of t- and v-SNARE molecules (Kummel et al. Nat Struct Mol Biol 2011; Malsam et al., Cell Reports 2020). Thus, it is possible that the alternate positioning of the accessory helix and other interactions might reduce the observed steric clash.

3) How does one reconcile that the aliphatic loops on Synaptotagmin C2B domain do not insert into the membrane upon calcium binding as observed in previous structural/functional studies (Grushin et al. Nat Comms 2019; Kuo et al. J Mol Biol 2009) even though synaptotagmin interacts with the membrane, including partial insertion of the C2B aliphatic loop, under calcium-free conditions. This is a rather crucial and missing piece considering that calcium-triggered membrane insertion is predicted to be the driving force for triggered fusion.

Reviewer #2 (Recommendations for the authors):

1. The authors' major conclusion is that the AA simulations support the model of Voleti et al. for the organization that clamps fusion in the pre-ca primed state. However, from Figures 3, 4 (and associated figure supplements) fusion seems very likely not to be clamped, given the vesicle contacts the planar membrane (the degree of contact is still growing at the end of the simulation, Figure 4 supp 4). As stated in (lines 420-425) the vesicle membrane is not flattened. This indicates a lower force than with SNAREs alone, but seems unlikely to block fusion. Due to running time limitations, AA simulations cannot test if fusion would occur in a physiological time. The structure does not keep the membranes apart, as it rotates and permits contact. The authors are clear about this – indeed, to predict the orientation is stated as a major objective. But the conclusions of lines 365-367 and the final sentence of the abstract, suggesting these results demonstrate a fusion clamp, seems unjustified as far as I can see. The emphasis on the cpx accessory helix role also appears somewhat exaggerated, as if on its own it provides a mini-buttress that separates vesicle and planar membrane. It's hard for me to imagine it supports much force in this configuration.

2. The simulations with bound calcium (final section of Results) seem inconclusive. The number of contacts is still growing at the end of the simulation, and we cannot know if the C2B will ever dissociate from the SNAREs. It's very reasonable to try this simulation but given the outcome I'm not sure a long section is merited, particularly with the tentative title "Potential effects of Ca2plus binding to synaptotagmin-1." This negative, albeit interesting finding, might be briefly summarized in the main text.

3. The manuscript would be strengthened by a more balanced presentation acknowledging the limitations of AA simulations (while of course still extolling their merits) and connecting to some degree with analysis on other scales, including coarse-grained approaches beyond MARTINI. SNARE-mediated fusion was studied using ultra coarse-grained (Mostafavi et al., 2017; McDargh et al., 2018) and even continuum (Manca et al., 2019) representations. Every approach has strengths and weaknesses. AA approaches scrutinize local issues as no others can, but presently they are remote from being able to demonstrate hemifusion, fusion, unclamping and ca-evoked fusion. Making matters worse, NT release is clearly stochastic, so multiple runs are needed for each condition. These limitations are apparent in this study: almost every conclusion comes with a caveat related to running time. In previous seminal MARTINI studies that achieved fusion (Risselada, Sharma and Lindau) the conditions were intentionally biased for fusion (vesicle size, lipid composition, temperature, helical LDs) or nanodiscs were used. In (Risselada, 2011) no fusion was observed when the LD was made unstructured.

In the Introduction the authors assert that experiments suggest "..the fusion step occurs in just a few microseconds," which timescales AA simulations may be able to access. They quote the 60 microsec delay times (ca influx to first sign of the excitatory post synaptic current, EPSC) reported by Sabatini and Regehr at 38 degrees. However, 0.5 -2 ms is much more typical in the literature (admittedly, the 38 degrees study is distinguished by the temperature being physiological.) Related, long-ago Katz argued other processes (e.g. NT diffusion across the synaptic cleft) are much faster than NT release (Katz and Miledi, 1965).

4. In simulations with SNAREs only, the SNARE complexes are cleared laterally, and the membranes are squashed together, generating an ECZ (extended contact zone, a flat portion of vesicle), Figures 1C, 1F. This is precisely the behavior seen in highly coarse-grained simulations (Mostafavi et al., 2017, Mcdargh et al., 2018), where entropic SNARE-SNARE and SNARE-membrane forces cleared the fusion site and pressed the vesicles together (those studies used undeformable membrane surfaces, so no vesicle flattening occurred). The entropic forces were predicted to provoke fusion after a time of order msec, with faster fusion for more SNAREs. These coarse-grained simulations and their relation to the present findings should be discussed.

The authors suggest the pressing together of the membranes is caused by binding of the LDs to the vesicle membrane (lines 262-266). This does not seem a plausible alternative to the proposed entropic forces, as LD-membrane adhesion would not favor the SNAREs being pushed outwards as far as I can see.

The authors argue that the ECZ in the SNARE-only simulations suggests SNAREs alone cannot fuse membranes rapidly, since fusion was slow in Hernandez et al., 2012 and Witkowska et al., 2021 where ECZs were seen. However, in those in vitro studies many other processes preceded fusion (SNARE assembly, docking etc) and micron scale GUVs were used by Witkowska et al.

5. A concern is the presentation, whose clarity would benefit from a more concise text. It is laudable to convey the details (computational papers where readers cannot tell what was done are frustrating), but many passages are long repeats of previous passages. For example, opening paragraphs of sections in Results often repeat descriptions of simulations in previous sections at great length, then specifying what was different in the current section. These could be massively shortcut. Short summaries in the main text, with details left to Methods or Supplementary materials, would be more digestible for readers.

6. This paper describes many current hot issues in the field, a great service. The figures are very nice but would be helped by a simple visual key to identify β sandwiches, the polybasic face, ca-binding loops, etc. For an uninitiated reader, it is tough staring at these protein structures trying to figure out which features are where? Also, I suggest adding a length bar to one or more Figures

7. It is stated that the Cpx accessory helix inhibits release "likely" because it causes steric clashes with the vesicle (line 85). I think this is a powerful and very reasonable suggestion, but perhaps "possibly" would better reflect current uncertainty about the mechanism.

8. Their 26 nm diameter vesicles are ~ 2-fold smaller than synaptic vesicles. I do understand why this measure is taken (and the authors mention why), but the synaptic vesicle size should be stated.

Reviewer #3 (Recommendations for the authors):

My overall sense from this study is that the simulation efforts are preliminary and sufficiently incomplete to cause concern about the validity of the conclusions. I am concerned about several omissions and their potential impact on conclusions about the prefusion complex and the possible trajectories leading to fusion:

1. SNARE/Syt/Cpx omissions – What is the potential impact of removing the Habc region of syntaxin 1 given its significant excluded volume and potential interactions with membrane PIP2? Similarly, excluding the palmitoylated linker regions of SNAP-25 may play important and interesting roles affecting SNARE orientation, the distribution of forces between SNAREs and membranes, and membrane behavior. The lack of a Syt1 juxtamembrane region (as well as its transmembrane anchor) seems like a real missed opportunity given past work suggesting several interesting hypotheses for intramolecular and membrane interactions of this region. Finally, omitting the C-terminal domain of Cpx1 with its known membrane-interacting region may have significant implications for the detailed behavior of Cpx1 and the forces acting on its SNARE-binding region. While no realistic simulation could currently hope to capture all of this, I would have preferred fewer simulations with more assessment of whether or not some of these omissions would cause major changes to the behavior of the simulated system.

2. Calcium-phospholipid interactions – When the authors included 5 calcium ions per Syt1 to assess the impact of elevated local calcium on the simulation dynamics, I was struck by a lack of corresponding calcium interactions with PS and PIP2. 20 calcium ions in the simulated volume would roughly correspond to 1 mM calcium, and even that wouldn't necessarily lead to all 20 potential binding sites on Syt1 being occupied. At the same time, one would expect divalent interactions with PS and PIP2, which could neutralize membrane repulsion and significantly lower at least one aspect of the complex membrane fusion energy barrier. Work by chemists such as Feigenson have indicated strong calcium-mediated interactions between even PS and PC at concentrations much lower than 1 mM (Biochemistry 1989). Some of these chemical details may not be capable of proper simulation in the MD formalism deployed in the current study, but this should be addressable in some fashion.

3. I was not convinced by the authors' reasoning regarding one microsecond being a relevant timescale for synaptic vesicle fusion. And given that even some initial phase of membrane fusion was not observed in these simulations, I find it impossible to access wherein the process of priming/fusion these current simulations reside. The fastest reported latency between presynaptic calcium entry and fusion is around 60 microseconds as the authors point with the Sabatini/Regehr study. Importantly, that was not a single-synapse measurement but instead, a population measure involving 1000s of synapses. So the first latency likely represents a small population from the fast tail of a distribution of fusion times. And given the 1-2 microsecond delay for cleft glutamate diffusion and the 10-20 microsecond activation time of a stellate cell AMPA receptor, it is likely that the calcium-fusion delay at this synapse resides in the 50-100 microsecond time window. Thus, a 400-nanosecond simulation would seem far too brief to do this process justice.

4. Since the simulations are certainly not trying to capture relevant roles and impacts of other core synaptic proteins such as Munc13 and Munc18, I thought that the use of 'primed' state was a bit oversold and misleading in this manuscript. These simulations seem most appropriate for interpreting in vitro liposome fusion experiments utilizing just SNAREs or SNAREs plus Cpx/Syt1. I am not sure what it would mean to describe a primed state for the SNAREs and synaptic vesicle without also having Munc13 present and bound at least to the two membranes if not also to the SNAREs. I appreciate that the authors are modeling something that represents our best guess for the SNARE assembly on a tightly docked and primed vesicle, but this simulation clearly lacks crucial elements that go into what the field usually refers to as a primed synaptic vesicle. I would want the language used to reflect this as much as possible.

5. I do not have a sense for how worrisome it is from a technical perspective to forgo replicate simulations. For instance, is it better to have two replicates each of three simulations rather than six slightly different simulations each done once? It would be useful to have some discussion of the uncertainty/reliability attached to these conclusions given the absence of replicates.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "A glimpse at the primed Synaptotagmin-SNARE-complexin complex from all-atom molecular dynamics simulations" for further consideration by eLife. Your revised article has been evaluated by Vivek Malhotra (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below.

Please address the points brought up by Reviewer #3 on the primed state and on calcium/lipid interactions, at least at the writing level. To avoid ambiguity, it would be better to remove the word 'primed' from the title, lines 34 and 37 in the abstract, and line 129 in the introduction, and change the corresponding sentences when needed. This is probably not sufficient because there are so many mentions of 'primed states', primed complexes', or 'vesicle priming'.

Regarding the interactions of calcium with lipids, we realize that getting computational time is a limiting and costly resource currently. Asking to perform additional simulations involving lipid/calcium interactions may be difficult but the authors can certainly mention that it is a limitation of their simulations that may affect the outcome and should be tested in the future.

Reviewer #3 (Recommendations for the authors):

Rizo and colleagues have shortened and edited their manuscript as requested in the first review. I wasn't strongly enthusiastic about this MD study during the first round and remain somewhat dissatisfied after reading the authors' response to our concerns. Two of my concerns were largely ignored by the authors in their rebuttal but remain worrisome to me nonetheless.

One concern is the authors' continued declaration that their simulations are synonymous with the primed fusion complex. Vesicle priming is already a somewhat muddled concept in the field and this manuscript doesn't help the confusion. I appreciate that they edited their title a bit but anyone glancing at the paper or searching for it on PubMed would very likely interpret this as the primed state prior to fusion. In addition, they conclude in the abstract (line 37) that 'the primed state contains macromolecular assemblies …' whereas I don't believe the simulations warrant this conclusion. This is reiterated in the last sentence of the introduction (line 129-132) but at least they soften the conclusion with 'suggest that'. I am not sure the authors got that much more out of the model than they put in to begin with since they chose starting points that they were already convinced represented their best guess at the primed state of the fusion complex. Perhaps some of the observations regarding the juxtamembrane linkers of the SNAREs are moderately unexpected, but given that no fusion was witnessed, the reader doesn't know which details of the current model truly correspond to relevant prefusion scenarios.

My other concern is that the authors continue to ignore the very real possibility that calcium interactions directly with the phospholipids (independent of Syt1 C2 domains) are a critical aspect of membrane fusion. This has been studied chemically and using in vitro membrane fusion assays for 50 years but wasn't even discussed as a possible explanation for the lack of fusion in the simulation where calcium was included. Just to be explicit, I am thinking of papers such as Papahadjopoulos BBA 1976, Feigenson Biochem 1986,1987, and 1989 studies, Kachar Biophys J 1986, and modern studies such as Churchward Biophys J 2008. While I don't know what the technical limitations of implementing calcium-phospholipid interactions are in all-atom MD, I can find examples in the literature such as Allolio and Harries ACS Nano 2021 and Allolio et al. PNAS 2018 where calcium ion interactions with phospholipids during membrane fusion are explicitly incorporated, so I assume there isn't a fundamental reason this cannot be explored or acknowledged. I don't think it would be surprising if some of the key results here such as the juxtamembrane linker electrostatic interactions with the membrane would be strongly affected in addition to the possibility that the fusion energy barrier would be lowered sufficiently to witness the beginning of a fusion event on a microsecond time scale.

Overall, this was a nice first effort at an ambitious simulation scale and could serve as an introductory template for future attempts at modeling SNARE-mediated fusion. The preliminary and underdeveloped feel of the manuscript and notably, the lack of some sort of fusion-like transition captured in the simulations diminish my enthusiasm a bit.
