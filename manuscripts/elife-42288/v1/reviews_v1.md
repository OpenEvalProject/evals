# Peer review - Round 1

Editors:
- Patricia Bassereau, Institut Curie France

Reviewers:
- Jeff Urbach, Georgetown University United States
- Gaudenz Danuser, UT Southwestern Medical Center United States

## Review text

DOI: [10.7554/eLife.42288.020](https://doi.org/10.7554/eLife.42288.020)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

[Editors’ note: this article was originally rejected after discussions between the reviewers, but the authors were invited to resubmit after an appeal against the decision.]

Thank you for submitting your work entitled "KymoButler: A deep learning software for automated kymograph analysis" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Jeff Urbach (Reviewer #1) and Gaudenz Danuser (Reviewer #2).

This manuscript describes KymoButler, a machine-learning software that has been developed for the automated analysis of kymographs. There is a big need in this area since kymograph analysis (or related linear tracking) is notoriously difficult to perform and to automate. Although the reviewers consider that KymoButler could potentially provide an open solution to automated kymograph tracking to the community, they eventually agree after discussion that in its current state, KymoButler has not been tested on challenging enough problems and so far, does not represent a general and new solution to complicated tracking problems. In particular, the reviewers were concerned about the performance of KymoButler for tracking elements on much more diverse traces that those considered in the manuscript: for instance, in the general case of axonal mobility tracking where cargoes or components can move in a direction, change speed, immobilize, reverse direction, and do any of this several times in a single trace. We feel that in its current form, this tool does not outperform some other existing tracking methods. For these reasons, we think that your manuscript does not meet the criteria of innovation of eLife and cannot be accepted for publication in the journal.

Reviewer #1:

This manuscript describes a very valuable contribution to the field of quantitative biological imaging. It is well written and clearly motivated, and I have no substantial concerns. The results look solid, the approach is creative and appropriate, and it seems likely that the software will be widely utilized. As with all machine learning applications, it would be nice to have a deeper understanding of how the software is actually working, but that isn't a reason not to share the results in their current form.

Reviewer #2:

This manuscript describes the use of a convolutional neural net (CNN) for the analysis of kymographs. While kymography is still used by the live cell imaging community to measure subcellular dynamics, and thus some tools to automate and reduce bias would be helpful, this work does not advance the existing repertoire of image analysis for this purpose.

First, the proposed method is not a kymograph analyzer, as claimed, but it relies on a CNN to learn a streak filter (the authors should have visualized the initial layers the trained net, and this would have become abundantly clear, I assume). The output of the CNN here is not a set of trajectories in the kymograph representation – the entity that eventually can be used to quantify particle velocities and, perhaps, lifetimes – but it offers merely a pixel-by-pixel map of a score that defines how probable the pixel is to be located on a streak. To get from the 'streakness' score map to the individual trajectories, the authors have to threshold the map, and then apply a morphological operator to thin the high score mask to single-pixel chains. Anyone who has written a program for line or edge detection knows, these two steps are much harder and are the decisive ones for the final results. These are the steps where the algorithm needs to account for streak crossings, junctions, and gaps. The authors largely wipe this under the rug. The results in Figures 2 and 3 reveal numerous places where exactly these two steps went wrong. And the authors probably intentionally pick data examples with relatively low particle density and/or fairly uniform particle motion. As the particle density and motion heterogeneity between and within trajectories increases, these limitations become overwhelming.

Second, the applicability of kymographs is very limited at large. Again, the authors wipe under the table that the task of selecting profiles is left to the user. When I was accepting to review this manuscript, I was hoping to see a creative solution to this very problem. The described software is far from providing an automated solution. In general, kymographs only work in scenarios where particles repeatedly follow a stationary path. As soon as trajectories deviate from the path, e.g. because of cell movement of deformation, the trajectory lifetime is unreliable and the velocity measurement, relying on streak integration in space and time, can get unstable/impossible. And even if sufficiently stationary paths exist, e.g. because the particle motion is much faster than the confounding cell movement, the paths are in all generality curvilinear and very difficult to define. For these reasons there is a sizeable community of labs developing single particle tracking methods. I do give the authors credit, however, for picking two scenarios, where the kymograph works. Axonal particle transport is one, Paul Foscher's glued down Aplysia is another. In both cases it is straightforward to manually identify a general particle path, and the required time scale separation between particle dynamics and path deformation holds up. The authors should have discussed at least the rare conditions under which kymograph analysis is valid. And, in this context, it would have been advantageous to present one full example where kymograph analysis would offer a new biological insight (like most high-profile methods paper do).

Third, the authors benchmark the performance of their kymograph analysis against a particle tracker. As the senior author of the plusTipTracker paper (published 2011) used as the benchmark reference, I get the shivers when I read that 'plusTipTracker is the gold standard for microtubule tracking'. Many advances have been made by us and other labs over the past 8 years. But, this is not the issue. The objection I raise here is that a kymograph analysis is tested against a particle tracking approach (whether it is plusTipTracker or any other software) in the one scenario the kymograph approach really has advantages over particle tracking. To repeat the statement above, the kymograph works well when particles follow a stationary path. And especially with bidirectional particle motion along this path, a more generic particle tracker that does not have the prior of directional stationarity, has a higher chance for confusion. This argument is trivial. My lab, for example, has taken the kymograph approach – also in an automated fashion – when we worked on bidirectional, axonal transport (PMID: 22398725). And, in my view, one of the most impressive examples of how the particle tracking and kymograph frameworks can be algorithmically merged to increase tracking robustness in cases of path stationarity is the work by Sibarita more than a decade ago (PMID:17371444). Neither one of these papers is discussed. If the authors want to benchmark their Deep Learning streak detector, then they should use automatic kymograph analyses as a reference (there are such tools in ImageJ, etc.). And in the spirit of my first comment, they should also benchmark against approaches that use steerable line filters or curvelets to generate the same score map. I am pretty sure that the Deep Learner will be widely outperformed by a filter that is designed to detect streaks a priori.

Even if the authors were to address these points, the innovation of this manuscript does not meet the bar of what I would expect to see in a journal like eLife. This tool may give the authors some useful results in their own research, but I do not think this is worth more than a subsection in a Materials and methods section.

Reviewer #3:

In this manuscript, Jakobs et al. provide a machine-learning tool to analyze kymographs. This is a worthy addition to the state of the art, as kymograph analysis (or the related linear tracking) are notoriously difficult to perform and to automate. I think this tool could have a significant impact on a large community (researchers interested on quantifying subcellular mobility), if it can be made easily available, easy to use and broadly applicable. Related to this, I have a number of questions about the current manuscript I would like to discuss before its eventual publication in eLife.

The first point is about how this software is made available. Two authors of this manuscript (M. Jakobs and A. Dimitracopoulos) have launched a website/company, https://deepmirror.ai, for AI-based image processing, offering custom service and including the KymoButler software,. In addition, deepmirror.ai is providing the web-based KymoButler tool that is mentioned in the current manuscript (also, it looks like the web app now uses the deep network rather than the shallow one). This is a bit confusing, a clarification on what will be 1. open source 2. free to use (not necessarily open source) 3. commercial would be useful, as would be a more detailed "Competing Interests" section if needed.

The second point is the current limit to monodirectional tracking on kymographs. While this works for the few particular cases highlighted in the present manuscript (end-binding proteins on microtubules; actin speckles), this significantly limits the general usefulness of the tool. Kymograph analyses are generally done for bidirectional transport of cargoes (vesicles or organelles), usually along linear processes such as axons. Including in the present manuscript the extension of KymoButler to bidirectional tracking on kymographs (as is currently developed, as stated here: https://deepmirror.ai/2018/09/25/improvements-to-kymobutler/) and making it available in the open source/free tool would be a big leap in usefulness for the community. This would make a very strong case for publication in a high-profile, broad-readership journal such as eLife, and justify the general aspect of the current title "A deep learning software for automated kymograph anaysis".

The third point is about network robustness. AI in image analysis is very useful, but the limiting factor for its adoption by biologists is the proper validation of deep-learning tools for different images, different situations etc. Due to a lack of knowledge from potential users, an improper use of deep-learning algorithms outside of their validated range is a real concern. In the current manuscript, the authors show that their trained algorithm can ba applied to a variety of cases (EBs in different cells, actin speckles) by adjusting the prediction probability threshold p. Do the authors think that the current tool could be generally used without the need of re-training? What advice/metric would help the interested researcher to validate results on one's own data? Would it be difficult (for a non-specialist) to re-train the open-source version of KymoButler for a particular application? Is this option considered as realistic by the authors? In my experience, this is usually the bottleneck of AI approaches in image analysis, because tools can be simple to use but the training part is usually beyond the skills of a non-specialist.

[Editors’ note: what now follows is the decision letter after the authors submitted for further consideration.]

Thank you for submitting your article "KymoButler, a deep learning software for automated kymograph analysis" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Vivek Malhotra as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Jeff Urbach (Reviewer #1).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The manuscript by Jakobs et al. describes a fully automated approach to analyze kymographs based on deep learning. The software can run on both uni- and bidirectional kymographs. The code is freely available and the tool itself is also available via a web application. This is an important state of-the-art contribution as kymographs are notoriously difficult to obtain and to automate.

Essential revisions:

We are impressed with the substantial improvements to the analysis tool and the presentation in the revised manuscript. We all agree that KymoButler is a promising tool for the field. Nevertheless, some issues remain and should be addressed.

1) The authors have shown that the current version of the software can manage unidirectional and bidirectional movements. But, the capabilities of the software should be tested more thoroughly, both on synthetic and also on "real" data. For instance:

– Synthetic data: the limit of systems performances should be explored by varying density of tracings and signal/noise ratio. Moreover, the authors should also comment on the similarities and differences of synthetic data to real kymographs.

– Real data: the tool must be tested on several examples of different real situations presented (Rab11, mitochondria, microtubule plus-ends), distinct form the training data, and average performance should be quantified against manual expert tracing and best-performing available tool.

Since the authors already have a lot of manually annotated kymographs, they could remove some of them from the training set and get hard numbers on the performance of KymoButler on such data.

In addition, for both synthetic and real data, quantitative comparison should go as far as the end result that people seek to obtain from kymographs: average directionality,% of reversals, average speed, processivity, pause duration, etc. These quantitative parameters should be compared between Kymobutler, manual expert tracing and automatic alternatives in order to evaluate how the difference in tracing detection affects the final measurements.

2) The authors should state clearly in Introduction and Discussion what can and cannot be done with their software.

Considering that biological objects move in a stochastic 3D environment, the first paragraph of the Introduction should state explicitly which classes of motions are appropriate for kymographs and for KymoButler, respectively. It is not clearly described in the current version.

What a " stationary path" means should be explained.

In addition, it would be helpful to the user to know how KymoButler manages the stochastic versus directed motions as well as the constraints on the frequency of changes in direction. These points should be added in the Discussion.

3) It also appears that KymoButler's usability can be further improved and that some issues in the program should be fixed.

For instance, when an error occurs there is no possibility to try again, but instead one has to go back to previous screen, drag the input files over again, remember the old sensitivity threshold, submit again and hope for the best. Likewise, there is no possibility to simply change the sensitivity once you see the oversegmented results. One has to go back, drag all the data over, and repeat. Considering the allowed image size, simple thresholding should be fast enough to be interactive in the browser.

From a visual inspection, it is unclear how sensitivity parameter affects the outcome. It appears that the less sensitive setting (-1) does not pick some faint traces, and also breaks trajectories in pieces, resulting in a similar trace number as at the medium sensitivity setting.
