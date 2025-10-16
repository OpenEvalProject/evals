# Peer review - Round 1

Editors:
- David Donoso, Escuela Politécnica Nacional Ecuador

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.57788.sa1](https://doi.org/10.7554/eLife.57788.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

For decades, negative density dependence (NDD) has been a major paradigm guiding theoretical and experimental research on mechanisms maintaining biodiversity. This paper goes outside the box and provides mathematical support for positive density dependence (PDD) as an additional viable force maintaining biodiversity. By reducing mortality, PDD could limit the exclusion of less competitive species by dominant ones. We are sure that this manuscript will inspire both theoreticians and field biologists aiming to understand how species to coexist in nature.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting your work entitled "Positive density-dependence acting on mortality can help maintain species-rich communities" for consideration by eLife. Your article has been reviewed by three peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The reviewers have opted to remain anonymous.

Our decision has been reached after consultation between the reviewers. Based on these discussions and the individual reviews below, we regret to inform you that your work will not be considered further for publication in eLife. We all agree, however, that an improved version of the manuscript (addressing completely reviewer's points below) may be submitted as a new submission in eLife.

All reviewers find merit in your study. And all of them suggest that more theoretical work (like yours) is needed to expand the field, given that positive density-dependence is so often observed in nature. The manuscript is inspiring. For example, one of the reviewers highlighted: "This manuscript is very creative and thought-provoking because it makes me think more about very steep positive density-dependent gradients in a new light, as facilitating coexistence rather than being a unique part of species' ecology". The reviewers also applaud the author's efforts in proposing potentially new mechanisms of species coexistence in light of positive density-dependence. However, the author needs to make more efforts in building biological motivation and checking the robustness of the results. The manuscript is too theoretical/mathematical for the eLife audience and lacks more-biological 'real-life' examples.

Reviewer #1:

I think Aubier accomplished an interesting modeling manuscript on an interesting topic, positive density dependence acting on mortality. However, I feel the manuscript is too theoretical/mathematical for eLife and lacks a more-biological 'real-life' examples.

I do think that a glossary, and a comparative table with NDD on the left, and PDD on the right, then specific patters (like PDD on mortality) on a second row, then possible mechanisms responsible for these patterns, outcomes, and finally examples in real life, could be something to add.

I think the author can do more to have an easily understandable manuscript. All, the mathematical formulas, the graphs, and the text itself are very difficult to follow. Even the code in the zip file is not annotated. This does not have to be this way. Also, some re-ordering may be also appropriate (the first paragraph in the Discussion should likely be the first of the Introduction), and many ideas are repeated two or more times (i.e., Positive density-dependence has been described for most major animal taxa…). Some combinations of words, like existence of coexistence, just make your manuscript unnecessarily difficult to follow. And discussion on mimicry seems just speculation at this point.

Sorry for self-advertizing, but in one of my papers, we forced NDD to Devil's Gardens, one case where ants decrease plant mortality. So patches of monospecific plants accumulate in the forest. We really had a hard time explaining this non-NDD case, (I guess this is then a case of PDD). What I want to say is that there are potentially hundreds of ecologists out there dealing with similar issues in their own system. This manuscript could benefit them. Currently, it does not.

Reviewer #2:

This manuscript is very creative and thought-provoking because it makes me think more about very steep positive density-dependent gradients in a new light, as facilitating coexistence rather than being a unique part of species' ecology. For example, bighorn sheep suffer strong Allee effects because small groups are depredated quickly by mountain lions. This is a terrific example of the Allee effect, but one rarely thinks of this sort of positive density dependence as being a mechanism of species coexistence between large ungulates. This paper makes me think about that.

I do think that the model needs more contextualization in biology from top to bottom. I had to read very carefully, and twice, to understand what I did – for eLife, the paper has to sing so that readers get most of it on the first read. There is an opportunity, and I would argue a necessity, to clarify intra- and interspecific density-dependent processes in the Introduction. The choice of terms in the modeling equations themselves could also be better tied to biology to explain exactly what kinds of systems they represent, and how broadly they can be interpreted. My specific comments are below:

1) Negative density dependence favors coexistence if intraspecific density dependence is stronger than interspecific density dependence. Positive density-dependence seems like a strange mechanism to promote species coexistence when it is interspecific because the most abundant species should only become a stronger and stronger competitor as it rises in abundance. Intraspecific positive density dependence – e.g. Allee effects – seems to make it more difficult for rare species to invade, so it does not promote global stability (subsection “Analytical resolution”, second paragraph). As I understand the analytical part of the model (and I have to be honest, I only read Supplementary file 1A), positive density dependence is only intraspecific because the D(ni) function for each species only includes individuals of that species. s it is always the same between species, though so their density dependence varies perfectly in tandem. I think this is really what struck me as counterintuitive because if I were to think about positive density dependence in the context of competition, I would imagine it to operate interspecifically as well so that the more abundant a species was, the better it would be able to outcompete its competitors (45-47). If I am right about what the model means, then it might be very helpful in the Introduction to explain not just "positive density dependence" writ large, but the different ways it might function (e.g. interspecifically versus intraspecifically, or using specific natural history examples that the model applies to and contrasting them to natural history examples where it does not). The fourth paragraph of the Introduction starts to do this, but are very abstract and don't go into enough detail about differences in kinds of positive density dependence, only its general effects.

2) At very high values of positive frequency dependence, the effects of positive density dependence essentially disappear because the populations hit zero mortality so quickly. I could imagine this being very important in cases where there are for example two aposematic species and both have sufficiently high population sizes that both are protected from predation. Perhaps it would also make sense to imagine two species of pack-hunting carnivores that have zero success alone, but much greater success with even a few individuals, so the two species might be able to coexist as long as both are already present in sufficient abundance. This is sort of an Allee effect too, of course, which are also experienced by species of herd animals that cannot survive in small groups, because they are too vulnerable to predation. But this model seems to describe species that are very similar in their ecology, not just because they are forced to be so to analyze the effects of density dependence, but also because density has identical intraspecific effects. Is this true? If so it would be helpful to explain in the text, and if not, then it would be helpful to explain how broadly it applies.

