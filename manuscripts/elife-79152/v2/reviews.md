# Peer review - Round 1

Editors:
- Piali Sengupta, https://ror.org/05abbep66 Brandeis University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.79152.sa0](https://doi.org/10.7554/eLife.79152.sa0)

This important work describes the temporal mechanisms of odor coding in the olfactory neurons of the locust. The supporting evidence is compelling and based on extensive experimental and computational analyses. This work will be of interest to sensory neuroscientists.


---

# Peer review - Round 1

Editors:
- Piali Sengupta, https://ror.org/05abbep66 Brandeis University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.79152.sa1](https://doi.org/10.7554/eLife.79152.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Olfactory receptor neurons generate multiple response motifs, increasing coding space dimensionality" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Piali Sengupta as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Martin Nawrot (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

As you can see from the individual reviews, all reviewers (and myself) agree that this is a study of high potential importance with expertly executed experiments that result in an impressive and highly valuable dataset. However, we also all agree that some work is needed not only to expand the discussion but in particular to link the modelling part better to the experimental/data analysis one.

1) Presentation and level of detail: Please include detailed statistical descriptions throughout, details about the recording configuration including sensillum type, as well as detailed statistics about the interaction of motif switching and odour types. Do expand figure descriptions to ensure that all figure parts are properly explained.

2) Computational modelling: Locusts have a specific and unusual arrangement in that OSNs expressing the same receptor project to different glomeruli. Moreover, they have significantly more OSNs than e.g. Drosophila. Please assess how OSN number and the specific projection pattern affect the conclusions of the model to qualify its generality.

This is indeed a key issue – with the architecture of the locust's olfactory system so different from other insects (and lots of unknowns with respect to the molecular make-up), this not only requires extensive and detailed discussion and comparison but also possibly exploring larger parameter space in the model.

3) Computational modelling: Tighten the link between experimental approach and model, for example, by comparing the distribution of response latencies and peak rates. Assess the validity of the filters used and perform explicit cross-validation. Individual model parameters need to be explicitly described and it needs to be made clear how they impact the model predictions. Figure 5 seems to assess the consequence of motif-switching for a situation where responses to one odor are held constant. Importantly, the comparison to ORN activity in Figure 6 needs to be quantified.

4) Computational modelling: Generally, the model needs to be described much better, and accessible to non-experts. Equations need to be labelled, parameters described in detail, etc.

5) The set of odours used is quite limited. Ideally, a broader set of odours would be presented including odour mixtures and ethologically relevant "specialist" odours. Please at least discuss your findings and their applicability to other odour classes such as complex odour mixtures or ecologically particularly relevant odours where possibly a specialized circuitry could be expected.

6) As you can see from the detailed reviews, several important references and discussion points are missed. Please thoroughly go through those and amend accordingly.

Reviewer #1 (Recommendations for the authors):

This study would largely improve and be less specialized if the authors would broaden their discussion and provide further insight into their modeling approach. Furthermore, by expanding the odor set with ecologically relevant and rather diverse odors (such as PAN), it would be highly interesting to see whether the separation in these four response motifs would persist and whether odor identity coding would be more prominent. In addition, I have several specific suggestions that would improve readability and the value of the MS:

– The authors used two odors at different concentrations, while the other two odors were applied in just one concentration. Please add the concentration of the other two odors. It would be interesting to see the impact of odor concentrations on the dynamic of the OSN responses. Are the observed response motif concentration-dependent?

– The authors recorded mainly from trichoid sensilla, since those contain small numbers of OSNs which simplifies spike sorting. However, the authors mention that they also included recordings of other sensillum types. Please specify which types were measured and whether the response dynamics were sensillum-specific since those should express different types of ORs or IRs.

– In general, I am missing detailed info about the statistics used. The authors mentioned e.g. in Figure 3 that offset responses increased significantly during adaptation without providing any details. This increase is hardly visible in the corresponding figure.

– The descriptions of the figures in the figure legends are often insufficient and do not allow us to understand what is actually represented. For example, what is exactly shown in the two panels in Figure 3B? Does each line correspond to the same OSN responding to either hexanol or cyclohexanol? What is the meaning of the color code in Figure 3C? What are the shaded traces in Figure 4B? What is exactly represented in Figure 5C and what is the meaning of the color code? Please also increase the font size in Figure 3 to make it readable.

