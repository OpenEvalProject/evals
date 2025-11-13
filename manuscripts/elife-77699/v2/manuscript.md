# Multiple preferred escape trajectories are explained by a geometric model incorporating prey’s turn and predator attack endpoint

## Authors

- Yuuki Kawabata<sup>1</sup> ([ORCID: 0000-0001-8267-5199](https://orcid.org/0000-0001-8267-5199)) †
- Hideyuki Akada<sup>2</sup>
- Ken-ichiro Shimatani<sup>3</sup>
- Gregory Naoki Nishihara<sup>4</sup>
- Hibiki Kimura<sup>1</sup> ([ORCID: 0000-0003-3710-2564](https://orcid.org/0000-0003-3710-2564))
- Nozomi Nishiumi<sup>1</sup>
- Paolo Domenici<sup>6</sup>

### Affiliations

1. Graduate School of Fisheries and Environmental Sciences, Nagasaki University Nagasaki Japan ([ROR:058h74p94](https://ror.org/058h74p94))
2. Faculty of Fisheries, Nagasaki University Nagasaki Japan ([ROR:058h74p94](https://ror.org/058h74p94))
3. The Institute of Statistical Mathematics Tachikawa Japan ([ROR:03jcejr58](https://ror.org/03jcejr58))
4. Institute for East China Sea Research, Organization for Marine Science Technology, Nagasaki University Nagasaki Japan ([ROR:058h74p94](https://ror.org/058h74p94))
5. National Institute for Basic Biology Okazaki Japan ([ROR:05q8wtt20](https://ror.org/05q8wtt20))
6. CNR-IAS, Località Sa Mardini Oristano Italy ([ROR:013fk0013](https://ror.org/013fk0013))
7. CNR-IBF, Area di Ricerca San Cataldo Pisa Italy ([ROR:041xzk838](https://ror.org/041xzk838))

† Corresponding author

## Abstract

The escape trajectory (ET) of prey – measured as the angle relative to the predator’s approach path – plays a major role in avoiding predation. Previous geometric models predict a single ET; however, many species show highly variable ETs with multiple preferred directions. Although such a high ET variability may confer unpredictability to avoid predation, the reasons why animals prefer specific multiple ETs remain unclear. Here, we constructed a novel geometric model that incorporates the time required for prey to turn and the predator’s position at the end of its attack. The optimal ET was determined by maximizing the time difference of arrival at the edge of the safety zone between the prey and predator. By fitting the model to the experimental data of fish Pagrus major, we show that the model can clearly explain the observed multiple preferred ETs. By changing the parameters of the same model within a realistic range, we were able to produce various patterns of ETs empirically observed in other species (e.g., insects and frogs): a single preferred ET and multiple preferred ETs at small (20–50°) and large (150–180°) angles from the predator. Our results open new avenues of investigation for understanding how animals choose their ETs from behavioral and neurosensory perspectives.

## Introduction

When exposed to sudden threatening stimuli such as ambush predators, most prey species initiate escape responses that include turning swiftly and accelerating away from the threat. The escape responses of many invertebrate and lower vertebrate species are controlled by giant neurons that ensure a short response time (Bullock, 1984). Many previous studies have focused on two behavioral traits that are fundamental for avoiding predation: when to escape (i.e., flight initiation distance, which is measured as the distance from the predator at the onset of escape) and where to escape (i.e., escape trajectory [ET], which is measured as the angle of escape direction relative to the stimulus direction) (Cooper, Jr and Blumstein, 2015). Previous studies have investigated the behavioral and environmental contexts affecting these variables (Meager et al., 2006; Arnott et al., 1999; Bateman and Fleming, 2014; Hein et al., 2018; Broom and Ruxton, 2005; Cooper et al., 2003), because they largely determine the success or failure of predator evasion (Walker et al., 2005; Shifferman and Eilam, 2004; Camhi et al., 1978; Kimura and Kawabata, 2018; Dangles et al., 2006), and hence the fitness of the prey species. A large number of models on how animals determine their flight initiation distances have been formulated and tested by experiments (Cooper, Jr and Blumstein, 2015). Although a number of models have also been developed to predict animal ETs (Arnott et al., 1999; Weihs and Webb, 1984; Domenici, 2002), there are still some unanswered questions about how the variability of the observed ETs is generated.

Two different escape tactics (and their combination) have been proposed to enhance the success of predator evasion (Jensen, 2018; Domenici et al., 2011a): the optimal tactic (deterministic), which maximizes the distance between the prey and the predator (Figure 1A; Arnott et al., 1999; Weihs and Webb, 1984; Domenici, 2002; Soto et al., 2015), and the protean tactic (stochastic), which maximizes unpredictability to prevent predators from adjusting their strike trajectories accordingly (Figure 1B; Humphries and Driver, 1970; Jones et al., 2011; Richardson et al., 2018; Moore et al., 2017). Previous geometric models, which formulate optimal tactics, predict a single ET that depends on the relative speeds of the predator and the prey (Arnott et al., 1999; Weihs and Webb, 1984; Domenici, 2002; Soto et al., 2015), and additionally, predator’s turning radii and sensory-motor delay in situations where the predator can adjust its strike path (Howland, 1974; Corcoran and Conner, 2016; Martin et al., 2022). The combination of the optimal tactic (formulated by previous geometric models), which predicts a specific single ET, and the protean tactic, which predicts variability, can explain the ET variability within a limited angular sector that includes the optimal ET (Figure 1C). However, the combination of the two tactics cannot explain the complex ET distributions reported in empirical studies on various taxa of invertebrates and lower vertebrates (reviewed in Domenici et al., 2011b). Whereas some animals exhibit unimodal ET patterns that satisfy the prediction of the combined tactics or optimal tactic with behavioral imprecision (e.g., Cooper, 2006), many animal species show multimodal ETs within a limited angular sector (esp., 90–180°) (Figure 1D) (e.g., Arnott et al., 1999; Bateman and Fleming, 2014; Domenici and Blake, 1993). To explore the discrepancy between the predictions of the models and empirical data, some researchers have hypothesized mechanical/sensory constraints (Domenici et al., 2011a; Domenici et al., 2008); however, the reasons why certain animal species prefer specific multiple ETs remain unclear.

![Figure 1.](https://cdn.elifesciences.org/articles/77699/elife-77699-fig1-v2.jpg)

**Figure 1.:** (A) The pure optimal tactic, which predicts a specific optimal ET. (B) The pure protean tactic, which predicts a random ET from all directions. (C) The combination of optimal and protean tactics, which predicts an ET selected randomly (or with a specific probability distribution) from a limited angular sector that includes the optimal ET. (D) The multiple preferred ETs, empirically observed in various species. Please also see Domenici et al., 2011a, for the review on potential ETs.

Multiple preferred ETs of prey can result from situations in which animals choose one behavior from multiple options. Previous work carried out in the field of human and animal psychology on the choice of a particular behavioral strategy out of a number of options has proposed a principle called ‘matching law’. According to this principle, the probability of a certain behavior to occur is related to the proportion of rewards obtained (Reed and Kaplan, 2011; Poling et al., 2011; McDowell, 2013; Houston et al., 2021). This is in contrast to a purely optimal tactic, where animals should always choose the best option (i.e., the highest rewards obtained) (Houston et al., 2021; Fawcett et al., 2013). Arguably, the field of predator-prey interactions has the potential to benefit from an analytical interpretation based on the matching law, because the multiple ETs available to the prey set a scenario similar to the multiple behavioral options considered in previous work analyzed using this principle. In line with this approach, the probability with which a prey chooses a particular ET can be related to the rewards (chances of survival) of each ET option calculated from a predator-prey geometric model.

In previous geometric models, the prey was assumed to instantaneously escape in any direction, irrespective of the prey’s initial body orientation relative to the predator’s approach path (hereafter, initial orientation) (Arnott et al., 1999; Weihs and Webb, 1984; Domenici, 2002). However, additional time is required for changing the heading direction (i.e., turn); therefore, a realistic model needs to take into account that the predator can approach the prey while the prey is turning (Kimura and Kawabata, 2018). Additionally, in previous models, attacking predators were assumed to move for an infinite distance at a constant speed (Arnott et al., 1999; Weihs and Webb, 1984; Domenici, 2002). However, the attacks of many real predators, especially ambush ones, end at a certain distance from initial positions of the prey (Webb and Skadsen, 1980; Fouts and Nelson, 1999; Anderson, 1993). Therefore, we constructed a geometric model that incorporates two additional factors: the time required for the prey to turn and the endpoint of the predator attack. First, using a fish species as a model, we tested whether our model could predict empirically observed multimodal ETs. Second, by calculating the chances of survival of each ET option from our model, we investigated how the prey fish chose a given ET from multiple options. Third, by extending the model, we tested whether other patterns of empirical ETs could be predicted: unimodal ETs and multimodal ETs directed at small (20–50°) and large (150–180°) angles from the predator’s approach direction. The biological implications resulting from the model and experimental data are then discussed within the frameworks of predator-prey interactions and behavioral decision-making.

### Model

We revised the previous model proposed by Domenici, 2002; Paglianti and Domenici, 2006 (Figure 2A) and the model proposed by Corcoran and Conner, 2016 (Appendix 1—figure 1A). Other previous models (Arnott et al., 1999; Weihs and Webb, 1984; Soto et al., 2015; Martin et al., 2022) made predictions similar to those of Domenici’s model or those of Corcoran’s model, although they used different theoretical approaches. In Domenici’s model, the predator with a certain width (i.e., the width of a killer whale’s tail used as a weapon to catch prey) directly approaches the prey, and the prey (the whole body) should enter the safety zone before the predator reaches that entry point. In this model, the prey can instantaneously escape in any direction, and the predation threat moves linearly and infinitely. Corcoran’s model is based on the same principle as Domenici’s model, but includes the concept that the predator (i.e., a bat) can adjust the approach path up to its minimum turning radius. Thus, Domenici’s model can be regarded as a special case of Corcoran’s model when the turning radius of the predator is infinitely large. These models are based on the escape response of the horizontal plane, which is realistic for many fish species as well as terrestrial and benthic species that move on substrates. They can also be applied to aerial animals such as moths escaping from bats because many predator-prey interactions are approximately two-dimensional in a local spatial scale (Corcoran and Conner, 2016; Fabian et al., 2018). Hereafter, we explain the modification of Domenici’s model (a special case of Corcoran’s model) because the data on previously published predator-prey experiments on the same species of prey and predator in our experiment (Kimura and Kawabata, 2018) show that the predator does not adjust the strike path during the attack (Figure 2—figure supplement 1, adjusted angle = 1.0 ± 6.6° [mean ± s.d.], n=5), and thus the number of parameters to estimate can be reduced. See Appendix 1 for details of the modified version of Corcoran’s model.

![Figure 2.](https://cdn.elifesciences.org/articles/77699/elife-77699-fig2-v2.jpg)

**Figure 2.:** (A) A previous geometric model proposed by Domenici, 2002; Paglianti and Domenici, 2006. The predation threat with a certain width (the tail of a killer whale, represented by the black triangle) directly approaches the prey, and the prey should reach the safety zone (a grey area) outside the danger zone (white area) before the threat reaches that point. In this model, the prey can instantaneously escape in any direction, and the predation threat moves linearly and infinitely. (B) Two factors are added to Domenici’s model: the endpoint of the predator attack, and the time required for the prey to turn. (Xcross, Ycross) denotes the x and y coordinates of the crossing point of the escape path and the safety zone edge.

![Figure 2—figure supplement 1.](https://cdn.elifesciences.org/articles/77699/elife-77699-fig2-figsupp1-v2.jpg)

**Figure 2—figure supplement 1.:** The intersection point is the crossing point between the trajectory of the prey’s center of mass (CoM) and the trajectory of the predator’s tip of the mouth. The adjusted angle is defined as the angle between the line passing through the predator’s tip of the mouth and the prey’s CoM at the onset of the prey’s escape response, and the line passing through the predator’s tip of the mouth at the onset of the escape response and the intersection point.

![Figure 2—figure supplement 2.](https://cdn.elifesciences.org/articles/77699/elife-77699-fig2-figsupp2-v2.jpg)

**Figure 2—figure supplement 2.:** Filled circle position of the center of mass; dotted arrow approach direction of the dummy predator; S0 position of the fish at the onset of stage 1, S1 position at the end of stage 1, S2 position at the end of stage 2, α turn angle, β initial orientation, α+β escape trajectory (ET).

In our new model (Figure 2B), two factors are added to the previous Domenici’s model: the time required for the prey to turn and the endpoint of the predator attack. We assume that a prey with a certain initial orientation β (spanning 0–180°, where 0° and 180° correspond to being attacked from front and behind, respectively) evades a sudden predation threat. Most prey species respond to the attack by turning at an angle α, and the ET results from the angular sum of α and β. ETs from the left and right sides were pooled and treated as though they were stimulated from the right side (Figure 2—figure supplement 2; see ‘Definition of the angles’ in Materials and methods for details).

When the prey’s CoM at the onset of its escape is located at point (0, 0), the trajectory of the CoM ($X_{prey}$ , $Y_{prey}$) is given by:

$$
Y_{prey}=X_{prey}tan⁡(\alpha+\beta)
$$

The edge of the safety zone is determined by the half-width of the predator capture device (e.g., mouth) Dwidth, the distance between the prey’s initial position and the tip of the predator capture device at the end of the predator attack Dattack, and the shape of the predator’s capture device at the moment of attack, which is approximated as an arc with a certain radius Rdevice. The projection of the predator’s capture device edge along the edge of the sideways safety zone $D_{2}$ can be expressed as:

$$
D_{2}=R_{device}{1−cos(sin^{−1}\frac{D_{width}}{R_{device}})}
$$

The ET toward the upper-left corner of the danger zone $\theta_{corner}$ can be expressed as:

$$
\theta_{corner}=tan^{−1}\frac{D_{width}}{D_{2}−D_{attack}}
$$

The x and y coordinates of the safety zone edge ($X_{safe}$ , $Y_{safe}$) are given by:

$$
{Y_{safe} =D_{width}, \alpha+\beta<\theta_{corner}(X_{safe}+D_{attack}−R_{device})^{2}+ Y_{safe}^{2}= R_{device}^{2}, \alpha+\beta\geq\theta_{corner}
$$

From Equation 1 to Equation 4, the x and y coordinates of the crossing point of the escape path and the safety zone edge ($X_{cross}$ , $Y_{cross}$) are given by a function of Dwidth, Dattack, Rdevice, and α+β.

The prey can escape from the predator when the time required for the prey to enter the safety zone (Tprey) is shorter than the time required for the predator’s capture device to reach that entry point (Tpred). Therefore, the prey is assumed to maximize the difference between the Tpred and Tprey (Tdiff). To incorporate the time required for the prey to turn, Tprey was divided into two phases: the fast-start phase, which includes the time for turning and acceleration ($T_{1}$), and the constant speed phase ($T_{2}$). This assumption is consistent with the previous studies (Domenici and Blake, 1991; Danos and Lauder, 2012; Fleuren et al., 2018) and was supported by our experiment (see Figure 4—figure supplement 1). Therefore:

$$
T_{prey}=T_{1}+T_{2}
$$

For simplicity, the fish was assumed to end the fast-start phase at a certain displacement from the initial position in any α (D1; the radius of the dotted circle in Figure 2B) and to move at a constant speed Uprey to cover the rest of the distance (toward the edge of the safety zone $\sqrt{X_{cross}^{2}+Y_{cross}^{2}}-D_{1}$ , plus the length of the body that is posterior to the CoM Lprey). Because a larger |α| requires further turning prior to forward locomotion, which takes time (Domenici and Blake, 1991; Ellerby and Altringham, 2001), and the initial velocity after turning was dependent on |α| in our experiment (see Figure 4B), $T_{1}$ is given by a function of |α| [ $T_{1}(|\alpha|)$ ]. Therefore, Tprey can be expressed as:

$$
T_{prey}=T_{1}(|\alpha|)+\frac{\sqrt{X_{cross}^{2}+Y_{cross}^{2}}−D_{1}+L_{prey}}{U_{prey}}
$$

Tpred can be expressed as:

$$
T_{pred}={\frac{D_{initial}+D_{2}−X_{cross}}{U_{pred}}, \alpha+\beta<\theta_{corner}\frac{D_{initial}+D_{attack}}{U_{pred}}, \alpha+\beta\geq\theta_{corner}
$$

where Dinitial is the distance between the prey and the predator at the onset of the prey’s escape response (i.e., the flight initiation distance or reaction distance), and $U_{pred}$ is the predator speed, which is assumed to be constant. From Equations 5–7, Tdiff can be calculated as:

$$
T_{diff}={\frac{D_{initial}}{U_{pred}}+\frac{D_{2}}{U_{pred}}−\frac{X_{cross}}{U_{pred}}−T_{1}(|\alpha|)−\frac{\sqrt{X_{cross}^{2}+Y_{cross}^{2}}}{U_{prey}}+ \frac{D_{1}}{U_{prey}}−  \frac{L_{prey}}{U_{prey}}, \alpha+\beta<\theta_{corner}\frac{D_{initial}}{U_{pred}}+\frac{D_{attack}}{U_{pred}}−T_{1}(|\alpha|)−\frac{\sqrt{X_{cross}^{2}+Y_{cross}^{2}}}{U_{prey}}+ \frac{D_{1}}{U_{prey}}−  \frac{L_{prey}}{U_{prey}}, \alpha+\beta\geq\theta_{corner}
$$

Because $\frac{D_{initial}}{U_{pred}}+\frac{D_{1}}{U_{prey}}-\frac{L_{prey}}{U_{prey}}$ are independent of α and β, we can calculate the relative values of $T_{diff}$ ($T_{diff}`$) in response to the changes of α and β, from:

$$
T_{diff}′={\frac{D_{2}}{U_{pred}}−\frac{X_{cross}}{U_{pred}}−T_{1}(|\alpha|)−\frac{\sqrt{X_{cross}^{2}+Y_{cross}^{2}}}{U_{prey}}, \alpha+\beta<\theta_{corner}\frac{D_{attack}}{U_{pred}}−T_{1}(|\alpha|)−\frac{\sqrt{X_{cross}^{2}+Y_{cross}^{2}}}{U_{prey}}, \alpha+\beta\geq\theta_{corner}
$$

Because $X_{cross}$ and $Y_{cross}$ are dependent on Dwidth, Dattack, and Rdevice as well as $\alpha+\beta$, and $D_{2}$ is dependent on Dwidth and Rdevice, we can calculate $T_{diff}`$ in response to the changes of α and β, from D1, Dwidth, Dattack, Rdevice, Uprey, Upred, and $T_{1}|\alpha|$ . Given that the escape success is assumed to be dependent on $T_{diff}`$, the theoretically optimal ET can be expressed as:

$$
The optimal ET=argmax\alpha+\beta(T_{diff}′)
$$

## Results

### Experimental results

Pagrus major exhibited a typical C-start escape response (Figure 2—figure supplement 2; Figure 3—figure supplement 1), which consists of the initial bend (stage 1), followed by the return tail flip (stage 2), and continuous swimming or coasting (stage 3) (Domenici and Blake, 1997; Weihs, 1973). Figure 3 shows the effect of the initial orientation β on the ETs. As was done in previous studies (Domenici et al., 2011b; Domenici et al., 2009; Nair et al., 2017), the away (contralateral) and toward (ipsilateral) responses, defined as the first detectable movement of the fish oriented either away from or toward the predator, were analyzed separately. When the initial orientation was small (i.e., the prey was attacked head-on; Figure 3A; 0°≤β<30°), two peaks in the ET distribution were observed: a larger peak at around 100° (away response) and a smaller one at around −80° (toward response). As the initial orientation increases (Figure 3A; 30°≤β<60°), the peak at around −80° disappeared. As the initial orientation further increases beyond 60°, another peak appeared at around 170° (Figure 3A). When the initial orientation was large (i.e., the prey was attacked from behind; Figure 3A; 150°≤β≤180°), there were two similar-sized peaks in the ET at around 130° (toward response), and 180–200° (away response). There were significant effects of initial orientation on the ET in both the away and the toward responses (away: generalized additive mixed model [GAMM] F=214.81, p<0.01, n=208; toward: GAMM, F=373.92, p<0.01, n=56). There were significant effects of initial orientation on the turn angle α in away and toward responses (Figure 3—figure supplement 2; away: GAMM, F=90.88, p<0.01, n=208; toward: GAMM, F=42.48, p<0.01, n=56). In the overall frequency distribution of ETs pooling the data on all initial orientations and both toward and away responses, there were two large peaks at 120–130° and 170–180°, and one small peak at around −80° (Figure 3C). These three peaks were confirmed by the Gaussian mixture model analysis (Domenici et al., 2008), where we fitted one to nine Gaussian curves to the ETs, and selected the most parsimonious model based on the Akaike information criterion (AIC) (Figure 3—source data 1).

![Figure 3.](https://cdn.elifesciences.org/articles/77699/elife-77699-fig3-v2.jpg)

**Figure 3.:** (A) Circular histograms of escape trajectories (ETs) in 30° initial orientation β bins. Solid lines are estimated by the kernel probability density function. Concentric circles represent 5% of the total sample sizes within each β bin, the bin intervals are 15°, and the bandwidths of the kernel are 50. A drawing of the prey and predator’s approach direction is shown in the upper-right corner of each graph. The arrow and dotted lines represent the median value and range of predator’s approach direction, respectively. (B) Relationship between initial orientation and ET. Different colors represent the away (blue) and toward (red) responses. Solid and dotted lines are estimated by the generalized additive mixed model (GAMM). (C) Circular histogram of ETs pooling all the data shown in A. Solid lines are estimated by the kernel probability density function. Concentric circles represent 10% of the total sample sizes, the bin intervals are 15°, and the bandwidths of the kernel are 50. The predator’s approach direction is represented by 0°. The dataset and R code are available at Figshare (‘Dataset1.csv’ and ‘Source code 1.R’) (n=264 [208 away and 56 toward responses] from 23 individuals).

![Figure 3—figure supplement 1.](https://cdn.elifesciences.org/articles/77699/elife-77699-fig3-figsupp1-v2.jpg)

**Figure 3—figure supplement 1.:** (A) Prey speed after the onset of escape response. (B) Prey’s body orientation relative to the predator’s approach path after the onset of escape response. (C) Speed of the approaching dummy predator. The speeds of the prey and the predator were calculated by first-order differentiation of the cumulative distance for the time series using a Lanczos five-point quadratic moving regression method.

![Figure 3—figure supplement 2.](https://cdn.elifesciences.org/articles/77699/elife-77699-fig3-figsupp2-v2.jpg)

**Figure 3—figure supplement 2.:** Different colors represent the away (blue) and toward (red) responses. Solid and dotted lines are estimated by the generalized additive mixed model (GAMM). The dataset and R code are available at Figshare (‘Dataset1.csv’ and ‘Source code 1.R’) (n=264 [208 away and 56 toward responses] from 23 individuals).

![Figure 3—figure supplement 3.](https://cdn.elifesciences.org/articles/77699/elife-77699-fig3-figsupp3-v2.jpg)

**Figure 3—figure supplement 3.:** (A) Sketch of the experimental tank for measuring the escape response of prey fish Pagrus major. (B) Sketch (3D model) of the actuation system of the dummy predator.

There were no significant effects of predator speed on the ET and |α| in either the toward or the away responses (ET, away: GAMM, F=0.01, p=0.93, n=208; ET, toward: GAMM, F=0.05, P=0.82, n=56; |α|, away: GAMM, F=0.01, p=0.93, n=208; |α|, toward: GAMM, F=0.05, p=0.82, n=56). There were no significant effects of predator speed (slow [from the minimum to the 33.3% quantile]: 0.13–0.93 m s−1; and fast [from the 66.7% quantile to the maximum]: 1.29–1.88 m s−1) on the variations of ETs and |α| in all 30° initial orientation bins (Levene’s test, W=0.02–3.22, p=0.09–0.88, n=22–47).

### Determination of parameter values

To predict the relationship between the ET (α+β) and the relative time difference Tdiff in each initial orientation (β) by the geometric model, we needed Dwidth, Rdevice, D1, Uprey, T1(|α|), Dattack, and Upred. The methods for determining parameter values are summarized in Table 1. Dwidth and Rdevice were determined from the mouth shape of the predator (the sacrificed specimen for making the dummy predator) when fully opened, which were 18 and 199 mm, respectively. D1, Uprey, and T1(|α|) were directly estimated by analyzing the escape responses of the prey. Because we have no previous knowledge about the values of Upred and Dattack that the prey regards as dangerous, optimal values of Upred and Dattack were determined iteratively by comparing model outputs with observed ETs. These optimal values were checked afterward with the data from previously published predator-prey experiments on the same species of prey and predator (Kimura and Kawabata, 2018). We applied this optimization procedure to estimating Upred instead of measuring the dummy predator speed per trial in the experiment because there was no significant effect of predator speed on ET in the experiment, suggesting that the prey is likely to have optimized their ETs based on a fixed predator speed (see Discussion for details). This assumption was also supported by the follow-up analysis using the dummy predator speed per trial, where the model fits became worse compared to the model using the fixed predator speed estimated through the optimization procedure (Table 3—source data 1; Figure 5—figure supplement 1).

**Table 1.**
 Methods for determining parameter values.


<table>
  <thead>
    <tr>
      <th>Symbol</th>
      <th>Description</th>
      <th>Value</th>
      <th>Method</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Dwidth</td>
      <td>The half-width of the predator capture device (e.g., mouth)</td>
      <td>18 mm</td>
      <td>Measured directly from the dummy predator (a sacrificed individual)</td>
    </tr>
    <tr>
      <td>Rdevice</td>
      <td>The radius of the predator’s capture device at the moment of attack, which is approximated as an arc</td>
      <td>199 mm</td>
      <td>Measured directly from the dummy predator (a sacrificed individual)</td>
    </tr>
    <tr>
      <td>D1</td>
      <td>The displacement from the initial position of prey where it was assumed to end the fast-start phase</td>
      <td>15 mm</td>
      <td>Estimated from the escape kinematics of prey in the experiment</td>
    </tr>
    <tr>
      <td>Uprey</td>
      <td>The prey speed after the displacement of D1, which is assumed to be constant</td>
      <td>1.04 m s–1</td>
      <td>Estimated from the escape kinematics of prey in the experiment</td>
    </tr>
    <tr>
      <td>T1(|α|)</td>
      <td>The time required for a displacement of D1 from the initial position of the prey, given by a function of turn angle |α|</td>
      <td>Figure 4A</td>
      <td>Estimated from the escape kinematics of prey in the experiment</td>
    </tr>
    <tr>
      <td>Dattack</td>
      <td>The distance between the prey’s initial position and the tip of the predator capture device at the end of the predator attack</td>
      <td>35 mm</td>
      <td>Optimized by comparing the model outputs with experimental data</td>
    </tr>
    <tr>
      <td>Upred</td>
      <td>The predator speed, which is assumed to be constant</td>
      <td>1.54 m s–1</td>
      <td>Optimized by comparing the model outputs with experimental data</td>
    </tr>
  </tbody>
</table>

The distance of the fast-start phase (D1) was regarded as 15 mm based on the relationship between displacement and velocity of the prey in the experiments (Figure 4—figure supplement 1), where the velocity increased up to about 15 mm of displacement from the initial position, beyond which it plateaus; over the 15 mm displacement from the initial position, there were no significant differences in the mean velocity between any combinations of 3 mm intervals in any 30° |α| bins (Figure 4—figure supplement 1; paired t-test with Bonferroni’s correction, all p=1.00, n=23). There were significant effects of |α| on the time for a displacement of 15 mm from the initial position (GAMM, F=78.84, p<0.01, n=263; note that the sample size is smaller than the total number of observations, 264, because the prey did not move over 15 mm in one case) and on the mean velocity during the displacement (GAMM, F=76.00, p<0.01, n=263). However, there were no significant effects of |α| on the time required for a displacement of 15–30 mm from the initial position (GAMM, F=1.52, p=0.22, n=257; note that the sample size is smaller than the total number of observations, 264, because the prey did not move over 30 mm in seven cases) and on the mean velocity during the displacement (GAMM, F=0.89, p=0.27, n=257). Therefore, the time required for the prey to turn was incorporated into the model by analyzing the relationship between |α| and the time required for a displacement of 15 mm. The mean velocity of the prey during the constant phase Uprey was estimated to be 1.04 m s–1, based on the experimental data. Because the cut-off distance might affect the overall results of the study, we have repeated all the statistical analyses (see Tables 2 and 3, and the text below for results with a cut-off distance of 15 mm) with cut-off distances of 10 and 20 mm and confirmed that the overall results are insensitive to the changes (Table 2—source data 1; Table 3—source data 2).

**Table 2.**
 Widely applicable or Watanabe-Akaike information criterion (WAIC) for each model in the hierarchical Bayesian models (n=263 and 264, respectively, from 23 individuals).Table 2—source data 1.The case where the distance for the fast-start phase was regarded as either 10 or 20 mm.


<table>
  <thead>
    <tr>
      <th>Relationship</th>
      <th>WAIC</th>
      <th>ΔWAIC</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>|α|–T1 relationship</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Piecewise linear</td>
      <td>1363.7</td>
      <td>0</td>
    </tr>
    <tr>
      <td>Linear</td>
      <td>1376.7</td>
      <td>7.0</td>
    </tr>
    <tr>
      <td>Constant</td>
      <td>1581.1</td>
      <td>217.4</td>
    </tr>
    <tr>
      <td>|α|-initial velocity after stage 1 turn relationship</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>Piecewise linear</td>
      <td>–218.1</td>
      <td>0</td>
    </tr>
    <tr>
      <td>Linear</td>
      <td>–205.1</td>
      <td>13.0</td>
    </tr>
    <tr>
      <td>Constant</td>
      <td>–171.5</td>
      <td>46.6</td>
    </tr>
  </tbody>
</table>

_|α|, absolute value of the turn angle; T1, time required for a displacement of 15 mm from the initial position. The best models are shown in bold._

**Table 3.**
 Comparison of the distribution of escape trajectories (ETs) between the model prediction (n=264 per simulation × 1000 times) and experimental data (n=264) using the two-sample Kuiper test.Table 3—source data 1.The case where Upred was determined from the dummy predator speed per trial in the experiment.Table 3—source data 2.The case where the distance for the fast-start phase was regarded as either 10 or 20 mm.


<table>
  <thead>
    <tr>
      <th>Model</th>
      <th>Median Kuiper’s V</th>
      <th>Median p</th>
      <th colspan="2">Rate of p&gt;0.05</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>With both Dattack and T1(|α|)</td>
      <td>0.11</td>
      <td colspan="2">0.44</td>
      <td>0.97</td>
    </tr>
    <tr>
      <td>With Dattack and without T1(|α|)</td>
      <td>0.26</td>
      <td colspan="2">&lt;0.01</td>
      <td>0.00</td>
    </tr>
    <tr>
      <td>Without Dattack and with T1(|α|)</td>
      <td>0.18</td>
      <td colspan="2">&lt;0.01</td>
      <td>0.12</td>
    </tr>
    <tr>
      <td>Neither Dattack nor T1(|α|)</td>
      <td>0.28</td>
      <td colspan="2">&lt;0.01</td>
      <td>0.00</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>

_Dattack, distance between the prey’s initial position and the endpoint of the predator attack; T1(|α|), relationship between the absolute value of the turn angle and the time required for a 15 mm displacement from the initial position (i.e., the time required for the prey to turn)._

The relationship between |α| and the time required for a displacement of 15 mm, T1(|α|), is shown in Figure 4. The time was constant up to 44° of |α|, above which the time linearly increased in response to the increase of |α| (Figure 4A). In the hierarchical Bayesian model, the lowest widely applicable or Watanabe-Akaike information criterion (WAIC) was obtained for the piecewise linear regression model (Table 2). To understand the possible mechanism of the relationship, the relationship between |α| and initial velocity after a stage 1 turn, calculated as the displacement per second during the 10 ms after the turn, was also evaluated (Figure 4B). The velocity increased in response to |α| up to 46°, beyond which it plateaus. In the hierarchical Bayesian model, the lowest WAIC was obtained for the piecewise linear regression model (Table 2). In both relationships, the regression lines by the piecewise linear model were similar to those by the GAMM, suggesting that the general trends of the relationships were clearly captured by this method. The change points of the two relationships were not significantly different (difference: 1.70±18.01° [mean ± 95% Bayesian credible intervals]). These results indicate that fish with a small |α| (<<45°) can accomplish the stage 1 turn quickly but their velocity after the turn is lower, while fish with an intermediate |α| (=45°) spend a longer time on the stage 1 turn, but their velocity after the turn is higher. Fish with a large |α| (>>45°) spend a still longer time on the stage 1 turn, but their velocity after the turn is similar to that with an intermediate |α| (Figure 4).

![Figure 4.](https://cdn.elifesciences.org/articles/77699/elife-77699-fig4-v2.jpg)

**Figure 4.:** (A) Relationship between |α| and the time required for a displacement of 15 mm from the initial position of the prey (n=263 from 23 individuals). (B) Relationship between |α| and the initial velocity after stage 1 turn (n=264 from 23 individuals). Solid blue lines are estimated by the piecewise linear regression model, and red dashed lines are estimated by the generalized additive mixed model (GAMM). The shaded regions indicate the 95% Bayesian credible intervals of the piecewise linear regression model. The dataset and R code are available at Figshare (‘Source code 1.R’, ‘Source code 2.pdf’, ‘Source code 3.pdf’, and ‘Dataset1.csv’).

![Figure 4—figure supplement 1.](https://cdn.elifesciences.org/articles/77699/elife-77699-fig4-figsupp1-v2.jpg)

**Figure 4—figure supplement 1.:** Unfilled circles denote the mean value for each individual. Different lowercase letters represent significant differences according to the paired t-test with Bonferroni’s correction (p<0.05). (A) |α|<30°. (B) 30°≤|α|<60°. (C) 60°≤|α|<90°. (D) |α|≥90°. (E) Mean of the individual mean value for each |α| bin. Vertical dashed line represents the cut-off distance of 15 mm used in this study, and vertical dotted lines represent the other cut-off distances tested in this study (Table 2—source data 1 and Table 3—source data 2). The datasets and R code are available at Figshare (‘Dataset1.csv’, ‘Dataset2.csv’, ‘Dataset3.csv’, and ‘Source code 1.R’) (n=23 individuals).

We have optimized the values of Upred and Dattack from the perspective of the prey using the experimental data (see Materials and methods for details). Briefly, the optimal values for prey were obtained using the ranking index, where 0 means that the real fish chose the theoretically optimal ET where Tdiff is the maximum, and 1 means that the real fish chose the theoretically worst ET where Tdiff is the minimum (e.g., going toward the predator). The result shows that the optimal value of Dattack is 34.73 mm and the optimal value of Upred is 1.54 m s–1. Using data from previously published predator-prey experiments on the same species of prey and predator (Kimura and Kawabata, 2018), we show that the estimated Dattack value is at the upper limit of the empirical data and the estimated Upred value is higher than the mean of the observed predator speed (Figure 5—figure supplement 2A, B). Similarly, the estimated Upred value is higher than the mean of the observed dummy predator speed in our experiment (Figure 5—figure supplement 2C, D). These results suggest that the values independently estimated in the present study are reasonable, and the prey may choose ETs by overestimating the values of Dattack and Upred.

### Comparison of model predictions and experimental data

Figure 5A plots the relationships between the ET and the relative time difference Tdiff for different initial orientations β, estimated by the geometric model; Figure 5B plots the relationship between the initial orientation and the theoretical ET. Forty-one percent, 76%, and 94% of observed ETs were within the top 10%, 25%, and 40% quantiles, respectively (0.1, 0.25, 0.40 ranking index) of the theoretical ETs (Figure 5B and Figure 5—figure supplement 3). In general, the predicted ETs are in line with the observed ones, where the model predicts a multimodal pattern of ET with a higher peak (i.e., optimal ET) at the maximum Tdiff (Tdiff,1) and a second lower peak (i.e., suboptimal ET) at the second local maximum of Tdiff (Tdiff,2). When the initial orientation is <20° (Figure 5A; β=15°, Figures 5B and 6B), the optimal and suboptimal ETs are around 100° (away response) and −100° (toward response), respectively, which is consistent with the bimodal distribution of our experiment (Figure 3A; 0°≤β<30°). At initial orientations in the range 20‒60°, the suboptimal ET switches from around −100° to 170° (Figure 5A; β=45°, Figures 5B and 6B), although Tdiff,2 is extremely small compared to Tdiff,1 (Figure 5A; β=45°, Figures 5B and 6B). Accordingly, the second peak (i.e., at around 170°) was negligible in our experimental data (Figure 3A; 30°≤β<60°), even though the fish can potentially reach such an ET (i.e., from such an initial orientation, an 170° ET is within the upper limit of |α|, 147°). When the initial orientation is 60‒120° (Figure 5A; β=75° and β=105°, Figures 5B and 6B), the optimal ET is 100‒140° (gradually shifting from 100° to 140°), and the suboptimal ET is around 170°. These two peaks and the shift of the optimal ET are consistent with the experimental results (Figure 3A; 60°≤β<90° and 90°≤β<120°). The values of the optimal and suboptimal ETs are reversed at initial orientations > 120° (Figures 5B and 6B), as the optimal and suboptimal values become 170‒180° and around 140°, respectively (Figure 5A). These results are again consistent with the bimodal distribution of our experiments (Figure 3A; 120°≤β<150° and 150°≤β≤180°).

![Figure 5.](https://cdn.elifesciences.org/articles/77699/elife-77699-fig5-v2.jpg)

**Figure 5.:** (A) Relationship between the escape trajectory (ET) and the time difference between the prey and predator Tdiff in different initial orientations β. The time difference of the best ET was regarded as 10 ms, and the relative time differences between 0 and 10 ms are shown by solid lines. Areas without solid lines indicate that either the time difference is below 0 or the fish cannot reach that ET because of the constraint on the possible range of turn angles |α|. A drawing of prey and predator’s approach direction (arrow) is shown in the upper-right corner of each graph. (B) Relationship between the initial orientation β and ET. Solid and dotted lines represent the best-estimated away and toward responses, respectively. Different colors represent the top 10%, 25%, and 40% quantiles of the time difference between the prey and predator within all possible ETs. (C) Circular histogram of the theoretical ETs, estimated by a Monte Carlo simulation. The probability of selection of an ET was determined by the truncated normal distribution of the optimal ranking index (Figure 5—figure supplement 3). This process was repeated 1000 times to estimate the frequency distribution of the theoretical ETs. Colors in the bars represent the away (blue) or toward (red) responses. Black lines represent the kernel probability density function. Concentric circles represent 10% of the total sample sizes, the bin intervals are 15°, and the bandwidths of the kernel are 50. Circular histogram of the observed ETs (Figure 3C) is shown in the lower-right panel for comparison. The predator’s approach direction is represented by 0°. The dataset and R code are available at Figshare (‘Dataset1.csv’ and ‘Source code 1.R’) (n=264 from 23 individuals for experimental data, and n=264,000 for Monte Carlo simulation).

![Figure 5—figure supplement 1.](https://cdn.elifesciences.org/articles/77699/elife-77699-fig5-figsupp1-v2.jpg)

**Figure 5—figure supplement 1.:** The probability of selection of an ET was determined by the truncated normal distribution of the optimal ranking index. This process was repeated 1000 times to estimate the frequency distribution of the theoretical ETs. Colors in the bars represent the away (blue) or toward (red) responses. Black lines represent the kernel probability density function. Concentric circles represent 10% of the total sample sizes, the bin intervals are 15°, and the bandwidths of the kernel are 50. The predator’s approach direction is represented by 0°. The resulting ETs (A and B) are statistically different from the observed ETs (lower-right panel of each figure), which show clear multiple peaks. This demonstrates that the prey fish do not choose ETs based on the predator speed. The dataset and R code are available at Figshare (‘Dataset1.csv’ and ‘Source code 1.R’) (A) n=264 per simulation × 1000 times; (B) n=257 per simulation × 1000 times; note that the sample size is smaller than the total number of observations, 264, because the dummy predator did not move over 75% of the flight initiation distance of prey in seven cases.

![Figure 5—figure supplement 2.](https://cdn.elifesciences.org/articles/77699/elife-77699-fig5-figsupp2-v2.jpg)

**Figure 5—figure supplement 2.:** (A) Histogram of the distance between the prey’s initial position and the predator’s mouth position at the onset of the mouth closing (Dattack) (n=30 from 7 individuals). (B) Histogram of the speed of the real predator (n=47 from 7 individuals). (C) Histogram of the dummy predator speed at the onset of escape response of prey (n=264 from 23 individuals). (D) Histogram of the dummy predator speed to cover 75% of the prey’s flight initiation distance (n=257 from 23 individuals. Note that the sample size is smaller than the total number of observations, 264, because the dummy predator did not move over 75% of the prey’s flight initiation distance in seven cases). Figures A and B are based on reanalysis of data from Kimura and Kawabata, 2018. Figures (C and D) are based on the experiment in this study. Vertical dashed blue lines represent the optimal values independently estimated in this study, and vertical dotted red lines represent the mean values of the real or dummy predator. The datasets and R code are available at Figshare (‘Dataset1.csv’, ‘Dataset4.csv’, ‘Dataset5.csv’, and ‘Source code 1.R’).

![Figure 5—figure supplement 3.](https://cdn.elifesciences.org/articles/77699/elife-77699-fig5-figsupp3-v2.jpg)

**Figure 5—figure supplement 3.:** The solid line is the density probability function of the truncated normal distribution. The dataset and R code are available at Figshare (‘Dataset1.csv’ and ‘Source code 1.R’) (n=264 from 23 individuals).

![Figure 5—figure supplement 4.](https://cdn.elifesciences.org/articles/77699/elife-77699-fig5-figsupp4-v2.jpg)

**Figure 5—figure supplement 4.:** (A) Circular plots of the time difference between the prey and predator Tdiff in different initial orientations β. The time difference of the best escape trajectory (ET) was regarded as 10 ms, and the relative time differences between 0 and 10 ms are shown by solid lines. Areas without solid lines indicate that either the time difference is below 0 or the fish cannot go to that ET because of the constraint on the possible range of |α|. Concentric circles represent 3 ms. (B) Relationship between the initial orientation β and ET. Solid and dotted lines represent the best-estimated away and toward responses, respectively. Different colors represent the top 10%, 25%, and 40% quantiles of the time difference between the prey and predator within all possible ETs. (C) Circular histogram of the theoretical ETs, estimated by a Monte Carlo simulation. The probability of selection of an ET was determined by the truncated normal distribution of the optimal ranking index. This process was repeated 1000 times to estimate the frequency distribution of the theoretical ETs. Colors in the bars represent the away (blue) or toward (red) responses. Black lines represent the kernel probability density function. Concentric circles represent 10% of the total sample sizes, the bin intervals are 15°, and the bandwidths of the kernel are 50. The predator’s approach direction is represented by 0°. The dataset and R code are available at Figshare (‘Dataset1.csv’ and ‘Source code 1.R’) (n=264 from 23 individuals for experimental data, and n=264,000 for Monte Carlo simulation).

![Figure 5—figure supplement 5.](https://cdn.elifesciences.org/articles/77699/elife-77699-fig5-figsupp5-v2.jpg)

**Figure 5—figure supplement 5.:** (A) Circular plots of the time difference between the prey and predator Tdiff in different initial orientations β. The time difference of the best escape trajectory (ET) was regarded as 10 ms, and the relative time differences between 0 and 10 ms are shown by solid lines. Areas without solid lines indicate that either the time difference is below 0 or the fish cannot go to that ET because of the constraint on the possible range of |α|. Concentric circles represent 3 ms. (B) Relationship between the initial orientation β and ET. Solid and dotted lines represent the best-estimated away and toward responses, respectively. Different colors represent the top 10%, 25%, and 40% quantiles of the time difference between the prey and predator within all possible ETs. (C) Circular histogram of the theoretical ETs, estimated by a Monte Carlo simulation. The probability of selection of an ET was determined by the truncated normal distribution of the optimal ranking index. This process was repeated 1000 times to estimate the frequency distribution of the theoretical ETs. Colors in the bars represent the away (blue) or toward (red) responses. Black lines represent the kernel probability density function. Concentric circles represent 10% of the total sample sizes, the bin intervals are 15°, and the bandwidths of the kernel are 50. The predator’s approach direction is represented by 0°. The dataset and R code are available at Figshare (‘Dataset1.csv’ and ‘Source code 1.R’) (n=264 from 23 individuals for experimental data, and n=264,000 for Monte Carlo simulation).

![Figure 5—figure supplement 6.](https://cdn.elifesciences.org/articles/77699/elife-77699-fig5-figsupp6-v2.jpg)

**Figure 5—figure supplement 6.:** (A) Circular plots of the time difference between the prey and predator Tdiff in different initial orientations β. The time difference of the best escape trajectory (ET) was regarded as 10 ms, and the relative time differences between 0 and 10 ms are shown by solid lines. Areas without solid lines indicate that either the time difference is below 0 or the fish cannot go to that ET because of the constraint on the possible range of |α|. Concentric circles represent 3 ms. (B) Relationship between the initial orientation β and ET. Solid and dotted lines represent the best-estimated away and toward responses, respectively. Different colors represent the top 10%, 25%, and 40% quantiles of the time difference between the prey and predator within all possible ETs. (C) Circular histogram of the theoretical ETs, estimated by a Monte Carlo simulation. The probability of selection of an ET was determined by the truncated normal distribution of the optimal ranking index. This process was repeated 1000 times to estimate the frequency distribution of the theoretical ETs. Colors in the bars represent the away (blue) or toward (red) responses. Black lines represent the kernel probability density function. Concentric circles represent 10% of the total sample sizes, the bin intervals are 15°, and the bandwidths of the kernel are 50. The predator’s approach direction is represented by 0°. The dataset and R code are available at Figshare (‘Dataset1.csv’ and ‘Source code 1.R’) (n=264 from 23 individuals for experimental data, and n=264,000 for Monte Carlo simulation).

![Figure 6.](https://cdn.elifesciences.org/articles/77699/elife-77699-fig6-v2.jpg)

**Figure 6.:** (A) The time difference between the prey and predator Tdiff at the initial orientation β of 75° is shown as an example. We defined the difference between the maximum of Tdiff (at the optimal ET) and the second local maximum of Tdiff (at the suboptimal ET) as the optimal ET advantage. (B) Relationship between the initial orientation β and the optimal ET advantage. Large and small arrows in circles represent the optimal and suboptimal ETs, respectively, for each β sectors. (C) Relationship between the optimal ET advantage and the proportion of the optimal ET used by the real prey in 20° initial orientation β bins. The line was estimated by the mixed-effects logistic regression analysis. The dataset and R code are available at Figshare (‘Dataset1.csv’ and ‘Source code 1.R’) (n=247 from 23 individuals).

Figure 5C shows the circular histogram of the overall theoretical ETs estimated by Monte Carlo simulation. The theoretical ETs show two large peaks at around 110–130° and 170–180°, and one small peak at around −100° (Figure 5C). This theoretically estimated ET distribution is similar to the frequency distribution of the observed ETs (Figure 3C); there were no significant differences in the frequency distribution between theoretical ETs (n=264 per simulation) and observed ETs (n=264) in 971 of 1000 simulations (Table 3; two-sample Kuiper test, median V=0.11, median p=0.44).

To investigate how the initial orientation of the prey modulates the proportion of using the theoretically optimal ET (i.e., where Tdiff is the maximum, Tdiff,1) compared to using the suboptimal ET (i.e., where Tdiff is the second local maximum, Tdiff,2), we calculated the optimal ET advantage (Tdiff,1−Tdiff,2) (Figure 6A), which represents the difference in the buffer time available for the prey to escape from the predator, at different initial orientations. The fish chose the optimal and suboptimal ETs to a similar extent when the optimal ET advantage is negligible (Figure 6C). For example, when looking at the optimal ET advantage <2 ms, where the initial orientation is 0‒7° and 106–180° (46% of all initial orientations), the proportion of the optimal ET used was only 55% (Figure 6B and C). On the other hand, the proportion of the optimal ET used was 81% when the optimal ET advantage is higher than 6 ms (i.e., when the initial orientation is 21–75°) (Figure 6B and C). There was a significant effect of optimal ET advantage on the proportion of the optimal ET used by fish tested in our experiments (mixed-effects logistic regression analysis, χ2=10.72, p<0.01, n=247).

To investigate the effects of two factors (i.e., the endpoint of the predator attack Dattack and the time required for the prey to turn T1(|α|)) on the predictions of ET separately, we constructed three additional geometric models (Figure 5—figure supplements 4–6): a model that includes only Dattack, a model that includes only T1(|α|), and a null model that includes neither factors (Figure 2A and Domenici, 2002). In all of these models, the theoretical ET distributions estimated through Monte Carlo simulations were significantly different from the observed ET distributions (Table 3; two-sample Kuiper test, median p<0.01). Although the model with Dattack and the model with T1(|α|) show multimodal patterns of ET distribution, the simulation based on these models do not match the experimental data, likely because of differences in the values and relative heights of the peaks (Figure 5—figure supplements 4 and 5). The null model shows a unimodal pattern of ET distribution (Figure 5—figure supplement 6).

### Potential application of the model to other ET patterns

Although many fish species and animals from other taxa exhibit multiple preferred ETs similar to what we observed here, some animals show different patterns of ETs: for example, a single preferred ET either at around 180° (Kanou et al., 1999) or at around 90° (Cooper, 2006), and multiple preferred ETs at small and large angles from the predator’s approach direction (Fuiman, 1993; Martín and López, 1996; Bulbert et al., 2015; Figure 7A–C). To investigate whether our geometric model has the potential to explain these different ET patterns, we changed the values of model parameters (e.g., Upred, Dattack) within a realistic range, and explored whether such adjustments can produce the ET patterns observed in the original work. At small Upred, the model predicts one strong peak at around 180° (Figure 7D), whereas at large Upred, the model predicts a strong peak at around 90° (Figure 7E). The model where the predator can adjust the approach path and its attack lasts for a long distance (i.e., large Dattack) predicts multiple preferred ETs directed at small (at around 30°) and large (at around 170°) angles from the predator’s approach direction (Figure 7F). These results indicate that our model has the potential to explain various patterns of observed animal ETs. See Figure 7—figure supplements 1–9 for details of the effect of each parameter on the ET distribution.

![Figure 7.](https://cdn.elifesciences.org/articles/77699/elife-77699-fig7-v2.jpg)

**Figure 7.:** Some previous studies have used the different definition for calculating the angles for ETs, in which the values range from 0° (directly toward the threat) to 180° (opposite to the threat), thereby using only one semicircle regardless of their turning direction and magnitude (e.g., both 120° and 240° of ETs are regarded as 120°). This angle is denoted as ETsemi, and is shown by a semicircular plot. (A) Unimodal ET distribution pattern at around 180° in two-spotted cricket Gryllus bimaculatus escaping from the air-puff stimulus. Data were obtained from Figure 4 in Kanou et al., 1999. (B) Unimodal ETsemi distribution pattern at around 90° in Carolina grasshopper Dissosteira carolina escaping from an approaching human. Data were obtained from Figure 3 in Cooper, 2006. (C) Bimodal ETsemi distribution pattern directed at small and large angles from the predator’s approach direction in túngara frog Engystomops pustulosus escaping from an approaching dummy bat. Data were obtained from Figure 5b in Bulbert et al., 2015 (D) Unimodal ET distribution pattern at around 180°, estimated by a Monte Carlo simulation of the geometric model. In this case, the predator speed Upred is very small (i.e., K=Upred/Uprey = 0.3), and the other parameter values are the same as the values used to explain the escape response of Pagrus major. (E) Unimodal ET distribution pattern at around 90°, estimated by a Monte Carlo simulation of the model. In this case, Upred is very large (i.e., K=Upred/Uprey = 7.5), and the other parameter values are the same as the values used to explain the escape response of P. major. (F) Bimodal ET distribution pattern directed at small and large angles from the predator’s approach direction, estimated by a Monte Carlo simulation of the geometric model where the predator can adjust its approach path. In this case, Dinitial is 130 mm, Dreact is 70 mm, Rturn is 12 mm, Dattack is 400 mm, SDchoice is 0.23, and the other parameter values are the same as the values used for explaining the escape response of P. major. Black lines represent the kernel probability density function with a bandwidth of 50, and concentric circles represent 10% of the total sample sizes. See Table 1 and the text for details of the definitions of the variables. The R code is available at Figshare (‘Source code 1.R’).

![Figure 7—figure supplement 1.](https://cdn.elifesciences.org/articles/77699/elife-77699-fig7-figsupp1-v2.jpg)

**Figure 7—figure supplement 1.:** Circular histograms of the theoretical ETs were estimated by a Monte Carlo simulation of the geometric model. ETsemi denotes the angle for ET ranging from 0° (directly toward the threat) to 180° (opposite to the threat), thereby using only one semicircle. The other parameter values are the same as the values used for explaining the escape response of Pagrus major. The R code is available at Figshare (‘Source code 1.R’).

![Figure 7—figure supplement 2.](https://cdn.elifesciences.org/articles/77699/elife-77699-fig7-figsupp2-v2.jpg)

**Figure 7—figure supplement 2.:** Circular histograms of the theoretical ETs were estimated by a Monte Carlo simulation of the geometric model. The other parameter values are the same as the values used for explaining the escape response of Pagrus major. The R code is available at Figshare (‘Source code 1.R’).

![Figure 7—figure supplement 3.](https://cdn.elifesciences.org/articles/77699/elife-77699-fig7-figsupp3-v2.jpg)

**Figure 7—figure supplement 3.:** Circular histograms of the theoretical ETs were estimated by a Monte Carlo simulation of the geometric model. The other parameter values are the same as the values used for explaining the escape response of Pagrus major. The R code is available at Figshare (‘Source code 1.R’).

![Figure 7—figure supplement 4.](https://cdn.elifesciences.org/articles/77699/elife-77699-fig7-figsupp4-v2.jpg)

**Figure 7—figure supplement 4.:** Circular histograms of the theoretical ETs were estimated by a Monte Carlo simulation of the geometric model. The other parameter values are the same as the values used for explaining the escape response of Pagrus major. The R code is available at Figshare (‘Source code 1.R’).

![Figure 7—figure supplement 5.](https://cdn.elifesciences.org/articles/77699/elife-77699-fig7-figsupp5-v2.jpg)

**Figure 7—figure supplement 5.:** Circular histograms of the theoretical ETs were estimated by a Monte Carlo simulation of the geometric model where the predator can adjust its approach path. Dinitial is 130 mm, Dreact is 70 mm, Rturn is 12 mm, Dattack is 400 mm, and the other parameter values are the same as the values used for explaining the escape response of Pagrus major. The R code is available at Figshare (‘Source code 1.R’).

![Figure 7—figure supplement 6.](https://cdn.elifesciences.org/articles/77699/elife-77699-fig7-figsupp6-v2.jpg)

**Figure 7—figure supplement 6.:** Circular histograms of the theoretical ETs were estimated by a Monte Carlo simulation of the geometric model where the predator can adjust its approach path. Dinitial is 130 mm, Dreact is 70 mm, Rturn is 12 mm, and the other parameter values are the same as the values used for explaining the escape response of Pagrus major. The R code is available at Figshare (‘Source code 1.R’).

![Figure 7—figure supplement 7.](https://cdn.elifesciences.org/articles/77699/elife-77699-fig7-figsupp7-v2.jpg)

**Figure 7—figure supplement 7.:** Circular histograms of the theoretical ETs were estimated by a Monte Carlo simulation of the geometric model where the predator can adjust its approach path. Dreact is 70 mm, Rturn is 12 mm, Dattack is 400 mm, and the other parameter values are the same as the values used for explaining the escape response of Pagrus major. The R code is available at Figshare (‘Source code 1.R’).

![Figure 7—figure supplement 8.](https://cdn.elifesciences.org/articles/77699/elife-77699-fig7-figsupp8-v2.jpg)

**Figure 7—figure supplement 8.:** Circular histograms of the theoretical ETs were estimated by a Monte Carlo simulation of the geometric model where the predator can adjust its approach path. Dinitial is 130 mm, Dreact is 70 mm, Dattack is 400 mm, and the other parameter values are the same as the values used for explaining the escape response of Pagrus major. The R code is available at Figshare (‘Source code 1.R’).

![Figure 7—figure supplement 9.](https://cdn.elifesciences.org/articles/77699/elife-77699-fig7-figsupp9-v2.jpg)

**Figure 7—figure supplement 9.:** Circular histograms of the theoretical ETs were estimated by a Monte Carlo simulation of the geometric model where the predator can adjust its approach path. Dinitial is 130 mm, Dreact is 70 mm, Dattack is 400 mm, and the other parameter values are the same as the values used for explaining the escape response of Pagrus major. The R code is available at Figshare (‘Source code 1.R’).

## Discussion

Our geometric model, incorporating the endpoint of the predator attack, Dattack, and the time required for the prey to turn, T1(|α|), to maximize the difference between the prey and the predator in the time of arrival at the edge of the safety zone, Tdiff, clearly explains the multimodal patterns of ETs in P. major. Figure 8 shows an example of how multiple ETs result in successful escapes from predators. Specifically, according to the model, when the prey escapes at 140° or 170°, it will not be captured by the predator. On the other hand, when the prey escapes along an intermediate trajectory (157°), it will be captured because it swims toward the corner of the danger zone to exit it, and therefore it needs to travel a longer distance than when escaping at 140° or 170°. This example illustrates that the multimodal patterns of ETs are likely to be attributable to the existence of two escape routes: either moving sideways to depart from the predator’s strike path or moving opposite to the predator’s direction to outrun it. Interestingly, both components of the predator-prey interaction (i.e., Dattack and T1(|α|)) added to the previous model (Domenici, 2002) are important for accurate predictions of the ET distribution because when they are considered by the model separately, the predictions do not match the experimental data (Figure 5—figure supplements 4 and 5; Table 3).

![Figure 8.](https://cdn.elifesciences.org/articles/77699/elife-77699-fig8-v2.jpg)

**Figure 8.:** The area enclosed by dash-dotted lines represents the danger zone the prey needs to exit in order to escape predation, outside of which is the safety zone. When the prey escapes toward the corner of the danger zone (ET = 157°) to exit it, it needs to travel a relatively long distance and therefore the predator can catch it. On the other hand, when the prey escapes with an ET at 170° or 140°, it covers a shorter distance and can reach the safety zone before the predator’s arrival. When the prey escapes with an even smaller ET (90°), it will be captured because the shorter travel distance for the predator overrides the benefits of the smaller turn and shorter travel distance for the prey. When the prey escapes with an even larger ET (190°), it will also be captured, because the prey requires a longer time to turn than if escaping along the 170° ET, whereas the travel distance for both predator and prey is the same as that for the 170° ET. In this example, the initial orientation, flight initiation distance, and the body length posterior to the center of mass were set as 110°, 60 mm and 30 mm, respectively.

Two different escape tactics have been proposed to enhance the success of predator evasion (Jensen, 2018; Domenici et al., 2011a): the optimal tactic, which maximizes Tdiff (i.e., the distance between the prey and the predator) (Arnott et al., 1999; Weihs and Webb, 1984; Domenici, 2002; Soto et al., 2015), and the protean tactic, which maximizes unpredictability to prevent predators from adjusting their strike trajectories accordingly (Humphries and Driver, 1970; Jones et al., 2011; Richardson et al., 2018; Moore et al., 2017). Our results suggest that the prey combines these two different tactics by using multiple preferred ETs. Specifically, when the optimal ET advantage is large (i.e., when the initial orientation is 20–60°), the prey mainly uses the optimal ET (Figures 3A and 6). However, when the optimal ET advantage over the suboptimal ET is negligible (i.e., the initial orientation is close to 0° or within the range 110‒180°), the prey uses optimal and suboptimal ETs to a similar extent (Figures 3A and 6). In such cases, the ET of the prey would be highly unpredictable for the predator. The unpredictability at initial orientations near 0° and 180° is consistent with the study that applied the conventional geometric model to the larval zebrafish Danio rerio (Nair et al., 2017), where the optimal and suboptimal ETs are approximately symmetrical to the axis of the predator attack. This phenomenon can be explained by the toward-away indecision at orientations nearly perpendicular to the threat (Domenici and Blake, 1993; Domenici and Batty, 1997). On the other hand, the unpredictability observed at initial orientations near 110–180° is related to the similarly advantageous choice between escaping with an ET at around 140° or 180°. Interestingly, at initial orientations >120°, our results show that these two ETs are reached by using toward and away responses, respectively. The overlap between the ETs of toward and away responses in the overall dataset (Figure 3) suggests that toward responses are not ‘tactical mistakes’ of the prey that turns toward a threat, but are simply related to reaching an optimal or suboptimal ET. These results suggest that the prey strategically adjusts the use of optimal and protean tactics based on their initial orientation. This allows the prey to have unpredictable ETs, thereby preventing predators from anticipating their escape behavior, while keeping Tdiff large enough to enter the safety zone before the predator reaches it.

From a behavioral decision-making perspective, our results suggest that the prey follows the matching law (Reed and Kaplan, 2011; Poling et al., 2011; McDowell, 2013; Houston et al., 2021), where the probability that an optimal or suboptimal ET is chosen is proportional to its chances of survival (i.e., Tdiff). As the matching law predicts (Houston et al., 2021), the prey stochastically draws from a Bernoulli distribution dictated by the optimal ET advantage for the binary choice between an optimal and a suboptimal ET, thereby introducing an element of unpredictability, which can prevent predators from learning. Because most empirical studies supporting the matching law use unnatural reinforcement learning paradigms or human behaviors (Reed and Kaplan, 2011; Poling et al., 2011; McDowell, 2013; Houston et al., 2021), this result suggests that the matching law is also applicable to animal behavior in realistic contexts. Further research using a real predator and dummy prey (e.g., Szopa-Comley and Ioannou, 2022) controlled to escape toward an optimal or suboptimal ET with various specific probabilities is required to test whether our model accurately predicts the best combination of the optimal and suboptimal ETs when accounting for the predator learning.

A relevant question from a perspective of neurosensory physiology is how the animals are able to determine their ETs within milliseconds of response time. The initial orientation of the prey has been incorporated into various neural circuit models (Eaton et al., 2001; Yono and Shimozawa, 2008; Card, 2012; Levi and Camhi, 2000), but these models assume that prey animals always escape in a 180° direction (i.e., opposite to the stimulus source), irrespective of the initial orientation. However, the present study shows that animals use suboptimal ETs as well as optimal ETs, and that these ETs may change in a nonlinear fashion, depending on the initial orientation. More specifically, the Mauthner cell and other neurons involved may be activated in accordance with the Bernoulli probabilities dictated by the model, which determine the proportions of away and toward responses and the magnitude of turn to achieve the multiple preferred ETs. Thus, we require new neurophysiological models of ETs to understand how neural circuits process the sensory cues of a threatening stimulus, resulting in muscle actions that generate multiple preferred ETs.

Our geometric model assumes that the prey determines the ETs based on a fixed predator speed. This assumption is supported by the results of our experiments, where the effects of predator speed on the mean and variability of ETs are not significant. Although we did not find any effect of predator speed, it is possible that a speed outside the range we used may affect ETs. Recent studies show that larval zebrafish exhibit less variable ETs under faster threats than they do under slower threats (Stewart et al., 2014; Bhattacharyya et al., 2017), and the difference in ET variability between fast and slow threats is dependent on whether the Mauthner cell is active or not (Bhattacharyya et al., 2017). Therefore, any differences in the ET variability of the present study compared to previous studies could be related to the different involvement of the Mauthner cells. Using the conventional geometric model (Weihs and Webb, 1984), Soto et al. showed that the choice of ET only matters to a prey when the predator speed is intermediate, because a prey that is much faster than its predator can escape by a broad range of ETs, whereas a prey that is much slower than its predator cannot escape by any ETs (Soto et al., 2015). The predator speed used in this study is in the range of the real predator speed in the previous study using the same species of both predator and prey (Kimura and Kawabata, 2018). Thus, our results are ecologically relevant, and the prey is likely to have optimized their ETs based on a fixed predator speed, where the choice of ET strongly affects their survival.

The relationship between |α| and the time required for a 15 mm displacement, T1(|α|), (Figure 4A) indicates that the time required for a 15 mm displacement is relatively constant up to an |α| of about 45°, while a further change in |α| requires additional time. This relationship is likely to be attributable to the kinematics and hydrodynamics of the C-start escape response, because the initial velocity after the stage 1 turn increases linearly up to about 45°, beyond which it plateaus (Figure 4B). Interestingly, a recent study on swimming efficiency during acceleration found that efficiency increases linearly with yaw amplitudes up to a certain value, beyond which efficiency plateaus (Akanyeti et al., 2017).

Based on the STRANGE framework for animal behavior research (Webster and Rutz, 2020), we identified potential biases that may limit the generalizability of our findings. Our empirical data are obtained from one species of hatchery-reared fish with a specific life stage, which has never experienced predators. Therefore, this study alone cannot exclude the possibility that fish of different species, origins, life stages, and rearing histories have different rules for ETs, which our model cannot explain. However, similar multiple preferred ETs have been observed in many fish species and other animal taxa, including hatcheries/wild origins and different life stages (Domenici et al., 2011b). Therefore, we believe that our model is not specific to our experiment but is applicable to other cases showing multiple preferred ETs.

We show that our model has the potential to explain other empirically observed ET patterns (Figure 7). Based on the model assuming that the predator makes an in-line attack toward the prey, which is realistic for ambush and stalk-and-attack predators (Moore and Biewener, 2015) (e.g., frogs [Camhi et al., 1978], spiders [Dangles et al., 2006], and fish [Kimura and Kawabata, 2018; Webb and Skadsen, 1980; Fouts and Nelson, 1999; Rand and Lauder, 1981]), either single or multiple ETs at around 90–150° and around 180° are predicted, as have been observed in many empirical studies of animals escaping from ambush predators and artificial stimuli (Domenici et al., 2011b). Based on the model assuming that the predator can adjust its approach path, which is realistic for pursuit predators, multiple ETs directed at small and large angles from the predator’s approach direction can be predicted, as observed in the empirical studies of prey escaping from pursuit predators (Corcoran and Conner, 2016; Bulbert et al., 2015). Further research measuring the escape response in various species and applying the data to our geometric model is required to verify the applicability of our geometric model to various predator-prey systems.

Our work represents a major advancement in understanding the basis of the variability in ETs observed in previous works (reviewed in Domenici et al., 2011b). Our results suggest that prey use multiple preferred ETs to maximize the time difference between themselves and the attacking predator, while keeping a high level of unpredictability. The results also suggest that prey strategically adjust the use of protean and optimal tactics with respect to the advantage of the optimal ET over the suboptimal ET. Because multimodal ETs similar to what we observed here have been found in many fish species and other animal taxa (Domenici et al., 2011b), this behavioral phenotype may result from convergent evolution in phylogenetically distant animals. From a neurosensory perspective, our findings open new avenues to investigate how the animals determine their ETs from multiple options with specific probabilities, which are modulated by the initial orientation with respect to the threat.

## Materials and methods

### Definition of the angles

The C-start escape response consists of an initial bend (stage 1), followed by a return tail flip (stage 2), and continuous swimming or coasting (stage 3) (Domenici and Blake, 1997; Weihs, 1973). In line with previous studies (Domenici et al., 2011b; Nair et al., 2017; Stewart et al., 2013), we defined initial orientation β, directionality (away or toward responses), turn angle α, and ET α+β as follows (Figure 2—figure supplement 1). Initial orientation (β): the angle between the line passing through the prey’s CoM (located at 34% of the total length from the tip of the snout; Kimura and Kawabata, 2018) and the tip of the snout at the onset of stage 1, and the midline of the predator model attacking in a straight line. Initial orientation ranges from 0° (i.e., when the prey is attacked from front) to 180° (i.e., when the prey is attacked from behind). Directionality: the away and toward responses were defined by the first detectable movement of the fish in a direction either away from or toward the predator, respectively (Domenici et al., 2011b). In rare cases (n=3; 1.1% of the total observations) where the initial orientation is exactly 0° (n=1) or 180° (n=2), the counterclockwise and clockwise turns were regarded as away and toward responses, respectively. Turn angle (α): the angle between the line passing through the CoM and the tip of the snout at the onset of stage 1, and the line passing through the CoM at the onset of stage 1 and the CoM at the end of stage 2. The angles of the away and toward responses are assigned positive and negative values, respectively. ET (α+β): the angular sum of the initial orientation (β) and the turn angle (α). Because the experimental data exhibited no asymmetry in directionality (Fisher’s exact test, p=1.00, n=264) and ET distribution (two-sample Kuiper test, V=0.14, p=0.61, n=264), we pooled the ETs from the left and right sides, treating all fish as though they were attacked from the right side (Domenici et al., 2011b). ET is a circular variable with a cycle of 360°. As the range of |β| is 0–180° and the range of |α| was 9–147° in the experiment, the ET value can potentially range from −147° to 327°. Circular graphs are shown with angles from 0° to 360° (Batschelet, 1981), where negative values such as −90° correspond to positive values shifted by one cycle (in this case, −90°+360°=270°).

### Experiment

Following the STRANGE framework for animal behavior research (Webster and Rutz, 2020), we provide details of the test samples and experimental procedure in the following two subsections.

#### Sample fish

We used young-of-year juvenile hatchery-reared red sea bream P. major for the experiment. Sixty-five individuals were purchased from commercial hatcheries (Marua Suisan Co., Ltd., Ehime, Japan), where they were reared communally in artificial tanks. After arriving at the laboratory at Nagasaki University, they were kept in a 200 l polycarbonate tank and were fed with commercial pellets (Otohime C2; Marubeni Nisshin Feed Co. Ltd, Tokyo, Japan) twice a day. The sex of the fish was not determined because the species of this size is in a bisexual juvenile stage (Law and Sadovy de Mitcheson, 2017). Water temperature was maintained at 23.8–24.9°C.

#### Experimental procedure

We have elicited the escape response of P. major (45.3±3.5 [39.4–51.5] mm total length, 37.2±2.9 [32.3–42.2] mm standard length, 1.6±0.4 [0.9–2.3] g body weight, mean ± s.d. [range], n=23) using a dummy predator. The value of Fulton’s condition factor (30.64±2.43 [26.10–35.56], mean ± s.d. [range]), calculated by the body weight of the fish divided by the standard length cubed, suggests that all fish were in a good nutritious condition (Miyajima-taga et al., 2014; Kudoh et al., 2002). The experiment was conducted in a plastic tank (540 × 890 × 200 mm3) filled with seawater to a depth of 80 mm. The water temperature was maintained at 23.8–24.7°C. An individual P. major was randomly captured by a hand net from the holding tank, introduced into a PVC pipe (60 mm diameter) set in the center of the experimental tank, and acclimated for 15 min. Because it was not difficult to capture any individual by a hand net, there should be no bias in selecting individuals with specific behavioral types. After the acclimation period, the PVC pipe was slowly removed, and the dummy predator, a cast of Sebastiscus marmoratus (164 mm in total length and 36 mm in mouth width), was moved toward the P. major for a distance of 200 mm (Figure 3—figure supplement 3A). The dummy predator was held in place by a metal pipe anchored to a four-wheel dolly, which is connected to a fixed metal frame via two plastic rubber bands (Figure 3—figure supplement 3B). The wheel dolly was drawn back to provide power for the dummy predator to strike toward the prey. Because the previous work shows that S. marmoratus attacks P. major using a variable speed (1.10±0.65 [0.09–2.31] m s−1, mean ± s.d. [range]) (Kimura and Kawabata, 2018), we used various strengths of plastic rubber bands to investigate the effect of predator speed on ET. The fish movements were recorded from above, using a high-speed video camera (HAS-L1; Ditect Co., Tokyo, Japan) at 500 frames s−1. Each individual P. major was stimulated from 5 to 23 times with a time interval of at least 15 min, and, in total, 297 trials were conducted. We eliminated 33 trials from the analysis because P. major moved away from the striking course of the dummy predator before the stimulation (in 14 trials) and because bubbles obscured the P. major image (in 19 trials). The final data analyzed are 5–20 escape responses per individual and, in total, 264 escape responses. The experiments for each P. major were accomplished within 1 day to eliminate possible effects of tank transfer, handling, and change of rearing conditions. The number of recordings of an individual P. major was different because we could not allocate the same amount of time to the experiment per day due to the experimental schedule and because the numbers of eliminated data are different among individuals. The recorded videos were analyzed frame by frame using Dipp-Motion Pro 2D (Ditect Co.). The CoM and the tip of the mouth of P. major and the tip of the predator’s mouth were digitized in each frame to calculate all the kinematic variables. The animal care and experimental procedures were approved by the Animal Care and Use Committee of the Faculty of Fisheries (Permit No. NF-0002), Nagasaki University in accordance with the Guidelines for Animal Experimentation of the Faculty of Fisheries and the Regulations of the Animal Care and Use Committee, Nagasaki University.

#### Statistical analysis

Because our geometric model predicts that the initial orientation β and the predator speed Upred affect the ET and turn angle α, we examined these effects by the experimental data using a GAMM with a normal distribution and identity link function (Zuur et al., 2009). ET and α were regarded as objective variables, while predator speed and initial orientation were regarded as explanatory variables and were modeled with a B-spline smoother. Fish ID was regarded as a random factor. Smoothed terms were fitted using penalized regression splines, and the amount of smoothing was determined using the restricted maximum likelihood method. As was done in previous studies (Domenici et al., 2011b; Domenici et al., 2009; Nair et al., 2017), the away and toward responses were analyzed separately. The significance of the initial orientation and predator speed was assessed by the F-test. The analysis was conducted using R 3.5.3 (R Foundation for Statistical Computing) with the R package gamm4.

### Determination of parameter values

#### Determination of the Prey’s kinematic parameters

The relationship between |α| and the time required for a displacement of 15 mm, T1(|α|), was estimated by piecewise linear regression (Brilleman et al., 2017). We used piecewise linear regression rather than a commonly used smoothing method such as GAMM, because the smoothing method does not output the timing of the regression change and thus the biological interpretation of the regression curve is problematic (Brilleman et al., 2017). The time required for a displacement of 15 mm was regarded as an objective variable, whereas |α| was regarded as an explanatory variable. Fish ID was included as a covariate in order to take into account potential individual differences in the relationship, T1(|α|). To detect the possible kinematic mechanism of the relationship T1(|α|), we also examined the relationship between |α| and initial velocity after the stage 1 turn, using piecewise linear regression. Initial velocity after the stage 1 turn was regarded as an objective variable, |α| was regarded as an explanatory variable, and fish ID was included as a covariate. A hierarchical Bayesian model with a Markov chain Monte Carlo (MCMC) method was used to estimate these relationships (Brilleman et al., 2017; Kéry and Schaub, 2011). The number of draws per chain, thinning rate, burn-in length, and number of chains were set as 200,000, 1, 100,000, and 5, respectively. To test the overall fit of the model, the WAIC of the model was compared with those of the null model (constant) and a simple linear regression model. MCMC was conducted using RStan 2.18.2 (Stan Development Team 2019).

#### Determination of predator speed and endpoint of the predator attack

Because we had no previous knowledge about the values of Upred and Dattack that the prey regards as dangerous (i.e., the values of Upred and Dattack that trigger a response in the prey), we optimized the values using the experimental data in this study. We have input the obtained values of Dwidth, Rdevice, D1, Uprey, and T1(|α|) into the theoretical model. The optimal values of Upred and Dattack were obtained using the ranking index. The ranks of the observed ETs among the theoretical ET choices of 1° increment were standardized as the ranking index, where 0 means that the real fish chose the theoretically optimal ET where Tdiff is the maximum, and 1 means that the real fish chose the theoretically worst ET where Tdiff is the minimum. The optimal set of Dattack and Upred values was determined by minimizing the mean ranking index of the observed ETs. The distribution of the optimal ranking index was then fitted to the truncated normal distribution and was used to predict how the fish chose the ETs from the continuum of the theoretically optimal and worst ETs.

### Model predictions

We input the above parameters (Dwidth, Rdevice, D1, Uprey, T1(|α|), Dattack, and Upred) into the model and calculated how the choice of different ETs affects Tdiff for each initial orientation β. Because there was a constraint on the possible range of |α| (i.e., fish escaping by C-start have a minimum and maximum |α| Domenici and Blake, 1991), the range of |α| was determined based on its minimum and maximum values observed in our experiment, which were 9–147°.

To estimate the overall frequency distribution of ETs that include the data on observed initial orientations, we conducted Monte Carlo simulations. In each observed initial orientation, the ET was chosen from the continuum of the theoretically optimal and worst ETs. The probability of the ET selection was determined by the truncated normal distribution of the optimal ranking index (e.g., the fish could choose theoretically good ETs with higher probability than theoretically bad ETs, but the choice is a continuum based on the truncated normal distribution). This process was repeated 1000 times to robustly estimate the frequency distribution of the theoretical ETs. In each simulation run, the frequency distribution of the theoretical ETs was compared with that of the observed ETs using the two-sample Kuiper test (Zar, 2010).

To investigate how the real prey changes the probability that it uses the theoretically optimal ET or suboptimal ET, we regarded the difference between the maximum of Tdiff (at the optimal ET) and the second local maximum of Tdiff (at the suboptimal ET) as the optimal ET advantage, and theoretically estimated the values for all initial orientations. We then examined the relationship between the optimal ET advantage and the proportion of the optimal ET the prey actually chose using a mixed-effects logistic regression analysis (Zuur et al., 2009). Each observed ET was designated as the optimal (1) or the suboptimal (0) based on whether the observed ET was closer to the optimal ET or suboptimal ET. When the prey chose the ET that was more than 35° different from both the optimal and suboptimal ETs, the ET data point was removed from the analysis (these cases were rare: 7%). The choice of ET (optimal (1) or suboptimal (0)) was regarded as an objective variable, while the optimal ET advantage was regarded as an explanatory variable. Fish ID was regarded as a random factor. The significance of the optimal ET advantage was assessed by the likelihood ratio test with χ2 distribution. The analysis was conducted using R 3.5.3 with the R package lme4.

To investigate the effects of two factors (i.e., the endpoint of the predator attack Dattack and the time required for the prey to turn T1(|α|)) on predictions of ET separately, we compared four geometric models: the model that includes both Dattack and T1(|α|), the model that includes only Dattack, the model that includes only T1(|α|), and the null model. Note that the null model is equivalent to the previous Domenici’s model (Domenici, 2002). In all models, the values of Upred and Dattack were optimized using the ranking index. The overall frequency distributions of ETs were estimated through Monte Carlo simulations, and in each simulation run, the theoretical ET distribution was compared with the observed ET distribution using the two-sample Kuiper test.

To investigate whether our model has the potential to explain other empirical ET patterns, we changed the values of model parameters (e.g., Upred, Dattack) within a realistic range, and conducted Monte Carlo simulations to estimate the frequency distribution of the theoretical ETs. For each initial orientation, ranging from 0° to 180° with an increment of 1°, the ET was chosen based on the probability of the truncated normal distribution (i.e., the continuum of the theoretically optimal and worst ETs), and this process was repeated 100 times. In the model where the predator cannot adjust the strike path (Figure 2B), we fixed three parameters and varied the fourth parameter (Upred, Dattack, Rdevice, and s.d. of the truncated normal distribution for ET choice, SDchoice) from the model produced for the escape response of P. major (i.e., Dattack = 34.73 mm, Upred = 1.54 m s–1, Rdevice = 199 mm, SDchoice = 0.33). Using the model where the predator can adjust the strike path (Appendix 1—figure 1B), we simulate the situation in which the safety zone shape inside the predator’s turning radius is similar to the Corcoran’s model (Appendix 1—figure 1A) but we included a safety zone opposite to the incoming direction of the predator. We considered Dattack as 400 mm, Dinitial as 130 mm, the minimum turning radius of the predator Rturn as 12 mm, and the reaction distance of the predator Dreact as 70 mm. We used the same values of the P. major model for Rdevice and the other parameters. We then fixed four parameters and varied the fifth parameter (Upred, Dattack, Dinitial, Rturn, SDchoice) to examine the effect of each parameter on the ET distribution.
