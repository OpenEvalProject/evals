# Peer review - Round 1

Editors:
- Sara Mitri, https://ror.org/019whta54 University of Lausanne Switzerland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.73870.sa0](https://doi.org/10.7554/eLife.73870.sa0)

The ultimate goal of this work is to apply machine learning to learn from experimental data on temporal dynamics and functions of microbial communities to predict their future behavior and design new communities with desired functions. Using a significant amount of experimental data, the authors suggest a method that outperforms the state-of-the-art approach. The work is of broad interest to those working on microbiome prediction and design.


---

# Peer review - Round 1

Editors:
- Sara Mitri, https://ror.org/019whta54 University of Lausanne Switzerland

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.73870.sa1](https://doi.org/10.7554/eLife.73870.sa1)

Our editorial process produces two outputs: i) public reviews designed to be posted alongside the preprint for the benefit of readers; ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Deep Learning Enables Design of Multifunctional Synthetic Human Gut Microbiome Dynamics" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Aleksandra Walczak as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Lingchong You (Reviewer #2).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) All three reviewers agreed that not enough detail of the methods was provided. Please include this in the methods section, as well as an in-depth discussion and justification as to the choices made, including why LIME and CAM have been chosen as opposed to other methods, what are the inputs and outputs to the system, how the training and testing sets were chosen and how parameters for the two models were chosen.

2) The reviewers also agreed that the comparison of the performance of gLV to LSTM was not quite fair, due to many differences between the two implementations. To more fairly compare gLV to the LSTM, please augment the PyTorch code to have LSTM+FF and gLV+FF.

3) Carefully consider the language used throughout the paper, for example in the use of the term "deep learning".

Reviewer #1 (Recommendations for the authors):

Results, first paragraph. 'The experimental102 data was split into non-overlapping training and hold-out test sets, and an appropriate LSTM network was trained to predict species abundances at various time points given the information of initial species abundance. The details on the train/test split and the number of model hyperparameters are provided in Table S2'.

It is worth mentioning these details in the main text, at least regarding data division and architecture of the LSTM based model.

What was the motivation behind the particular division of the dataset: 624 training communities and 3299 testing communities? Why 6 or fewer species were used in the training and > = 10 were used in the testing dataset?

The authors state that since the glv model was used to generate the simulated data, they were not surprised to see that it predicts very well on this dataset. Would it be possible to use another benchmark to compare the two models?

Regarding the computational time of the LSTM model, I imagine it takes a lot of time to tune the hyper-parameters of the LSTM model. I think it should be mentioned that the 2 minutes required to train the LSTM model does not include this computational overhead. It is not clear how hyper-parameter tuning (number of layers, nodes, learning rate, activation function, etc.) was performed. Could you please add further details about this in the method section?

It is not clear why a FFN was used at the output of the LSTM? I could not find any information in the methods section about this. Can you explain why this particular setting was chosen?

The following line is not clear: 'all the network weights are trained simultaneously'.

What was the motivation behind choosing CAM and LIME as the explanation method among all the existing explanation methods?

LIME is a heuristic based method. How did you verify the robustness of the explanations? Could you please comment on if you changed some parameters (such as number of variables) and how it affected the explanations? How can we be sure that the explanation provided by the linear LIME models is actually what the non-linear LSTM model is doing? Are we agreeing with the explanations just because it is consistent with the current knowledge?

Reviewer #2 (Recommendations for the authors):

My general impression is the work is very dense and key insights are somewhat masked due to the lack of clarity in places. At the highest level, I think I understood the major points the authors tried to deliver (see above). However, I feel the authors can improve the presentation of the basic methodology and the intuition on a few points, which I find myself just having to trust what the authors have to say. Providing such intuition could minimize the impression of some of the performance comparisons being ad hoc.

1. It is actually not entirely clear what exactly feeds into the LSTM (or the gLV) and what comes out during the training process. Figure 1 is supposed to explain that but I could only gather that they're predicting time series. More specifically, what are the input variables? How many time series are being predicted? The authors might want to revise/expand the schematic to better explain the basic methodology.

Also, an overlay of a few representative true time courses vs. predicted time courses (e.g. good predictions vs. failed predictions) would be illuminating.

