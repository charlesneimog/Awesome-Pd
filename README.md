<h1 align="center">Awesome Pd</h1> 


Awesome List of PureData Externals/Libraries/Compilers and another things. 

> [!IMPORTANT]  
> I am starting this list now, if you know some cool (or not cool) object, please make a PR or tell me in [issues](https://github.com/charlesneimog/Awesome-Pd-Externals/issues/new).

# Contents
<h1 align="center">Contents</h1> 

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

<table align="center" width="100%">
  <tr>
    <th>Name</th>
    <th>Deken</th>
    <th>Description</th>
  </tr>
  <tr>
    <td><a href="https://github.com/alexdrymonitis/neuralnet">neuralnet</a></td>
    <td>✅️</td>
    <td>An Artificial Neural Network framework for Pure Data.</td>
  </tr>
  <tr>
    <td><a href="https://github.com/acids-ircam/nn_tilde">nn~</a></td>
    <td>❌</td>
    <td>Pd External for real-time ai audio processing.</td>
  </tr>
</table>
 
### Ambisonics

<table align="center">
  <tr>
    <th>Name</th>
    <th>Deken</th>
    <th>Description</th>
  </tr>
  <tr>
    <td><a href="https://github.com/CICM/HoaLibrary-PD">HoaLibrary</a></td>
    <td>❌</td>
    <td>Music spatialization models based on high order ambisonics and sound fields synthesis.</td>
  </tr>
  <tr>
    <td><a href="https://github.com/rickygraham/grambilib">grambilib</a></td>
    <td>✅️</td>
    <td>A simple ambisonics library for Pd, written in C.</td>
  </tr>
  <tr>
    <td><a href="https://github.com/alainbonardi/abclib">abclib</a></td>
    <td>❌️</td>
    <td>It comes as a prolongation of the HOA library developed by the CICM.</td>
  </tr>
</table>

### Binaural

<table align="center">
  <tr>
    <th>Name</th>
    <th>Deken</th>
    <th>Description</th>
  </tr>
  <tr>
    <td><a href="https://github.com/pd-externals/earplug">earplug~</a></td>
    <td>✅️</td>
    <td>Binaural Filter Based on KEMAR impulse measurement.</td>
  </tr>
  <tr>
    <td><a href="https://github.com/sofacoustics/SOFAlizer-for-pd">SOFAlizer</a></td>
    <td>✅️</td>
    <td>An interactive, low-cost, binaural, virtual acoustics embedded system through headphones.</td>
  </tr>
</table>

### PartialTracking

<table align="center">
  <tr>
    <th>Name</th>
    <th>Deken</th>
    <th>Description</th>
  </tr>
  <tr>
    <td><a href="https://github.com/charlesneimog/smspd">smspd</a></td>
    <td>✅️</td>
    <td>Spectral Modeling and Synthesis Techniques to accomplish SMS analysis, synthesis, and modifications in real-time.</td>
  </tr>
</table>

-----

### Reverbs

<table align="center">
  <tr>
    <th>Name</th>
    <th>Deken</th>
    <th>Description</th>
  </tr>
  <tr>
    <td><a href="https://github.com/wbrent/convolve_tilde">convolve~</a></td>
    <td>✅️</td>
    <td>Partitioned impulse response (IR) convolution external for Pure Data.</td>
  </tr>
  <tr>
    <td><a href="https://github.com/d-i-s/piro">piro</a></td>
    <td>✅️</td>
    <td>Pd-port of the HISSTools Impulse Response Toolbox.</td>
  </tr>
</table>

### Synthesis<

<table align="center">
  <tr>
    <th>Name</th>
    <th>Deken</th>
    <th>Description</th>
  </tr>
  <tr>
    <td><a href="https://github.com/megrimm/pd-percolate">pd-percolate</a></td>
    <td>✅️</td>
    <td>Variety of synthesis and signal processing.</td>
  </tr>
  <tr>
    <td><a href="https://github.com/odiliscia/the_grainer_PureData_gh">grainer~</a></td>
    <td>❌</td>
    <td>Granular synthesis and Ambisonics spatialisation external for Pure Data.</td>
  </tr>
</table>

### Python 

<table align="center">
  <tr>
    <th>Name</th>
    <th>Deken</th>
    <th>Description</th>
  </tr>
  <tr>
    <td><a href="https://github.com/grrrr/py">py</a></td>
    <td>✅️</td>
    <td>Python scripting objects.</td>
  </tr>
  <tr>
    <td><a href="https://github.com/charlesneimog/py4pd">py4pd</a></td>
    <td>✅️</td>
    <td>Allows the use of complete Python environment within PureData.</td>
  </tr>
</table>

### WebServers

<table align="center">
  <tr>
    <th>Name</th>
    <th>Deken</th>
    <th>Description</th>
  </tr>
  <tr>
    <td><a href="https://github.com/charlesneimog/pd-server">pd-server</a></td>
    <td>✅️</td>
    <td>HTTP and HTTPS server for PureData.</td>
  </tr>
  <tr>
    <td><a href="https://github.com/Lucarda/pd-webserver">webserver</a></td>
    <td>✅️</td>
    <td>A web server for Pd.</td>
  </tr>
</table>

## Compilation Tools for Pure Data Objects

<table align="center">
  <tr>
    <th>Name</th>
    <th>Description</th>
  </tr>
  <tr>
    <td><a href="https://github.com/pure-data/pd-lib-builder">pd-lib-builder</a></td>
    <td>Helper Makefile for Pure Data external libraries.</td>
  </tr>
  <tr>
    <td><a href="https://github.com/pierreguillot/pd.build">pd.build</a></td>
    <td>Helper CMake for Pure Data external libraries.</td>
  </tr>
</table>


## Pd for Web Enviroments

<table align="center">
  <tr>
    <th>Name</th>
    <th>Description</th>
  </tr>
  <tr>
    <td><a href="https://github.com/Wasted-Audio/hvcc">hvcc</a></td>
    <td>hvcc is a python-based dataflow audio programming language compiler.</td>
  </tr>
  <tr>
    <td><a href="https://github.com/charlesneimog/pd4web">pd4web</a></td>
    <td>Run your Pure Data patches on the web with externals.</td>
  </tr>
  <tr>
    <td><a href="https://github.com/sebpiq/WebPd">Web Pd</a></td>
    <td>Run your Pure Data patches on the web.</td>
  </tr>
</table>
