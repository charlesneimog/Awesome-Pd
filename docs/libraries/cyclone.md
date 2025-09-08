---
search:
    exclude: true
---

# cyclone
`Cyclone` is a library for Pure Data (Pd) that provides objects mimicking those in Max/MSP.
It started as a Max 4.0 clone and has evolved, with updates closer to Max 7.
`Cyclone` is mainly maintained for bug fixes and backward compatibility, with some objects replaced or supplemented by the `ELSE` library in PlugData.
It allows building Max-like patches in Pd, but some newer Max features are not included.
<h2>Contributors</h2>

<div id="libcontributors"></div>

<p align="center">
<i>People who contribute to this project.</i>
</p>


<script>
async function updateList() {
    const repoOwner = 'porres';
    const repoName = 'pd-cyclone';
    try {
        const res = await fetch(`https://api.github.com/repos/${repoOwner}/${repoName}/contributors`);
        const contributors = await res.json();
        const container = document.getElementById('libcontributors');
        contributors.forEach(user => {
            const link = document.createElement('a');
            link.href = `https://github.com/${user.login}`;
            link.target = '_blank';
            const img = document.createElement('img');
            img.src = `https://github.com/${user.login}.png?size=100`;
            img.alt = user.login;
            img.className = 'libavatar';
            link.appendChild(img);
            container.appendChild(link);
        });
    } catch(err) {
        console.error(err);
    }
}
updateList();
</script>


<h2>Objects</h2>

<div class="grid cards" markdown>
- :material-tune: [__anal__](../objects/anal.md) `anal` reports how many times it received a number pair.
- :material-tune: [__bitand~__](../objects/bitand~.md) `bitand~` compares the bits of two values with "Bitwise-AND" (bits are set to 1 if both are "1", 0 otherwise).
- :material-tune: [__bitsafe~__](../objects/bitsafe~.md) `bitsafe~` replaces NaN (not a number) and +/- infinity values of an incoming signal with zero, which is useful in conjunction with the bitwise operators in cyclone or any other situation where these values are possible.
- :material-tune: [__bitshift~__](../objects/bitshift~.md) `bitshift~` can produce NaNs and +/-INFs - but denormals are zeroed out.
- :material-tune: [__buffer~__](../objects/buffer~.md) `buffer~` stores audio in a memory buffer (an array).
- :material-tune: [__click~__](../objects/click~.md) `click~` generates an impulse when receiving a bang.
- :material-tune: [__coll__](../objects/coll.md) `coll` stores/edits any messages at given addresses (an integer or a symbol).
- :material-tune: [__cycle~__](../objects/cycle~.md) `cycle~` is a linear interpolating oscillator* that reads repeatedly through one cycle of a waveform.
- :material-tune: [__deltaclip~__](../objects/deltaclip~.md) `deltaclip~` limits the change between samples in an incoming signal.
- :material-tune: [__grab__](../objects/grab.md) `grab` sets the value of GUIs but also grabs its ouotput.
- :material-tune: [__greaterthan~__](../objects/greaterthan~.md) `greaterthan~` or `>~` outputs a 1 signal when the left input is greater-than the right input or argument and a 0 when it is less-than or equal-to the right input or argument.
.
- :material-tune: [__histo__](../objects/histo.md) `histo` records how many times it received a positive integer (no floats allowed).
- :material-tune: [__lores~__](../objects/lores~.md) `lores~` implements an inexpensive resonant lowpass filter.
- :material-tune: [__matrix~__](../objects/matrix~.md) `matrix~` routes signals from any inlets to one or more outlets.
- :material-tune: [__maximum__](../objects/maximum.md) `maximum` outputs the maximum of two or more values.
- :material-tune: [__minimum__](../objects/minimum.md) `minimum` outputs the minimum of two or more values.
- :material-tune: [__mtr__](../objects/mtr.md) `mtr` records any messages in different tracks and plays them back.
- :material-tune: [__offer__](../objects/offer.md) `offer` stores a x/y integer number pair and accesses the 'y' value from the corresponding 'x' (after retrieving, the pair is deleted).
.
- :material-tune: [__peak__](../objects/peak.md) `peak` compares the input to a 'peak' (maximum) value.
- :material-tune: [__phaseshift~__](../objects/phaseshift~.md) `phaseshift~` is a 2nd allpass filter, which keeps the gain and only alters the phase from 0 (at 0 hz) to 360º (at the Nyquist frequency).
- :material-tune: [__prepend__](../objects/prepend.md) `prepend` will add messages set as argument to the beginning of any message sent to the input.
- :material-tune: [__rampsmooth~__](../objects/rampsmooth~.md) `rampsmooth~` smooths a signal across 'n' samples.
- :material-tune: [__record~__](../objects/record~.md) `record~` records up to 64 signal channels into arrays.
- :material-tune: [__round__](../objects/round.md) `round` approximates positive and negative numbers to an integer multiple of any given number that is greater or equal to 0 (0 makes no approximation, so the original input is output unchanged).
.
- :material-tune: [__round~__](../objects/round~.md) `round~` approximates positive and negative numbers to an integer multiple of any given number that is greater or equal to 0 (0 makes no approximation - so the original input is output unchanged).
.
- :material-tune: [__sampstoms~__](../objects/sampstoms~.md) `sampstoms~` works with floats and signal.
- :material-tune: [__scale__](../objects/scale.md) `scale` maps an input range to an output range.
- :material-tune: [__slide~__](../objects/slide~.md) `slide~` filters an input signal logarithmically between changes in signal value.
- :material-tune: [__spell__](../objects/spell.md) `spell` takes any message and converts each containing digit and character to UTF-8 (Unicode) values (`spell` doesn't understand non-integer float messages).
- :material-tune: [__substitute__](../objects/substitute.md) `substitute` will replace all recurring elements in a message, but if you have a 3rd argument, it operates in "first only" mode, where only the first element is replaced.
.
- :material-tune: [__svf~__](../objects/svf~.md) `svf~` implements Chamberlin's state-variable filter algorithm, which outputs lowpass, highpass, bandpass, and band reject (notch) simultaneously in parallel (in this order from left to right).
.
- :material-tune: [__table__](../objects/table.md) `table` stores and edits a number array.
- :material-tune: [__togedge__](../objects/togedge.md) `togedge` sends a bang in the left outlet for "zero to non-zero" transitions, and a bang in the right outlet for "non-zero to zero" transitions.
.
- :material-tune: [__train~__](../objects/train~.md) `train~` generates a pulse signal alternating from on (1) to off (0) at a period given in ms.
- :material-tune: [__trapezoid~__](../objects/trapezoid~.md) `trapezoid~` is a trapezoidal wavetable that is read with phase values from 0 to 1 into the first inlet, so a `phasor~` input turns it into a wavetable oscillator.
- :material-tune: [__triangle~__](../objects/triangle~.md) `triangle~` is a triangular wavetable that is read with phase values from 0 to 1 into the first inlet- a `phasor~` input turns it into a wavetable oscillator.
- :material-tune: [__trough__](../objects/trough.md) `trough` compares the input to a 'trough' (minimum) value.
- :material-tune: [__urn__](../objects/urn.md) `urn` generates random numbers in a range defined by the 'n' size (from 0 to n-1) without repeating them.
- :material-tune: [__wave~__](../objects/wave~.md) `wave~`'s input phase varies between 0 and 1, which in 32-bit floating point arithmetic has 24 bits of index resolution.
- :material-tune: [__zl__](../objects/zl.md) `zl` processes messages with one or more elements ("list messages' or "anything") according to a mode set via argument/message or in the object name after a `.` (dot)..
</div>