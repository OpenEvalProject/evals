# Peer review - Round 1

Editors:
- Alex Mogilner, NYU United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.58165.sa1](https://doi.org/10.7554/eLife.58165.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

We were very impressed with the level of integration of experiment and theory in this study, and the clarity that the authors brought to the murky question of Rac/Rho-regulated cell polarity.

Decision letter after peer review:

Thank you for submitting your article "Periodic propagating waves coordinate RhoGTPase network dynamics at the leading and trailing edges during cell migration" for consideration by eLife. Your article has been reviewed by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Aleksandra Walczak as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Leah Edelstein-Keshet (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below only address clarity and presentation.

The reviewers are enthusiastic about your manuscript.

Essential revisions:

Please focus broadly on the following issues:

1) Please improve the presentation of the study in general, and of the model in particular.

2) Please spell out more clearly the novelty and significance of the findings – what exactly do you consider the new insight into the Rac/Rho signaling system, which comes out of your study.

Reviewer #1:

In this paper, the authors combine mathematical modeling and experiment to investigate how Rac-Rho system self-organizes to regulate migration behaviour of a polarized cell. After establishing that ROCK is more abundant at the cell rear and body, whereas DIA is more abundant at the leading edge, the authors suggest distinct circuitries of RhoA-Rac1 interactions and different RhoA and Rac1 kinetics along a cell. Specifically, oscillations of RhoA and Rac1 activities at the leading edge guide local protrusions and retractions, whereas high, stable RhoA activity and low Rac1-GTP at the rear are beneficial for steady retraction. The leading-edge oscillations are shown to create waves that periodically propagate from the front to the rear. The model makes two nontrivial predictions – about hysteresis of RhoA and Rac1 activities upon PAK inhibition and about formation of multiple lamellipodia in ROCK-inhibited cells – that are both observed.

The study is interesting and novel.

Here are some questions and suggestions:

1) How were the parameter values in Supplementary file 2 determined? I understand that the concentrations are from proteomics, but where are the rates from?

2) There has to be at least some explanation of the model in the main text.

3) The claim is that there are oscillations at the leading edge, but surely the oscillations only occur under pretty restrictive conditions in the parameter space? What are these conditions?

4) I am not quite sure how the reaction-diffusion model is set up. Are there some model parameters that are assumed to be varied along the cell length, like Dia and Rock distributions? What are these parameters?

5) In many places in the Results the authors over-interpret the data and basically mix actual results with speculations. For example, in a number of places in the Results, the statements about release of focal adhesions at the rear are made. But there is no data on the adhesions. So, please, move all speculations to the Discussion.

Reviewer #2:

This is a very interesting paper from the lab of Kolch and Kholodenko that is a significant advance beyond an earlier contribution of this group in (Byrne et al., 2016) on Rac-Rho dynamics.

In this paper, the authors combine careful experiments with advanced computational modeling to untangle a signaling network that consists of both positive and negative feedbacks between Rho and Rac via the effectors ROCK, Dia, and PAK. What is beautiful about this system is that it can explain the front-back polarity and Rac or Rho dominated cells, and many more dynamical regimes in cells such as waves that correspond to cycles of protrusion-retraction at the leading edge.

This research is significant not only for understanding the migration of normal motile cells, but also for addressing the pathology of metastatic cells. It is at the usual high level of sophistication of work that comes from this lab.

I think this paper has high priority for publication, and will interest a wide readership. It will definitely be interesting to members of my group, as a significant new way to understand how GTPase dynamics regulates cell motility, and to consider fully deforming cell domains with our computational methods, based on these results.

My only major suggestion is that the authors should mention the fact that waves of these regulators could interact with a deforming cell edge, result in behaviour that is not captured in the static cell shapes simulated here. (For example, we have found that some waves get damped out by the protrusion of a cell edge in simulations with a fully deforming 2D cell domain.)

Reviewer #3:

Before continuing, I'll note that I am not an experimentalist and as such will not comment on experimental methods.

In this article, the authors take a joint theoretical and experimental approach to study how the interactions of Rho GTPases and their effectors generate different phases of cell motion. The main takeaway is that RhoA and Rac1 activity in different parts of the cell is, at least partly, determined by the compartmentalized localization of ROCK and DIA. In short, DIA is enriched in the leading edge membrane and ROCK in the trailing edge membrane, and these localizations cause different functional GTPase dynamics in the front and rear (e.g. oscillatory front versus a steady state rear).

