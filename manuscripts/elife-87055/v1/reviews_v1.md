# Peer review - Round 1

Editors:
- Lisa M Giocomo, Stanford School of Medicine United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.87055.4.sa0](https://doi.org/10.7554/eLife.87055.4.sa0)

This study provides valuable new insights on how a prevailing model of hippocampal sequence formation can account for recent data, including forward and backward sweeps, as well as constant cycling of sweeps across different arms of a T-maze. The convincing evidence presented in support of this work relies on classical analytical and computational techniques about continuous attractor networks.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.87055.4.sa1](https://doi.org/10.7554/eLife.87055.4.sa1)

Continuous attractor networks endowed with some sort of adaptation in the dynamics, whether that be through synaptic depression or firing rate adaptation, are fast becoming the leading candidate models to explain many aspects of hippocampal place cell dynamics, from hippocampal replay during immobility to theta sequences during run. Here, the authors show that a continuous attractor network endowed with spike frequency adaptation and subject to feedforward external inputs is able to account for several previously unaccounted aspects of theta sequences, including (1) sequences that move both forwards and backwards, (2) sequences that alternate between two arms of a T-maze, (3) speed modulation of place cell firing frequency, and (4) the persistence of phase information across hippocampal inactivations.

I think the main result of the paper (findings (1) and (2)) are likely to be of interest to the hippocampal community, as well as to the wider community interested in mechanisms of neural sequences. In addition, the manuscript is generally well written and the analytics are impressive. However, several issues should be addressed, which I outline below.

Major comments:

In real data, population firing rate is strongly modulated by theta (i.e., cells collectively prefer a certain phase of theta - see review paper Buzsaki, 2002) and largely oscillates at theta frequency during run. With respect to this cyclical firing rate, theta sweeps resemble "Nike" check marks, with the sweep backwards preceding the sweep forwards within each cycle before the activity is quenched at the end of the cycle. I am concerned that (1) the summed population firing rate of the model does not oscillate at theta frequency, and (2) as the authors state, the oscillatory tracking state must begin with a forward sweep. With regards to (1), can the authors show theta phase spike preference plots for the population to see if they match data? With regards to (2), can the authors show what happens if the bump is made to sweep backwards first, as it appears to do within each cycle?

I could not find the width of the external input mentioned anywhere in the text or in the table of parameters. The implication is that it is unclear to me whether, during the oscillatory tracking state, the external input is large compared to the size of the bump, so that the bump lives within a window circumscribed by the external input and so bounces off the interior walls of the input during the oscillatory tracking phase, or whether the bump is continuously pulled back and forth by the external input, in which case it could be comparable to the size of the bump. My guess based on Fig 2c is that it is the latter. Please clarify and comment.

I would argue that the "constant cycling" of theta sweeps down the arms of a T-maze was roughly predicted by Romani & Tsodyks, 2015, Figure 7. While their cycling spans several theta cycles, it nonetheless alternates by a similar mechanism, in that adaptation (in this case synaptic depression) prevents the subsequent sweep of activity from taking the same arm as the previous sweep. I believe the authors should cite this model in this context and consider the fact that both synaptic depression and spike frequency adaptation are both possible mechanisms for this phenomenon. But I certainly give the authors credit for showing how this constant cycling can occur across individual theta cycles.

The authors make an unsubstantiated claim in the paragraph beginning with line 413 that the Tsodyks and Romani (2015) model could not account for forwards and backwards sweeps. Both the firing rate adaptation and synaptic depression are symmetry breaking models that should in theory be able to push sweeps of activity in both directions, so it is far from obvious to me that both forward and backward sweeps are not possible in the Tsodyks and Romani model. The authors should either prove that this is the case (with theory or simulation) or excise this statement from the manuscript.

The section on the speed dependence of theta (starting with line 327) was very hard to understand. Can the authors show a more graphical explanation of the phenomenon? Perhaps a version of Fig 2f for slow and fast speeds, and point out that cells in the latter case fire with higher frequency than in the former?

I had a hard time understanding how the Zugaro et al., (2005) hippocampal inactivation experiment was accounted for by the model. My intuition is that while the bump position is determined partially by the location of the external input, it is also determined by the immediate history of the bump dynamics as computed via the local dynamics within the hippocampus (recurrent dynamics and spike rate adaptation). So that if the hippocampus is inactivated for an arbitrary length of time, there is nothing to keep track of where the bump should be when the activity comes back on line. Can the authors please explain more how the model accounts for this?

Can the authors comment on why the sweep lengths oscillate in the bottom panel of Fig 5b during starting at time 0.5 seconds before crossing the choice point of the T-maze? Is this oscillation in sweep length another prediction of the model? If so, it should definitely be remarked upon and included in the discussion section.

Perhaps I missed this, but I'm curious whether the authors have considered what factors might modulate the adaptation strength. In particular, might rat speed modulate adaptation strength? If so, would have interesting predictions for theta sequences at low vs high speeds.

I think the paper has a number of predictions that would be especially interesting to experimentalists but are sort of scattered throughout the manuscript. It would be beneficial to have them listed more prominently in a separate section in the discussion. This should include (1) a prediction that the bump height in the forward direction should be higher than in the backward direction, (2) predictions about bimodal and unimodal cells starting with line 366, (3) prediction of another possible kind of theta cycling, this time in the form of sweep length (see comment above), etc.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.87055.4.sa2](https://doi.org/10.7554/eLife.87055.4.sa2)

In this work, the authors elaborate on an analytically tractable, continuous-attractor model to study an idealized neural network with realistic spiking phase precession/procession. The key ingredient of this analysis is the inclusion of a mechanism for slow firing-rate adaptation in addition to the otherwise fast continuous-attractor dynamics. The latter continuous-attractor dynamics classically arises from a combination of translation invariance and nonlinear rate normalization.

For strong adaptation/weak external input, the network naturally exhibits an internally generated, travelling-wave dynamics along the attractor with some characteristic speed. For small adaptation/strong external stimulus, the network recovers the classical externally driven continuous-attractor dynamics. Crucially, when both adaptation and external input are moderate, there is a competition with the internally generated and externally generated mechanisms leading to an oscillatory tracking regime. In this tracking regime, the population firing profile oscillates around the neural field tracking the position of the stimulus. The authors demonstrate by a combination of analytical and computational arguments that oscillatory tracking corresponds to realistic phase precession/procession. In particular the authors can account for the emergence of unimodal and bimodal cells, as well as some other experimental observations with respect the dependence of phase precession/procession on the animal's locomotion.

The strengths of this work are at least three-fold: (1) Given its simplicity, the proposed model has a surprisingly large explanatory power of the various experimental observations. (2) The mechanism responsible for the emergence of precession/procession can be understood as a simple yet rather illuminating competition between internally driven and externally driven dynamical trends. (3) Amazingly, and under some adequate simplifying assumptions, a great deal of analysis can be treated exactly, which allows for a detailed understanding of all parametric dependencies. This exact treatment culminates with a full characterization of the phase space of the network dynamics, as well as the computation of various quantities of interest, including characteristic speeds and oscillating frequencies.

As mentioned by the authors themselves, the main limitation of this work is that it deals with a very idealized model and it remains to see how the proposed dynamical behaviors would persists in more realistic models. For example, the model is based on a continuous attractor model that assumes perfect translation-invariance of the network connectivity pattern. Would the oscillating tracking behavior persist in the presence of connection heterogeneities? Another limitation is that the system needs to be tuned to exhibit oscillation within the theta range and that this tuning involves a priori variable parameters such as the external input strength. Is the oscillating-tracking behavior overtly sensitive to input strength variations? The author mentioned that an external pacemaker can serve to drive oscillation within the desired theta band but there is no evidence presented supporting this. A final and perhaps secondary limitation has to do with the choice of parameter, namely the time constant of neural firing which is chosen around 3ms. This seems rather short given that the fast time scale of rate models (excluding synaptic processes) is usually given by the membrane time constant, which is typically about 15ms. I suspect this latter point can easily be addressed.
