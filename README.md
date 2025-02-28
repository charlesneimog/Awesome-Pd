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

### JavaScript

### Lua

- **[pd-lua]()** (✅️): 
- **[openFrameworks]()** (✅️): 

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

*  **[abl_link~](https://github.com/libpd/abl_link)**: Ableton Link integration for Pure Data on desktop and Android. 

*  **[absattr](https://github.com/grrrr/absattr)**:  Patcher attributes for Pure data 

*  aconnect: Alsa Connect (just for linux).

*  acre: ACRE Waveguide Library: Puredata abstractions library providing an intuitive simple set of objects to patch physical models of real or fantasy sounding objects primarily using waveguides. 

*  acre-amb: acre-amb is a collection of high level Pd abstraction, to implement Ambisonics functionality for Ambisonics mixer and processors, especially compositions, introducing multichannel patching 

*  adaptive: LMS: least mean square adaptation algorithm (Filter);

*  algo~: A suite of Pure Data abstractions for musical live coding (Live-Coding);

*  aoo: Audio over OSC based audio streaming

*  apple: Apple sensors (just for Apples machines);

*  array-abs: Array Abstraction Library for Pure Data (version >= 0.45). Arrays manipulations.

*  art_net: Simple Artnet protocol implementation with Pure Data.

*  artnetlib: Pure-Data objects to communicate with Art-Net protocol. 

*  asdf: Play Audio Scene Description Format (ASDF) files. Check this [link](https://AudioSceneDescriptionFormat.readthedocs.io/)

*  audiolab: Pure Data abstractions for electroacoustic composition & live electronics 

*  automatonism: Automatonism is a modular synthesiser that runs in the open source programming language Pure Data. It features a large library of 81 modules (version 2.1). Follow these simple steps to get started:


*  AutoPreset:  PureData parameter states management 

*  bandlimited: A computational expensive pure data external that generates signal (saw, triangle, square, and variable duty cycle pulse wave) band limited to the sampling rate. 

*  bassemu

*  bassemu~
*  bf-pd
*  binfile
*  boids
*  bsaylor: bsaylor is a library of Pure Data objects by Benjamin Saylor.
*  bytestruct
*  ceammc
*  chair
*  chaos
*  cicmtools
*  clk
*  command
*  completion-plugin
*  comport
*  constantq~
*  context
*  convolve~
*  Cream
*  creb
*  cxc
*  cyclone
*  DEAPd
*  deken-plugin
*  dnd-plugin
*  doublechord-plugin
*  DRFX
*  dw_lib
*  earplug~
*  easyflow
*  echocurve~
*  ekext
*  else
*  ext13
*  extra
*  ezaoo
*  faustgen~: The FAUST compiler embedded in a Pd external 
*  fd_lib
*  fftease
*  filemtime
*  flatgui: A sampler drum machine made in Pure Data vanilla. 
*  flite:  Speech synthesis for Pd 
*  Fraise: FRAmework for Interfacing Software and Electronics 
*  Fraise-toolchain

*  freeverb~: reverb external for Pure Data based on Freeverb, the free, studio-quality reverb 

*  Gem
*  gem2pdp
*  ggee
*  gigaverb~
*  gpmotion
*  guis
*  hcs
*  hexloader
*  hid
*  hid-0.7-1
*  hidin
*  hidio
*  hidraw
*  hotfix732-deadkeys-plugin
*  hrtf~

*  iem16
*  iem_adaptfilt
*  iem_ambi
*  iem_bin_ambi
*  iem_delay
*  iem_dp
*  iem_roomsim
*  iem_spec2
*  iem_tab
*  iem_vanilla
*  iemgui
*  iemguts
*  iemlib
*  iemmatrix
*  iemnet
*  iempluginOSC
*  iemxmlrpc

*  jackpatch
*  Jamoma
*  jasch_lib
*  jit_expr
*  jl
*  jmmmp
*  jpcex
*  jpcvisu
*  jsobj
*  kiosk-plugin
*  la-kitchen
*  leapmotion
*  libdir
*  list-abs
*  log
*  lolPd:  Tiny wrist-saving DSL for Pure Data. 

*  lyonpotpourri: LyonPotpourri is a collection of externals developed for the creation and performance of computer music. The externals were originally developed for Max/MSP, and then extended into hybrid code that could compile for both Max/MSP and Pd. As of version 3.0, the code bases of Max/MSP and Pd have diverged to such an extent that it was deemed advisable to split the LyonPotpourri code into separate Pd and Max/MSP versions. 


*  mapping
*  markex: Pd library of misc objects from Mark Danks.
*  martha~: martha~ is a companion to the \[sigmund~\] analysis object. It's designed to accept output from \[sigmund~\]'s sinusoidal tracking function, "tracks". In addition to providing an internal oscillator bank and doing all the data/voice bookkeeping, it has some useful features for independent glissing and amplitude pulsing of individual partials. \[martha~\] is also capable of managing the attack and release times of partials and forcing inharmonic spectra to harmonic arrangements. Combined, these features can create a variety of interesting effects.

*  maxlib: Music analysis extensions library by Olaf Matthes 

*  mc
*  mediasettings: get/set audio and MIDI settings within Pd

*  midifile:  Read and write MIDI files (.mid) with Pd 

*  missive~: missive~ is a vector synth object that uses a wavetable index to crossfade between neighboring wavetables in a set.

*  mjlib: Mjlib is a small Pure Data library created by Mark Williamson. 

*  mkmr: A compilation of abstractions and instruments compatible with Pure Data vanilla. 

*  ml.lib: ml-lib is a library of machine learning externals for Max and Pure Data. ml-lib is primarily based on the Gesture Recognition Toolkit by Nick Gillian ml-lib is designed to work on a variety of platforms including OS X, Windows, Linux, on Intel and ARM architectures.

*  moocow: Externals for Pure Data written by Bryan Jurish.

*  moonlib:  Some useful Pd externals. 

*  motex: This is a collection of Pure Data abstractions. It includes sequencers, GUIs, general utilities, and a few effects and synths. I’m still in the process of writing and updating them to fix bugs and add functionality

*  mp3cast~: stream audio to an Icecast2, Icecast, or Shoutcast server.

*  mrpeach: Pure Data externals written by Martin Peach.

*  muug: A non-linear digital implementation of the moog ladder filter for Pure Data. Based on Antti Houvilainen.

*  ndi:  Newtek NDI external for Pure Data/Gem 

*  net
*  nGui
*  nicinfo
*  nilwind
*  notesLib
*  nsend
*  nusmuk-audio
*  nusmuk-utils
*  ofelia
*  orchidea
*  osc
*  oscx
*  ossia
*  pan
*  patch2svg-plugin
*  patcherize-plugin: Selections to SubPatch.
*  pd-aubio: Various externals for PureData using the aubio library
*  pd-ji: 
*  pd-push-and-hold
*  pd-score: 
*  pd-server
*  pd-wavelet
*  pd-zmq
*  Pd_Spectral_Toolkit
*  PDContainer
*  pdcontainer
*  pddp
*  pde

*  pdjs
*  pdlua

*  pdmus
*  pdogg: pdogg~ is a collection of ogg/vorbis externals for pd (by Miller Puckette).

*  pdp
*  pdpii2c
*  pdpp
*  pduino
*  pii2c
*  piloslib
*  piro
*  pispi
*  pix_artoolkit
*  pix_drum
*  pix_fiducialtrack
*  pix_mano
*  pix_opencv
*  planifolia: Pd Vanilla abstractions to do many different things.
*  plugin~: LADSPA plug-in hosting for Pd.
*  pmpd: Physical Modelling for Pure Data.
*  pof
*  pofbeam
*  pool
*  psycho:  Pd library with some psychoacoustic tools.
*  pulqui
*  punish
*  puremapping
*  purepd
*  purest_json
*  queryresponse
*  quilt
*  RabbitControl
*  readdir
*  rfpg
*  rtc
*  rtcmix~
*  saturator: The saturator~ external performs a nonlinear compression on the input signal based on threshold (rms), attack/release (ms), push/pull, autogain, and polynomial order (N = [2, 736]) settings.

*  scroll-test-plugin
*  scrollpage-plugin
*  search-plugin
*  senselmorph
*  sfruit
*  shadylib
*  shmem
*  shotnoise
*  sigpack
*  simplex
*  simplex~
*  slip
*  smlib: Signal processing for Mapping library for Pure Data by Johannes Taelman 
*  soundhack

*  soundtouch~: [soundtouch~] is a Pure Data implementation of Olli Parviainen's SoundTouch library, ported by Katja Vetter. The class is implemented as a real-time pitch shifter, converting an audio stream to different pitch.

*  spect_scaled
*  spring22
*  ssr
*  stash
*  streamStretch~
*  swe~
*  syslog
*  tabreceive_mult~
*  tabwrite_dir~
*  tclpd
*  tclprompt-plugin
*  tdh.lib
*  tdh.satk
*  testtools
*  timbreIDLib
*  timestretch
*  timeStretch~
*  tof
*  tracker
*  triggerize-plugin
*  tune~
*  ultraleap
*  unauthorized
*  unicode
*  upp
*  vabs
*  vanilla
*  vasp
*  vbap
*  vinylcontrol~
*  websocketserver
*  windowing
*  ws
*  xsample
*  XXX-deken-test
*  zconf
*  zexy