3) In (2), has the carrying capacity – or effective carrying capacity – also changed? Is the purpose of this model to contrast with (1), where one spp. is a superior competitor, whereas here in (2), one spp. is a superior reproducer/survivor?

4) For Equation 3, I need more hand-holding to explain what's going on. It looks like the new term n2/(n2 + a'1*n1) means the frequency of individuals in the community that is composed of n2 – is that correct? So is this a way of incorporating positive interspecific frequency dependence into your model that already includes positive intraspecific density dependence? Would there be any difference if you modeled reproductive interference as an effect on d rather than on ni, since in a literal way it should affect reproduction rather than carrying capacity? I could also imagine it not matter if its influence is only supposed to be manifest by decreasing dn2/dt, though.

Reviewer #3:

Positive density-dependence is widely observed in nature. It is widely believed that positive density-dependence inhibits species coexistence. The main result of this manuscript is that a positive density-dependence on mortality, under certain forms of population dynamics, increases the feasibility domain of species coexistence. The paper is well-written (but I am not sure if the math here would be easily accessible to the majority of the readership at eLife). I applaud the author's efforts in proposing potentially new mechanisms of species coexistence by positive density-dependence, which could be an important contribution to the coexistence theory. However, the author needs to make more efforts in building biological motivation and checking the robustness of the results.

1) The biological relevance.

– The author motivated the paper by pointing up the ubiquitousness of positive density-dependence (Introduction, fifth paragraph). However, if I understood correctly, most references focus on the Allee effect of the birth rates. Then, is there substantive literature of empirical evidence that positive density-dependence acts on mortality? To be clear, I am not saying that there is not, but to encourage the author to be more explicit about the biological motivations.

– In the fifth paragraph of the Discussion, the author concluded that it is yet impossible to validate the results. I apologize if I misunderstood, but I feel that the paper offers no guidelines for empirical tests. To be clear, I am not asking the author to run analysis on some empirical data, but to encourage the author to discuss how this theory can be potentially tested. Otherwise, it may leave the reader the impression of a math exercise disconnected from ecological nature.

2) The robustness of the results. I understand the following requests can be a bit much, but I sincerely believe that when one proposes a new ecological mechanism, the author needs to prove that it is theoretically robust to convince the empiricists. However, I am happy for a discussion if the author disagrees with anything follows.

– This paper only studies one particular functional form of mortality with positive density-dependence. As the author stated that "assessing the functional form of positive density-dependence in natural populations is tedious", I think the author needs to study other functional forms of positive density-dependence, at least in the 2-species case.

– This paper does not have a sort of null model to estimate the effects of positive density-dependence. That is, whether the effects of positive density-dependence solely comes with the non-linear functional form or because of the positiveness. To do this, I suggest the author add some additional tests on negative density-dependence with the same functional response, to see that the effects are actually coming from positiveness.

– This paper considers the same functional form of positive density-dependence for every species. However, I think it is worth examining some with positive density-dependence and some without in multi-species case.

– To be honest, I am a bit lost why section 1 exists. I thought the author tries to prove that positive density-dependence helps coexistence, but why spent so much time on a particular case where positive density-dependence inhibits coexistence?

– I don't find the parametrization in Supplementary file 1D satisfactory. The range of parameters seems very arbitrary to me. I was puzzled that why no other parametrizations were examined.
