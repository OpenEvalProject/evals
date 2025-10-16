# Author response - Round 1

Authors:
- Tianhao Chu ([ORCID: 0000-0001-9910-9361](https://orcid.org/0000-0001-9910-9361))
- Zilong Ji ([ORCID: 0000-0001-7868-6178](https://orcid.org/0000-0001-7868-6178))
- Junfeng Zuo
- Yuanyuan Mi
- Wen-hao Zhang
- Tiejun Huang
- Daniel Bush ([ORCID: 0000-0002-5097-8117](https://orcid.org/0000-0002-5097-8117))
- Neil Burgess ([ORCID: 0000-0003-0646-6584](https://orcid.org/0000-0003-0646-6584))
- Si Wu ([ORCID: 0000-0001-9650-6935](https://orcid.org/0000-0001-9650-6935))

## Response text

DOI: [10.7554/eLife.87055.4.sa3](https://doi.org/10.7554/eLife.87055.4.sa3)

The following is the authors’ response to the previous reviews.

Response to reviewer #1:

We thank the reviewer for the further recommendations for improving our presentation. We would like to carefully address the remaining concerns of the reviewer.

(1) I realize now that I didn't make my point clear enough, which was that as far as I know there is no reason to believe that an oscillatory state cannot be induced with synaptic depression as with spike frequency adaptation when used in the context of the author's model. I'm fine with how the authors have distinguished their model from R&T 2015, but I think the more interesting question is whether there is any reason to believe that STD is not equally capable of doing all the things mentioned in this paper as SFA, and if not why not. I would like the authors to go out on a limb and address this, if only with a few sentences in the discussion.

Thank you for pointing this out again. In response to your query regarding the comparison between STD and SFA in generating bump sweeps, we have done simulations based on STD. The results showed that both STD and SFA are capable of inducing bi-directional sweeps. However, (based on our simulations) only SFA can produce uni-directional sweeps. The absence of uni-directional sweeps based on STD may be due to the subtle yet important differences between the two mechanisms. Specifically, STD modulates the neural activity by weakening the recurrent connections, which theoretically can only inhibit recurrent inputs, while SFA can attenuate all forms of excitatory inputs, including external inputs. However, since we did not exhaustively explore the entire parameter space, we cannot conclude that STD is incapable of producing uni-directional sweeps. Future simulations are required.

According to the Reviewer’s suggestion, we added few sentences to discuss the distinctions between STD and SFA in generating theta sweeps in the CANN in line 432 to 440 in the Discussion session:

“Based on our simulation, both STD and SFA show the ability to produce bi-directional sweeps within a CANN model, with the SFA uniquely enabling uni-directional sweeps in the absence of external theta inputs. This difference might be due to the lack of exhaustively exploration of the entire parameter space. However, it might also attribute to the subtle yet important theoretical distinctions between STD and SFA. Specifically, STD attenuates the neural activity through a reduction in recurrent connection strength, whereas SFA provides inhibitory input directly to the neurons, potentially impacting all excitatory inputs. These differences might explain the diverse dynamical behaviors observed in our simulations. Future experiments could clarify these distinctions by monitoring changes in synaptic strength and inhibitory channel activation during theta sweeps.”

(2) I appreciate the inclusion of the experimental data in Fig 6a (though I don't find the left-most panel very useful). I also understand what the authors are trying to convey with plots in 6c and 6c. However, I don't find the text that was added above very helpful at all. I was hoping for a simpler demonstration of the effect, by plotting a series of sequential sweeps (cell index vs time, with color indicating firing rate, as in Fig 2d) in the case of both the slow speed and fast speed regimes. Here, vertical lines could mark the individual theta cycles and the firing of individual cells, showing the constancy of the former but change of the latter.

Thank you for your constructive feedback. It seems there might be a misunderstanding in our previous explanation, for which we apologize. The phenomenon we want to elucidate is not an increase in the theta frequency as detected in LFPs, but rather the slope of phase precession with respect to the animal's movement speed. Due to phase precession, the oscillations of place cells as the animal traverses the field is higher than the theta frequency. A plot as Fig 2.d will not make this point clearer, since it shows the baseline theta frequency (i.e., theta sweeps as we claimed previously). A straightforward way of thinking this point is as we added previously: “…The faster the animal runs, the faster the extra half cycle can be accomplished. Consequently, the firing frequency will increase more (a steeper slope in Fig. 6a red dots) than the baseline frequency”. We hope this clarification addresses the concerns raised.

(3) This is still confusing to me. I just don't understand how the *phase* of the oscillating activity bump has anything to do with the movement of the animal. I would like to see a plot of the sweeps (again, cell index vs time, with color indicating the firing rate) before and after inactivation for short and long duration inactivation. Perhaps I am not understanding or appreciating how the bump recovers after inactivation and how this is related to the motion of the animal.

Thank you for pointing this out again. The activity bump will naturally pop out at the input location (which moves forward than before) after we remove the inactivation and then starts to sweep again as before the inactivation. Single cell phase precession and populational theta sweeps are actually the two sides of the same coin (if all cells start at roughly the same phase in theta cycles). If the reviewer accept this, then at the new location, the activity bump sweeps again (around the new location), and therefore phase precession starts again at a further phase, since phase codes the position as the animal traverses the place field.

(4) I am glad the authors are spending more time discussing this phenomenon, but I am unsure of their explanation: for a sweep moving at constant speed, neurons all along the path will be equally affected (inhibited), so where does the bias for suppressing the "end" neurons come from?

While it may appear that neurons along the path are equally inhibited as the bump sweeps over them, our model incorporates external inputs with Gaussian profiles. These inputs bias neurons closer to the input location, resulting in fewer activations in neurons further away from the input position.

(5) Here I was hoping that the authors might comment on what they suspect happens when the animal starts (or stops) moving, and how the network shifts from tracking regime to oscillatory regime (or vice versa), as is typically seen in experimental data (see for example, Kay et al., 2020, fig 4b,c). My apologies for not making this point clearer.

Thank you for pointing this out. In our model, we observed that when the animal stops, the network continues to generate theta oscillations near the input location, albeit with reduced amplitude (so the network dynamics looks like in the tracking regime). However, we hypothesize that when the animal pauses its movement for enough time (immobile but awake states), sensory input into the hippocampus also decreases, which is similar to removing external inputs in our model. In this case, the activity bump spontaneously moves away, resembling the phenomenon of replay (see also Romani & Tsodyks 2015).

Regarding the experimental data (Kay et al.), it indeed appears that theta sweeps decoded from neural activity become less pronounced when the mouse moves at slower speeds. This observation could potentially correspond to a decrease in the amplitude of bump oscillations when external inputs associated with movement are halted but not entirely removed in our model. However, in experiments, when the mouse's movement slows down, hippocampal activity no longer oscillates at theta frequency, making it challenging to decode theta sweeps.

We appreciate your clarification on this point and recognize the importance of further investigating how our model can accurately replicate the transition between tracking and oscillatory regimes observed in experimental data.
