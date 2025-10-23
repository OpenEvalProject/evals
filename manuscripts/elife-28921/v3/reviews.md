# Peer review - Round 1

Editors:
- Patricia J Wittkopp, University of Michigan United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.28921.036](https://doi.org/10.7554/eLife.28921.036)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Intermolecular epistasis increases phenotypic variation in a gene regulatory system" for consideration by eLife. Your article has been reviewed by three peer reviewers and the evaluation has been overseen by Patricia Wittkopp as the Reviewing Editor and Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has assembled a list of concerns for you to consider.

Summary:

The creative approach to investigating an important question (interactions among genetic changes affecting cis- and trans-regulatory components of a regulatory network) was applauded, but concerns were raised by two of the reviewers about the null model used to infer the effects of epistasis. Following discussion, we all agreed this is a major concern since this test underlies the core observation and advance of the paper, and must be convincingly addressed. I should note that the remedy for this concern is not straight forward to us, and we anticipate that it will require a proof of principle experiment with a small number of mutants and/or a much more sophisticated mathematical/statistical treatment to better model the null hypothesis. We are concerned that sufficiently addressing this concern will take more than the 2 months typically allowed by eLife for revisions prior to publication and/or result in findings that are less novel, but have decided to extend an opportunity to try to address this concern in a response letter.

Instead of our usual policy of consolidating the remarks, I am attaching the full set of reviews because the concerns are explained in more detail there.

Essential revisions:

1) Revise the null model to better align with prior work and theory, possibly including some proof-of-principle tests of the strategy adopted.

2) Provide stronger support for the conclusion that the interactions are epistatic (non-additive).

Reviewer #1:

The manuscript uses random mutants in a trans-acting repressor and its cis target and finds epistasis such that the combined cis and trans effects are not predicted by their effects alone. The work is conceptually novel and the data provide new insight into how regulatory systems might evolve. My main concern is what the expected phenotype distribution should look like in the absence of epistasis. In part this could be due to a lack of clarity in the definition of epistasis or the clarity of writing.

1) Epistasis is defined differently in different fields. In quantitative genetics (as in this study) it is a non-additive interaction. It appears the assumption is that the cis and trans components are additive on a log scale in the absence of epistasis. However, for fitness the assumption is often that epistasis is a deviation from multiplicative effects. The definition should be clearly stated.

2) Certain epistatic relationships are entirely expected. For example, in the absence of CI the phenotype of the cis + trans mutants should equal that of cis mutants regardless of trans effect since trans mutants are not expressed. This is nicely observed in Figure 2—figure supplement 1.

3) The expected phenotype distribution in the absence of epistasis is not clear and perhaps incorrect. The interpretation of Figure 2 is that there are too many cells with intermediate expression phenotype than expected. However, under a simple additive case one should expect panel D (cis) + panel (G) trans to produce mostly intermediate phenotypes since the most common phenotype in panel D is low expression and the most common in panel G is high expression, and low + high = intermediate. That said, the authors recognize that high expression in panel G (trans) is likely non-functional CI. To account for this they subtract out the high expression of panel G using WT in the absence of CI. This doesn't make sense. When non-functional CI is combine with cis mutations one would expect to see a phenotype distribution of cis in the absence of CI, as shown in Figure 2—figure supplement 1D, which is much more uniform and has a lot of intermediate frequency phenotypes. Eyeballing it looks like this would generate an expected pattern close to that observed a lot of intermediate phenotypes. The interpretation for the intermediate class is that mutant Cis are binding to mutant cis-elements. However, I don't think the authors have clearly shown that the increased frequency of the intermediate class is different from what one expect in the absence of epistasis.

There is not an obvious solution to calculating the expected phenotype distribution. The options I see are given below. However, engaging a mathematical biologist or statistician to appropriate generate expected phenotype distributions may yield better options.

a) average of cis and trans. Note that the methods stats that convolution of cis and trans yields phenotypes outside of biological range. The average of two numbers can't be above both numbers so the convolution must be cis+trans rather than (cis+trans)/2.

b) use a categorical model where cis + non-functional trans (high) = cis in the absence of CI, cis+ functional CI (low) = cis, cis + intermediate trans = weighted average of cis effects with CI and cis effects without CI with weighting depending on the whether intermediate is closer to low or high expression.

