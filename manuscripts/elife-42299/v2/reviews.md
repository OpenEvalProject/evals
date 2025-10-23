# Peer review - Round 1

Editors:
- Serge Charpak, Institut National de la Santé et de la Recherche Médicale, Université Paris Descartes France

Reviewers:
- Serge Charpak, Institut National de la Santé et de la Recherche Médicale, Université Paris Descartes France
- Andreas Linninger, University of Illinois Chicago United States

## Review text

DOI: [10.7554/eLife.42299.034](https://doi.org/10.7554/eLife.42299.034)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

[Editors’ note: this article was originally rejected after discussions between the reviewers, but the authors were invited to resubmit after an appeal against the decision.]

Thank you for submitting your work entitled "Homogenization of capillary flow and oxygenation in deeper cortical layers correlates with increased oxygen extraction" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Serge Charpak as the guest Reviewing Editor and Reviewer #1, and the evaluation has been overseen by a Senior Editor. The following individual involved in review of your submission has also agreed to reveal his identity: Andreas Linninger (Reviewer #2).

The reviewers have discussed the reviews with one another. All appreciated the quality of the data, however several analysis, hypothesis and statistical problems were raised, casting doubts on the article conclusion. As the amount of work required to improve the manuscript in a 2-month time period seems too important, the Reviewing and Senior Editors have taken the decision to reject the manuscript.

Please find below the detailed reviewer comments:

Reviewer #1:

Li's paper reports 2PLM measurements of PO2 in cortical vessels distributed from layer I-5, in awake mice. Using the new 2P phosphorescence probe PtTAPIP, synthesized by the group of S. Vinogradov (one of the co-authors) and which has an excellent 2PA cross section, the authors succeed in detecting all capillary parameters: mean-PO2, RBC flux and velocity and also erythrocyte-associated transients i.e. RBC PO2, Inter RBC-PO2. These measurements are reported for each layer of the cortex.

The work is interesting but lacks novelty and the analysis is not rigorously done. The Introduction requires a paragraph describing previous theoretical and experimental demonstrations of EATs and the scientific reasons for which the authors could not detected EATs previously. The community of 2PLM users is now expanding and it is important to mention all the flaws the initial labs working with this approach have been through. The introduction should properly describe previous 2PLM works reporting PO2 in mouse cortical layers. Surprisingly, the statistical tests are not adapted to the data preventing the interpretation of most comparisons. To conclude, the new dye is certainly a technical improvement, but the present manuscript requires major rewriting, analysis and does not reach the standards of eLife.

Technical comments:

Subsection “Calculation of capillary RBC flux, speed, and hematocrit”: The authors estimate RBC velocity as "v = ø/Δt, where Δt is the time for the RBC to pass through the focal zone, and ø is RBC diameter, assumed to be 6 μm (Unekawa et al., 2010). RBC diameter cannot assume to be 6 µm: in capillaries, RBC orientation and thus "RBC size" varies with capillary diameter, RBC density and velocity. As the shadow size in time, Δt, depends on the "RBC size", and thus velocity, it cannot be used to calculate velocity. All velocity measurements should be removed from the paper.

This also raises a problem in the way EATs are defined, as v.Δt is used to determine the distance to the nearest RBC center. I suggest that the authors reanalyze their data considering time and not distance to extract EATs.

Subsection “Calculation of capillary RBC flux, speed, and hematocrit”: The authors make the same mistake as Parpaleix et al., (2013) and Lyons et al., (2016) in the way they estimate hematocrit, which is normally a measure of blood volume percentage: "Hematocrit was estimated as the ratio of the combined duration of all valleys associated with the RBC passages to the duration of the entire time course." Because RBC elongation varies with velocity (see first comment), the hematocrit calculated in the paper will depend on velocity. The authors should name differently what is actually measured.

It is difficult to understand how RBC PO2 was determined. Could the authors elaborate on their approach: did they consider the first bin ("micron") or an average several bins to determine RBC PO2? Additionally, the use of the criterion of "the central 40% of the peaks in the binary segmented time course" to extract InterRBC-PO2 could be prone to error. Given that the InterRBC-PO2 is defined at the lowest value of plasma PO2 reached between the passage of RBCs, when the RBC flux is low, the use of the central 40% criterion could yield an accurate value of the this parameter, but is likely to become less accurate with increasing RBC flux, as the period when the plasma PO2 is at its minimum will be shorter, and the inflection will be sharper. The use of this criterion should be validated, comparing the InterRBC-PO2 value it provides with those values that are extracted from more restricted windows at greater distance from the RBCs.

All statistics are based on Student's t-test whereas in almost all comparisons, ANOVA test with multiple comparison analysis should be used.

Subsection “Calculation of capillary PO2 gradients and EATs” and subsection “Accumulated oxygen extraction fraction increases in deeper cortical layers” The authors estimate layer-specific oxygen extraction fraction by comparing the PO2 in arterioles and venules at a given depth. This approach tacitly assumes that a layer-specific network of microvessels connects arterioles and venules in this layer, and that all RBCs which leave arterioles in the given FOV and layer flow into venules in that same field of view and layer. The authors should cite which theoretical and experimental papers support the hypothesis. In addition, as they have the tools to reconstruct easily the vascular angiograms, they should trace a series of pathways from the pre-capillary arteriole to the post-capillary venule in order to verify the hypothesis, which is key for the paper. They could potentially limit their investigation to layer I and IV pathways, which are likely to differ.

Is the mouse's head rotated around the rostro-caudal axis during the 2PLM sessions? If not (and unless the objective lens can be inclined, thought this doesn't appear to be the case in Supplementary Figure 1(b)), due to the inclination of the cortical surface at the coordinates of the barrel field it is probable that there is a discrepancy between the reported measurement depths and the true depth of measurement in the cortex. As illustration, the approximately 40-45 degree inclination of the cortex relative to the horizontal at the level of the S1 barrel field (as per Paxinos and Watson), would mean that the maximum reported imaging depth of 600 micros would infact correspond to a true cortical depth of approximately 460 microns. Thus, the assignation of the measurements to different layers will be compromised. Conversely, if the mouse head is rotated, could the authors note this and comment on the likely effect on the comfort and behavioural state of the mouse during the imaging sessions.

