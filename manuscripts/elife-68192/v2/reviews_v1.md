# Peer review - Round 1

Editors:
- Tatyana O Sharpee, https://ror.org/03xez1567 Salk Institute for Biological Studies United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.68192.sa0](https://doi.org/10.7554/eLife.68192.sa0)

This work introduces a new unsupervised Bayesian method for identifying important patterns in neural population responses. The method offers improvements relative methods that do not assume correlations in neural responses, and is likely to also outperform methods that take into account pairwise correlations in neural responses.


---

# Peer review - Round 1

Editors:
- Tatyana O Sharpee, https://ror.org/03xez1567 Salk Institute for Biological Studies United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.68192.sa1](https://doi.org/10.7554/eLife.68192.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

[Editors’ note: the authors submitted for reconsideration following the decision after peer review. What follows is the decision letter after the first round of review.]

Thank you for submitting your work entitled "Unsupervised Bayesian Ising Approximation for revealing the neural dictionary in songbirds" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and a Senior Editor. The reviewers have opted to remain anonymous.

Our decision has been reached after consultation between the reviewers and your reviewing editor. It took an unusually long time to reach this decision due to both personal and global health emergencies. We are sorry for the delay. Based on these discussions and the individual reviews below, we regret to inform you that this manuscript will not be considered further for publication in eLife as a Research Article.

However, your reviewing editor and reviewers have agreed that they would be willing to consider a revised version of the paper, reformatted as a "Tools and Resources" paper, if you choose to resubmit it as such to eLife. That revised paper should address fully the methodological and technical questions raised by the reviewers and your reviewing editor in this letter. As it stands, the reviewing team did not feel that they had enough information to properly judge the merits of the method, and that would be reassessed if a new and revised Tools and Resources manuscript is submitted.

The individual reviewer comments are appended below and can be used either as directives for that new submission, or as helpful pointers for a submission elsewhere. Summary thoughts are included here, with the detailed reviews from the 2 reviewers included at the end.

The paper details a new approach to learning the input/output relationships in complex biological systems that drive things like motor behavior or (perhaps) protein folding and other processes. The work focuses on birdsong as an example of a complex motor task potentially modulated by precise temporal patterns of spiking in the bird motor cortex (RA). The method claims to be able to use very few jointly recorded samples of the input and output to learn both a model for the distribution of the spiking patterns observed as well as how they drive behavior. The method uses strong priors in a Bayesian Ising Approximation to identify the neural code words that are expressed at unusually high or low frequency with respect to the behavioral output. The authors find a large number of spike patterns correlated with behavioral variations in syllable pitch. The method has potential applications beyond birdsong; the ability to fit input/output relationships with very few samples is appealing.

The reviewing team, however, had some major reservations about the results and felt that the current draft did not give them enough details to properly evaluate the method. A summary of those major points is given here:

1) The method:

The reviewers felt that there wasn't enough detail presented to clearly analyze the results of the model. Much of the detail was in the SI and Methods, where the exposition wasn't clear or detailed enough for the reader to properly assess the results.

Questions raised included:

– What's the null model?

– How does this method scale to larger neural populations?

– Is the clustering used here justified? Can it be compared to other, simpler clustering methods?

– How do you justify the choice of prior and how are the unknowns fit from the data?

– Other extant methods for finding reliable interactions in exponential models were not referenced or compared.

– Artificial data used in the SI are based on properties of the recorded neurons, and as the authors explain the cells seem to be quite weakly coupled, so the relevance of the model for other data is not clear.

2) The behavioral results:

The reviewers were not convinced by the pitch results, primarily because of the coarse-graining of pitch into just two categories. Again, much of the explanation was relegated to the Methods part of the paper and could have been presented more clearly. If this method works, this is clearly interesting, but the results presented seemed rather weak.

3) The format of the paper:

The paper read a bit like 3 manuscripts glued together, each of which has merits, but none of which seemed to satisfactorily stand on its own. The paper starts with a grand introduction that talks about solving a major challenge in quantitative biology. Then it quickly dives into something that reads more like a methods paper, but with insufficient exposition and clarity. Finally, the paper shifts to the application of the method to behavior and neural data, the results of which seemed somewhat weak and preliminary.

