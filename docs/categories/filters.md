<div class="grid cards" markdown>
- :material-tune: [__pvoc.freeze~__](../objects/pvoc.freeze~.md) `pvoc.freeze~` is a freeze object based on a phase vocoder.
.

- :material-tune: [__biquads~__](../objects/biquads~.md) `biquads~` is a series of biquad filters in cascade.
.

- :material-tune: [__click~__](../objects/click~.md) `click~` generates an impulse when receiving a bang.

- :material-tune: [__slew~__](../objects/slew~.md) `slew~` takes an amplitude limit per second and an incoming value to be 'slew limited'.

- :material-tune: [__pluck~__](../objects/pluck~.md) `pluck~` is a Karplus-Strong algorithm with a 1st order lowpass filter in the feedback loop.

- :material-tune: [__fdn.rev~__](../objects/fdn.rev~.md) `fdn.rev~` is a feedback delay network reverberator which can be used for late reflections (a.k.a reverb tail).

- :material-tune: [__resonant~__](../objects/resonant~.md) `resonant~` is a bandpass resonator filter like `bandpass~`, but it doesn't have a maximum dB value of 0, so changing the Q increases the gain of the filter.

- :material-tune: [__resonbank~__](../objects/resonbank~.md) `resonbank~` is a bank of resonators made of `resonator~` objects.

- :material-tune: [__slew2~__](../objects/slew2~.md) `slew2~` is like `slew~` but has independent values for upwards & downwards ramps.

- :material-tune: [__rampsmooth~__](../objects/rampsmooth~.md) `rampsmooth~` smooths a signal across 'n' samples.

- :material-tune: [__bl.wavetable~__](../objects/bl.wavetable~.md) `bl.wavetable~` is a bandlimited wavetable oscillator abstraction that uses the upsampling/filtering techniquelike, which makes the object quite inefficient CPU wise.

- :material-tune: [__lores~__](../objects/lores~.md) `lores~` implements an inexpensive resonant lowpass filter.

- :material-tune: [__echo.rev~__](../objects/echo.rev~.md) `echo.rev~` is an echo/reverb abstraction.

- :material-tune: [__shaper~__](../objects/shaper~.md) `shaper~` performs waveshaping with transfer functions, in which signal input values (from -1 to 1) are mapped to the the transfer function's indexes.

- :material-tune: [__smooth2~__](../objects/smooth2~.md) `smooth2~` is just like `smooth~` but has distinct ramp times for both up and down.
.

- :material-tune: [__resonator~__](../objects/resonator~.md) `resonator~` is just like `resonant~`, but the resonance parameter is defined as resonance time in 't60'.

- :material-tune: [__phaseshift~__](../objects/phaseshift~.md) `phaseshift~` is a 2nd allpass filter, which keeps the gain and only alters the phase from 0 (at 0 hz) to 360º (at the Nyquist frequency).

- :material-tune: [__lag~__](../objects/lag~.md) `lag~` is a one pole filter that creates an exponential glide/portamento for its signal input changes.

- :material-tune: [__phaser~__](../objects/phaser~.md) `phaser~` is a mono phaser effect abstraction.

- :material-tune: [__slide~__](../objects/slide~.md) `slide~` filters an input signal logarithmically between changes in signal value.

- :material-tune: [__resonator2~__](../objects/resonator2~.md) `resonator2~` is a wrap around `cpole~`.

- :material-tune: [__bitand~__](../objects/bitand~.md) `bitand~` compares the bits of two values with "Bitwise-AND" (bits are set to 1 if both are "1", 0 otherwise).

- :material-tune: [__crusher~__](../objects/crusher~.md) `crusher~` is a bit-crusher/reducer and decimator abstraction based on the objects `quantizer~` (mode 4) and `downsample~`, where an input signal quantized and downsampled to generate distortion and aliasing.

- :material-tune: [__deltaclip~__](../objects/deltaclip~.md) `deltaclip~` limits the change between samples in an incoming signal.

- :material-tune: [__allpass.filt~__](../objects/allpass.filt~.md) `allpass.filt~` is an allpass filter that you can set its order with the first argument (needs to be a multiple of 2).

- :material-tune: [__filterdelay~__](../objects/filterdelay~.md) `filterdelay~` is a high level delay unit that goes thgouh a resonant lowpass filter, a soft clipper and a DC filter.

- :material-tune: [__bicoeff__](../objects/bicoeff.md) `bicoeff` is a GUI that generates coefficients for vanilla's `biquad~` according to different filter types ("eq" filter by default as in the example below).

- :material-tune: [__revdelay~__](../objects/revdelay~.md) `revdelay~` is a reverse delay effect.

- :material-tune: [__resonbank2~__](../objects/resonbank2~.md) `resonbank2~` is a bank of resonators made of `resonator2~` objects.

- :material-tune: [__bpbank~__](../objects/bpbank~.md) `bpbank~` is a bank made of `bandpass~` objects.

- :material-tune: [__decay~__](../objects/decay~.md) `decay~` is based on SuperCollider's "Decay" UGEN.

- :material-tune: [__svf~__](../objects/svf~.md) `svf~` implements Chamberlin's state-variable filter algorithm, which outputs lowpass, highpass, bandpass, and band reject (notch) simultaneously in parallel (in this order from left to right).
.

- :material-tune: [__bitsafe~__](../objects/bitsafe~.md) `bitsafe~` replaces NaN (not a number) and +/- infinity values of an incoming signal with zero, which is useful in conjunction with the bitwise operators in cyclone or any other situation where these values are possible.

- :material-tune: [__conv~__](../objects/conv~.md) `conv~` performs partitioned convolution.

</div>