Biological:

3D projections of PO2 maps (Figure 1G) are made with acquisitions lasting only 0.6 seconds (2000 decays). This is really short as PO2 varies with time. It is clearly shown in Figure 5. PO2 may change by more than a factor 2 within 9 s. Therefore, PO2 maps using such brief acquisitions will change dramatically from one acquisition to the other. What is the scientific value of such 3D map? In addition, it artificially increases the number of vessels imaged.

If this approach was also used to build Figure 2, it strongly decreases its significance.

In the absence of proper statistics, Figure 3, Figure 4, Figure 5, Figure 6 and Figure 7 cannot be interpreted.

In their 2014 paper, the authors reported that PO2 decreases with the capillary order. Could the author verify if their findings hold true in the awake mouse? This would require a simple analysis regrouping A1, A2 and A3 capillaries.

Given the concerns raised above about the definition of RBC-PO2 in capillaries and the method for estimation of OEF by comparing arterioles and venules (and indeed A1-A3 and V1-V3 capillaires) in the same layer, it follows that the estimation of the relative contribution of different vascular compartments and the related conclusions (Subsection “Low oxygen extraction along the superficial capillary paths contributes to an increase in the mean venular SO2 towards cortical surface”) are questionable.

Reviewer #2:

The article presents novel data on hemodynamic states in the different layers of the whisker barrel cortex of awake mice. in vivo data are acquired using a novel oxygen probing technique with two-photon phosphorescence lifetime microscopy. Specifically, steady averaged oxygen pressures and red blood cell (RBC) flux counts were acquired. In addition, temporal variations within a 9s observation window were collected. A detailed statistical analysis of the layer dependence of oxygenation and RBC fluxes is presented. The main conclusions include the experimental observation of depth dependence of oxygen extraction, and a reduction in the RBC flux variability with increasing cortical depth. This study presents an invaluable experimental body of work that will help to elucidate oxygen extraction mechanisms in the mouse cortex and create in vivo data for mechanistic models to explain the physiochemical principles that drive and control cerebral blood flow and metabolism. This is a significant piece of work which I highly recommend for publication after modifications listed below:

Technical comments:

Introduction. The EAT is used to characterize the heterogeneity of the oxygen extraction within capillaries. What is the physical rationale for correlating oxygen point measurements to intracapillary resistance to oxygen delivery? Are these measurements for erythrocyte bound versus unbound oxygen in plasma? How is this EAT related to oxygen saturation?

