# Peer review - Round 1

Editors:
- Jacqueline Sztepanacz, https://ror.org/03dbr7087 University of Toronto Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.80993.sa0](https://doi.org/10.7554/eLife.80993.sa0)

This is an important paper that takes advantage of a comprehensive evolutionary genetic dataset to tease apart the relationship between genetic variation, selection, and phenotypic divergence over 50 generations. The evidence supporting the conclusions is robust and aligns with a growing body of work that shows patterns of variation can predict divergence over long periods of time and also that evolution does not always occur in the direction of selection, particularly when selection is acting on genetically correlated traits. The questions addressed in this study will particularly appeal to evolutionary biologists and quantitative geneticists.


---

# Peer review - Round 1

Editors:
- Jacqueline Sztepanacz, https://ror.org/03dbr7087 University of Toronto Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.80993.sa1](https://doi.org/10.7554/eLife.80993.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Selection and the direction of phenotypic evolution" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by Molly Przeworski as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Greg Walter (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1. Include body size as a trait in the analyses (these data seem to have already been collected, but not included).

2. Describe and justify what the movement traits represent biologically and why they would be adaptive in a high-salt environment.

3. Justify/explain why the movement traits can be considered independent traits and are not simply multiple measurements of the same phenotype.

4. Provide evidence that the fitness of these populations increased throughout this experiment.

