<div class="grid cards" markdown>
- :material-tune: [__out~__](../objects/out~.md) `out~` has a built in `sum~` object, so it can take multichannel signals and sum them together for each input.
.

- :material-tune: [__unmerge~__](../objects/unmerge~.md) `unmerge~` separates the channels of a multichannel signal in groups of any size (default 1).

- :material-tune: [__grab__](../objects/grab.md) `grab` sets the value of GUIs but also grabs its ouotput.

- :material-tune: [__pdlink__](../objects/pdlink.md) `pdlink` allows you to communicate to/from different Pd instances over local network, as different versions and even forks of Pure Data (such as plugdata).

- :material-tune: [__presets__](../objects/presets.md) `presets` manages presets for patches and abstractions and has interpolation and morphing features.

- :material-tune: [__xgate2~__](../objects/xgate2~.md) `xgate2~` routes an input signal to 'n' specified outlets with crossfading between adjacent channels according to a spread parameter.
.

- :material-tune: [__pdlink~__](../objects/pdlink~.md) `pdlink~` allows you to send/receive audio streans to/from different Pd instances, as different versions, platforms and even forks of Pure Data (such as PlugData).

- :material-tune: [__canvas.setname__](../objects/canvas.setname.md) `canvas.setname` sets a symbol name to a canvas so you can send it messages.

- :material-tune: [__scales__](../objects/scales.md) `scales` generates scales as note names (default) or MIDI pitches.

- :material-tune: [__vocoder~__](../objects/vocoder~.md) `vocoder~` is classic cross synthesis channel vocoder abstraction.
.

- :material-tune: [__delace~__](../objects/delace~.md) `delace~` deinterleaves a multichannel signal according to the number of outlets.
.

- :material-tune: [__pipe2__](../objects/pipe2.md) `pipe2` is similar to vanilla's pipe.

- :material-tune: [__nchs~__](../objects/nchs~.md) `nchs~` gets the number of channels from a multi-channel connection, as provided by `snake~ in`, `clone` or other objects.

- :material-tune: [__matrix~__](../objects/matrix~.md) `matrix~` routes signals from any inlets to one or more outlets.

- :material-tune: [__nyquist~__](../objects/nyquist~.md) `nyquist~` reports the nyquist (which is half the sample rate) as a frequency or period.

- :material-tune: [__sigs~__](../objects/sigs~.md) `sigs~` is like vanilla's `sig~` but generates multichannel signals from an argument list and creates separate inlets for each argument (minimum size is 2).
.

- :material-tune: [__lores~__](../objects/lores~.md) `lores~` implements an inexpensive resonant lowpass filter.

- :material-tune: [__pulsediv~__](../objects/pulsediv~.md) `pulsediv~` outputs impulses when receiving triggers (signal changes from non-positive to positive).

- :material-tune: [__ctl.out__](../objects/ctl.out.md) `ctl.out` formats and sends raw MIDI control messages to Pd's MIDI output and its outlet.

- :material-tune: [__rand.hist__](../objects/rand.hist.md) `rand.hist` generates weighted randomnumbers based on a histogram (which specifies how many times an index is output).

- :material-tune: [__resonator~__](../objects/resonator~.md) `resonator~` is just like `resonant~`, but the resonance parameter is defined as resonance time in 't60'.

- :material-tune: [__maxpeak~__](../objects/maxpeak~.md) `maxpeak~` returns the maximum peak amplitude so far.

