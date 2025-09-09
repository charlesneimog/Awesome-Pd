<div class="grid cards" markdown>
- :material-tune: [__out~__](../objects/out~.md) `out~` has a built in `sum~` object, so it can take multichannel signals and sum them together for each input.
.

- :material-tune: [__quantizer~__](../objects/quantizer~.md) `quantizer~` approximates a value to step values defined by the argument.

- :material-tune: [__xmod2~__](../objects/xmod2~.md) `xmod2~` performs is a variant of `xmod~`, but only performs frequency modulation (so far) and uses a different and cheap sine waveform that promotes more chaotic and cool sounds.
.

- :material-tune: [__smooth~__](../objects/smooth~.md) `smooth~` smoothens a signal transition with linear interpolation by default, at a given time in ms.

- :material-tune: [__cosine~__](../objects/cosine~.md) `cosine~` is a cosine oscillator that accepts negative frequencies, has inlets for phase sync and phase modulation.

- :material-tune: [__spectrograph~__](../objects/spectrograph~.md) `spectrograph~` is an abstraction for visualizing FFT amplitudes from 0hz to Nyquist.

- :material-tune: [__retune__](../objects/retune.md) `retune` receives a scale as a list of steps in cents and a base MIDI pitch value (default 60).

- :material-tune: [__circle__](../objects/circle.md) `circle` is a two dimensional slider GUI abstraction with a circular area (see also [else/slider2d).
.

- :material-tune: [__autotune2__](../objects/autotune2.md) `autotune2` receives a scale as a list of steps in cents and then retunes incoming cents values to the closest step in the scale.
.

- :material-tune: [__wave~__](../objects/wave~.md) `wave~`'s input phase varies between 0 and 1, which in 32-bit floating point arithmetic has 24 bits of index resolution.

- :material-tune: [__add__](../objects/add.md) The `add` object in Pure Data accumulates input values to a running sum, starting from a configurable initial value (0 by default).

- :material-tune: [__maximum__](../objects/maximum.md) `maximum` outputs the maximum of two or more values.

- :material-tune: [__round__](../objects/round.md) `round` approximates positive and negative numbers to an integer multiple of any given number that is greater or equal to 0 (0 makes no approximation, so the original input is output unchanged).
.

- :material-tune: [__mag~__](../objects/mag~.md) `mag~` gets the spectrum magnitudes (amplitudes) from cartesian coordinates (real / imaginary).

- :material-tune: [__parabolic~__](../objects/parabolic~.md) `parabolic~` is a parabolic oscillator that accepts negative frequencies, has inlets for phase sync and and phase modulation.

- :material-tune: [__rotate~__](../objects/rotate~.md) `rotate~` performs equal power rotation for 'n' channels (default 2).

- :material-tune: [__scope3d~__](../objects/scope3d~.md) `scope3d~` displays signals in 3D.

- :material-tune: [__trapezoid~__](../objects/trapezoid~.md) `trapezoid~` is a trapezoidal wavetable that is read with phase values from 0 to 1 into the first inlet, so a `phasor~` input turns it into a wavetable oscillator.

- :material-tune: [__tanh~__](../objects/tanh~.md) `tanh~` calculates the hyperbolic tangent function of input sample.

- :material-tune: [__scale__](../objects/scale.md) `scale` maps an input range to an output range.

- :material-tune: [__polymetro__](../objects/polymetro.md) `polymetro` is a polyrhythmic metronome.

- :material-tune: [__shaper~__](../objects/shaper~.md) `shaper~` performs waveshaping with transfer functions, in which signal input values (from -1 to 1) are mapped to the the transfer function's indexes.

- :material-tune: [__phaseshift~__](../objects/phaseshift~.md) `phaseshift~` is a 2nd allpass filter, which keeps the gain and only alters the phase from 0 (at 0 hz) to 360º (at the Nyquist frequency).

- :material-tune: [__xfade~__](../objects/xfade~.md) `xfade~` crossfades between two sources (that can have 1 to 64 channels each).

- :material-tune: [__function~__](../objects/function~.md) `function~` generates functions from arguments/list input.

- :material-tune: [__pimpmul~__](../objects/pimpmul~.md) `pimpmul~` is a "pimp~" multiplier.

- :material-tune: [__metronome__](../objects/metronome.md) `metronome` understands complex time signatures and outputs timeline data (bar, sub-bar, beat and sub-beat count) and phase output.

- :material-tune: [__scale2freq__](../objects/scale2freq.md) `scale2freq` gets a scale as a list of cents values, a base/fundamental pitch and outputs a list of frequency in hertz between a minimum and maximum value.

- :material-tune: [__ceil~__](../objects/ceil~.md) `ceil~` is a ceil math function for signals.

- :material-tune: [__db2lin~__](../objects/db2lin~.md) `db2lin~` converts amplitude values from deciBel Full Scale (dBFS) to linear.

- :material-tune: [__rand.f__](../objects/rand.f.md) `rand.f` generates random float values for a given range when triggered with a bang.

- :material-tune: [__slide~__](../objects/slide~.md) `slide~` filters an input signal logarithmically between changes in signal value.

- :material-tune: [__mtx~__](../objects/mtx~.md) `mtx~` routes signals from any inlets to one or more outlets.

- :material-tune: [__hz2rad__](../objects/hz2rad.md) `hz2rad` converts a frequency in Hertz to "Radians per Sample" - which depends on the patch's sample rate (sr).

- :material-tune: [__pol2car~__](../objects/pol2car~.md) `pol2car~` converts polar coordinates (amplitude / phase) to cartesian coordinates (real / imaginary).
.

- :material-tune: [__sr~__](../objects/sr~.md) `sr~` can set the sample rate and also reports the sample rate frequency or period when loading the patch, when receiving a bang or when it changes.

- :material-tune: [__bitand~__](../objects/bitand~.md) `bitand~` compares the bits of two values with "Bitwise-AND" (bits are set to 1 if both are "1", 0 otherwise).

- :material-tune: [__crusher~__](../objects/crusher~.md) `crusher~` is a bit-crusher/reducer and decimator abstraction based on the objects `quantizer~` (mode 4) and `downsample~`, where an input signal quantized and downsampled to generate distortion and aliasing.

- :material-tune: [__round~__](../objects/round~.md) `round~` approximates positive and negative numbers to an integer multiple of any given number that is greater or equal to 0 (0 makes no approximation - so the original input is output unchanged).
.

- :material-tune: [__deltaclip~__](../objects/deltaclip~.md) `deltaclip~` limits the change between samples in an incoming signal.

- :material-tune: [__fm~__](../objects/fm~.md) `fm~` is a simple frequency modulation unit consisting of a pair of sinusoidal oscillators, where one modulates the frequency input of another.

- :material-tune: [__lag2~__](../objects/lag2~.md) `lag2~` is like `lag~` but has a different time for ramp up and ramp down.

- :material-tune: [__rint__](../objects/rint.md) `rint` takes floats and rounds them to the nearest integer value.
.

- :material-tune: [__trunc__](../objects/trunc.md) `trunc` truncates floats and lists towards zero, that means only the integer value is considered, like in vanilla's `int`.
.

- :material-tune: [__tabreader__](../objects/tabreader.md) `tabreader` accepts indexes from 0 to 1 by default and reads an array with different interpolation methods with multi channel support.

- :material-tune: [__amean__](../objects/amean.md) `amean` creates a list of arithmetic means.

- :material-tune: [__midi2note__](../objects/midi2note.md) `midi2note` converts a MIDI pitch value to note names (such as Eb3).

- :material-tune: [__scope~__](../objects/scope~.md) `scope~` displays signals in the style of an oscilloscope.

- :material-tune: [__blip~__](../objects/blip~.md) `blip~` uses DSF (Discrete-Summation Formulae) to generate waveforms as a sum of cosines.

- :material-tune: [__power~__](../objects/power~.md) `power~` is a power function waveshaper for signals that extends the usual definition of exponentiation and returns -pow(-a, b) when you have a negative signal input.

- :material-tune: [__tri~__](../objects/tri~.md) `tri~` is a triangular wave oscillator that accepts negative frequencies, has inlets for phase sync and phase modulation.

- :material-tune: [__knob__](../objects/knob.md) `knob` has an exponential and log feature just like the `rescale` object.

- :material-tune: [__dec2hex__](../objects/dec2hex.md) `dec2hex` converts decimal values to hexadecimal ones.

- :material-tune: [__compress~__](../objects/compress~.md) `compress~` is an abstraction that performs compression.

- :material-tune: [__sfz~__](../objects/sfz~.md) `sfz~` also has microtonal capabilities.

- :material-tune: [__fold__](../objects/fold.md) `fold` folds between a low and high value.

- :material-tune: [__quantizer__](../objects/quantizer.md) `quantizer` approximates a value to step values defined by the argument.

- :material-tune: [__rotate.mc~__](../objects/rotate.mc~.md) `rotate.mc~` performs equal power rotation for any number of channels given by a multichannel signal input.

- :material-tune: [__rand.i~__](../objects/rand.i~.md) `rand.i~` generates random integer values for a given range when triggered.

- :material-tune: [__hex2dec__](../objects/hex2dec.md) `hex2dec` converts hexadecimal values to decimal ones.

- :material-tune: [__gmean__](../objects/gmean.md) `gmean` creates a list of geometric means.

- :material-tune: [__a.sum__](../objects/a.sum.md) The `a.sum` object in Pure Data sums the last `x` numbers of an array.

- :material-tune: [__sum__](../objects/sum.md) `sum` sums a list of values.
.

- :material-tune: [__samps2ms~__](../objects/samps2ms~.md) `samps2ms~` is a simple abstraction that converts time values number of samples to ms.

- :material-tune: [__lin2db~__](../objects/lin2db~.md) `lin2db~` converts amplitude values from linear to a deciBel Full Scale (dBFS) with support for multichannel signals.

- :material-tune: [__db2lin__](../objects/db2lin.md) `db2lin` converts amplitude values from deciBel Full Scale (dBFS) to linear.

- :material-tune: [__rms~__](../objects/rms~.md) `rms~` is similar to Pd Vanilla's `env~`, but it reports the RMS value in linear amplitude (default) or in dBFS.
.

- :material-tune: [__note2midi__](../objects/note2midi.md) `note2midi` converts note names (such as 'C4') to MIDI pitch values.

- :material-tune: [__bend.out__](../objects/bend.out.md) `bend.out` formats and sends raw MIDI pitch bend messages to Pd's MIDI output and its outlet.

- :material-tune: [__bitshift~__](../objects/bitshift~.md) `bitshift~` can produce NaNs and +/-INFs - but denormals are zeroed out.

</div>