5. Provide evidence and clarification of the method used to determine statistical support for genetic variance in G (showing that G has more than 1 significant genetic dimension would help provide support for #3).

6. Justify why heritability is an appropriate scale of measurement, rather than raw genetic variances or mean-scaled genetic variance.

7. Revise the introduction to provide targeted background on the key questions addressed.

8. Re-write the methods and results to improve clarity.

Reviewer #1 (Recommendations for the authors):

Line 63: I think you mean phenotypically correlated, not genetically correlated.

Line 68: the equation shown does not explicitly consider non-linear selection.

Line 90: under the infinitesimal model G is not predicted to change and the framework should generally work well across generations.

Line 141: the described methods do not match what is said in the rest of the paper. These methods say that the evolved populations were evolved in 8mM of salt for 35 generations and then kept at 305mM of salt for 15 generations. The rest of the paper implies that the concentration of salt gradually increases throughout the selection experiment. Which is it?

Line 160: line-mean fitness values are estimated with error. Are these errors incorporated into the models?

Line 235: how informative was the prior that was used, and how sensitive are the estimates to changing the prior? It seems that there are not enough genetic degrees of freedom to estimate all of the parameters in the model from the data.

Line 245: how did you estimate the null distributions? This is not explained.

Line 255: it's not obvious that the null expectation is 45. Could you show this empirically using bootstrapping to generate the null distribution.

Line 257: 1/6 of the total genetic variance is not the appropriate "null" distribution. Due to sampling error alone, the genetic variance will decline exponentially across the eigenvectors of G (see McGuigan and Blows 2015; Sztepanacz and Blows 2017).

Line 295: This does not seem like the correct comparison because of the potential for founder effects when establishing GA[1,2,4].

Tables and Figures: it looks like heritability and not genetic variances are reported. This is an important distinction

Reviewer #2 (Recommendations for the authors):

In addition to the previous comments of support for the overall question addressed, and the breadth of data available, but concerns over the evidence of adaptive evolution and multivariate nature of the traits, I had several further requests for clarification or comments about the interpretation of evolutionary genetic concepts.

Overall, I found the logical arguments presented in the introduction hard to follow, and what the study aimed to address was a surprise to me when I arrived at the end.

– Consider a general restructuring of the information to make it clearer from the start what the major focus of the study is.

– A lot of ground is covered very quickly, leaving the reader to fill in some big gaps from their own knowledge – consider whether all topics are sufficiently important to introduce up front, or if you can focus on the key ones to set the stage.

– Adding to the challenge of following the logic of the study motivation is that each individual sentence presents multiple, interconnected ideas. Some simple editorial changes that limited each sentence to one or two ideas I think would really help.

More specifically:

– Line 45: why does plasticity need to align with axes of genetic variance for adaptation to occur? The orientation of G and selection still matters – which you seem to also swing back to in the final sentence. It's not clear to me what this entire paragraph adds to the argument already made other than that phenotypic plasticity may alter the selection a population experiences when the environment changes.

– Line 53: I disagree that an adaptive argument is the most plausible or parsimonious here. The simpler explanation is that the G and environment are channeled through the same developmental pathways, and thus generate similar variation (i.e., Cheverud's argument for P=G due to alignment of G and E).

– Line 58: I don't understand how you arrive at the conclusion that when plasticity isn't adaptive it means we've misunderstood selection. Why is a presumption that plasticity must be adaptive warranted?

– Line 62: This is a misunderstanding of selection and evolution. Genetic correlations have no relevance for estimating selection, which acts solely on the phenotypic variation, irrespective of the causes of that variation. Genetic correlations will impact response to selection (i.e., evolution), but not selection itself.

– Why does it matter if evolution is due to selection acting directly on a trait or due to the genetic correlation of that trait to fitness (or another trait contributing to phenotypic differences in fitness)? How does whether the selection is direct or indirect have any bearing on whether plastic responses are adaptive? The genetic variance in plastic responses? Whether G is aligned with the direction of selection? How G evolves?

Some further requests for clarification of information:

– Equation 1 (and subsequent models): what is "CG"?

– Why are plasticity and divergence modeled for each trait individually? G is estimated from a multivariate model, so why are plasticity and divergence compiled as a vector of individual estimates?

– Equation 2 and 3: what is "Div".

– Equation 6: why is there a single intercept for the 6 traits? Why would traits not have their own individual intercept? Centering the data prior to analysis will not preclude traits differing in intercept when the fixed effects are taken into account.

– Line 243: why is e11 defined as the dimension with the most divergence?

– Line 248: "strictly" not "strickly".

– Line 251: Please explain what Gqw is – the 13 trait G?

– Equation 8: what is this "G" / where does it come from? How much of a bias is introduced here by taking the inverse of a G where many dimensions have very low variance (only positive due to imposed constraints)?

– Line 256: given the size of your experiment, what is the expected variation (error) around 45 degrees for two unrelated vectors?

– Second line after Equation 10 – add "genetic" for clarity: "…maximum amount of genetic variance …".

– Table 2 please also provide the error estimates.

– Figure 2: Could you please provide further information on the approach employed by the cited Morrissey and Bonnet 2019 for establishing null expectations? I might have missed this in the methods, but the evidence that you actually have genetic variance is key to all conclusions in the paper, so being very clear about this evidence is important.

– Bottom panel in B -I presume the vertical line indicates 0, but the use of red here and for high salt is confusing.

– Line 281: It's not clear what you mean by "modular" – the definition that I am familiar with relates to the strength of correlation among one set of traits relative to their correlation with other traits, but does not depend on a shared direction of correlation (i.e., a module contains both positively and negatively associated traits, so long as those correlations are relatively strong). The observation that one (maybe 2) axes capture all variation suggests a single module (i.e. a single behavioral syndrome has been measured).

– Line 284: what is "rounder" and how do you determine it's not "important"?

– Figure 3: Where does the null expectation come from? Please report the actual numbers for observed and null (including CI – in text or table) as it is not possible to see the overlap on this small plot on the plot. The conclusion that phenotypic plasticity is aligned with one G and not the other is very strong given that it does not seem that you can actually tell any difference between the two estimates (beyond sampling error alone).

– Tables 3 and 4. I have no idea what is being shown here – please provide sufficient information to relate this back to the Methods and the models that were fit, and what null hypothesis the reported Χ2 is associated with.

– Line 328: what's the logic for concluding that genetic variance in fitness indicates a stressful environment? Perhaps such conclusions are better placed in the Discussion where they might be justified via further information.

– Line 368: where does the information on gene expression come from? How is gene expression restricted to active/still? Do you mean that there is only divergence in expression between these states? How does this explain why leaving the stationary state has a different sign of divergence from entering the stationary state or changing direction? These observations seem consistent with my earlier interpretation that there is a single behavioral trait being assessed here, not six.

– Line 377: how statistically robust are the estimates of mutational variance? Where there is no variance, zero covariance will be implicated. The strength of this evidence also speaks to the question of whether there is a single "trait" being assessed here.

– Line 383: will only facilitate adaptation if they are aligned with future directions of selection.

– Line 450: why do you expect that changes in locomotor behavior will be under direct selection here? If the environment was heterogeneous for salinity (or food), then there may be fitness benefits, but how does moving any particular way allow the worms to increase their survival or fecundity in a high-salinity environment? Again, how do these results reflect a response to selection versus neutral evolution?

– Line 480: more details on where these data on size, and these estimates are coming from would be appreciated.

Reviewer #3 (Recommendations for the authors):

While I think these data are very valuable and their results are likely robust, I found that some parts of the manuscript were difficult to follow. In particular, it would help if the methods and results could be described a bit more clearly. In my major points below I highlight the areas I struggled to follow, and provide some suggestions for how to better focus the conceptual framework.

I think the authors need to better refine the conceptual framework and clarify the hypotheses in the final paragraph of the introduction. My confusion is because I'm not sure if they are focussing on adaptive phenotypic responses to the novel salt environment (i.e. plastic and evolved movement towards an optimum phenotype), or to predict the direction of phenotypic evolution. If the former, then I think testing whether plasticity in the novel environment is non-adaptive or adaptive is important, and testing whether phenotypic evolution has occurred in the direction of gmax or phenotypic selection (i.e. the phenotypic optimum) is also important. However the focus seems to be the latter, which means that there are currently no hypotheses justifying the test of the amount of genetic variance in the direction of plasticity, and furthermore, direct vs indirect selection is not explicitly compared. Below I provide some suggestions on how the conceptual framework could be clarified, I hope these comments help.

1) The framing in the introduction could be improved. In particular, the first paragraph jumps from selection on multiple traits to mutation-selection balance and alignment with the selection surface. I found some of the sentences quite long and it took several reads to understand their meaning. Furthermore, I found that plasticity is not well-grounded in the conceptual framework throughout the introduction and is not closely linked to the focus of the manuscript (predicting phenotypic evolution). L.46 assumes that plasticity is adaptive in a novel environment, which is often not the case. If the authors want to test the role of plastic responses in persisting and then adapting to the novel environment, I think they need some way of quantifying adaptive vs non-adaptive plasticity as well as testing whether adaptation occurs in the direction of plasticity (I found some information in supplementary material, but the link with the main idea of predicting phenotypic evolution is not clear). If it is possible to estimate a phenotypic selection gradient, they could test whether plasticity is adaptive by how well it aligns with phenotypic selection. However, this is a slightly different topic to predicting phenotypic evolution, which I think is the main focus of the manuscript. Furthermore, the second paragraph ends with 'indicating that selection is often misunderstood', which is a little vague and does not connect plasticity to phenotypic evolution.

2) Adaptation is important for this study, but evidence that the evolved populations adapted to the high salt environment is not presented. On lines 114 and 411 there is a reference to another study, but I think the manuscript would benefit from a more detailed explanation (or some discussion) about adaptation to the stressful environment, especially if the proxy for fitness (fertility) did not show evidence of adaptation (L.411).

