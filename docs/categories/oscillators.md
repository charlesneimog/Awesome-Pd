<div class="grid cards" markdown>
- :material-tune: [__xmod2~__](../objects/xmod2~.md) `xmod2~` performs is a variant of `xmod~`, but only performs frequency modulation (so far) and uses a different and cheap sine waveform that promotes more chaotic and cool sounds.
.

- :material-tune: [__lfnoise~__](../objects/lfnoise~.md) `lfnoise~` is a low frequency (band limited) noise with or without interpolation.

- :material-tune: [__click~__](../objects/click~.md) `click~` generates an impulse when receiving a bang.

- :material-tune: [__wt2d~__](../objects/wt2d~.md) `wt2d~` is an interpolating wavetable oscillator like `wt~`, but besides a horizontal dimension, it can also scan through a vertical dimension of a sliced wavetable.

- :material-tune: [__cosine~__](../objects/cosine~.md) `cosine~` is a cosine oscillator that accepts negative frequencies, has inlets for phase sync and phase modulation.

- :material-tune: [__retune__](../objects/retune.md) `retune` receives a scale as a list of steps in cents and a base MIDI pitch value (default 60).

- :material-tune: [__bl.tri~__](../objects/bl.tri~.md) `bl.tri~` is a triangle oscillator like `else/tri~`, but it is bandlimited.

- :material-tune: [__bl.imp2~__](../objects/bl.imp2~.md) `bl.imp2~` is a two sided impulse oscillator like `else/imp2~`, but it is bandlimited.
.

- :material-tune: [__vibrato~__](../objects/vibrato~.md) `vibrato~` is a pitch shifter abstraction with an LFO controlling the pitch deviation in cents.
.

- :material-tune: [__vsaw~__](../objects/vsaw~.md) `vsaw~` is a variable sawtooth waveform oscillator that also becomes a triangular osccilator.

- :material-tune: [__oscnoise~__](../objects/oscnoise~.md) `oscnoise~` is an oscillator that accepts negative frequencies, has inlets for phase sync and phase modulation.

- :material-tune: [__sfont~__](../objects/sfont~.md) `sfont~` is a sampler synthesizer that plays SoundFont files.

