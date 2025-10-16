# A scalable and modular automated pipeline for stitching of large electron microscopy datasets

## Authors

- Gayathri Mahalingam<sup>1</sup> †
- Russel Torres<sup>1</sup> ([ORCID: 0000-0002-2876-4382](https://orcid.org/0000-0002-2876-4382))
- Daniel Kapner<sup>1</sup>
- Eric T Trautman<sup>2</sup> ([ORCID: 0000-0001-8588-0569](https://orcid.org/0000-0001-8588-0569))
- Tim Fliss<sup>1</sup>
- Shamishtaa Seshamani<sup>1</sup>
- Eric Perlman<sup>3</sup> ([ORCID: 0000-0001-5542-1302](https://orcid.org/0000-0001-5542-1302))
- Rob Young<sup>1</sup>
- Samuel Kinn<sup>1</sup>
- JoAnn Buchanan<sup>1</sup>
- Marc M Takeno<sup>1</sup> ([ORCID: 0000-0002-8384-7500](https://orcid.org/0000-0002-8384-7500))
- Wenjing Yin<sup>1</sup>
- Daniel J Bumbarger<sup>1</sup>
- Ryder P Gwinn<sup>4</sup>
- Julie Nyhus<sup>1</sup>
- Ed Lein<sup>1</sup>
- Steven J Smith<sup>1</sup> ([ORCID: 0000-0002-2290-8701](https://orcid.org/0000-0002-2290-8701))
- R Clay Reid<sup>1</sup> ([ORCID: 0000-0002-8697-6797](https://orcid.org/0000-0002-8697-6797))
- Khaled A Khairy<sup>5</sup> ([ORCID: 0000-0002-9274-5928](https://orcid.org/0000-0002-9274-5928))
- Stephan Saalfeld<sup>6</sup> ([ORCID: 0000-0002-4106-1761](https://orcid.org/0000-0002-4106-1761))
- Forrest Collman<sup>1</sup> ([ORCID: 0000-0002-0280-7022](https://orcid.org/0000-0002-0280-7022))
- Nuno Macarico da Costa<sup>1</sup> ([ORCID: 0000-0003-2001-4568](https://orcid.org/0000-0003-2001-4568)) †

### Affiliations

1. Allen Institute for Brain Science Seattle United States
2. Scientific Computing Janelia Research Campus Ashburn United States
3. Yikes LLC Baltimore United States
4. Epilepsy Surgery and Functional Neurosurgery Swedish Neuroscience Institute Seattle United States
5. St. Jude Children's Research Hospital Memphis United States
6. Saalfeld Lab Janelia Research Campus Ashburn United States

† Corresponding author

## Abstract

Serial-section electronmicroscopy (ssEM) is themethod of choice for studyingmacroscopic biological samples at extremely high resolution in three dimensions. In the nervous system, nanometer-scale images are necessary to reconstruct dense neural wiring diagrams in the brain, so called connectomes. In order to use this data, consisting of up to 10 8 individual EM images, it must be assembled into a volume, requiring seamless 2D stitching from each physical section followed by 3D alignment of the stitched sections. The high throughput of ssEM necessitates 2D stitching to be done at the pace of imaging, which currently produces tens of terabytes per day. To achieve this, we present a modular volume assembly software pipeline ASAP (Assembly Stitching and Alignment Pipeline) that is scalable to datasets containing petabytes of data and parallelized to work in a distributed computational environment. The pipeline is built on top of the Render (27) services used in the volume assembly of the brain of adult Drosophilamelanogaster (30). It achieves high throughput by operating on themeta-data and transformations of each image stored in a database, thus eliminating the need to render intermediate output. ASAP ismodular, allowing for easy incorporation of new algorithms without significant changes in the workflow. The entire software pipeline includes a complete set of tools for stitching, automated quality control, 3D section alignment, and final rendering of the assembled volume to disk. ASAP has been deployed for continuous stitching of several large-scale datasets of the mouse visual cortex and human brain samples including one cubic millimeter of mouse visual cortex (28; 8) at speeds that exceed imaging. The pipeline also has multi-channel processing capabilities and can be applied to fluorescence and multi-modal datasets like array tomography.
