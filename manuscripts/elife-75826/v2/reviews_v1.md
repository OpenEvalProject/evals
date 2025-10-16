# Peer review - Round 1

Editors:
- Matthieu Louis, https://ror.org/02t274463 University of California, Santa Barbara United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.75826.sa0](https://doi.org/10.7554/eLife.75826.sa0)

This paper contributes to the growing body of literature that investigates foraging in complex sensory landscapes. It is therefore of interest to both neuroscientists and ecologists. Using behavioral analysis and computational modeling, the authors characterize different behavioral components of the foraging strategy adopted by the Drosophila larva as a function of food quality and food distribution. Altogether, this works sets the stage for investigating the genetic and neural-circuit bases underlying the control of foraging behavior.


---

# Peer review - Round 1

Editors:
- Matthieu Louis, https://ror.org/02t274463 University of California, Santa Barbara United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.75826.sa1](https://doi.org/10.7554/eLife.75826.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Adaptation of Drosophila larva foraging in response to changes in food resources" for consideration by eLife. Your article has been reviewed by 3 peer reviewers, and the evaluation has been overseen by a Reviewing Editor and K VijayRaghavan as the Senior Editor. The following individual involved in the review of your submission has agreed to reveal their identity: Mason Klein (Reviewer #4).

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1. Defining a potential contribution of taste to foraging. Is it known that yeast is 'unnoticeable' by taste? Did the authors try or consider testing the Gr43a mutant on these substrates? When the larvae are pausing, are they trying to eat the substrate?

2. Defining the role of other modalities: On patchy substrates, is the border completely smooth or could the larvae also sense the border as a rough edge? Are there effects from mechanosensation due to the different preparation of the patch edge (printing for yeast versus cutting for juice and sucrose)? Does diffusion of patch edge play a role for apple juice and sucrose?

3. It would be important to highlight the contribution of the model. Could the model be used to guide new experiments or to suggest new ideas? Would the integration of chemotaxis in the model improve the reproduction of specific behavioral features observed experimentally? Related to this point, one aspect where the work could be strengthened is by highlighting or speculating about where the differences in patch residence times between the model and data might arise.

4. Technical concerns related to the methodology:

– Define whether the simulation's initial conditions matter.

– Specify whether the model samples a steady-state/ ergodic distribution of trajectories or if time-dependent properties should be accounted for.

– Compared to other models, no patch depletion is taken into account. Wouldn't this affect the leaving rates in small patches especially and more so than larger patches?

5. Statistics: For an animal that tends to have a very high variance in its behavior, the number of larvae used in each experiment seems to be pretty low. This limitation should be acknowledged in the conclusions drawn in the paper. More specifically, low sample sizes can lead to false negatives. To address this concern, the authors should perform a statistical power analysis to increase the confidence in the "not statistically significant" results.

The reviewers agreed that points 3 and 4 could be mainly addressed through computational work and/or editing. If any of the other concerns can be adequately addressed without additional experimental work, we will generally support this option so that it reduces the efforts entailed by the revision.

Reviewer #2 (Recommendations for the authors):

I have a few suggestions that I believe could strengthen the manuscript:

– Please comment on the simulation's initial conditions and if they matter? From the trajectories shown in Figures 2 and 5, it seems like there could be some finite duration effect

– Are you sampling a steady-state/ergodic distribution of trajectories or are there time-dependent properties?

– Could you show how well single-trial simulation data matches single-trial experimental data with respect to trajectory features?

It would be helpful for the reader if the model predictions from Figure 2 could be articulated more explicitly in the section discussing Figure 2. It is mentioned later, but it would be useful to summarize these results before the next section of experiments.

– What are the navigational metrics in apple juice on homogeneous patches?

– Does diffusion of patch edge play a role for apple juice and sucrose? Or are there effects from mechanosensation due to the different preparation of the patch edge (printing for yeats versus cutting for juice and sucrose)?

– Please explain the exact nature of the defect in anosmic larvae. The results appear somewhat confusing otherwise. Is it known that yeast is 'unnoticeable' by taste?

– Compared to other models, no patch depletion is taken into account. Wouldn't this affect the leaving rates in small patches especially and more so than larger patches? Relatedly, the paper could benefit if the phenomenological results of the model could be connected to optimal foraging theory, as the authors cite the marginal value theorem. However, this might be beyond the scope of this work.

Reviewer #3 (Recommendations for the authors):

