# Peer review - Round 1

Editors:
- Fabrice Cordelières, CNRS , France

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.22323.019](https://doi.org/10.7554/eLife.22323.019)

In the interests of transparency, eLife includes the editorial decision letter and accompanying author responses. A lightly edited version of the letter sent to the authors after peer review is shown, indicating the most substantive concerns; minor comments are not usually included.

Thank you for submitting your article "Decoupling global biases and local interactions between cell biological variables" for consideration by eLife. Your article has been favorably evaluated by Naama Barkai (Senior Editor) and three reviewers, one of whom, Fabrice Cordelières (Reviewer #1) served as Reviewing Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Chong Zhang (Reviewer #2); Perrine Paul-Gilloteaux (Reviewer #3).

The reviewers have discussed the reviews with one another and the Reviewing Editor has drafted this decision to help you prepare a revised submission.

Summary:

Zaritsky et al. propose a new approach to characterise interactions between two variables as a result of two influences: a global effect, independent of the two variables and influencing both, and a local effect that depends on their "direct" dependency. This paper raises the point of differentiating situations where correlations are observed, not due to a direct link between variables, but rather being the result of an overall behaviour. The authors built a framework in which both effects are reflected by two indicators: global and local indexes (GI and LI). The paper is divided into a theoretical part, where simulations are used to setup the framework, and a series of 4 biological examples where the "DeBias" method is applied.

Essential revisions:

1) The authors have performed simulation in which the bin widths of distributions or the number of observations have been progressively increased. Conclusions seem to be that a 15 quantization bins and a number of samples around 100 is acceptable. However, how should these parameters be set depending on the nature of the data to analyse? How should these parameters be set, depending on the distributions to analyse? Is there a generic rule? If so, this should be explained. If not, why did the author make those choices? The Methods section includes information about the number of quantization bins: why is it 89 for angular data, where as the value is 10 for PKC experiments and 39 for co-localization? From theoretical results, it seems LI or GI tends to (K-1)/2 when the other indicator is zero, K being the number of quantization bins. How would the authors recommend proceeding when the K parameter is not the same from one experiment to another? I fear we are missing proper guidelines.

2) For example of lack of usability: I did test it also with my own data of spot colocalization (simulation) and interestingly the GIs were inversely related to the spot density (but which was also related to the image size or N), and LIs was less obvious (my N was 100^2 and 256^2 with 100 spots each time with no colocalisation or with 50% of them colocalizing). I’ve found

GI no coloc 50% coloc

(squareroot size) 100 4.47 4.32

(squareroot size)256 3.67 3.62

LI no coloc 50% coloc

(squareroot size)100 1.59 2.24

(squareroot size)256 1.69 1.57

Before any conclusion, interpretation would require more characterisation work, or maybe provided with a simulation script in order to better apprehend the significance of it. I would have had to repeat the experiment, too laborious from the server, and in addition I do not know which number of bins was used in that case and if it was constant.

3) In terms of local interaction ζ, it is simulated as a ratio of θ by α, is this a generic assumption that local interaction is a variable linearly related to the alignment?

4) Subsection “Simulating synthetic data”, the authors demonstrated in the simulation the effectiveness of GI and LI. While it seems true by simulating local interaction of alignment by shifting one of the angles towards the other, how would GI and LI behave when the local interaction is not alignment, i.e., by shifting one away from the other? Would GI and LI show the opposite effect so as to be able to discriminate opposite local interactions?

5) Subsection “DeBias procedure”, for the adjustment #1 for the colocalization quantification, such normalization implicitly assumes the channel signals/intensities have linear relationship. This could be a strong assumption. What would be the adjustment for those signals that do not have linear relationship?

6) Probably some additional validation to highlight the method's advantage over other conventional intensity based colocalization methods would be useful. Such additional evaluation is probably not necessarily within the scope of a "Tools" submission, but that if such data were available, it would be a valuable scientific addition to the paper. Or at least some kind of generic guidelines about under which situations when DeBias may or may not be applied would be instructive.

7) The quantification power is actually relative: in the same conditions (meaning here same K, and potentially same N see point 2), the GIs and LIs would actually give relative information, but a twofold interaction factor would not show a twofold LI. In addition each experiment shows very different range of LIs and GIs. These values are theoretically in the range of [0; (k-1)/2], k been the number of bins, and does not denotes directly to the strength of the interaction, and have to be compared. Normalizing these descriptors by their upper bound may help to interpret.

8) In each of these experiments, the conclusions were drawn with a different path of reasoning and different constructions of statistical tests to compare and assess the significance of observed differences between these 2 descriptors for different conditions. I do believe that the manuscript would gain in impact by providing a general workflow (maybe a scheme with different possibilities), including the assessment of significance of the descriptors differences. Otherwise, the potential user of this powerful technique may struggle with the analysis and be led to erroneous conclusions.

9) The Discussion of this article is quite disappointing. The first part is a summary of previous conclusions, the second part being a short comparison to already published, approaching methods. The manuscript should benefit from this comparison being included into the proper section of the manuscript, namely the co-localisation one.