Taking these critiques together, the reviewing team felt that the paper could not be reasonably revised for eLife as a Research Article. However, the team did find the central method potentially interesting if more details are provided that allow for proper assessment of it. The team felt that it could be a good "Tools and Resources" advance, if the method holds up to this more detailed scrutiny.

Reviewer 2:

The paper is a potentially interesting application of a recent statistical method, the Bayesian Ising Approximation (Fisher and Mehta), aimed at addressing the problem of estimating a complex distribution, in particular the relationship between a code and an output, from very few samples. This is accomplished by heavily weighting by the prior. The authors have applied this method to support the idea that there are precisely timed spike patterns that are especially significant in the generation of behavior, in this case in the output of syllables of birdsong. They use the method to identify "code words", patterns that are claimed to appear with notably high or low frequency in correspondence with a behavioral variable. They apply this method to find a larger number of precise spike patterns correlated with behavioral variations in the tails of the behavioral distribution. They suggest an interpretation that perhaps larger exploratory motor gestures require a more precise spiking code; although it might also be argued that this shows that there are more ways to achieve these larger fluctuations? While the claim is counterintuitive, it rests on the power of the method, whose exposition left a number of gaps.

1. It is unclear to what extent this goal is meaningful in the case that the paper analyses: premotor drive of muscles in the birdsong pathway. It seems evident that timing of RA spikes necessarily sculpt motor output; and the authors have previously analyzed this in detail to reveal timing precision (Tang et al.). It was not clear, however, that specific patterns meaningfully emerge from a sea of similar spike trains to encode exact outputs. The authors ask whether precise patterns in 2ms bins have a significant relationship with binarized song characteristics in 40ms bins-a very low fidelity relationship on the "behavior" side compared with a high level of precision on the neural side. This seems a dramatic discrepancy between the dimensionality of neural response vs behavior that deserves more justification. How general a space of coding relationships (nonmonotonic, etc) does this method explore given this binarization?

2. Further, it was unclear whether a temporally structured firing rate would be equally convincing as a representation of behavioral variation. While the concept of "irreducible dictionaries" is appealing, does this method fairly compare a timing code to a rate code? For example, doesn't the competition component of the model suppress the identification of firing rate-like contributions? Looking at Figure 1, the cartoon of eliminating overlapping but similar code words seem equivalent to ignoring a less temporally precise method of coding for behavior. That is to say, if you are forcing your model to choose one of several similar code words in a winner-take all inclusion choice, isn't the timing precision you see partially a factor of not looking at the other similar code words which didn't win out? The comparison of this method to GLM methods of relating the spiking to behavior is unclear. One alternative model was analyzed in the online methods, but is not clearly explained and such comparisons deserve to be treated in the main text. It should also be easy to report the simple 0th order analysis of how well you can predict the binary version of behavior simply with a spike count within the 40 ms window, or with some intermediate level of temporal variation. Seeing these comparisons as a control of the assertion that precise timing matters in this system would enhance intuition for the necessity of this method and better justify the claim "that they predict behavioral features better than other approaches" (line 256).

3. In general, the exposition of the method leaves many questions and could be improved considerably in clarity. I have tried to summarize the logic of the paper's core argument below and underscored throughout where more help could be given to understand the meaning and generality of assumptions made.

Logic of the calculation:

The paper sets up the problem of writing down a model for the joint probability of a behavioral event s0 and the firing of a spike in each, i, of N bins, σi. The authors write this in terms of an expansion over every possible combination of σi,

Log P(σ|θμ) = -log Z + Σ θμ Π _{i in Vμ} σi.

Q3.1: please expand a little on the exponential form. In maximum entropy approaches, this form of distribution arises from the maximum entropy solution, but if we are avoiding MaxEnt approaches, can you briefly justify it? In this approach, a firing pattern with spikes in bins (1,2,3,4) is considered to be independent of the events (1,2) and (3,4); whereas in maxent, if one is only expanding up to order 2, one hypothesizes that the probability of the word (1,2,3,4) will be absorbed into the pairwise probabilities, and one can ask how different the data is from that guess. It seems that here one is parametrizing with vastly more parameters-one for every possible spike/behavior combination-- without a systematic method of cutting them down (or at least one that was clear to me; it is addressed at the end of the Online Methods calculations once we have moved into the s variables but it would be helpful to get some intuition from the start).