3) There is missing information in the methods.

a. What are the traits (transition rates)? What do they represent and how are they important for the salt environment? There is some information L.180-193, but there is no biological explanation of what was measured or why these traits were chosen. It is also stated elsewhere that these traits are independent, could the authors please clarify how they are independent given they seem to use some of the same information in their calculation? I have trouble understanding how (for example) SF is different from FS in Figure 1.

b. Is the data collected from the same experiment that is a reciprocal transplant of all populations in all treatments? The section describing fitness (L.155) makes it sound like they were from different experiments. Furthermore, the use of BLUPs as estimates of fitness (from another experiment) is worrying, as explained by Hadfield et al. (2010; https://doi.org/10.1086/648604). If this is the case, it would be better to estimate the additive genetic covariance between traits and fitness (rather than the BLUPs). This is stated later in the manuscript, but I'm confused about where estimates of fitness came from and how they were used. I apologise if I've misunderstood the methods.

c. L.246 the authors describe a null distribution, but how was this constructed? Morrissey et al. (2019; https://doi.org/10.1111/evo.13842) made an important suggestion for more conservative estimates of null G (also described in Hangartner et al. 2020; https://doi.org/10.1111/evo.13891).

4) The description of the statistical analyses is sometimes difficult to follow. There are (by necessity) many parameters estimated and some more justification throughout the methods would help.

a. Some clarity would help in the description of equations 1-3 as it is difficult to understand what the motivation is for each equation, or what they represent. Also, equations 4-5 could be easier to understand by including (in text) the definition of a plasticity vector from Noble et al. (2019): δ X = Xnn – Xnov, where X is the mean of each trait in the nonnovel and novel environments.

b. L.257 and Equation10-12: I think equation 10 represents the amount of genetic variance in the direction of plasticity, but as a proportion of total plasticity (i.e. the length of the plasticity vector), is this correct? If so, please clarify in the text. A minor point on L. 257: this equation represents the amount of genetic variance in the direction of plasticity, which is different to genetic variance in plasticity. I am also confused by equations 10-11, why not just calculate the proportion of genetic variance in the direction of maximum evolvability (i.e. denominator in equation 10 is the 1st eigenvalue of G) – with plasticity vector normalised to unit length so that it represents the direction of plasticity. This removes the need for equation 11 and gives you the same information: the amount of genetics in the direction of plasticity as a proportion of the direction of maximum genetic variance. I apologise again if I've misunderstood, but I think a more detailed description and justification for equations 10-11 would help.

c. Equation 12: I don't think this is the correct null expectation. Why would we expect plasticity to be in the direction of 'average' genetic variance? I would think a better null would be random vectors (of unit length) projected through G so that you would test whether plasticity is in a direction that describes greater genetic variance than expected by random sampling.

d. Equation 5: Is this calculated for each of the derived populations? This is important for understanding the results in Figure 5. Because they are independent populations (with G also estimated separately), to me it would make more sense to do pairwise comparisons for each derived population with the ancestral (which could be summarised in Figure 5).

e. Figure 6 and 7 (+ their interpretation): To test how to predict phenotypic evolution, I think it would be better to directly compare the distribution of β and the selection differentials. By comparing them separately it is not clear what hypothesis is being tested and the argument is verbal rather than quantitative – see Hajduk et al. (2020; https://doi.org/10.1098/rstb.2019.0359) for a nice example.

5) In the discussion, I found it very interesting that the authors found body size to be both genetically correlated to the movement traits, and that selection was predicted accurately (both sg and β). I am curious as to why this trait wasn't included in the analyses because, as the authors highlight, it is probably the trait selection is operating on (or at least provides an estimate of performance as outlined by the traditional Lande and Arnold selection analyses). It made me wonder how body size changed across treatments and whether it evolved in the high salt treatment. I would think that it would be important to include body size in the analysis.

6) The discussion could be a bit more concise. I also think alternative explanations need to be discussed as I'm not sure I agree with the interpretation on L.425. It is more parsimonious (or at least a viable alternative) that during adaptation genetic variance has been depleted as would be expected if the selection is strong. Another alternative would be that selfing in a stressful environment has reduced the amount of genetic variance. I think it could be worth including these alternative explanations.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Selection and the direction of phenotypic evolution" for further consideration by eLife. Your revised article has been evaluated by Molly Przeworski (Senior Editor) and a Reviewing Editor.

