# Peer review - Round 1

Editors:
- Katalin Toth, University of Ottawa Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.73046.sa0](https://doi.org/10.7554/eLife.73046.sa0)

This manuscript uses a combination of high-quality in vivo electrophysiology and modelling to demonstrate that Behavioural Time Scale Plasticity (BTSP) is bidirectional, and the amplitude and direction of this plasticity are dictated by the current weight of the inputs and not by the correlated activity of pairs of neurons. These findings challenge our current views on synaptic plasticity, which are primarily based on Hebb's concept. In addition, the network model used in this study demonstrates that this type of plasticity can rapidly reshape population activity to respond to environmental clues. This study will be of interest to the broad neuroscience audience and foster new ideas on biological and artificial learning.


---

# Peer review - Round 1

Editors:
- Katalin Toth, University of Ottawa Canada

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.73046.sa1](https://doi.org/10.7554/eLife.73046.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Bidirectional synaptic plasticity rapidly modifies hippocampal representations" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and Laura Colgin as the Senior Editor. The following individuals involved in review of your submission have agreed to reveal their identity: Jerome Epsztein (Reviewer #1); Richard Naud (Reviewer #2); Larry F Abbott (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

The reviewers unanimously expressed their support for this manuscript. Their comments will help the authors to improve the clarity of the manuscript. The changes suggested by the reviewers do not require the authors to do additional experiments.

Reviewers' comments detail the points of improvement.

1. Please provide more details of the BTSP procedures and the behaviour of the mice.

2. Please elaborate on the rationale behind experiments depicted on Figure 2E, 3 and 4.

3. Please improve the clarity of data depicted on Figure 3D and 6A.

4. Please consider Rev.#2's comments on the approach of the computational section.

5. Please address questions raised about W and Winit.

Reviewer #2 (Recommendations for the authors):

There are two parts to this article. One experimental part and one computational modelling part. My opinion of the experimental part is that it is very carefully done with impressive, compelling (and difficult!) experiments. The results are at first glance extremely perplexing, but the interpretation and follow-up experiments are clarifying a lot. In this respect, the manuscript is much improved over the biorxiv version I had read a year ago. My only note on the experimental part is that the p-value threshold for Figure 4 C and F used for denoting might have a bit of a higher rate of false positive because every time point would be considered as a comparison. This would be correctable by Bonferroni factors, but honestly, I don't think it is entirely necessary since there is a bit of ambiguity as to what hypothesis is being tested.

The computational part is compelling for the success of reproducing the data with a model that is intrinsically stable. I think the writing could be improved without too much work, focusing on two points.

The theory section was going deep in the implementation details. A level of depth that is uncommon for the main results part of a broad audience paper. I would suggest keeping the learning rule and maybe one or two crucial equations, but relegating many of the equations to the methods. For instance the linear ODE for the traces are so common that defining trace as a linear ODE or mono-exponential decay would be sufficient (if the equation remains in methods). Similar for the integration of the dW/dt over a trial. I want to stress that this is a stylistic point that I believe will help communicate the message, not something required for accepting the paper. Another stylistic point is the use of two-letter variables along with two conventions for multiplications (the Asterix and nothing as when tau multiples d λ /dt). I was also confused by the use of Winit in Equation 3, which in my view should be W (no init) all the time.

The results rely crucially less of the fact that q+ and q- are nonlinear than on the fact that the nonlinearities are different. This should be clear from the fixed point analysis: consider Equation 8 with q+=q- and you find that the fixed point is independent of timing even for nonlinear relationships. This can also be revealed when looking at the parameter values: the LTP term has a sigmoid with a small sensitivity (β+), a large threshold (α+) and a large saturating point (k+). The converse is true for the LTD term. Thus plotting the sigmoidal for each term should explain the Mexican hat: for a strong W, when the coincidence is very small, you only may only have a weak q+ effect (because the sensitivity difference). When the coincidence is medium, LTD dominates over LTP because q- sharp threshold has been met without having reached the saturation of q+. When coincidence is strong q+ dominates because k+ is larger than k- (and both sigmoids have saturated). All this depends on W of course. Personally, I would have liked to see q+ and q- plotted, and how they combine to give the Mexican hat (or not). As in Figure 5B but showing q+ and q- in addition. With respect to Figure 5B, the absence of potentiation at high coincidence IS*ET for the high W case is puzzling. Why is this not showing? W is not high enough? q+ should dominate in that regime.

Other notes. These are more comments which may or may not help rather than points to be addressed.

I would like to point that the plasticity model fits partially well with the model used in the recent paper by Payeur et al. 2021. In that paper, the bursts caused a potentiation that depended on previous potentiation (dependency on W). But that model had a very limited timing dependence and bursts would only lead to net LTD if they were not numerous enough relative to the number of spikes. Overall, a comparison with this model suggests that the BTSP model provided by Milstein et al. could be consistent with a coordination of plasticity, as acknowledged by the authors at the end of the discussion.

The model is also partially related with the model of Graupner,.… Brunel. Recently used to capture STDP phenomena by Aljadeff… Debanne. There, two threshold are present, one for LTP and one for LTD. So similar to the α+ and α- being different. But the dependence in that model is very limited.

I thought the description of how W was kept between 1 and Wmax was lacking. There are multiple ways of doing this. And the different types of implementation (hard threshold vs soft threshold) have been shown to lead to dramatically different functions in the STDP modelling literature.

I think there is a typo in the list of parameters given at the end as I don't find τIS and τET, but only τI and τE.

Reviewer #3 (Recommendations for the authors):

This paper is beautifully done and well written. I have just a few suggestions:

1) It seems a pity that after elegantly formulating a model of BTSP, the authors final formulation of the synaptic change in Equations 3 and 4 is ill-defined. This is because the relationship between W and Winit is not specified. Wouldn't a proper formulation state that Winit = W, equation 3 does not describe dW/dt but rather a factor that determines ΔW through Equation 4, and that this latter process only takes place after a delay?

Alternatively, could Winit in the equation for dW/dt just be set to W? This would have the nice property of keeping W bounded between 0 and Wmax. Does this not work?