This is a solid article, though I do have a few broad concerns. First and foremost, I do not see what the substantial new understanding is here. My reading is that it is mainly adding to our understanding of the specific details of how GTPase + effector interactions influence cell dynamics. While this is a useful contribution, it is something I would expect to see in a disciplinary journal such as MBoC or Biophysical Journal. Is there something more that I'm missing here?

Another, albeit smaller concern, is the article is a difficult read. The writing itself is ok. It is the presentation that I'm having trouble with. There are a lot of model details here and I had trouble putting them in context of the main results of each section. In some cases, it wasn't completely clear what the main result of the section is other than illustrating agreement between a model prediction and experiments. It is also currently difficult to compare the model results with experimental results. In a number of places static model images are compared to experimental kymographs or experimental kymographs are compared to model videos. Is it possible to use a more common presentation formats to compare the model and experimental results? Or is it possible to synopsize some features that you are trying to compare in some measure that can be more easily compared.

Here are some other detailed comments:

1) What is actin doing during this process? You are discussing wave like behaviors here. A significant number of articles over the last 10-20 years have suggested that actin may play a role in the propagation of such waves. Any idea if actin has a role here? The possibility should at least be discussed.

2) What would lead to stable, spatial compartments with different levels of DIA and ROCK? That compartmentalization is absolutely critical to all of the results in this article, but I did not find any discussion of what might lead to that stable compartmentalization. This is important to discuss.

3) Figure 1: In regards to this figure, you state that DIA and ROCK activity are preferentially localized near the leading and trailing edges respectively. What do you make of the observation that both appear to be at high activity levels in the middle compartment? Some discussion of this middle would be helpful.

4) Subsection “Spatially variable topology of the RhoA-Rac1 interaction network”, last paragraph: Here you mention that RhoA abundance is higher than that of DIA and ROCK. Are the binding of ROCK and DIA to Rho 1:1 binding proportions. That is, can more than one ROCK (for example) bind to the same Rho?

5) Subsection “Spatiotemporal dynamics of the RhoA-Rac1 network reconciles the distinct temporal behaviors at the cell front and rear”, "… leading to re-arrangement of the cytoskeleton and dissociation of focal adhesions… leads to the rear retraction": This set of text is confusingly mixing model results with model interpretation. You are not modeling focal adhesions or retractions, but currently the text makes it sound as if you are. I suggest, in this area of the text, more clearly delineating what are i) model results, ii) interpretations, and iii) experimental results. At the moment they are a little muddled. I would suggest trying to clarifying this throughout as well.

6) Subsection “Hysteresis of Rac1 and RhoA activities and cell shape features”: I found this section difficult to follow and had a hard time figuring out the message. The text discussing what happens as the system transitions from I --> II --> III and back is difficult to parse.

7) Subsection “ROCK inhibition results in multiple competing lamellipodia and multi-polar cell shapes”, "… chaotic spontaneous activity bursts.…": Looking at Figure 5B, RhoA activity doesn't look either chaotic or bursty to me. Instead, it looks (to me), like there are a few regions of activity that are somewhat dynamic. Why do you describe it this way?

8) In Figure 5, it would be useful to have kymographs of RhoA activity in both the unperturbed and ROCK inhibited cases, with similar presentation for comparison.

9) I'm having difficulty comparing the kymograph results of Figure 5 with the model simulation video (Video 3, I believe). Is there a more quantitative way to compare these that would support the point you are trying to make? It is just difficult to see the correspondence between the results and your statements about them at the moment.

10) In the last section, you chose to perturb ROCK. Why only ROCK? Up to this point, the discussion had resolved around the importance of ROCK and DIA and their compartmentalization. Why not similarly perturb DIA? This does get mentioned in the Discussion, but why is it not more thoroughly discussed as its own Results section on par with the discussion of ROCK manipulation?

11) Discussion, seventh paragraph: It is worth mentioning (with appropriate references to for example, Orien Weiner, Steve Altschuler, and Adam Cohen) that cell tension is another commonly discussed mechanism coordinating front back signaling.

12) In this model, you include the inactive forms of RhoA and Rac1. However, you also note that complex activity is much more limited by DIA and ROCK amounts. Why include the inactive forms in the model? I guess what I'm really asking here is, does the GTPase conservation play any role here as has been suggested in other past studies? Or is it ROCK and DIA limitations driving everything?