– The authors state that each OSN can exhibit different response motifs. How reliable/reproducible are the recorded responses? Do individual OSNs also switch between motifs for the same odor? Furthermore, it would be very informative if the motif switches would be analyzed with regard to odor specificity. Are the motif switches odor-dependent? Does for example an OSN that is tuned to hexanol always reveal an inhibition to cyclohexanol?

– As mentioned above, the computational modeling part is rather written for specialists and should be revised.

– Please cite and discuss the paper by Martelli and Fiala (eLife, 2019), which addresses adaptation mechanisms to odor pulses in OSNs in Drosophila.

Reviewer #2 (Recommendations for the authors):

Specific suggestions to address concerns are as follows:

1) There are 119 ORNs in the locust but simulations use a much greater number of receptors (10,000). Please justify this number or reduce it to match the experimental system.

2) The set of simulations in Figure 5 shows that motif switching improves odor classification. However, the comparison is made while holding responses to one odor constant while shifting responses to the second odor in different ways. This does not reflect the experimental situation where there is no motif switching for a given odorant.

3) The method that is used here to reconstruct neural filters is not appropriate for strongly correlated and natural odorant stimuli delivered experimentally. For a review of methods, please see https://pubmed.ncbi.nlm.nih.gov/23841838/.

4) It is imperative to add quantification for how accurately the model describes the ORN activity in Figure 6B.

5) Add error bars in Figure 6B for the estimated filters and gain functions.

Reviewer #3 (Recommendations for the authors):

Based on my opinion phrased in the public review above, I believe that this manuscript deserves publication with eLife if revised appropriately. That is, I have no doubt about the quality of experimental and theoretical methods and results. My concerns below refer to minor points in the description of the theoretical methods that may be improved, to a number of relevant but missing references including the observation of ORN response patterns in the fly, and to the Discussion that should be strengthened/deepened to further increase the impact of the present MS.

Specific review comments

1. ORN response motifs and temporal stimulus pattern responses in vivo and in silico

Galili et al. (2011) have shown clear offset responses (termed "post-odor responses") on ORNs in Drosophila. Martelli et al. (2013) have performed an extensive study on in vivo ORN responses and linear filter modeling of different stimulus-response patterns that partially fit the motif observations in the present manuscript. To my interpretation of their results, excitatory vs. delayed responses may also be odor concentration-dependent, different from the conclusion in the present supplementary figure. These studies should be cited and discussed; possibly there are additional references to that point that I am not aware of.

2. Discussion: ORN motifs in PN responses

PN responses have been shown to be highly complex in their odor-dependent temporal profile, in particular, they show inhibitory responses and delayed (late) responses (Krofczik et al., 2009), and off-responses (Galili et al., 2011). Individual PNs can respond rapidly to odor onset for one odor and exhibit a strong inhibition of other odors. This inhibition can be very fast abolishing PN response efficiently (Krofczik et al., 2009). The ORN motif switching shown here could provide an explanation for this observed behavior in PNs. Also, ORNs make direct connections to both, PNs and LNs (shown in detail in Drosophila) and this may further accentuate the expression of similar motifs in PNs odor code, e.g. if individual ORNs predominantly or exclusively target PNs and inhibitory LNs. Indicating the potential effect on PN coding in the Discussion will add to the impact of the present MS.

3. Discussion: mechanistic modeling of ORN adaptation in biophysical model neurons

The authors use a phenomenological linear filter model to describe the stimulus-response current. The Discussion does not indicate how realistic biophysical models for adaptive ORNs can at least capture the excitatory motif (as in classical stimulus adaptation reviewed in Benda 2021) and post-stimulus rebound effects. E.g the conductance-based spike frequency adaptation model (Farkhooi et al., 2013) has been shown to fit the excitatory response motif; this paper also showed that these mechanisms significantly increase response reliability across trials that cannot be captured by the phenomenological model presented here. This model of adaptation also explains the inhibitory post-stimulus effect after an excitatory response and the post-inhibition rebound as offset-response (Farkhooi et al., 2013, Betkiewicsz et al., 2020) that are also present in the response motifs where the avg. excitatory firing rate drops below baseline (Figure 1C, bottom and top) and in the inhibitory rebound after the offset of the long stimulus (Figure 1C, bottom, Figure 2A). The stimulus-response filters are designed to capture both these effects in the present MS (Figure 4B).

4. Discussion: Functional interpretation for odor sensing in a complex odor environment

