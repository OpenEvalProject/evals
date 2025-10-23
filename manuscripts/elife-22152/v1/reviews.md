# Peer review - Round 1

Editors:
- Frances K Skinner, University Health Network , Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.22152.022](https://doi.org/10.7554/eLife.22152.022)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "ICGenealogy: Mapping the function of neuronal ion channels in model and experiment" for consideration by eLife. Your article has been favorably evaluated by Eve Marder (Senior Editor) and three reviewers, one of whom, Frances Skinner, is a member of our Board of Reviewing Editors. The following individuals involved in review of your submission have agreed to reveal their identity: Timothy O'Leary (Reviewer #2); Farzan Nadim (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary of the work

For many years the physiological community has quantified ion channel kinetics for the purpose of building models, and for understanding the biological importance of the diversity of ion channels expressed in neurons and other cells. However, until now, there has not been a useable and comprehensive resource for documenting, organising and comparing ion channel models. The current manuscript offers a new, comprehensive resource for channel models, ICGenealogy, as well as analysis tools for comparing channel models.

ICGenealogy allows access to a large pool of already publicly available information regarding channel models (i.e., ion channel models in NEURON software as deposited into ModelDB), and classifies them through a genealogy method. It uses a standard, if somewhat ad hoc, set of protocols to classify the currents and uses PCA and a metric to classify them and explore their "distance" to build clusters. It facilitates the viewing of model channel development metadata as well as allows standardized comparisons of ion channel models. This would otherwise be time-consuming and inefficient for individual modellers to do on a per model basis. It thus offers much needed standardization to the field of model development.

Further, and most importantly, ICGenealogy facilitates model comparisons with experimental data so that more informed decisions can be made when using particular channel types in a model.

In summary, ICGenealogy provides diligence for ion channel modeling and should serve as a most helpful tool to bring model and experiment together in terms of perspectives and transparency of assumptions and rationales. Overall, all reviewers agreed that ICGenealogy is a useful and important contribution to the field.

Essential revisions:

1) Biological variability:

The issue of biological variability is touched on (subsection “Ion channel model groups defined by common metadata show variability in behavior”, first paragraph), but more should be said about this. At present, it is discussed too passively.

Even a single ion channel gene has multiple splice variants, subunit combinations, and possibilities for postranslational modification. Computationally-minded readers can fail to appreciate this and write-off the biological variation as noise or experimental incompetence. This is exacerbated by the subsequent assertions:

"A large portion of the variability may also stem from model fitting and idiosyncratic changes to individual model implementations. Consistent with this notion, we find that models defined by common families can occasionally fall into different clusters (Figure 4A). This suggests that experimental data used to fit models can be treated in different ways, perhaps combined with other data, and may lead to disparate models."

Actually, if you experimentally isolate a current pharmacologically, or even go to the trouble of cloning a channel gene to express it heterologously, you may still see measurable differences in kinetics within an 'identified channel type', for the reasons above. It is thus important to state more clearly that this variability might be genuine, even if we find it a nuisance and don't fully understand its possible significance.

Further, ion channels can have tens of phosphorylation sites that could allow for activity or neuromodulation to change their activation/inactivation properties. For example, Misonou et al., "Regulation of ion channel localization and phosphorylation by neuronal activity." Nat Neurosci 2004.

2) Maintenance and usage of resource:

As with all resources of this kind, its usefulness depends on its continued maintenance. What plans do the authors have in mind to achieve this? This should be delineated in the manuscript in some way.

In other words, the authors should take steps to ensure the maintenance of this resource is self-sustaining. It is only useful insofar as the community continues to use, update and build on its features.

The authors have constructed the resource to allow upload of data, but what capacity is there for ongoing, community-based curation? For example, can existing models be queried and annotated, or cross-referenced to external resources (such as EBI, NCBI, Allen Brain Atlas…)? These features would contribute to the longevity and flexibility of the resource and prevent a fate common to other resources that fade over time. It would be useful for a clear path to these additions to be laid out (e.g. in API documentation), even if, as the authors emphasize, the actual implementation is beyond the scope of the study.

I really loved the comparison of the Drosophila K+ current with existing models. Would be to allow submission of such experimental data on ionic currents, recorded with the standardized protocol of ICG, to the site so that best-matching models and geneology could be identified. This would greatly increase the value of this resource.

3) Potentially confusing terminology:

To avoid confusion and ambiguity, it would be helpful if the author specifically say 'ion channel model' or 'neuronal/cell model' rather than just 'model' in various places throughout the paper (e.g., Introduction, end of first paragraph, and several subsequent places).

Throughout the manuscript the authors should be more careful to distinguish the sense in which 'genealogy' is used. There is clear scope for confusing 'model genealogy' (i.e. similarity in behaviour), 'publication genealogy' (i.e. where the model was first described and its subsequent uses and citations) and 'genetic genealogy' in the biological sense! I think the authors should define their terms carefully at the beginning of the manuscript and occasionally remind readers of the differences.
