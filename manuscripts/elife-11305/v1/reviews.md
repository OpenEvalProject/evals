# Peer review - Round 1

Editors:
- Michael J Frank, Brown University , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.11305.018](https://doi.org/10.7554/eLife.11305.018)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your work entitled "Compulsivity is a trans-diagnostic trait characterized by deficits in goal-directed control" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by Reviewing Editor Michael Frank and Timothy Behrens as the Senior Editor. One of the two reviewers has agreed to reveal his identity:

Klaas Stephan.

The reviewers have discussed the reviews with one another and the Reviewing editor has drafted this decision to help you prepare a revised submission

Summary:

The authors conduct a comprehensive analysis from a large sample of subjects using questionnaire-based measures of clinical variables and two independent experiments using a sophisticated reinforcement learning task that dissociates goal-directed behavior from habitual stimulus-response learning. They report consistent demographic and clinical factors that underlie reductions in goal-directed behavior during learning. Supervised and unsupervised analysis of the link from questionnaire data to task performance points to compulsivity (and its various manifestations) as one key clinical factor that is related to reduced goal-directed behaviors.

Essential revisions:

Overall, the reviewers were impressed with the sophistication of the analysis and agreed that this study represents an important step toward large scale quantitative assessment of relevant phenotypes informed by computational cognitive neuroscience – that is, one of the main goals of computational psychiatry. They also agreed that the approach is original, exploits a large online sample (with appropriate controls for data quality), and is based on a systematic body of work, conducted by the authors over several years. However, they all expressed concerns with respect to the main take-home message of the manuscript that compulsivity is a trans-diagnostic factor that relates to deficits in model-based learning. This was particularly concerning given that other demographic factors (e.g., age) had even greater impact on the same measure of model-basedness, limiting the conclusions (and application) that one could garner from using this theoretically grounded construct clinically. Nevertheless, we all agree that the analysis is itself useful and sophisticated and we would like to see a revised manuscript that substantially tones down the main claim in the thrust of the motivation (including the title). We would be happy to consider a more nuanced, balanced and thorough (perhaps longer) characterization of the phenotype that is not as centrally focused on compulsivity, but rather presents a large scale analysis of factors that relate to MB vs. MF performance (and indeed other task measures not obviously MB per se, like the transition effect), including age, gender, IQ but also other clinical factors (impulsivity vs. compulsivity), whether these are independent or interactive factors, with discussions on whether they are likely to have similar or different mechanisms, etc. While this may seem like a major undertaking, we think that ultimately this kind of description can be more useful for showcasing the strength of your combination of theory-driven and data-driven approaches. Should you wish to maintain the stronger claim and message and focus on compulsivity we would suggest submitting elsewhere. Below these points are elaborated by comments from the individual reviewers, compiled together.

1) I've spent a substantial amount of time mulling over this paper, which really does have many strengths and is exemplary in many ways: a well-motivated task; applied to a large population; combined with an interesting methodology that makes an important step forwards in terms of relating neurobiological/cognitive mechanisms to psychopathology. The results are initially very intriguing – particularly those from the elastic net where impairments in goal-directed control seem to pick out symptoms of compulsivity and intrusive thoughts. However, on reading it more closely there are some important drawbacks which I think require the conclusions to be very significantly toned down; or additional analyses to substantiate them. This, in turn, might make it, in my view, more appropriate for less general journal. My major concerns are:

Age has much more of an effect than compulsivity – but OCD prevalence does not increase with age (e.g. Kessler et al. 2005, Arch Gen Psych 62(6):593-602). How can this be if goal-directed impairments underlie compulsivity in such a specific manner? The answer presumably is that goal-directedness depends on multiple processes, and that those related to compulsivity and age might in some way be dissociable. But does that not then make compulsivity a less specific guide to the underlying neurobiology? Isn't this also suggested by the fact that the relationship is, overall, quite weak: in the elastic net, the cross-validated correlation is 0.11? The temporal evolution of OCD decreasing with age also jars with the influence of age.

OCD, addiction, etc. are characterised by the positive presence of certain behaviors that bear the hallmark of 'habits'. Why does this not show up in the task? The possibility that the task seems to be insensitive to habitual variation (it never seems to show up in correlations despite the model-free prediction error regressors showing the strongest correlations with BOLD, i.e. neurobiology) somewhat questions the strong conclusions about compulsivity being specifically due to an impairment in goal-directed control: subjects could also have an impairment (excess?) in habitual learning (as one might conclude from excessive habitual behavior in e.g. Gillan et al., 2015 AJP), but this doesn't show up in the task because it's not sensitive. This again makes the conclusions they are drawing from the results just too strong. They state that the literature shows that deficits in model-based but not model-free decision-making has been found and cite Voon et al., Mol. Psych. 2014, but that study used the same task, hence not really addressing this point.

They make statements about patient populations but include neither patients nor any other measure by which functional impairment could be judged, and refer to diagnostic categories ('OCD', 'Alcohol addiction') despite not performing any diagnostic tests. The results, figures and discussion needs to avoid reference to diagnostic categories, and I find the term 'trans-diagnostic' difficult in the absence of any diagnosis. At the core if this is that it is unclear whether the results are driven by what one might observe in a typical patient population. One way to address this is to recapitulate the results only amongst those subjects with scores above cutoffs in any one measure, and then talk about 'putative patients' or so. We also need to know whether those subjects excluded based on performance were typical in terms of self-report.

