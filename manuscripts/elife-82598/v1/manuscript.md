# The impact of task context on predicting finger movements in a brain-machine interface

## Authors

- Matthew J Mender<sup>1</sup> ([ORCID: 0000-0003-1562-3289](https://orcid.org/0000-0003-1562-3289))
- Samuel R Nason-Tomaszewski<sup>1</sup>
- Hisham Temmar<sup>1</sup> ([ORCID: 0000-0002-4464-4911](https://orcid.org/0000-0002-4464-4911))
- Joseph T Costello<sup>2</sup>
- Dylan M Wallace<sup>3</sup>
- Matthew S Willsey<sup>1</sup>
- Nishant Ganesh Kumar<sup>4</sup>
- Theodore A Kung<sup>4</sup>
- Parag Patil<sup>1</sup> †
- Cynthia A Chestek<sup>1</sup> ([ORCID: 0000-0002-9671-7051](https://orcid.org/0000-0002-9671-7051)) †

### Affiliations

1. Department of Biomedical Engineering University of Michigan-Ann Arbor Ann Arbor United States
2. Department of Electrical Engineering and Computer Science University of Michigan-Ann Arbor Ann Arbor United States
3. Department of Robotics University of Michigan-Ann Arbor Ann Arbor United States
4. Department of Surgery University of Michigan-Ann Arbor Ann Arbor United States

† Corresponding author

## Abstract

A key factor in the clinical translation of brain-machine interfaces (BMIs) for restoring hand motor function will be their robustness to changes in a task. With functional electrical stimulation (FES) for example, the patient's own hand will be used to produce a wide range of forces in otherwise similar movements. To investigate the impact of task changes on BMI performance, we trained two rhesus macaques to control a virtual hand with their physical hand while we added springs to each finger group (index or middle-ring-small) or altered their wrist posture. Using simultaneously recorded intracortical neural activity, finger positions, and electromyography, we found that decoders trained in one context did not generalize well to other contexts, leading to significant increases in prediction error, especially for muscle activations. However, with respect to online BMI control of the virtual hand, changing either the decoder training task context or the hand's physical context during online control had little effect on online performance. We explain this dichotomy by showing that the structure of neural population activity remained similar in new contexts, which could allow for fast adjustment online. Additionally, we found that neural activity shifted trajectories proportional to the required muscle activation in new contexts. This shift in neural activity possibly explains biases to off-context kinematic predictions and suggests a feature that could help predict different magnitude muscle activations while producing similar kinematics.
