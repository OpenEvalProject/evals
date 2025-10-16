# Peer review - Round 1

Editors:
- Marcel van Gerven, Radboud Universiteit Netherlands

Reviewers:
- Marius V Peelen, Radboud University Netherlands

## Review text

DOI: [10.7554/eLife.38105.029](https://doi.org/10.7554/eLife.38105.029)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "How biological attention mechanisms improve task performance in a large-scale visual system model" for consideration by eLife. Your article has been reviewed by three peer reviewers, including Marcel van Gerven as the Reviewing Editor, and the evaluation has been overseen by Sabine Kastner as the Senior Editor. The following individual involved in review of your submission has agreed to reveal his identity: Marius Peelen (Reviewer #1).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

The authors present an approach to examining the feature similarity model of attention by incorporating attentional modulation in a convolutional neural network for object categorization. They find that task performance enhancements with attention can roughly approximate those found experimentally, but most interestingly, only when attention is applied to the later layers of the network. The authors demonstrate a dissociation between layers in the strength of tuning and the performance enhancement achieved by applying attention. This represents an interesting contribution to theories of attention to the extent that one considers CNNs a useful model for biological vision. Another key contribution is the distinction between gradient-based and tuning-based feedback. The findings obtained here in neural networks make several new predictions for biological experiments and raise fundamental questions about how tuning affects behavior.

Essential revisions:

Introduction, second paragraph: CNNs are introduced as great models of the ventral stream, but an increasing number of studies shows that the features used in these CNNs to classify objects are very different from those used by humans (e.g., Azulay and Weiss, 2018; Baker, Lu, Erlikhman, and Kelleman VSS 2018; Ullman et al., 2016). Some caution may be warranted.

In Figure 3 performance increase across layers is shown. This plot is created by using the best performing weighting parameter β. To dissociate the effect of β and of the attentional modulation f, please add a control condition in which f is set to one. The reasoning is that varying β alone and picking the best β may already induce performance changes.

In Figure 3 the results for modulating all layers are shown. It is felt that the conclusions drawn from these results are unsupported. Picking β at 1/10 of the optimal β for each layer does not constitute an optimal setting for modulating all layers. Also, modulations in early layers may negatively impact activity changes in later layers. Hence, the authors cannot exclude the possibility that modulation of all layers simultaneously could actually help. Results and interpretations of attention applied to all layers should therefore be removed from the paper.

In the subsection “Attention Strength and the Tradeoff between Increasing True and False Positives”, you compare the change in the magnitude of neural activation in the CNN to the changes in primate brains. It was not clear how to interpret these results. Can these magnitudes be meaningfully compared? What can we conclude from this?

In the subsection “Feature-based Attention Primarily Influences Criteria and Spatial Attention Primarily Influences Sensitivity”, it is argued that FBA works through a criterion shift rather than by increasing sensitivity, with FBA shifting the representation of all stimuli in the direction of the attended category. But earlier you show that FBA selectively increases TP (relative to FP), which suggests an increase in sensitivity. (Also, Figure 4E appears to show a positive effect of FBA (L13) on sensitivity). Please clarify.

For many of the analyses results of both types of feedback are shown. However, for some comparisons only tuning-based results are shown (e.g., see the aforementioned subsection). Why? Please ensure consistency throughout.

It is unclear why a new method for quantifying attention is introduced in Figure 7, or how the "FSGM-like" measure is related to feature matching and the activity ratios already discussed. Please motivate or restrict to feature matching and activity ratios. In general, the paper is a dense read due to the various analysis and metrics. Any steps towards simplification of the presentation will aid the reader.

The claim that the new measure of attention (Figure 7A), or the alternative measures of attention for that matter, is experimentally testable seems unsupported. In particular, getting with and without attention activity in response to images that are not classified as the target orientation is not possible to measure in experiments with humans or animals. Subjects are stochastic in their judgments. One could however, measure with and without attention responses to ambiguous stimuli that elicit near chance performance. This metric would then become very similar to a population version of the well-studied "choice probability" metric. This connection should at least be discussed.

It would be more useful to the experimental community to recast the orientation task and analysis more in terms of what would be measured empirically. For instance presenting the task in terms of correctly identified target orientation as a function of the presented orientations rotation from the target. This may be outside the scope of current manuscript though.

What would be the biological mechanism that can account for tuning-based and gradient-based feedback? Especially the gradient based approach seems to be hard to defend from a biological point of view. How would putative decision-related areas have access to this gradient information? Some words should be spent on this in the Discussion section.

Please mention relevant related work:

- Katz et al., 2016, related to the relationship between tuning and influence on decisions.

- Abdelhack and Kamitani, 2018, related to subsection “Recordings Show How Feature Similarity Gain Effects Propagate” (and Figure 7) showing that the activity in response to misclassified stimuli shifts towards the activity in response to correctly classified stimuli when attention is turned on.

- Stein and Peelen, 2015, related to the subsection “Feature-based Attention Primarily Influences Criteria and Spatial Attention Primarily Influences Sensitivity”, arguing that FBA in human experiments does not lead to an increase in sensitivity (see also work by Carrasco on effects of FBA on discrimination tasks).

- Discussion, fifth paragraph: Ni, Ray, and Maunsell, 2012, would appear to be very relevant to this Discussion section. Those authors found that strength of normalization was as strong a factor as tuning in the strength of attentional effects.

- The neural network community developed various models that implement some form of attention. See the Attention section in Hassabis et al., Neuron, 2017. The present work should be contrasted with the papers mentioned there.
