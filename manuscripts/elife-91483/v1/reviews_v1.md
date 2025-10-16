# Peer review - Round 1

Editors:
- Nicole Calakos, Duke University Medical Center United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.91483.3.sa0](https://doi.org/10.7554/eLife.91483.3.sa0)

The authors' dataset and analysis provide a fundamental new understanding of how cerebellar output contributes to various cerebellar-dependent diseases. The observation that different firing statistics at the level of the cerebellar nuclei directly impart disease-specific phenotypes is quite convincing. The classifier used in the article remains a potential weak point, showing limited efficacy, particularly for identifying mice with tremor. The concern about classifier accuracy is ameliorated by the fact that the classifier parameters are easily interpretable, and allowed the authors to use these parameters to design stimulation experiments.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.91483.3.sa1](https://doi.org/10.7554/eLife.91483.3.sa1)

Summary:

van der Heijden et al perform an ambitious analysis of single unit activity in the interposed nuclei of multiple mouse models of cerebellar dysfunction. Based on these recordings, they develop a classifier to predict the behavioral phenotype (ataxic, dystonic, or tremor) of each model, suggesting that highly regular spiking is associated with ataxia, irregular spiking is associated with dystonia, and rhythmic spiking is associated with tremor. Interestingly, the "dystonic" and "tremor" patterns appeared to be specific to those disorders, while ataxia could result from at least two different interposed nucleus firing patterns. After developing this classifier, they show that activating Purkinje neurons in different patterns that evoke interposed nuclear activity similar to their "ataxic", "dystonic", and "tremor" firing patterns induce similar behaviors in healthy mice. These results show convincingly that specific patterns of cerebellar output are sufficient to cause specific movement abnormalities. The extent to which cerebellar nuclear firing patterns are solely responsible for phenotypes in human disease remains to be established, however.

Strengths:

Major strengths are the recordings across multiple phenotypic models including genetic and pharmacologic manipulations, and the robust phenotypes elicited by Purkinje neuron stimulation.

Weaknesses:

The number of units recorded was small for each model (on the order of 20), limiting conclusions that can be drawn from the recording/classifier experiments.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.91483.3.sa2](https://doi.org/10.7554/eLife.91483.3.sa2)

Cerebellar diseases can manifest as various behavioral phenotypes, such as ataxia, dystonia, and tremor. In this study, van der Heijden and colleagues aim to understand whether these differing behavioral phenotypes are associated with disease-specific changes in the firing patterns of cerebellar output neurons in the cerebellar nuclei (CN). The authors effectively demonstrate that across different mouse models of cerebellar disease, there are distinct changes in the firing properties of CN neurons. They take a crucial step further by attempting to replicate disease-specific firing patterns in the cerebellar output neurons of healthy (control) mice using optogenetics. When Purkinje cells are stimulated in a manner that results in similar firing properties in CN neurons, the authors observe a variety of atypical behavioral responses, many of which align with the behavioral phenotypes observed in mouse models of the respective diseases.

Overall, the primary results are quite convincing. Specifically, they show that (1) different mouse models of cerebellar disease exhibit different statistics of firing in CN neurons, and (2) driving CN neurons in a time-varying manner that mimics the statistics measured in disease models results in behavioral phenomena reminiscent of the disease states. These findings suggest that aberrant activity in the CN can originate from various sources (e.g., developmental circuit deficits, abnormal plasticity, insult), but ultimately, these changes are funneled through the CN neurons, whose firing rates are affected, and this, in turn, drives some portion of the aberrant behavior. This is a noteworthy observation that underscores the potential of targeting these output neurons in the treatment of cerebellar disease. Moreover, this manuscript provides valuable insights into the firing patterns associated with the most common cerebellar-dependent disease phenotypes.

However, the applicability of the classifier for identifying mice cerebellar behavioral phenotypes directly from the spiking activity of neurons in the cerebellar nuclei remains this paper's weak point. Cross-validated performance of the model on a single mouse model of tremor is, for instance, only 54%. However, a benefit of this classifier is its overall simplicity; only three parameters are required to achieve average classifier performance of 76%. While more sophisticated models might provide improved classifier performance and enhanced generalization, such models would suffer from a lack of interpretability. This paper, therefore, represents a reasonable starting point for understanding the parameter space of cerebellar nuclei firing and its relationship to behavioral phenotypes during disease.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.91483.3.sa3](https://doi.org/10.7554/eLife.91483.3.sa3)

Summary:

This manuscript looks at the single-cell spike signatures taken from in vivo cerebellar nuclear neurons from awake mice suffering from 3 distinct diseases and uses a sophisticated classifier model to predict disease based on a number of different parameters about the spiking patterns, rather than just one or two. Single read-outs of spike firing patterns did not show significant differences between all 4 groups meaning that you need to analyze multiple parameters of the spike trains to get this information. The results are really satisfying and intriguing, with some diseases separating very well, and others having more overlap. It also represents a significant advancement for the rigor and creativity used for analyzing cerebellar output spike patterns. I really like this paper, it's a clever idea and has been done very well.

The authors examine multiple distinct forms of different diseases, including different types of ataxia, dystonia, and tremor. While some of the interpretation of this work remains unclear to this reviewer (in particular Fig. 2, with ataxia models), I applaud the rigor, and sharing complex data that is not always straightforward to understand.

Strengths:

The work is technically impressive and the analysis pushes the envelope of how cerebellar dysfunction is classified, which makes it an important paper for the field.

It's well written. The approach it is taking is clever. The analysis is thorough, and the authors examine a wide array of different disease models, which is time-consuming, costly, and very challenging to do. It's a very strong manuscript.
