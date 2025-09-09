<div class="grid cards" markdown>
- :material-tune: [__biquads~__](../objects/biquads~.md) `biquads~` is a series of biquad filters in cascade.
.

- :material-tune: [__resonant~__](../objects/resonant~.md) `resonant~` is a bandpass resonator filter like `bandpass~`, but it doesn't have a maximum dB value of 0, so changing the Q increases the gain of the filter.

- :material-tune: [__vsaw~__](../objects/vsaw~.md) `vsaw~` is a variable sawtooth waveform oscillator that also becomes a triangular osccilator.

- :material-tune: [__bl.wavetable~__](../objects/bl.wavetable~.md) `bl.wavetable~` is a bandlimited wavetable oscillator abstraction that uses the upsampling/filtering techniquelike, which makes the object quite inefficient CPU wise.

- :material-tune: [__trapezoid~__](../objects/trapezoid~.md) `trapezoid~` is a trapezoidal wavetable that is read with phase values from 0 to 1 into the first inlet, so a `phasor~` input turns it into a wavetable oscillator.

- :material-tune: [__mono~__](../objects/mono~.md) `mono~` emulates monophonic synth behaviour and is much like `mono`, but can also glide the pitch output with a portamento setting.
.

- :material-tune: [__resonator~__](../objects/resonator~.md) `resonator~` is just like `resonant~`, but the resonance parameter is defined as resonance time in 't60'.

- :material-tune: [__xmod~__](../objects/xmod~.md) `xmod~` performs cross modulation of two sine oscillators.

- :material-tune: [__square~__](../objects/square~.md) `square~` is a square oscillator that accepts negative frequencies, has inlets for pulse width, phase sync and phase modulation.

- :material-tune: [__triangle~__](../objects/triangle~.md) `triangle~` is a triangular wavetable that is read with phase values from 0 to 1 into the first inlet- a `phasor~` input turns it into a wavetable oscillator.

- :material-tune: [__pm~__](../objects/pm~.md) `pm~` is a very basic and simple phase modulation unit, which consists of a pair of sinusoidal oscillators, where one modulates the phase input of another.

- :material-tune: [__fbsine~__](../objects/fbsine~.md) `fbsine~` is a sinusoidal oscillator with phase modulation feedback.

- :material-tune: [__saw~__](../objects/saw~.md) `saw~` is a sawtooth wave oscillator that accepts negative frequencies, has inlets for phase sync and phase modulation.

- :material-tune: [__rm~__](../objects/rm~.md) `rm~` is a Ring Modulation abstraction.

</div>