# Peer review - Round 1

Editors:
- Arthur Prindle, https://ror.org/000e0be47 Northwestern University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.78075.sa0](https://doi.org/10.7554/eLife.78075.sa0)

The important contribution of this study is the ability to leverage engineered gene circuits to control cellular membrane potential. The presentation of the data in this work is convincing and the controls are in place to demonstrate that electrophysiological changes arise from external chemical stimuli. This study will be of interest to those working on non-neuronal bioelectricity, particularly synthetic biologists and bioengineers.


---

# Peer review - Round 1

Editors:
- Arthur Prindle, https://ror.org/000e0be47 Northwestern University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.78075.sa1](https://doi.org/10.7554/eLife.78075.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Macroscopic control of synchronous electrical signaling with chemically-excited gene expression" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, one of whom is a member of our Board of Reviewing Editors, and the evaluation has been overseen by a Reviewing Editor and Naama Barkai as the Senior Editor. The following individual involved in review of your submission has agreed to reveal their identity: Joseph Larkin (Reviewer #3).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) The title/abstract should be refocused to de-emphasize communication/electrical signaling/synchronous, since the coordinated behavior is largely driven by external chemical stimuli. The mechanistic basis of the external chemical stimuli -> membrane potential change is the priority and is impactful enough on its own.

2) With that goal in mind, the rationale behind the excitable dynamics, as well as each of the molecular mechanistic steps, should be made clearer:

a) Why are excitable dynamics important here? This should be justified more clearly in terms of the synthetic biology application, as it makes implementation by other researchers more complex. Does the circuit as constructed truly exhibit excitable dynamics? This should be probed using their computational model along with further experiments. For example, by trying other non-periodic inputs or checking for a refractory period.

b) What is the clear causal chain of molecular events for producing a membrane potential change using chemical stimuli, including inducer uptake, excitable circuit activation, ion channel expression, ionic flux, membrane potential change, and finally membrane potential reporter fluorescence? This is the core contribution of the manuscript and is necessary for others to use this toolbox. This should be clearly illustrated with a schematic figure and each of these mechanistic steps should be tested with experimental controls. For example, by using a more standard voltage dye (such as TMRM or a voltage-sensitive protein) to track membrane potential, a K+ selective dye to track ionic flux, and matching degradation tags between KCsA and GFP to demonstrate the expression lifetime of the channel. Is it possible that membrane channels are more difficult to degrade than free proteins? Is it also possible that other ionic fluxes and/or cellular metabolism related to PMP could be interacting with the excitable circuit dynamics?

Reviewer #1 (Recommendations for the authors):

Overall, I think that this is a promising manuscript that should be accepted following minor experimental revisions to supplement the results with additional mechanistic controls (described below).

Specific Questions/Suggestions:

1) The authors should use a more standard voltage-sensitive dye (such as TMRM) or a voltage-sensitive protein. ThT can act as a voltage-sensitive dye due to its positive charge but is nonstandard

2) The authors should use a K+ dye to confirm that voltage changes are due to K+ flux

3) KcsA and GFP have different degradation tags. Can you show an equivalent expression in KcsA system to show it tracks the dynamics? What if KcsA is always present but some other cellular feedback (such as YMC) results in the dynamics? Is the yeast metabolic cycle contributing to these dynamics? How do the timescales compare and can YMC oscillations be observed in this setting?

4) The time histogram for periods is intuitive in Figure 1, why isn't that continued in Figures 2/3 instead using a power spectra? I think using the period histograms would give more confidence in the results.

5) Is the TOK1 channel constitutively expressed based on literature data or data from the authors? Is there a chelator of K1 toxin to confirm its role as a relevant diffusible signal? Or pulsing external K1 toxin and/or other channel blocker?

6) Scales bars and scale information would be useful, particularly for the colony experiments. Additionally, images in Figure 3b could be improved, and (along with movies) suggest heterogeneity of voltage response and toxicity of KcsA expression and K1 toxin in general. How long can this strategy be sustained due to toxicity? Is this a challenge to bioengineering/synthetic biology applications?

Reviewer #2 (Recommendations for the authors):

