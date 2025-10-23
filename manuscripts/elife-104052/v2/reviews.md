# Peer review - Round 1

Editors:
- Bruno Lemaitre, https://ror.org/02s376052 École Polytechnique Fédérale de Lausanne Switzerland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.104052.sa0](https://doi.org/10.7554/eLife.104052.sa0)

Duneau et al. provide an extensive effort to model parameters of infection, an important topic in disease management. The theoretical findings of this study are important and will be of interest to mathematical biologists to model infection. The empirical data support the arguments, but may be incomplete, and more could be done in experiment design to shore up the robustness of these findings. This study helps us to better understand the complex course of infection.


---

# Peer review - Round 1

Editors:
- Bruno Lemaitre, https://ror.org/02s376052 École Polytechnique Fédérale de Lausanne Switzerland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.104052.sa1](https://doi.org/10.7554/eLife.104052.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting the paper "A within-host infection model to explore tolerance and resistance" for consideration at eLife. As you can see from the three reviewers and despite their interest on the manuscript, there are substantial issues needed to improve the manuscript both at the theoretical and experimental level. Note that eLife is opened to the idea of a new submission if the authors can address the points raised by reviewers. The reviewers did share that this article may be more suitable in its current format for a more specialized journal;

Reviewer #1 (Recommendations for the authors):

The authors provide an impressive, detailed, and nuanced discussion of parameters contributing to outcome of infection. This statistical model considers a variety of theoretical contributors to pathogen growth, immune defense, and damage amelioration. The topic at hand is of general interest in modelling infectious disease processes, and to understand what parameters contribute most to readouts of disease progression. The framework the authors set out is logically consistent, and there is a clear effort to be thorough in constructing their statistical framework.

However I am unconvinced that the experimental data support the conclusions of the model (Figure 7-8). As the model is entirely theory, it is essential that the experimental design and data used to validate the model robustly support its predictions. The authors may be able to address these concerns in revisions, and increase confidence in their conclusions.

The authors use different experimental treatments (ex. wounding prior to infection) and three key experimental readouts to inform on the interactions of their model parameters (Survival, SPPL, PLUD). However I am unconvinced by the experimental data presented to validate their model. This unfortunately derails the paper right at the critical stage, and deflates confidence in the conclusions.

Lines 484-497 (Figure 7) – The key question is if mortality increase caused by wounding is loss of resistance or tolerance. The metric used to test this is PLUD. The authors do find a general higher PLUD in wounded flies, though only in 2/4 genotypes. I am concerned this result comes from survivor bias effects.

As SPPL is variable across individuals, any flies surviving the initial phase of infection will suppress pathogen growth to a transient SPPL. However flies dying rapidly from the infection have uninterrupted pathogen growth towards PLUD. As seen in Figure 7A, many No Wound flies survive this initial infection, but have a steady mild mortality rate at later time points. On the other hand, Wounded flies die almost 100%, and survival curves plateau.

Therefore Wounded flies mostly die from unchecked bacterial growth. However No Wound flies die from either pathogen growth (majority) or at later time points, despite having suppressed the initial infection (minority). I suspect this is caused by a factor the authors ignore: Zd of their model is not fixed. Damage from the initial infection and autotoxicity from the immune response may not kill hosts in the first 24h, but can ultimately be the cause of death (ex. organ failure). In beetles, it is known that autotoxic effects of the immune response reduce lifespan associated with malpighian tubule dysfunction (doi:10.1098/rspb.2017.0125). Even a fly that successfully suppresses pathogens can die from failing organ systems without needing recurrent pathogen growth, which may not even be possible when the blood is antimicrobial.

The significance of Figure 7B is driven almost entirely by low-PLUD outliers present mostly in No Wound flies. This suggests PLUD differences are driven by loss of tolerance in No Wound survivors, and not loss of resistance in dying Wounded flies. This is the exact opposite conclusion of the authors. If the authors have time of death associated with their data points, this could confirm or counter my concern regarding low-PLUD outliers.

