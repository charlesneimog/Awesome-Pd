# Awesome Pd 

Awesome List of PureData Externals/Libraries/Compilers and another things. 

> [!IMPORTANT]  
> I am starting this list now, if you know some cool (or not cool) object, please make a PR or tell me in [issues](https://github.com/charlesneimog/Awesome-Pd-Externals/issues/new).

# Contents

- [Externals](#externals) 
  - [AI](#ai)
  - [Ambisonics](#ambisonics)
  - [Binaural](#binaural)
  - [Partial Tracking](#partialtracking)
  - [Reverbs](#reverbs)
  - [Synthesis](#synthesis)
  - [WebServers](#webservers)
- [Compilation Tools for Pure Data Objects](#compilation-tools-for-pure-data-objects)
- [Pd for Web Enviroments](#pd-for-web-enviroments)

## Externals

List of PureData externals. For objects/libraries marked with ✅️ in the `Deken` column, you can download them by opening PureData:
  1. Open PureData;
  2. Go to Help;
  3. Find Externals;
  4. Search for the object name;
  5. Click in `Install`.

### AI

| Name  | Deken | Description |
|:-------:|:-------:|:-------------:|
| [neuralnet](https://github.com/alexdrymonitis/neuralnet) |✅️| An Artificial Neural Network framework for Pure Data. |
| [nn~](https://github.com/acids-ircam/nn_tilde) |❌| Pd External for real-time ai audio processing. |

-----

### Ambisonics

| Name  | Deken | Description |
|:-------:|:-------:|:-------------:|
| [HoaLibrary](https://github.com/CICM/HoaLibrary-PD) |❌| Music spatialization models based on high order ambisonics and sound fields synthesis. |
| [grambilib](https://github.com/rickygraham/grambilib) |✅️| A simple ambisonics library for Pd, written in C. |
| [abclib](https://github.com/alainbonardi/abclib) |❌️| It comes as a prolongation of the HOA library developed by the CICM. |

-----

### Binaural

| Name  | Deken | Description |
|:-------:|:-------:|:-------------:|
| [earplug~](https://github.com/pd-externals/earplug) |✅️| Binaural Filter Based on KEMAR impulse measurement. |
| [SOFAlizer](https://github.com/sofacoustics/SOFAlizer-for-pd) |✅️| An interactive, low-cost, binaural, virtual acoustics embedded system through headphones. |

-----

### PartialTracking

| Name  | Deken | Description |
|:-------:|:-------:|:-------------:|
| [smspd](https://github.com/charlesneimog/smspd) |✅️|Spectral Modeling and Synthesis Techniques to accomplish SMS analysis, synthesis, and modifications in real-time.|

### Reverbs

| Name  | Deken | Description |
|:-------:|:-------:|:-------------:|
| [convolve~](https://github.com/wbrent/convolve_tilde) |✅️|Partitioned impulse response (IR) convolution external for Pure Data.|
| [piro](https://github.com/d-i-s/piro) |✅️|Pd-port of the HISSTools Impulse Response Toolbox.|

-----

### Synthesis
| Name  | Deken | Description |
|:-------:|:-------:|:-------------:|
| [pd-percolate](https://github.com/megrimm/pd-percolate) |✅️|Variety of synthesis and signal processing.|
| [grainer~](https://github.com/odiliscia/the_grainer_PureData_gh) |❌|Granular synthesis and Ambisonics spatialisation external for Pure Data|

-----

### Python

| Name  | Deken | Description |
|:-------:|:-------:|:-------------:|
| [py](https://github.com/grrrr/py) |✅️|Python scripting objects.|
| [py4pd](https://github.com/charlesneimog/py4pd) |✅️|Allows the use of complete Python enviroment within PureData.|

-----

### WebServers

| Name  | Deken | Description |
|:-------:|:-------:|:-------------:|
| [pd-server](https://github.com/charlesneimog/pd-server) |✅️|HTTP and HTTPS server for PureData.|
| [webserver](https://github.com/Lucarda/pd-webserver) |✅️| A web server for Pd.|

-----

## Compilation Tools for Pure Data Objects

| Name  | Description |
|:-------:|:-------:|
| [pd-lib-builder](https://github.com/pure-data/pd-lib-builder) | Helper Makefile for Pure Data external libraries. |
| [pd.build](https://github.com/pierreguillot/pd.build) | Helper Cmake for Pure Data external libraries.|

-----

## Pd for Web Enviroments

| Name  | Description |
|:-------:|:-------:|
| [hvcc](https://github.com/Wasted-Audio/hvcc) | hvcc is a python-based dataflow audio programming language compiler. |
| [pd4web](https://github.com/charlesneimog/pd4web) |Run your Pure Data patches on the web with externals.|
| [Web Pd](https://github.com/sebpiq/WebPd) | Run your Pure Data patches on the web.|
