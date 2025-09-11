# Stochastic

<div class="grid cards" markdown>

- :material-tune: [__chance~__](chance~.md) The `chance~` object probabilistically routes an incoming bang to one of its outlets based on a set of weighted chances.
- :material-tune: [__lfnoise~__](lfnoise~.md) The `lfnoise~` object generates band-limited low-frequency noise, producing random values between -1 and 1 at a specified frequency.
- :material-tune: [__white~__](white~.md) The `white~` object generates white noise using a pseudo-random number generator.
- :material-tune: [__grain.live~__](grain.live~.md) `grain.live~` is a live input granulator that generates clouds of audio grains from an incoming signal.
- :material-tune: [__lfnoise__](lfnoise.md) `lfnoise` is a control-rate low-frequency noise generator that outputs random values between 0 and 127.
- :material-tune: [__ikeda~__](ikeda~.md) The `ikeda~` object is a chaotic signal generator based on the Ikeda map, producing two audio outputs.
- :material-tune: [__drunkard__](drunkard.md) The `drunkard` object generates a sequence of pseudo-random numbers based on a drunkard's walk algorithm.
- :material-tune: [__standard~__](standard~.md) `standard~` is a chaotic signal generator based on the standard map equations.
- :material-tune: [__gray~__](gray~.md) The `gray~` object generates a unique type of noise based on "gray code" (reflected binary code), which results from flipping random bits using a pseudo-random number generator.
- :material-tune: [__dust~__](dust~.md) `dust~` generates random positive impulses at a specified density, based on SuperCollider's "Dust" UGEN.
- :material-tune: [__urn__](urn.md) The `urn` object is a unique random number generator.
- :material-tune: [__oscnoise~__](oscnoise~.md) `oscnoise~` is an oscillator that generates a white noise waveform, which can be updated by a bang message.
- :material-tune: [__noisi~__](noisi~.md) The `noisi~` object generates bandlimited noise by drawing random numbers at a specified rate in Hz and interpolating between them.
- :material-tune: [__lincong~__](lincong~.md) The `lincong~` object is a chaotic signal generator based on a linear congruential difference equation.
- :material-tune: [__drunk__](drunk.md) The `drunk` object generates a "drunk walk" sequence of random numbers.
- :material-tune: [__rand.f~__](rand.f~.md) The `rand.f~` object generates random floating-point values within a specified range.
- :material-tune: [__decide__](decide.md) The `decide` object randomly outputs either 0 or 1.
- :material-tune: [__rand.hist__](rand.hist.md) The `rand.hist` object generates weighted random numbers based on a user-defined histogram, which dictates the probability of each index being output.
- :material-tune: [__brown~__](brown~.md) `brown~` is a brown noise generator, also known as Brownian or red noise, which produces a signal whose spectral energy drops 6dB per octave.
- :material-tune: [__scramble__](scramble.md) The `scramble` object reorders the elements of an input message.
- :material-tune: [__drunkard~__](drunkard~.md) The `drunkard~` object generates a random walk signal, stepping within a defined range from its previous output.
- :material-tune: [__rand.f__](rand.f.md) The `rand.f` object generates pseudo-random floating-point numbers within a user-defined range when triggered by a `bang`.
- :material-tune: [__brown__](brown.md) The `brown` object generates control signals based on a bounded Brownian motion, which is a pseudo-random walk.
- :material-tune: [__prob__](prob.md) The `prob` object generates a weighted series of random numbers, functioning as a 1st-order Markov chain.
- :material-tune: [__rampnoise~__](rampnoise~.md) The `rampnoise~` object generates band-limited noise by interpolating between random values, producing "random ramps" within a specified frequency range.
- :material-tune: [__gendyn~__](gendyn~.md) The `gendyn~` object generates audio using Dynamic Stochastic Synthesis, based on Xenakis' 'GenDyn' algorithm.
- :material-tune: [__randpulse~__](randpulse~.md) `randpulse~` is a random pulse train oscillator that generates an audio signal alternating between a random value and zero.
- :material-tune: [__rampnoise__](rampnoise.md) The `rampnoise` object generates control-rate ramp noise, producing a pseudo-random waveform within the 0-127 range, making it suitable for MIDI control.
- :material-tune: [__randpulse__](randpulse.md) The `randpulse` object is a random pulse oscillator that alternates between a random value and zero at a control rate.
- :material-tune: [__stepnoise__](stepnoise.md) The `stepnoise` object generates control-rate stepped random values, typically within the 0-127 range, without requiring the DSP to be on.
- :material-tune: [__stepnoise~__](stepnoise~.md) The `stepnoise~` object generates band-limited noise with random, stepped values between -1 and 1.
- :material-tune: [__rand.u__](rand.u.md) The `rand.u` object generates a sequence of unrepeated random integer values within a specified range (0 to `size-1`).
- :material-tune: [__rand.list__](rand.list.md) The `rand.list` object selects a random element from a given list of floats.
- :material-tune: [__pix_noise__](pix_noise.md) The `pix_noise` object generates a uniform noise image, with adjustable width and height.
- :material-tune: [__tempo~__](tempo~.md) The `tempo~` object functions as a metronome, generating impulses at a specified tempo in BPM, milliseconds, or Hertz.
- :material-tune: [__dust2~__](dust2~.md) The `dust2~` object generates random impulses (values between -1 and 1) at random times, controlled by a density parameter.
- :material-tune: [__randpulse2__](randpulse2.md) `randpulse2` is a random pulse train oscillator that generates pulses (0 or 1, or random values between -1 and 1) at random intervals.
- :material-tune: [__noish~__](noish~.md) The `noish~` object generates bandlimited noise by drawing a random number every `n` samples and interpolating between these values.
- :material-tune: [__perlin~__](perlin~.md) The `perlin~` object generates 1-dimensional Perlin noise, producing a smoothly varying signal based on a specified frequency in Hertz.
- :material-tune: [__pvgrain~__](pvgrain~.md) `pvgrain~` is a spectral granulator that tracks an input sound and synthesizes grains based on its spectral characteristics.
- :material-tune: [__rand.dist__](rand.dist.md) The `rand.dist` object generates random numbers based on a user-defined probability density function (PDF) provided by a Pure Data array.
- :material-tune: [__rand.i~__](rand.i~.md) The `rand.i~` object generates random integer values within a specified range, triggered by signal transitions.
- :material-tune: [__disarrain~__](disarrain~.md) The `disarrain~` object functions as a spectrum scrambler, reordering a specified number of frequency bins within an audio signal.
- :material-tune: [__crackle~__](crackle~.md) The `crackle~` object generates noise using a chaotic difference equation.
- :material-tune: [__velvet~__](velvet~.md) `velvet~` is a velvet noise generator that produces audio by randomly choosing positive (1) or negative (-1) impulses at random positions within a specified frequency period.
- :material-tune: [__pink~__](pink~.md) The `pink~` object generates pink noise, an audio signal characterized by constant power per octave, with its energy decreasing by 3dB per octave.
- :material-tune: [__rand~__](rand~.md) `rand~` generates random values between -1 and 1 at a given frequency, linearly interpolating between these values to produce a bandlimited noise signal.
- :material-tune: [__chance__](chance.md) The `chance` object outputs a bang to one of its outlets based on a weighted probability distribution.
- :material-tune: [__rand.i__](rand.i.md) The `rand.i` object generates pseudo-random integer values within a specified numerical range.
- :material-tune: [__randpulse2~__](randpulse2~.md) `randpulse2~` is a random pulse train oscillator that generates signals at random intervals, with the average frequency controlled by a "density" parameter.

</div>