Lines 498-520 (Figure 8) – The authors use Bom mutants as a control, saying they have little effect on gram-negative bacteria (Hanson et al). But checking Hanson et al., they do not infect Bom mutants with gram-negative bacteria. In fact, Duneau et al. (2017,BMC BIOL) reports that the Toll pathway mediates a sexual dimorphism in response to P. rettgeri infection. Duneau et al. (2017,eLife) also showed PLUD does not vary across Imd, Toll, Phagocytosis, or Melanization mutants? These studies from one of the authors are in direct contradiction to the logic of this experiment.

Also Bomanin function is not known, and there is no evidence they are directly antimicrobial based on existing studies. Instead, the authors cite Lin et al. in their discussion (Lines 653-657), which is a study implicating Bomanin effects on tolerance through Bombardier, including a mortality associated with immune activation by heat-killed bacteria. It is likely Bomanins affect tolerance, so use of Bom mutants as a baseline for comparison is wholly inappropriate. Why did the authors not use a wild type control here?

Additionally, A group died more than Bomanin, so their claim that Defensin does not affect survival seems untrue in their conditions. The difference in PLUD in A, B, and AB is less convincing. Defensin is also associated with clearance of aberrant cells (doi:10.7554/eLife.45061), so even assuming a mild difference is true, it can again be due to tolerance effects. Why did the authors not compare Diptericins specifically in their question, given previous studies on the Diptericin and P. rettgeri? This is not a strict request for additional experiments, but I would be more convinced by use of AMP genotypes that might have specific activity against P. rettgeri, and genotypes with related but less important activity. A wild type control is necessary.

– It is not clear why the authors do not modulate JAK-STAT stress responses as a test of resistance vs tolerance (Lines 149-155 are not convincing).

– What is the status of the Diptericin locus in RAL-818, RAL-630, etc… Given Unckless et al. (2016)?

– In the discussion the authors comment on SPPL nicely. I am curious if they have considered the scenario where bacteria in SPPL stage are in a hibernation state. This is common in uropathogenic E. coli, which reside in host epithelial cells and cause recurrent outbreaks. But those E. coli are not constantly causing damage while in hibernation. Does the model assume a constant rate of damage for bacteria in SPPL phase?

– The authors should include a README file explaining the columns in their supplemental data files

Reviewer #2 (Recommendations for the authors):

Lafont et al. developed a novel theoretical model that describes how host resistance and tolerance affect within-host pathogen dynamics. Their model focuses on recently documented with-host bacterial dynamics in Drosophila. Specifically, it was previously shown that in some cases the same inoculation dose can lead to two distinct outcomes: (1) the host successfully controls pathogen growth, which leads to an apparently stable set-point pathogen load (SPPL), and (2) the pathogen growth out of control reaching very high levels termed pathogen load upon death (PLUD), which causes rapid host death. The developed model can successfully reproduce this type of branching process. In addition to other existing models, the authors are able to reproduce the empirically observed pattern that the SPPL can increase with an increasing inoculum dose. Two findings of the model analysis are particularly relevant for empiricists studying resistance and tolerance. First, the results contradict the previous belief that only tolerance affects the PLUD. Instead, the authors now demonstrate that also resistance can affect the PLUD. Second, the authors raise considerable doubt on the validity of a commonly applied method for quantifying tolerance, which is based on measuring the reaction norm of host fitness in relation to pathogen load (measured either by the inoculum dose or by pathogen load at one point during the infection). Specifically, the authors show that this reaction norm can be more strongly influenced by resistance than by tolerance. To overcome these problems, the authors propose a novel method to infer variation in resistance and tolerance, which is based on integrating measures of the PLUD and host survival. Finally, the authors validated parts of their model with experimental infection studies on Drosophila melanogaster. These studies demonstrate the predicted effect that the PLUD increases and survival decrease due to wounding, and due to the knockout of important resistance genes. The agreement between the predicted and observed effects is interpreted by the authors as a confirmation of the general validity of their model and the proposed method.

