# Peer review - Round 1

Editors:
- Stephen P Goffs, Howard Hughes Medical Institute, Columbia University , United States

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.03753.018](https://doi.org/10.7554/eLife.03753.018)

eLife posts the editorial decision letter and author response on a selection of the published articles (subject to the approval of the authors). An edited version of the letter sent to the authors after peer review is shown, indicating the substantive concerns or comments; minor concerns are not usually shown. Reviewers have the opportunity to discuss the decision before the letter is sent (see review process). Similarly, the author response typically shows only responses to the major concerns raised by the reviewers.

[Editors’ note: this article was originally rejected after review, but the authors were later invited to resubmit.]

Thank you for choosing to send your work entitled “Experimentally guided mathematical modeling reveals RNA virus replication principles shaping the mutation distribution” for consideration at eLife. Your full submission has been evaluated by Aviv Regev (Senior editor), a Reviewing editor, and 3 peer reviewers, and the decision was reached after discussions between the reviewers. We regret to inform you that your work will not be considered further for publication.

The three reviews are below for your consideration, with the following comments from the Reviewing editor.

This paper reports a new attempt to model viral replication, including stochastic effects from cell to cell, and pools of viral RNA that are in replicative vs. translation pools. The model fits data best with a geometric increase of RNA (no surprise) with about 5 generations occurring intracellularlly (before cell death?). The large number (ten or so) of parameters were explored by an Approximation Bayesian Computation method, not all were independent, and some having no major impact. While I cannot comment on the math, most of the assumptions of the model seem plausible and the predictions seem to fit the limited data. The model then is used to predict the distribution of mutations, with good correspondence to data.

While it seems like a useful framework has been devised, novel predictions of the model are few and far between.

I have a few issues that reflect my uncertainty about the working of the model.

1) I have a free-floating concern with identifying a cycle as a complete genome-to antigenome-to-genome cycle. How do we deal with the fact that there are many more genomes than antigenomes? In fact, this ratio is measured and predicted (Figure 3); wouldn't this be a good thing to include as a plotted output? Does one assume here that the excess of genomes are all moved out of the replication pool, while all the antigenomes are always in the pool? How do we deal with the necessary half-cycles? Some discussion of this would be helpful.

2) In the Results section, I might question the restriction that “following Nugent et al. (1999), genomes can only be packaged as they are synthesized from a negative-sense strand…”. Could we consider a more open view that any genome, new or old, could be packaged (from any pool)? Would this be compatible with the data? Was this tried?

Reviewer #1

Life history theory aims to quantify different parameters, such as time to reproduction or number of offsprings, in potential strategies in the life of organisms to maximize the number of surviving offspring. RNA viruses present a particularly simple lifestyle and their fast replication makes them particularly appropriate to test evolutionary models. The authors apply these principles to the evolution of poliovirus. This work is the collaboration between two strong groups in the area of mathematical modeling and experimental viral evolution. Of particularly interest in this work is the determination of parameters in single cell infection. For instance, the authors contrast two simple models of replication, stamping machine where the progeny is one generation away from the initial and the geometric replication model where several rounds of replication occur within a single cell. Main conclusions of this work the lifetime of viral progeny (∼5 generations) and the abundance RNA increase following an exponential pattern which allow to test different models of replication.

The mathematical model is a stochastic model a la Gillespie where the cell infection is decomposed into a set of individual steps (binding, uncoating, translation, replication complex formation, circularization, replication, packaging, strand dispersal). The model has many parameters. To infer the value of these parameters the authors use quantitative RT-PCR data of both positive-sense genomes and negative-sense, amounting to 27 measures. The stochastic approach coupled to high dimension of data and large numbers of parameters led the authors to choose an approximate Bayesian computation using as summary statistic the sum of the squared deviations of the average simulated RNA concentration.

Initially I was extremely excited about the manuscript, but I became less enthusiastic as I was reading along.

1) The model proposed discretized the infection into a set of simple steps each of this depending on a few parameters, creating a complex chain of steps. Each step has its own parameters that add complexity in addition to the challenges of stochasticity. The model fits many parameters. It would be more interesting to make some specific hypotheses to be tested experimentally beyond parameter fitting.

2) The steps follow a virology book cartoon model, but many other factors are known to be important (transport, cell factors, etc.), and it is unclear that the factors considered are the only important ones.

3) The variability among cells could be large, as reflected by recent single cell studies, and it is unclear how this variability is taken into account in these models. A critical question in this work is the cell to cell variability. In a system where there is geometric growth a progeny the mean number of viruses in a cell is not as informative as the whole distribution. One would think that the larger scale dynamics of the virus are determined by the cells producing more viruses, in particular, in a geometric growth model.

Reviewer #2