Overall, I think this is good work that should be published in eLife, as many in the community could benefit from novel approaches to synthetic biology – much more needs to be done in this emerging area. I do believe that the authors have supported their claim of control of synchronous electrical signaling via channel expression. However, overall, the presentation can be improved in a way that leads to a clear comprehension of what has been achieved. While synchronous fluorescence is achieved, what does this mean, that Vmem is identical across cells? Or just that Vmem is changing at the same rate? Or is it synchronous gene expression? It's not explicitly made clear but should be the key part of the introduction or methods. The greatest addition that can be made is a clear causal chain in Figure 1 drawing out the steps of channel expression, channel function, Vmem change, fluorescence, etc. If the goal is truly a tool or toolbox for others to use, this is necessary. Furthermore, the limited rigor in which the electrical activity was characterized, and the light discussion on drawbacks/limitations, reduces the impact of the claim that it is a 'robust synthetic transcriptional toolbox'. I think this is very nice work but needs to be presented a bit more thoughtfully.

General Remarks:

1. I would like to see an experimental null model that is not simply a control population (Sup 2-2, B), but where chemical stimulants are delivered in a manner seeking to abolish the periodicity.

2. In Figure 3D, it seems that this K1->TOK is slightly less reliable than the previous 2 experiments. There are a couple of communities that don't seem to sync as much. Why? This should be discussed.

3. It seems that the shorter the cycle, the less reliable the method (see figure S1, 5). I didn't see this mentioned anywhere.

4. In keeping with (2) and (3), there is little discussion of drawbacks/limitations/etc. – please add.

5. I'm not sure of the difficulty of the experiments, but many times you list that each experiment has been repeated, 'at least two times.' Why not give a precise sample size? N = 2 seems low, and perhaps the authors want to state what the limitations/difficulties were (which in turn bears on the issue of this being a toolbox – people need to know how many N's are reasonable).

6. While phase difference is a fine measure, there are many ways that periodic signals can be analyzed (wave shape, amplitude, etc.) including other measures of synchronicity. It may be useful to measure/characterize other aspects of how these electrical signals are related. I think this may be useful, as in Figure 2B and 3C that the mean dark line doesn't well represent the data spread.

Line Remarks:

1. Line 50-51: while I agree that ion expression may be noisy, it may also be attributed to biological degeneracy. It would be interesting to address this and how it may affect the results.

2. Line 69-71: I do not know why you chose Mar receptors, why it matters, the upsides/downsides, etc. Due to the earlier claim that this is a 'toolbox', please say more about these choices and what other choices could be made. As it stands, this is a single 'tool'.

3. Line 114-115: Does anything else contribute to potassium release? Are there any other mechanisms by which the PMP remains balanced? How does your method affect these, if at all?

4. Line 179-181: I do not understand the claim that this methodology is non-invasive. How would I do this in-vivo – don't you need a way to stimulate cells with chemicals in a periodic fashion?

5. Line 186-187: I would like to see in the discussion the author's thoughts on how this may disrupt electrical communication. In neuroscience, for example, electrical signaling is paramount for proper brain function. Would any system that depends on timed electrical communication not be eligible for this method?

Figure Remarks:

Overall, I think the figures need a bit more work and care put into them. They do not always communicate the ideas clearly, which is a shame given the valuable work:

1. Figure 1 – why is there a cyan channel inside the cell – what does this indicate?

2. Figure 1 – Most critical is to add a 'flow diagram' to walk me through what is happening overall. Figure A-B leave too much for my imagination. Especially for someone not familiar with the subject. Specifically, the causal chain downstream of the chemical stimulation – what happens next to the channel, the PMP, and eventually fluorescence – an explicit block diagram (and text) of what's driving what in this circuit.

3. Figure 1 (and others) the tiny boxes above C with SA/IAA are not obvious to see, nor to what they're doing. Again, more care should go into explaining the method and the results, as presenting this methodology is the entire point of the paper.

4. Figure 1D could have 'flow arrows' that better describe what's happening.

5. Figure 1 – The heat map is not labeled on the Y axis, and you reference specific community numbers a couple of times.

6. Figure 1E – The dashed colored lines make this too hard to read.

7. Figure S1, 3-4: These graphs are directly comparable, but have flipped y-axis. Why?

8. Figure 2E – I may be wrong, but the PSD seems strange. The peak of the dotted lines is ~0.002 Hz, which is around 8.3 minutes. However, this a 1h induced period. Is this off by a factor of 10? 0.0002 is closer to 1.3 hours.

9. Figure 2E – The entire point of this graph is to show that you can make a signal with a given frequency. However, I have no way to know what those peaks are, because they are not labeled, and the x-axis is making readers guess.

10. Figure S1, 6 A – please mark peaks or give me a x-axis that lets me guess better.

11. Figure S1, 6 D – I would not consider the variation here low. In fact, the title of the figure seems misleading. While yes, there is little change across stimulation period/shape the actual values are quite variable.

