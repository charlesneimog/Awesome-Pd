---
search:
    exclude: true
---

# else
`ELSE` is a big library of externals that extends the performance of Pd. `ELSE` provides a cohesive system for computer music; it also serves as a basis for a Live Electronics Tutorial by the same author, yours truly, Alexandre Torres Porres. This library's repository resides at https://github.com/porres/pd-else/. This tutorial is also included as part of the `ELSE` library download. Look for the 'Live-Electronics-Tutorial' folder inside it, and also check its README file for instructions on how to install it.
 `ELSE` is also part of [PlugData](https://plugdata.org/) by Timothy Schoen, which is a fork of Pd that loads as a standalone or VST with a revamped GUI. `ELSE` has received collaboration from Tim and others involved with PlugData, and many objects have been included in `ELSE` just so they are supported in PlugData.
`ELSE` also ships a modification of [pdlua](https://github.com/agraef/pd-lua), which is needed for a couple of GUI objects.
<h2>Contributors</h2>

<div id="libcontributors"></div>

<p align="center">
<i>People who contribute to this project.</i>
</p>


<script>
async function updateList() {
    const repoOwner = 'porres';
    const repoName = 'pd-else';
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
- :material-tune: [__out~__](../objects/out~.md) `out~` has a built in `sum~` object, so it can take multichannel signals and sum them together for each input.
.
- :material-tune: [__quantizer~__](../objects/quantizer~.md) `quantizer~` approximates a value to step values defined by the argument.
- :material-tune: [__unmerge~__](../objects/unmerge~.md) `unmerge~` separates the channels of a multichannel signal in groups of any size (default 1).
- :material-tune: [__pvoc.freeze~__](../objects/pvoc.freeze~.md) `pvoc.freeze~` is a freeze object based on a phase vocoder.
.
- :material-tune: [__keyboard__](../objects/keyboard.md) `keyboard` takes MIDI notes and also generates them via clicking.
.
- :material-tune: [__xmod2~__](../objects/xmod2~.md) `xmod2~` performs is a variant of `xmod~`, but only performs frequency modulation (so far) and uses a different and cheap sine waveform that promotes more chaotic and cool sounds.
.
- :material-tune: [__biquads~__](../objects/biquads~.md) `biquads~` is a series of biquad filters in cascade.
.
- :material-tune: [__lfnoise~__](../objects/lfnoise~.md) `lfnoise~` is a low frequency (band limited) noise with or without interpolation.
- :material-tune: [__pdlink__](../objects/pdlink.md) `pdlink` allows you to communicate to/from different Pd instances over local network, as different versions and even forks of Pure Data (such as plugdata).
- :material-tune: [__out8~__](../objects/out8~.md) `out8~` is a convenient octaphonic input/output abstraction.
- :material-tune: [__presets__](../objects/presets.md) `presets` manages presets for patches and abstractions and has interpolation and morphing features.
- :material-tune: [__tabplayer~__](../objects/tabplayer~.md) `tabplayer~` plays arrays with multichannel support.
- :material-tune: [__wt2d~__](../objects/wt2d~.md) `wt2d~` is an interpolating wavetable oscillator like `wt~`, but besides a horizontal dimension, it can also scan through a vertical dimension of a sliced wavetable.
- :material-tune: [__grain.sampler~__](../objects/grain.sampler~.md) `grain.sampler~` is a sample based granulator that generates clouds of grains.
.
- :material-tune: [__midi__](../objects/midi.md) `midi` plays/records raw MIDI streams and can save/read MIDI files or import/export to txt files.
.
- :material-tune: [__xgate2~__](../objects/xgate2~.md) `xgate2~` routes an input signal to 'n' specified outlets with crossfading between adjacent channels according to a spread parameter.
.
- :material-tune: [__white~__](../objects/white~.md) `white~` is a white noise generator from a pseudo random number generator algorithm.
- :material-tune: [__smooth~__](../objects/smooth~.md) `smooth~` smoothens a signal transition with linear interpolation by default, at a given time in ms.
- :material-tune: [__cosine~__](../objects/cosine~.md) `cosine~` is a cosine oscillator that accepts negative frequencies, has inlets for phase sync and phase modulation.
- :material-tune: [__spectrograph~__](../objects/spectrograph~.md) `spectrograph~` is an abstraction for visualizing FFT amplitudes from 0hz to Nyquist.
- :material-tune: [__retune__](../objects/retune.md) `retune` receives a scale as a list of steps in cents and a base MIDI pitch value (default 60).
- :material-tune: [__envgen~__](../objects/envgen~.md) `envgen~` is an envelope (and an all purpose line) generator (here it creates a 1000 ms line to 1 and then a 500 ms line to 0).
- :material-tune: [__slew~__](../objects/slew~.md) `slew~` takes an amplitude limit per second and an incoming value to be 'slew limited'.
- :material-tune: [__store__](../objects/store.md) `store` is an abstraction based on `text` that stores incoming messages sequentially.
.
- :material-tune: [__pluck~__](../objects/pluck~.md) `pluck~` is a Karplus-Strong algorithm with a 1st order lowpass filter in the feedback loop.
- :material-tune: [__pdlink~__](../objects/pdlink~.md) `pdlink~` allows you to send/receive audio streans to/from different Pd instances, as different versions, platforms and even forks of Pure Data (such as PlugData).
- :material-tune: [__bl.tri~__](../objects/bl.tri~.md) `bl.tri~` is a triangle oscillator like `else/tri~`, but it is bandlimited.
- :material-tune: [__fdn.rev~__](../objects/fdn.rev~.md) `fdn.rev~` is a feedback delay network reverberator which can be used for late reflections (a.k.a reverb tail).
- :material-tune: [__bl.imp2~__](../objects/bl.imp2~.md) `bl.imp2~` is a two sided impulse oscillator like `else/imp2~`, but it is bandlimited.
.
- :material-tune: [__gran.player~__](../objects/gran.player~.md) `gran.player~` is like `player~` but provides independent time stretching and pitch shifting via granulation (just like `pvoc.player~`).
- :material-tune: [__vibrato~__](../objects/vibrato~.md) `vibrato~` is a pitch shifter abstraction with an LFO controlling the pitch deviation in cents.
.
- :material-tune: [__canvas.setname__](../objects/canvas.setname.md) `canvas.setname` sets a symbol name to a canvas so you can send it messages.
- :material-tune: [__touch.in__](../objects/touch.in.md) `touch.in` extracts MIDI Aftertouch information from raw MIDI input or a connected MIDI device.
.
- :material-tune: [__circle__](../objects/circle.md) `circle` is a two dimensional slider GUI abstraction with a circular area (see also [else/slider2d).
.
- :material-tune: [__scales__](../objects/scales.md) `scales` generates scales as note names (default) or MIDI pitches.
- :material-tune: [__op__](../objects/op.md) `op` provides many operators and is most useful for lists, as there are objects in Pd Vanilla for most of these operations.
.
- :material-tune: [__equal__](../objects/equal.md) `equal` compares lists and outputs 1 if they're the same or 0 if they're not.
- :material-tune: [__autotune2__](../objects/autotune2.md) `autotune2` receives a scale as a list of steps in cents and then retunes incoming cents values to the closest step in the scale.
.
- :material-tune: [__loop__](../objects/loop.md) `loop` is a loop counter, but it can also loop bangs like `until` (using the -b flag).
- :material-tune: [__float2sig~__](../objects/float2sig~.md) `float2sig~` (or `f2s~` for short) is an abstraction based on `vline~` that converts floats to signals or lists to multichannel signals.
- :material-tune: [__midi.in__](../objects/midi.in.md) `midi.in` sends "cooked" MIDI data instead of "raw" data like `midiin` with MIDI data type symbol, values and channel (but a note output is sent as a simple numeric list).
- :material-tune: [__mtx.ctl__](../objects/mtx.ctl.md) `mtx.ctl` provides a user matrix interface control.
- :material-tune: [__gray~__](../objects/gray~.md) `gray~` generates noise based on "gray code" or reflected binary code (RBC), which results from flipping random bits (sot is is based on a pseudo random number generator algorithm.).
- :material-tune: [__vocoder~__](../objects/vocoder~.md) `vocoder~` is classic cross synthesis channel vocoder abstraction.
.
- :material-tune: [__midi.out__](../objects/midi.out.md) `midi.out` sends MIDI data from "cooked" data, instead of "raw" data like `midiout`.
- :material-tune: [__mono.rev~__](../objects/mono.rev~.md) `mono.rev~` is a reverb abstraction with mono input but stereo output.
- :material-tune: [__pack2__](../objects/pack2.md) `pack2` is kinda similar to Pd Vanilla's `pack`, but any inlet triggers the output (though a "set" message avoids the output).
- :material-tune: [__resonant~__](../objects/resonant~.md) `resonant~` is a bandpass resonator filter like `bandpass~`, but it doesn't have a maximum dB value of 0, so changing the Q increases the gain of the filter.
- :material-tune: [__resonbank~__](../objects/resonbank~.md) `resonbank~` is a bank of resonators made of `resonator~` objects.
- :material-tune: [__bend.in__](../objects/bend.in.md) The `bend.in` object in Pure Data extracts MIDI Pitch Bend information from either a connected MIDI device (internal source) or raw MIDI input (external source).
- :material-tune: [__above~__](../objects/above~.md) The `above~` object in Pure Data monitors a signal input and outputs impulses based on a threshold.
- :material-tune: [__slice__](../objects/slice.md) `slice` splits lists.
- :material-tune: [__autofade.mc~__](../objects/autofade.mc~.md) `autofade.mc~` is an automatic fade in/out for multichanne inputs.
- :material-tune: [__note.out__](../objects/note.out.md) `note.out` formats and sends raw MIDI pitch messages to Pd's MIDI output and its outlet.
- :material-tune: [__vsaw~__](../objects/vsaw~.md) `vsaw~` is a variable sawtooth waveform oscillator that also becomes a triangular osccilator.
- :material-tune: [__dust~__](../objects/dust~.md) The `dust~` object in Pure Data is a pseudo-random impulse generator that outputs positive random impulses (up to 1) according to a configurable density (rate) parameter.
- :material-tune: [__autofade2.mc~__](../objects/autofade2.mc~.md) `autofade2.mc~` is an automatic fade in/out for multichanne inputs.
- :material-tune: [__add__](../objects/add.md) The `add` object in Pure Data accumulates input values to a running sum, starting from a configurable initial value (0 by default).
- :material-tune: [__oscnoise~__](../objects/oscnoise~.md) `oscnoise~` is an oscillator that accepts negative frequencies, has inlets for phase sync and phase modulation.
- :material-tune: [__sfont~__](../objects/sfont~.md) `sfont~` is a sampler synthesizer that plays SoundFont files.
- :material-tune: [__damp.osc~__](../objects/damp.osc~.md) `damp.osc~` is an abstraction based `reonant2~` and also very very similar to it (to the point I think it wasn't worth having two objects with such subtle differences).
- :material-tune: [__delace~__](../objects/delace~.md) `delace~` deinterleaves a multichannel signal according to the number of outlets.
.
- :material-tune: [__pipe2__](../objects/pipe2.md) `pipe2` is similar to vanilla's pipe.
- :material-tune: [__nchs~__](../objects/nchs~.md) `nchs~` gets the number of channels from a multi-channel connection, as provided by `snake~ in`, `clone` or other objects.
- :material-tune: [__mag~__](../objects/mag~.md) `mag~` gets the spectrum magnitudes (amplitudes) from cartesian coordinates (real / imaginary).
- :material-tune: [__changed__](../objects/changed.md) `changed` passes its data input through only when it changed from the last receive message or the message that was set via arguments or messages.
- :material-tune: [__tabwriter~__](../objects/tabwriter~.md) `tabwriter~` records up to 64 signal channels into arrays.
- :material-tune: [__stream__](../objects/stream.md) `stream` mode makes a list with the last N received items.
.
- :material-tune: [__parabolic~__](../objects/parabolic~.md) `parabolic~` is a parabolic oscillator that accepts negative frequencies, has inlets for phase sync and and phase modulation.
- :material-tune: [__rotate~__](../objects/rotate~.md) `rotate~` performs equal power rotation for 'n' channels (default 2).
- :material-tune: [__drum.seq__](../objects/drum.seq.md) `drum.seq` provides a drum grid so you can activate cells to represent attacks.
.
- :material-tune: [__button__](../objects/button.md) `button` is a GUI button that opearets in three modes: latch (default), where it responds to mouse clicks and release, and 'bang' and 'toggle' mode.
.
- :material-tune: [__slew2~__](../objects/slew2~.md) `slew2~` is like `slew~` but has independent values for upwards & downwards ramps.
- :material-tune: [__wavetable~__](../objects/wavetable~.md) `wavetable~` is an interpolating wavetable oscillator like `tabosc4~`, but has more features like more interpolation options, inlets for phase sync, phase modulation and also an inlet for scanning through slices.
- :material-tune: [__scope3d~__](../objects/scope3d~.md) `scope3d~` displays signals in 3D.
- :material-tune: [__autofade2~__](../objects/autofade2~.md) `autofade2~` is an automatic fade in/out for multi inputs.
- :material-tune: [__bl.wavetable~__](../objects/bl.wavetable~.md) `bl.wavetable~` is a bandlimited wavetable oscillator abstraction that uses the upsampling/filtering techniquelike, which makes the object quite inefficient CPU wise.
- :material-tune: [__oscbank~__](../objects/oscbank~.md) `oscbank~` is a bank made of `sine~` objects.
- :material-tune: [__osc.format__](../objects/osc.format.md) `osc.format` is similar to Vanilla's `oscformat`.
- :material-tune: [__nyquist~__](../objects/nyquist~.md) `nyquist~` reports the nyquist (which is half the sample rate) as a frequency or period.
- :material-tune: [__sigs~__](../objects/sigs~.md) `sigs~` is like vanilla's `sig~` but generates multichannel signals from an argument list and creates separate inlets for each argument (minimum size is 2).
.
- :material-tune: [__merge__](../objects/merge.md) `merge` takes any type of messages in any inlet and combines them into a list message.
- :material-tune: [__spread.mc~__](../objects/spread.mc~.md) `spread.mc~` spreads any number of input channels across any number of output channels with equal power panning according to a spread parameter.
- :material-tune: [__tanh~__](../objects/tanh~.md) `tanh~` calculates the hyperbolic tangent function of input sample.
- :material-tune: [__score__](../objects/score.md) `score` has a 'tempo' syntax where 'tempo 60' internally sets the bpm to 60! The 'tempo' messages are output in the mid 'data' outlet.
.
- :material-tune: [__echo.rev~__](../objects/echo.rev~.md) `echo.rev~` is an echo/reverb abstraction.
- :material-tune: [__pulsediv~__](../objects/pulsediv~.md) `pulsediv~` outputs impulses when receiving triggers (signal changes from non-positive to positive).
- :material-tune: [__mono~__](../objects/mono~.md) `mono~` emulates monophonic synth behaviour and is much like `mono`, but can also glide the pitch output with a portamento setting.
.
- :material-tune: [__ctl.out__](../objects/ctl.out.md) `ctl.out` formats and sends raw MIDI control messages to Pd's MIDI output and its outlet.
- :material-tune: [__polymetro__](../objects/polymetro.md) `polymetro` is a polyrhythmic metronome.
- :material-tune: [__rand.hist__](../objects/rand.hist.md) `rand.hist` generates weighted randomnumbers based on a histogram (which specifies how many times an index is output).
- :material-tune: [__asr~__](../objects/asr~.md) The `asr~` object in Pure Data is an attack/sustain/release envelope generator, simplified compared to `adsr~`.
- :material-tune: [__bl.saw2~__](../objects/bl.saw2~.md) `bl.saw2~` is a sawtooth oscillator like `else/saw2~`, but it is bandlimited.
- :material-tune: [__shaper~__](../objects/shaper~.md) `shaper~` performs waveshaping with transfer functions, in which signal input values (from -1 to 1) are mapped to the the transfer function's indexes.
- :material-tune: [__smooth2~__](../objects/smooth2~.md) `smooth2~` is just like `smooth~` but has distinct ramp times for both up and down.
.
- :material-tune: [__resonator~__](../objects/resonator~.md) `resonator~` is just like `resonant~`, but the resonance parameter is defined as resonance time in 't60'.
- :material-tune: [__maxpeak~__](../objects/maxpeak~.md) `maxpeak~` returns the maximum peak amplitude so far.
- :material-tune: [__sort__](../objects/sort.md) `sort` sorts messages in ascending or descending order.
.
- :material-tune: [__osc.receive__](../objects/osc.receive.md) `osc.receive` receives OSC messages from network connections and is an abstraction based on `osc.parse` and `netreceive`.
- :material-tune: [__bl.saw~__](../objects/bl.saw~.md) `bl.saw~` is a sawtooth oscillator like `else/saw~`, but it is bandlimited.
- :material-tune: [__pad__](../objects/pad.md) `pad` is a GUI object that reports mouse coordinates over its area and click status.
- :material-tune: [__del~__](../objects/del~.md) `del~` sets and writes to a delay line if created as `del~ in` (default) and reads from it (with interpolation) if created as `del~ out`.
- :material-tune: [__xfade~__](../objects/xfade~.md) `xfade~` crossfades between two sources (that can have 1 to 64 channels each).
- :material-tune: [__function~__](../objects/function~.md) `function~` generates functions from arguments/list input.
- :material-tune: [__delace__](../objects/delace.md) `delace` deinterleaves a list according to the number of outlets.
.
- :material-tune: [__lag~__](../objects/lag~.md) `lag~` is a one pole filter that creates an exponential glide/portamento for its signal input changes.
- :material-tune: [__canvas.mouse__](../objects/canvas.mouse.md) `canvas.mouse` gets mouse click and mouse coordinates when your mouse is interacting with the canvas window.
- :material-tune: [__numbox~__](../objects/numbox~.md) `numbox~` goes into monitor mode when there's a signal connected to it.
- :material-tune: [__pimpmul~__](../objects/pimpmul~.md) `pimpmul~` is a "pimp~" multiplier.
- :material-tune: [__metronome__](../objects/metronome.md) `metronome` understands complex time signatures and outputs timeline data (bar, sub-bar, beat and sub-beat count) and phase output.
- :material-tune: [__above__](../objects/above.md) The `above` object in Pure Data monitors a float input and triggers events based on a threshold.
- :material-tune: [__adsr~__](../objects/adsr~.md) `adsr~` is an attack/decay/sustain/release gated envelope.
- :material-tune: [__phaser~__](../objects/phaser~.md) `phaser~` is a mono phaser effect abstraction.
- :material-tune: [__scale2freq__](../objects/scale2freq.md) `scale2freq` gets a scale as a list of cents values, a base/fundamental pitch and outputs a list of frequency in hertz between a minimum and maximum value.
- :material-tune: [__out4~__](../objects/out4~.md) `out4~` is a convenient quadraphonic input/output abstraction.
- :material-tune: [__sh~__](../objects/sh~.md) `sh~` samples and holds a value from the left inlet.
.
- :material-tune: [__brown~__](../objects/brown~.md) `brown~` is a brown noise generator (aka brownian noise or red noise), whose spectral energy drops 6dB per octave (sounding less hissy than white noise).
- :material-tune: [__unmerge__](../objects/unmerge.md) `unmerge` separates the elements of a message in groups of any size (default 1).
- :material-tune: [__datetime__](../objects/datetime.md) `datetime` gives us current/local date (right outlet) and time (left outlet) as lists.
.
- :material-tune: [__drunkard~__](../objects/drunkard~.md) `drunkard~` generates random nvalues within a given step range from the last output.
- :material-tune: [__delete__](../objects/delete.md) `delete` deletes one or more elements from an input message.
- :material-tune: [__play.file~__](../objects/play.file~.md) `play.file~` reads/plays files from your computer similarly to Vanilla's `readsf~`, but it supports more file formats (officialy AAC, AIF, CAF, FLAC, MP3, OGG, OPUS & WAV).
- :material-tune: [__ceil~__](../objects/ceil~.md) `ceil~` is a ceil math function for signals.
- :material-tune: [__sample~__](../objects/sample~.md) `sample~` is an abstraction that creates an audio buffer which you can use to load a sample or record into.
- :material-tune: [__format__](../objects/format.md) `format` formats symbols similarly to `makefilename`, but it accepts more than one '%' variable, where each corresponds to an inlet.
.
- :material-tune: [__mouse__](../objects/mouse.md) `mouse` grabs mouse interaction (click and coordinates).
.
- :material-tune: [__db2lin~__](../objects/db2lin~.md) `db2lin~` converts amplitude values from deciBel Full Scale (dBFS) to linear.
- :material-tune: [__any2symbol__](../objects/any2symbol.md) `any2symbol` converts any message to a symbol message.
.
- :material-tune: [__function__](../objects/function.md) `function` is a breakpoints function GUI, mainly used with `function~` or `envgen~`.
- :material-tune: [__phaseseq~__](../objects/phaseseq~.md) `phaseseq~` takes a list of thresholds and outputs impulses when reaching the threshold values.
.
- :material-tune: [__gaterelease__](../objects/gaterelease.md) `gaterelease` allows you to release one gate in your patch while you still hold another.
- :material-tune: [__rand.f__](../objects/rand.f.md) `rand.f` generates random float values for a given range when triggered with a bang.
- :material-tune: [__unite__](../objects/unite.md) `unite` unites and converts messages into a symbol message.
.
- :material-tune: [__envelope~__](../objects/envelope~.md) `envelope~` provides 6 different envelopes, which are generated via a phase input.
.
- :material-tune: [__brown__](../objects/brown.md) `brown` is a control brownian motion generator.
- :material-tune: [__setdsp~__](../objects/setdsp~.md) `setdsp~` is a convenient abstraction to display and set Pd's audio engine (aka 'DSP') state.
- :material-tune: [__gaussian~__](../objects/gaussian~.md) `gaussian~` is a gaussian oscillator.
- :material-tune: [__plaits~__](../objects/plaits~.md) `plaits~` is a Pure Data external based on the "Plaits" macro-oscillator module by Mutable Instruments.
- :material-tune: [__xmod~__](../objects/xmod~.md) `xmod~` performs cross modulation of two sine oscillators.
- :material-tune: [__resonator2~__](../objects/resonator2~.md) `resonator2~` is a wrap around `cpole~`.
- :material-tune: [__abs.pd~__](../objects/abs.pd~.md) The `abs.pd~` object in Pure Data loads a `.pd` file into a subprocess, providing two signal inlets and two signal outlets.
- :material-tune: [__glide~__](../objects/glide~.md) `glide~` generates a glide/portamento from its signal input changes.
- :material-tune: [__xgate2.mc~__](../objects/xgate2.mc~.md) `xgate2.mc~` routes an input signal to 'n' specified channels in a multichannel output with crossfading between adjacent channels according to a spread parameter.
.
- :material-tune: [__group__](../objects/group.md) `group` groups messages according to a group size.
- :material-tune: [__ramp~__](../objects/ramp~.md) `ramp~` is a resettable linear ramp between a minimum and maximum value.
- :material-tune: [__pic__](../objects/pic.md) `pic` loads image pictures that you can interact with.
- :material-tune: [__mtx~__](../objects/mtx~.md) `mtx~` routes signals from any inlets to one or more outlets.
- :material-tune: [__hz2rad__](../objects/hz2rad.md) `hz2rad` converts a frequency in Hertz to "Radians per Sample" - which depends on the patch's sample rate (sr).
- :material-tune: [__lfo__](../objects/lfo.md) `lfo` is a control rate LFO with some common waveforms.
.
- :material-tune: [__pol2car~__](../objects/pol2car~.md) `pol2car~` converts polar coordinates (amplitude / phase) to cartesian coordinates (real / imaginary).
.
- :material-tune: [__sr~__](../objects/sr~.md) `sr~` can set the sample rate and also reports the sample rate frequency or period when loading the patch, when receiving a bang or when it changes.
- :material-tune: [__voices~__](../objects/voices~.md) `voices~` is an abstraction based on `voices` and generates multichannel signals that can be used to control pitch and gate with polyphony.
.
- :material-tune: [__xselect2.mc~__](../objects/xselect2.mc~.md) `xselect2.mc~` selects from 'n' inputs with crossfading between adjacent channels according to a spread parameter.
.
- :material-tune: [__var__](../objects/var.md) `var` is similar to `value` but it can set and recall more than one variable as lists.
.
- :material-tune: [__rampnoise~__](../objects/rampnoise~.md) `rampnoise~` is a low frequency (band limited) noise generator with interpolation, therefore it ramps from one random value to another, resulting in random ramps.
- :material-tune: [__gendyn~__](../objects/gendyn~.md) `gendyn~` implements "Dynamic Strochastic Synthesis" based on Xenakis' GenDyn algorithm.
- :material-tune: [__osc.send__](../objects/osc.send.md) `osc.send` sends OSC messages over the network and is an abstraction based on `osc.format` and `netsend`.
- :material-tune: [__ptouch.out__](../objects/ptouch.out.md) `ptouch.out` formats and sends raw MIDI polyphonic aftertouch messages to Pd's MIDI output and its outlet..
- :material-tune: [__gatehold__](../objects/gatehold.md) `gatehold` holds a gate value for a certain amount of time (specified in ms) after the gate has closed.
- :material-tune: [__crusher~__](../objects/crusher~.md) `crusher~` is a bit-crusher/reducer and decimator abstraction based on the objects `quantizer~` (mode 4) and `downsample~`, where an input signal quantized and downsampled to generate distortion and aliasing.
- :material-tune: [__synth~__](../objects/synth~.md) `synth~` is multichannel aware and can send a multichannel signal out with the '-mc' flag or message.
.
- :material-tune: [__randpulse~__](../objects/randpulse~.md) `randpulse~` is a random pulse train oscillator (which alternates between a random value and 0, or on/off).
- :material-tune: [__receiver__](../objects/receiver.md) `receiver` is kinda like vanilla's `receive`.
- :material-tune: [__allpass.filt~__](../objects/allpass.filt~.md) `allpass.filt~` is an allpass filter that you can set its order with the first argument (needs to be a multiple of 2).
- :material-tune: [__square~__](../objects/square~.md) `square~` is a square oscillator that accepts negative frequencies, has inlets for pulse width, phase sync and phase modulation.
- :material-tune: [__giga.rev~__](../objects/giga.rev~.md) `giga.rev~` is a stereo reverb in Else based on Juhana Sadeharju’s *Gigaverb* algorithm, known for producing large, spacious, and dense reverberation tails.
- :material-tune: [__ctl.in__](../objects/ctl.in.md) `ctl.in` extracts MIDI CC information from raw MIDI input or a connected MIDI device.
.
- :material-tune: [__stepnoise~__](../objects/stepnoise~.md) `stepnoise~` is a low frequency (band limited) noise generator without interpolation, therefore it holds at a random value, resulting in random steps.
- :material-tune: [__fm~__](../objects/fm~.md) `fm~` is a simple frequency modulation unit consisting of a pair of sinusoidal oscillators, where one modulates the frequency input of another.
- :material-tune: [__lag2~__](../objects/lag2~.md) `lag2~` is like `lag~` but has a different time for ramp up and ramp down.
- :material-tune: [__rand.u__](../objects/rand.u.md) `rand.u` generates an unrepeated random values (from 0 to size-1).
- :material-tune: [__bl.vsaw~__](../objects/bl.vsaw~.md) `bl.vsaw~` is a variable sawtooth waveform oscillator that also becomes a triangular osccilator just like `else/vsaw~`, but it is bandlimited.
- :material-tune: [__args__](../objects/args.md) The `args` object in Pure Data loads and manages the arguments of an abstraction, allowing them to be queried or changed dynamically.
- :material-tune: [__dispatch__](../objects/dispatch.md) The `dispatch` object in Pure Data takes a list and sends each element to specified receive addresses in left-to-right order.
- :material-tune: [__pitch.shift~__](../objects/pitch.shift~.md) `pitch.shift~` is a pitch shifter abstraction based on granulation.
- :material-tune: [__rint__](../objects/rint.md) `rint` takes floats and rounds them to the nearest integer value.
.
- :material-tune: [__osc.route__](../objects/osc.route.md) `osc.route` routes OSC messages received from `osc.receive`.
- :material-tune: [__pick~__](../objects/pick~.md) `pick~` picks a channel from a multichannel connection.
- :material-tune: [__trunc__](../objects/trunc.md) `trunc` truncates floats and lists towards zero, that means only the integer value is considered, like in vanilla's `int`.
.
- :material-tune: [__tabreader__](../objects/tabreader.md) `tabreader` accepts indexes from 0 to 1 by default and reads an array with different interpolation methods with multi channel support.
- :material-tune: [__filterdelay~__](../objects/filterdelay~.md) `filterdelay~` is a high level delay unit that goes thgouh a resonant lowpass filter, a soft clipper and a DC filter.
- :material-tune: [__pulse~__](../objects/pulse~.md) `pulse~` is a pulse train oscillator (alternates between 1 and 0, or on/off) that accepts negative frequencies, has inlets for pulse width, phase sync and phase modulation.
- :material-tune: [__pm~__](../objects/pm~.md) `pm~` is a very basic and simple phase modulation unit, which consists of a pair of sinusoidal oscillators, where one modulates the phase input of another.
- :material-tune: [__norm~__](../objects/norm~.md) `norm~` is a normalizer abstraction based on `mov.rms~`.
- :material-tune: [__amean__](../objects/amean.md) `amean` creates a list of arithmetic means.
- :material-tune: [__level~__](../objects/level~.md) `level~` is a convenient abstraction for adjusting a signal's gain in dB.
- :material-tune: [__float2imp~__](../objects/float2imp~.md) `float2imp~` converts floats to impulses with sample accuracy.
- :material-tune: [__bicoeff__](../objects/bicoeff.md) `bicoeff` is a GUI that generates coefficients for vanilla's `biquad~` according to different filter types ("eq" filter by default as in the example below).
- :material-tune: [__dir__](../objects/dir.md) The `dir` object in Pure Data is used to access and manage files from directories.
- :material-tune: [__loadbanger__](../objects/loadbanger.md) `loadbanger` works with both kinds of bangs.
- :material-tune: [__midi2note__](../objects/midi2note.md) `midi2note` converts a MIDI pitch value to note names (such as Eb3).
- :material-tune: [__scope~__](../objects/scope~.md) `scope~` displays signals in the style of an oscilloscope.
- :material-tune: [__gatehold~__](../objects/gatehold~.md) `gatehold~` holds a gate value for a certain amount of time (specified in ms) after the gate has closed.
- :material-tune: [__combine__](../objects/combine.md) `combine` collects messages (with one or more elements) into a single list if they come within a certain given amount of time, but not if greater than it.
- :material-tune: [__sig2float~__](../objects/sig2float~.md) `sig2float~` converts signals to floats.
- :material-tune: [__revdelay~__](../objects/revdelay~.md) `revdelay~` is a reverse delay effect.
- :material-tune: [__blip~__](../objects/blip~.md) `blip~` uses DSF (Discrete-Summation Formulae) to generate waveforms as a sum of cosines.
- :material-tune: [__note.in__](../objects/note.in.md) `note.in` extracts MIDI Pitch information from external "raw" MIDI data or an internally connected device.
- :material-tune: [__select~__](../objects/select~.md) `select~` selects an input signal without crossfade and the signals can be of different channel sizes.
- :material-tune: [__repeat~__](../objects/repeat~.md) `repeat~` takes an input signal os any channel size and repeats it 'n' times.
.
- :material-tune: [__mtx.mc~__](../objects/mtx.mc~.md) `mtx.mc~` routes a channel signal from a multichannel input to one or more channels of a multichannel output.
.
- :material-tune: [__gain~__](../objects/gain~.md) `gain~` is a convenient mono gain abstraction for adjusting a signal's gain.
- :material-tune: [__perlin~__](../objects/perlin~.md) `perlin~` is an abastraction that implements 1-dimensional Perlin Noise (a type of gradient noise developed by Ken Perlin).
- :material-tune: [__power~__](../objects/power~.md) `power~` is a power function waveshaper for signals that extends the usual definition of exponentiation and returns -pow(-a, b) when you have a negative signal input.
- :material-tune: [__tri~__](../objects/tri~.md) `tri~` is a triangular wave oscillator that accepts negative frequencies, has inlets for phase sync and phase modulation.
- :material-tune: [__bl.square~__](../objects/bl.square~.md) `bl.square~` is a square oscillator like `else/square~`, but it is bandlimited.
- :material-tune: [__suspedal__](../objects/suspedal.md) `suspedal` holds MIDI Note Off messages when on and sends them out when it's switched off.
- :material-tune: [__knob__](../objects/knob.md) `knob` has an exponential and log feature just like the `rescale` object.
- :material-tune: [__dec2hex__](../objects/dec2hex.md) `dec2hex` converts decimal values to hexadecimal ones.
- :material-tune: [__markov__](../objects/markov.md) `markov` creates Markov chains of any order out of progressions of floats, symbols or lists (which can be used to create polyphonic chains).
- :material-tune: [__histogram__](../objects/histogram.md) `histogram` records into a table how many times it received a positive integer number (treated as indexes, floats are truncated).
- :material-tune: [__resonbank2~__](../objects/resonbank2~.md) `resonbank2~` is a bank of resonators made of `resonator2~` objects.
- :material-tune: [__bpbank~__](../objects/bpbank~.md) `bpbank~` is a bank made of `bandpass~` objects.
- :material-tune: [__lace__](../objects/lace.md) `lace` interleaves two or more lists.
- :material-tune: [__compress~__](../objects/compress~.md) `compress~` is an abstraction that performs compression.
- :material-tune: [__mpe.in__](../objects/mpe.in.md) `mpe.in` sends "cooked" MPE data from external "raw" MIDI data or an internally connected device.
- :material-tune: [__meter~__](../objects/meter~.md) `meter~` is a convenient mono VU-meter abstraction.
- :material-tune: [__gain2~__](../objects/gain2~.md) `gain2~` is a convenient stereo gain abstraction, so you can adjust a stereo signal's gain.
- :material-tune: [__sfz~__](../objects/sfz~.md) `sfz~` also has microtonal capabilities.
- :material-tune: [__display__](../objects/display.md) `display` can display a message just like `print`.
- :material-tune: [__rand.dist__](../objects/rand.dist.md) `rand.dist` is an abstraction based on `array quantile` and generates random numbers that follow a probability density function (given by an array).
- :material-tune: [__fold__](../objects/fold.md) `fold` folds between a low and high value.
- :material-tune: [__tabgen__](../objects/tabgen.md) `tabgen` is an abstraction that generates different functions for a given table name.
.
- :material-tune: [__beat~__](../objects/beat~.md) `beat~` takes an input signal and outputs a detected BPM value.
.
- :material-tune: [__sequencer__](../objects/sequencer.md) `sequencer` sends an element from a given sequence when banged.
- :material-tune: [__stretch.shift~__](../objects/stretch.shift~.md) `stretch.shift~` is like `gran.player~`, but for live input.
- :material-tune: [__changed~__](../objects/changed~.md) The `changed~` object in Pure Data monitors an input signal and outputs an impulse whenever the signal changes by an amount equal to or greater than a specified threshold.
- :material-tune: [__mix2~__](../objects/mix2~.md) `mix2~` has support for multichannel input.
.
- :material-tune: [__sfinfo__](../objects/sfinfo.md) `sfinfo` supports all files that `sfload` and `play.file~` support and can be used to query file sample information but so far only channels and 'inst' info for aif files (this object is still very experimental).
.
- :material-tune: [__quantizer__](../objects/quantizer.md) `quantizer` approximates a value to step values defined by the argument.
- :material-tune: [__pick__](../objects/pick.md) `pick` picks an element from an input message according to an element number.
- :material-tune: [__send2~__](../objects/send2~.md) `send2~` is like send but automatically resizes according to the number of input channels.
.
- :material-tune: [__rotate.mc~__](../objects/rotate.mc~.md) `rotate.mc~` performs equal power rotation for any number of channels given by a multichannel signal input.
- :material-tune: [__decay~__](../objects/decay~.md) `decay~` is based on SuperCollider's "Decay" UGEN.
- :material-tune: [__speed__](../objects/speed.md) `speed` is somewhat related to `line`.
- :material-tune: [__rand.i~__](../objects/rand.i~.md) `rand.i~` generates random integer values for a given range when triggered.
- :material-tune: [__fbsine~__](../objects/fbsine~.md) `fbsine~` is a sinusoidal oscillator with phase modulation feedback.
- :material-tune: [__hex2dec__](../objects/hex2dec.md) `hex2dec` converts hexadecimal values to decimal ones.
- :material-tune: [__saw~__](../objects/saw~.md) `saw~` is a sawtooth wave oscillator that accepts negative frequencies, has inlets for phase sync and phase modulation.
- :material-tune: [__saw2~__](../objects/saw2~.md) `saw2~` is a sawtooth wave oscillator that accepts negative frequencies, has inlets for phase sync and phase modulation.
- :material-tune: [__player~__](../objects/player~.md) `player~` is a convenient abstraction based on `sfload` (so it supports the same file formats, check it's help file) and `tabplayer~`.
- :material-tune: [__sine~__](../objects/sine~.md) `sine~` is a sinusoidal oscillator that accepts negative frequencies, has inlets for phase sync and phase modulation.
- :material-tune: [__meter2~__](../objects/meter2~.md) `meter2~` is a convenient stereo VU-meter abstraction.
- :material-tune: [__pvoc.live~__](../objects/pvoc.live~.md) `pvoc.live~` is like `pvoc.player~`, but for live input.
- :material-tune: [__gmean__](../objects/gmean.md) `gmean` creates a list of geometric means.
- :material-tune: [__noisegate~__](../objects/noisegate~.md) `noisegate~` is a noise gate abstraction.
- :material-tune: [__sum__](../objects/sum.md) `sum` sums a list of values.
.
- :material-tune: [__mono__](../objects/mono.md) `mono` takes note messages and handles them to emulate monophonic synth behaviour.
- :material-tune: [__voices__](../objects/voices.md) `voices` outputs a list with voice index, pitch, velocity and optional extra stuff.
- :material-tune: [__velvet~__](../objects/velvet~.md) `velvet~` is a velvet noise generator, which randomly chooses either positive (1) or negative (-1) impulses at random positions in a given period set in Hz.
- :material-tune: [__touch.out__](../objects/touch.out.md) `touch.out` formats and sends raw MIDI aftertouch messages to Pd's MIDI output and its outlet.
- :material-tune: [__samps2ms~__](../objects/samps2ms~.md) `samps2ms~` is a simple abstraction that converts time values number of samples to ms.
- :material-tune: [__midi.learn__](../objects/midi.learn.md) `midi.learn` is an abstraction based on `savestate` that learns and saves any MIDI input data.
- :material-tune: [__ptouch.in__](../objects/ptouch.in.md) `ptouch.in` extracts MIDI polyphonic aftertouch information from raw MIDI input (such as from `midiin`).
.
- :material-tune: [__remove__](../objects/remove.md) `remove` removes one or more number elements from a list.
- :material-tune: [__xselect.mc~__](../objects/xselect.mc~.md) `xselect.mc~` selects between multiple channels from a multichannel connection (maximum 512 channels) with equal power crossfading.
.
- :material-tune: [__morph~__](../objects/morph~.md) `morph~` allows you to make a spectral crossfade between the amplitudes and phases of two inputs.
- :material-tune: [__xselect2~__](../objects/xselect2~.md) `xselect2~` selects from 'n' inputs with crossfading between adjacent channels according to a spread parameter.
.
- :material-tune: [__mix4~__](../objects/mix4~.md) `mix4~` has support for multichannel input.
.
- :material-tune: [__colors__](../objects/colors.md) `colors` can output color values specially for Pd Vanilla's GUI objects (aka iemgus) and Data Structures.
- :material-tune: [__pattern__](../objects/pattern.md) `pattern` is a rhythmic pattern sequencer.
- :material-tune: [__pink~__](../objects/pink~.md) `pink~` is a pink noise generator, which sounds less hissy than white noise (but not as less as brown~).
- :material-tune: [__keymap__](../objects/keymap.md) `keymap` maps your computer keyboard to MIDI pitches and generates note on/off messages when keys get pressed and released.
- :material-tune: [__pimp~__](../objects/pimp~.md) `pimp~` is very convenient for both driving a process with its phase output (such as reading a sample or envelope) and also triggering at period transitions other objects or processes (such as with `sh~` below).
.
- :material-tune: [__bitnormal~__](../objects/bitnormal~.md) `bitnormal~` replaces NaN (not a number), +/- infinity values and denormals of an incoming signal with zero (hence, it only lets 'normal' floats through.
- :material-tune: [__router__](../objects/router.md) `router` routes a message from the left inlet to an outlet number specified by the float into the right inlet (if the number is out of range, the message is not output).
.
- :material-tune: [__lin2db~__](../objects/lin2db~.md) `lin2db~` converts amplitude values from linear to a deciBel Full Scale (dBFS) with support for multichannel signals.
- :material-tune: [__osc.parse__](../objects/osc.parse.md) `osc.parse` is similar to Vanilla's `oscparse` but the output is not a list and more closely related on how OSC messages are generally dealt with.
- :material-tune: [__freeze~__](../objects/freeze~.md) `freeze~` is an abstraction based on `sigmund~` (analysis & ressynthesis).
- :material-tune: [__bl.osc~__](../objects/bl.osc~.md) `bl.osc~` is a bandlimited oscillator based on `else/wavetable~`.
- :material-tune: [__keycode__](../objects/keycode.md) `keycode` outputs key codes from your keyboard based on their physical location, so it is layout independent (but please don't change layout after loading Pd and the object, this is problematic specially on Windows..
- :material-tune: [__notedur2ratio__](../objects/notedur2ratio.md) `notedur2ratio` converts from a note duration symbolic syntax to a ratio (either as fraction or float).
- :material-tune: [__db2lin__](../objects/db2lin.md) `db2lin` converts amplitude values from deciBel Full Scale (dBFS) to linear.
- :material-tune: [__out.mc~__](../objects/out.mc~.md) `out.mc~` takes multichannel signals and outputs them from given `dac~` channel output (default 1).
- :material-tune: [__rm~__](../objects/rm~.md) `rm~` is a Ring Modulation abstraction.
- :material-tune: [__autofade~__](../objects/autofade~.md) `autofade~` is an automatic fade in/out for multi inputs.
- :material-tune: [__rms~__](../objects/rms~.md) `rms~` is similar to Pd Vanilla's `env~`, but it reports the RMS value in linear amplitude (default) or in dBFS.
.
- :material-tune: [__note2midi__](../objects/note2midi.md) `note2midi` converts note names (such as 'C4') to MIDI pitch values.
- :material-tune: [__slice~__](../objects/slice~.md) `slice~` splits a multichannel signal.
- :material-tune: [__rand.i__](../objects/rand.i.md) `rand.i` generates random integer values for a given range when triggered with as bang.Use the seed message if you want a reproducible output.
- :material-tune: [__randpulse2~__](../objects/randpulse2~.md) `randpulse2~` is a random pulse train oscillator.
- :material-tune: [__bend.out__](../objects/bend.out.md) `bend.out` formats and sends raw MIDI pitch bend messages to Pd's MIDI output and its outlet.
- :material-tune: [__op~__](../objects/op~.md) `op~` is a signal operator where the first argument defines the the type (for either comparison, bitwise, logic and modulus operations).
- :material-tune: [__sender__](../objects/sender.md) `sender` is much like vanilla's `send`, but can have up to two names and at load time can expand dollar symbols according to parent patches.
.
- :material-tune: [__conv~__](../objects/conv~.md) `conv~` performs partitioned convolution.
- :material-tune: [__get~__](../objects/get~.md) `get~` gets one or more channels from a multichannel connection.
- :material-tune: [__score2__](../objects/score2.md) `score2` has a 'tempo' syntax where 'tempo 60' sets the bpm to 60! The 'tempo' messages are output in the third 'data' outlet.
- :material-tune: [__autotune__](../objects/autotune.md) `autotune` receives a scale as a list of steps in cents and a base MIDI pitch value (default 60).
- :material-tune: [__note__](../objects/note.md) `note` is a GUI meant only to display text notes.
</div>