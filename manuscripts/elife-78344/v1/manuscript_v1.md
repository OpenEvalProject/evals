# A hardware system for real time decoding of in vivo calcium imaging data

## Authors

- Zhe Chen<sup>1</sup>
- Garrett J Blair<sup>2</sup> ([ORCID: 0000-0003-2724-8914](https://orcid.org/0000-0003-2724-8914))
- Changliang Guo<sup>3</sup>
- Jim Zhou<sup>1</sup>
- Juan-Luis Romero-Sosa<sup>2</sup>
- Alicia Izquierdo<sup>2</sup> ([ORCID: 0000-0001-9897-2091](https://orcid.org/0000-0001-9897-2091))
- Peyman Golshani<sup>3</sup>
- Jason Cong<sup>1</sup>
- Daniel Aharoni<sup>4</sup> ([ORCID: 0000-0003-4931-8514](https://orcid.org/0000-0003-4931-8514))
- Hugh T Blair<sup>2</sup> ([ORCID: 0000-0001-8256-5109](https://orcid.org/0000-0001-8256-5109)) †

### Affiliations

1. Department of Electrical and Computer Engineering University of California, Los Angeles Los Angeles United States
2. Department of Psychology University of California, Los Angeles Los Angeles United States
3. David Geffen School of Medicine University of California, Los Angeles Los Angeles United States
4. Department of Neurology University of California, Los Angeles Los Angeles United States

† Corresponding author

## Abstract

Epifluorescence miniature microscopes ('miniscopes') are widely used for in vivo calcium imaging of neural population activity. Imaging data is typically collected during a behavioral task and stored for later offline analysis, but emerging techniques for online imaging can support novel closed-loop experiments in which neural population activity is decoded in real time to trigger neurostimulation or sensory feedback. To achieve short feedback latencies, online imaging systems must be optimally designed to maximize computational speed and efficiency while minimizing errors in population decoding. Here we introduce DeCalciOn , an open-source device for real-time imaging and population decoding of in vivo calcium signals that is hardware compatible with all miniscopes that use the UCLA Data Acquisition (DAQ) interface. DeCalciOn performs online motion stabilization, neural enhancement, calcium trace extraction, and decoding of up to 1024 traces per frame at latencies of <50 ms after fluorescence photons arrive at the miniscope image sensor. We show that DeCalciOn can accurately decode the position of rats (n=12) running on a linear track from calcium fluorescence in the hippocampal CA1 layer, and can categorically classify behaviors performed by rats (n=2) during an instrumental task from calcium fluorescence in orbitofrontal cortex (OFC). DeCalciOn achieves high decoding accuracy at short latencies using innovations such as field-programmable gate array (FPGA) hardware for real time image processing and contour-free methods to efficiently extract calcium traces from sensor images. In summary, our system offers an affordable plug-and-play solution for real-time calcium imaging experiments in behaving animals.
