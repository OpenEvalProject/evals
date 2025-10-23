# Peer review - Round 1

Editors:
- Babak Momeni, https://ror.org/02n2fzt79 Boston College United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.83690.sa0](https://doi.org/10.7554/eLife.83690.sa0)

This manuscript uses genome-scale metabolic modeling to estimate interspecies interactions and subsequently assess engraftment outcomes. This is an important line of work with potentially broad applications in different fields, including microbiota studies. The authors provide solid evidence to support the usefulness of their proposed approach in engraftment studies.


---

# Peer review - Round 1

Editors:
- Babak Momeni, https://ror.org/02n2fzt79 Boston College United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.83690.sa1](https://doi.org/10.7554/eLife.83690.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Decision letter after peer review:

Thank you for submitting your article "Metabolic Model-based Ecological Modeling for Probiotic Design" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, including Babak Momeni as Reviewing Editor and Reviewer #1, and the evaluation has been overseen by a Reviewing Editor and Aleksandra Walczak as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Daniel Rios Garza (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) Please include the limitations of GSMMs, such as the requirement for high-quality reconstruction and the need to have resolved genomes or a method to assign models to taxa (Figure 1). Please also the assumption of the defined medium used for this manuscript.

2) Please add an investigation of the impact of the growth media on the predictions to the manuscript.

3) Please clarify the details of the setup for the results in Figures 3, 4, and 5. How is the training set chosen? How is the test set chosen? For testing each model, what are the conditions explored? What is the justification behind these choices?

4) Please clarify the importance of Figure 3. It appears all models, even the simplest ones, accurately predict the outcomes in this case. What is unique/different about this example that leads to this situation?

5) Please add explanations for why the performance in Figures 4 and 5 is rather poor. What is the reason behind the low predictive power? There is also a need for explaining why some models perform better than others. What are the conditions under which you expect each model to do well?

6) Please include the detailed assumptions of your FBA model, in particular, the effect of the resource allocation threshold. If a fixed threshold is used for research allocation, it may lead to artifacts. Please specify how this threshold affects the AUCs and if a more general approach such as parsimonious FBA would give similar results.

7) A justification is needed for why log ratios are used to represent interaction coefficients (Equation 2). When does such a representation work well? Does this work well, for example, in a simple case of a community with a few interacting species in dynamic FBA?

8) The authors need to justify how they chose the species to include in the analysis ("Creating induced sub-graphs"). If the availability of GSMMs is the only criterion, the authors need to add a thorough investigation of how sub-sampling the species present in the community might impact the prediction quality.

9) Please clarify how exactly the 400 cases used in each case are drawn (by clarifying and expanding the description in "approximate edge swapping").

10) Please revise the Discussion section to address the limitations of the approach.

Additionally, I strongly encourage you to address the comments from individual reviewers (listed in the following) in your revision.

Reviewer #1 (Recommendations for the authors):

The authors in this manuscript use different models to explore if engraftment success can be predicted based on metabolic interactions. They use genome-scale metabolic models to train six different population-level models. They then assess how well these models predict the invasion/engraftment outcomes when compared with existing experimental results. The basic concept behind the work is interesting, relevant, and timely. However, there are issues with the organization of the paper and the clarity of results which make the paper hard to evaluate. Additionally, there are several assumptions made in the paper (e.g. how the interactions are estimated or how instances of communities are built) that need to be better justified. A thorough discussion about the limitations of the approach is also necessary to clarify for the reader the situations in which this approach is likely (or unlikely) to work well.

1. It is unclear to me what the ensemble used for Figures 3 to 5 is. How is the training set chosen? How is the test set chosen? For testing each model, what are the conditions explored?

2. Is it fair to consider the results in Figure 3 as trivial? It appears all models, even the simplest ones, accurately predict the outcome. What is unique/different about this example that leads to this situation?

3. In contrast to Figure 3, the results in Figures 4 and 5 are far from ideal. What is causing this significant drop in predictive power? I would recommend that the authors include the discussions to at least speculate under what conditions the predictive power will drop.

4. In the organization of the paper, there is a strong emphasis on the six different types of model in the abstract and introduction, but the most informative data comes from the InhibitLV model. I felt the models that are not informative could perhaps be de-emphasized, in favor of models that produce the best predictions and offer more mechanistic investigations.

