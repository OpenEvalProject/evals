# Peer review - Round 1

Editors:
- Caleb Kemere, https://ror.org/008zs3103 Rice University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.84296.sa0](https://doi.org/10.7554/eLife.84296.sa0)

This paper reports a new way to deal with the drift of neural signals and representations over time in a BCI. Given the context of the rapidly advancing field, the reviewers assessed the findings to be useful and potentially valuable. With the code provided for other investigators to use, the strength of evidence was convincing.


---

# Peer review - Round 1

Editors:
- Caleb Kemere, https://ror.org/008zs3103 Rice University United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.84296.sa1](https://doi.org/10.7554/eLife.84296.sa1)

Our editorial process produces two outputs: (i) public reviews designed to be posted alongside the preprint for the benefit of readers; (ii) feedback on the manuscript for the authors, including requests for revisions, shown below. We also include an acceptance summary that explains what the editors found interesting or important about the work.

Decision letter after peer review:

Thank you for submitting your article "Using adversarial networks to extend brain computer interface decoding accuracy over time" for consideration by eLife. Your article has been reviewed by 2 peer reviewers, including Caleb Kemere as the Reviewing Editor and Reviewer #1, and the evaluation has been overseen by Joshua Gold as the Senior Editor.

The reviewers have discussed their reviews with one another, and the Reviewing Editor has drafted this to help you prepare a revised submission.

Essential revisions:

1) Recognizing that it may seem unfair given the length of time that your work has been in review, for the general eLife audience, the reviewers felt that it was required was to address the performance of the NoMAD approach (https://www.biorxiv.org/content/10.1101/2022.04.06.487388v1). Ideally, this would be a direct comparison. More generally, it would be valuable to discuss the relative merits of alignment approaches based only on the moment-by-moment cofiring of neurons (e.g., CycleGAN) versus alignment approaches which further leverage the dynamics in the latent space.

Reviewer #2 (Recommendations for the authors):

In this paper, Ma et al. tackle the problem of how to allow intracortical BCIs to sustain a high level of performance when there is changes in the neural signals recorded from the array and the behavior of the monkey. Such changes could be due to changes in signal quality, the tuning of the neurons, turnover of recorded neurons etc. In an ideal world, for patients using this day in and day out, there would be a quick approach to understand what the current state of the decoder is and quickly and readily adapt to the current setting so that the patient sees no drop in performance. This is a somewhat well studied question and barring older work, Stavisky, Sussillo et al. 2016 proposed a solution to this problem by using multiplicative recurrent neural networks (RNNs) that can select the best decoder given the neural data by learning from many different samples. The Miller lab in 2018 proposed using GANs to solve this problem, and again in collaboration with Dr. Pandarinath's lab has developed an approach using LFADS (called NOMAD, Karpowicz et al. 2022) to solve this problem. Here they use a different type of GAN to solve this problem. The paper is well structured, reasonably clear, the datasets are impressive and the authors have applied their approach to these datasets and compared to an approach which is based on factor analysis.

However, currently I am unsure the degree of advance provided by this paper. In particular, given that two of the datasets studied in this paper (Monkey J and Monkey C center out reach) are also present in the Karpowicz et al. 2022 paper, we need to rigorously compare both of them. The improvement from the ADAN approach seems somewhat minor in my opinion.

1. I find the results only modestly improve over their own existing approach (ADAN) and yes it does better than a simple factor analysis based method but that is simply stated as a powerful neural network is way better than a simple set of linear operations. I mean this is a little bit like a sprint race between me and Usain Bolt, there is just no contest there.

2. The related issue is that they are at best proposing a minor improvement over their own Cycle-GAN study. More worryingly, their approach does not seem to be better than the NoMAD Study from Karpowicz et al. 2022? I am all for many different approaches, but I am tad worried that there is just minimal improvement over and above their previous approach. It also feels like we are not performing a fair comparison to the state of the art, which some subset of authors in this paper has worked on! I think at a minimum they need to run NoMAD on the same datasets with whatever binsizes they choose and show that their method is comparable. I say this from the perspective that these are all offline decoding analyses and yes it is computationally expensive but does not need new experiments. In fact NoMAD runs better on this dataset with a 20 ms bin compared to a 50 ms bin.

Karpowicz et al. 2022 (bioRxiv), shares considerable author overlap with Ma et al. 2022

(Xuan Ma, Lee Miller)

The reference for this is totally mangled btw.

3. Why do I say this. Any reader who is aware of NoMAD would be like this is a strawman comparison. I think putting all of these methods on equal footing is necessary to move the field forward! I hope the authors don't feel like this is unreasonable. In addition it is the same data from I think a rockstar monkey J (95 days of data, similar task etc). Monkey J is also used in the NoMAD paper. So same dataset, multiple papers and two to three different methods :)! Figure 3 at a minimum needs a plot of the NoMAD results.

4. Of interest would be to discuss the number of parameters in each of these approaches. If the authors want, it might make sense to show how long it takes for PAF, ADAN, Cycle-GAN and NoMAD and this could be a supplementary figure. Maybe NoMAD will need way more training trials. It looks like PAF should have minimal parameters but Cycle-GAN is at least 2x as expressive as ADAN.

5. There is a theoretical point here. The GANs are trying to make the data indistinguishable from one another but as the neural data analysis shows the principal angle is still pretty substantial for 10 dimensions (~50 degrees). This will hurt their decoders. This might be an inherent disadvantage of GANs because they will likely stop once the data look like they are similar to the original distribution. But what you want is ideally something that adjusts the Day-k data to be near identical to the Day-0 data, in which case methods that maximize alignment might be a better approach. This should be discussed in the manuscript.

6. A weakness of all of these studies is that it is all done offline, what approach wins best online is an open question. Of note Stavisky, Sussillo et al. worked online. This should be a caveat in the discussion of these studies as it is an open question which of these approaches will be most successful online.

[Editors' note: further revisions were suggested prior to acceptance, as described below.]

Thank you for resubmitting your work entitled "Using adversarial networks to extend brain computer interface decoding accuracy over time" for further consideration by eLife. Your response and revised article has been evaluated by Joshua Gold (Senior Editor) and a Reviewing Editor as well as the original reviewers.

The reviewers appreciated your thorough responses to their comments. However, upon discussion, there was a consensus that two important issues remain that should be addressed:

1. The comparison to NoMAD seems important enough that adding to the manuscript details from the response letter (point #3 from R2) would be useful, particularly in terms of your contention that best within-time-bin alignment is likely a valuable component of more complex systems.

2. Given that this is a Tools and Resources article, we believe that the description of the approach in Appendix 4 is still insufficient. In addition, we request code or pseudo-code that implements those algorithms in a way that a community member would be able to rapidly use them.
