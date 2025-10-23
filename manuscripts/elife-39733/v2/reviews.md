# Peer review - Round 1

Editors:
- Wenying Shou, Fred Hutchinson Cancer Research Center United States

Reviewers:
- Wenying Shou, Fred Hutchinson Cancer Research Center United States
- Christopher Quince, University of Warwick United Kingdom

## Review text

DOI: [10.7554/eLife.39733.030](https://doi.org/10.7554/eLife.39733.030)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

[Editors’ note: the authors were asked to provide a plan for revisions before the editors issued a final decision. What follows is the editors’ letter requesting such plan.]

Thank you for sending your article entitled "Quantifying biosynthetic network robustness across the human oral microbiome" for peer review at eLife. Your article is being evaluated by three peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation is being overseen by a Reviewing Editor and Naama Barkai as the Senior Editor.

Given the list of essential revisions, including new experiments, the editors and reviewers invite you to respond with an action plan and timetable for the completion of the additional work. We plan to share your responses with the reviewers and then issue a binding recommendation.

The most important issue you will need to address is the biological relevance of the proposed method. You can either show that the method is in agreement with previously published data (where a lot of direct evidence exist) in a manner that is better/more insightful than previous methods; or provide new experimental data to substantiate your claims.

Reviewer #1:

"Quantifying biosynthetic network robustness across the human oral microbiome" from Segre lab was motivated by a desire to overcome the gap-filling limitation of standard flux balance analysis and the need to make assumptions on environments in metabolic network topology analysis. They quantified "biosynthetic network robustness", essentially how the probability of a product being made (Pout) scales with the probability of the presence of input metabolites (Pin). This robustness can be summarized as PM – the higher PM, the more likely a metabolite can be synthesized. If one is worried about parameter overfitting (and one should worry about such problems in genome scale models), this seems like a good thing to try. Applying the metric PM to E. coli central metabolism, they found that PM is not correlated with connectivity. Some metabolites have high connectivity but low PM, and some low connectivity and high PM. They then quantified PM of 88 biomass metabolites for 456 oral microbes, and found that fastidious (difficult to culture) microbes have low PM values for several metabolites, consistent with them being fastidious. Genome size and taxonomy both contained information about PM. They found that cell wall metabolites have variable PM. They also found that a number of amino acids have high PM in Proteobacteria and low PM in Bacteroidetes. They also analyzed metabolic complementarity of several TM7 strains (fastidious microbes) and their symbiotic bacteria strains. The paper is of bioinformatics nature, and is in general clearly written.

1) What is the difference between PM and% completion of biosynthetic pathway?

2) It's also not entirely clear to what extent their method improves upon the state of the art. In their Introduction, they say that two downsides that limit FBA (but not their method) are assumptions on environmental conditions and reconciling with stoichiometry-based constraints. I don't really understand their second limitation, but they sidestep the first limitation by assuming a constant Pin among all inputs. This seems similar to assuming constant concentration among all inputs for FBA, which is never shown.

Reviewer #2:

The manuscript by Bernstein et al. presents a computational method to estimate metabolites that are likely to be exchanged in a microbial community. The essence of the novelty of the method, especially in comparison with the previous methods, is that it provides a probabilistic view accounting for multiple possible variations in substrate uptake combinations (e.g. different combinations of C/N sources etc.). The method is illustrated with the analysis of oral microbial community and the results suggest potential metabolic dependencies in the community. I find the method to be elegant but yet only of theoretical interest.

1) The method assumes a uniform distribution of possible substrate uptake combinations – which is not necessarily biologically observed. There are hierarchies – e.g. preference of glucose over other C-sources in most organisms.

2) The finding that metabolic dependencies may exist in oral microbiome is not that surprising per se given that a large body of literature (including papers also from the Segre lab) already suggest that metabolic dependencies are likely widespread in microbial communities. Thus, it is not clear whether only the proposed method would be able to identify these.