It appears that measurements of RBC fluxes (RBC counts) assume that signals are generated from individual RBCs that are sharply separated. Figure 1C shows signals with different durations (and intensity). Is it possible that two aligned RBCs (two or more RBCs in file) may cause a longer signal that is indistinguishable from a single slow RBC? How would this affect the analysis of RBC fluxes?

In the Introduction, the authors cite the next generation of biophysical models, which with the exception of Gagnon's 2016 paper do not correspond to the anatomical detail presented in this study. Layer specific oxygen consumption has been predicted by recent biophysical models that match the detailed anatomical scope and three-dimensional resolution of the proposed experimental study. For example, three dimensional predictions of depth dependent oxygen gradients in mouse are given in Gould et al., 2017. Biophysical models to predict depth dependent oxygen gradients in humans are presented in Linninger et al., 2013 and Gould and Linninger, 2015. These studies have been successful in solving oxygen delivery to brain tissue coupled with biphasic blood flow in a realistic cortical microanatomy and are therefore perfectly aligned with the scope of the current study. These advancements should therefore be incorporated and discussed.

Subsection “Accumulated oxygen extraction fraction increases in deeper cortical layers”. The data in Figure 2 seem to refer to steady magnitudes or levels, the use of the word "amplitudes" seems ambiguous.

Subsection “Capillary RBC flux and oxygenation homogenize in deeper cortical layers”. The prediction that homogenization of RBC flow velocity enhances the oxygen extraction is made based on a single segment analysis in the cited biophysical model. Here, experiments are presented for a three-dimensional vascular network. I am uncertain whether the two scopes are really "in line" with each other as suggested in the current text.

Figure 5. The trend line in Figure 5 does not intersect at zero. What does the non-zero intercept of roughly 16-18mmHg pO2 mean? Should the trend have a zero intercept?

Subsection “Capillary RBC flux and oxygenation homogenize in deeper cortical layers”. The number of segments in layer IV and V have only half the segments than layer I-III. Could this affect the statistics? If not, this observation should be listed in the limitations.

The assignment of upstream capillaries A1-A3 and downstream capillaries V1-V3 was done manually. Is it hard to imagine that roughly hundred segments (=according to subsection “Low oxygen extraction along the superficial capillary paths contributes to an increase in the mean venular SO2 towards cortical surface”, the analysis included 97 segments for all mice specimen) were identified by hand without the aid of image filters (e.g. Blinder et al., 2013; Hsu et al., 2017) in combination with automatic segmentation.

In subsection “Low oxygen extraction along the superficial capillary paths contributes to an increase in the mean venular SO2 towards cortical surface” it is argued that the manual method provides statistical power. It is not clear what statistical power is referred to? I suspect that the results could come out quite differently, if labels were assigned differently. Is there any data on operator dependence of the labeling method? I recommend to consider writing the discussion section more cautiously to reflect that results are based on an operator dependent method with high uncertainty in segmentation, and that major results would not be affected by uncertainty associated with operator dependence in upstream and downstream labeling. This point is optional to the discretion of the authors.

Subsection “Low oxygen extraction along the superficial capillary paths contributes to an increase in the mean venular SO2 towards cortical surface”. The hematocrit changes were reported between upstream (A1-A3) and downstream capillaries (V1-V3). Why did the study not explore layer dependence or branch hierarchy dependence (Strahler order analysis) of hematocrit?

Discussion section. The RBC flux is equal to the product of bulk flow rate and hematocrit (volume fraction). How should we understand the variance reduction in RBC flux without any relation to variations in hematocrit, since the quantities are directly related?

Discussion section. The wide variability of hemodynamic states (high heterogeneity of capillary flow and oxygenation) was predicted previously in a biophysical model by Gould et al.,.2017. It would be helpful if the experimental results could be aligned with already completed theoretical work that aims at addressing the same points as those that are here so elegantly presented experimentally.

In the same vein, it is worth mentioning that a main finding of the reduced variance of RBC fluxes was just recently predicted covering the whisker barrel mouse cortex with extension to the entire MCA territory (Hartung et al., 2018). The experiments confirm several findings so that the predictive model results are highly relevant for this study and should be discussed.

Reviewer #3:

The work addresses highly relevant questions (depth-dependent difference, homogeneity/heterogeneity of microvascular flow and oxygenation). The amount of measurements performed is significant and the capabilities of the new oxygen probe PtTAPIP to measure a variety of blood flow characteristics in large cortical depths is nicely demonstrated. However, we have major concerns regarding some of the analysis performed and some of the conclusions drawn (listed below). Furthermore, there is a significant shortcoming in referencing earlier work. It remains unclear, where the current work goes beyond what was published before.