The authors have built on their previous work in poliovirus cell interaction to develop an elaborate model of intracellular replication and consequent accumulation of mutations. In combination with careful experimental analysis of replication kinetics of both plus and minus strands as well as virions at several different MOIs, they are able to establish reasonably tight ranges for the 10 or so free parameters required by their model and draw several interesting conclusions, including that intracellular replication is best fit to a branching (rather than “stamping machine”) process, that, on average, progeny of an infected cell are about 5 copying generations removed from the infecting genome, and that, therefore, the underlying mutation rate (per copying event) is about 5-fold less than estimated from single-step experiments.

Although the modeling analysis seems to me to be quite elegant, to use up-to date techniques, and to be well supported by careful experimentation, and the conclusions seem reasonable and well justified, I am not an expert in either modeling or positive-strand virus replication, so I will defer to other reviewers on these issues. That said, my major concern is that the manuscript is rather inaccessible to the general readership expected for a journal like eLife. I found it quite difficult to read and understand, and I had to go back to a virology textbook a few times. It would help a lot if Figure 2 contained more information for the general reader, such as a map of the genome indicating the names and functions of the important gene products. Also very helpful would be a summary table listing the various parameters and the steps they refer to. Overall, the reader needs to have a clearer vision of the replication cycle than is accessible from the introductory material here. As another example, the description of the necessity for “circularization” of the RNA, and the drawing in Figure 2, leave the non-expert reader with the strong impression that the circles referred to are covalently bound RNA-only structures, rather than RNA-protein complexes, as the authors have nicely shown in previous work.

Although the stated goal of the analysis is to understand how the replication mode shapes the mutation distribution, the treatment of mutations seems rather lightweight, by comparison to replication dynamics, and also has confusing aspects. For starters, in most modeling I am accustomed to, μ is used to refer to the mutation rate, and s the selection coefficient. The use of different notation here made reading more difficult, for sure. Second, the use of a “one size fits all” approach to mutations seems oversimplified and inaccurate, because the kinetics of accumulation of different types of mutants will depend very strongly on how and where they act, whether in cis or trans to the genome, whether they affect one protein (e.g. missense mutations) or others (nonsense mutations), etc. If and how the authors included these issues in their simulations is not made clear. Obviously, there must be accumulation of some mutations that would be lethal in clonal replication, but not others, so the meaning of “replication deficit” is quite unclear.

Reviewer #3

Schulte et al. present a detailed analysis of the replication process of polio virus inside a cell. They develop a stochastic model of viral replication, fit it to empirical data via Approximate Bayesian Computation (ABC), and infer several parameters of interest. Most importantly, they show that polio virus does not replicate using the stamping-machine mechanism. Instead, there are intermediate rounds of replication inside the cell.

Overall, the paper is interesting, and the authors have a wealth of novel results. However, the presentation of the work is lacking at places, and the paper will require substantial revisions before it is publishable.

Most importantly, I feel the authors can't entirely decide on what their story is. Is the main motivation to identify the replication mode of the virus, or to show that a stochastic model is better than a deterministic model? At places, the paper seems to argue strongly for stochastic over deterministic treatment, but in the end there isn't a single result I could see that would demonstrate how a deterministic approach fails. I think it would be better to focus on the biological question (method of replication mode) and not worry so much about justifying the stochastic approach.

Secondly, the computational methods are not that well described. Notably, the methods section talks only about experimental work. Yet the main body of the text is not sufficient to fully understand the computational work, and some paragraphs currently in the Results would be better placed in the Materials and methods (see below). Also, the code and raw data for this project need to be made available.

Other comments:

I couldn't always figure out what parts of the work were simulation and what parts were fitting of the model to measured data. This needs to be worked out more clearly. Also, it would be good to have a table that lists the final parameter estimates obtained from fitting the model to the data.

It would be good to add a step of model verification where you simulate the model given some parameter set, and then see whether you can recover the parameters using the ABC method. In particular, can you distinguish SM and GR scenarios when all other parameters are the same?

In the Introduction: I would argue that if a deterministic model agrees well with measured data then that is sufficient evidence to conclude the stochastic fluctuations can be neglected.

In the Results: The modified Gillespie algorithm needs to be explained in detail in the Materials and methods section. For example, what is the threshold parameter at which you switch from stochastic to deterministic treatment? Also, the code needs to be made available.

In the Results, “we also assume that poliovirus genomes, and not cellular factors, are rate-limiting”: it is not clear to me to what extent this assumption biases results. Certainly, eventually cellular factors will be limiting viral replication inside a cell. So how does your model take this into account?

In the Results, “inferring based on mean of a larger number of replicates (n ≥ 1000) tended to select parameter sets with highly variable behavior. Reducing n led to a higher rate of parameter set rejection but more biologically plausible dynamics”: any idea why your results depend on n in this way?

Figure 1: Where does the number of 2.33 come from for GR? I doubt it is part of the definition for GR, but the sentence is written as if it were.
