# Peer review - Round 1

Editors:
- Lars Timmermann, https://ror.org/032nzv584 University Hospital of Gießen and Marburg Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.72929.sa0](https://doi.org/10.7554/eLife.72929.sa0)

The authors present a software tool combining and correlating the documentation of intraoperative neurophysiological findings with atlas and imaging data. They also show an exemplary validation of their tool in a clinical series of 52 Parkinson's disease patients who underwent DBS surgery. This article will be of interest to clinicians and researchers who are involved in both the placement and controlling of the accuracy of the location of deep brain stimulation electrodes.


---

# Peer review - Round 1

Editors:
- Lars Timmermann, https://ror.org/032nzv584 University Hospital of Gießen and Marburg Germany

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.72929.sa1](https://doi.org/10.7554/eLife.72929.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Lead-OR: A Multimodal Platform for Deep Brain Stimulation Surgery" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor Lars Timmermann and Christian Büchel as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Ausaf Bari (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

This paper from Oxenford et al. describes a new open-source software tool LEAD-OR which allows a real-time visualization and merging of imaging and MER data during a DBS implantation procedure.

The guest editor and the reviewers were agreeing that this new technology is a major step in academic analysis of joint electrophysiological and imaging derived information for the analysis of target areas for deep brain stimulation. However, the reviewers also see some points that should be made a little more clear to envision the potential pitfalls and limitations of this program:

1. MER data has been highly selectively analyzed retrospectively. A number of patients were sorted out because of insufficient MER data. Could the authors please give an impression how the program gives feedback to investigators in a real-life OR situation about e.g. noisy MER recordings? Does the program give a sufficient feedback? How are processing times during the OR approach using rea-time MER?

2. How is the actual visualization while the program is running in the OR?

3. The authors mention the brain shift as the major source of discrepancy between imaging data and MER data. However, those are the patients who really need a good localization by MER and a "warning" to the OR team that imaging based on pre-OP MRI is not reflecting the actual situation anymore…. With other words: We would like to see from the authors how the program visualizes in the patients with a larger brain shift the critical discrepancies between MER localization and imaging.

4. In many ORs intraoperative imaging is used to verify the correct electrode position. In some this is done by the AERO-CT, in some ORs a fixed conventional stereotactic imaging set-up is used. How is this intra-operative imaging integrated into LEAD-OR?

5. It would be nice to see a number of single cases with unusual STN configurations. The value of this program will NOT be the correct classification and identification in the classical textbook cases but rather in the patients with unusual configurations of e.g. the STN.

6. We are not totally clear in understanding: What is really the GOLD-Standard in defining the target area in the visualization for the OR team? The MER? OR pre-OP imaging? Or intra-OP imaging?

Please also have a detailed look at the reviewers comments and revise carefully.

Reviewer #1 (Recommendations for the authors):

There are several issues which need to be addressed upon revision of the manuscript:

The statement in the abstract that one would use "commonly … up to five trajectories in parallel" is inconclusive as it stands. Better to say, "using a single trajectory or up to five trajectories in parallel".

Page 2, line 41. The frame itself does not include markers. Such markers are located in the fiducial plates which are mounted for imaging.

Page 2, line 55: Most "expert electrophysiologists" actually are "expert neurosurgeons or neurologists".

Page 3, line 100. Why should the use of Lead-OR be "strictly limited to Institutional Review Board (IRB) approved Research"? This does not really make sense since IRB approval would not address questions of liability associated with open-source software tools. The discussion with that regard is also misleading. "Study contexts" do not solve the inherent problems.

It is good to see that the tool can be applied when several microelectrode recording trajectories are used in parallel, but it would be better to discuss its feasibility first for a single trajectory and then for three or up to five.

Figure 1 is quite unclear. The red nucleus appears to be 10 times larger than the STN in this figure, also the colours appear to be wrongly applied. Please correct.

In general, I would recommend not to use too many abbreviations in figure legends. What does SDK mean?

Figure 6 is referred to prior referring to figures 4 and 5. Please correct.

It is a weakness of the patient series that some recordings were made under general anaesthesia. The problems with this should be outlined more clearly.

What type of "macroelectrodes" were used?

Reviewer #2 (Recommendations for the authors):

This is an exciting achievement by the authors. However, my main criticism is that it is a fairly descriptive paper without a central scientific premise. It would have been strengthened if for example the STN recordings and atlas overlays had been analyzed in more depth as that could have served as the scientific premise in this case. The data would also be further bolstered by including thalamic and GP cases.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Lead-OR: A Multimodal Platform for Deep Brain Stimulation Surgery" for further consideration by eLife. Your revised article has been evaluated by Christian Büchel (Senior Editor), a Reviewing Editor, and three reviewers.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

Reviewer #3 (Recommendations for the authors):

Summary:

Oxenford and colleagues present a novel framework for integrating data from multiple domains during surgery for Deep Brain Stimulation lead placement to enable informed decisions about the best target location in key regions associated with Parkinson's disease in the future. The innovative approach of the very diligent group from Berlin goes far beyond the common practice of implantation based on the assessment of imaging results and neurophysiological patterns encountered and the team's experience in parallel and towards an integrative and publicly available toolbox aimed at processing this information at once.

Review:

The approach from the group paves the way for the discussion of how to better objectify target selection away from the sole consideration of often imperfect imaging by extending it via intraoperative recordings – what some would consider the undisputed gold standard for DBS lead placement. It's a very well written and meticulously ornated manuscript with multitudes of details and visualisations. One of the intriguing and possibly most underestimated parts of this work is its open source character, which lends credence to the analyses but invites literate scientists to obtain deep insights into technical details; but at the same time also offers the possibility to include this toolbox easily into their routine. This open science approach is a lived practice for this group as an unparalleled service for the entire DBS community. In the referee's opinion, it links at the same time a potential drawback for other centres with less experience. Regardless of the multitude of potential extensions in principle (tractography, intraoperative imaging, etc.), it remains to be ascertained whether centres with less experience and technical know-how will be able to incorporate such a toolbox into their protocols. Nevertheless, an overly specialized solution with a high potential for expansions should not serve as excessive criticism of the authors' highly innovative concept and the well-balanced manuscript.

Recommendations for the authors:

From a personal point of view, the reviewer would preferably arrange Figure 5E the other way round, as this is more intuitive to understand. In any case, it should be briefly noted that according to RAS, with increasing values on the z-axis, the layers display more dorsal/superior slices. This figure is yet also quite interesting in terms of its content, as it implies that there is a great overlap between imaging and putative neurophysiologic epiphenomena of the STN in PD-patients but at the same time offers a somewhat puzzling result of a discrepancy towards (a) the location of the dorsolateral STN and (b) to what is generally believed to be the spot to aim for. The reviewer does believe Oxenfurt et al. have already done a marvellous job adding information and addressing points that have been arisen, nonetheless, inclusion of considerations into the discussion of where final electrodes were located, ergo where the best clinical outcomes were to be found and the proposed combined analyses seem interesting the least.

One of the aspects that needs further explanation is the number of artefacts or that of participants. On the one hand, it is undisputed that the exclusion of erroneous or low-quality data is a common practice. Nonetheless, 40% exclusions appear rather high, so this may need some further clarification, as possibly indicated by another reviewer. In addition, the number of 52 patients included does not seem very transparent. It would be helpful to explain where these people came from, i.e. whether they were consecutive patients within a period of time or specially selected people, etc.