Taken together, the authors present very interesting theoretical and empirical results with potentially far-reaching consequences for understanding and measuring how hosts respond to pathogen infections. Nevertheless, there are some limitations of this study, which I think were not sufficiently considered when interpreting the results.

1. The theoretical and empirical work is biased towards resistance. The pronounced differences in the way both host strategies were modelled and empirically investigated could strongly limit the validity and generality of the model and the proposed method. As the authors explain, due to the lack of known tolerance genes in Drosophila, they were not able to empirically test tolerance specific predictions of their model. The authors acknowledge this limitation, but do not see it as a major problem. However, it appears doubtful that the empirically measured resistance effects are sufficient for concluding that also the tolerance effects are correctly predicted by the model. In addition to these limitations on the empirical side, the theoretical side contains the limitation that tolerance was modelled in a much more simplistic way compared to resistance. In the model, host resistance is characterized by three major features: it depends on host condition (i.e. the level of damage), it is costly (because it generates damage), and it is modulated by pathogen load. In contrast, the implementation of tolerance lacks all of these features: it is cost-free, it is independent of host condition and it is independent of pathogen load or amount of damage. The authors acknowledge that tolerance mechanisms are known to be modulated during an infection, but because related details are still unknown they chose to model tolerance in a very simplistic way. This choice is certainly a reasonable first step. Nevertheless, it leaves the possibility that more complex tolerance effects could strongly affect the dynamics predicted by the model. Especially in combination with the lack of empirical data on tolerance, this makes it challenging to fully assess the validity and generality of the model and the proposed method.

2. Effects on reaction norms are not very well explored. The authors have shown that the relationships between inoculation dose and host survival contradicts assumptions made in empirical studies (Figure 5). However, the relationship between SPPL and host survival is not explicitly shown and it is, therefore, hard to assess whether the problem also applies to this relationship. A more detailed analysis would be particularly informative for empirical studies that measure pathogen load during the infection. Furthermore, conducting empirical tests of the predicted effects is an important task that remains to be done before concluding that the reaction norm approach is generally flawed.

3. Host background mortality is not considered. The authors developed a deterministic model in which host death can only occur due to an infection. Host background mortality due to other causes is not considered. This is not necessarily a problem for the theoretical analyses. However, to avoid biased results, empirical applications of the proposed method should control for potential variation in background mortality among different host lines.

4. Very wide and skewed empirical PLUD distributions. In some cases, the empirically measured PLUD distributions are very skewed and very wide with a difference of up to five orders of magnitude between the smallest and the largest values (Figure 7B). It is not clear how this enormous variation arose and whether this might indicate a mismatch to the dynamics predicted by the model.

5. Differences between observed and predicted branching dynamics. There seems to be a mismatch between the empirically observed temporal pattern of branching (Figure 1) and the corresponding model dynamics (Figure 3D). In the model, branching starts immediately after inoculation with a rather slow separation of both branches, whereas in the empirical data branching appears to occur much later with a quite sudden, strong separation of both branches. However, the example shown in Figure 3D might not be a general representation of branching dynamics occurring in the model. Furthermore, it is hard to assess whether a mismatch would necessarily indicate a problem that is relevant to the main findings of this study.

L117-119: It would be appropriate to acknowledge that Ellner et al. (2021) proposed an extension of their basic model that includes a protected state, which allows for higher SPPLs.

Figure 3: I was wondering whether the colours are suitable for colour-blind people.

L 247: It would be nice if there would be a corresponding illustration of this result.

L 348-349: At first glance, this reads as a generalization beyond the model, which would not be appropriate at this point. It might be useful to add some clarification, e.g. "In the model …"

L 605-612: All this makes sense if the model correctly captures the dynamics of the investigated host-pathogen system. However, whether this is indeed the case for other host-pathogen systems still needs to be demonstrated. It seems to me that at this point it would be appropriate to remind the reader of this limitation.

Reviewer #3 (Recommendations for the authors):

