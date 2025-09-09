<div class="grid cards" markdown>
- :material-tune: [__out~__](../objects/out~.md) `out~` has a built in `sum~` object, so it can take multichannel signals and sum them together for each input.
.

- :material-tune: [__quantizer~__](../objects/quantizer~.md) `quantizer~` approximates a value to step values defined by the argument.

- :material-tune: [__unmerge~__](../objects/unmerge~.md) `unmerge~` separates the channels of a multichannel signal in groups of any size (default 1).

- :material-tune: [__out8~__](../objects/out8~.md) `out8~` is a convenient octaphonic input/output abstraction.

- :material-tune: [__tabplayer~__](../objects/tabplayer~.md) `tabplayer~` plays arrays with multichannel support.

- :material-tune: [__wt2d~__](../objects/wt2d~.md) `wt2d~` is an interpolating wavetable oscillator like `wt~`, but besides a horizontal dimension, it can also scan through a vertical dimension of a sliced wavetable.

- :material-tune: [__xgate2~__](../objects/xgate2~.md) `xgate2~` routes an input signal to 'n' specified outlets with crossfading between adjacent channels according to a spread parameter.
.

- :material-tune: [__white~__](../objects/white~.md) `white~` is a white noise generator from a pseudo random number generator algorithm.

- :material-tune: [__smooth~__](../objects/smooth~.md) `smooth~` smoothens a signal transition with linear interpolation by default, at a given time in ms.

- :material-tune: [__cosine~__](../objects/cosine~.md) `cosine~` is a cosine oscillator that accepts negative frequencies, has inlets for phase sync and phase modulation.

- :material-tune: [__envgen~__](../objects/envgen~.md) `envgen~` is an envelope (and an all purpose line) generator (here it creates a 1000 ms line to 1 and then a 500 ms line to 0).

- :material-tune: [__slew~__](../objects/slew~.md) `slew~` takes an amplitude limit per second and an incoming value to be 'slew limited'.

- :material-tune: [__float2sig~__](../objects/float2sig~.md) `float2sig~` (or `f2s~` for short) is an abstraction based on `vline~` that converts floats to signals or lists to multichannel signals.

- :material-tune: [__midi.in__](../objects/midi.in.md) `midi.in` sends "cooked" MIDI data instead of "raw" data like `midiin` with MIDI data type symbol, values and channel (but a note output is sent as a simple numeric list).

- :material-tune: [__gray~__](../objects/gray~.md) `gray~` generates noise based on "gray code" or reflected binary code (RBC), which results from flipping random bits (sot is is based on a pseudo random number generator algorithm.).

- :material-tune: [__midi.out__](../objects/midi.out.md) `midi.out` sends MIDI data from "cooked" data, instead of "raw" data like `midiout`.

- :material-tune: [__mono.rev~__](../objects/mono.rev~.md) `mono.rev~` is a reverb abstraction with mono input but stereo output.

- :material-tune: [__autofade.mc~__](../objects/autofade.mc~.md) `autofade.mc~` is an automatic fade in/out for multichanne inputs.

- :material-tune: [__vsaw~__](../objects/vsaw~.md) `vsaw~` is a variable sawtooth waveform oscillator that also becomes a triangular osccilator.

- :material-tune: [__autofade2.mc~__](../objects/autofade2.mc~.md) `autofade2.mc~` is an automatic fade in/out for multichanne inputs.

- :material-tune: [__delace~__](../objects/delace~.md) `delace~` deinterleaves a multichannel signal according to the number of outlets.
.

- :material-tune: [__nchs~__](../objects/nchs~.md) `nchs~` gets the number of channels from a multi-channel connection, as provided by `snake~ in`, `clone` or other objects.

- :material-tune: [__tabwriter~__](../objects/tabwriter~.md) `tabwriter~` records up to 64 signal channels into arrays.

- :material-tune: [__parabolic~__](../objects/parabolic~.md) `parabolic~` is a parabolic oscillator that accepts negative frequencies, has inlets for phase sync and and phase modulation.

- :material-tune: [__rotate~__](../objects/rotate~.md) `rotate~` performs equal power rotation for 'n' channels (default 2).

- :material-tune: [__matrix~__](../objects/matrix~.md) `matrix~` routes signals from any inlets to one or more outlets.

- :material-tune: [__wavetable~__](../objects/wavetable~.md) `wavetable~` is an interpolating wavetable oscillator like `tabosc4~`, but has more features like more interpolation options, inlets for phase sync, phase modulation and also an inlet for scanning through slices.

- :material-tune: [__scope3d~__](../objects/scope3d~.md) `scope3d~` displays signals in 3D.

- :material-tune: [__autofade2~__](../objects/autofade2~.md) `autofade2~` is an automatic fade in/out for multi inputs.

- :material-tune: [__oscbank~__](../objects/oscbank~.md) `oscbank~` is a bank made of `sine~` objects.

