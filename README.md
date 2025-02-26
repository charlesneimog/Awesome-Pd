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

*  abl_link~
*  absattr
*  aconnect
*  acre
*  acre-amb
*  acre-wg
*  adaptive
*  algo~
*  aoo
*  apple
*  array-abs
*  arraysize
*  art_net
*  artnetlib
*  asdf
*  audiolab
*  automatonism
*  AutoPreset
*  bandlimited
*  bassemu
*  bassemu~
*  bf-pd
*  binfile
*  boids
*  bsaylor
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
*  faustgen~
*  fd_lib
*  fftease
*  filemtime
*  flatgui
*  flite
*  Fraise
*  Fraise-toolchain
*  freeverb~
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
*  lolPd
*  lyonpotpourri
*  mapping
*  markex
*  martha~
*  maxlib
*  mc
*  mediasettings
*  midifile
*  missive~
*  mjlib
*  mkmr
*  ml.lib
*  moocow
*  moonlib
*  motex
*  mp3cast~
*  mrpeach
*  muug
*  ndi
*  net
*  neuralnet
*  nGui
*  nicinfo
*  nilwind
*  nn~
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
*  patcherize-plugin
*  pd-ji
*  pd-push-and-hold
*  pd-score
*  pd-server
*  pd-wavelet
*  pd-zmq
*  pd4web
*  Pd_Spectral_Toolkit
*  PDContainer
*  pdcontainer
*  pddp
*  pde
*  pdjs
*  pdlua
*  pdmus
*  pdogg
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
*  planifolia
*  plugin~
*  pmpd
*  pof
*  pofbeam
*  pool
*  psycho
*  pulqui
*  punish
*  puremapping
*  purepd
*  purest_json
*  py
*  py4pd
*  queryresponse
*  quilt
*  RabbitControl
*  readdir
*  rfpg
*  rtc
*  rtcmix~
*  saturator
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
*  smlib
*  smspd
*  SOFAlizer~
*  soundhack
*  soundtouch~
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
*  vstplugin~
*  webserver
*  websocketserver
*  windowing
*  ws
*  xsample
*  XXX-deken-test
*  zconf
*  zexy