Essential revisions:

1) Calculation of capillary RBC flux, speed and hematocrit (subsection “Calculation of capillary RBC flux, speed, and hematocrit”):

As the authors are well aware, the methods presented to compute RBC flux, RBC speed and hematocrit are only valid in vessels where single file flow persists. The authors write that those measurements were performed in "capillaries". However, it remains unclear how capillaries were identified as capillaries. Were diameter measurements performed? As the RBC diameter of the mouse is 6 µm, single file flow can only be expected for vessel diameters < 6 µm. This aspect is key for the validity of the results. We propose that the authors come up with a table describing the measured vessels (type, depth, number) for clarity.

1a) Additional Concern regarding velocity calculations (subsection “Calculation of capillary RBC flux, speed, and hematocrit”):

Characteristics Mouse RBC: Diameter 6 µm, Volume: 45.5 µm3 (Windberger et al., 2013), Thickness: 1.6 µm.

Assuming that each RBC is 6 µm is not correct. Especially, in larger vessels the RBC orientation makes a significant difference in the proposed velocity calculation (by a factor of ~4).

For vessel diameters <5.5 µm the applied velocity calculation is more suitable, because here RBCs need to squeeze into the vessel. However, also here we need to account for changes in RBC length depending on the vessel diameter.

In summary, the presented approach gives at best a rough estimate of the RBC velocity and it remains unclear, why the authors have not chosen line scans that would be so much more appropriate.

1b) Additional Concern regarding hematocrit calculations (subsection “Calculation of capillary RBC flux, speed, and hematocrit”):

The hematocrit computation is based on the assumption that plasma and RBCs have the same velocity. However, RBCs travel on average faster than plasma (Fahraeus effect). This velocity difference can cause an underestimation of hematocrit. Even so this approach is used frequently this assumption should be described and the term "line-density" should be used instead of "hematocrit".

1c) Additional Concern regarding flux and velocity calculation (subsection “Calculation of capillary RBC flux, speed, and hematocrit”):

For the flux and velocity computation it is crucial that individual RBCs can be distinguished from another. Can this be guaranteed for all hematocrit levels? Some discussion/comments should be added.

1d) Selection of vessels for analysis (Subsection “Capillary RBC flux and oxygenation homogenize in deeper cortical layers”, subsection “Imaging of EATs and capillary RBC flow”):

The selection criterion for the vessels that have been chosen to analyse flow properties are not described. Moreover, it remains unclear why the number of vessels investigated per layer differs so significantly (400, 356, 118, 104).

2) Quantification of the temporal fluctuations of capillary Mean-PO2, RBC flux, speed and hematocrit (subsection “Quantification of the temporal fluctuations of capillary Mean-PO2, RBC flux, speed, and hematocrit”, Discussion section):

On the one hand, the chosen measurement time is rather short for a good averaging of the readouts. On the other hand, an averaging interval of 0.6 s is too large to resolve fluctuations in the capillary bed. An RBC with an average velocity of 1mm/s would travel 600 µm during that time. So, for the overall statistics, longer periods should be measured, but for describing the fluctuations over time, those segments should be split up into smaller than 0.6 s intervals, so that the fluctuations are dampened too much due to the averaging.

The arguments given in the discussion for the chosen interval seem to be motivated by dynamics on a larger scale but not by microvascular fluctuations. Why is the rate of oxygen consumption relevant for the capturing microvascular flow dynamics?

Alternatively, it has to be described more clearly that only fluctuations on the time scale of seconds are analysed and that faster fluctuations persist but are not of interest in the current study.

3) Analysis of EATs:

Intracapillary resistance of oxygen transport to tissue decreases in deeper cortical layers (subsection “Intracapillary resistance of oxygen transport to tissue decreases in deeper cortical layers”) and Low oxygen extraction along the superficial capillary paths contributes to an increase in the mean venular SO2 towards cortical surface (subsection “Low oxygen extraction along the superficial capillary paths contributes to an increase in the mean venular SO2 towards cortical surface”):

