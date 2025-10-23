# Scratch-AID: a deep-learning based system for automatic detection of mouse scratching behavior with high accuracy

## Authors

- Huasheng Yu<sup>1</sup> †
- Jingwei Xiong<sup>2</sup>
- Adam Yongxin Ye<sup>3</sup>
- Suna Li Cranfill<sup>1</sup> ([ORCID: 0000-0002-3431-0061](https://orcid.org/0000-0002-3431-0061))
- Tariq Cannonier<sup>1</sup>
- Mayank Gautam<sup>1</sup> ([ORCID: 0000-0002-7257-5837](https://orcid.org/0000-0002-7257-5837))
- Marina Zhang<sup>4</sup>
- Rayan Bilal<sup>1</sup>
- Jong-Eun Park<sup>1</sup>
- Yuji Xue<sup>1</sup>
- Vidhur Polam<sup>1</sup>
- Zora Vujovic<sup>1</sup>
- Daniel Dai<sup>1</sup>
- William Ong<sup>1</sup>
- Jasper Ip<sup>1</sup> ([ORCID: 0000-0001-9773-1544](https://orcid.org/0000-0001-9773-1544))
- Amanda Hsieh<sup>1</sup>
- Nour Mimouni<sup>1</sup>
- Alejandra Lozada<sup>1</sup>
- Medhini Sosale<sup>1</sup>
- Alex Ahn<sup>1</sup>
- Minghong Ma<sup>1</sup>
- Long Ding<sup>1</sup> ([ORCID: 0000-0002-1716-3848](https://orcid.org/0000-0002-1716-3848))
- Javier Arsuaga<sup>2</sup>
- Wenqin Luo<sup>1</sup> ([ORCID: 0000-0002-2486-807X](https://orcid.org/0000-0002-2486-807X)) †

### Affiliations

1. Department of Neuroscience University of Pennsylvania Philadelphia United States
2. Graduate Group in Biostatistics University of California, Davis Davis United States
3. Program in Cellular and Molecular Medicine Howard Hughes Medical Institute, Harvard Medical School Boston United States
4. Department of Electrical Engineering and Computer Science Massachusetts Institute of Technology Cambridge United States

† Corresponding author

## Abstract

Mice are the most commonly used model animals for itch research and for development of anti-itch drugs. Most labs manually quantify mouse scratching behavior to assess itch intensity. This process is labor-intensive and limits large-scale genetic or drug screenings. In this study, we developed a new system, Scratch-AID Automatic Itch Detection), which could automatically identify and quantify mouse scratching behavior with high accuracy. Our system included a custom-designed videotaping box to ensure high-quality and replicable mouse behavior recording and a convolutional recurrent neural network (CRNN) trained with frame-labeled mouse scratching behavior videos, induced by nape injection of chloroquine (CQ). The best trained network achieved 97.6% recall and 96.9% precision on previously unseen test videos. Remarkably, Scratch-AID could reliably identify scratching behavior in other major mouse itch models, including the acute cheek model, the histaminergic model, and a chronic itch model. Moreover, our system detected significant differences in scratching behavior between control and mice treated with an anti-itch drug. Taken together, we have established a novel deep learning-based system that is ready to replace manual quantification for mouse scratching behavior in different itch models and for drug screening.