Two reviewers and I have reviewed the substantial changes made to the manuscript since its previous submission. We are all in agreement that the current version adequately addressed previous concerns and is largely improved. However, the manuscript would benefit from some additional minor revisions in writing to help improve the clarity of this technically and biologically complex paper. I do not expect the changes should take the authors very long to complete.

There are several suggestions from the reviewers for ways to improve clarity. Addressing the premise of the study in a clearer and more biologically motivated way, and clarifying the methods and results for testing indirect versus direct selection are particularly important.

Reviewer #2 (Recommendations for the authors):

The responses from the Authors are comprehensive, and I believe have adequately addressed concerns about analyses and interpretation, as well as improving clarity and accessibility of the paper. In particular, the Authors have clarified the approach taken to defining a null distribution against which observed parameter estimates are compared. The shuffling of data and estimation of G from multiple shuffled samples characterized random associations in the data. The Authors have also included further empirical data that provides evidence that the three experimental populations had adapted to high salt.

Throughout the manuscript there is a clear commitment to transparency of data and analyses, with access to data and additional results to support the main results reported.

Reviewer #3 (Recommendations for the authors):

The authors present an interesting test of whether experimental evolution can be predicted from the patterns of genetic variation in the ancestral population. The authors have done an impressive job to address the comments raised in the previous review, which means that the paper is much stronger and focused on the questions addressed. I appreciated their detailed responses to the questions raised in the previous review and I found the new version greatly improved.

