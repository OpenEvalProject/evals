# The interpretation of computational model parameters depends on the context

## Authors

- Maria Katharina Eckstein<sup>1</sup> ([ORCID: 0000-0002-0330-9367](https://orcid.org/0000-0002-0330-9367)) †
- Sarah L Master<sup>1</sup> ([ORCID: 0000-0003-2726-4586](https://orcid.org/0000-0003-2726-4586))
- Liyu Xia<sup>1</sup>
- Ronald E Dahl<sup>4</sup> ([ORCID: 0000-0002-1794-7132](https://orcid.org/0000-0002-1794-7132))
- Linda Wilbrecht<sup>1</sup> ([ORCID: 0000-0003-3492-8141](https://orcid.org/0000-0003-3492-8141))
- Anne GE Collins<sup>1</sup> ([ORCID: 0000-0003-3751-3662](https://orcid.org/0000-0003-3751-3662))

### Affiliations

1. Department of Psychology, University of California, Berkeley Berkeley United States ([ROR:01an7q238](https://ror.org/01an7q238))
2. Department of Psychology, New York University New York United States ([ROR:0190ak572](https://ror.org/0190ak572))
3. Department of Mathematics, University of California, Berkeley Berkeley United States ([ROR:01an7q238](https://ror.org/01an7q238))
4. Institute of Human Development, University of California, Berkeley Berkeley United States ([ROR:01an7q238](https://ror.org/01an7q238))
5. Helen Wills Neuroscience Institute, University of California, Berkeley Berkeley United States ([ROR:01an7q238](https://ror.org/01an7q238))

† Corresponding author

## Abstract

Reinforcement Learning (RL) models have revolutionized the cognitive and brain sciences, promising to explain behavior from simple conditioning to complex problem solving, to shed light on developmental and individual differences, and to anchor cognitive processes in specific brain mechanisms. However, the RL literature increasingly reveals contradictory results, which might cast doubt on these claims. We hypothesized that many contradictions arise from two commonly-held assumptions about computational model parameters that are actually often invalid: That parameters generalize between contexts (e.g. tasks, models) and that they capture interpretable (i.e. unique, distinctive) neurocognitive processes. To test this, we asked 291 participants aged 8–30 years to complete three learning tasks in one experimental session, and fitted RL models to each. We found that some parameters (exploration / decision noise) showed significant generalization: they followed similar developmental trajectories, and were reciprocally predictive between tasks. Still, generalization was significantly below the methodological ceiling. Furthermore, other parameters (learning rates, forgetting) did not show evidence of generalization, and sometimes even opposite developmental trajectories. Interpretability was low for all parameters. We conclude that the systematic study of context factors (e.g. reward stochasticity; task volatility) will be necessary to enhance the generalizability and interpretability of computational cognitive models.

## Introduction

In recent decades, cognitive neuroscience has made breakthroughs in computational modeling, demonstrating that reinforcement learning (RL) models can explain foundational aspects of human thought and behavior. RL models can explain not only simple cognitive processes such as stimulus-outcome and stimulus-response learning (Schultz et al., 1997; O’Doherty et al., 2004; Gläscher et al., 2009), but also highly complex processes, including goal-directed, temporally extended behavior (Ribas-Fernandes et al., 2011; Daw et al., 2011), meta-learning (Wang et al., 2018), and abstract problem solving requiring hierarchical thinking (Eckstein and Collins, 2020; Botvinick, 2012; Collins and Koechlin, 2012; Werchan et al., 2016). Underlining their centrality in the study of human cognition, RL models have been applied across the lifespan (van den Bos et al., 2018; Bolenz et al., 2017; Nussenbaum and Hartley, 2019), and in both healthy participants and those experiencing psychiatric illness (Huys et al., 2016; Adams et al., 2016; Hauser et al., 2019; Ahn and Busemeyer, 2016; Deserno et al., 2013). RL models are of particular interest because they also promise a close link to brain function: A specialized network of brain regions, including the basal ganglia and prefrontal cortex, implement computations that mirror specific components of RL algorithms, including action values and reward prediction errors (Frank and Claus, 2006; Niv, 2009; Lee et al., 2012; O’Doherty et al., 2015; Glimcher, 2011; Garrison et al., 2013; Dayan and Niv, 2008). In sum, RL, explaining behavior ranging from simple conditioning to complex problem solving, appropriate for diverse human (and nonhuman) populations, based on a compelling theoretical foundation (Sutton and Barto, 2017), and with strong ties to brain function, has seen a surge in published studies since its introduction (Palminteri et al., 2017), and emerged as a powerful and potentially unifying modeling framework for cognitive and neural processing.

Computational modeling enables researchers to condense rich behavioral datasets into simple, falsifiable models (e.g. RL) and fitted model parameters (e.g. learning rate, decision temperature) (van den Bos et al., 2018; Palminteri et al., 2017; Daw, 2011; Wilson and Collins, 2019; Guest and Martin, 2021; Blohm et al., 2020). These models and parameters are often interpreted as a reflection of (or ‘window into’) cognitive and/or neural processes, with the ability to dissect these processes into specific, unique components, and to measure participants’ inherent characteristics along these components. For example, RL models have been praised for their ability to separate the decision making process into value updating and choice selection stages, allowing for the separate investigation of each dimension. Hereby, RL models infer person-specific parameters for each dimension (e.g. learning rate and decision noise), seemingly providing a direct measure of individuals’ inherent characteristics. Crucially, many current research practices are firmly based on these (often implicit) assumptions, which give rise to the expectation that parameters have a task- and model-independent interpretation and will seamlessly generalize between studies. However, there is growing—though indirect—evidence that these assumptions might not (or not always) be valid. The following section lays out existing evidence in favor and in opposition of model generalizability and interpretability. Building on our previous opinion piece, which—based on a review of published studies—argued that there is less evidence for model generalizability and interpretability than expected based on current research practices (Eckstein et al., 2021), this study seeks to directly address the matter empirically.

Many current research practices are implicitly based on the interpretability and generalizability of computational model parameters (despite the fact that many researchers explicitly distance themselves from them). For our purposes, we define a model variable (e.g. fitted parameter) as generalizable if it is consistent across uses, such that a person would be characterized with the same values independent of the specific model or task used to estimate the variable. Generalizability is a consequence of the assumption that parameters are intrinsic to participants rather than task dependent (e.g. a high learning rate is a personal characteristic that might reflect an individual’s unique brain structure). One example of our implicit assumptions about generalizability is the fact that we often directly compare model parameters between studies—for example, comparing our findings related to learning rate parameters to a previous study’s findings related to learning rate parameters. Note that such a comparison is only valid if parameters capture the same underlying constructs across studies, tasks, and model variations, that is, if parameters generalize. The literature has implicitly equated parameters in this way in review articles (Huys et al., 2016; Adams et al., 2016; Hauser et al., 2019; Frank and Claus, 2006; Niv, 2009; Lee et al., 2012; O’Doherty et al., 2015; Glimcher, 2011; Dayan and Niv, 2008), meta-analyses (Garrison et al., 2013; Yaple and Yu, 2019; Liu et al., 2016), and also most empirical papers, by relating parameter-specific findings across studies. We also implicitly evoke parameter generalizability when we study task-independent empirical parameter priors (Gershman, 2016), or task-independent parameter relationships (e.g. interplay between different kinds of learning rates [Harada, 2020]), because we presuppose that parameter settings are inherent to participants, rather than task specific.

We define a model variable as interpretable if it isolates specific and unique cognitive elements, and/or is implemented in separable and unique neural substrates. Interpretability follows from the assumption that the decomposition of behavior into model parameters ‘carves cognition at its joints’, and provides fundamental, meaningful, and factual components (e.g. separating value updating from decision making). We implicitly invoke interpretability when we tie model variables to neural substrates in a task-general way (e.g. reward prediction errors to dopamine function [Schultz and Dickinson, 2000]), or when we use parameters as markers of psychiatric conditions in a model-independent way (e.g. working-memory deficits in schizophrenia [Collins et al., 2014]). Interpretability is also required when we relate abstract parameters to aspects of real-world decision making (Heinz et al., 2017), and generally, when we assume that model variables are particularly ‘theoretically meaningful’ (Huys et al., 2016).

However, in the midst of the growing application of computational modeling of behavior, the focus has also shifted toward inconsistencies and apparent contradictions in the emerging literature, which are becoming apparent in cognitive (Nassar and Frank, 2016), developmental (Nussenbaum and Hartley, 2019; Javadi et al., 2014; Blakemore and Robbins, 2012; DePasque and Galván, 2017), clinical (Adams et al., 2016; Hauser et al., 2019; Ahn and Busemeyer, 2016; Deserno et al., 2013), and neuroscience studies (Garrison et al., 2013; Yaple and Yu, 2019; Liu et al., 2016; Mohebi et al., 2019), and have recently become the focus of targeted investigations (Robinson and Chase, 2017; Weidinger et al., 2019; Brown et al., 2020; Pratt et al., 2021). For example, some developmental studies have shown that learning rates increased with age (Master et al., 2020; Davidow et al., 2016), whereas others have shown that they decrease (Decker et al., 2015). Yet others have reported U-shaped trajectories with either peaks (Rosenbaum et al., 2020) or troughs (Eckstein et al., 2022) during adolescence, or stability within this age range (Palminteri et al., 2016) (for a comprehensive review, see Nussenbaum and Hartley, 2019; for specific examples, see Nassar and Frank, 2016). This is just one striking example of inconsistencies in the cognitive modeling literature, and many more exist (Eckstein et al., 2022). These inconsistencies could signify that computational modeling is fundamentally flawed or inappropriate to answer our research questions. Alternatively, inconsistencies could signify that the method is valid, but our current implementations are inappropriate (Palminteri et al., 2017; Uttal, 1990; Webb, 2001; Navarro, 2019; Yarkoni, 2020; Wilson and Collins, 2019). However, we hypothesize that inconsistencies can also arise for a third reason: Even if both method and implementation are appropriate, inconsistencies like the ones above are expected—and not a sign of failure—if implicit assumptions of generalizability and interpretability are not always valid. For example, model parameters might be more context-dependent and less person-specific than we often appreciate (Nussenbaum and Hartley, 2019; Nassar and Frank, 2016; Yaple and Yu, 2019; Behrens et al., 2007; McGuire et al., 2014).

To illustrate this point, the current project began as an investigation into the development of learning in adolescence, with the aim of combining the insights of three different learning tasks to gain a more complete understanding of the underlying mechanisms. However, even though each task individually showed strong and interesting developmental patterns in terms of model parameters (Master et al., 2020; Eckstein et al., 2022; Xia et al., 2021), these patterns were very different—and even contradictory—across tasks. This implied that specific model parameters (e.g. learning rate) did not necessarily isolate specific cognitive processes (e.g. value updating) and consistently measure individuals on these processes, but that they captured different processes depending on the learning context of the task (lack of generalizability). In addition, the processes identified by one parameter were not necessarily distinct from the cognitive processes (e.g. decision making) identified by other parameters (e.g. decision temperature), but could overlap between parameters (lack of interpretability). In a nutshell, the ‘same’ parameters seemed to measure something different in each task.

The goal of the current project was to assess these patterns formally: We determined the degree to which parameters generalized between three different RL tasks, investigated whether parameters were interpretable as unique and specific processes, and provide initial evidence for context factors that potentially modulate generalizability and interpretability of model parameters, including feedback stochasticity, task volatility, and memory demands. To this aim, we compared the same individuals’ RL parameters, fit to different learning tasks in a single study, in a developmental dataset (291 participants, ages 8–30 years). Using a developmental dataset had several advantages: It provided large between-participant variance and hence better coverage of the parameter space, and allowed us to specifically target outstanding discrepancies in the developmental psychology literature (Nussenbaum and Hartley, 2019). The three learning tasks we used varied on several common dimensions, including feedback stochasticity, task volatility, and memory demands (Figure 1E), and have been used previously to study RL processes (Davidow et al., 2016; Collins and Frank, 2012; Javadi et al., 2014; Master et al., 2020; Eckstein et al., 2022; Xia et al., 2021). However, like many tasks in the literature, the tasks likely also engaged other cognitive processes besides RL, such as working memory and reasoning. The within-participant design of our study allowed us to test directly whether the same participants showed the same parameters across tasks (generalizability), and the combination of multiple tasks shed light on which cognitive processes the same parameters captured in each task (interpretability). We extensively compared and validated all RL models (Palminteri et al., 2017; Wilson and Collins, 2019; Lee, 2011) and have reported each task’s unique developmental results separately (Master et al., 2020; Eckstein et al., 2022; Xia et al., 2021).

![Figure 1.](https://cdn.elifesciences.org/articles/75474/elife-75474-fig1-v1.jpg)

**Figure 1.:** (A) Participant sample. Left: Number of participants in each age group, broken up by sex (self-reported). Age groups were determined by within-sex age quartiles for participants between 8–17 years (see Eckstein et al., 2022 for details) and 5 year bins for adults. Right: Number of participants whose data were excluded because they failed to reach performance criteria in at least one task. (B) Task A procedure of (‘Butterfly task’). Participants saw one of four butterflies on each trial and selected one of two flowers in response, via button press on a game controller. Each butterfly had a stable preference for one flower throughout the task, but rewards were delivered stochastically (70% for correct responses, 30% for incorrect). For details, see section 'Task design' and the original publication (Xia et al., 2021). (C) Task B Procedure (‘Stochastic Reversal’). Participants saw two boxes on each trial and selected one with the goal of finding gold coins. At each point in time, one box was correct and had a high (75%) probability of delivering a coin, whereas the other was incorrect (0%). At unpredictable intervals, the correct box switched sides. For details, see section 'Task design' and Eckstein et al., 2022. (D) Task C procedure (‘Reinforcement learning-working memory’). Participants saw one stimulus on each trial and selected one of three buttons ($A_{1}-A_{3}$) in response. All correct and no incorrect responses were rewarded. The task contained blocks of 2–5 stimuli, determining its ‘set size’. The task was designed to disentangle set size-sensitive working memory processes from set size-insensitive RL processes. For details, see section 'Task design' and Master et al., 2020. (E) Pairwise similarities in terms of experimental design between tasks A (Xia et al., 2021), B (Eckstein et al., 2022), and C (Master et al., 2020). Similarities are shown on the arrows connecting two tasks; the lack of a feature implies a difference. E.g., a ‘Stable set size’ on tasks A and B implies an unstable set size in task C. Overall, task A shared more similarities with tasks B and C than these shared with each other. (F) Summary of the computational models for each task (for details, see section 'Computational models' and original publications). Each row shows one model, columns show model parameters. ‘Y’ (yes) indicates that a parameter is present in a given model, ‘—’ indicates that a parameter is not present. ‘$\frac{1}{\beta}$ and $ϵ$’ refer to exploration / noise parameters; $\alpha_{+}$ ($\alpha_{-}$) to learning rate for positive (negative) outcomes; ‘Persist. P’ to persistence; ‘WM pars’. to working memory parameters.

Our results show a striking lack of generalizability and interpretability for some tasks and parameters, but convincing generalizability for others. This reveals an urgent need for future research to address the role of context factors in computational modeling, and reveals the necessity of taking context factors into account when interpreting and generalizing results. It also suggests that some prior discrepancies are likely explained by differences in context.

## Results

This section gives a brief overview of the experimental tasks (Figure 1B–D) and computational models (Figure 1F; also see sections 'Task Design', 'Computational Models', and 'Appendix 2'; for details, refer to original publications [Master et al., 2020; Eckstein et al., 2022; Xia et al., 2021]). We then show our main findings on parameter generalizability (section 'Part I: parameter generalizability') and interpretability (section 'Part II: parameter interpretability'). All three tasks are learning tasks and have been previously well-captured by RL models, yet with differences in parameterization (Javadi et al., 2014; Davidow et al., 2016; Collins and Frank, 2012). In our study as well, the best-fitting RL models differed between tasks, containing some parameters that were the same across tasks, and some that were task-specific (Figure 1F). Thus, our setup provides a realistic reflection of the diversity of computational models in the literature.

Task A required participants to learn the correct associations between each of four stimuli (butterflies) and two responses (flowers) based on probabilistic feedback (Figure 1B). The best-fitting model contained three free parameters: learning rate from positive outcomes $\alpha_{+}$, inverse decision temperature $\beta$, and forgetting $F$. It also contained one fixed parameter: learning rate from negative outcomes $\alpha_{-}=0$ (Xia et al., 2021). Task B required participants to adapt to unexpected switches in the action-outcome contingencies of a simple bandit task (only one of two boxes contained a gold coin at any time) based on semi-probabilistic feedback (Figure 1C). The best-fitting RL model contained four free parameters: $\alpha_{+}$, $\alpha_{-}$, $\beta$, and choice persistence $p$ (Eckstein et al., 2022). Task C required learning of stimulus-response associations like task A, but over several task blocks with varying numbers of stimuli, and using deterministic feedback (Figure 1D). The best model for this task combined RL and working memory mechanisms, containing RL parameters $\alpha_{+}$ and $\alpha_{-}$; working memory parameters capacity $K$, forgetting $F$, and noise $ϵ$; and mixture parameter $ρ$, which determined the relative weights of RL and working memory (Master et al., 2020; Collins and Frank, 2012). The Markov decision process (MDP) framework provides a common language to describe learning tasks like ours, by breaking them down into states, actions, and reward functions. Appendix 2 summarizes the tasks in this way and highlights major differences.

We employed rigorous model fitting, comparison, and validation to obtain the best-fitting models presented here (see Appendix 4 and Palminteri et al., 2017; Daw, 2011; Wilson and Collins, 2019; Lee, 2011): For each task, we compared a large number of competing models, based on different parameterizations and cognitive mechanisms, and selected the best one based on quantitative model comparison scores as well as the models’ abilities to reproduce participants’ behavior in simulation (Appendix 4—figure 1). We also used hierarchical Bayesian methods for model fitting and comparison where possible, to obtain the most accurate parameter estimates (Lee, 2011; Brown et al., 2020). Individual publications provide further details on the set of models compared and validate the claim that the models presented here are the best-fitting ones for each task (Master et al., 2020; Eckstein et al., 2022; Xia et al., 2021), an important premise for the claim that individual parameters are well estimated. This qualitative validation step for each dataset ensures that potential parameter discrepancies between tasks are not due to a lack of modeling quality, and can indeed provide accurate information about parameter generalizability and interpretability. (Though we acknowledge that no model is ever right.)

### Part I: parameter generalizability

Crucially, the parameter inconsistencies observed in previous literature could be caused by non-specific differences between studies (e.g. participant samples, testing procedures, modeling approaches, research labs). Our within-participant design allows us to rule these out by testing whether the same participants show different parameter values when assessed using different tasks; this finding would be strong evidence for the hypothesized lack of parameter generalizability. To assess this, we first determined whether participants showed similar parameter values across tasks, and then whether tasks showed similar parameter age trajectories.

#### Differences in absolute parameter values

We first used repeated-measures analyses of variance (ANOVAs) to test for task effects on absolute parameter values (Figure 2A). When ANOVAs showed significant task effects, we followed up with repeated-measures t-tests to compare each pair of tasks, using the Bonferroni correction.

![Figure 2.](https://cdn.elifesciences.org/articles/75474/elife-75474-fig2-v1.jpg)

**Figure 2.:** (A) Fitted parameters over participant age (binned) for all three tasks (A: green; B: orange; C: blue). Parameter values differed significantly between tasks; significance stars show the p-values of the main effects of task on parameters (Table 1; * $p<.05$; ** $p<.01$; *** $p<.001$). Dots indicate means of the participants in each age group (for n’s, see Figure 1A), error bars specify the confidence level (0–1) for interval estimation of the population mean. (B) Summary of the main results of part A. Double-sided arrows connecting tasks are replicated from Figure 1E and indicate task similarity (dotted arrow: small similarity; full arrow: large similarity). Lines connecting parameters between tasks show test statistics (Table 1). Dotted lines indicate significant task differences in Bonferroni-corrected pairwise t-tests (full lines would indicate the lack of difference). All t-tests were significant, indicating that absolute parameter values differed between each pair of tasks. (C) Parameter age trajectories, that is, within-task z-scored parameters over age. Age trajectories reveal similarities that are obscured by differences in means or variances in absolute values (part A). Significance stars show significant effects of task on age trajectories (Table 2). (D) Summary of the main results of part C. Lines connecting parameters between tasks show statistics of regression models predicting each parameter from the corresponding parameter in a different task (Table 4). Full lines indicate significant predictability and dotted lines indicate a lack thereof. In contrast to absolute parameter values, age trajectories were predictive in several cases, especially for tasks with more similarities (A and B; A and C), compared to tasks with fewer (B and C).

Learning rates $\alpha_{+}$ and $\alpha_{-}$ were so dissimilar across tasks that they occupied largely separate ranges: They were very low in task C ($\alpha_{+}$ mean: 0.07, sd: 0.18; $\alpha_{-}$ mean: 0.03, sd: 0.13), intermediate in task A ($\alpha_{+}$ mean: 0.22, sd: 0.09; $\alpha_{-}$ was fixed at 0), but fairly high in task B ($\alpha_{+}$ mean: 0.77, sd: 0.11; $\alpha_{-}$ mean: 0.62, sd: 0.14; for statistical comparison, see Table 1). Decision noise was high in task B ($\frac{1}{\beta}$ mean: 0.33, sd: 0.15), but low in tasks A ($\frac{1}{\beta}$ mean: 0.095, sd: 0.0087) and C ($ϵ$ mean: 0.025, sd: 0.032; statistics in Table 1 ignore $ϵ$ because its absolute values were not comparable to $\frac{1}{\beta}$ due to the different parameterization; see section 'Computational models'). Forgetting was significantly higher in task C (mean: 0.19, sd: 0.17) than A (mean: 0.056, sd: 0.028). Task B was best fit without forgetting.

**Table 1.**
 Statistics of ANOVAs predicting raw parameter values from task (A, B, C).When an ANOVA showed a significant task effect, we followed up with post-hoc, Bonferroni-corrected t-tests. * $p<.05$; ** $p<.01$; *** $p<.001$.


<table>
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Model</th>
      <th>Tasks</th>
      <th>F / t</th>
      <th>df</th>
      <th>p</th>
      <th>sig.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1β</td>
      <td>ANOVA</td>
      <td>A, B</td>
      <td>830</td>
      <td>1</td>
      <td>p&lt;0.001</td>
      <td>***</td>
    </tr>
    <tr>
      <td></td>
      <td>t-test</td>
      <td>A vs B</td>
      <td>25</td>
      <td>246</td>
      <td>p&lt;0.001</td>
      <td>***</td>
    </tr>
    <tr>
      <td>α+</td>
      <td>ANOVA</td>
      <td>A, B, C</td>
      <td>2,018</td>
      <td>2</td>
      <td>p&lt;0.001</td>
      <td>***</td>
    </tr>
    <tr>
      <td></td>
      <td>t-test</td>
      <td>A vs B</td>
      <td>66</td>
      <td>246</td>
      <td>p&lt;0.001</td>
      <td>***</td>
    </tr>
    <tr>
      <td></td>
      <td>t-test</td>
      <td>A vs C</td>
      <td>12</td>
      <td>246</td>
      <td>p&lt;0.001</td>
      <td>***</td>
    </tr>
    <tr>
      <td></td>
      <td>t-test</td>
      <td>B vs C</td>
      <td>51</td>
      <td>246</td>
      <td>p&lt;0.001</td>
      <td>***</td>
    </tr>
    <tr>
      <td>α-</td>
      <td>ANOVA</td>
      <td>B, C</td>
      <td>2,357</td>
      <td>1</td>
      <td>p&lt;0.001</td>
      <td>***</td>
    </tr>
    <tr>
      <td></td>
      <td>t-test</td>
      <td>B vs C</td>
      <td>49</td>
      <td>246</td>
      <td>p&lt;0.001</td>
      <td>***</td>
    </tr>
    <tr>
      <td>Forgetting</td>
      <td>ANOVA</td>
      <td>A, C</td>
      <td>161</td>
      <td>1</td>
      <td>p&lt;0.001</td>
      <td>***</td>
    </tr>
    <tr>
      <td></td>
      <td>t-test</td>
      <td>A vs C</td>
      <td>49</td>
      <td>246</td>
      <td>p&lt;0.001</td>
      <td>***</td>
    </tr>
  </tbody>
</table>

For all parameters, absolute parameter values hence differed substantially between tasks. This shows that the three tasks produced significantly different estimates of learning rates, decision noise/exploration, and forgetting for the same participants (Figure 2B). Interestingly, these parameter differences echoed specific task demands: Learning rates and noise/exploration were highest in task B, where frequent switches required quick updating and high levels of exploration. Similarly, forgetting was highest in task C, which posed the largest memory demands. Using regression models that controlled for age (instead of ANOVA) led to similar results (Table Appendix 8—table 2).

#### Relative parameter differences

However, comparing parameters in terms of their absolute values has shortcomings because it minimizes the role of relative variance between participants, which reflects participants’ mutual relationships to each other, and might be an important component of parameters. To test whether parameters generalized in relative, rather than absolute terms, we first correlated corresponding parameters between each pair of tasks, using Spearman correlation (Appendix 8—figure 1). Indeed, both $\alpha_{+}$ (Appendix 8—figure 1A) and noise/exploration parameters (Appendix 8—figure 1B) were significantly positively correlated between tasks A and B as well as between tasks A and C. Significant correlations were lacking between tasks B and C. This suggests that both $\alpha_{+}$ and noise/exploration generalized in terms of the relationships they captured between participants; however, this generalization was only evident between tasks A and B or A and C, potentially due to the fact that task A was more similar to tasks B and C than these were to each other (Figure 1E; also see section 'Main axes of variation'). Fig. Appendix 8—figure 3 shows the correlations between all pairs of features in the dataset (model parameters and behavioral measures). Note that noise parameters generalized between tasks A and C despite differences in parameterization ($ϵ$ vs. $1/\beta$), showing robustness in the characterization of choice stochasticity (Appendix 8—figure 1B).

#### Parameter age trajectories

This correlation analysis, however, is limited in its failure to account for age, an evident source of variance in our dataset. This means that apparent parameter generalization could be driven by a common dependence on age, rather than underlying age-independent similarities. To address this, we next focused on parameter age trajectories, aiming to remove differences between tasks that are potentially arbitrary (e.g. absolute mean and variance), while conserving patterns that are potentially more meaningful (e.g. shape of variance, i.e. participants’ values relative to each other). Age trajectories were calculated by z-scoring each parameter within each task (Figure 2C). To test for differences, mixed-effects regression was used to predict parameters of all tasks from two age predictors (age and squared age) and task (A, B, or C). A better fit of this model compared to the corresponding one without task indicates that task characteristics affected age trajectories. In this case, we followed up with post-hoc models comparing individual pairs of tasks.

For $\alpha_{-}$, the task-based regression model showed a significantly better fit, revealing an effect of task on $\alpha_{-}$’s age trajectory (Table 2). Indeed, $\alpha_{-}$ showed fundamentally different trajectories in task B compared to C (in task A, $\alpha_{-}$ was fixed): In task B, $\alpha_{-}$ decreased linearly, modulated by a U-shaped curvature (linear effect of age: $\beta=-0.11$, $p<0.001$; quadratic: $\beta=0.003$, $p<0.001$), but in task C, it increased linearly, modulated by an inverse-U curvature (linear: $\beta=0.32$, $p<0.001$; quadratic: $\beta=-0.07$, $p<0.001$; Figure 2C). The fact that these patterns are opposites of each other was reflected in the significant interaction terms of the overall regression model (Table 3). Indeed, we previously reported a U-shaped trajectory of $\alpha_{-}$ in task B, showing a minimum around age 13–15 (Eckstein et al., 2022), but a consistent increase up to early adulthood in task C (Xia et al., 2021). This shows striking differences when estimating $\alpha_{-}$ using task B compared to C. These differences might reflect differences in task demands: Negative feedback was diagnostic in task C, requiring large learning rates from negative feedback $\alpha_{-}$ for optimal performance, whereas negative feedback was not diagnostic in task B, requiring small $\alpha_{-}$ for optimal performance.

**Table 2.**
 Assessing task effects on parameter age trajectories.Model fits (AIC scores) of regression models predicting parameter age trajectories, comparing the added value of including (‘AIC with task’) versus excluding (‘AIC without task’) task as a predictor. Differences in AIC scores were tested statistically using F-tests. Better (smaller) model fits are highlighted in bold. The coefficients of the winning models (simpler model ‘without task’ unless adding task predictor leads to significantly better model fit) are shown in Table 3.


<table>
  <thead>
    <tr>
      <th>Parameter</th>
      <th>AIC without task</th>
      <th>AIC with task</th>
      <th>F(df)</th>
      <th>p</th>
      <th>sig.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1β/ϵ</td>
      <td>2,044</td>
      <td>2,054</td>
      <td>NA</td>
      <td>NA</td>
      <td>–</td>
    </tr>
    <tr>
      <td>α+</td>
      <td>2,044</td>
      <td>2,042</td>
      <td>F⁢(4,245)=2.34</td>
      <td>p=0.056</td>
      <td>–</td>
    </tr>
    <tr>
      <td>α-</td>
      <td>1,395</td>
      <td>1,373</td>
      <td>F⁢(2,245)=6.99</td>
      <td>p=0.0011</td>
      <td>**</td>
    </tr>
    <tr>
      <td>Forgetting</td>
      <td>1,406</td>
      <td>1,411</td>
      <td>NA</td>
      <td>NA</td>
      <td>–</td>
    </tr>
  </tbody>
</table>

**Table 3.**
 Statistical tests on age trajectories: mixed-effects regression models predicting z-scored parameter values from task (A, B, C), age, and squared age (months).When the task-less model fitted best, the coefficients of this (‘grand’) model are shown, reflecting shared age trajectories (Table 2; $\frac{1}{\beta}/ϵ$, $\alpha_{+}$, forgetting). When the age-based model fitted better, pairwise follow-up models are shown ($\alpha_{-}$), reflecting task differences. p-Values of follow-up models were corrected for multiple comparison using the Bonferroni correction. * $p<.05$; ** $p<.01$, *** $p<.001$.


<table>
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Tasks</th>
      <th>Predictor</th>
      <th>β</th>
      <th>p(Bonf.)</th>
      <th>sig.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1β/ϵ</td>
      <td>A, B, C</td>
      <td>Intercept</td>
      <td>1.86</td>
      <td>&lt;0.001</td>
      <td>***</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Age (linear)</td>
      <td>–0.17</td>
      <td>0.003</td>
      <td>**</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Age (quadratic)</td>
      <td>0.004</td>
      <td>&lt;0.001</td>
      <td>***</td>
    </tr>
    <tr>
      <td>α+</td>
      <td>A, B, C</td>
      <td>Intercept</td>
      <td>–2.10</td>
      <td>&lt;0.001</td>
      <td>***</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Age (linear)</td>
      <td>0.20</td>
      <td>&lt;0.001</td>
      <td>***</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Age (quadratic)</td>
      <td>–0.004</td>
      <td>&lt;0.001</td>
      <td>***</td>
    </tr>
    <tr>
      <td>α-</td>
      <td>B, C</td>
      <td>Task (main effect)</td>
      <td>4.15</td>
      <td>&lt;0.001</td>
      <td>***</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Task * linear age (interaction)</td>
      <td>0.43</td>
      <td>&lt;0.001</td>
      <td>***</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Task * quadratic age (interaction)</td>
      <td>–0.010</td>
      <td>&lt;0.001</td>
      <td>***</td>
    </tr>
    <tr>
      <td>Forgetting</td>
      <td>A, C</td>
      <td>Intercept</td>
      <td>0.37</td>
      <td>0.44</td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Age (linear)</td>
      <td>–0.034</td>
      <td>0.53</td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>Age (quadratic)</td>
      <td>0.001</td>
      <td>0.63</td>
      <td></td>
    </tr>
  </tbody>
</table>

For $\alpha_{+}$, adding task as a predictor did not improve model fit, suggesting that $\alpha_{+}$ showed similar age trajectories across tasks (Table 2). Indeed, $\alpha_{+}$ showed a linear increase that tapered off with age in all tasks (linear increase: task A: $\beta=0.33$, $p<0.001$; task B: $\beta=0.052$, $p<0.001$; task C: $\beta=0.28$, $p<0.001$; quadratic modulation: task A: $\beta=-0.007$, $p<0.001$; task B: $\beta=-0.001$, $p<0.001$; task C: $\beta=-0.006$, $p<0.001$). For noise/exploration and forgetting parameters, adding task as a predictor also did not improve model fit (Table 2), suggesting similar age trajectories across tasks. For decision noise/exploration, the grand model revealed a linear decrease and tapering off with age (Figure 2C; Table 3), in accordance with previous findings (Nussenbaum and Hartley, 2019). For forgetting, the grand model did not reveal any age effects (Figure 2C; Table 3), suggesting inconsistent or lacking developmental changes.

In summary, $\alpha_{-}$ showed different age trajectories depending on the task. This suggests a lack of generalizability: The estimated developmental trajectories of learning rates for negative outcomes might not generalize between experimental paradigms. However, the age trajectories of noise/exploration parameters, $\alpha_{+}$, and forgetting did not differ between tasks. This lack of statistically-significant task differences might indicate parameter generalizability—but it could also reflect high levels of parameter estimation noise. Subsequent sections will disentangle these two possibilities.

#### Predicting age trajectories

The previous analysis, focusing on parameter differences, revealed some lack of generalization (e.g. $\alpha_{-}$). The next analysis takes the inverse approach, assessing similarities in an effort to provide evidence for generalization: We used linear regression to predict participants’ parameters in one task from the corresponding parameter on another task, controlling for age and squared age.

For both $\alpha_{+}$ and noise/exploration parameters, task A predicted tasks B and C, and tasks B and C predicted task A, but tasks B and C did not predict each other (Table 4; Figure 2D), reminiscent of the correlation results (section 'Relative parameter differences'). For $\alpha_{-}$, tasks B and C showed a marginally significant negative relationship (Table 4), suggesting that predicting $\alpha_{-}$ between tasks can lead to systematically biased predictions, confirming the striking differences observed before (section 'Parameter age trajectories'). For forgetting, tasks A and C were not predictive of each other (Table 4), suggesting that the lack of significant differences we observed previously (Table 3) did not necessarily imply successful generalization, but might have been caused by other factors, for example, elevated noise.

**Table 4.**
 Statistics of the regression models predicting each parameter from the corresponding parameter in a different task, while controlling for age.Results were identical when predicting task A from B and task B from A, for all pairs of tasks. Therefore, only one set of results is shown, and predictor and outcome task are not differentiated. Stars indicate significance as before; ‘$’ indicates $p<0.1$.


<table>
  <thead>
    <tr>
      <th>Parameter</th>
      <th>Tasks</th>
      <th>β</th>
      <th>p</th>
      <th>sig.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1β, ϵ</td>
      <td>A &amp; B</td>
      <td>0.28</td>
      <td></td>
      <td>***</td>
    </tr>
    <tr>
      <td></td>
      <td>A &amp; C</td>
      <td>0.19</td>
      <td>0.0022</td>
      <td>**</td>
    </tr>
    <tr>
      <td></td>
      <td>B &amp; C</td>
      <td>0.039</td>
      <td>0.54</td>
      <td></td>
    </tr>
    <tr>
      <td>α+</td>
      <td>A &amp; B</td>
      <td>0.13</td>
      <td>0.035</td>
      <td>*</td>
    </tr>
    <tr>
      <td></td>
      <td>A &amp; C</td>
      <td>0.23</td>
      <td></td>
      <td>***</td>
    </tr>
    <tr>
      <td></td>
      <td>B &amp; C</td>
      <td>–0.073</td>
      <td>0.25</td>
      <td></td>
    </tr>
    <tr>
      <td>α-</td>
      <td>B &amp; C</td>
      <td>–0.12</td>
      <td>0.058</td>
      <td>$</td>
    </tr>
    <tr>
      <td>Forgetting</td>
      <td>A &amp; C</td>
      <td>0.097</td>
      <td>0.13</td>
      <td></td>
    </tr>
  </tbody>
</table>

#### Statistical comparison to generalizability ceiling

Our analyses so far suggest that some parameters did not generalize between tasks: We observed differences in age trajectories (section 'Parameter age trajectories') and a lack of mutual prediction (section 'Predicting age trajectories'). However, the lack of correspondence could also arise due to other factors, including behavioral noise, noise in parameter fitting, and parameter trade-offs within tasks. To rule these out, we next established the ceiling of generalizability attainable using our method.

We established the ceiling in the following way: We first created a dataset with perfect generalizability, simulating behavior from agents that use the same parameters across all tasks (Appendix 5—figure 1). We then fitted this dataset in the same way as the human dataset (e.g. using the same models), and performed the same analyses on the fitted parameters, including an assessment of age trajectories (Appendix 5—table 1) and prediction between tasks (Appendix 5—table 2, Appendix 5—table 3, and Appendix 5—table 4). These results provide the practical ceiling of generalizability, given the limitations of our data and modeling approach. We then compared the human results to this ceiling to ensure that the apparent lack of generalization was a valid conclusion, rather than stemming from methodological constraints: If the empirical human dataset is significantly below ceiling, we can conclude a lack of generalization, but if it is not significantly different from the expected ceiling, our approach might lack validity.

The results of this analysis support our conclusions. Specifically, whereas humans had shown divergent trajectories for parameter $\alpha_{-}$ (Figure 2B; Table 1), the simulated agents (that used the same parameters for all tasks) did not show task differences for $\alpha_{-}$ or any other parameter (Appendix 5—figure 1B, Appendix 5—table 1), even when controlling for age (Appendix 5—table 2, Appendix 5—table 3). Furthermore, the same parameters were predictive between tasks in all cases (Appendix 5—table 4). These results show that our method reliably detected parameter generalization in a dataset that exhibited generalization.

Lastly, we established whether the degree of generalization in humans was significantly different from agents. To this aim, we calculated the Spearman correlations between each pair of tasks for each parameter, for both humans (section 'Relative parameter differences'; Appendix 8—figure 1) and agents, and then compared humans and agents using bootstrapped confidence intervals (Appendix 5). Human parameter correlations were significantly below the ceiling for most parameters (exceptions: $\alpha_{+}$ in A vs B; $ϵ$ / $\frac{1}{\beta}$ in A vs C; Appendix 5—figure 1C). This suggests that the human sample showed less-than-perfect generalization for most task combinations and most parameters: Generalization was lower than in agents for parameters forgetting, $\alpha_{-}$, $\alpha_{+}$ (in two of three task combinations), and $ϵ$ / $\frac{1}{\beta}$ (in two of three task combinations).

#### Summary part I: Generalizability

So far, no parameter has shown generalization between tasks in terms of absolute values (Figure 2A and B), but noise/exploration and $\alpha_{+}$ showed similar age trajectories (Figure 2C), at least in tasks that were sufficiently similar (Figure 2D). To summarize, (1) all parameters differed significantly between tasks in terms of absolute values (Figure 2A and B). Intriguingly, absolute parameter values varied more between tasks than between participants within tasks, suggesting that task demands played a larger role in determining parameter values than participants’ individual characteristics. This was the case for all four model parameters (Noise/Exploration, $\alpha_{+}$, $\alpha_{-}$, and Forgetting). (2) However, there was evidence that in some cases, parameter age trajectories generalized between tasks: Task identity did not affect the age trajectories of noise/exploration, forgetting, or learning rate $\alpha_{+}$ (Figure 2C), suggesting possible generalization. However, only noise/exploration and $\alpha_{+}$ age trajectories were the same between tasks, hence revealing deeper similarities, and this was only possible when tasks were sufficiently similar (Table 4), highlighting the limits of generalization. No generalization was possible for $\alpha_{-}$, whose age trajectory differed both qualitatively and quantitatively between tasks, showing striking inverse patterns. Like for absolute parameter values, differences in parameter age trajectories were likely caused by differences in task demands. (3) Parameter $\alpha_{+}$ reached ceiling generalizability between tasks A and B, and parameter $ϵ$ / $\frac{1}{\beta}$ between tasks A and C. Generalizability of all other task combinations and parameters was significantly lower than expected from a perfectly-generalizing population. (4) For the parameters whose age trajectories showed signs of generalization, our results replicated patterns in the literature, with noise/exploration decreasing and $\alpha_{+}$ increasing from childhood to early adulthood (Nussenbaum and Hartley, 2019).

### Part II: Parameter interpretability

To address the second assumption identified above, Part II focuses on parameter interpretability, testing whether parameters captured specific, unique, and meaningful cognitive processes. To this end, we first investigated the relations between different parameters to assess whether individual parameters were uniquely interpretable (i.e. specific and distinct from each other). We then determined how parameters were related to observed behavior, seeking evidence for external interpretability.

#### Main axes of variation

To build a foundation for parameter interpretation, we first aimed to understand which cognitive processes and aspects of participant behavior were captured by each parameter. We opted for a data-driven approach, interpreting parameters based on the major axes of variance that emerged in our large dataset, identified without a priori hypotheses. Concretely, we used PCA to identify the principal components (PCs) of our joint dataset of behavioral features and model parameters (Abdi and Williams, 2010). We first gained a thorough understanding of these PCs, and then employed them to better understand what was captured by model parameters. Detailed information on our approach is provided in sections 'Principal component analysis (PCA)' (PCA methods), 'Appendix 6' (behavioral features), and Appendix 8—figure 4 (additional PCA results).

We first analyzed PC1, the axis of largest variation and main source of individual differences in our dataset (25.1% of explained variance; Appendix 8—figure 4A). We found that behaviors that indicated good task participation (e.g. higher percentage of correct choices) loaded positively on PC1, whereas behaviors that indicated poor participation loaded negatively (e.g. more missed trials, longer response times; Figure 3A). This was the case for performance measures in the narrow sense of maximizing choice accuracy (e.g. percentage correct choices, trials to criterion, proportion of win-stay choices), but also in the wider sense of reflecting task engagement (e.g. number of missed trials, response times, response time variability). PC1 therefore captured a range of ‘good’, task-engaged behaviors, and is likely similar to the construct of ‘decision acuity’ (Moutoussis et al., 2021): Decision acuity was recently identified as the first component of a factor analysis (variant of PCA) conducted on 32 decision-making measures on 830 young people, and separated good and bad performance indices. Decision acuity reflected generic decision-making ability, predicted mental health factors, and was reflected in resting-state functional connectivity, but distinct from IQ (Moutoussis et al., 2021). Like decision acuity Moutoussis et al., 2021, our PC1 increased significantly with age, consistent with increasing performance (Appendix 3—figure 1B; age effects of subsequent PCs in Appendix 8—figure 4; Appendix 8—table 1).

![Figure 3.](https://cdn.elifesciences.org/articles/75474/elife-75474-fig3-v1.jpg)

**Figure 3.:** A PCA was conducted on the entire dataset (39 behavioral features and 15 model parameters). The figure shows the factor loadings (y-axis) of of all dataset features (x-axis) for the first three PCs (panels A, B, and C). Features that are RL model parameters are bolded and in purple. Behavioral features are explained in detail in Appendix 1 and Appendix 3 (note that behavioral features differed between tasks). Dotted lines aid visual organization by grouping similar features across tasks (e.g. missed trials of all three tasks) or within tasks (e.g. working-memory-related features for task C). (A) PC1 captured broadly-defined task engagement, with negative loadings on features that were negatively associated with performance (e.g. number of missed trials) and positive loadings on features that were positively associated with performance (e.g. percent correct trials). (B–C) PC2 (B) and PC3 (C) captured task contrasts. PC2 loaded positively on features of task B (orange box) and negatively on features of task C (purple box). PC3 loaded positively on features of task A (green box) and negatively on features of tasks B and C. Loadings of features that are negative on PC1 are flipped in PC2 and PC3 to better visualize the task contrasts (section 'Principal component analysis (PCA)').

How can this understanding of PC1 (decision acuity) help us interpret model parameters? In all three tasks, noise/exploration and forgetting parameters loaded negatively on PC1 (Figure 3A), showing that elevated decision stochasticity and the decay of learned information were associated with poorer performance in all tasks. $\alpha_{+}$ showed positive loadings throughout, suggesting that faster integration of positive feedback was associated with better performance in all tasks. Taken together, noise/exploration, forgetting, and $\alpha_{+}$ showed consistency across tasks in terms of their interpretation with respect to decision acuity. Contrary to this, $\alpha_{-}$ loaded positively in task C, but negatively in task B, suggesting that performance increased when participants integrated negative feedback faster in task C, but performance decreased when they did the same in task B. As mentioned before, contradictory patterns of $\alpha_{-}$ were likely related to task demands: The fact that negative feedback was diagnostic in task C likely favored fast integration of negative feedback, while the fact that negative feedback was not diagnostic in task B likely favored slower integration (Figure 1E). This interpretation is supported by behavioral findings: ‘lose-stay’ behavior (repeating choices that produce negative feedback) showed the same contrasting pattern as $\alpha_{-}$ on PC1, loading positively in task B, which shows that lose-stay behavior benefited performance, but negatively on task C, which shows that it hurt performance (Figure 3A). This supports the claim that lower $\alpha_{-}$ was beneficial in task B, while higher $\alpha_{-}$ was beneficial in task C, in accordance with participant behavior and developmental differences.

We next analyzed PC2 and PC3. For easier visualization, we flipped the loadings of all features with negative loadings on PC1 to remove the effects of task engagement (PC1) when interpreting subsequent PCs (for details, see section 'Principal component analysis (PCA)'). This revealed that PC2 and PC3 encoded task contrasts: PC2 contrasted task B to task C (loadings were positive / negative / near-zero for corresponding features of tasks B / C / A; Figure 3B). PC3 contrasted task A to both B and C (loadings were positive / negative for corresponding features on task A / tasks B and C; Figure 3C). (As opposed to most features of our dataset, missed trials and response times did not show these task contrasts, suggesting that these features did not differentiate between tasks). The ordering of PC2 before PC3 shows that participants’ behavior differed more between task B compared to C (PC2: 8.9% explained variance) than between B and C compared to A (PC3: 6.2%; Appendix 8—figure 4), as expected based on task similarity (Figure 1E). PC2 and PC3 therefore show that, after task engagement, the main variation in our dataset arose from behavioral differences between tasks.

How can this understanding of PC2-3 promote our understanding of model parameters? The task contrasts encoded by the main behavioral measures were also evident in several parameters, including noise/exploration parameters, $\alpha_{+}$, and $\alpha_{-}$: These parameters showed positive loadings for task B in PC2 (A in PC3), and negative loadings for task C (B and C; PC2: Figure 3B, PC3: 3 C). This indicates that noise/exploration parameters, $\alpha_{+}$, and $\alpha_{-}$ captured different behavioral patterns depending on the task: The variance present in these parameters allowed for the discrimination of all tasks from each other, with PC2 discriminating task B from C, and PC3 discriminating tasks B and C from A. In other words, these parameters were clearly distinguishable between tasks, showing that they did not capture the same processes. Had they captured the same processes across tasks, they would not be differentiable between tasks, similar to, for example, response times. What is more, each parameter captured sufficient task-specific variance to indicate in which task it was measured. In sum, these findings contradict the assumption that parameters are specific or interpretable in a task-independent way.

Taken together, the PCA revealed that the emerging major axes of variation in our large dataset, together capturing 40.2% of explained variance, were task engagement (PC1) and task differences (PC2-PC3). These dimensions can be employed to better understand model parameters: Task engagement / decision acuity (PC1) played a crucial role for all four parameters (Figure 3A), and this role was consistent across tasks for noise/exploration, forgetting, and $\alpha_{+}$. This consistency supports the claim that parameters captured specific, task-independent processes in terms of PC1. For $\alpha_{-}$, however, PC1 played inverse roles across tasks, showing a lack of task-independent specificity that was likely due to differences in task demands. Furthermore, PC2 and PC3 revealed that noise/exploration, $\alpha_{+}$, and $\alpha_{-}$ specifically encoded task contrasts, suggesting that the parameters captured different cognitive processes across tasks, lacking a task-independent core of meaning.

#### Parameters and cognitive processes

Whereas the previous analysis revealed that parameter roles were not entirely consistent across tasks, it did not distinguish between parameter specificity (whether the same parameter captures the same cognitive processes across tasks) and distinctiveness (whether different parameters capture different cognitive processes).

To assess this, we probed how much parameter variance was explained by both corresponding and non-corresponding parameters across tasks: We predicted one parameter from all others to get a sense for which relationships were least and most explanatory, while accounting for all relationships of all parameters, using regression. We assumed that parameters reflected one or more cognitive processes, such that shared variance implies overlapping cognitive processes. If parameters are specific (i.e. reflect similar cognitive processes across tasks), then corresponding parameters should be predictive of each other (e.g. when predicting task B’s $\frac{1}{\beta}$ from task A’s parameters, task A’s $\frac{1}{\beta}$ should show a significant regression coefficient). If parameters are also distinct, then non-corresponding parameters should furthermore not be predictive (e.g. no other parameters beside task A’s $\frac{1}{\beta}$ should predict task B’s $\frac{1}{\beta}$). We used repeated, k-fold cross-validated Ridge regression to avoid overfitting, obtaining unbiased out-of-sample estimates of the means and variances of explained variance $R^{2}$ and regression coefficients $w$ (for methods, see section 'Ridge regression').

Assessing general patterns that arose in this analysis, we found that all significant coefficients connected tasks A and B or tasks A and C but never tasks B and C, mirroring previous results (Figure 2D; section 'Relative parameter differences') with regard to task similarity (Figure 1E). This suggests that no parameter had a specific core that extended across all three tasks—the largest shared variance encompassed two tasks.

We first address parameter specificity. Focusing on noise/exploration parameters, coefficients were significant when predicting noise/exploration in task A from noise/exploration in tasks B or C, but the inverse was not true, such that coefficients were not significant when predicting tasks B or C from task A (Figure 4A; Table 5). The first result implies parameter specificity, showing that noise/exploration parameters captured variance (cognitive processes) in task A that they also captured in tasks B and C. The second result, however, implies a lack of specificity, showing that noise/exploration parameters captured additional cognitive processes in tasks B and C that they did not capture in task A. A further lack of specificity was evident in that even the variance that both B and C captured in A was not the same: Prediction accuracy increased when combining tasks B and C to predict task A, showing that noise/exploration parameters in tasks B and C captured partly non-overlapping aspects of noise/exploration (Figure 4B, left-most set of bars, compare purple to orange and blue).

![Figure 4.](https://cdn.elifesciences.org/articles/75474/elife-75474-fig4-v1.jpg)

**Figure 4.:** (A) Parameter variance that is shared between tasks. Each arrow shows a significant regression coefficient when predicting a parameter in one task (e.g. $\alpha_{+}$ in task A) from all parameters of a different task (e.g. $P$, $\alpha_{-}$, $\alpha_{+}$, and $\frac{1}{\beta}$ in task B). The predicted parameter is shown at the arrow head, predictors at its tail. Full lines indicate positive regression coefficients, and are highlighted in purple when connecting two identical parameters; dotted lines indicate negative coefficients; non-significant coefficients are not shown. Table 5 provides the full statistics of the models summarized in this figure. (B) Amount of variance of each parameter that was captured by parameters of other models. Each bar shows the percentage of explained variance ($R^{2}$) when predicting one parameter from all parameters of a different task/model, using Ridge regression. Part (A) of this figure shows the coefficients of these models. The x-axis shows the predicted parameter, and colors differentiate between predicting tasks. Three models were conducted to predict each parameter: One combined the parameters of both other tasks (pink), and two kept them separate (green, orange, blue). Larger amounts of explained variance (e.g., Task A $\frac{1}{\beta}$ and $\alpha_{-}$) suggest more shared processes between predicted and predicting parameters; the inability to predict variance (e.g. Task B $\alpha_{+}$; Task C working memory parameters) suggests that distinct processes were captured. Bars show mean $R^{2}$, averaged over $k$ data folds ($k$ was chosen for each model based on model fit, using repeated cross-validated Ridge regression; for details, see section 'Ridge regression'); error bars show standard errors of the mean across folds. (C) Relations between parameters and behavior. The arrows visualize Ridge regression models that predict parameters (bottom row) from behavioral features (top row) within tasks (full statistics in Table 6). Arrows indicate significant regression coefficients, colors denote tasks, and line types denote the sign of the coefficients, like before. All significant within-task coefficients are shown. Task-based consistency (similar relations between behaviors and parameters across tasks) occurs when arrows point from the same behavioral features to the same parameters in different tasks (i.e. parallel arrows). (D) Variance of each parameter that was explained by behavioral features; corresponds to the behavioral Ridge models shown in part (C).

**Table 5.**
 Selected coefficients of the repeated, k-fold cross-validated Ridge regression models predicting one parameter from all parameters of a different task.The table includes all significant coefficients and selected non-significant coefficients.


<table>
  <thead>
    <tr>
      <th>Predicted parameter (Task)</th>
      <th>Predicting parameter (Task)</th>
      <th>Coefficient</th>
      <th>p</th>
      <th>sig.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Noise/exploration (A)</td>
      <td>Exploration 1β (B)</td>
      <td>0.14</td>
      <td>0.031</td>
      <td>*</td>
    </tr>
    <tr>
      <td></td>
      <td>α- (B)</td>
      <td>0.14</td>
      <td>0.032</td>
      <td>*</td>
    </tr>
    <tr>
      <td></td>
      <td>Persistence (B)</td>
      <td>–0.19</td>
      <td>0.0029</td>
      <td>**</td>
    </tr>
    <tr>
      <td></td>
      <td>Noise ϵ (C)</td>
      <td>0.12</td>
      <td>0.038</td>
      <td>*</td>
    </tr>
    <tr>
      <td></td>
      <td>α- (C)</td>
      <td>–0.18</td>
      <td>0.045</td>
      <td>*</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td>–0.19</td>
      <td>0.023</td>
      <td>*</td>
    </tr>
    <tr>
      <td>Noise/exploration (B)</td>
      <td>Noise/exploration (A)</td>
      <td>0.09</td>
      <td>0.27</td>
      <td>–</td>
    </tr>
    <tr>
      <td>Noise/exploration (C)</td>
      <td>Noise/exploration (A)</td>
      <td>0.04</td>
      <td>0.63</td>
      <td>–</td>
    </tr>
    <tr>
      <td>α+ (A)</td>
      <td>α- (C)</td>
      <td>0.22</td>
      <td>0.011</td>
      <td>*</td>
    </tr>
    <tr>
      <td></td>
      <td>ρ (C)</td>
      <td>0.16</td>
      <td>0.050</td>
      <td>*</td>
    </tr>
    <tr>
      <td></td>
      <td>K (C)</td>
      <td>0.15</td>
      <td>0.020</td>
      <td>*</td>
    </tr>
    <tr>
      <td></td>
      <td>Exploration 1β (B)</td>
      <td>0.19</td>
      <td>0.0026</td>
      <td>**</td>
    </tr>
    <tr>
      <td></td>
      <td>α- (B)</td>
      <td>–0.21</td>
      <td>&lt;0.001</td>
      <td>***</td>
    </tr>
    <tr>
      <td></td>
      <td>α+ (B)</td>
      <td>0.0042</td>
      <td>0.94</td>
      <td>–</td>
    </tr>
    <tr>
      <td></td>
      <td>Persistence (B)</td>
      <td>0.23</td>
      <td>&lt;0.001</td>
      <td>***</td>
    </tr>
    <tr>
      <td>α+(B)</td>
      <td>1β (A)</td>
      <td>–0.077</td>
      <td>0.37</td>
      <td>–</td>
    </tr>
    <tr>
      <td></td>
      <td>α+ (A)</td>
      <td>0.058</td>
      <td>0.48</td>
      <td>–</td>
    </tr>
    <tr>
      <td></td>
      <td>α+ (C)</td>
      <td>–0.00018</td>
      <td>0.99</td>
      <td>–</td>
    </tr>
    <tr>
      <td></td>
      <td>α- (C)</td>
      <td>–0.000055</td>
      <td>1.00</td>
      <td>–</td>
    </tr>
    <tr>
      <td></td>
      <td>Forgetting (A)</td>
      <td>0.015</td>
      <td>0.82</td>
      <td>–</td>
    </tr>
    <tr>
      <td>α+ (C)</td>
      <td>α+ (A)</td>
      <td>0.20</td>
      <td>0.013</td>
      <td>*</td>
    </tr>
    <tr>
      <td>α- (B)</td>
      <td>α+ (A)</td>
      <td>–0.25</td>
      <td>0.0018</td>
      <td>**</td>
    </tr>
    <tr>
      <td>α- (C)(C)</td>
      <td>α+ (A)</td>
      <td>0.24</td>
      <td>0.0022</td>
      <td>**</td>
    </tr>
  </tbody>
</table>

**Table 6.**
 Statistics of selected coefficients in the repeated, k-fold cross-validated Ridge regression models predicting each model parameter from all behavioral features of all three tasks.The table includes all significant coefficients of within-task predictors, and a selected number of non-significant and between-task coefficients.


<table>
  <thead>
    <tr>
      <th>Predicted parameter (Task)</th>
      <th>Predicting parameter (Task)</th>
      <th>coefficient</th>
      <th>p</th>
      <th>sig.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Noise/exploration (A)</td>
      <td>Win-stay (A)</td>
      <td>–0.30</td>
      <td>&lt;0.001</td>
      <td>***</td>
    </tr>
    <tr>
      <td></td>
      <td>Lose-stay (A)</td>
      <td>–0.23</td>
      <td>&lt;0.001</td>
      <td>***</td>
    </tr>
    <tr>
      <td></td>
      <td>Accuracy (A)</td>
      <td>–0.19</td>
      <td>0.0076</td>
      <td>**</td>
    </tr>
    <tr>
      <td></td>
      <td>Response times (A)</td>
      <td>0.092</td>
      <td>0.029</td>
      <td>*</td>
    </tr>
    <tr>
      <td></td>
      <td>Delay (A)</td>
      <td>0.25</td>
      <td>&lt;0.001</td>
      <td>***</td>
    </tr>
    <tr>
      <td>Noise/exploration (B)</td>
      <td>Win-stay (B)</td>
      <td>–0.58</td>
      <td>&lt;0.001</td>
      <td>***</td>
    </tr>
    <tr>
      <td></td>
      <td>Lose-stay (B)</td>
      <td>0.091</td>
      <td>0.0034</td>
      <td>**</td>
    </tr>
    <tr>
      <td></td>
      <td>Accuracy (B)</td>
      <td>–0.36</td>
      <td>&lt;0.001</td>
      <td>***</td>
    </tr>
    <tr>
      <td></td>
      <td>Win-stay (A)</td>
      <td>–0.12</td>
      <td>0.032</td>
      <td>*</td>
    </tr>
    <tr>
      <td></td>
      <td>Response times (A)</td>
      <td>0.059</td>
      <td>0.051</td>
      <td>–</td>
    </tr>
    <tr>
      <td>α+ (A)</td>
      <td>Win-stay (A)</td>
      <td>0.74</td>
      <td>&lt;0.001</td>
      <td>***</td>
    </tr>
    <tr>
      <td>α+ (B)</td>
      <td>Win-stay (B)</td>
      <td>0.27</td>
      <td>&lt;0.001</td>
      <td>***</td>
    </tr>
    <tr>
      <td>α+ (C)</td>
      <td>Accuracy (C)</td>
      <td>0.24</td>
      <td>0.033</td>
      <td>*</td>
    </tr>
    <tr>
      <td>α- (B)</td>
      <td>Win-stay (B)</td>
      <td>0.29</td>
      <td>&lt;0.001</td>
      <td>***</td>
    </tr>
    <tr>
      <td></td>
      <td>Lose-stay (B)</td>
      <td>–0.71</td>
      <td>&lt;0.001</td>
      <td>***</td>
    </tr>
    <tr>
      <td></td>
      <td>Accuracy (B)</td>
      <td>–0.28</td>
      <td>&lt;0.001</td>
      <td>***</td>
    </tr>
    <tr>
      <td>α- (C)</td>
      <td>Win-stay (C)</td>
      <td>0.16</td>
      <td>0.009</td>
      <td>**</td>
    </tr>
    <tr>
      <td></td>
      <td>Lose-stay (C)</td>
      <td>–0.41</td>
      <td>&lt;0.001</td>
      <td>***</td>
    </tr>
  </tbody>
</table>

Focusing next on learning rates, specificity was evident in that learning rate $\alpha_{+}$ in task A showed a significant regression coefficient when predicting learning rates $\alpha_{+}$ and $\alpha_{-}$ in task C, and learning rate $\alpha_{-}$ in task C showed a significant coefficient when predicting learning rate $\alpha_{+}$ in task A (Figure 4A; Table 5). This suggests a shared core of cognitive processes between learning rates $\alpha_{+}$ and $\alpha_{-}$ in tasks A and C. However, a lack of specificity was evident in task B: When predicting $\alpha_{+}$ in task B, no parameter of any task showed a significant coefficient (including $\alpha_{+}$ in other tasks; Table 5), and it was impossible to predict variance in task B’s $\alpha_{+}$ even when combining all parameters of the other tasks (Figure 4B, ‘Task B’ panel). This reveals that $\alpha_{+}$ captured fundamentally different cognitive processes in task B compared to the other tasks. The case was similar for parameter $\alpha_{-}$, which strikingly was inversely related between tasks A and B (Table 5), and impossible to predict in task B from all other parameters (Figure 4B). This reveals a fundamental lack of specificity, implying that learning rates in task B did not capture the same core of cognitive processes compared to other tasks.

We next turned to distinctiveness, that is, whether different parameters capture different cognitive processes. Noise/exploration in task A was predicted by Persistence and $\alpha_{-}$ in task B, and by $\alpha_{-}$ and working memory weight $ρ$ in task C (Figure 4A; Table 5). This shows that processes that were captured by noise/exploration parameters in task A were captured by different parameters in other tasks, such that noise/exploration parameters did not capture distinct cognitive processes.

In the case of learning rates, $\alpha_{+}$ in task A was predicted nonspecifically by all parameters of task B (with the notable exception of $\alpha_{+}$ itself; Figure 4A; Table 5), suggesting that the cognitive processes that $\alpha_{+}$ captured in task A were captured by an interplay of several parameters in task B. Furthermore, task A’s $\alpha_{+}$ was predicted by task C’s working memory parameters $ρ$ and $K$ (Figure 4A; Table 5), suggesting that $\alpha_{+}$ captured a conglomerate of RL and working memory processes in task A that was isolated by different parameters in task C (Collins and Frank, 2012). In support of this interpretation, no variance in task C’s working memory parameters could be explained by any other parameters (Figure 4B), suggesting that they captured unique working memory processes that were not captured by other parameters. Task C’s RL parameters, on the other hand, could be explained by parameters in other tasks (Figure 4B), suggesting they captured overlapping RL processes. In tasks B and C, $\alpha_{+}$ and $\alpha_{-}$ were partly predicted by other learning rate parameters (specific and distinct), partly not predicted at all (lack of specificity), and partly predicted by several parameters (lack of distinctiveness; Figure 4A).

In sum, in the case of noise/exploration, there was evidence for both specificity and a lack thereof (mutual prediction between some, but not all noise/exploration parameters). Noise/exploration parameters were also not perfectly distinct, being predicted by a small set of other parameters from different tasks. In the case of learning rates, some specificity was evident in the shared variance between tasks A and C, but that specificity was missing in task B. Distinctiveness was particularly low for learning rates, with variance shared widely between multiple different parameters. When conducting the same analyses in simulated agents using the same parameters across tasks (section 'Statistical comparison to generalizability ceiling'), we obtained much higher specificity and distinctiveness.

#### Parameters and behavior

The previous sections suggested that parameters captured different cognitive processes across tasks (i.e. different internal characteristics of learning and choice). We lastly examined whether parameters also captured different behavioral features across tasks (e.g. tendency to stay after positive feedback), and whether behavioral features generalized better. To investigate this question, we assessed the relationships between model parameters and behavioral features across tasks, using regularized Ridge regression as before, and predicting each model parameter from each task’s behavioral features (15 predictors, see 'Appendix 1' and 'Appendix '6; for regression methods, see section 'Ridge regression').

We found that noise/exploration parameters were predicted by the same behavioral features in tasks A and B, such that task A’s accuracy, win-stay, and lose-stay behavior predicted task A’s $\frac{1}{\beta}$; and task B’s accuracy, win-stay, and lose-stay behavior predicted task B’s $\frac{1}{\beta}$ (Figure 4C; Table 6). This shows consistency in terms of which (task-specific) behaviors were related to (task-specific) parameter $\frac{1}{\beta}$. Similarly for learning rates, $\alpha_{+}$ was predicted by the same behavior (win-stay) in tasks A and B, and $\alpha_{-}$ was predicted by the same behaviors (lose-stay, win-stay) in tasks B and C (Figure 4C; Table 6). This consistency in $\alpha_{-}$ is especially noteworthy given the pronounced lack of consistency in the previous analyses.

In sum, noise/exploration parameters, $\alpha_{+}$, and $\alpha_{-}$ successfully generalized between tasks in terms of which behaviors they reflected (Figure 4C), despite the fact that many of the same parameters did not generalize in terms of how they characterized participants (sections 'Differences in absolute parameter values', 'Relative parameter differences', and 'Parameter age trajectories'), and which cognitive processes they captured (sections 'Main axes of variation and parameters and cognitive processes'). Notably, the behavioral and parameter differences we observed between tasks often seemed tuned to specific task characteristics (Figure 1E), both in the case of parameters (most notably $\alpha_{-}$; Figures 2C and 3A) and behavior (most notably lose-stay behavior; Appendix 3—figure 1B), suggesting that both behavioral responses and model parameters were shaped by task characteristics. This suggests a succinct explanation for why parameters did not generalize between tasks: Because different tasks elicited different behaviors (Appendix 3—figure 1B), and because each behavior was captured by the same parameter across tasks (Figure 4C), parameters necessarily differed between tasks.

## Discussion

Both generalizability (Nassar and Frank, 2016) and interpretability (i.e. the inherent ‘meaningfulness’ of parameters Huys et al., 2016) have been stated as advantages of computational modeling, and many current research practices (e.g. comparing parameter-specific findings between studies) endorse them (Eckstein et al., 2021). However, RL model generalizability and interpretability has so far eluded investigation, and growing inconsistencies in the literature potentially cast doubt on these assumptions. It is hence unclear whether, to what degree, and under which circumstances we should assume generalizability and interpretability. Our developmental, within-participant study revealed that these assumptions warrant both increased scepticism and continued investigation: Generalizability and interpretability were suprisingly low for most parameters and tasks, but reassuringly high for a few others:

Exploration/noise parameters showed considerable generalizability in the form of correlated variance and age trajectories. Furthermore, the decline in exploration/noise we observed between ages 8–17 was consistent with previous studies (Nussenbaum and Hartley, 2019; Somerville et al., 2017; Gopnik, 2020), revealing consistency across tasks, models, and research groups that supports the generalizability of exploration/noise parameters. Still, for 2/3 pairs of tasks, the degree of generalization was significantly below the level of generalization expected by agents with perfect generalization.

Interpretability of exploration/noise parameters was mixed: Despite evidence for specificity in some cases (overlap in parameter variance between tasks), it was missing in others (lack of overlap), and crucially, parameters lacked distinctiveness (substantial overlap in variance with other parameters). Thus, while exploration/noise parameters were generalizable across tasks, they were not neurocognitively “interpretable” (as defined above).

Learning rate from negative feedback showed a substantial lack of generalizability: parameters were less consistent within participants than within tasks, and age trajectories differed both quantitatively and qualitatively. Learning rates from positive feedback, however, showed some convincing patterns of generalization. These results are consistent with the previous literature, which shows mixed results for learning rate parameters (Nussenbaum and Hartley, 2019). In terms of interpretability, learning rates from positive and negative feedback combined were somewhat specific (overlap in variance between some tasks). However, a lack of specificity (lack of shared core variance) and distinctiveness (fundamental entangling with several other parameters, most notably working memory parameters) overshadowed this result.

Taken together, our study confirms the patterns of generalizable exploration/noise parameters and task-specific learning rate parameters that are emerging from the literature (Nussenbaum and Hartley, 2019). Furthermore, we show that this is not a result of between-participant comparisons, but that the same participants will show different parameters when tested using different tasks. The inconsistency of learning rate parameters leads to the important conclusion that we cannot measure an individual’s ‘intrinsic learning rate’, and that we should not draw general conclusions about ‘the development of learning rates’ with the implication that they apply to all contexts.

These findings help clarify the source of parameter inconsistencies in previous literature (besides replication problems and technical issues, such as model misspecification [Nussenbaum and Hartley, 2019], lack of model comparison and validation [Palminteri et al., 2017; Wilson and Collins, 2019], lack of model critique [Nassar and Frank, 2016], inappropriate fitting methods [Daw, 2011; Lee, 2011], and lack of parameter reliability [Brown et al., 2020]): Our results show that discrepancies are expected even with a consistent methodological pipeline and up-to-date modeling techniques, because they are an expected consequence of variations in context (e.g. features of the experimental task [section Parameters and behavior] and the computational model). The results also suggest that the mapping between cognitive processes and exhibited behavior is many-to-many, such that different cognitive mechanisms (e.g. reasoning, value learning, episodic memory) can give rise to the same behaviors (e.g. lose-stay behavior) and parameters (e.g. $\alpha_{-}$), while the same cognitive mechanism (e.g. value learning) can give rise to different behaviors (e.g. win-stay, lose-shift) and influence several parameters (e.g. $\alpha_{+}$, $\alpha_{-}$), depending on context factors. Under this view, analysis of model parameters alone does not permit unequivocal conclusions about cognitive processes if the context varies (Figure 5B), and the interpretation of model parameter results requires careful contextualization.

![Figure 5.](https://cdn.elifesciences.org/articles/75474/elife-75474-fig5-v1.jpg)

**Figure 5.:** In this view, which is implicitly endorsed by much current computational modeling research, models are fitted in order to reveal individuals’ intrinsic model parameters, which reflect clearly delineated, separable, and meaningful (neuro)cognitive processes, a concept we call interpretability. Interpretability is the assumption that every model parameter captures a specific cognitive process (bidirectional arrows between each parameter and process), and that cognitive processes are separable from each other (no connections between processes). Task characteristics are treated as irrelevant, a concept we call generalizability, such that parameters of any learning task (within reason) are expected to capture similar cognitive processes. (B) Updated view, based on our results, that acknowledges the role of context (e.g. task characteristics, model parameterization, participant sample) in computational modeling. Which cognitive processes are captured by each model parameter is influenced by context (green, orange, blue), as shown by distinct connections between parameters and cognitive processes. Different parameters within the same task can capture overlapping cognitive processes (not interpretable), and the same parameters can capture different processes depending on the task (not generalizable). However, parameters likely capture consistent behavioral features across tasks (thick vertical arrows).

Future research needs to investigate context factors to characterize these issues in more detail. For example, which task characteristics determine which parameters will generalize and which will not, and to what extent? Does context impact whether parameters capture overlapping versus distinct variance? Here, the systematic investigation of task space (i.e., testing the same participants on a large battery of learning tasks created as the full factorial of all task features) could elucidate the relationships between parameter generalizability and task-based context factors (e.g., stochasticity, volatility, reward probability). To determine the distance between tasks, the MDP framework might be especially useful because it decomposes tasks along theoretically meaningful features. Future research will also need to determine the relative contributions of different sources of inconsistency, differentiating those caused by technical issues from those caused by context differences.

In sum, our results suggest that relating model parameters to cognitive constructs and real-world behavior might require us to carefully account for task variables and environmental variability in general. This ties into a broader open question of how neurocognitive processes are shared between tasks (Eisenberg et al., 2019; Moutoussis et al., 2021), and reflects a larger pattern of thought in psychology that we cannot objectively assess an individual’s cognitive processing while ignoring context. We have shown that in lab studies, different task contexts recruit different system settings within an individual; similarly, our real-life surroundings, the way they change during development, and our past environments (Lin et al., 2020; Lin et al., 2022) may also modulate which cognitive processes we recruit.

### Limitations

Our study faces several potential limitations, both due to the technical aspects of model creation and selection, and to the broader issue of parameter reliability. One potential technical limitation is the existence of within-model parameter correlations. These correlations may mean the values of parameters of the same model trade off during fitting, potentially leading to lower parameter correlations between models, and decreased estimates of parameter generalizability. However, this limitation is unlikely to affect our overall conclusion: Our simulation analysis showed that generalization was detectable despite this issue (section 'Statistical comparison to generalizability ceiling'), suggesting that we would have been able to detect more generalization in humans if it had been present. Furthermore, the majority of previous work using computational models to study human behavior is subject to the same within-model parameter tradeoffs (e.g. common negative correlation between $\alpha$ and $\beta$ in RL models), meaning that the results of our study likely give a realistic estimate of expected parameter generalization in the current literature.

Another limitation relates to the potential effects of model misspecification on our results. An example of model misspecification is the failure to include a variable in the model that was relevant in the data-generating process (e.g. outcome-independent choice persistence); such misspecification can lead to the inaccurate estimation of other parameters in the model (e.g. learning rate [Katahira, 2018]). In our study, model misspecification—if present—could account for some of the lack of generalization we observed. As for the previous limitation, however, the fact that model misspecification is likely a ubiquitous feature of the current modeling literature (and potentially fundamentally unattainable when fitting complex data-generating processes such as human decision makers) means that our results likely provide a realistic picture of the generalizability of current models.

Another potential limitation is the difference between the models for each task, despite shared or overlapping cognitive processes. It is possible, for example, that parameters would generalize better if the same model had been used across tasks. The current dataset, however, is not suitable to answer this question: It would be impossible to fit the same model to each task due to issues of model misspecification (when using a model that is too simple) or violation of the principle of simplicity (when using a model that is too complex; for details, see 'Appendix 7'). Future research will be required to address this issue, and to potentially dissociate the effects of model differences and task differences we here jointly call ‘context’.

Lastly, model parameter reliability might play a crucial role for our results: If parameters lack consistency between two instantiations of the same task (reliability), generalization between different tasks would necessarily be low as well. A recent wave of research, however, has convincingly demonstrated that good reliability is possible for several common RL models (Brown et al., 2020; Shahar et al., 2019; Pratt et al., 2021; Waltmann et al., 2022), and we employ the recommended methods here (Xia et al., 2021; Eckstein et al., 2022). In addition, our simulation analysis shows that our approach can detect generalization.

In conclusion, a variety of methodological issues could explain (part of) the lack of generalization we find for most parameters in the human sample. However, these issues cannot explain all of our results because the same approach successfully detects generalization in a simulated dataset. Furthermore, none of these issues are unique to our approach, but likely ubiquitous in the current modeling literature. This means that our results likely provide a realistic estimate of parameter generalization based on current methods. A more detailed discussion of each limitation is provided in 'Appendix 7'.

### Moving forward

With this research, we do not intend to undermine RL modeling as a practice, or challenge pre-existing findings drawn from it, but to improve its quality. Computational model parameters potentially provide highly valuable insights into (neuro)cognitive processing—we just need to refrain from assuming that the identified processes are always—through their mere nature as model parameters—specific, distinct, and ‘theoretically meaningful’ (Huys et al., 2016). Some parameters with the same names do not tend to transfer between different tasks, making them non-interchangeable, while others seem to transfer well. And in all cases, the behavioral features captured by parameters seem to generalize well. In the long term, we need to understand why RL parameters differ between tasks. We suggest three potential, not mutually exclusive answers:

### Conclusion

Our research has important implications for computational modeling in general, and specifically for fields that focus on individual differences, including developmental and clinical computational research: We show that contextual factors critically impact computational modeling results. Larger, targeted studies will be necessary to identify the most important contextual factors and their precise roles, and to quantify their effects. Other areas of modeling besides RL might face similar issues, given that generalizability and interpretability are also commonly assumed in models of sequential sampling (Sendhilnathan et al., 2020; McDougle and Collins, 2021), Bayesian inference (Eckstein et al., 2022; Radulescu et al., 2019; Konovalov and Krajbich, 2018), model-based versus model-free RL (Brown et al., 2020; Kool et al., 2016; Hare, 2020), and others.

If a model parameter lacks generalizability and/or interpretability, it does not measure task-independent, person-specific characteristics, as we often assume. This parameter is more closely tied to the specific, contextual factors of experimental paradigms, and should be interpreted within the context of that task, and only compared between studies with the clear understanding of this task-dependence. We hope that acknowledging this will help the field of computational modeling to accurately interpret computational models (in direct relation to the experimental task), to combine insights of different studies (by taking into account differences in parameter optimality, modulatory factors, and processes captured by each parameter), and to achieve improved generalizability and interpretability of findings in the future. This work aims not to discourage the use of RL models to model behavior, but to improve the application of these models, in particular the robustness of the conclusions we draw from their fits.

## Materials and methods

### Study design

Our sample of 291 participants was balanced between females and males, and all ages (8–30 years) were represented equally (Figure 1A, left). Participants completed four computerized tasks, questionnaires, a saliva sample during the 1–2 hr lab visit, and another take-home sample (see section 'Testing procedure'). To reduce noise, we excluded participants based on task-specific performance criteria (see section 'Participant sample'). Due to worse performance, more younger than older participants were excluded, which is a caveat for the interpretation of age effects (note, however, that these exclusions cannot account for the observed age effects but act against them; Figure 1A). Our tasks—A (‘Butterfly task’ Xia et al., 2021; Davidow et al., 2016), B (‘Stochastic Reversal’ Tai et al., 2012; Eckstein et al., 2022), and C (‘Reinforcement learning-Working memory’ Master et al., 2020; Collins and Frank, 2012)—were all classic reinforcement learning tasks: on each trial, participants chose between several actions in an effort to earn rewards, which were presented as binary feedback (win/point or lose/no point) after each choice.

The tasks varied on several common dimensions (Figure 1E), which have been related to discrepancies in behavioral and neurocognitive results in the literature (Garrison et al., 2013; Yaple and Yu, 2019; Liu et al., 2016). For example, in one task (task C), positive feedback was deterministic, such that every correct action led to a positive outcome, whereas in the two other tasks (tasks A and B), positive feedback was stochastic, such that some correct actions led to positive and others to negative outcomes. A different set of two tasks (B and C) provided diagnostic positive feedback, such that every positive outcome indicated a correct action, whereas in the third (A), positive feedback was non-diagnostic, such that positive outcomes could indicate both correct and incorrect actions. Two tasks (A and C) presented several different stimuli/states for which correct actions had to be learned, whereas the third (B) only presented a single one. Overall, task A shared more similarities with both tasks B and C than either of these shared with each other, allowing us to ask the exploratory question whether task similarity played a role in parameter generalizability and interpretability. A comprehensive list of task differences is shown in Figure 1E, and each task is described in more detail in section 'Task design'. Section 'Appendix 3' explains the most prominent findings of each task individually, and shows several behavioral measures over age.

### Participant sample

#### Sample overview

All procedures were approved by the Committee for the Protection of Human Subjects at the University of California, Berkeley, with reference number 2016-06-8925. We tested 312 participants: 191 children and adolescents (ages 8–17) and 55 adults (ages 25–30) were recruited from the community and completed a battery of computerized tasks, questionnaires, and saliva samples; 66 university undergraduate students (aged 18–50) completed the four tasks as well, but not the questionnaires or saliva sample. Community participants of all ages were pre-screened for the absence of present or past psychological and neurological disorders; the undergraduate sample indicated the absence of these. Compensation for community participants consisted of $25 for the 1–2 hr in-lab portion of the experiment and $25 for completing optional take-home saliva samples; undergraduate students received course credit for participation in the 1-hr study.

#### Participant exclusion

Two participants from the undergraduate sample were excluded because they were older than 30, and 7 were excluded because they failed to indicate their age. This led to a sample of 191 community participants under 18, 57 undergraduate participants between the ages of 18–28, and 55 community participants between the ages of 25–30. Of the 191 participants under 18, 184 completed task B, and 187 completed tasks A and C. Reasons for not completing a task included getting tired, running out of time, and technical issues. All 57 undergraduate participants completed tasks B and C and 55 completed task A. All 55 community adults completed tasks B and A, and 45 completed task C. Appropriate exclusion criteria were implemented separately for each task to exclude participants who failed to pay attention and who performed critically worse than the remaining sample (for task A, see Xia et al., 2021; task B Eckstein et al., 2022; task C Master et al., 2020). Based on these criteria, 5 participants under the age of 18 were excluded from task B, 10 from task A, and none from task C. One community adult participant was excluded from task A, but no adult undergraduates or community participants were excluded from tasks B or C.

Because this study related the results from all three tasks, we only included participants who were not excluded in any task, leading to a final sample of 143 participants under the age of 18 (male: 77; female: 66), 51 undergraduate participants (male: 17; female: 34), and 53 adults from the community (male: 25; female: 28), for a total of 247 participants (male: 119; female: 128). We excluded the fourth task of our study from the current analysis, which was modeled after a rodent task and used in humans for the first time (Johnson and Wilbrecht, 2011), because the applied performance criterion led to the exclusion of the majority of participants under 18. We split participants into quantiles based on age, which were calculated separately within each sex (for details, see Eckstein et al., 2022).

#### Testing procedure

After entering the testing room, participants under 18 years and their guardians provided informed assent and permission; participants over 18 provided informed consent. Guardians and participants over 18 filled out a demographic form. Participants were led into a quiet testing room in view of their guardians, where they used a video game controller to complete four computerized tasks, in the following order: The first task was called ‘4-choice’ and assessed reversal learning in an environment with 4 different choice options, with a duration of approximately 5 min (designed after Johnson and Wilbrecht, 2011). This task was excluded from the current analysis (see section 'Participant exclusion'). The second task was C (‘Reinforcement learning-Working memory’) and took about 25 min to complete (Collins and Frank, 2012; Master et al., 2020). After the second task, participants between the ages of 8–17 provided a saliva sample (for details, see Master et al., 2020) and took a snack break (5–10 min). After that, participants completed task A (‘Butterfly task’), which took about 15 min (Davidow et al., 2016; Xia et al., 2021), and task B (‘Stochastic Reversal’), which took about 10 min to complete (Eckstein et al., 2022). At the conclusion of the tasks, participants between 11 and 18 completed the Pubertal Development Scale (PDS Petersen et al., 1988) and were measured in height and weight. Participants were then compensated with $25 Amazon gift cards. For subjects under 11, their guardians completed the PDS on their behalf. The PDS questionnaire and saliva samples were administered to investigate the role of pubertal maturation on learning and decision making. Pubertal analyses are not the focus of the current study and will be or have been reported elsewhere (Master et al., 2020; Eckstein et al., 2022; Xia et al., 2021). For methodological details, refer to Master et al., 2020. The entire lab visit took 60–120 min, depending on the participant, and the order of procedures was the same for all subjects.

### Task design

#### Task A (‘butterfly task’)

The goal of task A was to collect as many points as possible, by guessing correctly which of two flowers was associated with each of four butterflies. Participants were instructed to guess which flower each butterfly liked more, having been told that butterflies would sometimes also choose the less-liked flower (i.e. act probabilistically). Correct guesses were rewarded with 70% probability, and incorrect guesses with 30%. The task contained 120 trials (30 for each butterfly) that were split into 4 equal-sized blocks, and took between 10 and 20 min to complete. More detailed information about methods and results can be found in Xia et al., 2021.

#### Task B (‘stochastic reversal’)

The goal of task B was to collect golden coins, which were hidden in two green boxes. Participants completed a child-friendly tutorial, in which they were instructed to help a leprechaun find his treasure by collecting individual coins from two boxes. Task volatility (i.e. boxes switching sides) and stochasticity (i.e. correct box not rewarded each time) were introduced one-by-one (for details, see Eckstein et al., 2022). The task could be in one of two states: ‘Left box is correct’ or ‘Right box is correct’. In the former, selecting the left box led to reward in 75% of trials, while selecting the right box never led to a reward (0%). Several times throughout the task, task contingencies changed unpredictably and without notice (after participants had reached a performance criterion indicating they had learned the current state), and the task switched states. Participants completed 120 trials of this task (2–9 reversals), which took approximately 5–15 min. For more information and additional task details, refer to Eckstein et al., 2022.

#### Task C (‘reinforcement learning-working memory’)

The goal of task C was to collect as many points as possible by pressing the correct key for each stimulus. Participants were instructed to learn an ‘alien language’ of key presses by associating individual pictures with specific key presses. Pressing the correct key for a specific stimulus deterministically led to reward, and the correct key for a stimulus never changed. Different blocks required subjects to learn about different numbers of stimuli, with set sizes ranging from 2 to 5 images. In each block, each stimulus was presented 12–14 times, for a total of 13 * set size trials per block. Three blocks had set sizes of 2–3, and 2 blocks had set sizes of 4–5, for a total of 10 blocks. The task took between 15 and 25 minutes to complete. For more details, as well as a full analysis of this dataset, refer to Master et al., 2020.

### Computational models

For all tasks, we used RL theory to model how participants adapted their behavior in order to maximize reward. RL models assume that agents learn a policy $\pi⁢(a|s)$ that determines (probabilistically) which action $a$ to take in each state $s$ of the world (Sutton and Barto, 2017). Here and in most cognitive RL models, this policy is based on action values $Q⁢(a|s)$, that is, the values of each action $a$ in each state $s$. Agents learn action values by observing the reward outcomes, rt, of their actions at each time step $t$. Learning consists of updating existing action values $Q_{t}⁢(a|s)$ using the ‘reward prediction error’, the difference between the expected reward $Q_{t}⁢(a|s)$ and the actual reward rt:

$$
Q_{t+1}⁢(a|s)=Q_{t}⁢(a|s)+\alpha⁢(r_{t}-Q_{t}⁢(a|s))
$$

How much a learner weighs past action value estimates relative to new outcomes is determined by parameter $\alpha$, the learning rate. Small learning rates favor past experience and lead to stable learning over long time horizons, while large learning rates favor new outcomes and allow for faster and more flexible changes according to shorter time horizons. With enough time and in a stable environment, the RL updating scheme guarantees that value estimates will reflect the environment’s true reward probabilities, and thereby allow for optimal long-term choices (Sutton and Barto, 2017).

In order to choose actions, most cognitive RL models use a (noisy) ‘softmax’ function to translate action values $Q⁢(a|s)$ into policies $p⁢(a|s)$:

$$
p(a_{i}|s)=\frac{exp(\beta Q(a_{i}|s))}{\suma_{j}\inAexp(\beta Q(a_{j}|s))}
$$

$A$ refers to the set of all available actions (tasks A and B have 2 actions, task C has 3), and ai and aj to individual actions within the set. How deterministically versus noisily this translation is executed is determined by exploration parameter $\beta$, also called inverse decision temperature, and/or $ϵ$, the decision noise (see below). Small decision temperatures $\frac{1}{\beta}$ favor the selection of the highest-valued actions, biasing an agent towards exploitation, whereas large decision temperatures select actions of low and high values more evenly, enabling exploration. Parameter $ϵ$ adds undirected noise to action selection, selecting random actions with a small probability $ϵ$ on each trial.

Besides $\alpha$, $\beta$, and noise, cognitive RL models often include additional parameters to better fit empirical behavior in humans or animals. Common choices include Forgetting—a consistent decay of action values back to baseline—, and Persistence—the tendency to repeat the same action independent of outcomes, a parameter also known as sticky choice or perseverance (Sugawara and Katahira, 2021). In addition, cognitive models often differentiate learning from positive versus negative rewards, splitting learning rate $\alpha$ into two separate parameters $\alpha_{+}$ and $\alpha_{-}$, which are applied to only positive and only negative outcomes, respectively (Harada, 2020; Javadi et al., 2014; Christakou et al., 2013; van den Bos et al., 2012; Frank et al., 2004; Cazé and van der Meer, 2013; Palminteri et al., 2016; Lefebvre et al., 2017; Dabney et al., 2020). The next paragraphs introduce these parameters in detail.

In task A, the best fitting model included a forgetting mechanism, which was implemented as a decay in Q-values applied to all action values of the three stimuli (butterflies) that were not shown on the current trial:

$$
Q_{t+1}⁢(a|s)=(1-f)*Q_{t+1}⁢(a|s)+f*0.5.
$$

The free parameter $0<1$ reflects individuals’ tendencies to forget.

In task B, free parameter $P$ captured choice persistence, which biased choices on the subsequent trial toward staying ($P>0$) or switching ($P<0$). $P$ modifies action values $Q⁢(a|s)$ into $Q^{′}⁢(a|s)$, as follows:

$$
Q_{t}^{′}(a|s)=Q_{t}(a|s)+P  if  a_{t}=a_{t−1}
$$



$$
Q_{t}^{′}(a|s)=Q_{t}(a|s)  if  a_{t}\neqa_{t−1}
$$

In addition, the model of task B included counter-factual learning parameters $\alpha_{C+}$ and $\alpha_{C-}$, which added counter-factual updates based on the inverse outcome and affected the non-chosen action. For example, after receiving a positive outcome ($r=1$) for choosing left ($a$), counter-factual updating would lead to an ‘imaginary’ negative outcome ($r¯=0$) for choosing right ($a¯$).

$$
Q_{t+1}(a¯|s)=Q_{t}(a¯|s)+\alpha_{C−}(r¯−Q_{t}(a¯|s))  if  r_{t}=0
$$



$$
Q_{t+1}(a¯|s)=Q_{t}(a¯|s)+\alpha_{C+}(r¯−Q_{t}(a¯|s))  if  r_{t}=1
$$

$a¯$ indicates the non-chosen action, and $r¯$ indicates the inverse of the received outcome, $r¯=1-r$. The best model fits were achieved with $\alpha_{C+}=\alpha_{+}$ and $\alpha_{C-}=\alpha_{-}$, so counter-factual learning rates are not reported in this paper.

In tasks A and B, positive and negative learning rates are differentiated in the following way:

$$
Q_{t+1}(a|s)=Q_{t}(a|s)+\alpha_{+}(r_{t}−Q_{t}(a|s))  if  r_{t}=1
$$



$$
Q_{t+1}(a|s)=Q_{t}(a|s)+\alpha_{−}(r_{t}−Q_{t}(a|s))  if  r_{t}=0
$$

In the best model for task A, only $\alpha_{+}$ was a free parameter, while $\alpha_{-}$ was fixed to 0. In task C, $\alpha_{-}$ was a function of $\alpha_{+}$, such that $\alpha_{-}=b*\alpha_{+}$, where $b$ is the neglect bias parameter that determines how much negative feedback is neglected compared to positive feedback. Throughout the paper, we report $\alpha_{-}=b*\alpha_{+}$ for task C.

In addition to an RL module, the model of task C included a working memory module with perfect recall of recent outcomes, but fast forgetting and strict capacity limitations. Perfect recall was modeled as an RL process with learning rate $\alpha_{W⁢M+}=1$ that operated on working-memory weights $W⁢(a|s)$ rather than action values. On trials with positive outcomes ($r=1$), the model reduces to:

$$
W_{t+1}⁢(a|s)=r_{t}
$$

On trials with negative outcomes ($r=0$), multiplying $\alpha_{W⁢M+}=1$ with the neglect bias $b$ leads to potentially less-than perfect memory:

$$
W_{t+1}⁢(a|s)=W_{t}⁢(a|s)+b*(r_{t}-W_{t}⁢(a|s))
$$

Working-memory weights $W⁢(a|s)$ were transformed into action policies $p_{W⁢M}⁢(a|s)$ in a similar way as RL weights $Q⁢(a|s)$ were transformed into action probabilities $p_{R⁢L}⁢(a|s)$, using a softmax transform combined with undirected noise:

$$
p⁢(a_{i}|s)=(1-ϵ)*\frac{e⁢x⁢p⁢(\beta⁢Q⁢(a_{i}|s))}{\sum_{a_{j}\ina}e⁢x⁢p⁢(\beta⁢Q⁢(a_{j}|s))}+ϵ*\frac{1}{|a|}
$$

$|a|=3$ is the number of available actions and $\frac{1}{|a|}$ is the uniform policy over these actions; $ϵ$ is the undirected noise parameter.

Forgetting was implemented as a decay in working-memory weights $W⁢(a|s)$ (but not RL Q-values):

$$
W_{t+1}⁢(a|s)_{t+1}=(1-f)*W_{t}⁢(a|s)_{t}+f*\frac{1}{3}
$$

Capacity limitations on working memory were modeled as an adjustment in the weight $w$ of $p_{W⁢M}⁢(a|s)$ compared to $p_{R⁢L}⁢(a|s)$ in the final calculation of action probabilities $p⁢(a|s)$:

$$
w=ρ∗(min(1,\frac{K}{ns}))
$$



$$
p(a|s)=w∗p_{WM}(a|s)+(1−w)∗p_{RL}(a|s)
$$

The free parameter $ρ$ is the probability of using values stored in working memory to choose an action (relative to RL), $n⁢s$ indicates a block’s stimulus set size, and $K$ captures individual differences in working memory capacity.

We fitted a separate RL model to each task, using state-of-the-art methods for model construction, fitting, and validation (Wilson and Collins, 2019; Palminteri et al., 2017). Models for tasks A and B were fitted using hierarchical Bayesian methods with Markov-Chain Monte-Carlo sampling, which is an improved method compared to maximum likelihood that leads to better parameter recovery, amongst other advantages (Gelman et al., 2013; Katahira, 2016; Watanabe, 2013). The model for task C was fitted using classic non-hierarchical maximum-likelihood because model parameter $K$ is discrete, which renders hierarchical sampling less tractable. In all cases, we verified that the model parameters were recoverable by the selected model-fitting procedure, and that the models were identifiable. Details of model-fitting procedures are provided in the original publications (Master et al., 2020; Eckstein et al., 2022; Xia et al., 2021).

For additional details on any of these models, as well as detailed model comparison and validation, the reader is referred to the original publications (task A: Xia et al., 2021; task B: Eckstein et al., 2022; task C: Master et al., 2020).

### Principal component analysis (PCA)

The PCA in section Main axes of variation included 15 model parameters ($\alpha_{+}$ and noise/exploration in each task; Forgetting and $\alpha_{-}$ in two tasks; Persistence in task B; four working memory parameters in task C; see section 'Computational models') and 39 model-free features, including simple behavioral features (e.g. overall performance, reaction times, tendency to switch), results of behavioral regression models (e.g. effect of delay between presentations of the same stimulus on accuracy), and the model parameters of an alternative Bayesian inference model in task B. All behavioral features, including their development over age, are described in detail in Appendix 6 and Appendix 3—figure 1B. For simplicity, section Main axes of variation focused on the first three PCs only; the weights, explained variance, and age trajectories of remaining PCs are shown in Appendix 8—figure 4.

PCA is a statistical tool that decomposes the variance of a dataset into so-called ‘principal components’ (PCs; Abdi and Williams, 2010). PCs are linear combinations of a dataset’s original features (e.g. response times, accuracy, learning rates), and explain the same variance in the dataset as the original features. The advantage of PCs is that they are orthogonal to each other and therefore capture independent aspects of the data. In addition, subsequent PCs explain subsequently less variance, such that selecting just the top PCs of a dataset retains the bulk of the variance and the ability to reconstruct the dataset up to some ceiling determined by random noise. When using this approach, it is important to understand which concept each PC captures. So-called factor loadings, the original features’ weights on each PC, can provide this information.

PCA performs a change of basis: Instead of describing the dataset using the original features (in our case, 54 behaviors and model parameters), it creates new features, PCs, that are linear combinations of the original features and capture the same variance, but are orthogonal to each other. PCs are created by eigendecomposition of the covariance matrix of the dataset: the eigenvector with the largest eigenvalue shows the direction in the dataset in which most variance occurs, and represents the first PC. Eigenvectors with subsequently smaller eigenvalues form subsequent PCs. PCA is related to Factor analysis, and results are very consistent between both methods in our dataset. PCA and FA are often used for dimensionality reduction. In this case, only a small number of PCs / Factors is retained, whereas the majority is discarded, in an effort to retain most variance with a reduced number of features.

We highlight the most central behavioral features here; more detail is provided in 'Appendix 1' and 'Appendix 6'. Response to feedback was assessed using features ‘Win-stay’ (percentage of trials in which a rewarded choice was repeated), and ‘Lose-stay’ (percentage of trials in which a non-rewarded choice was repeated). For task B, we additionally included ‘Win-lose-stay’ tendencies, which is the proportion of trials in which participants stay after a winning trial that is followed by a losing trial. This is an important measure for this task because the optimal strategy required staying after single losses.

We also included behavioral persistence measures in all tasks. In tasks A and C, these included a measure of action repetition (percentage of trials in which the previous key was pressed again, irrespective of the stimulus and feedback) and choice repetition (percentage of trials in which the action was repeated that was previously selected for the same stimulus, irrespective of feedback). In task B, both measures were identical because every trial presents the same stimulus.

We further included task-specific measures of performance. In task A, these were: the average accuracy for the first three presentations of each stimulus, reflecting early learning speed; and the asymptote, intercept, and slope of the learning progress in a regression model predicting performance (for details about these measures, see Xia et al., 2021). In task B, task-specific measures of performance included the number of reversals (because reversals were performance-based); and the average number of trials to reach criterion after a switch. In tasks A and C, we also included a model-independent measure of forgetting. In task A, this was the effect of delay on performance in the regression model mentioned above. In task C, this was the effect of delay in a similar regression model, which also included set size, the number of previous correct choices, and the number of previous incorrect choices, whose effects were also included. Lastly for task C, we included the slope of accuracy and response times over set sizes, as measures of the effect of set size on performance. For task B, we also included the difference between early (first third of trials) and late (last third) performance as a measure of learning. To avoid biases in the PCA toward any specific task, we included equal numbers of behavioral features for each task. Before performing the PCA, we individually standardized each feature, such that each feature was centered with a mean of 0 and a standard deviation of 1.

To facilitate the interpretation of PC2 and PC3, we normalized the loadings (PCA weights) of each feature (behavioral and model parameter) with respect to PC1, flipping the loadings of all features in PC2 and PC3 that loaded negatively on PC1. This step ensured that the directions of factor loadings on PC2 and PC3 were interpretable in the same way for all features, irrespective of their role for task performance, and revealed the encoding of task contrasts.

### Ridge regression

In sections Parameters and cognitive processes and parameters and behavior, we use regularized, cross-validated Ridge regression to determine whether parameters captured overlapping variance, which would point to an overlap in cognitive processes. We used Ridge regression to avoid problems that would be caused by overfitting when using regular regression models. Ridge regression regularizes regression weight parameters $w$ based on their L2-norm. Regular regression identifies a vector of regression weights $w$ that minimize the linear least squares $||y-w⁢X||_{2}^{2}$. Here, $||a||_{2}^{2}=\sqrt{\sum_{a_{i}\inx}a_{i}^{2}}$ is the L2-norm of a vector $a$, vector $y$ represents the outcome variable (in our case, a vector of parameters, one fitted to each participant), matrix $X$ represents the predictor variables (in our case, either several behavioral features for each participant [section 'Parameters and cognitive processes'], or several parameters fitted to each participant [section 'Parameters and behavior']), and vector $w$ represents the weights assigned to each feature in $X$ (in our case, the weight assigned to each predicting behavioral pattern or each predicting parameter).

When datasets are small compared to the number of predictors in a regression model, exploding regression weights $w$ can lead to overfitting. Ridge regression avoids this issue by not only minimizing the linear least squares like regular regression, but also the L2 norm of weights $w$, that is, by minimizing $||y-w⁢X||_{2}^{2}+\alpha*||w||_{2}^{2}$. Parameter $\alpha$ is a hyper-parameter of Ridge regression, which needs to be chosen by the experimenter. To avoid bias in the selection of $\alpha$, we employed repeated cross-validated grid search. At each iteration of this procedure, we split the dataset into a predetermined number $s\in$ [2, 3, …, 8] of equal-sized folds, and then fitted a Ridge regression to each fold, using values of $\alpha\in$ [0, 10, 30, 50, 100, 300, …, 10,000, 100,000, 1,000,000]. For each $s$, we determined the best value of $\alpha$ based on cross-validation between folds, using the amount of explained variance, $R^{2}$, as the selection criterion. To avoid biases based on the random assignment of participants into folds, we repeated this procedure $n=100$ times for each value of $\alpha$. To avoid biases due to the number of folds, the entire process was repeated for each $s$, and the final value of $s$ was selected based on $R^{2}$. We used the python package ‘scikit learn’ (Pedregosa et al., 2011) to implement the procedure.

We conducted three models per parameter to determine the relations between parameters: predicting each parameter from all the parameters of each of the other two tasks (2 models); and predicting each parameter from all parameters of both other tasks combined (1 model; Figure 4A). We conducted the same three models per parameter to determine the relations between parameters and behaviors, predicting each parameter from behavioral features of the other tasks (Figure 4A). In addition, we conducted a fourth model for behaviors, predicting each parameter from the behaviors of all three tasks combined, to assess the contributions of all behaviors to each parameter (Figure 4C). Meta-parameters $s$ and $\alpha$ were allowed to differ (and differed) between models. The final values of $R^{2}$ (Figure 4B and D) and the final regression weights $w$ (Figure 4A and C; Table 6) were determined by refitting the winning model.

### Data Availability

The data collected for this study are openly available at osf.io/h4qr6/. The analysis code is available at https://github.com/MariaEckstein/SLCN/blob/master/models/MetaSLCN-01ReadInData.ipynb. (copy archived at swh:1:rev:4fb5955c1142fcbd8ec80d7fccdf6b35dbfd1616, Eckstein, 2022).