Figure 4 also shows expectations in the absence of epistasis that don't make sense. The results show that 7/9 system libraries show prevalent epistasis because adding in the cis mutants alters the phenotypic effects of the trans mutants. The figure and interpretation now seem to use a different definition of epistasis – the one used in classical genetics. In Figure 4 the grey shows unmodified trans and orange shows trans which is modified by cis. Panel G is an example where low trans is combined with high cis mutants. Unmodified (grey) is low, modified (orange) is intermediate or high. The observed distribution is spread across low, intermediate and high expression. But this is exactly what one would expect under an additive model of low + high effects.

4) The convolution of libraries to get an expectation. A gamma distribution was used for the cis library. It would be better to use the actual empirical distribution through random sampling of cis effects and trans effects with replacement. What assumption was made about the trans distribution? It is bimodal so not easily fit to a standard distribution. Is it a gamma after subtraction?

5) Noise in expression should be mentioned as it could contribute as well to the sorting accuracy statements.

6) Properties of mutant library. How was the average mutation frequency measured (1%-7%), and are mutants Poisson distributed. Simply using estimates provided by mutagenesis kit is not a sufficient measure of the library complexity. The manuscript states that 40 clones were Sanger sequenced. Is this 40 for each of the low, intermediate and high? What are the observed average number of mutants? Simply stating that they conform to the expected distribution given by the kit is not ok, you should use the empirical estimate obtained from sequencing.

7) What is the frequency of plasmids with no insert from cloning, either for the CI protein or the cis element? Typically this is low, but clones are confirmed this way. In high throughput experiments there will always be some frequency of plasmids ligated without an insert.

Reviewer #2:

Lagator et al. measure how mutations lead to phenotypic variation in gene expression at the systems levels. This minimal system based on phage lambda contains the CI repressor and a constitutive promoter driving venus-yfp. Three types of mutagenesis libraries were created: the 'cis' library mutated the constitutive promoter, the 'trans' library mutated the protein coding sequence of the CI repressor, and the 'system' library mutated combined both sets of mutations. For each library flow cytometry was used to measure the Distribution of Mutational Effects (DME), the phenotypic variation in gene expression of the population. The main finding is that the quantitative shapes of the DME are different for the cis, trans, and combined libraries. In particular there is an excess of constructs in the combined library with intermediate expression levels. The authors claim epistasis between cis and trans mutations must be invoked to explain the intermediate level phenotypes in the DME of the combined libraries. The authors further discuss how phenotypically neutral mutations may express phenotypes in combination with other mutations.

I may be missing something here, but I think the main result of this manuscript may be trivial. There is a straw man hypothesis in the text which says that "the intuitive expectation (is) that an increase in the number of mutations ought to result in an increase in non-functional ('no expression') phenotypes". I agree that an increased mutation will lead to more loss of function mutations, but in this system loss of function trans mutants in CI increase expression while loss of function cis mutations in the promoter either decrease expression through decreased polymerase binding or increase expression through decreased CI binding. We might very well expect the combined library to have more intermediate phenotypes as loss of function mutations that both increase and decrease expression average each other out. One need not necessarily invoke epistasis to explain the increase in intermediate phenotypes in the combined library.

I also disagree with the primary interpretation that there are many "neutral" cis mutations that then manifest phenotypically in combination with a trans mutation. This is one plausible interpretation. An opposite interpretation is that there are many highly penetrant trans mutations (21.7% in Figure 2E) and that in combination with a cis mutation the effects of these trans mutations are buffered. The 10% increase in intermediate phenotypes in Figure 2H almost exactly mirrors the 10% decrease in high expressing phenotypes. This suggests that a large fraction of intermediate phenotypes come from highly penetrant trans mutations being buffered by cis mutations, and not from silent cis mutations that interact with trans mutations. In other words the mass in the DME moves from the high expressing bin into the medium expressing bin, not from the low expressing bin into the medium bin.

Reviewer #3:

This manuscript describes the DME for interacting cis- and trans-regulatory sequences in a well-defined regulatory system. The primary finding is that epistatic interactions between mutations in these two components produce a larger range of phenotypes than variation in either single component. On the one hand, this type of epistasis is perhaps required to emerge from the known interactions of CI and the cis-sequence in the system. On the other hand, the quantitative consequences of this epistasis have rarely been described in detail and I think it is interesting to see how these interactions shape the phenotypic space explored. The use of mutant alleles with multiple mutations and the absence of any discussion of the identity of mutations mediating the observed epistasis that would have provided more insight into molecular mechanisms reduced my enthusiasm for this work, however. In addition, how much does intramolecular epistasis contribute to the patterns reported? One point where these questions are ameliorated is in the analysis of 109 single point mutations in cis and 73 in trans, but the locations of these changes with CI and the promoter are not described. Looking at the identity of these mutations in more detail might provide some insight into the specific interactions between cis and trans acting factors that produced the intermediate expression phenotypes.

