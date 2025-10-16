# Peer review - Round 1

Editors:
- George H Perry, Pennsylvania State University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.64669.sa1](https://doi.org/10.7554/eLife.64669.sa1)

In the interests of transparency, eLife publishes the most substantive revision requests and the accompanying author responses.

Acceptance summary:

This paper describes a novel approach for detecting adaptive introgression using a deep neural network. The authors demonstrate that their method can accurately detect adaptive introgression under a number of scenarios, and they apply the method to find loci where modern humans may have received beneficial alleles from Neandertals and Denisovans. This application of a convolutional neural network to detect events of adaptive introgression represents an excellent contribution to the field of population and evolutionary genomics.

Decision letter after peer review:

Thank you for submitting your article "Detecting adaptive introgression in human evolution using convolutional neural networks" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by George Perry as the Senior Editor and Reviewing Editor. The following individual involved in review of your submission has agreed to reveal their identity: Diego Ortega Del Vecchyo (Reviewer #2).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

We would like to draw your attention to changes in our revision policy that we have made in response to COVID-19 (https://elifesciences.org/articles/57162). Specifically, we are asking editors to accept without delay manuscripts, like yours, that they judge can stand as eLife papers without additional data, even if they feel that they would make the manuscript stronger. Thus the revisions requested below only address clarity and presentation.

Summary:

This paper describes a novel approach for detecting adaptive introgression using a deep neural network. The authors demonstrate that their method can accurately detect adaptive introgression under a number of scenarios, and they apply the method to find loci where moderns humans may have received beneficial alleles from Neanderthals and Denisovans. This application of a convolutional neural network to detect events of adaptive introgression represents an excellent contribution to the field of population and evolutionary genomics.

Essential revisions:

I highlight three points of essential revision, and then include the full reviews below which contain additional context on these points as well as a number of other excellent suggestions for your consideration as you revise your paper.

1) Model misidentification. You should test a few more scenarios in which there is demographic model misspecification. For example, you assume that the Yoruba are an 'unadmixed sister population'. Yet recent papers have pointed out that this assumption is potentially incorrect on timescales relevant for your analysis. How does your method perform despite such potential model misidentification? See the individual reviews for several other specific scenarios that would also be ideal examples to test.

2) Comparison with previous methods. The reviewers point out several previous methods to detect adaptive introgression. Please perform a direct comparison of results obtained between your and the previously available approaches.

3) Select a method other than guided propagation for the saliency map, and then evaluate the data along the lines of the detailed suggestions provided by reviewer 3.

Reviewer #1:

This manuscript, "Detecting adaptive introgression in human evolution using convolutional neural networks" by Gower et al., proposes a novel approach toward detecting adaptive introgression using a deep neural network. The paper is well written, the authors have taken care to ensure reproducibility and code availability. This method joins a rapidly growing group of deep learning tools for population genetic analysis, and the growing body of evidence that these methods represent an important step forward for the field.

1) I do think that it is essential that the authors compare the power of their method to some existing methods. I know that not all approaches use the exact same information as genomatnn, but I do think that the authors could easily compare power to some of the statistics from Racimo et al., 2017 MBE paper. This would at least offer some context to help readers gauge the level of advance offered by this method.

2) As the authors point out, their accuracy can go down substantially in the case of model misspecification. But they have only examined one scenario--training on Model A and applying to Model B--and this might be unrealistically pessimistic. It would therefore be helpful to see what happens for more modest amounts of misspecification. For example, the authors could sample a few different areas of the parameter space between Model A and Model B and see what happens when the model gets more and more mis-specified. This would give the reader a better feel for how good a demographic model estimate needs to be to use the genomeatnn method in practice.

Reviewer #2:

The authors have developed a new method to detect adaptive introgression events using convolutional neural networks (CNN). To use the CNN's, the authors create a training set consisting of 100 kb region simulations where three different scenarios could take place: an adaptive introgression event, a de novo mutation undergoing a sweep without introgression and a scenario without advantageous mutations. The authors use these simulations to train their CNN's to be able to differentiate between an adaptive introgression event happening in the 100 kb region from the latter two scenarios. The methodology presented by the authors includes innovations in the form of codifying the data to run the CNN´s and the CNN architecture used to solve this problem. The authors show that their methodology is able to perform very accurate classifications of regions undergoing adaptive introgression events in realistic human demographic scenarios. Finally, the authors show an application of their method to identify regions undergoing adaptive introgression events from Neanderthals to Europeans, and from Denisovans to Melanesians.

Convolutional neural networks have been recently applied to efficiently solve a variety of problems in population genetics. The application presented by the authors to detect events of adaptive introgression is an excellent and necessary contribution to the field. The manuscript is very well written, and the methods are clearly explained. The method is very robust and I can see that it will be applied to other species as genomic data becomes available. I only have a few minor comments about this manuscript.