In order to understand the observed EAT trends, it is crucial to also analyse RBC-PO2 and interRBC-PO2. This aspect has been neglected for most EAT results. As such, possible reasons for the observed EAT drop in Figure 6C and the EAT increase in V1-V3 segments have not been analysed sufficiently (Based on Figure 3—figure supplement 1ARBC-PO2 does not drop? Thus interRBC-PO2 should rise for deeper layers to explain the EAT drop? How can a rise in RBC-PO2 and interRBC-PO2 for deeper cortical layers be explained? A higher interRBC-PO2 would however suggest a "higher intercapillary resistance to oxygen transport" instead of a lower one.)

Moreover, the EAT strongly depends on the distance of the capillary to the arteriole/venule (see Figure 7C). This impact should be discussed, e.g. how do you make sure that your depth-dependent EAT average is not affected by a larger number capillaries close to arterioles?

In an earlier work by the same authors, they did not observe EATs. The authors should discuss in detail where this discrepancy originates from.

4) Depth-dependent oxygen extraction (subsection “Accumulated oxygen extraction fraction increases in deeper cortical layers”, Discussion section):

We generally agree with the idea to use the difference in oxygen saturation as an indicator of oxygen extraction. However, as also shown in this work here, many factors have an impact on the oxygen saturation. Thus, saturation difference is not always equal to oxygen extraction. For example, higher blood flow in layer I leads to a higher oxygen availability in layer I and thus to higher SO2 values in the venules, even if the oxygen extraction is constant over depth.

"Benefitting from the improved sensitivity of the new oxygen probe, we were able to measure intracapillary longitudinal PO2 gradients in a larger number of capillaries…" why does the application of the improved probe help to increase the number of vessels measured?

[Editors’ note: what now follows is the decision letter after the authors submitted for further consideration.]

Thank you for submitting your article "More homogeneous capillary flow and oxygenation in deeper cortical layers correlate with increased oxygen extraction" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Serge Charpak as the guest Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Timothy Behrens as the Senior Editor. The following individual involved in review of your submission has also agreed to reveal his identity: Andreas Linninger (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing editor has drafted this decision to help you prepare a revised submission. All reviewers believe that the work is interesting. They however raised a number of questions that I ask you to address and which would clarify the manuscript. No new data is required. I have summarized the key questions:

1) The demonstration that RBC size can be estimated from the 2PLM measurements is still not convincing. The way you analyzed your new data is not informative: Comparing the mean RBC values from 58 capillaries measured with Line-Scan and Point-Scan (Author response image 2) does not solve the problem, in particular as the variability is large. Please show the plot in Author response image 2A, with lines joining each values, capillary per capillary. It is important as Author response image 2B and C already seem to demonstrate that RBC longitudinal size varies a lot. The 3 reviewers believe that if your new analysis reveals that RBC size cannot be accurately estimated, all RBC velocity data should be removed from the paper and the resulting uncertainty of RBC PO2 measurements be carefully addressed in the discussion.

2) Please address in the discussion the issue that a saturation difference may depend on several factors.

3) Add the plot for interRBC-PO2 over depth to the supplementary figures.

4) Add in the Impact Statement that the measurements are done at the steady state.

The reviewers have added some comments (see the full reviews attached below) to which you could briefly answer.

Reviewer #1:

The authors have made new experiments, new analysis and the text has improved. Previous works are now better described and discussed. The statistics are more appropriate.

The new experiments and analysis done in response to comments #2 and #3 are interesting but they do not fully address the issues raised. This concerns primarily RBC velocity measurements. The good news is that it could be easily done with simple analysis without any further experiment.

The authors initially used the assumption of an identical average size of RBCs to base other calculations, in particular RBC speed. They now show new experiments which results are summarized in several "R1" plots. The plots show that RBC longitudinal size is very variable, increasing very significantly with RBC speed and spreading from 3 to 14 µm (R1C1261 c plot (<30% RBC line-density)). This clearly indicates that RBC shadows measured during PO2 acquisitions cannot be used to estimate RBC speed. Note that the authors should give the "n" for each of the groups of capillaries in all the new "R1" plots.

This variability of RBC size is unfortunately masked in the R1C2-2 plot. This plot needs to show paired measurements in specific capillaries, the question being whether or not similar values of RBC velocity are recorded by the two methods when (presumably) similar real RBC velocities are measured. Showing population averages for the 58 capillaries assessed occludes the similarity/difference on a capillary by capillary basis. The important point here is that all the data are already acquired, for capillaries of known diameters. So the authors could now easily compare RBC values for paired measurements (with the 2 methods) in capillaries of different diameters. Please indicate the "n" for each of the groups of capillaries and plot, for each group, all RBC speed values measured with the 2 methods. I suspect that the authors will find differences with the two techniques. This would invalidate all RBC measurements obtained with point scan PO2 acquisitions.

