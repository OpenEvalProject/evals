# Peer review - Round 1

Editors:
- Yuuki Y Watanabe, https://ror.org/05k6m5t95 National Institute of Polar Research Japan

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.85703.sa0](https://doi.org/10.7554/eLife.85703.sa0)

This valuable study will be of interest to researchers in the fields of behavioural ecology, social ecology and evolution, and network science. The authors use simulations on empirically-recorded great tit social networks to examine how behavioural contagion might spread through social groups if individuals follow different social learning rules. The evidence supporting the conclusions is convincing, with careful modeling and parameterization for the chosen system.


---

# Peer review - Round 1

Editors:
- Yuuki Y Watanabe, https://ror.org/05k6m5t95 National Institute of Polar Research Japan

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.85703.sa1](https://doi.org/10.7554/eLife.85703.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting your article "Social learning mechanisms shape transmission pathways through replicate great tit social networks" for consideration by eLife.

Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The reviewers have opted to remain anonymous.

Comments to the Authors:

All three reviewers found the modeling approach and main results valuable. That said, they raised a number of major concerns, which can be summarized as follows (for many additional points, please see their original reports below):

(1) A more thorough description of the model should be provided. Ideally, all code should be made available so that readers can replicate the modeling.

(2) Parameter selection is weakly justified, and sensitivity analyses for the parameters are missing.

(3) It is unclear to what extent the results depend on the characteristics of great tit networks and how they are relevant to other species. Related to this point, the relevant literature needs to be covered better, including earlier work using empirically-recorded networks to simulate diffusion processes.

Reviewer #1 (Recommendations for the authors):

In this manuscript, the authors simulate learning processes using data collected from wild birds on their social networks. The results suggest that the nature of the learning process, as well as the size of the social network, determine which individuals will adopt a new behavior faster.

1. The main advance is simulating information spread over empirical networks rather than artificial networks. I doubt that this constitutes a major advance. Specifically, the authors mention in the discussion that the results are in agreement with previous results obtained from artificial networks. Therefore, while it is important and interesting to use empirical networks, their usage did not seem to provide additional insight.

2. The results depend on the characteristics of great tit networks. Although many different networks were used in the simulations, we can expect different results if networks of other species would be used. It would be helpful if the authors can provide some information about the structure of the empirical networks, and perhaps some predictions regarding their relevance to other species.

3. As far as I could tell, the specific code and data for running these simulations were not shared (not just the package). This makes it impossible to replicate the results and assess the data structure.

4. Learning rules in the wild were briefly mentioned in the introduction. Is there any evidence for the rules being used in wild animal populations, supporting the inclusion of these four rules?

5. Figure 2 and S2: I don't really understand why the order of acquisition is plotted as predicting the network traits (e.g., clustering coefficient). If there is any connection between the two it should be the other way around. To me it makes these figures confusing. Perhaps related, at least in the lower panels all individuals seem to have very similar trait values (e.g., weighted degree) -- how can this be explained?

6. L. 94-100: Earlier, the authors mention that individuals may tend to learn from specific individuals such as relatives or with a given trait value. To me that sounds like a very likely mechanism, such as "learn only from your mother, or from your strongest affiliation". I would be very interested to see versions of such rules tested here.

L. 90: Did you mean predator avoidance?

L. 152: The introduction mentioned weekly networks but here weekends are reported. How much time does each network include?

Figure 1: This figure is referenced only from the methods section. It raises a question: Why were the networks generated from only one location each time? I assume that two birds may have also interacted in adjacent locations. Perhaps some data on the overlap across adjacent locations can help.

L. 206-207: This statement does not seem to be supported by Figure 3, in which the correlation coefficients for weighted degree and weighted betweenness are actually lower in the simple learning rule.

L. 248…: I was surprised to see here, in the last part of the results, an explanation of the simulation procedure, which belongs either to the methods section, or to the beginning of the results.

L. 470: foal should be focal

Reviewer #2 (Recommendations for the authors):

Overall, I found the article interesting and feel that it provides an interesting examination of the consequences of how individuals learn on how behavioural contagions spread through animal societies. Previous studies have not applied these types of model to empirically-derived animal network data or studied as many forms of behavioural contagion simultaneously. Consequently, while (in the context of broader network science research) the individual results here are not new, it is valuable to see them presented together and in a way that is accessible to behavioural ecologists.

I felt the article was well-framed in the introduction, and the results were largely presented clearly and intuitively. In particular, I thought that Figures 2 and 5 were an excellent way to clearly show some of the main results of the study. However, there was insufficient information provided about the models or the experimental design of the modelling component prior to the results, which made interpretation of model results harder than it should be and at times made the results hard to follow when intertwined with methodological information.

I have some concerns about the modelling approach used, although perhaps some of them are related to the rather limited information provided on the simulation approach (I would really encourage the authors to provide clearer methods that incorporate functions for the learning rules and a step-by-step description of the simulation algorithm). It is not clear to me whether acquisition is deterministic based on likelihoods or probabilistic, and the step explaining how the likelihood of information being acquired socially or asocially is particularly unclear. This plays in to some concerns about the appropriateness of a strictly order-based algorithm -- it seems a rather artificial choice based on an existing statistical model rather than clearly biologically justified. Given the shape of the adoption curves for different contagions will differ, and that there is a probability of asocial component, avoiding a time-based approach seems like it could potentially have different consequences for different social learning rules. I can potentially see an argument that individuals would never truly acquire information at the "same" time, but this perhaps raises the question as to: (a) how meaningful changes in behaviour might or might not be to the subsequent individual to acquire the behaviour; and (b) how biologically meaningful differences in adoption time are (outside of very particular biological contexts such as during a predation event).

Another concern of the work presented here is that there are minimal checks of sensitivity to model parameterization (aside from changing the threshold number of connections in the threshold model). Parameter selection for the different forms of social learning is fairly weakly justified and not well explained so it is not clear what effect this might have on the generalizability of the results. For example, previous modeling work has suggested that the difference (in speed) in how simple contagions and contagions based on conformist learning spread through some types of networks depends on how easy the contagion can spread. This may not impact results related to the order of acquisition, but it is hard to tell if this is likely to be the case, especially given there is also an asocial learning component that has an impact on the adoption of behaviours.

I also found it interesting that the networks were weighted using simple ratio indices, and the reasoning for this wasn't clear. There are some important assumptions hidden in this choice that could potentially impact the results of the study related to what these indices relate to and how individuals learn. An (intentionally) naïve starting point (in my mind at least) would be that the likelihood of social learning depends on the number of times individuals associate at a food resource rather than a proportion of times that they occur together (e.g., individuals that occur together 4 out of 10 observations may well have more opportunities to learn than 1 out of 2 times). This is clearly a very direct interpretation of the simple ratio indices which ignores the potential for associations elsewhere and their "representative value". It is also based on the assumption that number of associations is the factor that drives social learning (as opposed to, e.g., associations, within a set amount of time, strength of social bond, etc.). However, it would be good to more clearly set out the reasoning for this choice and perhaps test or discuss the sensitivity to different assumptions here.

Away from the research itself, one frustration when reading this paper is that it does a fairly poor job of placing itself in the context of the wider literature. First, while it does a good job of citing the relevant studies that conduct similar modelling work in animal societies, there is relatively little effort to engage with the findings of these studies in the introduction or discussion of the paper. There is a real opportunity here to unpack the results of this study in relation to similar and contrasting findings from other papers that is missed here. Different papers have focused on different aspects of how social structure and connections influence contagions in animal societies and by linking better with some of these papers it could perhaps address how the findings of this study might generalize (e.g., to different social structures, considering different "transmissibilities" of contagions, etc.). Second, there is little effort made to acknowledge or consider the large number of modelling studies that address similar questions in the broader network science literature. While the network here is empirically derived, from that point on this study is purely computational and there are studies that have addressed very similar or overlapping questions elsewhere in this literature (e.g., how the number of connections influences speed of acquisition for different forms of contagion).

Related to this point, it would be nice to see a more nuanced discussion about the strengths and weaknesses of computational research that either applies simulation models to a single empirical case study vs. that the applies similar computational models to more generalized network structures. While there was a point when these types of model were applied to very generic network structures (random, small-world, etc.) and to an extent still are in network science (where the research aims are somewhat different), more frequently now studies that use simulated network structures do so with express biological questions in mind and design simulated networks accordingly. Taking this approach is a powerful way of tackling specific questions and/or generating a range of generalizable structures. Equally applying these types of models to particular empirical case studies is very valuable in its own right for different reasons. Related to the previous point, I think it would be great to make the most of their complementary strengths to better integrate the lessons learned from these different approaches.

This recently published paper is perhaps relevant/useful:

https://royalsocietypublishing.org/doi/full/10.1098/rspb.2022.1001

L20: Given the weak correlations illustrated in Figure 3, it feels slightly misleading to describe this as a "strong" relationship.

L22-23 (and elsewhere): Discussion of this idea throughout the paper doesn't acknowledge previous work showing this outside ecology. This review contains more links to studies in network science as a useful resource https://onlinelibrary.wiley.com/doi/full/10.1111/oik.07148?saml_referrer. For example, this paper https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0020207 tackles how conformist social learning leads to this pattern.

L48: "requiring exposure to multiple sources" isn't necessarily a difference between infection and behaviour spread in networks (e.g., see literature on dose-response curves).

L76-78: Evans et al. (2021) also consider a simple contagion and conformist learning and explore the potential implications of considering the simple contagion as being something other than the spread of infection in the discussion.

L83-85: While I think a really interesting aspect of this study is its exploration of the role of network size, I am not sure how well this criticism works (in its current form) given that even big networks can capture interaction patterns at small spatial scales, and that how network structure depends on the temporal scale will be highly study-system dependent.

L96-100: Given the methods come last, these rules need to be more accurately described here to help with the interpretation of the results. It would also be good to provide a more in-depth exploration of previous theory/discussion about these rules beyond ecology.

L112-113: Low clustering coefficient will not always indicate a less sociable individual, this will depend considerably on the broader structure of the network. It would seem to in this study, but some greater context would be helpful here. In the results it would be helpful to quickly describe the correlation between the centrality measures used in the studied networks.

Figure 1: Would be useful (and take up no extra space) to give the thresholds used here.

L151-154: It would be good to provide more clear information on networks per feeder site, network appearances per bird, etc., and an indication of what timespan were data included from. Also perhaps valuable to point out that the minimum of 10 (and rest of these descriptive stats) applies after some networks were excluded.

Figure 2: One thing I found particularly interesting in these results is that for simple, threshold and to some extent conformity there appears to be a stronger pattern of being the most peripheral is costly rather than being the most central is beneficial. Clearly, this may depend on what the information/behaviour that is spreading is related to, but it's a neat result and perhaps worthy of some discussion for what it means for social ecology/evolution in this system.

L210: Is this now meant to refer to Figure 3?

Figure 3/Figure 4: Even the correlations different from zero are (predominantly) small. Later in the paper it might be interesting to discuss how biologically meaningful they are in networks of different sizes in this system. One thing apparent in these results is that there is a lot of noise (presumably) related to the seeded individual. It may be worth using this to highlight that in small networks who you know is just as/more important than how many you know -- even if it is just as a suggestion for further research.

Figure 4: I found distinguishing between the two blues here pretty difficult. Another colour scheme may be clearer or a different way of presenting the data given how dense the point clouds are.

L219-231: It would be good to make this aspect of the experimental design clearer earlier. I also found these results were written less clearly than other parts -- some rewriting might be helpful.

L248-255: Some indication of how the model broadly works such as this should ideally come at the end of the methods to help with interpreting the results in this methods-last format.

L270-274: Would perhaps be helpful at the end of the introduction to set up the model or in the methods?

L362-364: Is there not a little more nuance here given that there won't necessarily be a single learning rule for each behaviour so it suggests perhaps that the importance of different learning rules varies as a behaviour spreads.

L378-380: Similarly to the previous point, an appropriately parameterized (dynamic) network for a large population can capture interactions at very fine spatial and temporal scale -- this doesn't seem so much a point directly related to network size. One aspect of network size that perhaps becomes interesting is that the importance of "who" you know versus how many you know changes in importance in different size networks.

L383: Is there a reason for using network "shape" here rather than more established terms like topology or structure?

L387-405: Good to see a sensible consideration of model limitations.

L449-453: Is there empirical data to support this for this study system given it has been the subject of previous experimental work? Justifying with previous empirical work would strengthen this point considerably.

L449-453: What biases do you introduce to the networks by only including interactions at a single feeder? How many individuals use multiple feeders?

L470: I am not convinced the use of clique (in the strict network analysis definition) is correct here.

L505: I would suggest making it clear earlier in this description that simulations were repeated multiple times in each network.

L520: Is this number correct given different thresholds were used too for further simulation runs?

L530-53: Would be good to provide confirmatory information on model goodness of fit checks and clarify how statistical inference was done (presumably from the full/fitted model?).

I hope my comments help improve the manuscript.

Reviewer #3 (Recommendations for the authors):

This study is a timely theoretical exploration of how variation in transmission rules interacts with variation in social phenotype to influence diffusion dynamics. The authors predict that the likelihood of an individual adopting novel behaviors should depend on the learning rule, as well as the individual's sociality. The authors explore the spread of behavior under 4 different learning rules: a simple adoption rule, a threshold rule, a proportion rule and a conformity adoption rule. They quantify the sociality of individuals by calculating their weighted degree, clustering coefficient and betweenness.

The authors find that under simple and threshold rules, high degree, high betweenness, and low clustered individuals acquired the seeded behavior earlier in simulations. Under proportional and conformity rules, there was no strong relationship between social phenotype and order of acquisition. The authors find that network size predicts the magnitude and direction of the correlation between social phenotype and order of acquisition and that this relationship also depends on the learning rules.

Strengths

1. Overall the paper is well written, and the motivation for using computational simulations is well warranted to explore this question.

2. The topic is timely, and tackles an important theoretical question of how variation in learning rules might interact with social phenotype to influence cultural diffusions. This is a difficult topic to address but is critical for improving our understanding of how diffusions might differ between populations.

3. The authors construct simulations using real social networks of great tits, rather than artificially generated networks, which is a rarity, and thus of great value, in the SL modeling literature. These networks are hard earned -- taken at a relatively fine temporal scale from weekly sampling.

4. The authors provide a thorough discussion of the implications of their results.

Weaknesses

1. One main weaknesses of the paper is the lack of details given about the transmission model. The authors do not provide equations, descriptions of parameters, a detailed schedule of the model. The descriptions they do provide are spread throughout the manuscript, making it more difficult to assess. NBDA is definitely an appropriate model for the question they want to answer, but it seems like the authors have altered some features of the model (e.g., only 1 individual can learn per timestep, 1 individual must learn per timestep). This lack of clarity makes it harder to assess the results they present. Further, from their description, it appears that they have allowed for asocial learning, which adds unnecessary noise to a study that is focused on social transmission.

2. Another main weakness is that the authors do not use a sensitivity analysis, and thus it is difficult to assess the relative effects of each network metric, as they are not necessarily independent of one another. For example, degree and clustering can be correlated simply as a result of how clustering is calculated. This is the downside of using real networks, as without synthetic data, there may be insufficient data to perform a sensitivity analysis. Further, the authors do not present an assessment of variation in their results, instead showing mean values within network size as evidence of their claims.

3. Related to the interpretation of sociality, there is opportunity to increase clarity. The authors describe more social individuals as having a high degree, high betweenness, and low clustering, and less social individuals as low degree, low betweenness and high clustering. One could also imagine a bird who has high degree, low betweenness, and high clustering, being at the center of their group, but rarely going between groups. It seems harder to argue that this bird is less social than a bird with high degree and high betweenness but low clustering. The manuscript would benefit from a careful description of how different combinations of these social metrics could be interpreted.

Point by point comments

1. It should probably be mentioned somewhere in the introduction that social learning rules apply to either the social transmission of novel behavior (e.g., Aplin et al. 2015) or the social influence of others on behavior (e.g., Pike and Laland 2010, Danchin 2018), and that you aim specifically to look at social transmission.

2. The initial conditions of the simulations are not well enough explained before we get to the results. I was left wondering how the authors chose the first knowledgeable agent, which isn't answered until later.

3. The methods section could use more explanation. Those who are unfamiliar with NBDA would need to refer to other publications to see the equations, especially the meaning of 's=1', etc. Also, what are the other parameters set to (λ, A)? Consider including the equations, as well as a more thorough description of parameters. The same could be said for equations describing the network metrics.

4. Related to point 4, what happens when A=0, in a pure social learning environment? This would reduce stochasticity due to asocial innovations, and would provide a pure test of the effect that authors predict arises from sociality and learning rules.

5. L470 "foal" should be "focal".

6. I actually think it's more helpful to show results when you standardize network size in the main text, and put Figure 2 in the supplement. Figure 2 is difficult to read, and something like Figure S2 is easier to interpret if you're assessing relative differences in diffusion dynamics. Also rather than presenting each network size as a color, select one network size (or a binned size) and present a variation metric (e.g., percentile intervals).

7. Suggest changing section title "Social network size and behavioral spreading" to match first section "Relationship between…". Also suggest "diffusion" rather than behavioural spreading. After reading the section, this seems more to do with how network size impacts the correlation between variables, rather than the diffusion itself. Maybe change the heading to reflect this?

8. L204 – 231: Overall I think this section is fairly dense compared to the first section, and after reading it several times, I'm still not sure what I should take away from it. It looks like you have a very low N at large network sizes, which could drive some of these correlations in Figure 4. The fact that agents can asocially learn also makes it hard to interpret what these correlations mean.

9. L204-216: I had to read the beginning of this section several times, and it's more confusing than the first section of results. The results communicated until L210 do not relate to network size, and seem to repeat the previous section. I suggest removing this or incorporating it into the previous section and starting with how network size affected simulation dynamics.

a. Also I suggest rewriting to avoid putting the variable of interest in parentheses (e.g., L 209, 213).

b. L208: "the mean average network metric" was confusing -- do you mean "average network measure"?

c. L210: I suggest "The direction and magnitude of the correlation between ind. Sociality and order of acquisition were predicted by network size. This relationship was modulated by transmission rule…" to improve clarity.

10. Figure 4: I find it very hard to see all 4 lines, maybe choose different colors?

11. L224: Which means network metric?

12. L248: This information about initial conditions should come before the results.

13. L248: "Spreading simulation" -> diffusion simulation.

14. L253: Without the equations written out in the methods, it's difficult to assess how the learning model works. Is asocial learning turned off under obligate social learning? It's my understanding that in NBDA, the s parameter controls the relative strength of social learning per unit connection to asocial learning. In the usual formalization of NBDA, the probability of asocial learning is constant in all individuals, contra L251 which states that asocial learning only occurs in unconnected individuals. Does your model assume that individuals who are "well-connected" (also undefined in the manuscript) have the $A$ parameter set to zero? If this is the case, the authors should include a justification/definition of being well-connected.

15. L317: I'm still finding it hard to wrap my head around how a bird with low clustering is central and highly social. A nice way to explain/justify the differences between more and less social individuals would be to make a figure of an exemplar network, with several stereotypes highlighted, along with their social metrics.

16. L332: Cantor et al. (2021, Proc. R. Soc. B) should probably also be cited here, as they measure the performance of recombination and subsequent diffusion.

17. L342: Overall, this manuscript has synergy with the study "Cultural diffusion dynamics depend on behavioural production rules" (doi.org/10.1098/rspb.2022.1001), which explicitly explores the difference between acquisition and usage, and also uses NBDA as a generative model. It would be relevant to cite here.

18. Figure 5: If individuals have a low probability of social learning, do they have a high probability of asocial learning? Or not learning at all? Are there cases when both the probability of individual learning and social learning are low? Also, this is another case where normalizing the x axis between network sizes would be more informative. The authors might set asocial learning to 0 and simply directly measure the probability of acquisition by each naive agent at each time-step, since the manuscript is focused on social transmission rather than social transmission and asocial learning.

19. Related to the interpretation of the model, the authors use the word "adopt" throughout the manuscript, although one could argue that their model is not of adoption, but of knowledge transmission, since there is no mechanism to determine whether individuals would actually use the behavior once acquiring knowledge of it. In other places, the authors have used the language of knowledge transmission (e.g., Figure 1 caption). It might be best to stick with knowledge transmission throughout the paper.
