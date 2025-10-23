# Real-time, low-latency closed-loop feedback using markerless posture tracking

## Authors

- Gary A Kane<sup>1</sup> ([ORCID: 0000-0002-7703-5055](https://orcid.org/0000-0002-7703-5055))
- Gonçalo Lopes<sup>2</sup> ([ORCID: 0000-0003-0731-4945](https://orcid.org/0000-0003-0731-4945))
- Jonny L Sanders<sup>3</sup>
- Alexander Mathis<sup>4</sup> ([ORCID: 0000-0002-3777-2202](https://orcid.org/0000-0002-3777-2202))
- Mackenzie Mathis<sup>5</sup> ([ORCID: 0000-0001-7368-4456](https://orcid.org/0000-0001-7368-4456)) †

### Affiliations

1. Department of Psychology Princeton University Princeton United States
2. NeuroGears London United Kingdom
3. Institute of Neuroscience, Department of Psychology University of Oregon Eugene United States
4. Life Sciences EPFL Geneva Switzerland
5. Brain Mind Institute EPFL Genève Switzerland

† Corresponding author

## Abstract

The ability to control a behavioral task or stimulate neural activity based on animal behavior in real-time is an important tool for experimental neuroscientists. Ideally, such tools are noninvasive, low-latency, and provide interfaces to trigger external hardware based on posture. Recent advances in pose estimation with deep learning allows researchers to train deep neural networks to accurately quantify a wide variety of animal behaviors. Here we provide a new DeepLabCut-Live! package that achieves low-latency real-time pose estimation (within 15 ms, >100 FPS), with an additional forward-prediction module that achieves zero-latency feedback, and a dynamic-cropping mode that allows for higher inference speeds. We also provide three options for using this tool with ease: (1) a stand-alone GUI (called DLC-Live! GUI, and integration into (2) Bonsai and (3) AutoPilot. Lastly, we benchmarked performance on a wide range of systems so that experimentalists can easily decide what hardware is required for their needs.
