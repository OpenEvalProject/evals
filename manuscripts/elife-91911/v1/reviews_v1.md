# Peer review - Round 1

Editors:
- Yongliang Yang, Dalian University of Technology China

Reviewers:
- (Reviewers not individually listed)

## Review text

DOI: [10.7554/eLife.91911.3.sa0](https://doi.org/10.7554/eLife.91911.3.sa0)

This valuable prospective study develops a new tool to accelerate pharmacological studies by using neural networks to emulate the human ventricular cardiomyocyte action potential. The evidence supporting the conclusions is convincing, based on using a large and high-quality dataset to train the neural network emulator. There are nevertheless a few areas in which the article may be improved through validating the neural network emulators against extensive experimental data. In addition, the article may be improved through delineating the exact speed-up achieved and the scope for acceleration. The work will be of broad interest to scientists working in cardiac simulation and quantitative system pharmacology.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.91911.3.sa1](https://doi.org/10.7554/eLife.91911.3.sa1)

Summary:

The authors present a neural network (NN)-based approach to computationally cheaper emulation of simulations of biophysically relatively detailed cardiac cell models based on systems of ordinary differential equations. Relevant case studies are used to demonstrate the performance in prediction of standard action potentials, as well as action potentials manifesting early depolarizations. Application to the "reverse problem" (inferring the effect of pharmacological compounds on ion channels based on action potential data before and after drug treatment) is also explored, which is a task of generally high interest.

Strengths:

This is a well-designed study, which explores an area that many in the cardiac simulation community will be interested in. The article is well written and I particularly commend the authors on transparency of methods description, code sharing, etc. - it feels rather exemplary in this regard and I only wish more authors of cardiac simulation studies took such an approach. The training speed of the network is encouraging and the technique is accessible to anyone with a reasonably strong GPU, not needing specialized equipment.

Weaknesses:

Below are several points that I consider to be weaknesses and/or uncertainties of the work:

1. The scope for acceleration of single cell simulations is not vast, as it is easy to simulate tens of thousands of cells per day on a workstation computer, using simulation conditions similar to those of the authors. While this covers a large part of what is needed in the field, I agree with the authors that there are applications where the presented technology is helpful. In such cases, e.g., in uncertaintly quantification, it will enable studies that would be difficult to carry out previously. In addition, any application involving long-term pre-pacing of a large number of cells will benefit greatly from the reported tool.

An area which is definitely in need of acceleration is simulations of whole ventricles or hearts, but it is not clear how much potential for speedup would the presented technology bring there. I can imagine interesting applications of rapid emulation in such a setting, some of which could be hybrid in nature (e.g. using simulation for the region around the wavefront of propagating electrical waves, while emulating the rest of the tissue, which is behaving more regularly/predictable, and is likely to be emulated well), but this is definitely beyond of the scope of this article.

2. The exact speed-up achieved by the NN emulation is somewhat context-dependent. In particular, the reported speedup critically depends on the number of beats in the simulation. The emulator learns to directly estimate the state of the cell after X beats (where X is decided by the operator of training). The speedup appears to be relatively marginal when a single beat is simulated versus emulated - but when 1000 beats are simulated, this takes 1000fold more time for simulation, but unchanged time for emulation.

While the initial submission did not communicate the practical speedup entirely clearly, this was addressed well by the authors in the revised version.

3. It appears that the accuracy of emulation drops off relatively sharply with increasing real-world applicability/relevance of the tasks it is applied to. That said, the authors are to be commended on declaring this transparently, rather than withholding such analyses. I particularly enjoyed the discussion of the not always amazing results of the inverse problem on the experimental data. The point on low parameter identifiability is an important one, and serves as a warning against overconfidence in our ability to infer cellular parameters from action potentials alone. On the other hand, I'm not that sure the difference between small tissue preps and single cells which authors propose as another source of the discrepancy will be that vast beyond the AP peak potential (probably much of the tissue prep is affected by the pacing electrode?), but that is a subjective view only. The influence of coupling could be checked if the simulated data were generated from 2D tissue samples/fibres, e.g. using the Myokit software.

In summary, I believe the range of tasks where the emulator provides a major advance is relatively narrow, particularly given the relatively limited need for further speedup compared to simulations. However, this does not make the study uninteresting in the slightest - on the contrary, it explores something that many of us are thinking about, and it is likely to stimulate further development in the direction of computationally efficient emulation of relatively complex simulations.


---

# Peer review - Round 1

Reviewers:
- Anonymous Reviewer

## Review text

DOI: [10.7554/eLife.91911.3.sa2](https://doi.org/10.7554/eLife.91911.3.sa2)

Summary:

1. Grandits and colleagues were trying to develop a new tool to accelerate pharmacological studies by using neural networks to emulate the human ventricular cardiomyocyte action potential (AP). The AP is a complex electrical signal that governs the heartbeat, and it is important to accurately model the effects of drugs on the AP to assess their safety and efficacy. Traditional biophysical simulations of the AP are computationally expensive and time-consuming. The authors hypothesized that neural network emulators could be trained to predict the AP with high accuracy and that these emulators could also be used to quickly and accurately predict the effects of drugs on the AP.

Strengths:

2. One of the study's major strengths is that the authors use a large and high-quality dataset to train their neural network emulator. The dataset includes a wide range of APs, including normal and abnormal APs exhibiting EADs. This ensures that the emulator is robust and can be used to predict the AP for a variety of different conditions.

Another major strength of the study is that the authors demonstrate that their neural network emulator can be used to accelerate pharmacological studies. For example, they use the emulator to predict the effects of a set of known arrhythmogenic drugs on the AP. The emulator is able to predict the effects of these drugs, even though it had not been trained on these drugs specifically.

Weaknesses:

One weakness of the study is that it is important to validate neural network emulators against experimental data to ensure that they are accurate and reliable. The authors do this to some extent, but further validation would be beneficial. In particular for the inverse problem, where the estimation of pharmacological parameters very challenging and led to particularly large inaccuracies.

Additional context:

4. The work by Grandits et al. has the potential to revolutionize the way that pharmacological studies are conducted. Neural network emulation has the promise to reduce the time and cost of drug development and to improve the safety and efficacy of new drugs. The methods and data presented in the paper are useful to the community because they provide a starting point for other researchers to develop and improve neural network emulators for the human ventricular cardiomyocyte AP. The authors have made their code and data publicly available, which will facilitate further research in this area.

5. It is important to note that neural network emulation is still a relatively new approach, and there are some challenges that need to be addressed before it can be widely adopted in the pharmaceutical industry. For example, neural network emulators need to be trained on large and high-quality datasets. Additionally, it is important to validate neural network emulators against experimental data to ensure that they are accurate and reliable. Despite these challenges, the potential benefits of neural network emulation for pharmacological studies are significant. As neural network emulation technology continues to develop, it is likely to become a valuable tool for drug discovery and development.