I only have one comment: The writing, while comprehensive, is quite dense and often abstract throughout the paper. This will make it difficult for a broader audience to follow. In addition, because of the (necessary) statistical rigor, it felt like the biology is missing, especially in the setup of the study and the results. For example, terms such as 'canonical traits' and references to alignments in the first paragraph make it difficult for a more broader audience to understand the background of the study, or the gap in knowledge that is being addressed.

I provide some specific examples below, but suggest that revising should focus on clarity throughout (and on the biological rather than statistical importance):

– L29-33 it seems early in the introduction to introduce G and Lande's equation, and it does so with little biological foundation.

– L.13 a better way of saying 'follow their selection gradient' would be 'whether phenotypic evolution occurs in the direction of selection'.

– L.14 'the canonical trait of the multivariate phenotype' this is not broadly accessible. Perhaps 'trait combinations with large amounts of genetic variation' (or something similar) would be more intuitive.

The premise of the study is much clearer but could be clarified further. The paragraph in the introduction L.115-116 needs to be simplified as it is difficult to follow and just lists the contrasts in a complicated way. Instead, it would be better to include the tests and hypotheses, rather than 'characterising' adaptation. The final two sentences are confusing (L.123-127), they should more clearly outline the focus of the study. In particular, I'm not sure what the final sentence is saying: are you testing whether genetic selection gradients in the ancestral population = phenotypic selection gradients after adaptation? I would have thought you would compare genetic selection gradients with phenotypic divergence between the ancestral and adapted populations.

I liked the addition of the explanation of the traits in the introduction, but is it possible to add some more biology? L.111-112 '… which ones [traits] are genetically or environmentally independent' is a bit vague. Do you instead have an idea of how the movement traits help them to navigate low vs high salt environments? Or some other more biological reasoning. It is suggested 'movement can increase during experimental evolution due to more foraging and dwelling' – but this is confusing, is it that there is selection for greater movement across generations? Or just that there is greater movement in a new environment? Foraging and dwelling seem like opposites unless dwelling is defined as a specific behaviour.

I found the major tests of indirect vs direct selection and also how phenotypic evolution is predicted very difficult to follow in the results. I think the analyses are correct, but the results need to be described more simply so that it is easier to understand. I'm not sure the section on direct selection is required, and if removed, could help simplify the study to focusing on predicting phenotypic evolution. Or there needs to be a better justification for including direct selection because the Stinchombe (2014) and Hajduk et al. (2020) framework does not seem to have been used (but I apologise if I've misinterpreted something). Specifically, is there a reference for equation 7? Why does this Β represent phenotypic selection when it seems to capture phenotypic divergence. I am also a little confused as to why selection differentials are not just compared to observed divergence. And if you want to include direct vs indirect, predicted evolutionary change with indirect selection could be calculated using δ Z = G*Β where Β is calculated as per equation 6 – this uses the Stinchcombe (2014) framework. Sorry again if I've misinterpreted something, but there seems to be a disconnect between the results as written, the figures and the interpretation seems contradictory in the abstract (L.15-16).

Overall I found the study very interesting, I hope my comments help.
