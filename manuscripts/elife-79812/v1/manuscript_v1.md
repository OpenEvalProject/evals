# Determining growth rates from bright-field images of budding cells through identifying overlaps

## Authors

- Julian MJ Pietsch<sup>1</sup> ([ORCID: 0000-0002-9992-2384](https://orcid.org/0000-0002-9992-2384))
- Alan F Munoz<sup>1</sup>
- Diane-Yayra A Adjavon<sup>1</sup>
- Iseabail Farquhar<sup>1</sup>
- Ivan BN Clark<sup>1</sup>
- Peter S Swain<sup>1</sup> ([ORCID: 0000-0001-7489-8587](https://orcid.org/0000-0001-7489-8587)) †

### Affiliations

1. Centre for Engineering Biology University of Edinburgh Edinburgh United Kingdom

† Corresponding author

## Abstract

Much of biochemical regulation ultimately controls growth rate, particularly in microbes. Although time-lapse microscopy visualises cells, determining their growth rates is challenging, particularly for those that divide asymmetrically, like Saccharomyces cerevisiae, because cells often overlap in images. Here we present the Birth Annotator for Budding Yeast (BABY), an algorithm to determine single-cell growth rates from label-free images. Using a convolutional neural network, BABY resolves overlaps through separating cells by size and assigns buds to mothers by identifying bud necks. BABY uses machine learning to track cells and determine lineages and estimates growth rates as the rates of change of volumes. Using BABY and a microfluidic device, we show that bud growth is likely first sizer- then timer-controlled, that the nuclear concentration of Sfp1, a regulator of ribosome biogenesis, varies before the growth rate does, and that growth rate can be used for real-time control. By estimating single-cell growth rates and so fitness, BABY should generate much biological insight.
