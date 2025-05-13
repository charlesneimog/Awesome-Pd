# abclib

The abclib library also provides utility objects for mixed music, including chowning-like panners, matrices, envelopes, an attack and release detector, and various synthesizers (additive, subtractive, sound coat, sound grain, Risset's bell).

Teaching mixed music at Paris 8 University influenced many implementation choices, considering practical requirements for composers, allowing them to test their patches in multichannel academic studios or at home in simple stereo setups.

CICM (Centre de recherches Informatique et Création Musicale) - University Paris 8

The abclib library represents 20 years of research, teaching, and creation in mixed music using the Faust language. It extends the HOA library developed by CICM between 2012 and 2015, which provided a robust framework for ambisonics: [HOA Library](http://hoalibrary.mshparisnord.fr).

abclib builds on HOA, offering a wide range of processes written in Faust and implemented at various ambisonic orders (from 1 to 7, which means from 3 to 15 parallel instances). It also emphasizes multi-channel sound processing with dimensions ranging from 1 to 16 parallel instances. The use of Faust ensures software durability and interoperability between Mac and Windows systems, as well as Max and PureData software. Faust files are available on a [GitHub repository](https://github.com/alainbonardi/abclib/).

The Faust processes are compiled into Max or PureData objects. Help patches are provided, along with overview patches or graphic abstractions based on jitter (in Max) or gem libraries (in PureData). In ambisonics, 2D objects are available, including general objects (encoders, decoders, optimizers, scopes), geometry objects (maps, mirrors, rotates, specific trajectory generators), and a set of spatial sound processes (decorrelators, delays, granulators, ring modulators) in both 'syn' and 'fx' modes. The names of the ambisonic objects in 2D use '2d' as a prefix: for instance, `abc_2d_decoder3~` is an ambisonic decoder in 2D at order 3. Multi-channel sound process objects do not use the '2d' prefix: for instance, `abc_delays16` implements a set of 16 parallel delay lines. Multi-channel sound processors include flangers, parallel and sequential delays, frequency shifters, harmonizers, granulators, and reverberations.


### `abc_2d_decoder1~`  

The `abc_2d_decoder1~` object (and its variants) decode ambisonic spatial components to loudspeaker sets. These decoders were developed using the Faust language and have fixed configurations based on ambisonic order:  

- **Order 1** → 4 loudspeakers  
- **Order 2** → 6 loudspeakers  
- **Order 3** → 8 loudspeakers  
- **Order 7** → 16 loudspeakers  

Additional objects allow decoding for any number of loudspeakers between **3 and 16** at any order. Examples:  
- `abc_2d_decoder1_8~` → Order 1 with 8 loudspeakers  
- `abc_2d_decoder3_11~` → Order 3 with 11 loudspeakers  
- `abc_2d_decoder1_4~` → Equivalent to `abc_2d_decoder1~`  

<h4> Parameters: </h4>
- **angularoffset** → Angular shift of the loudspeakers (in degrees)  
- **directangles** → 1 for anticlockwise (as in ambisonic norm), 0 for clockwise  
- **a_0, a_1, ..., a_n** → Loudspeaker angles in degrees, allowing for irregular setups  
- **stereo** → 1 for stereo decoding, 0 for ambisonic decoding  

A simple representation of the sound field can be visualized using `cyclone/scope~`.  

---

### `abc_2d_encoder1~`  

The `abc_2d_encoder1~` object (and its variants) generate sound sources either as rotating at a set speed or as static at a defined angle on the ambisonic circle.  

<h4> Parameters: </h4>

- **angle** → Default static angle (in degrees) when speed is zero  
- **returntime** → Transition time (in ms) between the fixed angle and the dynamic position when speed > 0  


### `abc_2d_map1~`  

The `abc_2d_map1_1~` to `abc_2d_map7_8~` objects receive three input signals:  
1. The source to be spatialized  
2. The radius (distance of the source from the center of the scene)  
3. The angle of the source's position (in radians)  

These objects handle multiple signal mappings:  
- `abc_2d_map3_4~` → Manages 4 sources at ambisonic order 3  
- `abc_2d_mapN_1~` is equivalent to `abc_2d_mapN~` when there is only one source (e.g., `abc_2d_map3_1~` = `abc_2d_map3~`)  


### `abc_2d_mirror1~`  

The `abc_2d_mirror1~`, `abc_2d_mirror2~`, etc., objects apply left/right symmetry to ambisonic spatial components by inverting certain components based on a **factor** parameter:  
- **1** → Original sound field  
- **0** → Original and mirrored sound fields combined  
- **-1** → Only the mirrored sound field  

Here’s the cleaned-up and structured version of the documentation:

### `abc_2d_multiencoder1~`  

The `abc_2d_multiencoderN_S~` objects combine multiple encoders within a single unit.  
- **N** → Ambisonic order (1 to 7)  
- **S** → Number of sources (up to 8)  

For example, at ambisonic **order 3**, `abc_2d_multiencoder3_4~` encodes **4 monophonic sources**.  

<h4> Parameters </h4>:  
- **s00, s01, ...** → Source speeds (turns per second)  
- **a00, a01, ...** → Fixed angles (degrees) when speed = 0  
- **returntime (it)** → Transition time (ms) between static and dynamic positions  

---

### `abc_2d_optim1~`  

The `abc_2d_optim1~`, `abc_2d_optim2~`, etc., objects optimize the sound field using **three optimization levels** based on the `optimtype` parameter:  
- **1 = maxRe** → Best for audiences **confined to the center** of the circle  
- **2 = inPhase** → Best when the audience **covers the entire circle**  

These optimizations improve the listening experience when the audience is **not centered** in the ambisonic space.  

### `abc_2d_rotate1~`  

The `abc_2d_rotate1~`, `abc_2d_rotate2~`, etc., objects enable **rotation of the entire ambisonic sound field**:  
- **Continuous rotation** → Controlled by `speed` (tours per second)  
- **Fixed rotation** → Controlled by `angle` (degrees), when `speed = 0`  
- **returntime** → Transition time (ms) between fixed and continuous rotation  

Unlike encoding, which rotates **individual sources**, `abc_2d_rotateN~` rotates the **entire sound field**.  
Here's the cleaned-up and structured version of the documentation:

---

### `abc_2d_scope1~`  

The `abc_2d_scope1~`, `abc_2d_scope2~`, etc., objects visualize the ambisonic sound field using `cyclone/scope~`.  

#### Outputs:  
1. **X signal**  
2. **Y signal**  
3. **Sign of the spatial function** (positive → red, negative → blue)  

---

### `abc_2d_spatialtrajectories~`  

These objects generate **2D movement trajectories** in Cartesian coordinates:  
- `abc_2d_squaretrajectory~` → Square trajectory  
- `abc_2d_ztrajectory~` → Z-shaped trajectory  
- `abc_2d_squareandztrajectory~` → Interpolation between square and Z trajectories  
- `abc_2d_randomtrajectory~` → Random trajectory  

#### Common Parameters:  
- **freq** → Frequency of the trajectory (cycles per second)  
- **size** → Size of the trajectory  

**Additional Parameter for `abc_2d_squareandztrajectory~`**:  
- **crossfade** → Blends between square and Z trajectories  

#### Circular Trajectories:  
- `abc_2d_polarvariablecircle~` generates a circular trajectory (radius = 1) in **polar coordinates**.  
  - **ampRho, freqRho** → Control sinusoidal variation of the radius  
  - **ampTheta, freqTheta** → Control sinusoidal variation of the angle  
  - **rotSpeed** → Rotation speed (turns per second)  

---

### `abc_2d_stereodecoder1~`  

The `abc_2d_stereodecoder1~`, `abc_2d_stereodecoder2~`, etc., objects **decode ambisonic spatial components to stereo**.  

<h4> Parameters </h4>:  
- **gain** → Output gain (dB)  
- **directangles** → 1 for **anticlockwise** (ambisonic norm), 0 for **clockwise**  

---

### `abc_2d_stereoencoder1~`  

The `abc_2d_stereoencoder1~`, `abc_2d_stereoencoder2~`, etc., objects **encode stereo sources into ambisonics** using **two encoders**.  

<h4> Parameter: </h4>  
- **Opening angle** → Initialized to **60 degrees**  

---

### `abc_2d_synfxdecorrelation1~`  

The `abc_2d_syn_decorrelation1~`, `abc_2d_syn_decorrelation2~`, etc., objects **generate spatially decorrelated ambisonic components from a mono signal**.  

The `abc_2d_fx_decorrelated1~`, `abc_2d_fx_decorrelated2~`, etc., **apply decorrelation** to pre-existing ambisonic spatial components (from encoders, maps, etc.).  

If ambisonic **order = N**, the number of spatial components **P = 2N + 1**.  
Each spatial component is delayed, and the **P delay lines** are controlled by the **factor** parameter (0 to 1).  

<h4> Parameters </h4>:  
- **delay** → Maximum delay in samples (default **48,000**, min **10**, max **262,144** ≈ **5.46 sec @ 48 kHz**)  
- **factor** → Controls how much delay is applied (0 to 1)  
- **functiontype** → Distribution mode for delay times (values: **0 to 21**)  
## `abc_2d_synfxdelay1~`

The `abc_2d_syn_delay1~`, `abc_2d_syn_delay2~`, etc., objects generate spatial delayed components in ambisonic from one mono signal. The `abc_2d_fx_delay1~`, `abc_2d_fx_delay2~`, etc., objects apply delays to spatial components already created by encoders or maps. 

If ambisonic order is N, the number of spatial components is P = 2N + 1. The P delays are equally spread between `deltime/N` and `deltime`, which is the maximum delay in milliseconds (H0 → `deltime/N`, H-1 & H1 → `2*deltime/N`, etc., H-N & HN → `deltime`).

<h4> Parameters </h4>
- **deltime**: Maximum delay in milliseconds of the upper spatial component (default 100, min 2, max 10000)
- **window**: Duration in milliseconds of the interpolation between two values of delay without any click (default 400, min 10, max 1000)
- **feedback**: Provides a possibility of reinjection on the P delay lines (between 0 and 1)

## `abc_2d_synfxgrain1~`

The `abc_2d_syn_grain1~`, `abc_2d_syn_grain2~`, etc., objects generate spatial granular components in ambisonic from one mono signal. The `abc_2d_fx_grain1~`, `abc_2d_fx_grain2~`, etc., objects apply granulators to spatial components already created by encoders or maps.

If ambisonic order is N, the number of spatial components is P = 2N + 1. For these P granulators, grain sizes and maximum delays are equally spread. The grain sizes decrease from GS (H0) to GS/(N+1) (H-N & HN) through GS*N/(N+1) (H-1 & H1), etc. The maximum delays increase from 0 (H0) to D*N/(N+1) (H-N & HN) through D/(N+1) (H-1 & H1).

<h4> Parameters </h4>
- **GS (grain size)**: Grain size in milliseconds (default 400, min 2, max 3000)
- **D (deltime)**: Delay in milliseconds (default 100, min 2, max 5000)
- **feedback**: Provides a possibility of reinjection on the P delay lines (between 0 and 1)
## `abc_2d_synfxringmod1~`

The `abc_2d_syn_ringmod1~`, `abc_2d_syn_ringmod2~`, etc., objects generate spatial components in ambisonics from a mono signal using ring modulators. The `abc_2d_fx_ringmod1~`, `abc_2d_fx_ringmod2~`, etc., objects apply ring modulation to pre-existing spatial components.

If the ambisonic order is N, the number of spatial components is P = 2N + 1. The P ring modulators are driven by a `factor` parameter (0 to 1). The ith ring modulation frequency is (i+1)*f0/P. The `factor` parameter determines whether ring modulation is applied or the direct sound is output.

<h4> Parameters </h4>
- **factor**: Controls the ring modulators (0 to 1)
- **functiontype**: Sets the distribution used to spread delay time between spatial components (0 to 21)
- **f0**: Maximum modulation frequency of the ring modulators (Hz, default 10, min 0, max 10000)

## `abc_2d_vbap2~`

The `abc_vbap2~`, `abc_vbap3~`, etc., objects implement the VBAP algorithm by Ville Pulkki for various numbers of loudspeakers arranged in a circle with potentially irregular angles.

<h4> Parameters </h4>
- **a-0, a-1, a-2, ...**: Angles of the loudspeakers (degrees)

## `abc_2d_wider1~`

The `abc_2d_wider1~`, `abc_2d_wider2~`, etc., objects widen the diffusion of a localized sound. The order-dependent signals are weighted logarithmically for linear changes.

## `abc_addsynth1~`

The `abc_addsynth1~`, `abc_addsynth2~`, etc., objects enable additive synthesis by combining elementary sound modules. Each module includes two oscillators that start at the same frequency but can be tuned finely using `fbeat` frequencies.

<h4> Parameters </h4>
- **f0**: General fundamental frequency
- **fmult00, fmult01, ...**: Multipliers of f0 for partial frequencies
- **amp00, amp01, ...**: Amplitudes of the partials (dB)
- **fbeat**: Frequency increment of the second oscillator

## `abc_ambi_scope`

The `abc_ambi_scope1_m`, `abc_ambi_scope2_m`, ..., `abc_ambiscope7_m` objects include the necessary `abc_2d_scope1_m`, `abc_2d_scope2_m`, ..., `abc_2d_scope7_m` objects to enable direct visualization of the ambisonic sound field at the corresponding ambisonic order (1 to 7).

<h4> Parameters </h4>
- **gridcolor, bgcolor, fgcolor, ...**: Color parameters from the `scope~` object in the cyclone library
- **refresh time**: Refresh time in milliseconds for the embedded `abc_2d_scope[N]` objects

## `abc_ambi_scope_m`

The `abc_ambi_scope_m` objects (`abc_ambi_scope1_m`, `abc_ambi_scope2_m`, ..., `abc_ambi_scope7_m`) include the necessary `abc_2d_scope1_m`, `abc_2d_scope2_m`, ..., `abc_2d_scope7_m` objects to enable direct visualization of the ambisonic sound field at the corresponding ambisonic order (1 to 7).

<h4> Parameters </h4>
- **gridcolor, bgcolor, fgcolor, etc.**: Color parameters from the `scope~` object in the cyclone library.
- **refresh time**: Refresh time in milliseconds for the embedded `abc_2d_scope[N]` objects.

## `abc_amp_scope`

The `abc_amp_scope` object offers a visual representation of the amplitude of a signal over time. The horizontal axis represents time in samples, and the vertical axis represents the amplitude of the signal.

<h4> Parameters </h4>
- **ticktime**: Duration in milliseconds between two triggerings of the display from left to right.

## `abc_busmult1~`

The `abc_busmult1~`, `abc_busmult2~`, ... objects enable multichannel bus multiplications (from 1 signal to 16 signals). Two buses are connected to the object, the left one and the right one.

## `abc_busplus1~`

The `abc_busplus1~`, `abc_busplus2~`, ... objects enable multichannel bus additions (from 1 signal to 16 signals). Two buses are connected to the object, the left one and the right one.

## `abc_busselect1~`

The `abc_busselect1~`, `abc_busselect2~`, ... objects enable multichannel bus selections (from 1 signal to 15 signals). Two buses are connected to the object, the left one and the right one.

<h4> Parameters </h4>
- **leftOrRight**: Selects between the left or the right bus.
- **ramp**: Sets a crossfade duration when switching between the two buses.

## `abc_cartopol~`

The `abc_cartopol~` object converts Cartesian coordinates to polar coordinates (both as signals). The angle is in radians.

## `abc_chopan1~`

The `abc_chopan1~`, `abc_chopan2~`, ... objects enable multichannel stereo panning using the Chowning model to maintain constant acoustic energy and avoid a loss in the center of the scene.

<h4> Parameters </h4>
- **phi0 angle**: Sets the opening angle of the stereo in degrees.
- **incAngle**: Controls the incident angle (in degrees) of the incoming sound (for `abc_chopan1~` only).

## `abc_cosrandenv1~`

The `abc_cosrandenv1~`, `abc_cosrandenv2~`, ... objects provide multichannel envelopes based on the cosine curve.

<h4> Parameters </h4>
- **rarefaction**: A probability distribution applied to each channel, providing a factor that is 1 or 0 to apply a statistical duration of silence. A rarefaction of 0.3 means 30% of the envelopes are muted and 70% are played. When rarefaction is 0, the envelope is constantly played; when it is 1, no sound is played at all (maximum rarefaction).

## `abc_delay1~`

The `abc_delay1~`, `abc_delay2~`, etc., objects provide multiple parallel delay lines with reinjection. Each line is a double overlapped delay enabling duration changes without clicking at a maximum speed set by the `updatefreq` parameter, initialized at 30 Hz. Durations are given as musical durations: 1 stands for a quarter note, 0.5 for an eighth note, 0.25 for a sixteenth note, etc.

<h4> Parameters </h4>
- **dur-0, dur-1, dur-2, ...**: Musical durations automatically converted to milliseconds based on the `tempo` parameter (in bpm).
- **fdbk-0, fdbk-1, fdbk-2, ...**: Individual feedback for each delay line (between 0 and 1).
- **gain-0, gain-1, gain-2, ...**: Individual gain for each delay line (in dB, between -127 and +18).

## `abc_delaychain2~`

The `abc_delaychain2~`, `abc_delaychain3~`, etc., objects provide chains of delays where the output of delay #k is internally connected to the input of delay #k+1, with a global reinjection. Each line is a double overlapped delay enabling duration changes without clicking at a maximum speed set by the `updatefreq` parameter, initialized at 30 Hz. Durations are given as musical durations: 1 stands for a quarter note, 0.5 for an eighth note, 0.25 for a sixteenth note, etc.

<h4> Parameters </h4>
- **dur-0, dur-1, dur-2, ...**: Musical durations automatically converted to milliseconds based on the `tempo` parameter (in bpm).
- **gain-0, gain-1, gain-2, ...**: Individual gain for each delay line (in dB, between -127 and +18).
- **fdbk**: Feedback parameter to loop the rhythmic structure.

## `abc_drops~`

The `abc_drops~` object simulates raindrops with a periodic exciter that enters a resonant filter whose frequency varies randomly at a random speed.

<h4> Parameters </h4>
- **dropperiod**: Period of the drop (in milliseconds).
- **dropthinness**: Thinness of the impulse entering the resonant filter (higher values mean thinner impulses).
- **qf**: Quality factor of the resonant filter.
- **limiter**: Use of the limiter at the output (1 for yes, 0 for no).
- **avgfreq**: Average frequency of the randomization of drop frequencies (in Hz).
- **attackdur**: Duration of the attack of the envelope (in milliseconds).

## `abc_env_noise~`

The `abc_env_noise~` object is a noise generator enveloped with a positive cosine shape (Hanning window). It uses rarefaction.

## `abc_envfollower~`

The `abc_envfollower~` object tracks the envelope of an incoming signal.

<h4> Parameters </h4>
- **attack**: Attack duration (in seconds, initial value: 0.001 sec).
- **release**: Release duration (in seconds, initial value: 0.01 sec).

## `abc_flanger1~`

The `abc_flanger1~`, `abc_flanger2~`, etc., objects provide classic multichannel flangers with sinusoidal delay.

<h4> Parameters </h4>
- **rate**: Frequency of the sinusoid varying the delay duration.
- **depth**: Maximum delay duration in milliseconds.
- **offset**: Shifts the variation of the delay duration between `offset` and `offset + depth`.
- **spread**: Controls spatial spreading (0 = mono, 1 = maximum spatial split).

## `abc_freqshift1~`

The `abc_freqshift1~`, `abc_freqshift2~`, etc., objects provide parallel multiple frequency shifters. Each line is a frequency shifter in Direct Form 2 provided by a quadruple biquad.

<h4> Parameters </h4>
- **fr-0, fr-1, ...**: Shifting frequencies in Hz (positive or negative).
- **gain-0, gain-1, ...**: Individual gain in dB (between -127 and +18).

## `abc_gain`

The `abc_gaincontrol` abstraction outputs a message 'gain' followed by an amplitude value in dB (from -127 to +18 dB). It enables control of `abc_gain` and `abc_decoder` objects.

## `abc_gain1~`

The `abc_gain1~`, `abc_gain2~`, etc., objects provide multichannel gain controls in dB.

## `abc_generator~`

The `abc_generator~` object enables the generation of various sounds (noise, sinus, phasor). Generated sounds are pulsed at a certain frequency (pulse rate) and have a pulse ratio (or duty: ratio between sound and silence).

## `abc_gotoevent`

The `abc_gotoevent` object is used to jump to a specific event in a sequence.

## `abc_grain1~`

The `abc_grain1~`, `abc_grain2~`, etc., objects are parallel granular processes.

<h4> Parameters </h4>
- **gs-0, gs-1, gs-2, ...**: Grain sizes in milliseconds for the granulators.
- **dt-0, dt-1, dt-2, ...**: Maximum delays in milliseconds for the granulators.
- **fdbk-0, fdbk-1, fdbk-2, ...**: Feedback levels for the granulators (0 to 1).
- **rrf-0, rrf-1, rrf-2, ...**: Rarefaction levels for the granulators (0 to 1, where 0 means no rarefaction and 1 means total rarefaction).

## `abc_harmo1~`

The `abc_harmo1~`, `abc_harmo2~`, etc., objects provide parallel multiple harmonizers using the Doppler effect.

<h4> Parameters </h4>
- **gain-0, gain-1, gain-2, ...**: Individual gains in dB (between -127 and +18).
- **trans-0, trans-1, trans-2, ...**: Transposition coefficients in midicents (e.g., 100 for an upper semitone, 200 for an upper tone, -400 for a lower major third).

## `abc_jupiterbank2~`

The `abc_jupiterbank2~` object is inspired by Philippe Manoury's bank of 14 oscillators used in "Jupiter" for flute and live electronics. It generates spectra that can evolve from harmonic to inharmonic content. Each partial has a separate output.

<h4> Parameters </h4>
- **k**: Constant determining the harmonic/inharmonic behavior.
- **f0**: Fundamental frequency.
- **osc2filter**: Crossfade between oscillators and filters (0 for oscillators, 1 for filters).
- **resg**: Gain of the filters.
- **resq**: Quality factor of the filters.
- **fa**: Factor controlling the amplitudes of the 14 oscillators.
- **transfer function**: Maps each frequency multiplied by `fa` to a level between 0 and 127.

The Faust implementation is inspired by Maxence Larrieu's article: [Maxence Larrieu's article](https://hal.archives-ouvertes.fr/hal-02135597).

## `abc_jupiterbank~`

The `abc_jupiterbank~` object is inspired by Philippe Manoury's bank of 14 oscillators used in "Jupiter" for flute and live electronics. It generates spectra that can evolve from harmonic to inharmonic content. Each partial has a separate output.

<h4> Parameters </h4>
- **k**: Constant determining the harmonic/inharmonic behavior.
- **f0**: Fundamental frequency.
- **osc2filter**: Crossfade between oscillators and filters (0 for oscillators, 1 for filters).
- **resg**: Gain of the filters.
- **resq**: Quality factor of the filters.

The 14 frequencies (i from 0 to 13) are given by the formula: \( f_i = (k+i) \times f0 \). When `k` is 1, the spectrum is harmonic (e.g., \( f0, 2 \times f0, \ldots, 14 \times f0 \)). When `k` is not an integer, the spectrum is inharmonic. The crossfade between oscillators and filters is controlled by `osc2filter`.

The Faust implementation is inspired by Maxence Larrieu's article: [Maxence Larrieu's article](https://hal.archives-ouvertes.fr/hal-02135597).
## `abc_linedrive~`

The `abc_linedrive~` object converts a signal between 0 and 127 to a signal between 0 and `outputmax` following an exponential profile defined by the `expcurve` parameter.

## `abc_linrandenv1~`

The `abc_linrandenv1~`, `abc_linrandenv2~`, etc., objects provide multichannel envelopes based on linear segments.

A probability distribution is applied to each channel, providing a factor of 1 or 0 for each envelope, enabling a statistical duration of silence. For example, if the shortening is 0.3, it means 30% of the envelopes are muted (multiplied by 0) and 70% are played (multiplied by 1). When the shortening is 0, the envelope is constantly played, whereas when it is 1, no sound is played at all (maximum shortening).

## `abc_matrix2~`

The `abc_matrix2~`, `abc_matrix3~`, etc., objects provide signal matrices with coefficients ranging from -1 to 1. Note that there is no `abc_matrix1~`.

The `ramp` parameter sets the crossfade duration (in milliseconds) between the current matrix status and the next.

## `abc_mult2pi~`

The `abc_mult2pi~` object multiplies the incoming signal by 2π. Therefore, a `phasor~` signal between 0 and 1 becomes an angle between 0 and 2π.
## `abc_multinoise1~`

The `abc_multinoise1~`, `abc_multinoise2~`, etc., objects produce multiple decorrelated white noise signals.

## `abc_musdur`

The `abc_musdur` object provides a selection of musical durations:
- **whole** = 4
- **half** = 2
- **quarter** = 1
- **8th** = 0.5
- **16th** = 0.25
- **32nd** = 0.125
- **triplet** = 0.333

## `abc_peakamp~`

The `abc_peakamp~` object computes the highest absolute value of the incoming signal over a duration defined by the `period` attribute in milliseconds.

<h4> Parameters </h4>
- **period**: Sets the measurement window for the peak amplitude (in milliseconds).

## `abc_phasor2pi~`

The `abc_phasor2pi~` object generates a phasor signal that ranges from 0 to 2π, directly expressing an angle in radians.

## `abc_poltocar~`

The `abc_poltocar~` object converts polar coordinates to Cartesian coordinates, with the angle expressed in radians.

## `abc_puckettespaf~`

The `abc_puckettespaf~` object is a Phase-Aligned Formant (PAF) generator based on Miller Puckette's technique. It consists of a two-cosine carrier signal multiplied by a waveshaping pulse generator.

<h4> Parameters </h4>
- **cf**: Central frequency (Hz).
- **f0**: Fundamental frequency (Hz).
- **bw**: Bandwidth (Hz) controlling the width of the central peak.
- **wf**: Waveshaping function (0 for Gaussian, 1 for Cauchy).
- **sigma**: Controls the Gaussian waveshaping function.
- **a**: Controls the Cauchy waveshaping function.

The `abc_puckettespaf2~` object adds the possibility of inharmonic generation by adding a variable phase to the driving phasor, controlled by:
- **ifreq**: Inharmonic frequency (Hz).
- **iamp**: Inharmonic amplitude (0 to 1).

For more details, refer to Miller Puckette's paper: [Phase-Aligned Formant (PAF) Generator](http://msp.ucsd.edu/techniques/v0.11/book-html/node96.html).

## `abc_quadriout`

The `abc_quadriout` abstraction enables 4-channel output with global gain control in dB. The global gain and output numbers (for the `dac~` object) can be set as default values.

## `abc_rev4~`

The `abc_rev4~` module is a classic reverberation effect. It is available in two versions: `abc_rev4stereo~` for stereo output and `abc_rev4quadri~` for quadriphonic output, which splits the delay line outputs to 4 channels.

<h4> Controls </h4>
- **revDur**: Reverberation duration (0 to 127, where 127 means 'infinite' duration)
- **revGain**: Gain control (0 to 127)

## `abc_rissetsbell~`

The `abc_rissetsbell~` object synthesizes bell sounds based on Risset's bell model, using 11 oscillators and envelopes. The model is extended with a double oscillator for detuning and a filter for crossfading between synthesis and filtering.

<h4> Parameters </h4>
- **freq**: Base frequency (Hz) for computing the 11 partials
- **dur**: Global duration of the synthesized bell (milliseconds)
- **pfreq2**: Frequency multiplication factor for the second oscillator (1 means no detuning)
- **osc2filter**: Crossfade factor between oscillators and filters (1 means no filtering)
- **resg**: Gain of the filters when activated
- **resq**: Quality factor of the filters when activated

## `abc_simplefmburst`

The `abc_simplefmburst` abstraction generates a short (110 milliseconds) FM synthesized sound with a carrier at 440 Hz, a modulator at 220 Hz, and a modulation index of 5.

## `abc_slider2map`

The `abc_slider2map` abstraction enables graphical control of the `abc_2d_map` objects.

## `abc_sounddetector~`

The `abc_sounddetector~` object detects attacks and releases of incoming sound. It provides:
- An on-off envelope (first outlet)
- A binary signal for attack detection (second outlet)
- A binary signal for release detection (third outlet)

<h4> Parameters </h4>
- **offset**: dB offset to increase amplitude measurement (default: 10 dB)
- **noiseFloor**: dB threshold to distinguish between incoming sound and ambient noise (default: -50 dB)
- **noteOn**: Threshold in dB for attack detection (default: 60 dB)

## `abc_spectrogram`

The `abc_spectrogram` object visually represents the spectrum of frequencies of a signal. The horizontal axis represents frequency bins (dependent on FFT size), and the vertical axis represents the amplitude of frequency bins.

<h4> Parameters </h4>
- **ampscale**: Amplitude scale (0 for rms, 1 for decibel, 2 for power)
## `abc_stereoout`

The `abc_stereoout` abstraction enables 2-channel output (dac~ 1 & 2) with global gain control in dB. The global gain can be set as a default value.

## `abc_subtractsynth1~`

The `abc_subtractsynth1~`, `abc_subtract2~`, etc., objects enable subtractive synthesis by applying banks of band-pass filters to incoming sounds (e.g., white, pink, decorrelated). 

<h4> Parameters </h4>
- **f0**: General fundamental frequency.
- **fmult00, fmult01, ...**: Multipliers of f0 for partial frequencies.
- **amp00, amp01, ...**: Amplitudes of the partials (dB).
- **gain**: General amplitude control (dB).
- **filterQ**: Quality factor of the filters.
- **filterG**: Gain of the filters.

## `abc_synthesizers~`

- **abc_soundcoat~**: A set of 16 band-pass filters receiving a noise sound as input. The output gains of the filters are slowly randomized.
    - **randwin**: Duration of the randomization cycle (ms, default 3000, min 1, max 20000).

- **abc_soundgrain~**: A granulator on a rainstick sound looped at a controllable speed.
    - **freqmult**: Loop speed multiplier (default 1, min 0.01, max 100).

- **abc_audiotester~**: Tests the audio configuration from 1 to 16 loudspeakers by sending pink noise alternately to them.

- **abc_pulsedenv2synthN~**: Multichannel sound burst generators based on a sinusoidal sound.
    - **carrierFreq**: Frequency of the carrier sinusoid.
    - **envFreq**: Frequency of the triangular envelopes.
    - **ratio**: Silence/sound ratio.
    - **spread**: Decorrelates short envelopes (0 to 1).
    - **fc**: Low-pass filter frequency.
    ## `abc_xy_scope`

    The `abc_xy_scope` abstraction visualizes X-Y signals, such as ambisonic components at order N, using `abc_2d_scopeN~` objects. It leverages the `scope~` object from the cyclone library.

    <h4> Controls </h4>
    Refer to the `scope~` object documentation in the cyclone library for detailed control information.