2. Figure 2 shows the prediction of gLV-model-simulated data using the LSTM or the gLV model. Only a brief description was provided, from which, I had a hard time understanding how the data were generated or predicted. For instance, the authors stated that a 25-member gLV model was used to make predictions. Those with < = 6 species were used to train the LSTM or the gLV model. Does it mean that, in these communities, only < = 6 species persisted after some time? And, the trained LSTM or gLV models only predict < = 6 species? If so, the following sentence becomes confusing. This confusion is related to the confusion above.

Also, how are higher-order interactions modeled in the gLV simulator?

3. It feels like the results in Figure 2 should go first (before Figure 1). The rationale is simple – for the simulated data, you have complete confidence in the ground truth, which can allow you to test the performance of the method in the idealized scenario. Also, the analysis on this data can probably allow you to provide an intuition when and why LSTM outperforms the gLV model (especially when the data were generated by another gLV model).

4. Also in Figure 2, since the data generation or training were not super time consuming, I wonder if the LSTM or gLV predictions could be drastically improved if larger training data sets are used. I'm actually quite surprised by the performance of LSTM on the simulated data, considering the somewhat limited size of the training set (624). A recent work had to use a much larger training set to achieve a high performance of LSTM (Wang et al., Nature Comm 2019) – this related work should be cited.

5. The overall performance of LSTM is impressive. It does fail occasionally even on simulated data (which is true for all ML models). To this end, the authors should discuss/show how to evaluate the confidence in individual predictions – checking each one (even if the ground truth is known) would defeat the purpose of using the neural network. This point is relevant when the trained neural network is being used to make predictions and probe biological insights.

6. I like how they use a side product of training procedure (backpropagation) to provide a quantitative metric of system sensitivity. I feel they could explain this point more.

7. For me, part of the reason the paper feels dense is that there are actually two stories (though closely related). One is the prediction of community dynamics. The other is the prediction of metabolite profiles. They represent somewhat different challenges in terms of evaluating LSTM performance.

The paper could have been split into two. Combining the two might have caused some of the confusion raised above.

Reviewer #3 (Recommendations for the authors):

Major comment: To make the comparison fair I would suggest using your torch code base to also obtain point estimates for the gLV parameters as well. There is no reason to use a sampling-based result from the prior study which uses a different model for metabolite prediction as well. Furthermore, the composite code is not accessible without a Matlab license (and thus not really reproducible). It is also trained in a two-step fashion (if this is not the case then there was not enough detail in the text to understand how the composite model was trained), and thus will be less accurate because of this. It should not take 5 hours for the model to learn the gLV parameters (your own reference [56] states that you have this down to minutes). Your torch code can be easily modified for the dynamics \log x_{t+1} = \log (x_t) + (diagonal(r) + A x_t) \δ_t and then this also means that you could have the same FF architecture for metabolites. This would allow for a much fairer comparison, both models could be trained in an identical fashion with the same metabolite prediction architecture. Although regularization and hyperparameter tuning would be slightly different of course.

Title and throughout: A single LSTM unit with a single hidden state (which can be of large dimension) is not really a deep network. With this interpretation a linear dynamical systems model with a single hidden state is a deep model as well.

21: In the abstract it is stated that current ODE models fail to capture complex behavior. This is not true. You fit an Ordinary difference equation to your data when solving for GLV, RNN, or LSTM (these are all ordinary because time is the only differential or difference variable). I think you meant to characterize the difference between parametric models like linear or gLV, etc, that are more "rigid" vs dynamical systems models that convolve functions up to arbitrary complexity (RNN, etc). Both are certainly classes of "Ordinary" difference or differential equations.

147: A gLV model is linear in the parameters so it is trivial to solve for the coefficients of the model in seconds. The text should be changed here. Also why does it take 5 hours to learn the gLV model when you state in [56] that you have this down to minutes?

Figure 1 (a) is this the model or the teacher forcing training procedure depicted. Also there is a subscript i, suggesting that there is no microbe-microbe interaction information captured by the model. Is the data in figure 1 all forecasted from t=0 or is this 1 sample look ahead prediction performance, it was not clear from the text?

Figure 2 (a) also has i subscript, was this intentional.

Methods:

– The LSTM model is not described in enough detail (what are the dimensions of the objects, how many hidden states [and why], how did you tune the hyperparameters of the model and the gradient solver [what gradient method did you use and why]).