- :material-tune: [__damp.osc~__](../objects/damp.osc~.md) `damp.osc~` is an abstraction based `reonant2~` and also very very similar to it (to the point I think it wasn't worth having two objects with such subtle differences).

- :material-tune: [__parabolic~__](../objects/parabolic~.md) `parabolic~` is a parabolic oscillator that accepts negative frequencies, has inlets for phase sync and and phase modulation.

- :material-tune: [__wavetable~__](../objects/wavetable~.md) `wavetable~` is an interpolating wavetable oscillator like `tabosc4~`, but has more features like more interpolation options, inlets for phase sync, phase modulation and also an inlet for scanning through slices.

- :material-tune: [__bl.wavetable~__](../objects/bl.wavetable~.md) `bl.wavetable~` is a bandlimited wavetable oscillator abstraction that uses the upsampling/filtering techniquelike, which makes the object quite inefficient CPU wise.

- :material-tune: [__oscbank~__](../objects/oscbank~.md) `oscbank~` is a bank made of `sine~` objects.

- :material-tune: [__nyquist~__](../objects/nyquist~.md) `nyquist~` reports the nyquist (which is half the sample rate) as a frequency or period.

- :material-tune: [__trapezoid~__](../objects/trapezoid~.md) `trapezoid~` is a trapezoidal wavetable that is read with phase values from 0 to 1 into the first inlet, so a `phasor~` input turns it into a wavetable oscillator.

- :material-tune: [__mono~__](../objects/mono~.md) `mono~` emulates monophonic synth behaviour and is much like `mono`, but can also glide the pitch output with a portamento setting.
.

- :material-tune: [__bl.saw2~__](../objects/bl.saw2~.md) `bl.saw2~` is a sawtooth oscillator like `else/saw2~`, but it is bandlimited.

- :material-tune: [__bl.saw~__](../objects/bl.saw~.md) `bl.saw~` is a sawtooth oscillator like `else/saw~`, but it is bandlimited.

- :material-tune: [__pimpmul~__](../objects/pimpmul~.md) `pimpmul~` is a "pimp~" multiplier.

- :material-tune: [__brown~__](../objects/brown~.md) `brown~` is a brown noise generator (aka brownian noise or red noise), whose spectral energy drops 6dB per octave (sounding less hissy than white noise).

- :material-tune: [__phaseseq~__](../objects/phaseseq~.md) `phaseseq~` takes a list of thresholds and outputs impulses when reaching the threshold values.
.

- :material-tune: [__envelope~__](../objects/envelope~.md) `envelope~` provides 6 different envelopes, which are generated via a phase input.
.

- :material-tune: [__gaussian~__](../objects/gaussian~.md) `gaussian~` is a gaussian oscillator.

- :material-tune: [__plaits~__](../objects/plaits~.md) `plaits~` is a Pure Data external based on the "Plaits" macro-oscillator module by Mutable Instruments.

- :material-tune: [__xmod~__](../objects/xmod~.md) `xmod~` performs cross modulation of two sine oscillators.

- :material-tune: [__resonator2~__](../objects/resonator2~.md) `resonator2~` is a wrap around `cpole~`.

- :material-tune: [__ramp~__](../objects/ramp~.md) `ramp~` is a resettable linear ramp between a minimum and maximum value.

- :material-tune: [__hz2rad__](../objects/hz2rad.md) `hz2rad` converts a frequency in Hertz to "Radians per Sample" - which depends on the patch's sample rate (sr).

- :material-tune: [__lfo__](../objects/lfo.md) `lfo` is a control rate LFO with some common waveforms.
.

- :material-tune: [__voices~__](../objects/voices~.md) `voices~` is an abstraction based on `voices` and generates multichannel signals that can be used to control pitch and gate with polyphony.
.

- :material-tune: [__cycle~__](../objects/cycle~.md) `cycle~` is a linear interpolating oscillator* that reads repeatedly through one cycle of a waveform.

- :material-tune: [__synth~__](../objects/synth~.md) `synth~` is multichannel aware and can send a multichannel signal out with the '-mc' flag or message.
.

- :material-tune: [__randpulse~__](../objects/randpulse~.md) `randpulse~` is a random pulse train oscillator (which alternates between a random value and 0, or on/off).

- :material-tune: [__square~__](../objects/square~.md) `square~` is a square oscillator that accepts negative frequencies, has inlets for pulse width, phase sync and phase modulation.

- :material-tune: [__stepnoise~__](../objects/stepnoise~.md) `stepnoise~` is a low frequency (band limited) noise generator without interpolation, therefore it holds at a random value, resulting in random steps.

- :material-tune: [__fm~__](../objects/fm~.md) `fm~` is a simple frequency modulation unit consisting of a pair of sinusoidal oscillators, where one modulates the frequency input of another.

- :material-tune: [__bl.vsaw~__](../objects/bl.vsaw~.md) `bl.vsaw~` is a variable sawtooth waveform oscillator that also becomes a triangular osccilator just like `else/vsaw~`, but it is bandlimited.

- :material-tune: [__triangle~__](../objects/triangle~.md) `triangle~` is a triangular wavetable that is read with phase values from 0 to 1 into the first inlet- a `phasor~` input turns it into a wavetable oscillator.

- :material-tune: [__train~__](../objects/train~.md) `train~` generates a pulse signal alternating from on (1) to off (0) at a period given in ms.

- :material-tune: [__pulse~__](../objects/pulse~.md) `pulse~` is a pulse train oscillator (alternates between 1 and 0, or on/off) that accepts negative frequencies, has inlets for pulse width, phase sync and phase modulation.

- :material-tune: [__pm~__](../objects/pm~.md) `pm~` is a very basic and simple phase modulation unit, which consists of a pair of sinusoidal oscillators, where one modulates the phase input of another.

- :material-tune: [__scope~__](../objects/scope~.md) `scope~` displays signals in the style of an oscilloscope.

- :material-tune: [__blip~__](../objects/blip~.md) `blip~` uses DSF (Discrete-Summation Formulae) to generate waveforms as a sum of cosines.

- :material-tune: [__tri~__](../objects/tri~.md) `tri~` is a triangular wave oscillator that accepts negative frequencies, has inlets for phase sync and phase modulation.

- :material-tune: [__bl.square~__](../objects/bl.square~.md) `bl.square~` is a square oscillator like `else/square~`, but it is bandlimited.

- :material-tune: [__resonbank2~__](../objects/resonbank2~.md) `resonbank2~` is a bank of resonators made of `resonator2~` objects.

- :material-tune: [__stretch.shift~__](../objects/stretch.shift~.md) `stretch.shift~` is like `gran.player~`, but for live input.

- :material-tune: [__fbsine~__](../objects/fbsine~.md) `fbsine~` is a sinusoidal oscillator with phase modulation feedback.

- :material-tune: [__saw~__](../objects/saw~.md) `saw~` is a sawtooth wave oscillator that accepts negative frequencies, has inlets for phase sync and phase modulation.

- :material-tune: [__saw2~__](../objects/saw2~.md) `saw2~` is a sawtooth wave oscillator that accepts negative frequencies, has inlets for phase sync and phase modulation.

- :material-tune: [__sine~__](../objects/sine~.md) `sine~` is a sinusoidal oscillator that accepts negative frequencies, has inlets for phase sync and phase modulation.

- :material-tune: [__pink~__](../objects/pink~.md) `pink~` is a pink noise generator, which sounds less hissy than white noise (but not as less as brown~).

- :material-tune: [__pimp~__](../objects/pimp~.md) `pimp~` is very convenient for both driving a process with its phase output (such as reading a sample or envelope) and also triggering at period transitions other objects or processes (such as with `sh~` below).
.

- :material-tune: [__freeze~__](../objects/freeze~.md) `freeze~` is an abstraction based on `sigmund~` (analysis & ressynthesis).

- :material-tune: [__bl.osc~__](../objects/bl.osc~.md) `bl.osc~` is a bandlimited oscillator based on `else/wavetable~`.

- :material-tune: [__rm~__](../objects/rm~.md) `rm~` is a Ring Modulation abstraction.

- :material-tune: [__randpulse2~__](../objects/randpulse2~.md) `randpulse2~` is a random pulse train oscillator.

- :material-tune: [__bitshift~__](../objects/bitshift~.md) `bitshift~` can produce NaNs and +/-INFs - but denormals are zeroed out.

</div>