There is no information about the stability of the effects over time, and hence the term trait is confusing. In fact, the covariates are mostly measures of state, not trait.

2) On closer inspection, the elastic net analysis is far less convincing than on reading the results – the strongest loadings (I tried to sort them in descending order from Table 3A):

I feel that there are good and bad numbers;

Am preoccupied with the thought of having fat on my body;

I vomit after I have eaten;

I check things more often than necessary;

Am terrified about being overweight;

Like my stomach to be empty;

My heart beats faster than usual.

With overall only two items from the OCI-R (the measure of OCD used), and neither of these is being significantly loaded onto by the compulsivity factor. The fact that so many eating disorder items show up certainly deserves some comment beyond it being just another compulsive phenotype, but overall this just doesn't quite capture 'compulsivity'. Only one out of the top 8 items has anything obvious to do with compulsivity (other than referring to a disease which they labelled as compulsive).

3) I do wonder about how overall severity contributes. This is important because severity is strongly related to comorbidity (see e.g. Kessler et al., 2005, in the same volume as above), and hence important for any trans-diagnostic processes. Half the questionnaires are correlated (and picked up by the compulsivity factor). The most severely ill patients might thus be most likely to respond positively on many compulsivity items. Could it be that the most severely impaired patients simply look compulsive because they are more likely to have more comorbid disorders and hence show up in the compulsive category?

4) In the FA, the first component doesn't contain anxiety at all. Anxiety loads much more on the second factor, and does so possibly even more than compulsivity: there are around 9 or 10 items that clearly relate to anxiety loading onto it, but only 2 items relating to compulsive behaviours. A number of the AUDIT variables are hard to relate to compulsions: alcoholics start drinking early as they experience withdrawal symptoms after a night of sleep. If anything, this component is more related to obsessions, anxious worries and difficulties controlling thoughts – which is, in terms of constructs, much closer to goal-directed deficits, it seems to me.

5) The task itself isn't obviously specific as it is not clear what the model-free component quite captures. This makes it more of a shame they didn't test components we know impact on m-b choices, such as working memory or stress. Impairments in this are also 'trans-diagnostic', and it would have been nice to show that they don't have the specificity of g-d choices.

6) Both reviewers expressed concerns about the explanatory power (of excessive habit formation due to deficient model-based control) for understanding clinical aspects of compulsivity. As you outlined in the Introduction, a key motivation for studying the relation between model-based /goal-directed decision-making and compulsive symptoms is the notion that "a deficit in deliberative, goal-directed control may leave individuals vulnerable to rely excessively on forming more rigid habits". I understand why this is a straightforward and attractive perspective to explain certain aspects of compulsivity. However, I think it would also be appropriate to mention challenges and potential limitations of this perspective in the Discussion – particularly because the dimensional approach chosen here suggests applicability of the proposed mechanism to clinical phenomena. For example, how exactly would a putative deficit in model-based control lead to prominent symptoms in OCD, such as excessive checking, fear of germs, or desire for order? The nomenclature and with it the framing need quite some work, e.g. categorical/dimensional measures, in terms of state/trait distinction, and distinctions between compulsions and obsessions.

7) The paper is very well written and of beautiful simplicity – a pleasure to read. However, sometimes a few more technical details or conceptual distinctions may have to be included in the main text to avoid confusion. First, the Introduction repeatedly refers to unspecified "OCD symptoms" which I found confusing, given that the paper is about the general population and that numerous symptoms of OCD exist. I would recommend avoiding the clinical label OCD and referring to compulsivity instead, stating the specific questionnaire you used. Similarly, in the Results section (second paragraph), there is a tension between using trait labels (impulsivity, compulsivity) and diagnostic labels (eating disorders, alcohol addiction); the latter is confusing (and not quite appropriate), given that your study examines the general population. You could eliminate this tension and, at the same time, increase clarity by always referring to the scores of the respective questionnaires. Second, the Results section should define the measure of model-based learning used (first paragraph). Until I went through the Methods section, I was not sure how exactly model-based learning was operationalised, and whether you were referring to a behavioural readout or to the parameter estimates of a computational model.

8) You report analyses based on behavioural readouts (trial-by-trial stay/switch behaviour), not model parameter estimates, because the qualitative conclusions drawn from both types of analyses seemed to be almost equivalent. Does this also hold with regard to how well questionnaire scores can be predicted, or does the computational model have a competitive advantage there? It would be instructive for the technically interested reader if you could include estimates of predictive accuracy for both approaches, perhaps in the supplementary material.

9) In the subsection “Quantifying Model-based Learning (Logistic Regression)”, second paragraph: The significant main effect of Transition is very interesting. Could you please state the direction of this effect and perhaps even offer a (speculative) interpretation? This is another place in which a more thorough analysis of the factors on both sides (task measures and demographic/clinical variables) can be useful.