3) Lack of experimental validation makes it difficult to assess whether the identified exchanges are happening in the system. At the least, a detailed analysis of systems with known metabolite exchanges (and how the proposed method there differs from the previous ones) should be provided.

In summary, I do find the proposed method elegant and appealing but miss substantiation of the biological relevance.

Reviewer #3:

This manuscript introduces a new robustness metric that attempts to quantify the probability that an organism can produce a given metabolite directly from the genome. This probability is calculated as an average over possible environments defined by the presence or absence of the other metabolites in the network with production determined through the application of an FBA model. I found the metric itself intuitively appealing and easy to understand. In addition, the manuscript was clear and well written. The application to the oral microbiome and the novel CPR organisms in particular was also well motivated and interesting.

Given the rate of generation of microbial genomes it would be very useful to have a better method to even approximately predict metabolic products of organisms. However, what the study lacks in my opinion, is quantitative evidence that the metric actually does translate into a prediction that the organism produces a given metabolite. They provide some anecdotal examples where it appears to work but without a more thorough analysis of what the metric means then it will only be useful in a qualitative sense i.e. a higher PM indicating that one organism is more likely to produce a metabolite than another. Metabolic modelling is admittedly not my field, but datasets capable of testing the metric, must exist. A possible example might be this collection of E. coli strains and phenotypes defined in terms of growth conditions (Galardini et al., 2017, eLife). If such datasets are not available then I feel the authors need to be more circumspect in their conclusions and concede that the metric may say something about the production of metabolites but without any certainty about how a given PM value translates into an actual probability of production.

Other than the above caveat, I thought this was a good study but it was sparse on the practical details of the methodology. The GitHub repository consists of a selection of Matlab scripts without a clear description of how to apply them. What would be really useful is a complete walkthrough of the methodology from genome to PM values including for example ggkbase commands used to build the models. This is necessary if this work is to be properly reproducible. One final comment was that some evaluation of the impact of sample number on the calculated PM values would be a worthwhile addition. The authors mention that 50 samples of input metabolite combinations were used but no analysis of the impact of this choice on the PM values was given.

[Editors’ note: formal revisions were requested, following approval of the authors’ plan of action.]

Thank you for submitting a revision plan for your article entitled "Quantifying biosynthetic network robustness across the human oral microbiome". The editors and reviewers have considered your plan and invite you to proceed with your revisions. Please also consider the following comments when preparing your revised manuscript.

The Reviewing Editor stated:

"I think that I know how authors can fix their problems from a theoretical aspect. They can start with a complete model as the "ground truth" model, but hide or mis-annotate various% links to mimic our incomplete knowledge of the system, and compare their method with existing methods. This way, they will always have a "ground truth" curve for any metric of interest to biologists. Of course, the task of assigning missing links will need to be repeated many times and in double-blind fashion to gain statistical power. I suspect that different methods might show tradeoff. For example, in their Figure 1, it is not clear whether the extra info provided by PM is useful to a biologist if all mutants are auxotrophic. Any tradeoff between methods is also valuable to know. Authors can also use this ground truth model to illustrate problems of gap filling etc."

Another reviewer said:

"I agree this is a very comprehensive plan and they do seem to have taken our comments to heart and developed a proposal to address them. I was pleased with their suggestions regarding an alternate dataset of E. coli phenotypes to test their metric and the improved GitHub repository. "

The last reviewer said:

"I agree that the proposal is comprehensive and I like the Reviewing Editor's simulation idea. This also reminds me that the authors' should comment on the ensembleFBA approach which does address the main criticisms of the gap-filling. Furthermore, I think that a clear focus on oral microbiome would benefit the study much more rather than claiming general validity that is very difficult to substantiate based on their proposed plan – after all, E. coli is one organism and by no means representative of natural diversity and community complexity. E. coli auxotroph complementation experiments are also unique in some sense as I haven't seen many other studies showing similar data in other organisms. So, overall, I think recommending to focus on oral microbiome and reducing the general claims would put the paper on more solid foundation I believe."