– How was the composite model trained, was it indeed in a two-step fashion whereby the gLV model was trained and then a separate inference procedure was run for the metabolite model. More detail is needed here to understand what exactly was done and how the models were trained.

Plots in general:

– Plots only really show how the most abundant taxa are performing, would be nice to see the performance on the lower abundance taxa (maybe take a log of the OD?).

References:

You seem to be missing some important references from the Gerber Lab, "MDSINE Microbial Dynamical Systems INference Engine for microbiome time-series analyses" https://doi.org/10.1186/s13059-016-0980-6 is one such example but there are likely more given that lab primarily focuses on microbiome dynamics.

[Editors’ note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Deep Learning Enables Design of Multifunctional Synthetic Human Gut Microbiome Dynamics" for further consideration by eLife. Your revised article has been evaluated by Aleksandra Walczak (Senior Editor) and a Reviewing Editor.

The manuscript has been improved but there are some remaining issues that need to be addressed, as outlined below:

Reviewer #3 still finds that there is a need for a direct "apples-to-apples" comparison of gLV and LSTM. In your response to the reviewer's initial request, you are arguing that such a direct comparison would result in a very low performance of gLV. If this is the case, it would simply strengthen your argument and support the use of LSTM even more. It also did not seem like much additional work to carry out this analysis. If this is done and added as a supplement with some explanation of why it's not in the main text, I believe this would be satisfactory to all reviewers. Other than that, the reviewers were very appreciative of the modifications and the current quality of the paper.Reviewer #1 (Recommendations for the authors):

Thank you. This is exciting work, and the authors have addressed all of my concerns thoroughly.

Reviewer #2 (Recommendations for the authors):

The authors have fully addressed my comments on the original submission. I support its publication in the journal.

Reviewer #3 (Recommendations for the authors):

One outstanding issue with the paper remains. There is no apples-to-apples comparison of the LSTM+NN to a gLV+NN. I now comment on the authors' responses to an original comment.

[Authors] "We did not estimate new gLV parameters for this work, but rather used the gLV parameters that were already determined in [6]."

Having a composite model trained on different data and comparing it to a jointly trained model on entirely different data is not a sufficient comparison.

[Authors] "While we agree that the reviewer's proposed method for determining the gLV parameters would be a more direct comparison, there are several reasons why we chose to use the gLV parameters estimated in our previous study: (1) Higher resolution time-series measurements are needed to determine the exponential growth rate in the gLV model. Thus, estimating gLV parameters without the time-series measurements of monocultures would result in a poorly predictive model due to high uncertainty in the exponential growth rate parameters of the gLV model. Therefore, the proposed method of inferring parameters of the gLV model would yield a poorly predictive model."

If this is the case then the authors should show that the gLV model is not predictive with this sparse data. This begs the question though. Why did one need the LSTM model if the data doesn't really capture complex dynamics? The abstract stated that the LSTM was necessary for this very reason [Abstract]"Current models based on ecological theory fail to capture complex community behaviors due to higher-order interactions, do not scale well with increasing complexity and in considering multiple functions. We develop and apply a long short-term memory (LSTM) framework to advance our understanding of community assembly and health-relevant metabolite production using a synthetic human gut community." The authors are simultaneously arguing that the dynamics are too complex for simple gLV dynamics while also stating that the new time series are too simple to reliably train a gLV model. Is this a contradiction?

"(2) The methods used to estimate the gLV model parameters in our previous work were informed by higher resolution time-series measurements of monocultures (individual species). Thus, the gLV model had additional information beyond that of the LSTM model, which was only informed by the initial point and endpoint (with the exception of Figure 5)."

This statement is confusing. The LSTM model was trained using teacher forcing with intermediate time points per the methods section?

"(3) The optimization algorithm MATLAB FMINCON is a widely used approach for estimating parameters of the gLV model (see [6], [8] and [10], for example) (4) The proposed method of log transforming the gLV model only works with higher resolution time-series data. We have sparse time sampling in our datasets."

If indeed the data is so sparse that a traditional gLV model would not learn then it would be easy for the authors to show this. In order to be published Figure 4 should compare gLV+NN and LSTM+NN trained on the same data in the same way and compare the model's performance directly.
