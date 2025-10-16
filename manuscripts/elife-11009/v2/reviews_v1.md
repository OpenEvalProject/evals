# Peer review - Round 1

Editors:
- Axel T Brunger, Stanford University , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.11009.026](https://doi.org/10.7554/eLife.11009.026)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

Thank you for submitting your work entitled "Distinct kinetic determinants of influenza hemagglutinin-mediated membrane fusion" for peer review at eLife. Your submission has been generally favorably evaluated by Michael Marletta (Senior editor), a Reviewing editor (Axel Brunger), and three reviewers, but they identified several areas that require some revision.

The reviewers have discussed the reviews with one another and the Reviewing editor has drafted this decision to help you prepare a revised submission.

Summary:

This manuscript presents a quantitative analysis of influenza single particle membrane fusion data that represents an important contribution to understanding this process at the molecular level. The authors have previously developed a simulation model for these single virion fusion studies and in this manuscript substantially extend this analysis to gain insight into the dependency of experimental observables (e.g. fusion delay times and fusion yield) as a function of non-active HA trimers, the number of HA trimers required for fusion and the number of antibody Fabs that inhibit fusion. The parameters that govern the overall process of fusion and its susceptibility to inhibition by Fabs suggest why some influenza strains may be more easily neutralized by antibody and how physical attributes of the individual HA trimers can influence both fusion and neutralization. The simulation model also makes specific predictions about individual HA trimer activation rates and contributions to the free energy requirements to drive membrane fusion that are likely to be testable in future experiments.

Essential revisions:

1) The current manuscript is quite dense and takes significant effort to work through many details of both the model and the simulation data presented. The authors are encouraged to simplify some of the figures and to divide some of these further (e.g. Figure 1) so that the main points can be more easily followed by a reader who is unfamiliar with the approach. Specific suggestions by one of the reviewers are provided below. Some of the detailed graphs could be provided as supplementary data figures.

2) The predicted N from the gamma model is dependent on the fraction of non-productive HA trimers (quite striking in Figure 2C). However, one would not expect the number of required active trimers to trigger fusion be dependent on the fraction of non-productive or antibody-inactivated HA trimers. Thus, the gamma distribution model is indeed questionable if there is a significant fraction of non-productive "molecules". Perhaps this limitation of the gamma function treatment should be made more explicit since it has rather general implications (as hinted in the manuscript).

3) Although the simulation model seems physically more reasonable than the gamma distribution model, the derived parameters (k, N, etc.) are not entirely unique as discussed in this work. Moreover, the simulation model itself may not be unique. Future experimental data may require further revision of the model or even perhaps a different model. Some discussion of this point might be appropriate.

4) Cooperativity of the action of fusion proteins in conjunction with the membrane has been inferred from the simulation model analysis of kinetic traces. However, is there direct evidence for the arrest to be in an extended conformation prior to HA fold-back?

5) Paragraph two, subheading “Simulations of molecular events at the virus-target membrane interface”: how do these increases in time to hemifusion compare to those from the Otterstrom data?

6) Paragraph three, subheading “Simulations of molecular events at the virus-target membrane interface” regarding lag time plateaus: is there an increase in bound virus that does not fuse when the hemifusion lag plateau is reached?

7) The fusion kinetics for X31 and Udorn are faster than the 10-minute incubation times shown in the immunoblots. It would be helpful to see time courses with time points better corresponding to fusion timescales.

8) The simulation model uses the parameter k, the rate of activation of independent HA. In the present manuscript, a somewhat different rate is used compared to the 2013 eLife work where k = 0.0025 /s for all simulations of X31 (H3N2) influenza. Here ksim was changed so that it matched experiments in Otterstrom 2014 (paragraph two, subheading “Fab inhibition of H3 HA” and paragraph two, subheading “Fab inhibition of H1 HA”). Question: is the resulting fit rather insensitive to changes of 5-10 in this rate? This point may need some discussion.

9) Abstract: comparing only 2 strains and one mutant might be too few to make a general statement about HA evolvability. Perhaps this statement should be softened.

Specific suggestions on the figures:

Figure 1 should be revised to represent each of the parameters of the modeling more clearly. A schematic of the model that explicitly shows how each of the main parameters (Nh, ksim, fnp, antibody Fab, and patch size) plays a role in the process of fusion is important. Figure 1 shows prefusion productive vs. non-productive HA refolding, but a more comprehensive schematic overview of all of the key steps that are being modeled would be useful in order to quickly grasp what is being simulated.

Leave out the HA structural details in an overall schematic of the modeling, although it is still useful for showing productive vs. non-productive HA.

Use a simple representation for active HA trimers, inactive HA trimers, or Fab-inhibited trimers.

Make the schematic multiple panels, displaying the HA molecules (active and inactive) at the interface of the viral and cellular membranes.

Within each panel one can highlight/define two model parameters – the fraction of non-participating trimers (fnp) and the patch size (PS).

Use multiple panels to show individual HA trimers being activated (to highlight/represent ksim) and also use the number of panels to indicate the number of activated HA trimers required for driving membrane fusion (e.g three activation panels for Nh of 3).

There could be an indicator for the overall fusion delay time above the panels that helps tie this observable to the discrete steps affected by ksim, fnp and Nh

Split Figure 1 into two figures. The first could show the hemifusion and hemifusion delay predictions and the second could show the Ngamma and kgamma. There may be other ways to divide these up (e.g. separated by patch size).

In Figure 5, consider putting the PS55 panels into supplementary information. The PS121 are really the most interesting with comparisons to the experimental data.

Figure 4 and Figure 6: Although the figure has boxes around the parameter sets of Nh and fnp that agree best with the Fab inhibition data, the main point is still mostly buried. The figures could be simplified somehow, by de-emphasizing the majority of the bars that are not relevant to the main point being made (e.g. using different colors or some other approach).

Figure 7: Same as Figure 5. Consider moving the left panels to supplementary figures and just show the predictions with the experimental data. The authors should discuss why they think the experimentally observed hemifusion delay could increase as a function of the bound Fabs in contrast to the model.

Figure 8: panel A could be removed if a comprehensive schematic is shown in Figure 1. In this current panel 8A the model parameters are insufficiently represented. fnp is shown as an arrow, similar to kfp (or ksim). The participating HA trimers go immediately to two postfusion trimers, indicating Nh. However, this is too similar to a standard representation of fusion that loses the key point that there are multiple independent HA activation events contributing to the accumulation of Nh trimers, which can then drive fusion. Panel 8B also could use some revision to make the H3N2 and H1N1 comparison more clearly. Question: what do the filled diamonds represent?
