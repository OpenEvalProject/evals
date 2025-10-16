# Peer review - Round 1

Editors:
- Vaughn S Cooper, University of Pittsburgh United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.60067.sa1](https://doi.org/10.7554/eLife.60067.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

x

Acceptance summary:

This is a monumental effort to compare methods of predicting the evolution of the influenza A virus, the cause of seasonal flu, which is of critical importance for vaccine design. The study uses open-source models that integrate multiple types of genetic and phenotypic data about the virus and helps us understand why these models succeed or fail. A key discovery is that viral titers combined with sequence-based mutational load provide the best predictive power. Overall, the study highlights the sobering complexity of predicting H3 evolution in a variable and changing human immune landscape and the need for multiple strategies and forms of data integration to improve composite models going forward. This is interesting work for anyone interested in predicting evolution.

Decision letter after peer review:

Thank you for submitting your article "Integrating genotypes and phenotypes improves long-term forecasts of seasonal influenza A/H3N2 evolution" for consideration by eLife. Your article has been reviewed by two peer reviewers, and the evaluation has been overseen by a Reviewing Editor and George Perry as the Senior Editor. The reviewers have opted to remain anonymous.

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below address clarity and presentation and would strengthen an already promising manuscript.

Summary:

This is a monumental effort to compare methods of predicting H3 evolution. The study demonstrates the value of composite, open-source models that integrate multiple types of genetic and phenotypic data. And it is particularly valuable for understanding the context under which different models and types of data perform better. Interestingly they find that HI titers combined with sequence-based mutational load provide the best predictive power. Along the way, the study also uncovers insights about the forces behind influenza evolution that are interesting in their own right. The exploration into why previously identified epitopes fail to predict modern patterns of evolution explains why HI is a better predictor. But it also highlights the flexibility of HA antigenicity and the volatility of the human immune landscape. Overall, the study highlights the sobering complexity of predicting H3 evolution in a variable and changing human immune landscape and the need for multiple strategies and forms of data integration to improve composite models going forward. This is interesting work for anyone interested in predicting evolution.

Essential revisions:

1) It would be helpful to further explore model performance in different contexts.

a) Overall, do the models perform any better or worse at predicting Northern v Southern hemisphere viruses populations?

b) I'm surprised the authors don't discuss more the recent problem of multiple H3 cocirculating clades (observed in Figure 9). Predicting H3 evolution has always been difficult, but at least there was generally a linear tree and a single dominant H3 clade at any given time. Did certain models better predict the emergence and persistence of this tree pattern? Do they offer insights?

2) Given that this study tackles a very real world problem (selecting strains for influenza vaccines), it would be helpful to have these results better translated for readers with public health backgrounds.

a) A simple addition would be an opening table/chart that describes the different models and categorizes them (lab data, sequence-based, tree-based etc.)

b) Figure 8 nicely visualizes model performance against actual vaccine strains. But can you quantify/summarize the results in this figure better (i.e., exactly how much 'closer' to the future than the vaccine strain?). Perhaps also including additional models in those measures?

c) In the Introduction can you provide more context for this study? What is the current range of influenza vaccine effectiveness? How frequent are H3 mismatches? And how well have we been trending at matching H3 vaccine strains to H3s in circulation? Are we making any discernible progress? Or have improvements in modeling been offset by the H3 cocirculating clades problem?

d) A key message from this study is how challenging prediction H3 is, even with new analysis tools and new types of experimental data. We have so much further to go. It's worth highlighting in the Discussion how CDC FluSight has collectively advanced epi flu forecasting by making weighted ensembles drawn from multiple modeling groups and how valuable a similar program would be for vaccine strain selection.

3) Some epitopes are more important than others. Did you consider weighting epitopes differently? Or would that just exacerbate overfitting? And how do you handle glycosylations in the model?