I like the paper overall, the main results are interesting and well supported. I have some issues with the logic of the simulations and how they inform the experiments. My only "major" change would be to rearrange the paper a bit and put the simulations after what is now Figure 3, maybe even after all of the experimental data figures.

General/broader comments:

(1) Using 30 or fewer larvae for each experiment type feels quite low in my experience. I'm not suggesting performing a bunch of new experiments (I almost never do in reviews), but I think it's important to be careful with claims about any comparison being "the same" (specific instances pointed out below) -- finding "n.s." does not mean two things are the same, especially when a small number of data points is used in the comparison.

(2) The introduction feels like it's missing at least a whole paragraph that should probably be explaining to a non-fly, non-foraging researcher why this study is important and useful. I study fly larvae too, and it's certainly exciting and interesting to me, but I think some more effort to draw in other researchers is warranted.

(3) The simulations. I like the method of using results from actual experiments to make the probability distributions that the simulation draws from in its random-walk-style tracks. I'm sure the simulations are done properly and make sense. What dampens my enthusiasm for them in this specific paper is that they don't seem to be informing the experiments or suggesting new ideas to the extent that they could. Numerous statements that start with "as predicted by the model" make it sound like the simulations are providing some kind of insight, but often that doesn't seem true -- like the model predicting the animals spend more time in yeast patches vs. other food, of course they do, because the model makes them crawl slower and pause more in yeast. It's a cool result, but it comes from your real experiments. It's just not very clear what benefit the simulations have here. I don't mean they aren't useful or you should remove them, I mean it should be much more clear what they are for:

– they are used as a check to confirm what is very strongly implied by your own experiments. If you include the modulations from crawling in isotropic substrates, and you include chemotaxis, and then the simulations match your experiments pretty closely, then you have successfully identified the important behavioral features, right? –

I like studying larva behavior and I like building simulations of larva behavior too, but something about the flow and logic of how they are deployed here feels off. I'll try to be more specific in the detailed comments.

(4) When the larvae are pausing, are they trying to eat the substrate? It seems like with third instar larvae and a pretty low % gel, they could if they wanted to.

(5) You talk about distance traveled throughout the paper, but I don't think mention displacement. Wouldn't that be important for describing motion too? Like the animals diffusing away from their start point vs. traveling a lot of distance, these aren't quite the same thing when exploring an environment for food. In particular, when you mention reduced turn and increased pause rate -- don't these do opposite things? Turning less frequently means the animals leave a space faster and the higher pause rate keeps them there longer right? They are often mentioned together in the paper, with the net effect being that larvae spend longer times in such regions, and I trust that's true, but that's because the pausing rate (and duration of pauses) carries more weight in this case?

(6) Does what the larvae do in between turns (or pauses) matter? The simulations draw them as straight lines, but don't larvae drift towards preferable odors? (I could be remembering that wrong, but I think I saw that in a Louis lab paper at some point).

(7) Is there a reason the simulations are never referred to as Monte Carlo simulations, or as (modified) random walks? Those are two pretty important reference points, especially for a general audience I think?

More detailed comments:

(1) line 26: what does "permanence time" mean? The time they spend in the patches?

(2) line 35: "all living organisms need to explore their surroundings…" That doesn't sound true. Not all living organisms even move. And some animals in the ocean just sit around and let food come to them.

(3) line 53: "gradients of light" --> "gradients of light intensity"? (light has a lot of properties).

(4) line 53: the paper used as a thermotaxis reference isn't really a thermotaxis paper, if you want one from the same group I would choose Luo, Gershow, et al. 2010, J. Neurosci. (For the record, I am an author on the one you already cite, not on the one I'm suggesting you add).

(5) line 94-95. This sentence is hard for me to understand.

(6) line 95-98. This is stated several times (basis for neuronal circuits), but is it explained why this is true? (in the Discussion section?)

(7) line 103-104. This section title maybe needs a comma and "pauses frequency" should say something else?

(8) line 113. 50 minutes seems like a long time for these experiments. If I'm back-of-the-enveloping something moving a 1 mm/s, turning every 20 s… wouldn't they leave the arena a lot faster than that? Does the arena have walls? Do their pauses last a really long time on average?

(9) Figure 1.

In 1B. Could the pauses be marked too? Maybe with open/empty circles instead of a solid/filled one? The pausing seems so important in this paper, it seems weird to leave it out.

In 1A, could there be labels for the camera and the red thing (the IR filter?).

In 1B (this figure and others), I think you mean 3pi/2 for the lower quadrant in the turn angle distributions, not 2pi/3?