One then defines "indicator variables" sμ which tell us which patterns appear significantly less or more often than one would expect under some null model. It would be good to specify this null model right away, and in straightforward terms; I don't see it defined in the main text at all.

Q3.2: Please explain at this point the null model for the frequency of appearance of any possible pattern of spikes and its correlation with behavior? Should it not depend on the specific behavior?

It is unclear why one is now allowed to write that the original definition of the model is EQUAL to the model now written including only terms defined by a criterion defined by our subjective interest in them:

Log P(σ|θ) = -log Z + Σ θμ sμ Π _{i in Vμ} σi

Q3.3: Why does one not here need to define a new and different probability distribution, something that makes some claim about belonging to the codeword dictionary, in which these terms are the only ones that appear?

Now the authors turn to the task of estimating the 2N parameters θμ. Instead of doing this estimation directly from the data (i.e. the a posteriori expectation), they use a prior on these values: they choose to assume that each of the values are narrowly distributed about some mean θ∗μ:

P(θ∗μ : sμ=1) ~ exp(-(θμ −θ∗μ)2).

This distribution is taken only to hold if the word is indeed a code word, ie statistically associated with a behavior. If it is not a code word, the prior is not defined.

Q3.4: Please justify this choice in more detail. Why are the epsilons not dependent on μ?

Q3.5: The argument for where these 2N values of θ∗μ come from is very unclear. Please spell out more clearly how constraining the means of the individual σis provides sufficient constraints for all 2N values, or why this is not needed.

Q3.6: Why does a code word have an a priori likelihood of 0.5 of being in the dictionary?

Now rather than estimating or computing the values of the θμs, the next step is to flip the variables in the distribution we seek, to P(s|theta), and then integrate out the thetas, based (it seems?) only on their prior distributions, Equation (5).

Q3.7: Now that s can again take value of either 0 or 1, why did we not need the distribution over θs in the case that s = 0? How can a distribution over s on the LHS in Equation (5) limit itself to the case of s = 1 on the RHS?

The calculations in the online methods may resolve some of these issues? But these all appear to start from Equation (5) and at least for me at this stage, the route to this equation is unclear.

Reviewer #3:

The manuscript suggests a new approach to learning coding dictionaries. The method is applied to neural population data recorded in singing birds. While the idea of the approach is interesting, it was hard to understand the details or how well it works. It seems that too much has been pushed to the SI, and more controls and examples over synthetic data sets would be useful. Moreover, and importantly – it was hard to interpret the results. Also, the current approach was not compared against other methods presented in recent years for learning metrics on neural population patterns, or even more simple clustering approaches.

Briefly, the authors use a log-linear model for the population words of N neurons and two behavioral states – using 2^(N+1) terms that span all potential orders of interactions among cells (theta's). To avoid arbitrary cutoff on the order of interactions that they consider, and use the important ones, they use a constructed prior distribution over theta's to learn a posterior model over the population words after integrating out the theta's. This gives an Ising model over 2^N interacting 'spins' where each sping now stands for a word that may or may not have appeared in the sampled data. The local fields acting on each of these spins is related to the prob of appearance of the words the spins stand for, and the pairwise interaction terms stand for an overlap between the words. These interactions now imply a 'competition' between words in terms of the explanatory power they carry (and are therefore typically negative)

Thus, if I understand this correctly, the constructed model gives a form of compression of the population 'codebook' by picking words that are dominant to be included in the dictionary and omitting similar words with less explanatory power and frequency.

Critically, it was unclear to me how one should evaluate the results. It is hard to interpret the structure of the dictionary in Figures4-5, and in particular over the pooling of conditions in Figure 5. In addition, there have been different approaches towards learning neural dictionaries in recent years, which are not mentioned here or compared against the current approach. Maybe this is too naïve, but it seems natural to ask how well would naïve clustering or Edit-distance based methods work here? Then, how does the current approach compare to more structured metrics such as those presented in Ganmor et al. eLife 2015, Prentice et al. Plos Comp Biol 2016, Rubin et al. Nature Comm, 2019, or Chaudhuri et al. Nature Neuro, 2019 ?

Finally, how would approach work for larger populations, where all observed patterns would appear just once?

It was not clear how should one interpret the nature of the organization of patterns in Figure 4B (the gap between lines, their very linear dependency?)

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for submitting your article "Unsupervised Bayesian Ising Approximation for decoding neural activity and other biological dictionaries" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Aleksandra Walczak as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) The numerical comparison to other existing methods is minimal and should be expanded. The analysis of the irreducibility of the codewords has insufficient support based on the numerical simulations. Moreover, the generality of the tool and comparison to other methods are discussed in almost entirely theoretical terms, which makes the claim on immediate utility for other datasets less convincing, especially outside the neuroscience community. In particular, the identified codewords are relatively short (3rd, 4th order stats) and N=20 is easy to fit an Ising model; so one would think that it would be relatively straightforward to fit the Ganmor model jointly. At least on artificial data one should be able to explore a larger N regime where there is a more immediate gain relative to existing models.