In this manuscript, the authors study a model of within-host dynamics of pathogens that aims to capture the fact that some hosts may survive infections while others die from them, even if these infections are identical. The model recovers previous experimental observations, and a prediction from it is tested through new experiments.

Specifically, the authors propose a deterministic model based on coupled partial differential equations, where various parameters describe host resistance (via immune response) and tolerance to the disease. The equations include a specific nonlinear immune regulation, written as the product of an activation of immune defense production by pathogen load, and of a negative feedback that depends both on immune defense level itself and on damage caused. The model can be bistable, allowing for different outcomes (death or survival) under the same parameters, with different initial conditions. A difference in the host initial state (preexisting damage level) suffices to cause a different outcome for the same infection.

The authors make a thorough analysis of the equilibrium states of the model, and of the impact of each parameter. They demonstrate that in this model, infections can evolve either to clearance, to death (once damage exceeds a certain threshold), or become chronic. The authors show that the latter case can in fact be transient, and that the set-point pathogen load, which depends on initial conditions, is then a predictor of life span. True chronicity is also possible. In deadly cases, the authors find that the pathogen load upon death is almost independent from inoculum size, and they demonstrate that the value of this load, together with a hazard ratio, could be employed to distinguish the effects of tolerance and resistance.

Finally, the authors report experiments where Drosophila melanogaster is infected by Providencia rettgeri. Their experimental study follows up on a previous one where some of the same authors observed that some hosts survived while others died, under the same infection conditions [Duneau, D. et al. (2017) eLife, 6, e28298] – an observation that is recovered by the present model. The new experiments demonstrate that wounding the hosts or suppressing some of their immune effectors both increase the pathogen load upon death. This provides a test of the model prediction that damage should increase the pathogen load upon death as it hinders defense production.

Strengths:

The manuscript provides a comprehensive analysis of the model proposed. An important strength of this work is that a prediction of the model is directly tested by a novel experiment. A Shiny App performing a numerical resolution of the model is provided and allows the reader to directly experiment with its outcomes.

Weaknesses:

The model builds on previous ones which are cited. Some of them already featured bistability [Pujol, J. M. et al. (2009) PLoS Computational Biology, 5 (6), e1000399; Souto-Maior, C. et al. (2018) PLoS Neglected Tropical Diseases, 12 (3), e0006339; Ellner, S. P. et al. (2021) Proceedings of the Royal Society B, 288 (1951), 20210786]. The main formal difference is the specific nonlinear immune regulation form that is chosen. The main consequence is that a rather high set-point pathogen load (SPPL) is possible, and that it can be transient (but note that Ellner et al. proposed another mechanism to obtain a high SPPL). However, no full theoretical insight is provided on the key feature that allows this behavior, as the nonlinear immune regulation chosen is quite complex and includes multiple parameters. The default parameter values are not explicitly related to realistic ones.

While this manuscript is very interesting, I have some concerns that prevent me from recommending publication at least in the present form.

1. The authors should highlight more clearly the impact of the differences between the model that is proposed and previous ones, especially those that already aimed to describe the results of [Duneau, D. et al. (2017) eLife, 6, e28298].

– Can a link be made to the model which was proposed in [Duneau, D. et al. (2017) eLife, 6, e28298], in particular to the tipping point which played an important role there?

– What novel insights does the present model bring compared to [Ellner, S. P. et al. (2021) Proceedings of the Royal Society B, 288 (1951), 20210786], which is directly motivated by [Duneau, D. et al. (2017) eLife, 6, e28298]? The authors mention that a difference is that a nonlethal infection gets almost cleared in that paper (no high SPPL), but this is only true of the "conceptual model" proposed there, and Ellner et al. then propose that some pathogens may be protected from the host immune response, which can result in a high SPPL. This point should be discussed.

2. The model that is chosen is quite complex, which raises several questions:

– The authors refer to the previous study [Mayer, H. et al. (1995) Chaos 5 (1), 155-161] to justify the specific nonlinear immune regulation form they chose, but in that paper, the functions F and G are added and not multiplied in the equation regarding the immune defense level. The authors should motivate their choice.