The authors assume that YRI is an 'unadmixed sister population'. However, African populations also had introgression with another archaic ghost population (as reported by Ragsdale and Gravel (2019) PLoS Genetics; Durvasula and Sankararaman (2020), Science Advances). Would this have an impact on the detection of introgressed segments from Neanderthals to Europeans or Denisova to Melanesian populations using the method developed by the authors?

Reviewer #3:

The authors present in this work a new method based on convolutional neural network to infer adaptive introgression in human population. They trained their network on two types of scenarios with different demographic models. They show that the method works well.

The authors propose interesting features for their network which I think will be of interest of the population genomic and deep learning community.

They also advertise their method as being one of the few to do adaptive introgression inference.

The method is constrained by a demographic model.

The network takes as input a genotype matrix, with sorted and ordered individuals, and m bins in a window of 100kb.

The network is trained as a classification task to say whether the window of interest corresponds to adaptive introgression or not. The output of the sigmoid function (last layer of the CNN), is then used as the probability of AI in the given window.

This probability is then calibrated to take into account the fact that on real world dataset, the categories used in the training phase will likely not match the relative frequency of 100kb region under neutrality, selective sweep or AI.

Finally, the authors applies their method on real dataset and propose new gene as candidate for archaic adaptive introgression.

1. The authors suggest that few methods exist for this task, however, I believe this would be of interest to know how existing methods perform (such as the one from Setter et al., 2020) compared to genomatnn, if possible.

2. The results are good (>95% recall, Figure 2) for scenarios with high selection coefficient and/or early time of onset. The same as Figure 2B but with the precision in addition to recall might be interesting to know whether good precision is found in the same space or in another one (e.g. low selection coeff and late time of onset). Besides, the results seem quite affected by the coefficient of selection, time of onset, and also time of gene flow. Again, having a comparison with other method might help to assess whether the results presented here are good or not, in terms of method. Could this be calibrated as well, or given more weight in the training to improve accuracy for low selection coefficient for instance?

3. Authors do not use a test set. How can we be sure that the author did not "overfit" (unconsciously) the validation dataset after trying different hyperparameters? Showing result on a test set is better practice.

4. The attention analysis should be improved. First, guided backpropagation has been shown to not pass sanity check (Adebayo et al., "Sanity check for saliency maps", NIPS, 2018). It was shown that guided backpropagation highlight pixels that are independent of both the data used for training and the model parameters, and this method should not be used for explanation and interpretation tasks. In this paper, guided backpropagation appears to work merely as an edge detector. I wonder whether this is what is captured by the vertical lines we see in the saliency map that would correspond to clusters made by the rearrangement of the individuals. So I would highly recommend the author to choose another method for the saliency map (that passes sanity check). With the new saliency maps, if there is a signal localized along the SNP dimension, it would be interesting to know whether this actually due to the fact that the beneficial mutation was in the middle of the window, or caused by some other artifact. To do so, the authors could re-simulate scenarios that were easily well classed (e.g. with high selection coefficient and early time of onset), but with the mutation not in the middle.

5. I do no understand why the author propose to study the results with 2 cut-offs of 5 and 25% for the beneficial allele. Also only the 25% cut-off is discussed at the end. So why a cut-off in the first place? Then, why two? And finally, why showing and discussing the results only with 25%? For instance, table 1 and S2 have only 5 regions in common out of 25. How the reader should interpret that?

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Detecting adaptive introgression in human evolution using convolutional neural networks" for further consideration by eLife. Your revised article has been evaluated by George Perry (Senior Editor) and a Reviewing Editor.

All reviewers expressed appreciation for your hard work and thorough revisions. We have just two relatively small remaining requests before we can consider accepting your paper for publication in eLife:

1. You now state in the text: "We note, however, that, as with previous methods, visual inspection of the haplotypes or genotypes of the top candidate regions remains a necessary criterion to accurately assess whether a region may have been under adaptive introgression." We would also like for you to briefly discuss what to do with regions classified as AI are not among the "top candidates". These cases might be harder to validate by visual inspection. Do you think that these cases should be discarded? Or can you share any other insights on how to tell whether these AI regions could be legitimate, and whether users could use this tool to detect the impact of AI across the genome more broadly than just the "top candidates".

2. One previous reviewer comment concerned the absence of a test set (because having only a validation set might lead to overfitting hyperparameters to that set). In your response to reviewer comments you noted that you actually used different simulations and then simulate a new dataset while writing the paper. However, this clarification does not appear in the main text – please revise the manuscript to describe to the reader that the choice of hyperparameters was not made on the validation set mentioned, but instead during the "Preliminary analysis". Otherwise, the reader could think that the network might be biased.
