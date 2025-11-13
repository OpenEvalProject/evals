# A spike sorting toolbox for up to thousands of electrodes validated with ground truth recordings in vitro and in vivo

## Authors

- Pierre Yger<sup>1</sup>
- Giulia LB Spampinato<sup>1</sup>
- Elric Esposito<sup>1</sup>
- Baptiste Lefebvre<sup>1</sup>
- Stéphane Deny<sup>1</sup>
- Christophe Gardella<sup>1</sup> ([ORCID: 0000-0003-3204-9012](https://orcid.org/0000-0003-3204-9012))
- Marcel Stimberg<sup>1</sup> ([ORCID: 0000-0002-2648-4790](https://orcid.org/0000-0002-2648-4790))
- Florian Jetter<sup>2</sup>
- Guenther Zeck<sup>2</sup>
- Serge Picaud<sup>1</sup>
- Jens Duebel<sup>1</sup>
- Olivier Marre<sup>1</sup> ([ORCID: 0000-0002-0090-6190](https://orcid.org/0000-0002-0090-6190)) †

### Affiliations

1. Physiology and Information Processing Institut de la Vision - INSERM URMS 968 Paris France
2. Neurophysics group The Natural and Medical Sciences Institute Reutlingen Germany

† Corresponding author

## Abstract

In recent years, multielectrode arrays and large silicon probes have been developed to record simultaneously between hundreds and thousands of electrodes packed with a high density. However, they require novel methods to extract the spiking activity of large ensembles of neurons. Here we developed a new toolbox to sort spikes from these large-scale extracellular data. To validate our method, we performed simultaneous extracellular and loose patch recordings in rodents to obtain 'ground truth' data, where the solution to this sorting problem is known for one cell. The performance of our algorithm was always close to the best expected performance, over a broad range of signal to noise ratios, in vitro and in vivo. The algorithm is entirely parallelized and has been successfully tested on recordings with up to 4225 electrodes. Our toolbox thus offers a generic solution to sort accurately spikes for up to thousands of electrodes.