– Multiple parameters are introduced, and their default values are listed in Figure 2. It would be important how these values are chosen, and to assess how realistic these choices are, and how robust the conclusions are to parameter variations in the realistic range. For instance, is the transient SPPL expected to last for a duration substantially shorter than host lifetime or not?

– Is this the simplest model that allows to have a high SPPL in addition to the bistability already present in other models? What key ingredient allows this?

3. Experimentally, what is the impact of the wound alone (without infection)?

4. The manuscript is quite long and conciseness would make it better. I recommend focusing on the key new insights and minimizing repetitions between the text and the figure legends, as well as between the Results and the Discussion.

5. The use of inappropriate theoretical terms should be avoided.

– In the legend of Figure 3, please avoid the term "stochastic simulations" as the model is entirely deterministic. What is done here is varying the initial conditions used to numerically solve the deterministic equations.

– The model is called "Lotka-Volterra" in reference to the prey-predator model but the similarities are not very strong. For instance, there are no oscillations in the dynamics here, while they are a hallmark of the Lotka-Volterra prey-predator model. Thus, unless there is a specific reason for calling the model "Lotka-Volterra" I would recommend refraining from using this name.

Detailed points:

1. Providing a Shiny App is great as it allows the reader to try the model out, but I strongly recommend to also post the code on GitHub and archive it to Zenodo, as it is durable and identifiable by a DOI.

2. Line 143: "For the sake of simplicity, the first equation of system (1) is written dimensionless": in fact, all three equations are in dimensionless form.

3. Line 166: Is α assumed to be positive? If yes, it would be good to mention it here.

4. Some letters are quite small in figures. In Figure 3 it would be helpful to use different colors and to put explicit legends for each curve.

5. Legend of Figure 3: x_0 is set to 10^-6, not log(x_0). Is the initial level of damage increased by 3% of z_d (legend) or 0.3% (figure)? Please clarify.

6. Figure 4 A,D,E: Can a qualitative explanation be provided for the way the white region size varies between these cases?

7. Line 483: Please spell out GLMM and explain notations (df etc.).

8. In Eq. S1-1 I believe that eta/xi should be to the power l and not l+1.

9. Line 893: "A necessary condition for clearance to be stable is that dx/dt(0,yh,zh)<0": this is problematic because equilibrium implies that dx/dt(0,yh,zh)=0. Do the authors mean dx/dt(epsilon,yh,zh)<0? Please clarify this.

10. Line 912: I believe that the last > should actually read <.

11. Figure S2-2: I believe that this corresponds to a stable equilibrium. It would be good to specify it.

12. Figure S3-1: Please explain what the various curves and lines are.

13. Line 1062: f and g should read F and G.

14. Figure S4-1: I believe that blue and red indicate increasing and decreasing PLUD, not higher and lower.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "A within-host infection model to explore tolerance and resistance" for further consideration by eLife. Your revised article has been evaluated by Wendy Garrett (Senior Editor) and a Reviewing Editor.

The manuscript has been improved, but there are some remaining issues that need to be addressed, as outlined below:

Reviewer #1 (Recommendations for the authors):

1) Experimental data set

I fully disagree with response 3. My concerns of Bomanins affecting tolerance have now been validated by further studies since this manuscript was first submitted (Xu et al. 2023 EMBO Rep). This supports signals already seen in Lin et al. (the authors should review Lin et al. Fig5bbd-early vs late and Fig6). In the new experiments, the authors use of Drs is inappropriate. Drs is involved in hemocyte recruitment to cancerous tissue and Drs OE suppresses JNK activation (Krautz et al. 2020 eLife). Drs is further implicated in other anti-cancer or traumatic brain injury responses (papers by Inoue lab 2019 and multiple recently by Wassarman lab). Both Bom and Drs can reasonably affect tolerance, and any mutation might have unintended consequences. A wild-type control is essential, and there is no justifiable reason not to include one.

