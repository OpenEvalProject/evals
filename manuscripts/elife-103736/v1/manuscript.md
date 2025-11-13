# Hunger shifts attention and attribute weighting in dietary choice

## Authors

- Jennifer March<sup>1</sup> ([ORCID: 0009-0002-3133-8170](https://orcid.org/0009-0002-3133-8170)) †
- Sebastian Gluth<sup>1</sup> ([ORCID: 0000-0003-2241-5103](https://orcid.org/0000-0003-2241-5103))

### Affiliations

1. Department of Psychology and Hamburg Center of Neuroscience, University of Hamburg Hamburg Germany ([ROR:00g30e956](https://ror.org/00g30e956))

† Corresponding author

## Abstract

Hunger is a biological drive which can promote unhealthy dietary decisions. Yet, the cognitive mechanisms underlying this effect, and in particular the interactive role of attention and choice processes, remain elusive. To address this gap, we conducted an eye-tracking experiment, in which 70 participants completed a multi-attribute food choice task in hungry and sated states. Confirming our preregistered hypotheses, participants’ preference for tasty over healthy food items was amplified by hunger. Attention mediated this influence of hunger, as hungry participants focused more on tasty options, leading them to make less healthy decisions. Rigorous model comparisons revealed that an extension of the recently proposed multi-attribute attentional drift diffusion model best explained choice and response times. According to this model, hunger did not only increase the relative taste compared to health weight, but it also increased the fixation-related discounting of health but not taste information. Our results suggest that the cognitive mechanisms underlying unhealthy dietary decisions under hunger are characterized by a nuanced interplay between attention and the significance assigned to the options’ underlying attributes.

## Introduction

Throughout a single day, we make numerous food choices. These choices are largely influenced by the food and its environment, as well as by the decision maker’s trait and state factors (Chen and Antonelli, 2020). For example, it has been shown that health information such as nutritional scores on food options (Rramani et al., 2020) or health primes (Hare et al., 2011; Sullivan and Huettel, 2021) can increase the number of healthy choices. On the other hand, a hungry decision maker is more likely to make unhealthy decisions (Cheung et al., 2017; Hoefling and Strack, 2010). Evolutionarily, a preference for energy dense foods was adaptive and ensured survival under conditions of scarcity (Hanßen et al., 2022; Mattson, 2019). While the food environment in Western societies has become increasingly obesogenic, with high caloric food options being affordable and easily available, the neurobiological mechanism continues to reward the consumption of energy dense foods contributing to a global surge in obesity rates (Mitchell et al., 2011; World Health Organization, 2021; Lobstein et al., 2023). The critical involvement of reward circuitries in the brain in determining food choice highlights the importance of cognitive affective drivers, alongside homeostatic ones, in shaping food-related behavior (Plassmann et al., 2022; Rangel, 2013). Here, we set out to shed light on these cognitive mechanisms underlying food choice which drive energy intake and weight, by investigating the effect of hunger on attention and valuation processes in multi-attribute dietary choice.

Consistent with the evolutionary mechanism that reinforces high-energy dense food options, behavioral (Cameron et al., 2014; Cheung et al., 2017; Epstein et al., 2003), and neuroimaging studies (e.g. Banica et al., 2023; Dagher, 2012; Malik et al., 2008) indicate that under hunger (high-caloric) food options are viewed more rewarding, are more frequently chosen over healthy alternatives, and draw more attention. Meta-analyses have revealed an attentional bias towards food versus neutral stimuli, which was further amplified by hunger state (Hardman et al., 2021; Pool et al., 2016). Given these findings, it appears critical to thoroughly understand the interplay between attention and decision-making processes in shaping maladaptive food choices under hunger. To better explain the mechanisms by which hunger affects attention and valuation processes in dietary choice, we leverage recent advances in modeling attentional dynamics in the accumulation of evidence in decision-making (Gluth et al., 2020; Krajbich et al., 2010; Shimojo et al., 2003). This work has provided evidence for a strong positive association between the time people spend looking at a (food) option and the probability with which they choose it (Krajbich, 2019). Recently, these models have also incorporated the distinct attentional influence of the options’ underlying attributes such as taste and health (Fisher, 2021; Yang and Krajbich, 2023). To the best of our knowledge, there is no study modeling attention and choice dynamics under different hunger states leaving the cognitive and attentional mechanisms underlying hunger-driven food choice unknown.

To fill this gap, we conducted a within-subject experiment, in which 70 participants completed a binary food choice task in hungry and sated states while their eye movements were being recorded (Figure 1). The considered attributes of the binary options were taste and health as represented by food images and their nutritional scores, respectively. Confirming our preregistered hypotheses, participants were more likely to choose tasty over healthy food items, and this difference was amplified under hunger. Notably, attention mediated the influence of hunger on dietary decisions, as participants focused more on taste information under hunger, leading them to make less healthy decisions. To better understand the cognitive mechanisms underlying hunger-driven dietary choice, we implemented different variants of the diffusion decision model (DDM, Ratcliff, 1978), which included the consideration of both attributes (Maier et al., 2020; Sullivan and Huettel, 2021) and the incorporation and extension of attentional mechanisms (Fisher, 2021; Krajbich et al., 2010; Yang and Krajbich, 2023). Critically, we extended the recently proposed multi-attribute attentional DDM (Yang and Krajbich, 2023) to allow the discounting of unattended information to differ across different attributes (here: taste vs. health). This model not only provided the best account of our behavioral data, but also revealed a twofold mechanism, wherein hunger affects valuation of choice options by shifting the relative weighting of taste information and by exacerbating the attentional discounting of health (but not taste) information.

![Figure 1.](https://cdn.elifesciences.org/articles/103736/elife-103736-fig1-v1.jpg)

**Figure 1.:** (a) Food rating task. Participants rated all food images and their corresponding Nutri-Scores (see Methods) in terms of taste, health, wanting, and perceived caloric content on a continuous scale (b) Trial sequence of food choice task. In each trial, participants made a binary choice between two food options represented by food image and corresponding Nutri-Scores; Feedback and fixation-based fixation dots were implemented (c) Experimental procedures; blue refers to sated, yellow to hungry condition (order counterbalanced). VAS refers to visual analog scale used to assess subjective feelings of hunger. Positive and negative affect scale (PANAS) refers to a questionnaire assessing mood (see Appendix 1). FEV II refers to a questionnaire assessing eating behavior (see Appendix 2); *indicates that these steps were only required in the first session.

## Results

We used a within-subject experiment, in which 70 participants were tested in hungry and sated conditions in counterbalanced order. In the sated condition, participants received a Protein Shake, with its size being determined by their metabolic rate (see Methods). The experiment consisted of a food rating and a multi-attribute binary food choice task, as well as control measures including hunger state, mood, and eating behavior (Figure 1; see Methods for details).

### Hunger state manipulation

First, we tested whether the manipulation of hunger state was successful (Figure 2a). Upon arrival at the lab, participants’ hunger ratings did not differ between the stated condition ($M_{satedt1}=51.98$, $SD_{satedt1}=27.54$) and the hungry condition ($M_{hungryt1}=57.99$, $SD_{hungryt1}=23.54$, t(63)=-1.265, p=0.211, d=0.159). The RM-ANOVA indicated that the change in hunger ratings between the last and first time point differed across conditions (F(1)=26.31, p<.001, d=0.708). Specifically, in the hungry condition the change was positive, meaning participants got hungrier throughout the experiment ($M_{hungrydiff}=22.4$, $SD_{hungrydiff}=20$), whereas in the sated condition, this difference was negative ($M_{sateddiff}=−36.3$, $SD_{sateddiff}=31.3$). Thus, our hunger state manipulation had the desired effect on the subjective feeling of hunger. Notably, there were no effects of hunger state on positive and negative affect across timepoints (Appendix 1—figure 1).

![Figure 2.](https://cdn.elifesciences.org/articles/103736/elife-103736-fig2-v1.jpg)

**Figure 2.:** (a) Manipulation check: The green boxplot displays the difference (hungry-sated) in hunger state at arrival at the lab, yellow and blue boxplots display the difference (last timepoint-first timepoint) in hunger state in the hungry and sated condition, respectively. (b) Response time (RT) quantile plot displaying the cumulative probability of tasty (dashed lines) and healthy choices (solid lines) separately for the two conditions (quantiles are 0.1, 0.3, 0.5, 0.7, 0.9 of choices). (c, d) Probability to choose the left option as a function of taste and health value difference (left-right), respectively. Importantly, the dependency of choice on health information was eliminated under hunger. (e, f) Corresponding mean RTs as a function of taste and health value difference, respectively. For illustration purposes, value differences were segmented into 25 bins, and a locally weighted scatterplot smoothing technique was applied with a span of 0.75. Plots (c–f) are based on all trials. Transparent shades indicate the standard errors of the smoothed choice probability and RT for the respective value bins (see also Figure 2—figure supplement 3).

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/103736/elife-103736-fig2-figsupp1-v1.jpg)

**Figure 2—figure supplement 1.:** Screeplot, the first component positively loads on health rating and Nutri-Score and negatively on objective and subjective caloric content, the second component positively loads on taste and wanting ratings.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/103736/elife-103736-fig2-figsupp2-v1.jpg)

**Figure 2—figure supplement 2.:** vd refers to value difference left – right option.

![Figure 2—figure supplement 3.](https://cdn.elifesciences.org/articles/103736/elife-103736-fig2-figsupp3-v1.jpg)

**Figure 2—figure supplement 3.:** Response time (RT) quantile plot displaying the cumulative probability separately for the two conditions (blue = sated condition and yellow = hungry condition) of (a) higher wanted (dashed lines) and healthy choices (solid lines); and (b) higher caloric (dashed lines) and lower caloric choices (solid lines) (quantiles are 0.1, 0.3, 0.5, 0.7, 0.9 of choices).

![Figure 2—figure supplement 4.](https://cdn.elifesciences.org/articles/103736/elife-103736-fig2-figsupp4-v1.jpg)

**Figure 2—figure supplement 4.:** (a–c) Probability to choose the left option as a function of wanting, subjective caloric content, and Nutri-Score value difference (left-right), respectively. Higher wanted options increased probability of choice, irrespective of condition. While lower calories and a better Nutri-Score promoted choice in the sated condition, this dependency was eliminated under hunger (d-f). Corresponding mean response times (RTs) as a function of wanting, subjective caloric content, and Nutri-Score value difference (left-right), respectively. Importantly, the pattern of the wanting plots (a) and (d) closely corresponds to those of the taste plots (Figure 2c and e), while the pattern of the Nutri-Score plots closely corresponds to those of the health plots (Figure 2d and f). For illustration purposes, value differences were segmented into 25 bins, and a locally weighted scatterplot smoothing technique was applied with a span of 0.75. Plots are based on all trials. Transparent shades indicate the standard errors of the smoothed choice probability and RT for the respective value bins.

### Drivers of food choice

For each food item, we had six measures: Nutri-Score, four subjective ratings (taste, health, wanting, estimated caloric content), and objective caloric content. To assess whether our preregistered goal to study dietary decisions in terms of contrasting taste vs. health aspects was justified, we performed a principal component analysis (PCA) on these measures. Results revealed that 81% of variance was explained by two components, the first loading positively on caloric information (subjective and objective) and negatively on health information (subjective health rating and Nutri-Score), while the second one loaded positively on taste and wanting (Figure 2—figure supplements 1 and 2). Importantly, loadings of taste measures on the health component and loadings of health measures on the taste component were low suggesting independence of these factors. As the PCA clearly suggested our different measures to be linked to participants’ decisions by two main components that represent health and taste aspects, respectively, we focus on tasty vs healthy decisions in our main behavioral and modeling analyses.

### Effect of hunger state on choice and RT

In both conditions, a larger value difference (VD) with respect to taste was predictive of tasty choice (Figure 2c), while a larger VD with respect to health was predictive of healthy choice, particularly in the sated condition (Figure 2d). The GLMM of choice (tasty vs. healthy) indicated that overall participants preferred tasty over healthy options ($\beta_{intercept}=0.73$, SE = 0.098, p<0.001). In line with our preregistered hypotheses, we found that participants were less likely to choose the tasty option when being sated as compared to hungry ($\beta_{sated}=−0.211$, SE = 0.103, p=0.04). Moreover, longer relative dwell time on the tasty option increased the likelihood of tasty choice ($\beta_{dwelltime}=0.998$, SE = 0.027, p<0.001) (Figure 3a) (see Appendix 4—table 1 for model specifications, random effects, and an alternative model with additional predictors).

![Figure 3.](https://cdn.elifesciences.org/articles/103736/elife-103736-fig3-v1.jpg)

**Figure 3.:** (a) Dwell time difference between the tasty and healthy option was positively associated with the probability of choosing the tasty option in both conditions. (b) The average probability to look at food image (taste attribute) compared to Nutri-Score (health attribute) was even higher in the hungry than sated condition. (c) Path diagram with posterior means of the parameters, associated 95%-credible interval in squared brackets.

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/103736/elife-103736-fig3-figsupp1-v1.jpg)

**Figure 3—figure supplement 1.:** (a) Proportion (y-axis) of last fixation by category (x-axis) (b) Proportion (y-axis) of first fixation by category (x-axis) (c) Proportion (y-axis) of first fixation by location on the screen (y-axis) (d) Fixation transitions across participants and conditions. In line with the strong tendency to fixate food images, rather than the Nutri-score, participants’ fixations mostly switched within attributes ($M_{sated}=0.868$, $SD_{sated}=0.14$; $M_{hungry}=0.899$, $SD_{hungry}=0.108$), with only few transitions within alternatives ($M_{sated}=0.096$, $SD_{sated}=0.105$; $M_{hungry}=0.073$, $SD_{hungry}=0.081$), and even fewer transitions being diagonal ($M_{sated}=0.037$, $SD_{sated}=0.038$; $M_{hungry}=0.028$, $SD_{hungry}=0.029$). We performed the Wilcoxon rank sum test due to violations against normality, which revealed no differences between conditions across transition types (diagonal: W=2152.5, p=0.216; within alternative: W=2189.5, p=0.279; within attribute: W=2750.5, p=0.211). We further used the Payne index (Payne, 1976) to describe participants’ search patterns, confirming that search was mostly attribute-based: hungry participants had a Payne index of –0.846 ($SD_{hungry}=0.178$) and sated participants one of –0.793 ($SD_{sated}=0.234$), with no difference between conditions (W=2189.5, p=0.279). Blue indicates sated condition, yellow indicates hungry condition.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/103736/elife-103736-fig3-figsupp2-v1.jpg)

**Figure 3—figure supplement 2.:** a is the effect of hunger state to attention, b is the effect from attention to choice, cp is the indirect effect of hunger state on choice taking attention into account, c is the direct effect of hunger state on choice, when not considering attention, me refers to the mediation effect, thus the combination of paths a and b, pme refers to the proportion of the effect that is mediated. Output refers to posterior, mean, standard deviation (=standard error; SE), median, and credible interval respectively. n_eff refers to the number of effective posterior samples, to obtain confident estimates, it is recommended to be >100 Vuorre and Bolger, 2018; R-hat is the scale reduction factor, to accurately predict posterior distributions, it should be 1.00, according to Vuorre and Bolger, 2018 values within 0.05 are acceptable.

![Figure 3—figure supplement 3.](https://cdn.elifesciences.org/articles/103736/elife-103736-fig3-figsupp3-v1.jpg)

Importantly, we assessed the robustness of our findings by testing alternative GLMMs to predict choices, in which we replaced the taste/health ratings as predictors by wanting/health ratings (Appendix 5—table 1) and by high/low caloric information (Appendix 6—table 1). Of note, the effects of hunger on higher wanted vs healthy and high vs low caloric choice were markedly stronger (Appendix 5—table 1, Appendix 6—table 1, Figure 2—figure supplement 3).

With respect to response time (RT), we found that RT was highest for choices in which taste ratings were similar for both options (Figure 2e), while health value did not affect RT (Figure 2f). The GLMM of RT indicated an average RT of 2.748 s (SE = 0.096). Tasty choices were associated with faster decisions, decreasing RT by 0.15 s (SE = 0.018, p<0f.001). Longer relative dwell time on the tasty option predicted slower choice in general ($\beta_{dwelltime}=0.065$, SE = 0.014, p<0.001), but was sped-up for tasty choices ($\beta_{dwelltime∗tastychoice}=−0.13$, SE = 0.017, p<0.001) (see Appendix 4—table 2 for model specifications, random effects, and an alternative model with additional predictors).

Altogether, we found that participants preferred tasty over healthy options, and that this preference was amplified under hunger. While tasty choices were faster in general, we did not find an effect of hunger state on RT. Finally, our GLMMs indicate that dwell time is an important predictor of choice and RT.

### Hunger affects attention and dietary choice

In line with previous work (Gluth et al., 2018; Krajbich et al., 2010; Weilbächer et al., 2021; Yang and Krajbich, 2023), our choice GLMM indicated that looking longer at the tasty option predicted tasty choice. This effect was observed in both conditions to a very similar degree (Figure 3a). When analyzing dwell time on the attribute level, however, there was a significant condition difference: Although participants were much more likely to look at food images (taste attribute) than the Nutri-Scores (health attribute) in both conditions, this difference was even more pronounced in the hungry compared to the sated state (t(69)=2.595, P=.006, d=0.312; Figure 3b). This effect remained significant after excluding outlier data (t(68)=2.392, P=.01, d=0.29). First and last fixations and transition patterns are shown in Figure 3—figure supplement 1.

The analysis so far suggests that dwell time depends on hunger state (Figure 3b) and is predictive of choice (Figure 3a). To better understand these interactions, we conducted a hierarchical Bayesian mediation analysis testing whether attention (i.e. dwell time) mediates the relationship between hunger state and food choice (Figure 3C, Figure 3—figure supplements 2 and 3). In line with our GLMM on choice, the direct path between hunger state and food choice was significant ($M_{c}=0.27$, $SE_{c}=0.12$, $CI_{c}=[0.03,0.52]$), meaning hungry individuals were more likely to choose tasty options. Similarly, the path between attention and food choice was significant ($M_{b}=5.41$, $SE_{b}=0.45$, $CI_{b}=[4.54,6.32]$), indicating that longer dwell times on the tasty option were predictive of choosing that option. Furthermore, there was a small yet significant relationship between hunger state and attention ($M_{a}=0.01$, $SE_{a}=0.01$, $CI_{a}$=[<0.001, 0.022]), demonstrating that hungry individuals paid relatively more attention to tasty options. Critically, our mediation analysis revealed that the direct path between hunger state and food choice was no longer significant when attention was considered ($M_{cp}=0.19$, $SE_{cp}=0.11$, $CI_{cp}$=[–0.02, 0.41]), while the population-level mediation path (a*b) was significant ($M_{a∗b}=0.08$, $SE_{a∗b}=0.04$, $CI_{a∗b}$=[0.01, 0.16]). Alternative mediation models (with wanting ratings or caloric information are reported in Appendix 7—tables 1–4).

Altogether, the eye-tracking analyses demonstrated that attention was predictive of choice, and hungry participants’ preference for tasty foods was reflected in their dwell time. Finally, attention emerged as a pivotal mediator of the relationship between hunger state and food choice.

### Mechanisms underlying the effect of hunger on attention and dietary choice

In line with our hypotheses, we found that participants were more likely to choose tasty over healthy food items, and this difference was amplified by hunger (Figure 2b). Moreover, we demonstrated that attention mediated the effect of hunger on choice (Figure 3c). To further elucidate the cognitive processes underlying these effects, we estimated and compared different versions of DDMs against one another using hierarchical Bayesian cognitive modeling. Models varied in terms of whether and how they accounted for attention and whether a starting point bias (towards tasty vs. healthy options) was included (see Methods) Figure 4. We report parameter estimates for all models (Figure 5, Figure 5—figure supplement 1 and Appendix 8—figures 1–6), as well as posterior predictive checks (Figure 4, Figure 4—figure supplement 1 and Appendix 9—figure 1) and recoveries (Appendix 10—figures 1–4) for the best fitting models.

![Figure 4.](https://cdn.elifesciences.org/articles/103736/elife-103736-fig4-v1.jpg)

**Figure 4.:** Posterior predictive checks maaDDM2 $ϕ$.Quantile plots of simulated data with fitted parameters of the maaDDM2 $ϕ$ in blue (sated) and yellow (hungry) with highest density intervals (HDI) of each quantile (vertical lines) and behavior. Posterior predictive checks were performed by drawing 1000 parameter values from the individual posterior parameter distribution to simulate the new data.

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/103736/elife-103736-fig4-figsupp1-v1.jpg)

**Figure 4—figure supplement 1.:** Quantile plots of simulated data with fitted parameters of the maaDDM in blue (sated) and yellow (hungry) with highest density intervals (HDI) of each quantile (vertical lines) and behavior. Posterior predictive checks were performed by drawing 1000 parameter values from the individual posterior parameter distribution to simulate the new data.

![Figure 5.](https://cdn.elifesciences.org/articles/103736/elife-103736-fig5-v1.jpg)

**Figure 5.:** Parameter estimates of maaDDM2 $ϕ$.Group parameter estimates (blue = sated, yellow = hungry; left panels) and the effect of hunger state (gray; right panels). Dashed black lines indicate the 95% HDI. (a) Estimated taste weights. In both conditions the weight is larger than 0.5, indicating a higher weight on taste compared to health. This preference was even stronger under hunger. (b–f) Parameter estimates of $d$, nDT, $\alpha$, $\theta$ and $ϕ_{T}$, and the corresponding effects of hunger state. (g) Parameter estimates of $ϕ_{H}$ and the corresponding effects of hunger state, showing that the attention-driven discounting of health information was amplified under hunger.

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/103736/elife-103736-fig5-figsupp1-v1.jpg)

**Figure 5—figure supplement 1.:** Fitted parameters across participants (blue = sated, yellow = hungry; left panels) and the effect of hunger state (gray; right panels). Dashed black lines indicate the 95% highest density interval (HDI) edges. If ‘0’ (red line) is included in HDI, no credible difference between conditions (a) Estimated relative taste weight across participants. In both conditions, the relative taste weight is larger than 0.5, indicating that participants generally weigh taste more than health. There is a positive shift in the distribution of this effect, and the HDI does not include 0, indicating that hungry individuals have a higher relative taste weight (b–e). Estimated parameter values for drift scaling, non-decision time (nDT), boundary separation, and theta across participants and the corresponding effects of hunger state. (f) Estimated parameter values for phi across participants. The corresponding effect of hunger indicates that hungry participants discount the non-looked upon attribute more strongly.

Initial model comparison revealed that there was no evidence for a starting point effect, as models without starting point consistently outperformed models with starting point. In addition, the multi-attribute attentional DDMs (maaDDM and maaDDM2 $ϕ$), which allow modeling discounting of unattended options as well as unattended attributes, outperformed simpler variants (i.e. DDM, aDDM) (Table 1).

**Table 1.**
 Quantitative model comparison.


<table>
  <thead>
    <tr>
      <th>Model</th>
      <th>α\begin{document}$\alpha $\end{document}</th>
      <th>nDT</th>
      <th>d\begin{document}$d$\end{document}</th>
      <th>ω\begin{document}$\omega $\end{document}</th>
      <th>β\begin{document}$\beta $\end{document}</th>
      <th>θ\begin{document}$\theta $\end{document}</th>
      <th>ϕ1\begin{document}$\phi _{1}$\end{document}</th>
      <th>ϕ2\begin{document}$\phi _{2}$\end{document}</th>
      <th>DIC</th>
      <th>Rhat</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>DDM</td>
      <td>YES</td>
      <td>YES</td>
      <td>YES</td>
      <td>YES</td>
      <td>NO</td>
      <td>NO</td>
      <td>NO</td>
      <td>NO</td>
      <td>69646</td>
      <td>1.002</td>
    </tr>
    <tr>
      <td>DDMsp</td>
      <td>YES</td>
      <td>YES</td>
      <td>YES</td>
      <td>YES</td>
      <td>YES</td>
      <td>NO</td>
      <td>NO</td>
      <td>NO</td>
      <td>69668</td>
      <td>1.004</td>
    </tr>
    <tr>
      <td>aDDM</td>
      <td>YES</td>
      <td>YES</td>
      <td>YES</td>
      <td>YES</td>
      <td>NO</td>
      <td>YES</td>
      <td>NO</td>
      <td>NO</td>
      <td>65561</td>
      <td>1.004</td>
    </tr>
    <tr>
      <td>aDDMsp</td>
      <td>YES</td>
      <td>YES</td>
      <td>YES</td>
      <td>YES</td>
      <td>YES</td>
      <td>YES</td>
      <td>NO</td>
      <td>NO</td>
      <td>65587</td>
      <td>1.003</td>
    </tr>
    <tr>
      <td>maaDDM</td>
      <td>YES</td>
      <td>YES</td>
      <td>YES</td>
      <td>YES</td>
      <td>NO</td>
      <td>YES</td>
      <td>YES</td>
      <td>NO</td>
      <td>65155</td>
      <td>1.005</td>
    </tr>
    <tr>
      <td>maaDDMsp</td>
      <td>YES</td>
      <td>YES</td>
      <td>YES</td>
      <td>YES</td>
      <td>YES</td>
      <td>YES</td>
      <td>YES</td>
      <td>NO</td>
      <td>65214</td>
      <td>1.011</td>
    </tr>
    <tr>
      <td>maaDDM2 ɸ</td>
      <td>YES</td>
      <td>YES</td>
      <td>YES</td>
      <td>YES</td>
      <td>NO</td>
      <td>YES</td>
      <td>YES</td>
      <td>YES</td>
      <td>64002</td>
      <td>1.017</td>
    </tr>
    <tr>
      <td>maaDDM2 ϕ\begin{document}$\phi $\end{document} sp</td>
      <td>YES</td>
      <td>YES</td>
      <td>YES</td>
      <td>YES</td>
      <td>YES</td>
      <td>YES</td>
      <td>YES</td>
      <td>YES</td>
      <td>65070</td>
      <td>1.027</td>
    </tr>
  </tbody>
</table>

_The first column states the name of the model; the following nine columns indicate whether the drift diffusion model (DDM) variants included a given parameter or not. α\begin{document}$\alpha $\end{document} refers to the boundary separation; nDT refers to non-decision time; d\begin{document}$d$\end{document} refers to the drift scaling parameter; ω\begin{document}$\omega $\end{document} refers to the relative taste compared to health weight; β\begin{document}$\beta $\end{document} refers to the starting point bias; θ\begin{document}$\theta $\end{document} refers to the discounting of the non-looked upon option; ϕ1\begin{document}$\phi _{1}$\end{document} refers to the discounting of the non-looked upon attribute, in case the model includes ϕ1\begin{document}$\phi _{1}$\end{document} and ϕ2\begin{document}$\phi _{2}$\end{document} they refer to the discounting of taste and heath information, respectively; The deviance information criterion (DIC) was used as goodness-of-fit measure. Rhat is the scale reduction factor, to accurately predict posterior distributions, it should be 1.00, according to Vuorre and Bolger, 2018 values within 0.05 are acceptable. The best model (i.e. maaDDM2 ϕ\begin{document}$\phi $\end{document}) is highlighted in bold._

Further inspection of differences in the maaDDM’s parameter estimates between the hungry and sated conditions suggested that hunger increased the weight of taste information relative to health information and exacerbated attribute-wise attentional discounting i.e., lower estimates of parameter ϕ (Figure 5—figure supplement 1). To shed more light on this attentional effect of hunger, we tested an extension of the maaDDM that assumed two separate attribute-wise discounting parameters for taste and health information (i.e. maaDDM2ϕ, see also Figure 6). Remarkably, this model provided a substantially improved model fit compared to the maaDDM and all other models (Table 1). Moreover, the posterior predictive checks of this model indicated that it provides an exquisite account of the choice and RT data (Figure 4). Again, we assessed the robustness of our results by also testing additional models in which health and taste attributes were replaced by Nutri-Scores (Appendix 11—table 1, Appendix 11—figures 1–8) and wanting (Appendix 12—table 1, Appendix 12—figures 1–4), respectively. Importantly, these complementary modeling analyses yielded comparable quantitative and qualitative results.

![Figure 6.](https://cdn.elifesciences.org/articles/103736/elife-103736-fig6-v1.jpg)

**Figure 6.:** Illustration of the maaDDM2 $ϕ$.The decision-making process underlying choice and response time (RT) data as conceived by the maaDDM2ϕ. The decision is assumed to emerge from a noisy evidence-accumulation process commencing from the starting point ($\beta$) and terminating at one of the two boundaries (here: 0=healthy boundary and  $\alpha$ = tasty boundary) representing the tasty and healthy choice, respectively. The non-decision time (nDT) reflects processes unrelated to the decision itself, here illustrated as stimulus encoding time. The drift rate represents the rate of evidence accumulation. It is determined by the scaled value difference (VD) of the displayed options, which in turn is given by the taste (T) and health (H) ratings of the options, the relative weight of tastiness $\omega$ vs. healthiness (1- $\omega$) as well as the currently attended item on the screen as illustrated by the differently colored segments and the corresponding images. The coloring scheme of the VD equation shows which part of the equation defines the drift rate at any given attended item. Attending to the tasty option (here: chocolate bar with Nutri-Score E), and in particular to its taste information (i.e. the image), increases the drift towards the tasty boundary (orange), while attending to the healthy option (here: cucumber with Nutri-Score B), and in particular to its health information (i.e. the Nutri-Score) increases the drift towards the healthy boundary (green).

Taking a closer look at the group parameter distributions of the winning model (i.e. maaDDM2 $ϕ$), we examined the highest density intervals (HDI), which reflects the part of the posterior distributions that contain 95% of all values. We found that participants relative taste weight was larger than 0.5 in both conditions, indicating a higher taste compared to health preference ($HDI_{sated}$=[0.698,0.831]; $HDI_{hungry}$=[0.788,0.922]), as the HDIs did not include 0.5. Critically, this preference was credibly higher under hunger (HDI=[0.122, 0.642]; Figure 5a), as the HDI of the effect of hunger did not include 0. We did not find differences between conditions with respect to the drift scaling parameter $d$ (HDI=[–0.165, 0.025]; Figure 5b), the non-decision time nDT (HDI=[–0.02, 0.087]; Figure 5c), or the boundary separation $\alpha$ (HDI = [–0.12, 0.18]; Figure 5d). Similarly, there were no credible hunger effects with respect to the attentional discounting of the options $\theta$ (HDI = [–0.092, 0.017]; Figure 5e). Looking at the two attribute-wise attentional discounting parameters revealed that there was no condition effect on discounting of the taste attribute (i.e. $ϕ_{T}$, HDI=[–0.291, 0.16]; Figure 5f), but instead, hunger exclusively increased the discounting of health information (i.e. $ϕ_{H}$, HDI=[-1.088,–0.188]; Figure 5g).

Taken together, our extension of the multi-attribute attentional DDM with separate attention parameter for taste and health attributes (i.e. maaDDM2 $ϕ$) provided the best quantitative and an excellent qualitative account of the data, and it suggests that hunger affects the relative weighting of taste compared to health information and further increases the discounting of unattended health information during the evidence-accumulation process.

## Discussion

The goal of this study was to elucidate the cognitive mechanisms driving dietary choice under hunger. We found that individuals prefer tasty over healthy food options, and that this preference is amplified by hunger state. This pattern was also reflected in our modeling analyses, revealing that taste was weighted more than health in both, but especially in the hungry condition. Our mediation analysis suggests that the cognitive mechanism underlying the influence of hunger state on food choice is driven by a shift in attention. Specifically, hungry individuals pay more attention to tasty food options in general and the taste attribute in particular, which in turn increases the probability of tasty choices. Again, our cognitive modeling analyses integrated these findings, demonstrating increased attentional discounting of the health attribute under hunger. Together, our findings suggest a nuanced interplay between attention and the significance assigned to the options’ underlying attributes in dietary decision-making.

First, in line with previous research (Cheung et al., 2017; Otterbring, 2019; Read and Leeuwen, 1998) we demonstrate that hunger affects dietary choice. Participants were more likely to choose options that were rated more tasty than healthy, for which reported higher wanting, and that contained higher caloric content. Moreover, our findings indicate that higher taste ratings were strongly predictive of choice across conditions, whereas higher health ratings only predicted choice in the sated condition, albeit less influential than taste ratings (Figure 2c and d). Crucially, our modeling analyses endorsed this account: across models, we demonstrate that the relative taste weight was larger in both conditions and particularly in the hungry condition. This finding adds to previous work demonstrating the distinct influence of taste and health attributes in guiding choice (Barakchian et al., 2021; Enax et al., 2016; Hutcherson and Tusche, 2022; Maier et al., 2020; Rramani et al., 2020), by illustrating that these effects can differ across states. This also aligns with results from a food bidding task (Fisher and Rangel, 2014), wherein the authors find that hunger elevated the bids and speculate that this effect was driven by an increased taste but not health valuation of food items.

Second, we show that the valuation is not only influenced by the attributes underlying decision weights, but moreover by attention. Behaviorally, we show that attention mediates the impact of hunger state on food choice, such that hunger state predicts overall less dwell time on the healthy option, thereby increasing the probability of tasty choice. Upon closer examination of attention allocation to the respective attributes, we show that participants, especially when hungry, spent much more time on food images compared to Nutri-Scores. We see two explanations for the excessively high proportion of dwell time on food images compared to Nutri-Scores: First, food images were more important for deciding, as indicated by the relative weight parameter being larger than 0.5. Consequently and in line with previous work (Orquin et al., 2021), people pay more attention to more important attributes. Second, food images contain more complex information. Whereas extracting taste information from a food image can be seen as a complex inference process, a (color-coded) nutritional score provides salient and easily discernible evidence about a product’s healthiness and consequently requires less dwell time. This account is supported by studies showing that nutritional scores can promote healthy choice despite proportionally little dwell time (e.g. Bialkova et al., 2014; Gabor et al., 2020; Rramani et al., 2020).

To take these putatively different attentional demands of different attributes into account, we extended the maaDDM of Yang and Krajbich, 2023 and developed the maaDDM2 $ϕ$, which assumes separate discounting parameters for separate (unattended) attributes. Consistent with the above-mentioned attribute-specific effect of hunger on choices, we found that the attentional discounting of the health attribute but not the taste attribute was amplified under hunger, such that unattended nutritional information had a blunted influence on the evidence accumulation process. Notably, we also found a hunger effect on the attribute discounting parameter ϕ in the regular maaDDM (Figure 5—figure supplement 1), but our extension allowed us to pinpoint this effect specifically to health information. Given related work on the malleability of attentional discounting on mnemonic demands (Eum et al., 2023; Weilbächer et al., 2021), we speculate that hunger could impede a person’s ability or willingness to maintain health considerations in working memory when attention is currently drawn to the tasty food stimulus.

Several supplementary analyses demonstrate the robustness of our findings. In essence, and in line with a large body of literature (e.g. Garlasco et al., 2019; Otterbring, 2019; Read and Leeuwen, 1998), hungry participants were more likely to choose items which they rated higher in terms of tastiness, wanting and caloric content. Importantly, the pivotal role of attention was also established in the exploratory wanting and calorie analyses. Moreover, we performed a PCA to identify the major components that drive food choices, finding that two factors representing tastiness and healthiness aspects explain 81% of the variance in the data. We see this as a justification to describe and study dietary choices by means of these two attributes, essentially following a series of previous studies in our field (e.g. Hutcherson and Tusche, 2022; Maier et al., 2020; Rramani et al., 2020; Sullivan and Huettel, 2021).

The present results and supplementary analyses clearly support the twofold effect of hunger state on the cognitive mechanisms underlying choice. However, we acknowledge potential demand effects arising from the within-subject Protein-shake manipulation. A recent study (Khalid et al., 2024) showed that labeling water to decrease or increase hunger affected participants subsequent hunger ratings and food valuations. For instance, participants expecting the water to decrease hunger showed less wanting for food items. DDM modeling suggested that this placebo manipulation affected both drift rate and starting point. The absence of a starting point effect in our data speaks against any prior bias in participants due to any demand effects. Yet, we cannot rule out that such effects affected the decision-making process, for example by increasing the taste weight (and thus the drift rate) in the hungry condition.

From a neurobiological perspective, both homeostatic and hedonic mechanisms drive eating behavior. While homeostatic mechanisms regulate eating behavior based on energy needs, hedonic mechanisms operate independent of caloric deficit (Alonso-Alonso et al., 2015; Lowe and Butryn, 2007; Saper et al., 2002). Participants’ preference for tasty high-caloric food options in the hungry condition aligns with a drive for energy restoration and could thus be taken as an adaptive response to signals from the body. On the other hand, our data shows that participants preferred less healthy options also in the sated condition. Here, hedonic drivers could predominate indicating potentially maladaptive decision-making that could lead to adverse health outcomes if sustained. Notably, our modeling analyses indicated that participants in the sated condition showed reduced attentional discounting of health information, which poses potential for attention-based intervention strategies to counter hedonic hunger. This has been investigated, for example, in behavioral (Barakchian et al., 2021; Bucher et al., 2016; Cheung et al., 2017; Sullivan and Huettel, 2021), eye-tracking (Schomaker et al., 2022; Vriens et al., 2020) and neuroimaging studies (Hare et al., 2011; Hutcherson and Tusche, 2022) showing that focusing attention on health aspects increased healthy choice. For example, Hutcherson and Tusche, 2022 compellingly demonstrated that the mechanism through which health cues enhance healthy choice is shaped by increased value computations in the dorsolateral prefrontal cortex (dlPFC) when cue and choice are conflicting (i.e. health cue, tasty choice). In the context of hunger, these findings together with our analyses suggest that drawing people’s attention towards health information will promote healthy choice by mitigating the increased attentional discounting of such information in the presence of tempting food stimuli.

In conclusion, our study provides substantial insights into the mechanism underlying dietary choice across metabolic states. Our extension of the multi-attribute attentional DDM revealed that the valuation of food options under hunger is compromised by a relatively lower weighting and a stronger attentional discounting of health information. This modeling extension represents a general contribution to advance research on multi-attribute decision-making, as it allows modeling attribute-specific attentional discounting, which is likely to occur if attributes are described in markedly different formats.

## Materials and methods

### Preregistration

The study was preregistered on Open Science Framework (https://osf.io/tmdw3/). An a-priori power analysis was conducted to determine the required sample size of the experiment using G*Power (Faul et al., 2009). The power analysis was targeted on testing an effect of hunger on non-food choices (which were part of the same study but are not reported here). A study by Skrynka and Vincent, 2019 demonstrated that hunger state affected the discounting of food and other commodities, for which the authors report very large and medium-large effect sizes, respectively. Given inflated effect sizes due to publication bias (Simonsohn, 2015), we set our smallest effect size of interest (Lakens et al., 2018) to Cohen’s d=0.3, with an alpha level of 0.05, and a power of 0.8, resulting in a required sample size for a one-tailed paired t-test of 70 participants. In line with Skrynka and Vincent, 2019, we expected a larger effect of hunger on food choices (i.e. d=0.5) and thus consider the current experiment being sufficiently powered.

### Participants

A total of 70 participants (53 females, 16 males and one diverse, $M_{age}=25.6$, $SD_{age}=8.064$, $M_{BMI}=23.224$, $SD_{BMI}=4.363$) completed both sessions of the experiment. Participants were recruited from the University of Hamburg using the recruiting system SONA (n=40) and from the city of Hamburg using the job portal Stellenwerk (stellenwerk-hamburg.de) (n=30). Compensation for participation were course credits or money (€12.50 per hour). Individuals were eligible to participate in the study if they were proficient in German and were at least 18 yr old. Exclusion criteria included dietary-related aspects (e.g. diets, vegan, food allergies, and intolerances), physical or mental illnesses, drug use, pregnancy, and breastfeeding. The Local Ethics Committee of the Faculty of Psychology and Human Movement Sciences at the University of Hamburg approved the study.

### Procedure

Before participants signed up for the study, a questionnaire was acquired to assess participants’ eligibility and collect demographic information. The latter was used to compute the amount of protein shake participants received in the sated condition (see Hunger state manipulation). Hunger state was counterbalanced such that n=36 completed the experiment in the hungry condition first and n=34 in the sated condition first. In the first session, participants were informed about the procedure (Supplementary file 1) and provided their informed consent. In both sessions, participants first rated their subjective feeling of hunger (see VAS, Appendix 3—figure 1) and mood (see Appendix 1). In the sated condition, participants received a protein shake matched to their daily caloric needs (see Hunger state manipulation) and rated hunger and mood again. In both sessions, the experiment started with a rating task, followed by hunger and mood ratings, then the choice tasks, and concluded with subsequent hunger and mood ratings before reaching the reward screen (Figure 1c). At the end of the first session, participants filled out a questionnaire assessing eating behavior (see Appendix 2). Finally, participants were compensated and received their reward. Overall, one session lasted for approximately 2 hr. The second session took place 5–10 d (M=7.915, SD = 2.755) after the first.

#### Hunger state manipulation

In both conditions, participants came to the lab after an overnight fast. In the sated condition, participants received an individually determined amount of whey protein shake from MyProtein (https://www.myprotein.com/) (flavor: vanilla, or strawberry) amounting to 25% of participants’ daily caloric needs in line with Schofield equations (Schofield, 1985). The equation considers gender, age, weight, and activity level, which was set to 1.4 (‘sedentary’) for all participants, in line with Wever et al., 2021.

### Experimental tasks and materials

The experiment was implemented in OpenSesame version 3.3 (Mathôt et al., 2012), and PyGaze (Dalmaijer et al., 2014) was used for the implementation of different eye-tracking functions. Participants completed the experiment on a 24-inch screen with a resolution of 1024×768 pixels. The experiment consisted of three counterbalanced rating blocks, and corresponding choice blocks (i.e. food preference and choice, social preference and choice, intertemporal preference and choice). Here, we report the results of the food rating and food choice task only. The social and intertemporal ratings and choices will be reported separately. Stimuli of the food tasks were taken from the Full4Health Image Collection and included 66 standardized images of food presented on a plate (Charbonnier et al., 2016, available at https://osf.io/cx7tp/). Food images were selected based on their familiarity in Germany, and matched with respect to the Nutri-Score, which represents a rating of the nutritional quality of a food item within a product category (from A=balanced nutrition to E=unbalanced nutrition, Federal Ministry of Food and Agriculture). While familiar in Germany and other European countries, participants were also informed about meaning of the Nutri-Score before the experiment started. We included 13 food images of Nutri-Scores A and B each with approximately half sweet (e.g. kiwi) and half savory (e.g. cucumber); 12 food images of Nutri-Score C each half sweet (e.g. dried apricots) and half savory (e.g. olives); and 14 images of Nutri-Scores D and E each with approximately half sweet (e.g. Oreo biscuits) and half savory (e.g. Potato Crisps). Food images (387.2×259.2 pixels) and corresponding Nutri-Scores (166.5×94.1 pixels) were displayed in both rating and choice task. The position of the images was counterbalanced, such that for half the participants, the Nutri-Score was displayed on the upper part of the screen and the food image on the lower part, while for the other half of the participants, the positions were reversed. A gray background (#777777) was used for the entire experiment. The experimental tasks, questionnaires, and stimuli used are available on https://osf.io/pef9t/files/.

#### Food rating task

Participants were asked to rate all 66 food images on a continuous scale using the mouse to move the slider and mouse button to log their response (Figure 1a). The initial position of the slider was in the center of the scale. Food images appeared after a white fixation dot (1000 ms) in random order. Overall, participants rated items on four scales indicating perceived tastiness (‘How tasty would you rate this item? Not tasty at all – very tasty’), healthiness (‘How healthy would you rate this item? Not healthy at all – very healthy’), wanting (‘How much would you like to eat this item at the end of the experiment? Not at all – very much’), and perceived caloric content (‘How high would you rate the caloric content of this item? Very low– very high’). Text and slider were white. No time limit was imposed in this task.

#### Food choice task

In the binary food choice task, participants were asked to select the food image they preferred, knowing that they would be incentivized in line with their choices (see Incentivization). Overall, participants made 190 choices per session, including a self-paced break halfway through the task. During the task participants’ eye movements were recorded (see Eye-tracking data). One trial consisted of a white fixation dot (i.e. participants had to fixate the dot for 1000 ms before the trial began, which ensured calibration at each trial), the option screen (self-paced), and a feedback screen (500 ms). The option screen included two food images and their corresponding Nutri-Scores, in counterbalanced positioning. As for the feedback, a black frame was implemented around the chosen option (Figure 1b). This part of the experiment took approximately 25 min.

#### Visual analogue scale (VAS)

A VAS (Sepple and Read, 1989) was used to assess subjective feeling of hunger and fullness (i.e. ‘how hungry/full are you?’) on a continuous scale ranging from ‘0=not hungry/full at all to 100=very hungry/full’ (Parker et al., 2004).

#### Other control measures

Demographic information including gender, age, weight, height, handedness, level of education, and monthly disposable income were recorded before the experimental sessions. In both experimental sessions, additional questions concerning participants last meal and usual breakfast routines were collected. If applicable, women also answered questions with respect to their menstrual cycle. Throughout each session, we assessed participants’ mood (see Appendix 1). At the end of the first session, we also assessed eating behavior (see Appendix 2).

#### Incentivization

To ensure ecological and external validity (Barakchian et al., 2021) during the choice task, participants received a food item for which they indicated a preference of at least 50 in the food rating task and had chosen in a randomly selected trial in the choice task, at the end of each session. We stored the 66 food items in shelves and a fridge in our lab. After each testing session, inventory was assessed, and stores were refilled.

### Eye-tracking data

During the choice tasks, participants’ fixation patterns were recorded using a SR Research EyeLink 1000 Plus eye-tracker for high-quality recording of eye movements and pupillometry with up to 2 kHz sampling rate. A chin rest was used to avoid head movements of the participants and subsequent recalibrations. The distance between screen and chin rest was approximately 93 cm. The eye-tracker was calibrated at the beginning of each choice task and after completing half of the trials.

Preprocessing of eye-tracking data was performed in Matlab (2021b, https://www.mathworks.com/) using the edfmex converter (SR Research Ltd.). Preprocessing included parsing the events into trials and locations. Areas of interest (AOI) were the four positions on the screen, where food images and Nutri-Scores were displayed. We increased these areas by 5% of their original size. Preprocessing resulted in two data frames per participant: one in which the length corresponded to the number of trials and fixation durations and the different AOIs were summed within (for multiple fixations at one location) trials; the length of second data frame corresponded to the total number of fixations of all trials of each participant in each condition.

### Data analysis

#### Preprocessing

In line with our preregistration, RTs were preprocessed before further analyses by excluding trials that were >4 SD above the individual mean RT per condition or <250 ms. As we had a different number of hunger ratings between conditions (participants rated their hunger three times in the hungry and four times in the sated condition; see Figure 1c), we evaluated the effectiveness of our hunger state manipulation with a RM-ANOVA on the difference scores in hunger rating (i.e. last timepoint–first timepoint) with condition as a within-subject factor and a paired t-tests to assess differences in hunger ratings at lab arrival. Participants’ hunger ratings did not entail extreme outliers, and a Shapiro-Wilk test suggested that hunger ratings were normally distributed. Due to missing data in the VAS and PANAS at timepoint 1 (i.e. upon arrival at the lab) in six participants, the analysis of the hunger state manipulation had a sample size of 64. Reported values include F- and t-statistics, (Bonferroni-corrected) p-values, and effect sizes based on Cohen’s d.

#### Principal component analysis

Overall, we had six different measures of the presented food stimuli, including subjective ratings of tastiness, wanting, healthiness, and caloric content, as well as objective characteristics such as Nutri-Score and objective total caloric content. These measures were highly correlated (Appendix 3—figure 2). To assess whether our preregistered goal to study dietary decisions in terms of contrasting taste vs. health aspects was justified, we performed a PCA on these measures using the R package ‘FactoMineR’ (Lê et al., 2008).

#### Generalized linear mixed models

In line with our preregistration, analyses of the food choice task were focused on trials in which one option was rated higher in taste and lower in health compared to the other option (i.e. conflict choices). There were on average 75.68 (SD = 21.96) of these trials per participant. The main analyses comprised two types of generalized linear mixed models (GLMM) using the lme4 package (Bates et al., 2015) in R (version: 4.3.1). First, we implemented a mixed-effects logistic regression analysis with tasty vs. healthy choice (Appendix 4) as binary outcome with a binomial distribution and a logit link function (see also Appendix 5 for analysis of wanting vs health and Appendix 6 for analysis of high caloric versus low caloric choice); second, we implemented a mixed effects regression analysis with RT as dependent variable and a Gamma distribution with an identity link function. In both analyses, models with random intercepts for each participant and random slopes for condition ($AIC_{GLMM2choice}=13017.95$, $AIC_{GLMM2RT}=23438.93$) outperformed models without random effects ($AIC_{GLMchoice}=13845.4$, $AIC_{GLMRT}=24556.97$) and those with random intercepts only ($AIC_{GLMM1choice}=13216.59$; $AIC_{GLMMRT}=28544.95$). In line with our preregistration, we included condition (hungry vs sated) and attention (proportion of dwell time on tasty option) as predictors (Appendix 4—table 1). Exploratory models including demographic information as well as scores on participants mood and eating behavior are reported in Appendix 4—table 1 For the RT model, we used the same predictors as in our choice model with ‘choice’ (tasty vs healthy) as an additional predictor (Appendix 4—table 2). Controlling for the order of testing (i.e. whether participants were first tested in the hungry or the sated session) neither affected choices and RTs, nor the predictive power of the main predictors. Reported values include correlation coefficients, standard errors (SE), z- and p-values.

### Eye-tracking

The eye-tracking analyses were implemented on conflicting trials (i.e. one option was tastier compared to the other option). The analyses included a paired t-tests for the difference in relative dwell time on attribute between conditions and a Bayesian within-subject multilevel mediation analysis (Vuorre and Bolger, 2018) with choice (tasty vs. healthy) as dependent variable, hunger state as independent variable, and proportion of dwell time on tasty option as mediating variable, using the bmlm package in R (Vuorre, 2023). Reported values include t-statistics, p-values, and effect sizes based on Cohen’s d for the t-test, as well as correlation coefficients, SEs, and credibility intervals (CI) for the mediation analysis. Convergence for the mediation analysis was assessed via the Gelman-Rubin statistic (‘Rhat’) (Gelman and Rubin, 1992) with a threshold of 1.05 (Vuorre and Bolger, 2018).

### Cognitive models

To elucidate the cognitive mechanisms underlying the interaction of attention and decision-making in dietary choice, we preregistered to use the multi-attribute time-dependent drift diffusion model (mtDDM) (Maier et al., 2020; Sullivan and Huettel, 2021) and extend it with attention-related parameters for both options (Krajbich et al., 2010) and attributes. The core assumption of the mtDDM is that different attributes enter the choice process at different times (e.g. taste information before health information). However, our modeling analyses quickly revealed that there was little to no support for different onset times of the two attributes. In addition, we ran into convergence issues in the parameter recovery with the relative starting time parameter not recovering. Therefore, our modeling analyses focused on models incorporating attentional dynamics, and we refrained from further developing the mtDDM model.

The computational models were fit to choices and RT of all (pre-processed) trials. In case of DDMs that included attentional dynamics, eye-tracking data was used to inform the model (see below). Overall, we tested eight different versions of DDMs, all of them including boundary separation ($\alpha$), non-decision time (nDT), and a drift scaling parameter $d$ as free parameters. Note that attentional DDMs are often estimated with $\alpha$ being fixed and the standard deviation of the drift being a free parameter; here, we followed the convention in the larger DDM community and estimated $\alpha$ while fixing the standard deviation to 1. The definition of the drift rate varied across models, and the (relative) starting point ($\beta$) was either fixed to 0.5 or estimated. For the most basic DDM, the drift rate was determined by multiplying the scaling parameter $d$ with the VD which was given by the taste (T) and health (H) differences of the two options i and j, weighted by the free parameters $\omega$ (relative taste weight) and $1−\omega$ (relative health weight), respectively (0 ≤ $\omega$ ≤ 1). Taste and health values were scaled in line with, such that they would be between one and ten using a generalized distance function (Berkowitsch et al., 2015).

$$
VD=\omega(T_{i}−T_{j})+(1−\omega)(H_{i}−H_{j})
$$

The second model was an attentional DDM (aDDM) (Krajbich et al., 2010), which included (next to $\omega$) the relative dwell time on each option and parameter $\theta$, which models a dependency of VD on the (dwell) time spent on each option. Specifically, the VD in favor of option i relative to option j depends on the dwell time (f) on the options as follows:

$$
VD=f_{i}(\omega(T_{i}−\thetaT_{j})+(1−\omega)(H_{i}−\thetaH_{j}))+f_{j}(\omega(\thetaT_{i}−T_{j})+(1−\omega)(\thetaH_{i}−H_{j}))
$$

The third model, the multi-attribute attentional DDM (maaDDM) (Yang and Krajbich, 2023) included two attentional parameters to discount the non-looked upon option ($\theta$) and attribute ($ϕ$), respectively. Thus, VD is defined as follows:

$$
VD=f_{i,T}(\omega(T_{i}−\thetaT_{j})+(1−\omega)ϕ(H_{i}−\thetaH_{j}))+f_{i,H}(\omegaϕ(T_{i}−\thetaT_{j})+(1−\omega)(H_{i}−\thetaH_{j}))+f_{j,T}(\omega(\thetaT_{i}−T_{j})+(1−\omega)ϕ(\thetaH_{i}−H_{j}))+f_{j,H}(\omegaϕ(\thetaT_{i}−T_{j})+(1−\omega)(\thetaH_{i}−H_{j}))
$$

Finally, we developed and tested an extension of the maaDDM with two separate $ϕ$ parameters for taste ($ϕ_{T})$ and health $(ϕ_{H}$) (maaDDM2 $ϕ$). The rationale behind the extension is that in our study (but also other related studies), the attributes representing taste and health differed with respect to image complexity, size, and informational content and consequently might differ with respect to their rate of discounting (Figure 6). For the maaDDM2 $ϕ$, the VD is thus given by:

$$
VD=f_{i,T}(\omega(T_{i}−\thetaT_{j})+(1−\omega)ϕ_{H}(H_{i}−\thetaH_{j}))+f_{i,H}(\omegaϕ_{T}(T_{i}−\thetaT_{j})+(1−\omega)(H_{i}−\thetaH_{j}))+f_{j,T}(\omega(\thetaT_{i}−T_{j})+(1−\omega)ϕ_{H}(\thetaH_{i}−H_{j}))+f_{j,H}(\omegaϕ_{T}(\thetaT_{i}−T_{j})+(1−\omega)(\thetaH_{i}−H_{j}))
$$

For each of these four models, we tested two versions which either allowed the relative starting point parameter ($\beta$) to be free or fixed it to 0.5. Models with fixed $\beta$ consistently provided a more parsimonious account of the data. In addition, we also tested models in which the drift rate was informed by the scaled VD of taste and Nutri-Score (Appendix 11) wanting and health, as well as wanting and Nutri-Score (Appendix 12). Importantly and in line with our PCA, these models yielded comparable results to those reported in the main text.

#### Parameter estimation

Parameter estimation was targeted at testing differences across the two hunger state conditions. Specifically, we estimated a set of ‘baseline’ parameters for the sated condition as well as the ‘change’ in each parameter under hunger (i.e. $parameter_{hungry}$ = $parameter_{sated}$ + change). Following our previous work (Kraemer and Gluth, 2023), all group-level parameters were drawn from normal distributions N(µ,SD) and half-normal distributions HN(µ,SD) for group mean and group SD, respectively. More specifically, for the ‘baseline’ parameters, the group mean and SD for $\alpha$ were drawn from N(2,1) and HN(0,3), respectively, the group mean and SD for nDT were drawn from N(–1,1) and HN(0,1), respectively, and the group mean and SD for all remaining parameters were drawn from N(0,0.5) and HN(0,0.5), respectively. For the ‘change’ parameters, the group mean and SD for $\alpha$ and nDT were drawn from N(0,1) and HN(0,1), respectively, and the group mean and SD for all remaining parameters were drawn from N(0,0.25) and HN(0,0.25), respectively. On the participant-level, all individual parameters were drawn from normal distributions N(µgroup,SDgroup). Some of these parameter values were then soft-plus transformed (in case of $\alpha$, nDT and $\sigma$) to enforce strictly positive values or phi-transformed (in case of $\beta$ and $\omega$) to enforce values between 0 and 1. In the Results, we report transformed parameter values which are easier to interpret, but untransformed values for the effect of hunger to illustrate deviations from 0. Hierarchical Bayesian parameter estimation (Farrell and Lewandowsky, 2018) was performed with JAGS, called within R using the R2jags package (Su and Yajima, 2021), and accelerated by parallel computing. We used piecewise constant averaging (Lombardi and Hare, 2021) to speed up model fit, in particular, of the (ma)aDDMs. For sampling, we used eight chains, with 60,000 iterations, 30,000 burnin samples, and a thinning of 12, resulting in 2500 samples per chain. Convergence was assessed via the Gelman-Rubin statistic (‘Rhat’) (Gelman and Rubin, 1992) with a threshold of 1.05. Model fit was quantified with the Deviance Information Criterion (DIC) (Spiegelhalter et al., 2002). For our best-performing models (maaDDM, maaDDMsp, maaDDM2 $ϕ$, maaDDM2 $ϕ$ sp), we performed posterior predictive checks, by drawing 1000 parameter values from the individual posterior parameter distributions, simulating new data, and checking whether the empirical means fell into the 95% HDI of the simulated choice and RT data (see Figure 4, Figure 4—figure supplement 1 and Appendix 9—figures 1 and 1). We implemented parameter recoveries of our best models (Appendix 10—figures 1–4).