The results are relevant for biologically realistic integrative models of the sensory pathway and sensory-motor transformations. The temporal dynamics of ORN responses are particularly relevant when simulating odor navigation behavior in flying or walking insects. The recent study by Rapp and Nawrot (2020) has shown that ORN adaptation (classical) translates to PN firing (which are modeled as non-adaptive neurons) and is important to reproduce temporally sparse coding in the mushroom body and is thus required for the active sampling of the statistics of odor encounters that can subserve navigation.

5. Discussion: Distance-related odor plume statistics

There have been several studies on the distance-dependent odor plume statistics and their mimicking in temporally patterned stimulation during physiological recordings, in particular in the moth (Jacob et al. 2017, Levakova et al. 2018).

6. Quantitative measures to inform models

For modeling purposes, it would be valuable if the authors can provide additional quantitative measures such as a distribution of response latencies and peak rates. Also, Figure 1C shows average response rates +-SEM for the 4 motifs in the overlay. A supplemental figure that shows trial-averaged average responses per unit in overlay separately for the four motives would allow for variability across neurons.

7. Method description of the theoretical model

– The methods section appears in front of the Results section. I believe it should appear after the Discussion according to eLife instructions.

– Please number equations.

– Eqn. following l.189: I understand u=(y_n+β_n) as in the first equation, correct? I was puzzled by the spike that "can" be produced if -0.5 < x_n < 1 and expected a stochastic process. The correct interpretation is that a spike is produced when threshold -0.5 is crossed I assume. x_n+1 is set to -1 after a spike, which is a reset. Can x_n become smaller than -1 due to input and noise or is it bound?

– Eqn. following l.207: Is γ^S < = 1 and > = 0? Is it a fixed parameter?

– The description of the effect of the model parameters β, γ, and α remains somewhat vague and very short in lines 212/213; it is not entirely transparent to me which parameter drives post-stimulus effects and whether γ is fixed or, likely, follows the stimulus step response.

– The authors show PID responses in Figure 6 for random stimulus trains. What do they look like for the long stimulus pulses? I would expect a low-pass type PID response (charging curve) and could this account for some of the low-pass filter properties in the model?

– Prediction with linear non-linear cascade model. It is not clear to me how cross-validation is performed here. The filter and transfer functions are estimated from the responses to the stochastic pulse presentation. How is the cross-validation done? Training on a set of trials (how large) and prediction on a different set? Even more convincing would be to train the model on the first half of the stimulus train and test on the second half. I understand that all animals were presented with the same stimulus. Can the authors train the model on individual neurons and predict the response of the pseudo population of non-simultaneously recorded cells? How well does the model work when the filter is estimated from single or repeated pulse presentations, does this easily transfer?

References:

Benda, J. (2021). Neural adaptation. Current Biology, 31(3), R110-R116.

Betkiewicz, R., Lindner, B., and Nawrot, M. P. (2020). Circuit and cellular mechanisms facilitate the transformation from dense to sparse coding in the insect olfactory system. Eneuro, 7(2).

Farkhooi, F., Froese, A., Muller, E., Menzel, R., and Nawrot, M. P. (2013). Cellular adaptation facilitates sparse and reliable coding in sensory pathways. PLoS computational biology, 9(10), e1003251.

Galili, D. S., Lüdke, A., Galizia, C. G., Szyszka, P., and Tanimoto, H. (2011). Olfactory trace conditioning in Drosophila. Journal of Neuroscience, 31(20), 7240-7248.

Jacob, V., Monsempès, C., Rospars, J. P., Masson, J. B., and Lucas, P. (2017). Olfactory coding in the turbulent realm. PLOS Computational Biology, 13(12), e1005870.

Krofczik, S., Menzel, R., and Nawrot, M. P. (2009). Rapid odor processing in the honeybee antennal lobe network. Frontiers in computational neuroscience, 2, 9.

Levakova, M., Kostal, L., Monsempès, C., Jacob, V., and Lucas, P. (2018). Moth olfactory receptor neurons adjust their encoding efficiency to temporal statistics of pheromone fluctuations. PLoS computational biology, 14(11), e1006586.

Martelli, C., Carlson, J. R., and Emonet, T. (2013). Intensity invariant dynamics and odor-specific latencies in olfactory receptor neuron response. Journal of Neuroscience, 33(15), 6285-6297.

Rapp, H., and Nawrot, M. P. (2020). A spiking neural program for sensorimotor control during foraging in flying insects. Proceedings of the National Academy of Sciences, 117(45), 28412-28421.