- :material-tune: [__zl__](../objects/zl.md) `zl` processes messages with one or more elements ("list messages' or "anything") according to a mode set via argument/message or in the object name after a `.` (dot)..

- :material-tune: [__canvas.mouse__](../objects/canvas.mouse.md) `canvas.mouse` gets mouse click and mouse coordinates when your mouse is interacting with the canvas window.

- :material-tune: [__numbox~__](../objects/numbox~.md) `numbox~` goes into monitor mode when there's a signal connected to it.

- :material-tune: [__sh~__](../objects/sh~.md) `sh~` samples and holds a value from the left inlet.
.

- :material-tune: [__datetime__](../objects/datetime.md) `datetime` gives us current/local date (right outlet) and time (left outlet) as lists.
.

- :material-tune: [__delete__](../objects/delete.md) `delete` deletes one or more elements from an input message.

- :material-tune: [__format__](../objects/format.md) `format` formats symbols similarly to `makefilename`, but it accepts more than one '%' variable, where each corresponds to an inlet.
.

- :material-tune: [__function__](../objects/function.md) `function` is a breakpoints function GUI, mainly used with `function~` or `envgen~`.

- :material-tune: [__gaterelease__](../objects/gaterelease.md) `gaterelease` allows you to release one gate in your patch while you still hold another.

- :material-tune: [__setdsp~__](../objects/setdsp~.md) `setdsp~` is a convenient abstraction to display and set Pd's audio engine (aka 'DSP') state.

- :material-tune: [__sr~__](../objects/sr~.md) `sr~` can set the sample rate and also reports the sample rate frequency or period when loading the patch, when receiving a bang or when it changes.

- :material-tune: [__xselect2.mc~__](../objects/xselect2.mc~.md) `xselect2.mc~` selects from 'n' inputs with crossfading between adjacent channels according to a spread parameter.
.

- :material-tune: [__ptouch.out__](../objects/ptouch.out.md) `ptouch.out` formats and sends raw MIDI polyphonic aftertouch messages to Pd's MIDI output and its outlet..

- :material-tune: [__receiver__](../objects/receiver.md) `receiver` is kinda like vanilla's `receive`.

- :material-tune: [__triangle~__](../objects/triangle~.md) `triangle~` is a triangular wavetable that is read with phase values from 0 to 1 into the first inlet- a `phasor~` input turns it into a wavetable oscillator.

- :material-tune: [__args__](../objects/args.md) The `args` object in Pure Data loads and manages the arguments of an abstraction, allowing them to be queried or changed dynamically.

- :material-tune: [__dispatch__](../objects/dispatch.md) The `dispatch` object in Pure Data takes a list and sends each element to specified receive addresses in left-to-right order.

- :material-tune: [__mtr__](../objects/mtr.md) `mtr` records any messages in different tracks and plays them back.

- :material-tune: [__float2imp~__](../objects/float2imp~.md) `float2imp~` converts floats to impulses with sample accuracy.

- :material-tune: [__trough__](../objects/trough.md) `trough` compares the input to a 'trough' (minimum) value.

- :material-tune: [__mtx.mc~__](../objects/mtx.mc~.md) `mtx.mc~` routes a channel signal from a multichannel input to one or more channels of a multichannel output.
.

- :material-tune: [__markov__](../objects/markov.md) `markov` creates Markov chains of any order out of progressions of floats, symbols or lists (which can be used to create polyphonic chains).

- :material-tune: [__rand.dist__](../objects/rand.dist.md) `rand.dist` is an abstraction based on `array quantile` and generates random numbers that follow a probability density function (given by an array).

- :material-tune: [__stretch.shift~__](../objects/stretch.shift~.md) `stretch.shift~` is like `gran.player~`, but for live input.

- :material-tune: [__mix2~__](../objects/mix2~.md) `mix2~` has support for multichannel input.
.

- :material-tune: [__send2~__](../objects/send2~.md) `send2~` is like send but automatically resizes according to the number of input channels.
.

- :material-tune: [__speed__](../objects/speed.md) `speed` is somewhat related to `line`.

- :material-tune: [__sine~__](../objects/sine~.md) `sine~` is a sinusoidal oscillator that accepts negative frequencies, has inlets for phase sync and phase modulation.

- :material-tune: [__midi.learn__](../objects/midi.learn.md) `midi.learn` is an abstraction based on `savestate` that learns and saves any MIDI input data.

- :material-tune: [__remove__](../objects/remove.md) `remove` removes one or more number elements from a list.

- :material-tune: [__xselect2~__](../objects/xselect2~.md) `xselect2~` selects from 'n' inputs with crossfading between adjacent channels according to a spread parameter.
.

- :material-tune: [__mix4~__](../objects/mix4~.md) `mix4~` has support for multichannel input.
.

- :material-tune: [__keycode__](../objects/keycode.md) `keycode` outputs key codes from your keyboard based on their physical location, so it is layout independent (but please don't change layout after loading Pd and the object, this is problematic specially on Windows..

- :material-tune: [__rms~__](../objects/rms~.md) `rms~` is similar to Pd Vanilla's `env~`, but it reports the RMS value in linear amplitude (default) or in dBFS.
.

- :material-tune: [__table__](../objects/table.md) `table` stores and edits a number array.

- :material-tune: [__slice~__](../objects/slice~.md) `slice~` splits a multichannel signal.

- :material-tune: [__sender__](../objects/sender.md) `sender` is much like vanilla's `send`, but can have up to two names and at load time can expand dollar symbols according to parent patches.
.

- :material-tune: [__get~__](../objects/get~.md) `get~` gets one or more channels from a multichannel connection.

- :material-tune: [__note__](../objects/note.md) `note` is a GUI meant only to display text notes.

</div>