5. In my opinion, more details about how FBA is used to find the parameters of the model should be included in the main text.

6. The authors briefly mention that in some cases one or more models failed because of fitting issues. In my opinion, including the conditions that each model fails as well as a description of why it fails and how the situation can be remedied is necessary. This will be very informative for others to troubleshoot and fix similar issues in other contexts.

7. If I understand correctly, the authors use log ratios to represent interaction coefficients (Equation 2). In my opinion, the justification for this choice needs to be included in the manuscript. Does this work well, for example, in a simple case of a community with a few interacting species in dynamic FBA?

8. It appears to me that in choosing what species to include in the analysis ("Creating induced sub-graphs"), species to include are chosen based on whether there is a match for them in the AGORA database, rather than how important they are for the process of engraftment. The potential downside of this choice for accurately representing each system can be large (for example, it may miss the dominant species as an obvious example). The authors need to include a justification of why this choice is justified.

9. I would like to ask for some clarification on how exactly the 400 cases used in each case are drawn. The procedure is described in lines 423-432 ("approximate edge swapping"), but I think expanding the description (maybe using a simplified visual illustration of the protocol with 4 or 5 species) would be helpful.

10. The Discussion section of the paper summarizes the advantages of the proposed method (using genome-scale metabolic modeling to make inferences about engraftment outcomes) but does not adequately discuss the limitations of the approach. In my opinion, this is one of the major weaknesses of the paper.

Reviewer #2 (Recommendations for the authors):

The study presents a promising framework to predict the outcome of colonization experiments, such as the ones that are attempted in probiotic therapy. Previous studies have tackled this problem with both machine learning approaches (ML) and ecological models (based on interspecies interactions) but encountered some major limitations. The ML approaches are context-specific and require a large amount of training data per condition to have predictive power, while the ecologic models require dense time series to reliably find the interspecies interaction parameters.

The authors propose to solve these limitations by making use of reconstructed genome-scale metabolic models (GSMMs) to predict the strength and direction of species interactions. The main advantage of such an approach is the possibility to fit ecological models to individual samples, without the need for extensive training data or dense time series. But does this approach work?

To test its strength, the authors predicted the outcome of three colonization experiments and show that the ecological models parameterized with GSMMs outperform ML methods such as random forest and support vector machines.

While the approach is certainly promising, some careful validations might still be useful before it can be widely used.

Even if the framework seemingly outperforms the tested ML methods, the predictive values are relatively low and might depend on details of the approach that were not systematically evaluated. High-quality GSMMs are not widely available. Automated and semi-automated reconstructions such as the ones in AGORA contain many errors and might not provide the correct information about species growth and interactions. The study partially tackles this limitation by showing that predictions using the interactions of a null model (i.e. random interactions) are significantly worse than predictions based on the GSMM interactions.

Of notice, the framework uses a modified version of community FBA which is not accessible in a publicly available tool and relies on the arbitrary definition of a flux threshold. Furthermore, the use of GSMMs requires the formulation of the growth media. Here an artificial formulation (termed the Western diet) was used. It is unclear how much these choices affect the prediction quality and prevent the framework from being widely used.

How about the ecological models? The authors extensively tested six alternatives divided into two classes: generalized Lotka-Volterra-based models (GLVs) and linear models. Overall, the GLVs outperformed the linear models. Finally, if the approach can be used and makes reliable predictions, then one can perform perturbations to the structure of the model and gain further insights into the ecology of a species' colonization into a community.

In my opinion, the following additional validations would significantly increase the impact of the study and strengthen its conclusions:

– Growth media: the manuscript would benefit by showing how much the growth media affects the quality of the predictions;

– Resource allocation threshold: It's not specified in the methods, but based on the previous study, I assume that a threshold was fixed, which sounds fairly artificial. It would be useful to know how this threshold affects the AUCs and if a more general approach such as parsimonious FBA would give similar results.

– Induced sub-graphs: what is the consequence of working with only a fraction of the microbiome given the impossibility to map it to a GSMM? For instance, how does down-sampling the community composition impact the prediction quality?