[Editors' note: further revisions were requested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Intermolecular epistasis increases phenotypic variation in a gene regulatory system" for further consideration at eLife. Your revised article has been favorably evaluated by three peer reviewers, and the evaluation was overseen byPatricia Wittkopp as the Reviewing and Senior Editor. The following individual involved in review of your submission has agreed to reveal his identity: Justin Fay.

The manuscript has been improved but there are some remaining issues that need to be addressed before acceptance, as outlined below:

We appreciate the authors response to the reviewer's comments and inclusion of additional data addressing the concerns raised. For example, the definitions of epistasis and the methodology used to compute the naive DME are now more clear and easier to understand. We also appreciated the comparison to an empirically derived DME that accounts for our molecular knowledge of the components of CI system in phage. We remain convinced this is an interesting dataset addressing an interesting question, but also remain concerned that the conclusions drawn depend on the assumptions of the model, some of which we think are not plausible. We also agree, however, that it is not clear what the "correct" set of assumptions should be, so are supportive of publication despite these concerns.

In light of this uncertainty, we think a modification of the title and adjustment of the conclusions is appropriate. For example, we think the title should convey that the structure of regulatory circuits determines patterns of epistasis rather than regulatory circuits generate lots of unexpected epistasis.

In addition, we ask that the authors clarify their work further (no new data is needed). For example, two areas that seem fundamental to understanding the paper are: Does low + low = high expression under a naive model? If so what does low + high equal under an additive model? I'm still not sure. Statements like: "increasing the number of mutated components should introduce additional constraints, limiting the variation accessible through mutation" remain confusing. I am including the full comments from reviewer #1 below because they explain these remaining questions more fully.

Reviewer #1:

In this resubmitted manuscript, the authors revised their analysis and included substantial additional data. Primarily, they measured expression from 150 point mutations along with their double mutants. Overall the manuscript is greatly improved: it is more clearly presented and the individual single double mutant assays provides much greater confidence in their main result – epistasis between cis-trans mutants such that mutant trans-elements can bind mutant cis-elements generating expression patterns not expected from either mutant alone. However, as brought up in the initial review, the calculation of the double mutant expectations is problematic. In part, this may be related to clarity/understanding, but it could also indicate a problem in how these expectations were calculated. The expectations that I find problematic occur in Figure 2, but also in the double mutants, Figure 3 along with Figure 2—figure supplement 2.

Overall, there are some strong indications of surprising epistasis. For me this came from looking at Figure 3—figure supplement 3 through Figure 3—figure supplement 5 showing both the doubles and singles. However, eyeballing it is not easy and it would be much easier to read using bargraphs of single, single, double (obs) and expected. The examples of doubles with negative epistasis (Figure 3—figure supplement 3) seem to be quite small deviations since they look simply like a combination of the two single mutants. However, the cases with positive epistasis are striking in that many show low + low = intermediate rather than low which is what I believe the expectation to be.

While the examples are nice, the main analysis contains expectations that I don't find logical for the naive analysis. "Increasing the number of mutated components should introduce additional constraints, limiting the variation accessible through mutation": I disagree, given two sources of variation, combining them will increase variation beyond each individual component.

Central to the calculation of epistasis is the use of the convolution of cis + trans effects to derive an expectation for the system (doubles). This expectation is shown in Figure 2. The question is what do we expect when we combine a low (cis) with either a low (trans) or high (trans) expression mutant. The convolution predicts this will mostly be high with a small amount of intermediate and low. Under a simple additive model one would expect low + low = low, and low + high = intermediate, which is quite similar to what is found. What is not clear to me is whether this is a problem in calculating the convolution of three DMEs or the assumptions in applying the convolution to get an expected level of expression. I think there must be clarity and agreement on what the expectation of low + high should be from the cis and trans library.

The 150 single mutants show similar patterns to what I would expect based on an additive model.

71/150 deviate from additive expectation. However, F2-2 shows that most single mutants have no effect (i.e. low expression). Why then do most of the observed doubles have an effect in the range of 1-3 when their effect should be zero? These observations are at odds with one another.

If the argument that high (trans) + low (cis) should be high expression because the repressor doesn't work, then this is exactly what one would expect if you include epistasis as a consequence of the way the regulatory system works and so is not really insightful. While this is a fine assumption to make later (non-naive), the simplest naive expectation needs to be understandable before making things more complicated.

Why didn't the positional information predict those that affect expression? One would expect that changes in binding sites for RNAP or CI would have quite different effects on expression.
