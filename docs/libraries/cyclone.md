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
- :material-tune: [__accum__](../objects/accum.md) The `accum` object accumulates a numerical value by either adding an increment or multiplying by a given factor.
- :material-tune: [__acos__](../objects/acos.md) The `acos` object calculates the arc-cosine (inverse cosine) of a given number.
- :material-tune: [__acosh__](../objects/acosh.md) The `acosh` object calculates the hyperbolic arc-cosine of a given float input.
- :material-tune: [__acosh~__](../objects/acosh~.md) The `acosh~` object computes the hyperbolic arc-cosine of an incoming audio signal, sample by sample.
- :material-tune: [__acos~__](../objects/acos~.md) The `acos~` object calculates the arc-cosine of an incoming signal.
- :material-tune: [__active__](../objects/active.md) The `active` object reports the activity status of a Pure Data patch window.
- :material-tune: [__allpass~__](../objects/allpass~.md) The `allpass~` object implements an all-pass filter, which passes all frequencies without altering their gain but changes their phase.
- :material-tune: [__anal__](../objects/anal.md) The `anal` object reports the number of times it receives a specific number pair, effectively building a histogram of occurrences.
- :material-tune: [__append__](../objects/append.md) The `cyclone/append` object concatenates a predefined message to the end of any incoming message.
- :material-tune: [__asin__](../objects/asin.md) The `asin` object calculates the arc-sine (inverse sine) of a given number.
- :material-tune: [__asinh__](../objects/asinh.md) The `asinh` object calculates the hyperbolic arc-sine of a given number.
- :material-tune: [__asinh~__](../objects/asinh~.md) The `asinh~` object calculates the hyperbolic arc-sine of each incoming audio sample.
- :material-tune: [__asin~__](../objects/asin~.md) The `asin~` object calculates the arc-sine of an input signal.
- :material-tune: [__atan2~__](../objects/atan2~.md) The `atan2~` object calculates the arctangent of two input signals, 'a' and 'b', as atan(a/b).
- :material-tune: [__atanh__](../objects/atanh.md) The `atanh` object calculates the hyperbolic arc-tangent of a given number.
- :material-tune: [__atanh~__](../objects/atanh~.md) The `atanh~` object calculates the hyperbolic arc-tangent of an input signal, sample by sample.
- :material-tune: [__atan~__](../objects/atan~.md) `atan~` calculates the arc-tangent of an input signal, sample by sample.
- :material-tune: [__atodb__](../objects/atodb.md) The `atodb` object converts linear amplitude values into decibels full scale (dBFS).
- :material-tune: [__atodb~__](../objects/atodb~.md) The `atodb~` object converts a linear amplitude audio signal to its equivalent decibel full scale (dBFS) value.
- :material-tune: [__average~__](../objects/average~.md) The `average~` object calculates a moving average of an audio signal over a specified number of samples.
- :material-tune: [__bangbang__](../objects/bangbang.md) The `bangbang` object outputs a specified number of `bang` messages from its outlets in right-to-left order when it receives any input.
- :material-tune: [__bitand~__](../objects/bitand~.md) The `cyclone/bitand~` object performs a bitwise AND operation on two incoming signals or a signal and a given bitmask.
- :material-tune: [__bitnot~__](../objects/bitnot~.md) The `bitnot~` object performs a bitwise NOT operation (one's complement) on an incoming audio signal, inverting all bits of its 32-bit representation.
- :material-tune: [__bitor~__](../objects/bitor~.md) The `bitor~` object performs a bitwise OR operation on two audio signals or a signal and a 32-bit integer bitmask.
- :material-tune: [__bitsafe~__](../objects/bitsafe~.md) The `bitsafe~` object processes incoming audio signals, replacing any "Not a Number" (NaN) or infinity values with zero.
- :material-tune: [__bitshift~__](../objects/bitshift~.md) `bitshift~` performs bitwise shifting on an incoming signal, moving its bit values to the left or right.
- :material-tune: [__bitxor~__](../objects/bitxor~.md) The `bitxor~` object performs a bitwise exclusive OR (XOR) operation on two input signals, or a signal and a given bitmask.
- :material-tune: [__bondo__](../objects/bondo.md) The `bondo` object in Pure Data synchronizes and routes incoming messages.
- :material-tune: [__borax__](../objects/borax.md) The `borax` object processes incoming MIDI note and velocity data, reporting detailed information about active notes.
- :material-tune: [__bucket__](../objects/bucket.md) The `bucket` object passes incoming numbers sequentially through its multiple outlets in a rotational pattern, like a bucket brigade.
- :material-tune: [__buddy__](../objects/buddy.md) The `buddy` object synchronizes incoming messages from its inlets.
- :material-tune: [__buffer~__](../objects/buffer~.md) The `buffer~` object stores audio data in memory as a multichannel array, supporting up to 64 channels.
- :material-tune: [__buffir~__](../objects/buffir~.md) The `buffir~` object is a table/buffer-based Finite Impulse Response (FIR) filter.
- :material-tune: [__capture__](../objects/capture.md) The `capture` object stores incoming messages (floats and symbols) in the order they are received, acting as a sequential data buffer.
- :material-tune: [__capture~__](../objects/capture~.md) The `capture~` object is designed for signal debugging and investigation, capturing audio samples into an internal buffer.
- :material-tune: [__cartopol__](../objects/cartopol.md) The `cartopol~` object converts Cartesian coordinates (real and imaginary parts) into polar coordinates (amplitude and phase).
- :material-tune: [__cartopol~__](../objects/cartopol~.md) The `cartopol~` object converts a complex signal from Cartesian coordinates (real and imaginary parts) to polar coordinates (amplitude and phase).
- :material-tune: [__change~__](../objects/change~.md) The `change~` object detects if an incoming audio signal is changing and its direction.
- :material-tune: [__click~__](../objects/click~.md) The `click~` object generates a single-sample audio impulse upon receiving a bang message.
- :material-tune: [__clip__](../objects/clip.md) The `cyclone/clip` object constrains incoming float or list values to a specified numerical range.
- :material-tune: [__clip~__](../objects/clip~.md) The `clip~` object constrains an input audio signal to a specified minimum and maximum value.
- :material-tune: [__coll__](../objects/coll.md) The `coll` object in Pure Data is a versatile data collection and manipulation tool.
- :material-tune: [__comb~__](../objects/comb~.md) The `comb~` object implements a comb filter, an audio effect that combines a signal with a delayed version of itself to create a series of regularly spaced notches or peaks in the frequency response.
- :material-tune: [__comment__](../objects/comment.md) The `cyclone/comment` object is a GUI element for displaying customizable text within a Pure Data patch.
- :material-tune: [__cosh__](../objects/cosh.md) The `cosh` object calculates the hyperbolic cosine of a given number.
- :material-tune: [__cosh~__](../objects/cosh~.md) The `cosh~` object calculates the hyperbolic cosine of an input signal sample by sample.
- :material-tune: [__cosx~__](../objects/cosx~.md) The `cyclone/cosx~` object calculates the cosine of an incoming signal, expecting the input values to be in radians.
- :material-tune: [__counter__](../objects/counter.md) The `counter` object in Pure Data increments or decrements an integer value within a specified range.
- :material-tune: [__count~__](../objects/count~.md) The `count~` object is a sample-accurate counter that outputs a signal incrementing by one for each elapsed sample.
- :material-tune: [__curve~__](../objects/curve~.md) `curve~` is a signal-rate object that generates non-linear (curved) ramp signals, functioning as an envelope generator.
- :material-tune: [__cycle__](../objects/cycle.md) The `cycle` object distributes incoming messages to its outlets in a round-robin fashion.
- :material-tune: [__cycle~__](../objects/cycle~.md) The `cycle~` object is a linear interpolating oscillator that generates an audio signal by repeatedly reading through a waveform.
- :material-tune: [__cyclone__](../objects/cyclone.md) The `cyclone` library for Pure Data provides a comprehensive set of mathematical and comparative operators, many of which are direct aliases for common Max/MSP objects.
- :material-tune: [__dbtoa__](../objects/dbtoa.md) The `dbtoa` object converts decibel (dBFS) amplitude values to their corresponding linear amplitude.
- :material-tune: [__dbtoa~__](../objects/dbtoa~.md) The `dbtoa~` object converts a decibel full scale (dBFS) amplitude signal to a linear amplitude signal.
- :material-tune: [__decide__](../objects/decide.md) The `decide` object randomly outputs either 0 or 1.
- :material-tune: [__decode__](../objects/decode.md) The `decode` object routes a `1` to a specific outlet and `0` to all others, based on a numerical input.
- :material-tune: [__degrade~__](../objects/degrade~.md) The `degrade~` object processes an audio signal, reducing its sampling rate and bit depth.
- :material-tune: [__delay~__](../objects/delay~.md) The `delay~` object delays an audio signal by a specified number of samples.
- :material-tune: [__deltaclip~__](../objects/deltaclip~.md) The `deltaclip~` object limits the rate of change (slew rate) of an incoming audio signal.
- :material-tune: [__delta~__](../objects/delta~.md) The `delta~` object calculates the difference between the current and previous sample of an incoming audio signal.
- :material-tune: [__downsamp~__](../objects/downsamp~.md) The `downsamp~` object performs a sample-and-hold operation on an input audio signal, effectively reducing its sample rate.
- :material-tune: [__drunk__](../objects/drunk.md) The `drunk` object generates a "drunk walk" sequence of random numbers.
- :material-tune: [__edge~__](../objects/edge~.md) The `edge~` object detects transitions in an audio signal.
- :material-tune: [__equals~__](../objects/equals~.md) The `equals~` (or `==~`) object performs a signal-level comparison.
- :material-tune: [__flush__](../objects/flush.md) The `flush` object functions as a "panic button" for MIDI Note-on messages.
- :material-tune: [__forward__](../objects/forward.md) The `forward` object sends messages to various destinations, allowing the target to change dynamically with each message, similar to using semicolons in message boxes.
- :material-tune: [__frameaccum~__](../objects/frameaccum~.md) `frameaccum~` accumulates the values of each sample across incoming signal blocks, primarily designed for computing a running phase of FFT frames.
- :material-tune: [__framedelta~__](../objects/framedelta~.md) The `framedelta~` object calculates the running phase deviation of an FFT analysis.
- :material-tune: [__fromsymbol__](../objects/fromsymbol.md) The `fromsymbol` object converts an incoming `symbol` message into its corresponding Pure Data message type, such as a `float`, `bang`, `list`, or `anything` message.
- :material-tune: [__funbuff__](../objects/funbuff.md) The `funbuff` object stores and manages ordered pairs of x/y integer values.
- :material-tune: [__funnel__](../objects/funnel.md) The `funnel` object receives data from multiple inlets and outputs it through a single outlet, tagging the incoming data with its inlet number.
- :material-tune: [__gate__](../objects/gate.md) The `gate` object functions as a message router, directing incoming messages from its second inlet to one of its multiple outlets.
- :material-tune: [__gate~__](../objects/gate~.md) The `gate~` object routes an incoming audio signal from its second inlet to one of its multiple outlets.
- :material-tune: [__grab__](../objects/grab.md) The `grab` object in Pure Data sends a message to another object and captures its output, routing it through `grab`'s own outlets.
- :material-tune: [__greaterthaneq~__](../objects/greaterthaneq~.md) The `greaterthaneq~` (or `>=~`) object performs a signal-rate comparison, outputting a 1 signal when the left inlet's signal is greater than or equal to the right inlet's signal or argument.
- :material-tune: [__greaterthan~__](../objects/greaterthan~.md) The `greaterthan~` (or `>~`) object in Pure Data performs a signal comparison.
- :material-tune: [__histo__](../objects/histo.md) The `histo` object records the frequency of positive integer inputs, effectively building a histogram.
- :material-tune: [__index~__](../objects/index~.md) The `index~` object reads values from an array without interpolation, using a signal as the index to read the array.
- :material-tune: [__iter__](../objects/iter.md) The `iter` object splits an incoming message (which can contain floats or symbols) into its individual elements.
- :material-tune: [__join__](../objects/join.md) The `join` object in Pure Data combines messages from multiple inlets into a single output list.
- :material-tune: [__kink~__](../objects/kink~.md) The `kink~` object distorts a `phasor~` signal by applying a "kink" to its phase.
- :material-tune: [__lessthaneq~__](../objects/lessthaneq~.md) The `lessthaneq~` (or `<=~`) object performs a signal-rate comparison.
- :material-tune: [__lessthan~__](../objects/lessthan~.md) The `lessthan~` (or `<~`) object performs a "less than" comparison on incoming audio signals.
- :material-tune: [__linedrive__](../objects/linedrive.md) The `linedrive` object scales numbers from an input range to an output range using an exponential curve.
- :material-tune: [__line~__](../objects/line~.md) The `cyclone/line~` object generates linear signal ramps or envelopes.
- :material-tune: [__listfunnel__](../objects/listfunnel.md) The `listfunnel` object takes an incoming list and outputs its elements sequentially, each preceded by its corresponding index.
- :material-tune: [__loadmess__](../objects/loadmess.md) The `loadmess` object sends a predefined message automatically when its containing patch is loaded, or when it receives a `bang` message.
- :material-tune: [__lookup~__](../objects/lookup~.md) The `lookup~` object performs a signal-rate table lookup, mapping input signal values (typically from -1 to 1) to indices within a specified array.
- :material-tune: [__lores~__](../objects/lores~.md) `lores~` is an inexpensive resonant lowpass filter for audio signals.
- :material-tune: [__match__](../objects/match.md) The `match` object outputs incoming data when it matches a predefined pattern.
- :material-tune: [__matrix~__](../objects/matrix~.md) The `matrix~` object routes and mixes audio signals from multiple inlets to multiple outlets.
- :material-tune: [__maximum__](../objects/maximum.md) The `maximum` object outputs the largest value from its inputs.
- :material-tune: [__maximum~__](../objects/maximum~.md) The `maximum~` object outputs the greater of two input signals, or the greater of an input signal and a given argument.
- :material-tune: [__midiflush__](../objects/midiflush.md) The `midiflush` object acts as a "panic button" for MIDI notes.
- :material-tune: [__midiformat__](../objects/midiformat.md) The `midiformat` object converts various discrete MIDI inputs, such as note, control change, and pitch bend messages, into a single raw MIDI message stream.
- :material-tune: [__midiparse__](../objects/midiparse.md) The `midiparse` object receives raw MIDI data, typically from `midiin`, and parses it into various MIDI messages.
- :material-tune: [__minimum__](../objects/minimum.md) The `minimum` object outputs the smallest value from its inputs.
- :material-tune: [__minimum~__](../objects/minimum~.md) The `minimum~` object outputs a signal that represents the minimum value between two input signals, or between an input signal and a numerical argument.
- :material-tune: [__minmax~__](../objects/minmax~.md) The `minmax~` object tracks and outputs the minimum and maximum signal levels it has received since its creation or last reset.
- :material-tune: [__modulo~__](../objects/modulo~.md) The `modulo~` (or `%~`) object is a signal remainder operator.
- :material-tune: [__mousefilter__](../objects/mousefilter.md) The `mousefilter` object acts as a gate, preventing messages from passing through while a mouse button is held down.
- :material-tune: [__mousestate__](../objects/mousestate.md) The `mousestate` object reports the current state of the mouse, including click status, cursor X and Y positions, and delta movement.
- :material-tune: [__mstosamps~__](../objects/mstosamps~.md) The `mstosamps~` object converts a time value in milliseconds to the corresponding number of audio samples, taking the current sample rate into account.
- :material-tune: [__mtr__](../objects/mtr.md) The `mtr` object in Pure Data functions as a multi-track message recorder and playback system.
- :material-tune: [__next__](../objects/next.md) The `next` object in Pure Data detects whether an incoming message is part of the same "logical event" as the previous one.
- :material-tune: [__notequals~__](../objects/notequals~.md) The `notequals~` (or `!=~`) object performs a signal-level "not equal to" comparison.
- :material-tune: [__number~__](../objects/number~.md) The `number~` object in Pure Data functions as a dual-mode signal utility: it can either monitor an incoming audio signal, displaying its value, or generate a signal with a user-defined ramp time.
- :material-tune: [__offer__](../objects/offer.md) The `offer` object stores temporary `x`/`y` number pairs.
- :material-tune: [__onebang__](../objects/onebang.md) The `onebang` object acts as a conditional gate for bang messages.
- :material-tune: [__onepole~__](../objects/onepole~.md) The `onepole~` object implements a simple, efficient one-pole IIR low-pass filter, providing 6dB per octave attenuation.
- :material-tune: [__overdrive~__](../objects/overdrive~.md) The `overdrive~` object simulates analog overdrive by applying a non-linear transfer function to an incoming audio signal, mimicking the soft clipping of a tube-based circuit.
- :material-tune: [__pak__](../objects/pak.md) The `pak` object creates a list from its inlets, similar to `pack`.
- :material-tune: [__past__](../objects/past.md) The `past` object compares an incoming list of numbers against a corresponding list of thresholds.
- :material-tune: [__peak__](../objects/peak.md) The `peak` object compares incoming numbers to a stored "peak" (maximum) value.
- :material-tune: [__peakamp~__](../objects/peakamp~.md) The `peakamp~` object measures the absolute peak amplitude of an incoming audio signal.
- :material-tune: [__peek~__](../objects/peek~.md) The `peek~` object provides direct, non-interpolated access to Pure Data arrays (tables) for both reading and writing values via messages.
- :material-tune: [__phaseshift~__](../objects/phaseshift~.md) The `phaseshift~` object is a 2nd order allpass filter that alters the phase of an audio signal without changing its gain.
- :material-tune: [__phasewrap~__](../objects/phasewrap~.md) The `phasewrap~` object wraps an incoming signal's value between -π and π.
- :material-tune: [__pink~__](../objects/pink~.md) The `pink~` object generates pink noise, an audio signal characterized by constant power per octave, with its energy decreasing by 3dB per octave.
- :material-tune: [__play~__](../objects/play~.md) The `play~` object plays audio from an array, allowing playback of any segment, at varying speeds (including backwards), and with interpolation.
- :material-tune: [__plusequals~__](../objects/plusequals~.md) The `plusequals~` (or `+=~`) object in Pure Data continuously sums incoming audio signal values, maintaining a running total.
- :material-tune: [__poke~__](../objects/poke~.md) `poke~` writes audio signals into a Pure Data array at specified indices.
- :material-tune: [__poltocar__](../objects/poltocar.md) The `poltocar` object converts polar coordinates (amplitude and phase) to Cartesian coordinates (real and imaginary).
- :material-tune: [__poltocar~__](../objects/poltocar~.md) The `poltocar~` object converts signal values from polar coordinates (amplitude and phase) to Cartesian coordinates (real and imaginary parts).
- :material-tune: [__pong__](../objects/pong.md) The `pong` object in Pure Data is a utility for manipulating numerical inputs.
- :material-tune: [__pong~__](../objects/pong~.md) The `pong~` object limits an input audio signal within a specified low-high range.
- :material-tune: [__pow~__](../objects/pow~.md) `cyclone/pow~` raises a base value to the power of an exponent.
- :material-tune: [__prepend__](../objects/prepend.md) The `prepend` object adds a predefined message, set as an argument or via a `set` message, to the beginning of any incoming message.
- :material-tune: [__prob__](../objects/prob.md) The `prob` object generates a weighted series of random numbers, functioning as a 1st-order Markov chain.
- :material-tune: [__pv__](../objects/pv.md) The `pv` object in Pure Data functions as a private variable, storing any type of message.
- :material-tune: [__rampsmooth~__](../objects/rampsmooth~.md) The `rampsmooth~` object smooths an incoming audio signal by applying a linear ramp whenever the input value changes.
- :material-tune: [__rand~__](../objects/rand~.md) `rand~` generates random values between -1 and 1 at a given frequency, linearly interpolating between these values to produce a bandlimited noise signal.
- :material-tune: [__rdiv__](../objects/rdiv.md) The `rdiv` (or `!/`) object performs division with reversed inlet behavior compared to the standard `/` object.
- :material-tune: [__rdiv~__](../objects/rdiv~.md) The `rdiv~` object, also known as `!/~`, performs division on audio signals.
- :material-tune: [__record~__](../objects/record~.md) The `record~` object captures audio signals and stores them into Pure Data arrays, supporting up to 64 channels.
- :material-tune: [__reson~__](../objects/reson~.md) `reson~` is a bandpass resonant filter designed for audio signals.
- :material-tune: [__rminus__](../objects/rminus.md) The `rminus` (or `!-`) object performs subtraction with its inlets reversed compared to the standard `[-]` object.
- :material-tune: [__rminus~__](../objects/rminus~.md) The `rminus~` (or `!-~`) object performs subtraction on audio signals.
- :material-tune: [__round__](../objects/round.md) The `round` object approximates incoming numbers (floats or lists of floats) to the nearest integer multiple of a specified value.
- :material-tune: [__round~__](../objects/round~.md) The `round~` object quantizes an incoming audio signal by approximating its values to an integer multiple of a specified number.
- :material-tune: [__sah~__](../objects/sah~.md) The `sah~` object samples and holds an input audio signal based on a trigger signal.
- :material-tune: [__sampstoms~__](../objects/sampstoms~.md) The `sampstoms~` object converts a time value from samples to milliseconds, adjusting for the current sample rate.
- :material-tune: [__scale__](../objects/scale.md) The `scale` object maps an input numerical range to an output numerical range.
- :material-tune: [__scale~__](../objects/scale~.md) `scale~` maps an input signal range to an output signal range, supporting both linear and exponential scaling.
- :material-tune: [__scope~__](../objects/scope~.md) `scope~` is a Pure Data object that functions as an oscilloscope, visualizing audio signals.
- :material-tune: [__selector~__](../objects/selector~.md) The `selector~` object acts as a signal-rate multiplexer, routing one of its 'n' signal inputs to a single output.
- :material-tune: [__seq__](../objects/seq.md) The `seq` object in Pure Data is a MIDI sequencer that can play, record, load, and save MIDI streams to and from MIDI or text files.
- :material-tune: [__sinh__](../objects/sinh.md) The `sinh` object calculates the hyperbolic sine of a given numerical input.
- :material-tune: [__sinh~__](../objects/sinh~.md) The `sinh~` object calculates the hyperbolic sine of an incoming signal.
- :material-tune: [__sinx~__](../objects/sinx~.md) The `sinx~` object calculates the sine of an incoming audio signal.
- :material-tune: [__slide~__](../objects/slide~.md) The `slide~` object logarithmically smooths an incoming audio signal, providing non-linear transitions between signal value changes.
- :material-tune: [__snapshot~__](../objects/snapshot~.md) The `cyclone/snapshot~` object converts a sample from an audio signal into a control-rate float.
- :material-tune: [__speedlim__](../objects/speedlim.md) The `speedlim` object controls the rate at which messages are passed through.
- :material-tune: [__spell__](../objects/spell.md) The `spell` object converts incoming messages, character by character, into their corresponding UTF-8 (Unicode) integer values.
- :material-tune: [__spike~__](../objects/spike~.md) The `spike~` object detects zero-to-non-zero transitions in an audio signal and reports the time interval (in milliseconds) since the last detected transition.
- :material-tune: [__split__](../objects/split.md) The `split` object separates incoming float numbers into two outlets based on whether they fall within a specified minimum and maximum range.
- :material-tune: [__spray__](../objects/spray.md) The `spray` object distributes incoming list elements to its outlets.
- :material-tune: [__sprintf__](../objects/sprintf.md) The `sprintf` object in Pure Data formats messages similar to C's `printf` function.
- :material-tune: [__substitute__](../objects/substitute.md) The `substitute` object replaces elements within an input message.
- :material-tune: [__sustain__](../objects/sustain.md) The `sustain` object emulates a MIDI sustain pedal, holding note-off messages while active and releasing them when deactivated.
- :material-tune: [__svf~__](../objects/svf~.md) The `svf~` object implements a Chamberlin state-variable filter, simultaneously outputting lowpass, highpass, bandpass, and notch filtered signals.
- :material-tune: [__switch__](../objects/switch.md) The `switch` object in Pure Data acts as a message router, allowing only one of its 'n' inlets to pass data through to its single outlet at a time.
- :material-tune: [__table__](../objects/table.md) The `table` object in Pure Data stores and manipulates a numerical array.
- :material-tune: [__tanh__](../objects/tanh.md) The `tanh` object calculates the hyperbolic tangent of its input.
- :material-tune: [__tanh~__](../objects/tanh~.md) The `tanh~` object calculates the hyperbolic tangent of an input audio signal.
- :material-tune: [__tanx~__](../objects/tanx~.md) The `tanx~` object calculates the tangent of an incoming audio signal, expecting the input values to be in radians.
- :material-tune: [__teeth~__](../objects/teeth~.md) The `teeth~` object implements a comb filter, processing an audio signal with independent feedforward and feedback delays.
- :material-tune: [__thresh__](../objects/thresh.md) The `thresh` object collects incoming numbers and lists, combining them into a single output list if they arrive within a specified time interval (default 10ms).
- :material-tune: [__thresh~__](../objects/thresh~.md) `thresh~` is a Schmitt trigger for audio signals.
- :material-tune: [__togedge__](../objects/togedge.md) The `togedge` object detects transitions in numerical input.
- :material-tune: [__tosymbol__](../objects/tosymbol.md) The `tosymbol` object converts any incoming message (e.g., floats, lists) into a single symbol message.
- :material-tune: [__train~__](../objects/train~.md) The `train~` object generates a periodic pulse signal that alternates between 1 (on) and 0 (off), with configurable period, pulse width, and an onset phase offset.
- :material-tune: [__trapezoid~__](../objects/trapezoid~.md) The `trapezoid~` object generates a trapezoidal waveform, functioning as a wavetable oscillator when fed a phase signal (0-1) from `phasor~`.
- :material-tune: [__triangle~__](../objects/triangle~.md) The `triangle~` object generates a variable-duty triangle waveform at signal rate.
- :material-tune: [__trough__](../objects/trough.md) The `trough` object compares incoming float values to a stored 'trough' (minimum) value.
- :material-tune: [__trunc~__](../objects/trunc~.md) The `trunc~` object truncates an audio signal towards zero, effectively taking only the integer part of each sample's value.
- :material-tune: [__universal__](../objects/universal.md) The `universal` object sends messages to all instances of a specified object type within the current Pure Data patch.
- :material-tune: [__unjoin__](../objects/unjoin.md) The `unjoin` object separates an incoming list into smaller groups of elements.
- :material-tune: [__uzi__](../objects/uzi.md) The `uzi` object generates a sequence of bangs and corresponding counter values, useful for iterating through a specified number of steps.
- :material-tune: [__vectral~__](../objects/vectral~.md) The `vectral~` object smooths or filters frame-based signal data, such as the output of an `fft~` object, primarily for visualization purposes.
- :material-tune: [__wave~__](../objects/wave~.md) The `wave~` object reads audio data from a specified array (wavetable) using a phase signal (0-1) as an index.
- :material-tune: [__xbendin__](../objects/xbendin.md) The `xbendin` object retrieves 14-bit pitch bend messages from raw MIDI input data.
- :material-tune: [__xbendin2__](../objects/xbendin2.md) The `xbendin2` object processes incoming raw MIDI data to extract the Most Significant Byte (MSB) and Least Significant Byte (LSB) of pitch bend messages.
- :material-tune: [__xbendout__](../objects/xbendout.md) The `xbendout` object formats and sends 14-bit MIDI pitch bend messages.
- :material-tune: [__xbendout2__](../objects/xbendout2.md) The `xbendout2` object formats 14-bit pitch bend messages into two 7-bit values (MSB and LSB) and sends them as a raw MIDI data stream.
- :material-tune: [__xnotein__](../objects/xnotein.md) The `xnotein` object parses raw MIDI data streams, providing more detailed information than the standard `notein` object.
- :material-tune: [__xnoteout__](../objects/xnoteout.md) The `xnoteout` object sends MIDI note messages, offering enhanced control over the standard `noteout` object by including both Note On and Note Off (release) velocities.
- :material-tune: [__zerox~__](../objects/zerox~.md) The `zerox~` object functions as a zero-crossing detector and counter for audio signals.
- :material-tune: [__zl__](../objects/zl.md) The `zl` object in Pure Data is a versatile list processor that manipulates messages containing one or more elements.
</div>