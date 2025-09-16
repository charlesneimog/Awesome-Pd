---
search:
    exclude: true
---

# cyclone
`Cyclone` is a library for Pure Data (Pd) that provides objects mimicking those in Max/MSP. It started as a Max 4.0 clone and has evolved, with updates closer to Max 7. `Cyclone` is mainly maintained for bug fixes and backward compatibility, with some objects replaced or supplemented by the `ELSE` library in PlugData. It allows building Max-like patches in Pd, but some newer Max features are not included.
<h2>Contributors</h2>

<div id="libcontributors"></div>

<p align="center">
<i>People who contribute to this project.</i>
</p>

<script>
async function updateList() {
    let repoOwner = 'porres';
    let repoName = 'pd-cyclone';
    try {
        let res = await fetch(`https://api.github.com/repos/${repoOwner}/${repoName}/contributors`);
        let contributors = await res.json();
        let container = document.getElementById('libcontributors');
        contributors.forEach(user => {
            let link = document.createElement('a');
            link.href = `https://github.com/${user.login}`;
            link.target = '_blank';
            let img = document.createElement('img');
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
- :material-tune: [__accum__](../objects/general_utilities/accum.md) The `accum` object maintains an internal numerical value, which can be initialized or set at any time.
- :material-tune: [__acos__](../objects/math/acos.md) The `acos` object calculates the arc-cosine (inverse cosine) of a given number.
- :material-tune: [__acosh__](../objects/math/acosh.md) The `acosh` object calculates the hyperbolic arc-cosine of a given floating-point number.
- :material-tune: [__acosh~__](../objects/math/acosh~.md) The `acosh~` object calculates the hyperbolic arc-cosine of an incoming signal, sample by sample.
- :material-tune: [__acos~__](../objects/math/acos~.md) The `acos~` object calculates the arc-cosine of an incoming signal, sample by sample.
- :material-tune: [__active__](../objects/general_utilities/active.md) The `active` object outputs `1` when its parent patch canvas is the active, front-most window, and `0` when it is inactive.
- :material-tune: [__allpass~__](../objects/filters/allpass~.md) The `allpass~` object implements an all-pass filter, which passes all frequencies without altering their gain but changes their phase.
- :material-tune: [__anal__](../objects/statistical_models/anal.md) The `anal` object calculates and stores transition probabilities between sequences of numbers, primarily for implementing Markov Chains.
- :material-tune: [__append__](../objects//append.md) The `append` object concatenates a predefined message, set as an argument, to the end of any incoming message, outputting the combined result.
- :material-tune: [__asin__](../objects/math/asin.md) The `asin` object calculates the arc-sine of a given float input.
- :material-tune: [__asinh__](../objects/math/asinh.md) The `asinh` object calculates the hyperbolic arc-sine of a given floating-point number.
- :material-tune: [__asinh~__](../objects/math/asinh~.md) The `asinh~` object computes the hyperbolic arc-sine of an incoming audio signal, sample by sample.
- :material-tune: [__asin~__](../objects/math/asin~.md) The `asin~` object calculates the arc-sine of each input audio sample.
- :material-tune: [__atan2~__](../objects/math/atan2~.md) The `atan2~` object calculates the arc-tangent of two signal-rate input values, 'a' and 'b', as `atan(a/b)`.
- :material-tune: [__atanh__](../objects/math/atanh.md) The `atanh` object calculates the hyperbolic arc-tangent of a given float input.
- :material-tune: [__atanh~__](../objects/math/atanh~.md) The `atanh~` object calculates the hyperbolic arc-tangent of an incoming signal.
- :material-tune: [__atan~__](../objects/math/atan~.md) The `atan~` object calculates the arc-tangent of each incoming audio sample.
- :material-tune: [__atodb__](../objects/math/atodb.md) The `atodb` object converts linear amplitude values to their decibel full scale (dBFS) equivalents.
- :material-tune: [__atodb~__](../objects/math/atodb~.md) The `atodb~` object converts a linear amplitude signal to its equivalent in decibels full scale (dBFS).
- :material-tune: [__average~__](../objects/math/average~.md) `average~` calculates a moving average of an audio signal over a specified number of recent samples.
- :material-tune: [__avg~__](../objects/math/avg~.md) The `avg~` object calculates the absolute average of an input signal.
- :material-tune: [__bangbang__](../objects/general_utilities/bangbang.md) The `bangbang` object emits multiple bang messages from its outlets in right-to-left order whenever it receives any input.
- :material-tune: [__bitand~__](../objects/logic/bitand~.md) The `bitand~` object performs a bitwise AND operation on two input signals or a signal and a given bitmask.
- :material-tune: [__bitnot~__](../objects/logic/bitnot~.md) `bitnot~` performs a bitwise NOT operation (one's complement) on an incoming signal.
- :material-tune: [__bitor~__](../objects/logic/bitor~.md) The `bitor~` object performs a bitwise OR operation on two 32-bit values, either two audio signals or an audio signal and a bitmask.
- :material-tune: [__bitsafe~__](../objects/general_utilities/bitsafe~.md) The `bitsafe~` object replaces NaN (Not a Number) and infinity values in an incoming signal with zero.
- :material-tune: [__bitshift~__](../objects//bitshift~.md) The `bitshift~` object performs bitwise left or right shifts on an incoming audio signal.
- :material-tune: [__bitxor~__](../objects/logic/bitxor~.md) The `bitxor~` object performs a bitwise exclusive OR (XOR) operation on two audio signals, or between an audio signal and a 32-bit integer bitmask.
- :material-tune: [__bondo__](../objects/routing/bondo.md) The `bondo` object synchronizes and routes messages in Pure Data.
- :material-tune: [__borax__](../objects/midi/borax.md) The `borax` object processes incoming MIDI note and velocity data, providing detailed reports on individual note events.
- :material-tune: [__bucket__](../objects/routing/bucket.md) The `bucket` object acts as a data shifter, passing incoming float values sequentially from one outlet to the next in a rotational pattern.
- :material-tune: [__buddy__](../objects/logic/buddy.md) The `buddy` object synchronizes incoming messages across its inlets, outputting them only when all inlets have received a message.
- :material-tune: [__buffer~__](../objects/samplers/buffer~.md) The `buffer~` object stores and manipulates audio data in memory as a multichannel array, similar to Pd's `table` but with advanced file I/O.
- :material-tune: [__buffir~__](../objects/filters/buffir~.md) The `buffir~` object is a table/buffer-based Finite Impulse Response (FIR) filter that convolves an input signal with samples from a specified buffer.
- :material-tune: [__capture__](../objects/data_structures/capture.md) The `capture` object stores a sequential list of incoming floats and symbols, acting as a data buffer.
- :material-tune: [__capture~__](../objects/file_io/capture~.md) The `capture~` object is a debugging and investigation tool that captures incoming audio signals (`signal`) and stores their samples.
- :material-tune: [__cartopol__](../objects/math/cartopol.md) The `cartopol~` object converts Cartesian coordinates (real and imaginary parts) from signal inputs into polar coordinates (amplitude and phase) as signal outputs.
- :material-tune: [__cartopol~__](../objects/math/cartopol~.md) The `cartopol~` object converts a signal from Cartesian coordinates (real and imaginary parts) to polar coordinates (amplitude and phase).
- :material-tune: [__change~__](../objects/general_utilities/change~.md) The `change~` object detects changes in an incoming audio signal and outputs its direction.
- :material-tune: [__click~__](../objects//click~.md) The `click~` object is an audio impulse generator that outputs a single-sample impulse when triggered by a `bang` message.
- :material-tune: [__clip__](../objects/math/clip.md) The `clip` object (or `cyclone/clip~`) constrains incoming float or list values to a specified numerical range.
- :material-tune: [__clip~__](../objects/math/clip~.md) The `cyclone/clip~` object constrains an input audio signal to a specified minimum and maximum range.
- :material-tune: [__coll__](../objects/data_structures/coll.md) The `coll` object stores and manages collections of messages at integer or symbol addresses.
- :material-tune: [__comb~__](../objects/delay/comb~.md) The `comb~` object implements a comb filter, which can be used for both filtering and delay effects on audio signals.
- :material-tune: [__comment__](../objects/gui/comment.md) The `comment` object is a GUI element in Pure Data used for displaying customizable text labels or notes within a patch.
- :material-tune: [__cosh__](../objects/math/cosh.md) The `cosh` object calculates the hyperbolic cosine of a given floating-point number.
- :material-tune: [__cosh~__](../objects/math/cosh~.md) The `cosh~` object calculates the hyperbolic cosine of an input signal sample by sample.
- :material-tune: [__cosx~__](../objects/math/cosx~.md) The `cosx~` object computes the cosine of an input signal, expecting values in radians.
- :material-tune: [__counter__](../objects/general_utilities/counter.md) The `counter` object increments or decrements an integer value within a specified minimum and maximum range.
- :material-tune: [__count~__](../objects//count~.md) The `count~` object outputs a signal that increments by one for each audio sample, functioning as a sample-accurate counter.
- :material-tune: [__cross~__](../objects/filters/cross~.md) `cross~` is a 3rd order Butterworth crossover filter designed to split an incoming audio signal into lowpass and highpass components.
- :material-tune: [__curve~__](../objects/math/curve~.md) `curve~` generates non-linear, curved ramp signals, offering an exponential curve factor to shape the transition between values.
- :material-tune: [__cycle__](../objects/routing/cycle.md) The `cycle` object distributes incoming messages to its outlets in a round-robin fashion.
- :material-tune: [__cycle~__](../objects/oscillators/cycle~.md) The `cycle~` object is a linear interpolating oscillator that generates a periodic waveform.
- :material-tune: [__cyclone__](../objects/extensions/cyclone.md) The `cyclone` object acts as an interface to the Cyclone library, a collection of common Pure Data objects, often with Max/MSP-compatible alphanumeric aliases.
- :material-tune: [__dbtoa__](../objects/math/dbtoa.md) The `dbtoa` object converts decibel (dBFS) values into their corresponding linear amplitude using the formula `amp = pow(10, dBFS / 20)`.
- :material-tune: [__dbtoa~__](../objects/math/dbtoa~.md) The `dbtoa~` object converts a decibel full scale (dBFS) amplitude signal or float into its linear amplitude equivalent.
- :material-tune: [__decide__](../objects/stochastic/decide.md) The `decide` object randomly outputs either 0 or 1, acting as a simple random boolean generator.
- :material-tune: [__decode__](../objects/routing/decode.md) The `decode` object takes an integer input and activates the corresponding output (0-indexed) by sending a `1`, while all other outputs receive `0`.
- :material-tune: [__degrade~__](../objects/distortion/degrade~.md) The `degrade~` object reduces the quality of an incoming audio signal by manipulating its sampling rate and bit depth.
- :material-tune: [__delay~__](../objects/delay/delay~.md) The `delay~` object delays an audio signal by a specified number of samples, with the delay time dependent on the sample rate.
- :material-tune: [__deltaclip~__](../objects//deltaclip~.md) The `deltaclip~` object limits the rate of change between consecutive samples in an incoming signal, a process also known as 'slew limiting'.
- :material-tune: [__delta~__](../objects/math/delta~.md) The `delta~` object calculates the difference between the current incoming audio sample and the previous sample.
- :material-tune: [__downsamp~__](../objects//downsamp~.md) The `downsamp~` object samples and holds an input signal at a specified rate, expressed in samples, without interpolation.
- :material-tune: [__drunk__](../objects/stochastic/drunk.md) The `drunk` object generates a "drunk walk" sequence of random numbers.
- :material-tune: [__edge~__](../objects//edge~.md) The `edge~` object detects transitions in an audio signal.
- :material-tune: [__equals~__](../objects/logic/equals~.md) The `equals~` (or `==~`) object performs a signal comparison, outputting a signal of 1 when its left inlet signal is equal to its right inlet signal or argument, and 0 otherwise.
- :material-tune: [__flush__](../objects/midi/flush.md) The `flush` object acts as a "panic button" for MIDI notes.
- :material-tune: [__forward__](../objects/routing/forward.md) The `forward` object in Pure Data is designed to send messages to various destinations, allowing the target to change dynamically with each message.
- :material-tune: [__frameaccum~__](../objects//frameaccum~.md) The `frameaccum~` object accumulates the values of incoming signal blocks sample by sample, producing a running sum for each sample position across blocks.
- :material-tune: [__framedelta~__](../objects/math/framedelta~.md) The `framedelta~` object computes the difference between successive signal blocks, specifically designed for running phase deviation in FFT analysis.
- :material-tune: [__fromsymbol__](../objects/text/fromsymbol.md) The `fromsymbol` object converts a Pure Data symbol message into other message types, such as bangs, floats, or lists.
- :material-tune: [__funbuff__](../objects/data_structures/funbuff.md) The `funbuff` object stores and manages ordered pairs of x/y integers, functioning as a lookup table or a simple function buffer.
- :material-tune: [__funnel__](../objects/routing/funnel.md) The `funnel` object collects data from multiple inlets and outputs it through a single outlet, prepending an inlet number to each message.
- :material-tune: [__gate__](../objects/routing/gate.md) The `gate` object routes messages from its second inlet to one of its 'n' specified outlets, or to no outlet if set to 0.
- :material-tune: [__gate~__](../objects/routing/gate~.md) The `gate~` object routes an input signal from its second inlet to one of its 'n' specified outlets, or to none of them.
- :material-tune: [__grab__](../objects/gui/grab.md) The `grab` object sends a message to another object and intercepts its output, routing it through `grab`'s own outlets.
- :material-tune: [__greaterthaneq~__](../objects/logic/greaterthaneq~.md) The `greaterthaneq~` (or `>=~`) object performs a "greater than or equal to" comparison for audio signals.
- :material-tune: [__greaterthan~__](../objects/logic/greaterthan~.md) The `greaterthan~` (or `>~`) object performs a sample-by-sample comparison between two signal inputs.
- :material-tune: [__histo__](../objects/statistical_models/histo.md) The `histo` object records the frequency of received positive integers, creating a histogram.
- :material-tune: [__index~__](../objects/data_structures/index~.md) The `index~` object reads values from an array without interpolation, similar to `tabread~` but with rounded index values.
- :material-tune: [__iter__](../objects//iter.md) The `iter` object splits an incoming message (a list of floats or symbols) into its individual elements.
- :material-tune: [__join__](../objects/data_structures/join.md) The `join` object combines messages of any type from its multiple inlets into a single output list.
- :material-tune: [__kink~__](../objects/distortion/kink~.md) The `kink~` object distorts a `phasor~` signal by applying a non-linear bend or "kink" to its phase.
- :material-tune: [__lessthaneq~__](../objects/logic/lessthaneq~.md) The `lessthaneq~` (or `<=~`) object performs a "less than or equal to" comparison on incoming audio signals.
- :material-tune: [__lessthan~__](../objects/logic/lessthan~.md) The `lessthan~` (or `<~`) object performs a "less than" comparison for audio signals.
- :material-tune: [__linedrive__](../objects/math/linedrive.md) The `linedrive` object scales numbers from one range to another using an exponential curve, similar to `cyclone/scale`.
- :material-tune: [__line~__](../objects/envelopes/line~.md) The `line~` object generates linear signal ramps or envelopes.
- :material-tune: [__listfunnel__](../objects/data_structures/listfunnel.md) The `listfunnel` object receives any list and outputs its elements sequentially, each preceded by its index.
- :material-tune: [__loadmess__](../objects//loadmess.md) The `loadmess` object automatically outputs a predefined message when its containing Pure Data patch is loaded or opened.
- :material-tune: [__lookup~__](../objects/distortion/lookup~.md) The `lookup~` object performs waveshaping distortion by mapping input signal values (from -1 to 1) to indices of an array or table, which acts as a transfer function.
- :material-tune: [__lores~__](../objects/filters/lores~.md) The `lores~` object implements an inexpensive resonant lowpass filter, designed to shape audio signals by attenuating frequencies above a specified cutoff.
- :material-tune: [__match__](../objects/logic/match.md) The `match` object outputs data when its input matches its arguments.
- :material-tune: [__matrix~__](../objects/routing/matrix~.md) The `matrix~` object functions as a signal routing and mixing matrix, enabling dynamic redirection of audio signals from multiple inlets to various outlets.
- :material-tune: [__maximum__](../objects/math/maximum.md) The `maximum` object outputs the greatest value among two or more numbers.
- :material-tune: [__maximum~__](../objects/math/maximum~.md) The `maximum~` object outputs a signal representing the greater of two input signals, or the greater of an input signal and a numerical argument.
- :material-tune: [__mean__](../objects/math/mean.md) The `mean` object calculates a running or moving average of all received numbers.
- :material-tune: [__midiflush__](../objects/midi/midiflush.md) The `midiflush` object acts as a "panic button" for raw MIDI data streams, preventing hanging notes.
- :material-tune: [__midiformat__](../objects/midi/midiformat.md) The `midiformat` object receives various MIDI messages (note on/off, polyphonic aftertouch, control change, program change, channel aftertouch, pitch bend) through its inlets and formats them into a raw MIDI message output.
- :material-tune: [__midiparse__](../objects/midi/midiparse.md) The `midiparse` object receives a raw MIDI data stream and parses it into various MIDI messages, such as note messages, control changes, program changes, and pitch bend.
- :material-tune: [__minimum__](../objects/math/minimum.md) The `minimum` object outputs the smallest value from its inputs.
- :material-tune: [__minimum~__](../objects/math/minimum~.md) The `minimum~` object outputs the smaller of two input signals, or the smaller of an input signal and a numerical argument.
- :material-tune: [__minmax~__](../objects/math/minmax~.md) The `minmax~` object continuously tracks the minimum and maximum amplitude values of an incoming audio signal.
- :material-tune: [__modulo~__](../objects/math/modulo~.md) The `modulo~` (or `%%~`) object is a signal remainder operator.
- :material-tune: [__mousefilter__](../objects/control_io/mousefilter.md) The `mousefilter` object controls the flow of messages based on mouse button activity.
- :material-tune: [__mousestate__](../objects/control_io/mousestate.md) The `mousestate` object reports real-time mouse data, including click status, cursor position (x, y), and movement deltas.
- :material-tune: [__mstosamps~__](../objects/math/mstosamps~.md) The `mstosamps~` object converts a time value in milliseconds into the corresponding number of audio samples, taking the current sample rate into account.
- :material-tune: [__mtr__](../objects/sequencers/mtr.md) The `mtr` object records and plays back sequences of messages across multiple tracks.
- :material-tune: [__next__](../objects/logic/next.md) The `next` object in Pure Data determines if an incoming message belongs to the same "logical event" as the preceding message.
- :material-tune: [__notequals~__](../objects/logic/notequals~.md) The `notequals~` (or `!=~`) object performs a "not equal to" comparison between its left signal input and either its right signal input or a creation argument.
- :material-tune: [__number~__](../objects/gui/number~.md) The `number~` object in Pure Data serves as a dual-purpose GUI element, either monitoring an incoming audio signal's value or generating a ramped signal.
- :material-tune: [__offer__](../objects/data_structures/offer.md) The `offer` object stores temporary `x/y` integer pairs.
- :material-tune: [__onebang__](../objects/logic/onebang.md) The `onebang` object gates incoming bangs, allowing the first bang through its left outlet only after a bang has been received in its right inlet.
- :material-tune: [__onepole~__](../objects/filters/onepole~.md) `onepole~` is a highly efficient one-pole IIR low-pass filter that provides 6dB per octave attenuation.
- :material-tune: [__overdrive~__](../objects/distortion/overdrive~.md) The `overdrive~` object simulates analog tube-based soft clipping, applying a non-linear transfer function to an incoming audio signal to create distortion.
- :material-tune: [__pak__](../objects/data_structures/pak.md) The `pak` object combines multiple inputs of various types (float, int, symbol) into a single list.
- :material-tune: [__past__](../objects/logic/past.md) The `past` object compares an incoming list of numbers against a list of thresholds.
- :material-tune: [__peak__](../objects/math/peak.md) The `peak` object tracks and outputs the highest float value it has received.
- :material-tune: [__peakamp~__](../objects/descriptors/peakamp~.md) The `peakamp~` object reports the absolute peak amplitude of an audio signal since its last output.
- :material-tune: [__peek~__](../objects/data_structures/peek~.md) The `peek~` object provides functionality to read and write individual values to and from arrays in Pure Data.
- :material-tune: [__phaseshift~__](../objects/filters/phaseshift~.md) The `phaseshift~` object is a 2nd order allpass filter that alters the phase of an audio signal without changing its gain.
- :material-tune: [__phasewrap~__](../objects/math/phasewrap~.md) The `phasewrap~` object wraps an input signal's value between -π and π.
- :material-tune: [__pink~__](../objects/stochastic/pink~.md) The `pink~` object generates pink noise, characterized by constant power per octave and a -3dB/octave decrease in spectral power.
- :material-tune: [__play~__](../objects/samplers/play~.md) The `play~` object provides flexible audio playback from arrays, supporting variable speed (including backwards), looping with optional crossfading, and multi-channel output up to 64 channels.
- :material-tune: [__plusequals~__](../objects/math/plusequals~.md) The `plusequals~` (or `+=~`) object is a signal accumulator that continuously sums its input samples, generating a running total.
- :material-tune: [__poke~__](../objects/data_structures/poke~.md) `poke~` writes audio signals or control messages into a specified array at a given index, which can also be controlled by a signal.
- :material-tune: [__poltocar__](../objects/math/poltocar.md) The `poltocar` object converts polar coordinates (amplitude and phase in radians) into cartesian coordinates (real and imaginary parts).
- :material-tune: [__poltocar~__](../objects/math/poltocar~.md) The `poltocar~` object converts signal values from polar coordinates (amplitude and phase) to Cartesian coordinates (real and imaginary parts).
- :material-tune: [__pong__](../objects/math/pong.md) The `pong` object limits input values by folding, wrapping, or clipping them within a specified low-high range.
- :material-tune: [__pong~__](../objects/math/pong~.md) The `pong~` object functions as a signal range limiter, enabling users to fold, wrap, or clip an input signal within a defined low-high range.
- :material-tune: [__pow~__](../objects/math/pow~.md) The `cyclone/pow~` object calculates the power of a base value, raising it to the exponent.
- :material-tune: [__prepend__](../objects/data_structures/prepend.md) The `prepend` object adds a specified message or argument to the beginning of any incoming message.
- :material-tune: [__prob__](../objects/statistical_models/prob.md) The `prob` object generates a weighted series of random numbers based on a first-order Markov chain.
- :material-tune: [__pv__](../objects/data_structures/pv.md) The `pv` object functions as a private variable, storing and retrieving any message type by name within a patch and its subpatches.
- :material-tune: [__rampsmooth~__](../objects/filters/rampsmooth~.md) The `rampsmooth~` object linearly smooths an incoming audio signal over a specified number of samples.
- :material-tune: [__rand~__](../objects/stochastic/rand~.md) The `rand~` object generates an interpolated random noise signal, producing values between -1 and 1 at a specified frequency.
- :material-tune: [__rdiv__](../objects/math/rdiv.md) `rdiv` performs division, similar to the `[/]` object, but with reversed inlet functionality.
- :material-tune: [__rdiv~__](../objects/math/rdiv~.md) The `rdiv~` object performs signal division, similar to `/~`, but with its inlets reversed.
- :material-tune: [__record~__](../objects/multichannel/record~.md) The `record~` object captures incoming audio signals and stores them into one or more Pure Data arrays.
- :material-tune: [__reson~__](../objects/filters/reson~.md) `reson~` is a bandpass resonant filter that processes audio signals.
- :material-tune: [__rminus__](../objects/math/rminus.md) The `rminus` (or `!-`) object performs subtraction with its inlets reversed compared to the standard `[-]` object.
- :material-tune: [__rminus~__](../objects/math/rminus~.md) The `rminus~` (or `!-~`) object performs signal subtraction, similar to `~`, but with its inlets reversed.
- :material-tune: [__round__](../objects/math/round.md) The `round` object approximates input numbers (floats or lists) to the nearest integer multiple of a specified value.
- :material-tune: [__round~__](../objects/math/round~.md) The `round~` object quantizes incoming audio signals to an integer multiple of a specified value.
- :material-tune: [__sah~__](../objects/general_utilities/sah~.md) The `sah~` object samples an input signal when a trigger signal crosses a specified threshold, then holds that sampled value until the trigger crosses the threshold again.
- :material-tune: [__sampstoms~__](../objects/math/sampstoms~.md) The `sampstoms~` object converts a time value from samples to milliseconds, taking the current sample rate into account.
- :material-tune: [__scale__](../objects/math/scale.md) The `scale` object maps an input numerical range to an output numerical range, allowing for inversion and exponential scaling.
- :material-tune: [__scale~__](../objects/math/scale~.md) `scale~` maps an input signal range to an output signal range, allowing for linear, inverted, or exponential scaling.
- :material-tune: [__scope~__](../objects/gui/scope~.md) The `scope~` object visualizes audio signals in the style of an oscilloscope.
- :material-tune: [__selector~__](../objects/routing/selector~.md) `selector~` is an audio object that selects one of its multiple signal inputs to be passed to its output.
- :material-tune: [__seq__](../objects/sequencers/seq.md) The `seq` object plays and records raw MIDI data streams, functioning as a MIDI sequencer.
- :material-tune: [__sinh__](../objects/math/sinh.md) The `sinh` object calculates the hyperbolic sine of a given floating-point number.
- :material-tune: [__sinh~__](../objects/math/sinh~.md) The `sinh~` object calculates the hyperbolic sine of an incoming signal, sample by sample.
- :material-tune: [__sinx~__](../objects/math/sinx~.md) The `sinx~` object calculates the sine of an incoming signal.
- :material-tune: [__slide~__](../objects/filters/slide~.md) The `slide~` object logarithmically smooths an input audio signal, preventing abrupt changes and clicks.
- :material-tune: [__snapshot~__](../objects//snapshot~.md) The `snapshot~` object converts a signal sample to a float value.
- :material-tune: [__speedlim__](../objects/general_utilities/speedlim.md) The `speedlim` object limits the rate at which messages are passed through.
- :material-tune: [__spell__](../objects/text/spell.md) The `spell` object converts incoming messages, including digits and characters, into their corresponding UTF-8 (Unicode) integer values.
- :material-tune: [__spike~__](../objects//spike~.md) The `spike~` object detects zero to non-zero transitions in an audio signal and outputs the time interval in milliseconds since the last detected event.
- :material-tune: [__split__](../objects/routing/split.md) The `split` object routes incoming float numbers to one of two outlets based on whether they fall within a defined minimum and maximum range.
- :material-tune: [__spray__](../objects/routing/spray.md) The `spray` object distributes incoming values to its multiple outlets.
- :material-tune: [__sprintf__](../objects/text/sprintf.md) The `sprintf` object formats messages using C-style `printf` syntax, where each '%' format specifier (e.g., `%f` for float, `%s` for string) creates a corresponding inlet.
- :material-tune: [__substitute__](../objects/general_utilities/substitute.md) The `substitute` object replaces elements within an incoming message.
- :material-tune: [__sustain__](../objects/midi/sustain.md) The `sustain` object emulates a MIDI sustain pedal, holding `noteoff` messages while active and releasing them when deactivated.
- :material-tune: [__svf~__](../objects/filters/svf~.md) The `svf~` object implements a state-variable filter, simultaneously outputting lowpass, highpass, bandpass, and notch filtered signals.
- :material-tune: [__switch__](../objects/logic/switch.md) The `switch` object routes messages from one of its multiple data inlets to a single outlet.
- :material-tune: [__table__](../objects/data_structures/table.md) The `table` object stores and edits a number array, which can be graphically manipulated via an editor window or by double-clicking.
- :material-tune: [__tanh__](../objects/math/tanh.md) The `tanh` object calculates the hyperbolic tangent function of a given number.
- :material-tune: [__tanh~__](../objects/math/tanh~.md) `tanh~` calculates the hyperbolic tangent of an input signal.
- :material-tune: [__tanx~__](../objects/math/tanx~.md) `tanx~` calculates the tangent of an incoming signal, expecting its input in radians.
- :material-tune: [__teeth~__](../objects/delay/teeth~.md) The `teeth~` object functions as a comb filter, offering independent control over feedforward and feedback delay times, along with their corresponding gain coefficients.
- :material-tune: [__thresh__](../objects/data_structures/thresh.md) The `thresh` object collects incoming numbers and lists, combining them into a single output list if they arrive within a specified time interval.
- :material-tune: [__thresh~__](../objects/logic/thresh~.md) The `thresh~` object acts as a Schmitt trigger, detecting when an input signal crosses specified high and low thresholds.
- :material-tune: [__togedge__](../objects/logic/togedge.md) The `togedge` object detects transitions in numerical input.
- :material-tune: [__tosymbol__](../objects/general_utilities/tosymbol.md) The `tosymbol` object converts any incoming message, including floats, lists, or other data types, into a single symbol message.
- :material-tune: [__train~__](../objects/lfos/train~.md) The `train~` object generates a pulse signal that alternates between 1 and 0, with configurable period, pulse width, and onset phase offset.
- :material-tune: [__trapezoid~__](../objects/oscillators/trapezoid~.md) `trapezoid~` generates a trapezoidal waveform.
- :material-tune: [__triangle~__](../objects/oscillators/triangle~.md) The `triangle~` object generates a variable-duty triangular wavetable.
- :material-tune: [__trough__](../objects/general_utilities/trough.md) The `trough` object tracks a minimum (trough) value.
- :material-tune: [__trunc~__](../objects/math/trunc~.md) `trunc~` truncates an incoming audio signal towards zero, effectively retaining only the integer part of each sample.
- :material-tune: [__universal__](../objects/routing/universal.md) The `universal` object sends messages to all instances of a specified Pure Data object type within the current patch, or optionally into subpatches.
- :material-tune: [__unjoin__](../objects/routing/unjoin.md) The `unjoin` object separates an incoming list into multiple sub-lists, each containing a specified number of elements.
- :material-tune: [__urn__](../objects/stochastic/urn.md) The `urn` object generates a sequence of unique random integers within a specified range (0 to n-1) without repetition.
- :material-tune: [__uzi__](../objects/patching/uzi.md) The `uzi` object generates a specified number of bangs and a corresponding counter value for each bang, executing its loop as fast as possible.
- :material-tune: [__vectral~__](../objects//vectral~.md) The `vectral~` object smooths or filters frame-based signal data, such as the output from `fft~`, primarily for visualization.
- :material-tune: [__wave~__](../objects/oscillators/wave~.md) The `wave~` object reads a wavetable (array) using a phase signal input (0-1), offering seven different interpolation modes including linear, cosine, cubic, spline, and Hermite.
- :material-tune: [__xbendin__](../objects/midi/xbendin.md) The `xbendin` object retrieves 14-bit pitch bend messages from raw MIDI input, outputting the pitch bend value (0-16383) and optionally the MIDI channel.
- :material-tune: [__xbendin2__](../objects/midi/xbendin2.md) The `xbendin2` object parses incoming raw MIDI data to extract the Most Significant Byte (MSB) and Least Significant Byte (LSB) of pitch bend messages, which can be combined to form a 14-bit value.
- :material-tune: [__xbendout__](../objects/midi/xbendout.md) The `xbendout` object formats and sends 14-bit MIDI pitch bend messages, ranging from 0 to 16383, to a specified MIDI channel.
- :material-tune: [__xbendout2__](../objects/midi/xbendout2.md) The `xbendout2` object formats and sends 14-bit pitch bend messages as two 7-bit values: a Most Significant Byte (MSB) and a Least Significant Byte (LSB).
- :material-tune: [__xnotein__](../objects/midi/xnotein.md) The `xnotein` object processes raw MIDI data streams, providing more detailed information than `notein`.
- :material-tune: [__xnoteout__](../objects/midi/xnoteout.md) The `xnoteout` object sends MIDI Note On and Note Off messages, uniquely supporting both Note On and Note Off (release) velocities for enhanced control.
- :material-tune: [__zerox~__](../objects/descriptors/zerox~.md) The `zerox~` object detects and counts zero crossings in an audio signal.
- :material-tune: [__zl__](../objects/data_structures/zl.md) The `zl` object is a versatile Pure Data list processor that performs various operations on incoming lists based on its selected mode.
</div>