- :material-tune: [__sigs~__](../objects/sigs~.md) `sigs~` is like vanilla's `sig~` but generates multichannel signals from an argument list and creates separate inlets for each argument (minimum size is 2).
.

- :material-tune: [__spread.mc~__](../objects/spread.mc~.md) `spread.mc~` spreads any number of input channels across any number of output channels with equal power panning according to a spread parameter.

- :material-tune: [__tanh~__](../objects/tanh~.md) `tanh~` calculates the hyperbolic tangent function of input sample.

- :material-tune: [__bl.saw~__](../objects/bl.saw~.md) `bl.saw~` is a sawtooth oscillator like `else/saw~`, but it is bandlimited.

- :material-tune: [__xfade~__](../objects/xfade~.md) `xfade~` crossfades between two sources (that can have 1 to 64 channels each).

- :material-tune: [__function~__](../objects/function~.md) `function~` generates functions from arguments/list input.

- :material-tune: [__out4~__](../objects/out4~.md) `out4~` is a convenient quadraphonic input/output abstraction.

- :material-tune: [__buffer~__](../objects/buffer~.md) `buffer~` stores audio in a memory buffer (an array).

- :material-tune: [__ceil~__](../objects/ceil~.md) `ceil~` is a ceil math function for signals.

- :material-tune: [__sample~__](../objects/sample~.md) `sample~` is an abstraction that creates an audio buffer which you can use to load a sample or record into.

- :material-tune: [__db2lin~__](../objects/db2lin~.md) `db2lin~` converts amplitude values from deciBel Full Scale (dBFS) to linear.

- :material-tune: [__gaussian~__](../objects/gaussian~.md) `gaussian~` is a gaussian oscillator.

- :material-tune: [__glide~__](../objects/glide~.md) `glide~` generates a glide/portamento from its signal input changes.

- :material-tune: [__xgate2.mc~__](../objects/xgate2.mc~.md) `xgate2.mc~` routes an input signal to 'n' specified channels in a multichannel output with crossfading between adjacent channels according to a spread parameter.
.

- :material-tune: [__voices~__](../objects/voices~.md) `voices~` is an abstraction based on `voices` and generates multichannel signals that can be used to control pitch and gate with polyphony.
.

- :material-tune: [__xselect2.mc~__](../objects/xselect2.mc~.md) `xselect2.mc~` selects from 'n' inputs with crossfading between adjacent channels according to a spread parameter.
.

- :material-tune: [__rampnoise~__](../objects/rampnoise~.md) `rampnoise~` is a low frequency (band limited) noise generator with interpolation, therefore it ramps from one random value to another, resulting in random ramps.

- :material-tune: [__synth~__](../objects/synth~.md) `synth~` is multichannel aware and can send a multichannel signal out with the '-mc' flag or message.
.

- :material-tune: [__randpulse~__](../objects/randpulse~.md) `randpulse~` is a random pulse train oscillator (which alternates between a random value and 0, or on/off).

- :material-tune: [__square~__](../objects/square~.md) `square~` is a square oscillator that accepts negative frequencies, has inlets for pulse width, phase sync and phase modulation.

- :material-tune: [__stepnoise~__](../objects/stepnoise~.md) `stepnoise~` is a low frequency (band limited) noise generator without interpolation, therefore it holds at a random value, resulting in random steps.

- :material-tune: [__fm~__](../objects/fm~.md) `fm~` is a simple frequency modulation unit consisting of a pair of sinusoidal oscillators, where one modulates the frequency input of another.

- :material-tune: [__record~__](../objects/record~.md) `record~` records up to 64 signal channels into arrays.

- :material-tune: [__pick~__](../objects/pick~.md) `pick~` picks a channel from a multichannel connection.

- :material-tune: [__tabreader__](../objects/tabreader.md) `tabreader` accepts indexes from 0 to 1 by default and reads an array with different interpolation methods with multi channel support.

- :material-tune: [__pulse~__](../objects/pulse~.md) `pulse~` is a pulse train oscillator (alternates between 1 and 0, or on/off) that accepts negative frequencies, has inlets for pulse width, phase sync and phase modulation.

- :material-tune: [__pm~__](../objects/pm~.md) `pm~` is a very basic and simple phase modulation unit, which consists of a pair of sinusoidal oscillators, where one modulates the phase input of another.

- :material-tune: [__level~__](../objects/level~.md) `level~` is a convenient abstraction for adjusting a signal's gain in dB.

- :material-tune: [__scope~__](../objects/scope~.md) `scope~` displays signals in the style of an oscilloscope.

- :material-tune: [__gatehold~__](../objects/gatehold~.md) `gatehold~` holds a gate value for a certain amount of time (specified in ms) after the gate has closed.

- :material-tune: [__sig2float~__](../objects/sig2float~.md) `sig2float~` converts signals to floats.

