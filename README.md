<h1 align="center">Awesome Pd</h1>

_Awesome List of PureData Externals, Libraries, Compilers, and More_


<h1 align="center">Contents</h1>

- [Externals](#externals)
  - [AI](#ai)
  - [Ambisonics](#ambisonics)
  - [Binaural](#binaural)
  - [Partial Tracking](#partial-tracking)
  - [Reverbs](#reverbs)
  - [Synthesis](#synthesis)
  - [Python](#python)
  - [VST](#vst)
  - [WebServers](#webservers)
- [Compilation Tools for Pure Data Objects](#compilation-tools-for-pure-data-objects)
- [Pd for Web Environments](#pd-for-web-environments)
- [Pd-to-C Converter](#pd-to-c-converter)

---

## Externals

A curated list of PureData externals. For objects/libraries marked with **(✅️)**, you can install them directly from within PureData using Help -> Find Externals.:

### AI

- **[neuralnet](https://github.com/alexdrymonitis/neuralnet)** (✅️): An artificial neural network Pd external written in pure C, without any dependencies.  
- **[nn~](https://github.com/acids-ircam/nn_tilde)** (❌): An external for real-time AI audio processing.  

### Ambisonics

- **[HoaLibrary](https://github.com/CICM/HoaLibrary-PD)** (❌): Implements music spatialization models based on high order ambisonics and sound fields synthesis.
- **[grambilib](https://github.com/rickygraham/grambilib)** (✅️): A simple ambisonics library for Pd, written in C.
- **[abclib](https://github.com/alainbonardi/abclib)** (❌️): An extension of the HOA library from CICM (2012–2015) offering an impressive framework for ambisonics.

### Binaural

- **[earplug~](https://github.com/pd-externals/earplug)** (✅️): Binaural filter based on KEMAR impulse measurement.
- **[SOFAlizer](https://github.com/sofacoustics/SOFAlizer-for-pd)** (✅️): An interactive, low-cost binaural virtual acoustics system for headphones.

### Partial Tracking

- **[smspd](https://github.com/charlesneimog/smspd)** (✅️): Uses spectral modeling and synthesis techniques to achieve SMS analysis, synthesis, and modifications in real-time.
- **[pd-partialtrack](https://github.com/charlesneimog/pd-partialtrack)** (✅️):  A realtime partial-tracking library for PureData implement SMS, Loris, Mq and SndObj partial-tracking.
### Reverbs

- **[convolve~](https://github.com/wbrent/convolve_tilde)** (✅️): Partitioned impulse response (IR) convolution external for Pure Data.

- **[piro](https://github.com/d-i-s/piro)** (✅️): A Pd port of the HISSTools Impulse Response Toolbox.

### Synthesis

- **[pd-percolate](https://github.com/megrimm/pd-percolate)** (✅️):  Offers a variety of synthesis and signal processing techniques.
- **[grainer~](https://github.com/odiliscia/the_grainer_PureData_gh)** (❌): Granular synthesis and ambisonics spatialisation external for Pure Data.

### Python

- **[py](https://github.com/grrrr/py)** (✅️): Provides Python scripting capabilities within Pure Data.
- **[py4pd](https://github.com/charlesneimog/py4pd)** (✅️): Integrates the Python environment into Pure Data.

### VST

- **[vstplugin~](https://git.iem.at/pd/vstplugin)** (✅️): Enables the use of VST plugins in Pure Data on Windows, MacOS, and Linux.

### WebServers

- **[pd-server](https://github.com/charlesneimog/pd-server)** (✅️): HTTP and HTTPS server implementation for Pure Data.
- **[webserver](https://github.com/Lucarda/pd-webserver)** (✅️): A simple web server designed for Pure Data.


### Score Followers

- **[antescofo~](https://forum.ircam.fr/projects/detail/antescofo/)** (❌): Antescofo is a real-time module for Max and PureData. 
- **[o.scofo~](https://github.com/charlesneimog/OScofo)** (❌): A Open Source Score Follower based on the research of Arshia Cont (2010), base for `antescofo~` object.

---

## Compilation Tools for Pure Data Objects

- **[pd-lib-builder](https://github.com/pure-data/pd-lib-builder)**: A helper Makefile for building Pure Data external libraries.
- **[pd.cmake](https://github.com/pure-data/pd.cmake)**: A CMake-based tool to facilitate the compilation of Pure Data externals.

---

## Pd for Web Environments

- **[hvcc](https://github.com/Wasted-Audio/hvcc)**: A Python-based compiler for a dataflow audio programming language.
- **[pd4web](https://github.com/charlesneimog/pd4web)**: Run your Pure Data patches on the web, complete with external support.
- **[Web Pd](https://github.com/sebpiq/WebPd)**: Bring your Pure Data patches to the web.

---

## Pd-to-C Converter

- **[hvcc](https://github.com/Wasted-Audio/hvcc)**: A Python-based compiler that converts dataflow audio programs (Pd patches) to C code.

---

_Contributions, suggestions, and improvements are very welcome. Feel free to fork the repository and submit your changes!_