It is important that the authors clarify the point as fluctuations of RBC shadows, whether measured in distance or time from the center of the shadow, will modify the RBC PO2 value. In fact, it will decrease RBC PO2 and thus the EAT amplitude. Could the authors measure the decays as a function of time, but after an alignment at the RBC border? This would solve the problem.

Reviewer #2:

The authors have addressed all previous concerns and submitted a more concise revised manuscript. Well done.

Reviewer #4:

To the editors:

Overall the authors improved their manuscript by clarifying various methodological issues and by providing a more detailed introduction and discussion. Nonetheless, some major issues remain. In my opinion the evidence for some of the major results is not strong enough or to put it differently the claims are currently too strong for the presented results. To be more precise: (1) I am still not convinced by the RBC speed calculation (comment #1a). (2) Oxygen extraction and saturation difference are not necessarily equivalent (comment #4). (3) The analysis of the depth dependent EATs should be more rigorous (comment #3). Nonetheless, I believe that this work is relevant and builds onto a large body of experimental work. It can be further improved by a more rigorous analysis of the available data and a more concise discussion of the uncertainties in the presented results. However, this may require that some of the conclusions of the manuscript are slightly weakened/adapted. More details on the major issues are provided in the detailed reply, which follows below.

I thank the authors for the additional explanations and the adjustments made. Below I list the comments where additional clarification is necessary in order to answer the initial question. Only the comments where further adjustments are necessary are listed. The ones where major issues remain are highlighted and positioned at the beginning.

I also read the comments of reviewers 1 and 2 as well as the subsequent changes to the manuscript. As some of the points raised by the other reviewers are very relevant, I added an additional comment for some of them.

The additional studies are an important step to judge the accuracy of the RBC velocity measurements.

However, the following major concerns remain:

- Author response image 2: a scatter plot that directly compares the RBC velocity from the line-scan and the point measurement would be more appropriate. Additionally, the average relative difference between the two measurements should be provided.

- Author response image 7: The results clearly show that there is significant variability in the longitudinal RBC size (CV = 0.4, longitudinal sizes ranging from 4-14 µm). Moreover, the RBC longitudinal RBC size is correlated with the RBC speed and the RBC Line-Density. It is impossible to estimate the impact of these dependencies on the presented RBC speed results.

I thank the authors for the additional explanations regarding IVR and I believe that the changes in the discussion are very valuable. However, some aspects of my initial comment have not been addressed.

The EAT is computed from the RBC-PO2 and the interRBC-PO2. As such I believe that EAT, RBC-PO2 and interRBC-PO2 should always be analysed and discussed hand in hand. Thus, it would be valuable for the manuscript to add the plot for the interRBC-PO2 over depth to the supplementary figures and to discuss RBC-PO2 and interRBC-PO2. Moreover, I suggest to add and discuss the EAT STD & CV plots over depth as it is done for all other quantities.

As stated in my original comment it is a surprising results that RBC-PO2 increases over depth and I don't know which mechanism could explain this increases (Figure 3—figure supplement 1). The same holds for interRBC-PO2 (which has to increase more than RBC PO2 in order to explain the EAT drop over depth). I do not ask for additional experiments, but I believe that is important to discuss these trends.

In my initial question I asked how the author's ensured that the depth-dependent differences are not affect by the position of the chosen capillaries along the capillary pathway or to put it differently how the capillaries were chosen over depth to guarantee an equal distribution of "upstream" and "downstream" capillaries. I kindly ask the author to describe if this has been considered in some way? If it has not been considered the possible impact on the depth dependent results should be discussed.

The EAT drop over depth is one of the major results of this manuscript and as the authors state in the discussion "EAT measurements are typically much noisier" (Discussion section). Consequently, I believe that the available data should be analysed as rigorously as possible.

I disagree with the given explanations why RBC flux in layer IV is supposed to be higher than in layer I. What matters here is not the average RBC flux and the higher capillary density per layer but the flux into the capillary bed per layer or to put it differently the flux out of the diving arterioles per layer.

The given arguments connecting average RBC flux and capillary density are not plausible. I try to explain this with a simplified example. Imaging two similar tissue volumes: One with a single vessel and flow rate q1 through that vessel. The second one also has an inflow rate of q1 but the vessel splits in two vessels. In both cases the inflow (and thus the oxygen availability) per tissue volume is the same. The vessel density is however higher in the second one. The authors now argue that the macroscopic flow rate would be larger in the second example, which is not true.

Of course, higher vessel density, i.e. more flow pathways, might have an effect on the overall flow rate. However, many open questions remain regarding these issues and simply relating RBC flux and capillary density to estimate the overall flow is not correct.

The referenced figures (Suppl. Figure 7b in Sakadazic et al., 2014 and Figure 2c in Gould et al., 2017) show the number of capillary segments, which is not the same as vessel density.

In the original work from Blinder et al., 2013 Figure 2c the capillary density increased from ~4% in layer I to ~5% in layer IV, which is an increase by ~20% but not by 50%.

Taken together, my initial question remains, i.e. the depth-dependent blood flow/oxygen availability has a strong impact on the actual oxygen extraction per layer. This should be discussed properly. Maybe it would good to change the variable name to depth-dependent saturation difference or comparable, because the term oxygen extraction seems to be misleading.

I believe the impact statement should be improved. "Homogenization", "Mechanism" and "adapts" suggest that the presented study looks at active mechanisms or dynamic changes. However, the work is a detailed description of the steady state flow and oxygen distribution.

[Editors’ note: further revisions were suggested before acceptance, as shown below.]

Thank you for resubmitting your work entitled "More homogeneous capillary flow and oxygenation in deeper cortical layers correlate with increased oxygen extraction" for further consideration at eLife. Your revised version has been discussed by the peer reviewers that raised some issues about your previous version and overseen by Serge Charpak as the guest Reviewing Editor and Timothy Behrens as the Senior Editor.

All acknowledged your efforts in responding to their comments. Most of your responses are satisfactory but some reviewers raised the concerns that your manuscript does not reflect at all the intense and fruitful discussion that occurred during the reviewing process. As the Reviewing Editor, I am pleased to inform you that your work is suitable for publication in eLife, providing that you include in the manuscript your responses to some of the questions/responses raised during the process of reviewing (see below). Note that most controversial points have been discarded. This will not take you more than a couple of hours and I will be pleased to address your revised version to the production department.

Please add in the manuscript:

Measurements of RBC velocity:

Several reviewers are still not fully convinced but accepted that the data are included in supplementary figures, providing that you add your work done to estimate the RBC size. The sole sentence line 145 (RBC speed calculation was model based …) and the discussion on RBC size are not fully satisfactory.

To end the controversy, I propose the following:

1) Subsection “Oxygen extraction fraction increases in the deeper cortical layers”: substitute the sentence by something like: "Note that as the instantaneous RBC shadow varies with both RBC speed, position and vessel size (see Figure 1—figure supplement 1), RBC speed calculation was model-based by assuming a constant RBC size (6µ)(Unekawaet al., 2010).