Small typos:

1. Line 37, 'which in turn provides (a?) power reservoir'

Reviewer #3 (Recommendations for the authors):

We would like to reiterate that this paper impressed us and we are enthusiastic about it.

First, here are some suggestions for addressing the two major issues we mentioned;

– To address this first issue, we think it is possible to remove references to signaling or communication within the text and focus it on chemical control of membrane potential. Again, we think that result in itself is impactful. The text and figures should make it clearer that the data show a group of cells all independently responding to the same driving stimulus. This is not engineering communication. It is a step toward that goal.

Another option would be for the authors to present analysis of the existing data that demonstrates spatial signal propagation.

We do not think Figure 2 supplement 3 should be included in the paper unless there is clear observation of a spatially propagating excitable signal.

– We suggest multiple approaches to argue for excitable dynamics. First, the authors could experimentally test several predictions of the excitable model with the microfluidic system. Do they observe a refractory period? Do they observe the expected behavior from the model if only one of the phytohormones is added or taken away? Supplements 3 and 4 of Figure 1 provide some support, but those results are not compared to specific predictions or a non-excitable scenario.

We have several overall questions and suggestions:

– Please describe the device in more detail. How physically large is each well? Roughly how many cells are contained in each well? When reporting average fluorescence values from colonies, roughly how many cells are being averaged over?

– The text often remarks about noise and how the system buffers noise. However, the Figure 1 video shows notable heterogeneity in GFP expression. Some cells have low signal, others very high. Is this expected for the excitable circuit? At the same time, the ThT movies from Figure 2 appear less heterogeneous, which is interesting given that the experiments have the same underlying circuit. Is this due to some buffering of noise by physiology that maintains membrane potential? Could it be due to buffering of cells by each other when they all release or take up potassium? What do the authors think about this? Or are we wrong about our observations of heterogeneity? The text presents no analysis, so one can only guess by looking at the movies.

– As described above, is it possible to perform a co-culture experiment of wild-type cells with the engineered KcsA* strain and drive the engineered strain with chemical stimuli? This would result in collective potassium leak by the engineered cells. Figure 2 supplement 1 suggests that this may modulate the membrane potential of the WT cells. While similar to the experiments of Figure 3, it may come closer to demonstrating electrical communication.

– The early discussion of TOK1 was distracting. We believe that TOK1 can be introduced with Figure 3.

– What do we know about the relevance of membrane potential in yeast? Given what we know, does this system offer any way to control yeast physiology? If the authors have any thoughts on this, it would be great to include those in the concluding remarks.

There are some components of the paper that were highlighted, but we didn't fully grasp their importance. It would be great if the authors could describe the importance of these aspects more. Here are the components whose importance we would like to better understand:

– Why is construction of an excitable circuit central to this result? Reasons to do this would be to synchronize cells and to create a spatially propagating wave. However, as we have indicated, it does not appear in the data that the system does these things.

– What is the importance of the phase drift measurements? Does the different phase drift for different stimulation patterns tell us something about the synthetic circuit?

We have several comments on the figures:

– Figure 1A and 1B are confusing. Figure 1A shows control of ion channels, which is the point of the paper, but not of Figure 1. This sets up the expectation that the results of Figure 1 are with ion channels. Figure 1B is very difficult to read. Perhaps color-coding the regulatory arrows for the two parts of the circuit would make it more clear? Or showing a simplified version like that of Figure 2A? As is, it takes a lot of examination and thought to understand what Figure 1B is showing.

– Is it possible to show where the pulses of the phytohormones are happening on the time trace graphs as shading in the background throughout the time trace? As the figures are now, it is difficult to tell that the chemical stimuli are periodic.

– In the autocorrelation graphs, why is one curve a heavy black line and the others light, colored, dotted lines? This makes it difficult to read the colored lines and leads the reader to believe there is something fundamentally different about those conditions from the black line.

– A small comment: is it possible to use a different color scale for ThT and GFP heatmaps? Or add color bar scales to the heatmaps with labels like "GFP Intensity" or "ThT Intensity"?

We believe some panels in the supplements could be brought into the main figures:

– Figure 1 – supplement 1B and D, could be added to main text Figure 1 to illustrate the excitable dynamics of the circuit.

– Figure 2 supplement 2A and B are essential and support what we believe is the most impressive result here, engineering the ability to dynamically control cellular membrane potential. Perhaps ACFs could be computed and compared for the two examples in this supplementary figure also.