2) Although the paper is written as a methods paper, emphasizing the technical contributions and promising wide applicability to a range of different types of datasets, the numerical validation of the method is very much restricted to the statistical regime of the songbird dataset. From the perspective of a potential future user of the tool it's less clear how the method would behave on different datasets, and what needs to happen in practice for adopting the tool to data with different statistics. Based on current content, it would be better to focus the abstract and introduction on applications that are actually studied here.

3) The songbird analysis already reveals some challenges with respect to interpretability: in particular it is not clear how much information about the underlying neural processes can be revealed by summary statistics generated by the method, such as the number of codewords and their length distribution.

4) Limiting the analysis to N=20 patterns with somewhat random code structure makes it hard for a potential user of the tool to work out what needs to change when switching to a novel dataset (with respect to N, M, codeword complexity, sparsity of neural responses). Some work could be invested in spelling out the considerations of applicability with respect to quantities that an experimentalist would know about the data.

5) Is it possible to include multiple binary quantifications of behavior, similarly to how words are constructed from neural spike trains? For example, one can envision describing a particular song segment with respect to multiple binary features simultaneously.

Reviewer #1 (Recommendations for the authors):

Line 168: I think the notation here should P(s_mu=0) not s_mu=-1.

Reviewer #2 (Recommendations for the authors):

I am overall very excited about the framework and I see significant technical potential in the approach. Nonetheless, there are several missed opportunities in the numerical analysis, and things that could and should probably be improved to maximize the impact of the work on the broader community.

– Limiting the analysis to N=20 patterns with somewhat random code structure makes it hard for a potential user of the tool to work out what needs to change when switching to a novel dataset (with respect to N, M, codeword complexity, sparsity of neural responses). Some work could be invested in spelling out the considerations of applicability with respect to quantities that an experimentalist would know about the data.

– The codeword irreducibility could be analyzed in more detail, again in terms of experimentally relevant quantities.

– The comparison to other methods is minimal. The identified codewords are relatively short (third, fourth order stats) and N=20 is easy to fit an Ising model; so I'd think that it would be relatively straightforward to fit the Ganmor model jointly. At least on artificial data one should be able to explore a larger N regime where there is a more immediate gain relative to existing models.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Unsupervised Bayesian Ising Approximation for decoding neural activity and other biological dictionaries" for further consideration by eLife. Your revised article has been evaluated by Aleksandra Walczak (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

Essential revisions:

Thank you for the revised manuscript. The reviewers found the manuscript much improved and close to acceptance. Nevertheless, reviewers are suggesting a few additional analyses to demonstrate the advantages of the method and increase its impact.

1) Please consider the null model that includes pairwise correlations.

2) Please test the method to a larger dataset.

Reviewer #2 (Recommendations for the authors):

I generally find that the revisions have improved the overall clarity of the text, and addressed most of my questions.

Nonetheless, I found the answer to two of my concerns underwhelming:

– Discussing the practical considerations about translating the approach to other datasets (new discussion paragraph) is quite vague, essentially saying that the hyperparameters will more or less have to be figured out de novo. I was expecting a quantitative description of how different statistical properties of the data affect the process, which would translate into something closer to a concrete recipe for hyperparameters adjustment. The fact that this is not straightforward to do makes a broad adoption of the tool less likely.

– The concern about the overall interpretability of the extracted statistics remains unaddressed. I don't agree with the position is that "it only matters to estimate these statistics well, interpretation can come later." Being able to estimate a quantity does not necessarily make it useful to do. In the context of songbird specifically, the paper make the case for the results being difficult to interpret even when the statistics are well estimated. This seems like a pretty big problem, at least big enough to warrant a minimum amount of thought and a couple of sentences in the discussion.

Reviewer #3 (Recommendations for the authors):

The authors already made a great effort to improve their manuscript. However, from my side, I provide the following concerns about the significance and broad impact of the current revised manuscript.

Strength of the manuscript

The traditional model of maximum entropy type requires a large amount of data to predict effective interactions among elements (e.g., neurons), and fails to identify statistically over- or under-represented (relative to a null model) codewords, and thus the neural-behavior prediction remains elusive. This manuscript provides a novel approach that can systematically search for the significant codewords, yet requiring fewer data samples (compared to the number of higher-order model parameters).

The method first writes all orders of interactions in a probability distribution form; finding non-zero higher order interaction parameters could tell which codewords should be included in the neural dictionary and how they matter. To make the method algorithmically solvable, the authors turn the optimization into an Ising model of interacting indicator variables. This indicator variable is responsible for identification of key codewords. The inferred value of the external fields signals the importance of the codeword, while the sign of the high-order interaction parameter reflects whether the word is over or under-represented. To explain the neural-behavior correlates, the authors also include the behavior variable into the components of the activity. This framework works consistently in the songbird motor experiments.

Weakness of the manuscript

To relate the neural activity and behavior, the authors test their method in both synthetic data and songbird real data. There are two weakness, considering the impact of the method in a broad context. First, the variable size is limited to N~20, which is severely below the number of neurons the neural data scientists get interested in (e.g., for modeling retinal ganglion cells, and even cortical cells). This may be a tradeoff between all order of interactions to be considered and the number of model parameters. Second, a null model is chosen to be an independent model that neglects correlations in the data, which may affect the characterization of the redundancy of the uBIA model. Even if an irreducible ensemble of codewords is obtained, what is the predictive power of this ensemble with respect to control the macroscopic behavior (e.g., skilled motor control or sensorimotor learning), rather than showing statistics of neural-behavior activity, remains obscure in the current manuscript.

Considering the strength and weakness of the manuscript, I recommend the following issues for the authors to improve their idea.

1. The proposed model is limited to symmetric couplings and i.i.d data samples. First, in a neural circuit, the asymmetric coupling is common among neurons; Second, the temporal order of each spiking activity may play a key role in encoding information. For example, a paper "Blindfold learning of an accurate neural metric" (PNAS, 2018) takes the temporal information into account. When putting in the context of neural-behavior relationship, these two factors would become important. But they seem neglected in the current manuscript.

2. To achieve a higher-order-interaction-included and non-redundant model is really important problem in the field. For example, the reliable interaction model proposed in ref. 26 is not fully compared in the current manuscript, i.e., what is the new advance? This is better to clearly demonstrated in a plot in the main text. Second, a recent paper (Phys Rev E, 104, 024407, 2021) used an information-based criterion to identify statistically significant couplings, which may be applicable to the context the authors consider here. In this eLife submission, the method relies on the magnetization inclusion threshold, which may be expensive for real data analysis.

3. On the equation 1, the authors seem to use the local model parameter to detect the global significance of the collective codeword, which I could not understand very well, because a codeword is determined by all order of interactions considered in the log-linear model.

4. Technically, the logic going from Equation 7 to Equation 8 is broken, since the s-dependence in Equation 8 does not naturally arise from Equation7.

5. I could not understand well how the sign of reflects whether the word is over- or under-represented, and even, how the parameter account for the reducibility of the dictionaries. This part is better to be expanded in the manuscript, although these parameters have highly non-linear function relationship.