2) In Figure 1—figure supplement 1 (it will replace the current supplementary figure 1 which is not informative) please add the following plots which are interesting, justify the model based-choice and explain the problem of point measurements to estimate the RBC speed:

Add the plot from your summary comment (Title comparison between the RBC speed measurements by the line-scan and point-scan method.)

Add the new Author response image 7 plot (title Correlation between the line-scan and point-scan RBC-speed values in the capillaries having the diameter of 2-3 μm (left panel) and 3-5 μm (right panel)).

Add the plot Author response image 1 from your former response (Title a-c. RBC longitudinal size vs. capillary diameter, RBC speed, and line-density, respectively.)

3) Add the comments on these findings in the Discussion section.

Smaller EATs in layer IV:

Include in the discussion your detailed responses to the following points:

The increase in interRBC-PO2 and RBC-PO2 over depth, which is a very surprising result, as generally the most saturated RBCs enter the vasculature at the surface.

The impact of the sampling of "upstream" and "downstream" vessels and their distribution over depth.

Saturation difference/oxygen extraction:

As oxygen extraction, saturation difference and total blood flow are related quantities, it is important to add this information at two locations:

- where the depth-dependent oxygen extraction fraction is introduced (subsection “Oxygen extraction fraction increases in the deeper cortical layers”) and

- where the calculation of the depth-dependent OEF is described (subsection “Calculation of SO2 and depth-dependent OEF.”).