Also, I don't think you need the same scale bar three times for the three panels.

Could it maybe be more clear that 1F is kind of a summary/consequence of C/D/E? It's kind of the main summary statistic here.

Some of the panels have four * symbols, but the p-value for that is not given in the caption (this figure and others).

1D: (here and elsewhere) when the turning rate is calculated, I get that turns in just the number of turns, but what's in the denominator? The actual time elapsed, or only the time during forward crawling (i.e., the total time when they are could start a turn, excluding when they are already turning or paused).

Maybe the panels and overall figure could be a bit larger? It's a little hard to read at this size.

(10) line 156. would it make sense to do a significance test for your strong handedness? The very long experiments help you here because you measure a lot of turns for individuals, but presumably, a 50/50 binomial distribution of turns would yield some "strong handedness" animals too right?

(11) line 164-167. Are you sure about that? Your data in S1F might turn out to be significant with more data taken? Similarly for the yeast substrate in Figure S1B (mentioned in line 223). I would hesitate with claims about non-significance when comparing a pretty small number of larvae.

(12) Figure 2

Why would only 30 larvae be simulated? It's a simulation, you can simulate millions of them if you wanted?

(13) Line 226ff. This is where the simulation logic seems weird to me. Maybe the order of the sections in the paper throws it off. This section laid out a simulation method, then ran simulations with patches of food substrates. But at this point you know the simulation is missing chemotaxis, and you know that real animals can smell things and move towards/away from them. I'm not sure what the point is of setting this up and then "testing the predictions of the model" with your (very cool) food patch experiments. Similarly in line 281ff, saying "the model predicted" that larvae spend more time in certain substates, doesn't feel like the right statement, because the model is only telling you what you directly put in yourself. This part is written as if the model is helping you figure out what's going on, but that doesn't seem true in this part. I think it might be better to put the simulation stuff after you have looked at the experimental patch data, then build up its capabilities if you want, or just include chemotaxis right away. The in between thing with only using the isotropic data kind of feels like a waste of time in this paper, and really interrupts the flow of some really interesting experimental results.

(14) line 232-233. Also, an oddly phrased section heading.

(15) line 237. What is the reason for apple juice showing up here suddenly? The other substances seem more fundamental -- what chemicals are in apple juice that makes it attractive? Why weren't there isotropic experiments done with an apple juice substrate?

(16) Figure 3.

3B, could this have a legend that says what the white and black circles are? (I know it's in the caption, but it would help to put it in both places).

3I. Could this be drawn more clearly with labels? (the part defining the angles). To understand what you are doing here I had to read the methods section, draw my own picture, then go look up the Tao reference (which has a better picture). Also, a general issue/concern with this definition of "towards the center". Wouldn't there be many circumstances where either a right or a left turn (of the same size) would point the animal more towards the center? Is the rate that the larvae turn different as they crawl away from a food source? Would anything change if you defined "towards the center" as the larva picking the direction that points them more toward the center than the other direction? It seems like some crawling directions would have more crucial turning decisions in them, like crawling perpendicular to the vector from food patch center (matters the most) vs. crawling parallel (directly away from the food, doesn't matter which way you turn). Pooling the turn decisions into those subsets (like you do with distance away) might make the effect more pronounced.

(17) line 300. I think you mean J instead of B?

(18) line 304. Why is this surprising? Larvae can smell, you cited a bunch of papers earlier that show this in detail.

(19) line 329 + Figure 4 -- again, a claim about non-significance with a small data set is maybe not be warranted.

(20) line 384. "Therefore…" Again, this implies the simulation result is telling you something, but you already knew this before simulating, based on the real anosmic data.

(21) line 390-392, this seems like a really interesting idea -- could this be expanded/discussed further in the discussion part of the paper?

(22) line 426ff. I think it would help to more clearly state which simulation results are obvious based on what you put in the simulation, and which gives you something unexpected.

(23) line 480-482. Here too, larvae spending less time in less nutritious patches, isn't that a direct result of putting your empirical result into the simulation? They crawl faster and pause less, doesn't this have to be true?

(24) line 636: is that hours after egg laying or after eclosion?

(25) line 641ff: I don't quite follow -- you are choosing a lower frame rate in order to prioritize spatial resolution because the camera doesn't run faster when recording at 2048x2048?

(26) line 690: when is instantaneous turn rate used? You are generally finding the total for long trajectories right?

(27) line 695: What is the distance dimension parameter? Could you briefly explain what it means?

(28) line 699: typo with the brackets vs. parentheses.