With these comparisons in hand, one could understand better why the AUCs are so low and what is expected to get reliable predictions.

Figure 1: could make clear some of the limitations of GSMMs, such as the requirement of high-quality reconstruction and the need to have resolved genomes or a method to assign models to taxa. Also, the assumption of a defined medium.

Figure 3: why is the null model not centered at 0.5?

Reviewer #3 (Recommendations for the authors):

Recent years have shown that despite the strong link between the microbiome and health, the administration of a probiotic is not sufficient to alter the microbiome in a desired, therapeutic, way. Engraftment of the administered microbial species is often limited, with most patients failing to show signs of medium-term or long-term engraftment. This study uses pairwise metabolic modeling to build a network of species-species interactions. Considering three experimental engraftment studies, they assess the likelihood of invader engraftment based on network structure, comparing model predictions to data. Comparing several related models, it is shown that a generalized Lotka-Volterra model is predictive if an invader or probiotic will successfully engraft into an existing microbiota community, potentially revealing which microbe-microbe interactions drive the engraftment. A known weakness of generalized Lotka-Volterra models is the difficulty to parametrize them from experimental data, and the lack of generalizability of the resulting model to new situations. Here, by leveraging metabolic modeling (relying on the AGORA network) the authors claim to parameterize population models in a way that is predictive also of novel environments. Thus, the authors claim to predict the engraftment of an invader into a microbial community.

Strengths:

– The question of engraftment is important, and the attempt to tackle it by trying several related models and AGORA is justified and may yet prove fruitful.

– Figure 2 explained the six models well, clarifying the differences and similarities between them.

– The code shared on github is good practice. Yet one may improve the code release significantly, e.g.: a readme file, a quick explanation of how to use the code, etc. In its current form, it is not so usable by a third party.

Weaknesses:

– The message in Figure 1 is lost on me. The two panels appear quite similar, and I do not understand what the difference between them is supposed to mean.

– I do not agree that the ecological principle of engraftment is the same between pathogens and probiotics. The pathogen cares only about short-term engraftment as a means to grow and infect further hosts (hence its pathogenic nature, ultimately damaging the host), therefore, the notion of long-term engraftment is ill-defined. Indeed, pathogens may employ strategies to assist in short-term engraftment (e.g. cause the host diarrhea), that probiotics cannot. Probiotics (or commensal species in general) are presumed to form stable long-term associations with the host without damaging the host.

– I found the exposition of the methods and results lacking. For a start: how precisely is AGORA used? Why do the authors presume the readers are familiar with AGORA? Equation 1 is not properly explained. The Results section shows mostly trivial information instead of a deeper understanding of the modeling results.

– It is not at all obvious that given the FBA data for a single microbe, one can predict its growth paired with another species. Processes of adaptation and evolution kick in and can change the single-microbe growth profiles significantly. This weakens the foundation of this entire approach. There is much recent literature on this co-culture question (some of it cited in the manuscript) and it simply cannot be brushed off so casually.

Justification of claims and conclusions:

The manuscript raises an important question and proposes a solid direction, but I am not convinced by the evidence presented-possibly due to the presentation itself. Though the approach proposed in this manuscript may yet prove useful, it needs much more justification, proper exposition, and experimental validation to be taken truly seriously.

– Abstract (line 20) "reflect connect" should probably be just "connect".

– While I think there is no need to explain the AUROC, I do think that the Kendall-tau correlation should be better motivated, as it is not often used in the microbiome literature.

– The AGORA database should be better exposed. The authors should not assume the reader is familiar with it.

– I do not understand why it is useful to show Figure 3a – a bunch of 100% AUROC values (as a bar plot!). The fact that it is easy to predict C.diff. engraftment is stated in the text and the figure frankly just looks a bit silly. Indeed, Figure 3b is even less informative, we know what a 100% AUROC looks like, and it needs no visual assistance. Though Figure 3c contains something for us to learn, it is a weak statement about the role of shuffling the AGORA parameters. Altogether – I would say remove 3a and 3b altogether and change 3c or put it in a supplement.

– Regarding Figure 4a: the use of bar plots is discouraged, using box plots would be a lot more informative in the same presentation style and space. 4b: why is the AUROC not stated? The classifier seems hardly impressive.