- :material-tune: [__select~__](../objects/select~.md) `select~` selects an input signal without crossfade and the signals can be of different channel sizes.

- :material-tune: [__repeat~__](../objects/repeat~.md) `repeat~` takes an input signal os any channel size and repeats it 'n' times.
.

- :material-tune: [__mtx.mc~__](../objects/mtx.mc~.md) `mtx.mc~` routes a channel signal from a multichannel input to one or more channels of a multichannel output.
.

- :material-tune: [__gain~__](../objects/gain~.md) `gain~` is a convenient mono gain abstraction for adjusting a signal's gain.

- :material-tune: [__tri~__](../objects/tri~.md) `tri~` is a triangular wave oscillator that accepts negative frequencies, has inlets for phase sync and phase modulation.

- :material-tune: [__bpbank~__](../objects/bpbank~.md) `bpbank~` is a bank made of `bandpass~` objects.

- :material-tune: [__meter~__](../objects/meter~.md) `meter~` is a convenient mono VU-meter abstraction.

- :material-tune: [__gain2~__](../objects/gain2~.md) `gain2~` is a convenient stereo gain abstraction, so you can adjust a stereo signal's gain.

- :material-tune: [__mix2~__](../objects/mix2~.md) `mix2~` has support for multichannel input.
.

- :material-tune: [__sfinfo__](../objects/sfinfo.md) `sfinfo` supports all files that `sfload` and `play.file~` support and can be used to query file sample information but so far only channels and 'inst' info for aif files (this object is still very experimental).
.

- :material-tune: [__send2~__](../objects/send2~.md) `send2~` is like send but automatically resizes according to the number of input channels.
.

- :material-tune: [__rotate.mc~__](../objects/rotate.mc~.md) `rotate.mc~` performs equal power rotation for any number of channels given by a multichannel signal input.

- :material-tune: [__decay~__](../objects/decay~.md) `decay~` is based on SuperCollider's "Decay" UGEN.

- :material-tune: [__rand.i~__](../objects/rand.i~.md) `rand.i~` generates random integer values for a given range when triggered.

- :material-tune: [__fbsine~__](../objects/fbsine~.md) `fbsine~` is a sinusoidal oscillator with phase modulation feedback.

- :material-tune: [__saw~__](../objects/saw~.md) `saw~` is a sawtooth wave oscillator that accepts negative frequencies, has inlets for phase sync and phase modulation.

- :material-tune: [__saw2~__](../objects/saw2~.md) `saw2~` is a sawtooth wave oscillator that accepts negative frequencies, has inlets for phase sync and phase modulation.

- :material-tune: [__sine~__](../objects/sine~.md) `sine~` is a sinusoidal oscillator that accepts negative frequencies, has inlets for phase sync and phase modulation.

- :material-tune: [__meter2~__](../objects/meter2~.md) `meter2~` is a convenient stereo VU-meter abstraction.

- :material-tune: [__velvet~__](../objects/velvet~.md) `velvet~` is a velvet noise generator, which randomly chooses either positive (1) or negative (-1) impulses at random positions in a given period set in Hz.

- :material-tune: [__samps2ms~__](../objects/samps2ms~.md) `samps2ms~` is a simple abstraction that converts time values number of samples to ms.

- :material-tune: [__xselect.mc~__](../objects/xselect.mc~.md) `xselect.mc~` selects between multiple channels from a multichannel connection (maximum 512 channels) with equal power crossfading.
.

- :material-tune: [__xselect2~__](../objects/xselect2~.md) `xselect2~` selects from 'n' inputs with crossfading between adjacent channels according to a spread parameter.
.

- :material-tune: [__mix4~__](../objects/mix4~.md) `mix4~` has support for multichannel input.
.

- :material-tune: [__pink~__](../objects/pink~.md) `pink~` is a pink noise generator, which sounds less hissy than white noise (but not as less as brown~).

- :material-tune: [__bitnormal~__](../objects/bitnormal~.md) `bitnormal~` replaces NaN (not a number), +/- infinity values and denormals of an incoming signal with zero (hence, it only lets 'normal' floats through.

- :material-tune: [__lin2db~__](../objects/lin2db~.md) `lin2db~` converts amplitude values from linear to a deciBel Full Scale (dBFS) with support for multichannel signals.

- :material-tune: [__out.mc~__](../objects/out.mc~.md) `out.mc~` takes multichannel signals and outputs them from given `dac~` channel output (default 1).

- :material-tune: [__slice~__](../objects/slice~.md) `slice~` splits a multichannel signal.

- :material-tune: [__randpulse2~__](../objects/randpulse2~.md) `randpulse2~` is a random pulse train oscillator.

- :material-tune: [__op~__](../objects/op~.md) `op~` is a signal operator where the first argument defines the the type (for either comparison, bitwise, logic and modulus operations).

- :material-tune: [__get~__](../objects/get~.md) `get~` gets one or more channels from a multichannel connection.

</div>