The RNAi experiments are appreciated, and useful. However they raise some concerns as somehow the PLUD of Cat-IR is 10^2 higher than of Dpt-IR. PLUD is not a metric that should be so sensitive to inter-experiment variation, so these data are difficult to reconcile, and their meaning is difficult to trust. Also, what is the control? No detail is given for "mock-RNAi", and in general RNAi is best used as supporting evidence due to the need to mix genetic backgrounds that could affect results in cryptic ways.

2) Regarding my previous point, apologies if this was not clear, but reflecting 2 years later perhaps I can frame this concern better: lower resistance increasing PLUD is misleading phrasing. The way Figure 5 is presented reflects theoretical space. But PLUD is something defined by a biological limit of the host carrying capacity with a physical volume restriction as a theoretical maximum. As shown previously by Duneau et al. 2017, max PLUD of Dmel individuals in Figure 2 of Duneau was log2(25) to log2(26) across all D. melanogaster studied. What is different across strains here (and in Duneau et al. 2017 to some extent) is variance of PLUD. Thus why it's odd to frame it as "PLUD increases by loss of resistance," because in fact the maximum PLUD in Fig7 is pretty consistent across all genotypes and treatments, and no increase is really possible (physical/biological limits). Instead, loss of resistance leads to more consistent microbial growth, faster, and reflected by more consistent mortality outcomes. Thus you get more consistent PLUDS near the maximum physical PLUD. In a wild-type host, resistance creates more complex dynamics, and opens the door for tolerance to impact the outcome and the PLUD. The response supplementary data support this concern exactly. Here, seemingly in 3of4 cases, the PLUD data have an intrinsic survivor bias: blue data points with bimodal survival outcomes have a right skew, while red data points lacking diverse survival outcomes skew to the left, and may even show less diverse ranges (certainly true of 630 and 559).

3) The theory of the model, to this reviewer, seems exceptionally detailed, consistent, and logical. This study has merits and contributes to a body of literature that is seeking to formalize host-pathogen interactions in a mathematical biology framework. I remain concerned with the application of this model to empirical data, which appears to be complex to interpret.

Reviewer #2 (Recommendations for the authors):

General appreciation: The authors put a lot of effort in responding to all the reviewer comments, which I think greatly improved the manuscript.

1) There is from my point of view only one issue remaining, which has not been sufficiently addressed. I apologize in case my previous comment on that matter was not clear enough. I had remarked that potential variation in host background mortality should be controlled for in empirical analyses. The authors addressed this issue in the context of their PLUD analyses by removing outliers. However, variation in host background mortality could also be a serious issue for the survival analyses. It seems that currently the implicit assumption in the conducted survival analyses is that there is no variation in background mortality among the compared strains or treatments. Thus, any inferred survival difference is attributed to different infection dynamics. If the possibility of different background mortalities is considered, then a correct interpretation of the survival analyses seems to require the analysis of appropriate non-infection controls. In the simplest case, it might be sufficient to show that there are no apparent survival differences among strains or treatments in non-infection controls. If there are any differences, they would need to be somehow controlled for in the survival analyses of the infected individuals. In case the authors disagree with my argumentation, it would be useful to provide a corresponding explanation in the manuscript why it is not necessary to include non-infection controls in the conducted survival analyses.

Reviewer #3 (Recommendations for the authors):

General appreciation: The authors have addressed my comments thoroughly, and I thank them for this. The manuscript is improved as a result. I still have two points about the model.

1) I still find the use of the term "stochastic simulations" misleading in the legend of Figure 3. I recommend that the authors explicitly specify "Dots corresponds to results of stochastic simulations where the initial pathogen load is randomly drawn (…) and then the deterministic equations of the model are solved numerically."

2) I got a bit worried by the authors' response regarding parameter values and robustness to varying them. Indeed they state: "As often with models, duration can be changed almost at will by adjusting parameters or initial conditions!" One would hope that if the parameters are varied in a physiological range, the conclusions do not vary "at will"… This said, I understand the difficulty of precisely determining each parameter.

Overall, I find that the theory-experiment comparison is an important strength of this manuscript.
