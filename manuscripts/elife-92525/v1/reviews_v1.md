# Peer review - Round 1

Editors:
- Timothy E Behrens

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.92525.3.sa0](https://doi.org/10.7554/eLife.92525.3.sa0)

This potentially valuable study presents claims of evidence for coordinated membrane potential oscillations in E. coli biofilms that can be linked to a putative K+ channel and that may serve to enhance photo-protection. The finding of waves of membrane potential would be of interest to a wide audience from molecular biology to microbiology and physical biology. Unfortunately, a major issue is that it is unclear whether the dye used can act as a Nernstian membrane potential dye in E. coli. The arguments of the authors, who largely ignore previously published contradictory evidence, are not adequate in that they do not engage with the fact that the dye behaves in their hands differently than in the hands of others. In addition, the lack of proper validation of the experimental method including key control experiments leaves the evidence incomplete.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.92525.3.sa1](https://doi.org/10.7554/eLife.92525.3.sa1)

(1) Significance of the findings:

Cell-to-cell communication is essential for higher functions in bacterial biofilms. Electrical signals have proven effective in transmitting signals across biofilms. These signals are then used to coordinate cellular metabolisms or to increase antibiotic tolerance. Here, the authors have reported for the first time coordinated oscillation of membrane potential in E. coli biofilms that may have a functional role in photoprotection.

(2) Strengths of the manuscript:

- The authors report original data.

- For the first time, they showed that coordinated oscillations in membrane potential occur in E. coli biofilms.

- The authors revealed a complex two-phase dynamic involving distinct molecular response mechanisms.

- The authors developed two rigorous models inspired by (1) Hodgkin-Huxley model for the temporal dynamics of membrane potential and (2) Fire-Diffuse-Fire model for the propagation of the electric signal.

- Since its discovery by comparative genomics, the Kch ion channel has not been associated with any specific phenotype in E. coli. Here, the authors proposed a functional role for the putative gated-voltage-gated K+ ion channel (Kch channel) : enhancing survival under photo-toxic conditions.

(3) Weakness:

- Contrarily to what is stated in the abstract, the group of B. Maier has already reported collective electrical oscillations in the Gram-negative bacterium Neisseria gonorrhoeae (Hennes et al., PLoS Biol, 2023).

- The data presented in the manuscript are not sufficient to conclude on the photo-protective role of the Kch channel. The authors should perform the appropriate control experiments related to Fig4D,E, i.e. reproduce these experiments without ThT to rule out possible photo-conversion effects on ThT that would modify its toxicity. In addition, it looks like the data reported on Fig 4E are extracted from Fig 4D. If this is indeed the case, it would be more conclusive to report the percentage of PI-positive cells in the population for each condition. This percentage should be calculated independently for each replicate. The authors should then report the average value and standard deviation of the percentage of dead cells for each condition.

- Although Fig 4A clearly shows that light stimulation has an influence on the dynamics of ThT signal in the biofilm, it is important to rule out possible contributions of other environmental variations that occur when the flow is stopped at the onset of light stimulation. I understand that for technical reasons, the flow of fresh medium must be stopped for the sake of imaging. Therefore, I suggest to perform control experiments consisting in stopping the flow at different time intervals before image acquisition (30min or 1h before). If there is no significant contribution from environmental variations due to medium perfusion arrest, the dynamics of ThT signal must be unchanged regardless of the delay between flow stop and the start of light stimulation.

- To precise the role of K+ in the habituation response, I suggest using the ionophore valinomycin at sub-inhibitory concentrations (5 or 10µM). It should abolish the habituation response. In addition, the Kch complementation experiment exhibits a sharp drop after the first peak but on a single point. It would be more convincing to increase the temporal resolution (1min->10s) to show that there are indeed a first and a second peak. Finally, the high concentration (100µM) of CCCP used in this study completely inhibits cell activity. Therefore, it is not surprising that no ThT dynamics was observed upon light stimulation at such concentration of CCCP.

- Since TMRM signal exhibits a linear increase after the first response peak (Supp Fig1D), I recommend to mitigate the statement at line 78.

- Electrical signal propagation is an important aspect of the manuscript. However, a detailed quantitative analysis of the spatial dynamics within the biofilm is lacking. At minima, I recommend to plot the spatio-temporal diagram of ThT intensity profile averaged along the azimuthal direction in the biofilm. In addition, it is unclear if the electrical signal propagates within the biofilm during the second peak regime, which is mediated by the Kch channel: I have plotted the spatio-temporal diagram for Video S3 and no electrical propagation is evident at the second peak. In addition, the authors should provide technical details of how R^2(t) is measured in the first regime (Fig 7E).

- In the series of images presented in supplementary Figure 4A, no wavefront is apparent. Although the microscopy technics used in this figure differs from other images (like in Fig2), the wavefront should be still present. In addition, there is no second peak in confocal images as well (Supp Fig4B) .

- Many important technical details are missing (e.g. biofilm size, R^2, curvature and 445nm irradiance measurements). The description of how these quantitates are measured should be detailed in the Material & Methods section.

- Fig 5C: The curve in Fig 5D seems to correspond to the biofilm case. Since the model is made for single cells, the curve obtained by the model should be compared with the average curve presented in Fig 1B (i.e. single cell experiments).

- For clarity, I suggest to indicate on the panels if the experiments concern single cell or biofilm experiments. Finally, please provide bright-field images associated to ThT images to locate bacteria.

- In Fig 7B, the plateau is higher in the simulations than in the biofilm experiments. The authors should add a comment in the paper to explain this discrepancy.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.92525.3.sa2](https://doi.org/10.7554/eLife.92525.3.sa2)

The authors use ThT dye as a Nernstian potential dye in E. coli. Quantitative measurements of membrane potential using any cationic indicator dye are based on the equilibration of the dye across the membrane according to Boltzmann's law.

Ideally, the dye should have high membrane permeability to ensure rapid equilibration. Others have demonstrated that E. coli cells in the presence of ThT do not load unless there is blue light present, that the loading profile does not look like it is expected for a cationic Nernstian dye. They also show that the loading profile of the dye is different for E.coli cells deleted for the TolC pump. I, therefore, objected to interpreting the signal from the ThT as a Vm signal when used in E.coli. Nothing the authors have said has suggested that I should be changing this assessment.

Specifically, the authors responded to my concerns as follows:

(1) 'We are aware of this study, but believe it to be scientifically flawed. We do not cite the article because we do not think it is a particularly useful contribution to the literature.' This seems to go against ethical practices when it comes to scientific literature citations. If the authors identified work that handles the same topic they do, which they believe is scientifically flawed, the discussion to reflect that should be included.

(2)'The Pilizota group invokes some elaborate artefacts to explain the lack of agreement with a simple Nernstian battery model. The model is incorrect not the fluorophore.'

It seems the authors object to the basic principle behind the usage of Nernstian dyes. If the authors wish to use ThT according to some other model, and not as a Nernstian indicator, they need to explain and develop that model. Instead, they state 'ThT is a Nernstian voltage indicator' in their manuscript and expect the dye to behave like a passive voltage indicator throughout it.

(3)'We think the proton effect is a million times weaker than that due to potassium i.e. 0.2 M K+

versus 10-7 M H+. We can comfortably neglect the influx of H+ in our experiments.'

I agree with this statement by the authors. At near-neutral extracellular pH, E. coli keeps near-neutral intracellular pH, and the contribution from the chemical concentration gradient to the electrochemical potential of protons is negligible. The main contribution is from the membrane potential. However, this has nothing to do with the criticism to which this is the response of the authors. The criticism is that ThT has been observed not to permeate the cell without blue light. The blue light has been observed to influence the electrochemical potential of protons (and given that at near-neutral intracellular and extracellular pH this is mostly the membrane potential, as authors note themselves, we are talking about Vm effectively). Thus, two things are happening when one is loading the ThT, not just expected equilibration but also lowering of membrane potential. The electrochemical potential of protons is coupled via the membrane potential to all the other electrochemical potentials of ions, including the mentioned K+.

(4) 'The vast majority of cells continue to be viable. We do not think membrane damage is dominating.' In response to the question on how the authors demonstrated TMRM loading and in which conditions (and while reminding them that TMRM loading profile in E. coli has been demonstrated in Potassium Phosphate buffer). The request was to demonstrate TMRM loading profile in their condition as well as to show that it does not depend on light. Cells could still be viable, as membrane permeabilisation with light is gradual, but the loading of ThT dye is no longer based on simple electrochemical potential (of the dye) equilibration.

(5) On the comment on the action of CCCP with references included, authors include a comment that consists of phrases like 'our understanding of the literature' with no citations of such literature. Difficult to comment further without references.

(6) 'Shielding would provide the reverse effect, since hyperpolarization begins in the dense centres of the biofilms. For the initial 2 hours the cells receive negligible blue light. Neither of the referee's comments thus seem tenable.'

The authors have misunderstood my comment. I am not advocating shielding (I agree that this is not it) but stating that this is not the only other explanation for what they see (apart from electrical signaling). The other I proposed is that the membrane has changed in composition and/or the effective light power the cells can tolerate. The authors comment only on the light power (not convincingly though, giving the number for that power would be more appropriate), not on the possible changes in the membrane permeability.

(7) 'The work that TolC provides a possible passive pathway for ThT to leave cells seems slightly niche. It just demonstrates another mechanism for the cells to equilibrate the concentrations of ThT in a Nernstian manner i.e. driven by the membrane voltage.' I am not sure what the authors mean by another mechanism. The mechanism of action of a Nernstian dye is passive equilibration according to the electrochemical potential (i.e. until the electrochemical potential of the dye is 0).

(8) 'In the 70 years since Hodgkin and Huxley first presented their model, a huge number of similar models have been proposed to describe cellular electrophysiology. We are not being hyperbolic when we state that the HH models for excitable cells are like the Schrödinger

equation for molecules. We carefully adapted our HH model to reflect the currently understood electrophysiology of E. coli.'

I gave a very concrete comment on the fact that in the HH model conductivity and leakage are as they are because this was explicitly measured. The authors state that they have carefully adopted their model based on what is currently understood for E. coli electrophysiology. It is not clear how. HH uses gKn^4 based on Figure2 here https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1392413/pdf/jphysiol01442-0106.pdf, i.e. measured rise and fall of potassium conductance on msec time scales. I looked at the citation the authors have given and found a resistance of an entire biofilm of a given strain at 3 applied voltages. So why n^4 based on that? Why does unknown current have gqz^4 form? Sodium conductance in HH is described by m^3hgNa (again based on detailed conductance measurements), so why unknown current in E.coli by gQz^4? Why leakage is in the form that it is, based on what measurement?

Throughout their responses, the authors seem to think that collapsing the electrochemical gradient of protons is all about protons, and this is not the case. At near neutral inside and outside pH, the electrochemical potential of protons is simply membrane voltage. And membrane voltage acts on all ions in the cell.

Authors have started their response to concrete comments on the usage of ThT dye with comments on papers from my group that are not all directly relevant to this publication. I understand that their intention is to discredit a reviewer but given that my role here is to review this manuscript, I will only address their comments to the publications/part of publications that are relevant to this manuscript and mention what is not relevant.

Publications in the order these were commented on.

(1) In a comment on the paper that describes the usage of ThT dye as a Nernstian dye authors seem to talk about a model of an entire active cell.

'Huge oscillations occur in the membrane potentials of E. coli that cannot be described by the SNB model.' The two have nothing to do with each other. Nernstian dye equilibrates according to its electrochemical potential. Once that happens it can measure the potential (under the assumption that not too much dye has entered and thus lowered too much the membrane potential under measurement). The time scale of that is important, and the dye can only measure processes that are slower than that equilibration. If one wants to use a dye that acts under a different model, first that needs to be developed, and then coupled to any other active cell model.

(2) The part of this paper that is relevant is simply the usage of TMRM dye. It is used as Nernstian dye, so all the above said applies. The rest is a study of flagellar motor.

(3) The authors seem to not understand that the electrochemical potential of protons is coupled to the electrochemical potentials of all other ions, via the membrane potential. In the manuscript authors talk about, PMF~Vm, as DeltapH~0. Other than that this publication is not relevant to their current manuscript.

(4) The manuscript in fact states precisely that PMF cannot be generated by protons only and some other ions need to be moved out for the purpose. In near neutral environment it stated that these need to be cations (K+ e.g.). The model used in this manuscript is a pump-leak model. Neither is relevant for the usage of ThT dye.

Further comments include, along the lines of:

'The editors stress the main issue raised was a single referee questioning the use of ThT as an indicator of membrane potential. We are well aware of the articles by the Pilizota group and we believe them to be scientifically flawed. The authors assume there are no voltage-gated ion channels in E. coli and then attempt to explain motility data based on a simple Nernstian battery model (they assume E. coli are unexcitablematter). This in turn leads them to conclude the membrane dye ThT is faulty, when in fact it is a problem with their simple battery model.'

The only assumption made when using a cationic Nernstian dye is that it equilibrates passively across the membrane according to its electrochemical potential. As it does that, it does lower the membrane potential, which is why as little as possible is added so that this is negligible. The equilibration should be as fast as possible, but at the very least it should be known, as no change in membrane potential can be measured that is faster than that.

This behaviour should be orthogonal to what the cell is doing, it is a probe after all. If the cell is excitable, a Nernstian dye can be used, as long as it's still passively equilibrating and doing so faster than any changes in membrane potential due to excitations of the cells. There are absolutely no assumptions made on the active system that is about to be measured by this expected behaviour of a Nernstian dye. And there shouldn't be, it is a probe. If one wants to use a dye that is not purely Nernstian that behaviour needs to be described and a model proposed. As far as I can find, authors do no such thing.

There is a comment on the use of a flagellar motor as a readout of PMF, stating that the motor can be stopped by YcgR citing the work from 2023. Indeed, there is a range of references such as https://doi.org/10.1016/j.molcel.2010.03.001 that demonstrate this (from around 2000-2010 as far as I am aware). The timescale of such slowdown is hours (see here Figure 5 https://www.cell.com/cell/pdf/S0092-8674(10)00019-X.pdf). Needless to say, the flagellar motor when used as a probe, needs to stay that in the conditions used. Thus one should always be on the lookout at any other such proteins that could slow it down and we are not aware of yet or make the speed no longer proportional to the PMF. In the papers my group uses the motor the changes are fast, often reversible, and in the observation window of 30min. They are also the same with DeltaYcgR strain, which we have not included as it seemed given the time scales it's obvious, but certainly can in the future (as well as stay vigilant on any conditions that would render the motor a no longer suitable probe for PMF).


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.92525.3.sa3](https://doi.org/10.7554/eLife.92525.3.sa3)

This manuscript by Akabuogu et al. investigates membrane potential dynamics in E. coli. Membrane potential fluctuations have been observed in bacteria by several research groups in recent years, including in the context of bacterial biofilms where they have been proposed to play a role in cellular communication. Here, these authors investigate membrane potential in E. coli, in both single cells and biofilms. I have reviewed the revised manuscript provided by the authors, as well as their responses to the initial reviews; my opinion about the manuscript is largely unchanged. I have focused my public review on those issues that I believe to be most pressing, with additional comments included in the review to authors. Although these authors are working in an exciting research area, the evidence they provide for their claims is inadequate, and several key control experiments are still missing. In some cases, the authors allude to potentially relevant data in their responses to the initial reviews, but unfortunately these data are not shown. Furthermore, I cannot identify any traveling wavefronts in the data included in this manuscript. In addition to the challenges associated with the use of Thioflavin-T (ThT) raised by the second reviewer, these caveats make the work presented in this manuscript difficult to interpret.

First, some of the key experiments presented in the paper lack required controls:

(1) This paper asserts that the observed ThT fluorescence dynamics are induced by blue light. This is a fundamental claim in the paper, since the authors go on to argue that these dynamics are part of a blue light response. This claim must be supported by the appropriate negative control experiment measuring ThT fluorescence dynamics in the absence of blue light- if this idea is correct, these dynamics should not be observed in the absence of blue light exposure. If this experiment cannot be performed with ThT since blue light is used for its excitation, TMRM can be used instead.

In response to this, the authors wrote that ‘the fluorescent baseline is too weak to measure cleanly in this experiment.’ If they observe no ThT signal above noise in their time lapse data in the absence of blue light, this should be reported in the manuscript- this would be a satisfactory negative control. They then wrote that ‘It appears the collective response of all the bacteria hyperpolarization at the same time appears to dominate the signal.’ I am not sure what they mean by this- perhaps that ThT fluorescence changes strongly only in response to blue light? This is a fundamental control for this experiment that ought to be presented to the reader.

(2) The authors claim that a ∆kch mutant is more susceptible to blue light stress, as evidenced by PI staining. The premise that the cells are mounting a protective response to blue light via these channels rests on this claim. However, they do not perform the negative control experiment, conducting PI staining for WT the ∆kch mutant in the absence of blue light. In the absence of this control it is not possible to rule out effects of the ∆kch mutation on overall viability and/or PI uptake. The authors do include a growth curve for comparison, but planktonic growth is a very different context than surface-attached biofilm growth. Additionally, the ∆kch mutation may have impacts on PI permeability specifically that are not addressed by a growth curve. The negative control experiment is of key importance here.

Second, the ideas presented in this manuscript rely entirely on analysis of ThT fluorescence data, specifically a time course of cellular fluorescence following blue light treatment. However, alternate explanations for and potential confounders of the observed dynamics are not sufficiently addressed:

(1) Bacterial cells are autofluorescent, and this fluorescence can change significantly in response to stress (e.g. blue light exposure). To characterize and/or rule out autofluorescence contributions to the measurement, the authors should present time lapse fluorescence traces of unstained cells for comparison, acquired under the same imaging conditions in both wild type and ∆kch mutant cells. In their response to reviewers the authors suggested that they have conducted this experiment and found that the autofluorescence contribution is negligible, which is good, but these data should be included in the manuscript along with a description of how these controls were conducted.

(2) Similarly, in my initial review I raised a concern about the possible contributions of photobleaching to the observed fluorescence dynamics. This is particularly relevant for the interpretation of the experiment in which catalase appears to attenuate the decay of the ThT signal; this attenuation could alternatively be due to catalase decreasing ThT photobleaching. In their response, the authors indicated that photobleaching is negligible, which would be good, but they do not share any evidence to support this claim. Photobleaching can be assessed in this experiment by varying the light dosage (illumination power, frequency, and/or duration) and confirming that the observed fluorescence dynamics are unaffected.

Third, the paper claims in two instances that there are propagating waves of ThT fluorescence that move through biofilms, but I do not observe these waves in any case:

(1) The first wavefront claim relates to small cell clusters, in Fig. 2A and Video S2 and S3 (with Fig. 2A and Video S2 showing the same biofilm.) I simply do not see any evidence of propagation in either case- rather, all cells get brighter and dimmer in tandem. I downloaded and analyzed Video S3 in several ways (plotting intensity profiles for different regions at different distances from the cluster center, drawing a kymograph across the cluster, etc.) and in no case did I see any evidence of a propagating wavefront. (I attempted this same analysis on the biofilm shown in Fig. 2A and Video S2 with similar results, but the images shown in the figure panels and especially the video are still both so saturated that the quantification is difficult to interpret.) If there is evidence for wavefronts, it should be demonstrated explicitly by analysis of several clusters. For example, a figure of time-to-peak vs. position in the cluster demonstrating a propagating wave would satisfy this. Currently, I do not see any wavefronts in this data.

(2) The other wavefront claim relates to biofilms, and the relevant data is presented in Fig. S4 (and I believe also in what is now Video S8, but no supplemental video legends are provided, and this video is not cited in text.) As before, I cannot discern any wavefronts in the image and video provided; Reviewer 1 was also not able to detect wave propagation in this video by kymograph. Some mean squared displacements are shown in Fig. 7. As before, the methods for how these were obtained are not clearly documented either in this manuscript or in the BioRXiv preprint linked in the initial response to reviewers, and since wavefronts are not evident in the video it is hard to understand what is being measured here- radial distance from where? (The methods section mentions radial distance from the substrate, this should mean Z position above the imaging surface, and no wavefronts are evident in Z in the figure panels or movie.) Thus, clear demonstration of these wavefronts is still missing here as well.

Fourth, I have some specific questions about the study of blue light stress and the use of PI as a cell viability indicator:

(1) The logic of this paper includes the premise that blue light exposure is a stressor under the experimental conditions employed in the paper. Although it is of course generally true that blue light can be damaging to bacteria, this is dependent on light power and dosage. The control I recommended above, staining cells with PI in the presence and absence of blue light, will also allow the authors to confirm that this blue light treatment is indeed a stressor- the PI staining would be expected to increase in the presence of blue light if this is so.

(2) The presence of ThT may complicate the study of the blue light stress response, since ThT enhances the photodynamic effects of blue light in E. coli (Bondia et al. 2021 Chemical Communications). The authors could investigate ThT toxicity under these conditions by staining cells with PI after exposing them to blue light with or without ThT staining.

(3) In my initial review, I wrote the following: "In Figures 4D - E, the interpretation of this experiment can be confounded by the fact that PI uptake can sometimes be seen in bacterial cells with high membrane potential (Kirchhoff & Cypionka 2017 J Microbial Methods); the interpretation is that high membrane potential can lead to increased PI permeability. Because the membrane potential is largely higher throughout blue light treatment in the ∆kch mutant (Fig. 3[BC]), this complicates the interpretation of this experiment." In their response, the authors suggested that these results are not relevant in this case because "In our experiment methodology, cell death was not forced on the cells by introducing an extra burden or via anoxia." However, the logic of the paper is that the cells are in fact dying due to an imposed external stressor, which presumably also confers an increased burden as the cells try to deal with the stress. Instead, the authors should simply use a parallel method to confirm the results of PI staining. For example, the experiment could be repeated with other stains, or the viability of blue light-treated cells could be addressed more directly by outgrowth or colony-forming unit assays.

The CFU assay suggested above has the additional advantage that it can also be performed on planktonic cells in liquid culture that are exposed to blue light. If, as the paper suggests, a protective response to blue light is being coordinated at the biofilm level by these membrane potential fluctuations, the WT strain might be expected to lose its survival advantage vs. the ∆kch mutant in the absence of a biofilm.

Fifth, in several cases the data are presented in a way that are difficult to interpret, or the paper makes claims that are different to observe in the data:

(1) The authors suggest that the ThT and TMRM traces presented in Fig. S1D have similar shapes, but this is not obvious to me- the TMRM curve has very little decrease after the initial peak and only a modest, gradual rise thereafter. The authors suggest that this is due to increased TMRM photobleaching, but I would expect that photobleaching should exacerbate the signal decrease after the initial peak. Since this figure is used to support the use of ThT as a membrane potential indicator, and since this is the only alternative measurement of membrane potential presented in text, the authors should discuss this discrepancy in more detail.

(2) The comparison of single cells to microcolonies presented in figures 1B and D still needs revision:

First, both reviewer 1 and I commented in our initial reviews that the ThT traces, here and elsewhere, should not be normalized- this will help with the interpretation of some of the claims throughout the manuscript.

Second, the way these figures are shown with all traces overlaid at full opacity makes it very difficult to see what is being compared. Since the point of the comparison is the time to first peak (and the standard deviation thereof), histograms of the distributions of time to first peak in both cases should be plotted as a separate figure panel.

Third, statistical significance tests ought to be used to evaluate the statistical strength of the comparisons between these curves. The authors compare both means and standard deviations of the time to first peak, and there are appropriate statistical tests for both types of comparisons.

(3) The authors claim that the curve shown in Fig. S4B is similar to the simulation result shown in Fig. 7B. I remain unconvinced that this is so, particularly with respect to the kinetics of the second peak- at least it seems to me that the differences should be acknowledged and discussed. In any case, the best thing to do would be to move Fig. S4B to the main text alongside Fig. 7B so that the readers can make the comparison more easily.

(4) As I wrote in my first review, in the discussion of voltage-gated calcium channels, the authors refer to "spiking events", but these are not obvious in Figure S3E. Although the fluorescence intensity changes over time, these fluctuations cannot be distinguished from measurement noise. A no-light control could help clarify this.

(5) In the lower irradiance conditions in Fig. 4A, the ThT dynamics are slower overall, and it looks like the ThT intensity is beginning to rise at the end of the measurement. The authors write that no second peak is observed below an irradiance threshold of 15.99 µW/mm2. However, could a more prominent second peak be observed in these cases if the measurement time was extended? Additionally, the end of these curves looks similar to the curve in Fig. S4B, in which the authors write that the slow rise is evidence of the presence of a second peak, in contrast to their interpretation here.

Additional considerations:

(1) The analysis and interpretation of the first peak, and particularly of the time-to-fire data is challenging throughout the manuscript the time resolution of the data set is quite limited. It seems that a large proportion of cells have already fired after a single acquisition frame. It would be ideal to increase the time resolution on this measurement to improve precision. This could be done by imaging more quickly, but that would perhaps necessitate more blue light exposure; an alternative is to do this experiment under lower blue light irradiance where the first spike time is increased (Figure 4A).

(2) The authors suggest in the manuscript that "E. coli biofilms use electrical signalling to coordinate long-range responses to light stress." In addition to the technical caveats discussed above, I am missing a discussion about what these responses might be. What constitutes a long-range response to light stress, and are there known examples of such responses in bacteria?

(3) The presence of long-range blue light responses can also be interrogated experimentally, for example, by repeating the Live/Dead experiment in planktonic culture or the single-cell condition. If the protection from blue light specifically emerges due to coordinated activity of the biofilm, the ∆kch mutant would not be expected to show a change in Live/Dead staining in non-biofilm conditions. The CFU experiment I mentioned above could also implicate coordinated long-range responses specifically, if biofilms and liquid culture experiments can be compared (although I know that recovering cells from biofilms is challenging.)

4. At the end of the results section, the authors suggest a critical biofilm size of only 4 μm for wavefront propagation (not much larger than a single cell!) The authors show responses for various biofilm sizes in Fig. 2C, but these are all substantially larger (and this figure also does not contain wavefront information.) Are there data for cell clusters above and below this size that could support this claim more directly?

(5) In Fig. 4C, the overall trajectories of extracellular potassium are indeed similar, but the kinetics of the second peak of potassium are different than those observed by ThT (it rises minutes earlier)- is this consistent with the idea that Kch is responsible for that peak? Additionally, the potassium dynamics also include the first ThT peak- is this surprising given that the Kch channel has no effect on this peak according to the model?

Detailed comments:

Why are Fig. 2A and Video S2 called a microcluster, whereas Video S3, which is smaller, is called a biofilm?

"We observed a spontaneous rapid rise in spikes within cells in the center of the biofilm" (Line 140): What does "spontaneous" mean here?

"This demonstrates that the ion-channel mediated membrane potential dynamics is a light stress relief process.", "E. coli cells employ ion-channel mediated dynamics to manage ROS-induced stress linked to light irradiation." (Line 268 and the second sentence of the Fig. 4F legend): This claim is not well-supported. There are several possible interpretations of the catalase experiment (which should be discussed); this experiment perhaps suggests that ROS impacts membrane potential but does not indicate that these membrane potential fluctuations help the cells respond to blue light stress. The loss of viability in the ∆kch mutant might indicate a link between these membrane potential experiments and viability, but it is hard to interpret without the no light controls I mention above.

"The model also predicts... the external light stress" (Lines 338-341): Please clarify this section. Where does this prediction arise from in the modeling work? Second, I am not sure what is meant by "modulates the light stress" or "keeps the cell dynamics robust to the intensity of external light stress" (especially since the dynamics clearly vary with irradiance, as seen in Figure 4A).

"We hypothesized that E. coli not only modulates the light-induced stress but also handles the increase of the ROS by adjusting the profile of the membrane potential dynamics" (Line 347): I am not sure what "handles the ROS by adjusting the profile of the membrane potential dynamics" means. What is meant by "handling" ROS? Is the hypothesis that membrane potential dynamics themselves are protective against ROS, or that they induce a ROS-protective response downstream, or something else? Later the authors write that changes in the response to ROS in the model agree with the hypothesis, but just showing that ROS impacts the membrane potential does not seem to demonstrate that this has a protective effect against ROS.

"Mechanosensitive ion channels (MS) are vital for the first hyperpolarization event in E. coli." (Line 391): This is misleading- mechanosensitive ion channels totally ablate membrane potential dynamics, they don't have a specific effect on the first hyperpolarization event. The claim that mechanonsensitive ion channels are specifically involved in the first event also appears in the abstract.

Also, the apparent membrane potential is much lower even at the start of the experiment in these mutants (Fig. 6C-D)- is this expected? This seems to imply that these ion channels also have a blue light-independent effect.

Throughout the paper, there are claims that the initial ThT spike is involved in "registering the presence of the light stress" and similar. What is the evidence for this claim?

"We have presented much better quantitative agreement of our model with the propagating wavefronts in E. coli biofilms..." (Line 619): It is not evident to me that the agreement between model and prediction is "much better" in this work than in the cited work (reference 57, Hennes et al. 2023). The model in Figure 4 of ref. 57 seems to capture the key features of their data.

In methods, "Only cells that are hyperpolarized were counted in the experiment as live" (Line 745): what percentage of cells did not hyperpolarize in these experiments?

Some indication of standard deviation (error bars or shading) should be added to all figures where mean traces are plotted.

Video S8 is very confusing- why does the video play first forwards and then backwards? It is easy to misinterpret this as a rise in the intensity at the end of the experiment.
