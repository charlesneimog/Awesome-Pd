<div class="grid cards" markdown>
- :material-tune: [__out~__](../objects/out~.md) `out~` has a built in `sum~` object, so it can take multichannel signals and sum them together for each input.
.

- :material-tune: [__l.readsvg__](../objects/l.readsvg.md) `l.readsvg` is a `pdlua` object designed to read SVG files created or edited in Inkscape.

- :material-tune: [__quantizer~__](../objects/quantizer~.md) `quantizer~` approximates a value to step values defined by the argument.

- :material-tune: [__keyboard__](../objects/keyboard.md) `keyboard` takes MIDI notes and also generates them via clicking.
.

- :material-tune: [__grab__](../objects/grab.md) `grab` sets the value of GUIs but also grabs its ouotput.

- :material-tune: [__pdlink__](../objects/pdlink.md) `pdlink` allows you to communicate to/from different Pd instances over local network, as different versions and even forks of Pure Data (such as plugdata).

- :material-tune: [__out8~__](../objects/out8~.md) `out8~` is a convenient octaphonic input/output abstraction.

- :material-tune: [__envgen~__](../objects/envgen~.md) `envgen~` is an envelope (and an all purpose line) generator (here it creates a 1000 ms line to 1 and then a 500 ms line to 0).

- :material-tune: [__store__](../objects/store.md) `store` is an abstraction based on `text` that stores incoming messages sequentially.
.

- :material-tune: [__bl.imp2~__](../objects/bl.imp2~.md) `bl.imp2~` is a two sided impulse oscillator like `else/imp2~`, but it is bandlimited.
.

- :material-tune: [__canvas.setname__](../objects/canvas.setname.md) `canvas.setname` sets a symbol name to a canvas so you can send it messages.

- :material-tune: [__touch.in__](../objects/touch.in.md) `touch.in` extracts MIDI Aftertouch information from raw MIDI input or a connected MIDI device.
.

- :material-tune: [__circle__](../objects/circle.md) `circle` is a two dimensional slider GUI abstraction with a circular area (see also [else/slider2d).
.

- :material-tune: [__op__](../objects/op.md) `op` provides many operators and is most useful for lists, as there are objects in Pd Vanilla for most of these operations.
.

- :material-tune: [__equal__](../objects/equal.md) `equal` compares lists and outputs 1 if they're the same or 0 if they're not.

- :material-tune: [__autotune2__](../objects/autotune2.md) `autotune2` receives a scale as a list of steps in cents and then retunes incoming cents values to the closest step in the scale.
.

- :material-tune: [__loop__](../objects/loop.md) `loop` is a loop counter, but it can also loop bangs like `until` (using the -b flag).

- :material-tune: [__float2sig~__](../objects/float2sig~.md) `float2sig~` (or `f2s~` for short) is an abstraction based on `vline~` that converts floats to signals or lists to multichannel signals.

- :material-tune: [__midi.out__](../objects/midi.out.md) `midi.out` sends MIDI data from "cooked" data, instead of "raw" data like `midiout`.

- :material-tune: [__pack2__](../objects/pack2.md) `pack2` is kinda similar to Pd Vanilla's `pack`, but any inlet triggers the output (though a "set" message avoids the output).

- :material-tune: [__slice__](../objects/slice.md) `slice` splits lists.

- :material-tune: [__note.out__](../objects/note.out.md) `note.out` formats and sends raw MIDI pitch messages to Pd's MIDI output and its outlet.

- :material-tune: [__urn__](../objects/urn.md) `urn` generates random numbers in a range defined by the 'n' size (from 0 to n-1) without repeating them.

- :material-tune: [__maximum__](../objects/maximum.md) `maximum` outputs the maximum of two or more values.

- :material-tune: [__oscnoise~__](../objects/oscnoise~.md) `oscnoise~` is an oscillator that accepts negative frequencies, has inlets for phase sync and phase modulation.

- :material-tune: [__l.attrfilter__](../objects/l.attrfilter.md) The `l.attrfilter` object in Pure Data (using `pdlua`) filters elements from an SVG file loaded with [`l.readsvg`](l.readsvg.md) based on attributes such as stroke, fill, or ID.

- :material-tune: [__round__](../objects/round.md) `round` approximates positive and negative numbers to an integer multiple of any given number that is greater or equal to 0 (0 makes no approximation, so the original input is output unchanged).
.

- :material-tune: [__damp.osc~__](../objects/damp.osc~.md) `damp.osc~` is an abstraction based `reonant2~` and also very very similar to it (to the point I think it wasn't worth having two objects with such subtle differences).

- :material-tune: [__pipe2__](../objects/pipe2.md) `pipe2` is similar to vanilla's pipe.

- :material-tune: [__nchs~__](../objects/nchs~.md) `nchs~` gets the number of channels from a multi-channel connection, as provided by `snake~ in`, `clone` or other objects.

- :material-tune: [__changed__](../objects/changed.md) `changed` passes its data input through only when it changed from the last receive message or the message that was set via arguments or messages.

- :material-tune: [__stream__](../objects/stream.md) `stream` mode makes a list with the last N received items.
.

- :material-tune: [__drum.seq__](../objects/drum.seq.md) `drum.seq` provides a drum grid so you can activate cells to represent attacks.
.

- :material-tune: [__button__](../objects/button.md) `button` is a GUI button that opearets in three modes: latch (default), where it responds to mouse clicks and release, and 'bang' and 'toggle' mode.
.

- :material-tune: [__scope3d~__](../objects/scope3d~.md) `scope3d~` displays signals in 3D.

- :material-tune: [__osc.format__](../objects/osc.format.md) `osc.format` is similar to Vanilla's `oscformat`.

- :material-tune: [__nyquist~__](../objects/nyquist~.md) `nyquist~` reports the nyquist (which is half the sample rate) as a frequency or period.

- :material-tune: [__sampstoms~__](../objects/sampstoms~.md) `sampstoms~` works with floats and signal.

- :material-tune: [__sigs~__](../objects/sigs~.md) `sigs~` is like vanilla's `sig~` but generates multichannel signals from an argument list and creates separate inlets for each argument (minimum size is 2).
.

- :material-tune: [__peak__](../objects/peak.md) `peak` compares the input to a 'peak' (maximum) value.

- :material-tune: [__merge__](../objects/merge.md) `merge` takes any type of messages in any inlet and combines them into a list message.

- :material-tune: [__pulsediv~__](../objects/pulsediv~.md) `pulsediv~` outputs impulses when receiving triggers (signal changes from non-positive to positive).

- :material-tune: [__scale__](../objects/scale.md) `scale` maps an input range to an output range.

- :material-tune: [__ctl.out__](../objects/ctl.out.md) `ctl.out` formats and sends raw MIDI control messages to Pd's MIDI output and its outlet.

- :material-tune: [__polymetro__](../objects/polymetro.md) `polymetro` is a polyrhythmic metronome.

- :material-tune: [__rand.hist__](../objects/rand.hist.md) `rand.hist` generates weighted randomnumbers based on a histogram (which specifies how many times an index is output).

- :material-tune: [__maxpeak~__](../objects/maxpeak~.md) `maxpeak~` returns the maximum peak amplitude so far.

- :material-tune: [__sort__](../objects/sort.md) `sort` sorts messages in ascending or descending order.
.

- :material-tune: [__osc.receive__](../objects/osc.receive.md) `osc.receive` receives OSC messages from network connections and is an abstraction based on `osc.parse` and `netreceive`.

- :material-tune: [__pad__](../objects/pad.md) `pad` is a GUI object that reports mouse coordinates over its area and click status.

- :material-tune: [__function~__](../objects/function~.md) `function~` generates functions from arguments/list input.

- :material-tune: [__delace__](../objects/delace.md) `delace` deinterleaves a list according to the number of outlets.
.

- :material-tune: [__lag~__](../objects/lag~.md) `lag~` is a one pole filter that creates an exponential glide/portamento for its signal input changes.

- :material-tune: [__canvas.mouse__](../objects/canvas.mouse.md) `canvas.mouse` gets mouse click and mouse coordinates when your mouse is interacting with the canvas window.

- :material-tune: [__numbox~__](../objects/numbox~.md) `numbox~` goes into monitor mode when there's a signal connected to it.

- :material-tune: [__togedge__](../objects/togedge.md) `togedge` sends a bang in the left outlet for "zero to non-zero" transitions, and a bang in the right outlet for "non-zero to zero" transitions.
.

- :material-tune: [__out4~__](../objects/out4~.md) `out4~` is a convenient quadraphonic input/output abstraction.

- :material-tune: [__sh~__](../objects/sh~.md) `sh~` samples and holds a value from the left inlet.
.

- :material-tune: [__unmerge__](../objects/unmerge.md) `unmerge` separates the elements of a message in groups of any size (default 1).

- :material-tune: [__datetime__](../objects/datetime.md) `datetime` gives us current/local date (right outlet) and time (left outlet) as lists.
.

- :material-tune: [__drunkard~__](../objects/drunkard~.md) `drunkard~` generates random nvalues within a given step range from the last output.

- :material-tune: [__delete__](../objects/delete.md) `delete` deletes one or more elements from an input message.

- :material-tune: [__play.file~__](../objects/play.file~.md) `play.file~` reads/plays files from your computer similarly to Vanilla's `readsf~`, but it supports more file formats (officialy AAC, AIF, CAF, FLAC, MP3, OGG, OPUS & WAV).

- :material-tune: [__ceil~__](../objects/ceil~.md) `ceil~` is a ceil math function for signals.

- :material-tune: [__format__](../objects/format.md) `format` formats symbols similarly to `makefilename`, but it accepts more than one '%' variable, where each corresponds to an inlet.
.

- :material-tune: [__mouse__](../objects/mouse.md) `mouse` grabs mouse interaction (click and coordinates).
.

- :material-tune: [__any2symbol__](../objects/any2symbol.md) `any2symbol` converts any message to a symbol message.
.

- :material-tune: [__rand.f__](../objects/rand.f.md) `rand.f` generates random float values for a given range when triggered with a bang.

- :material-tune: [__unite__](../objects/unite.md) `unite` unites and converts messages into a symbol message.
.

- :material-tune: [__setdsp~__](../objects/setdsp~.md) `setdsp~` is a convenient abstraction to display and set Pd's audio engine (aka 'DSP') state.

- :material-tune: [__histo__](../objects/histo.md) `histo` records how many times it received a positive integer (no floats allowed).

- :material-tune: [__slide~__](../objects/slide~.md) `slide~` filters an input signal logarithmically between changes in signal value.

- :material-tune: [__glide~__](../objects/glide~.md) `glide~` generates a glide/portamento from its signal input changes.

- :material-tune: [__group__](../objects/group.md) `group` groups messages according to a group size.

- :material-tune: [__ramp~__](../objects/ramp~.md) `ramp~` is a resettable linear ramp between a minimum and maximum value.

- :material-tune: [__pic__](../objects/pic.md) `pic` loads image pictures that you can interact with.

- :material-tune: [__mtx~__](../objects/mtx~.md) `mtx~` routes signals from any inlets to one or more outlets.

- :material-tune: [__hz2rad__](../objects/hz2rad.md) `hz2rad` converts a frequency in Hertz to "Radians per Sample" - which depends on the patch's sample rate (sr).

- :material-tune: [__pol2car~__](../objects/pol2car~.md) `pol2car~` converts polar coordinates (amplitude / phase) to cartesian coordinates (real / imaginary).
.

- :material-tune: [__voices~__](../objects/voices~.md) `voices~` is an abstraction based on `voices` and generates multichannel signals that can be used to control pitch and gate with polyphony.
.

- :material-tune: [__var__](../objects/var.md) `var` is similar to `value` but it can set and recall more than one variable as lists.
.

- :material-tune: [__cycle~__](../objects/cycle~.md) `cycle~` is a linear interpolating oscillator* that reads repeatedly through one cycle of a waveform.

- :material-tune: [__osc.send__](../objects/osc.send.md) `osc.send` sends OSC messages over the network and is an abstraction based on `osc.format` and `netsend`.

- :material-tune: [__gatehold__](../objects/gatehold.md) `gatehold` holds a gate value for a certain amount of time (specified in ms) after the gate has closed.

- :material-tune: [__synth~__](../objects/synth~.md) `synth~` is multichannel aware and can send a multichannel signal out with the '-mc' flag or message.
.

- :material-tune: [__round~__](../objects/round~.md) `round~` approximates positive and negative numbers to an integer multiple of any given number that is greater or equal to 0 (0 makes no approximation - so the original input is output unchanged).
.

- :material-tune: [__deltaclip~__](../objects/deltaclip~.md) `deltaclip~` limits the change between samples in an incoming signal.

- :material-tune: [__spell__](../objects/spell.md) `spell` takes any message and converts each containing digit and character to UTF-8 (Unicode) values (`spell` doesn't understand non-integer float messages).

- :material-tune: [__allpass.filt~__](../objects/allpass.filt~.md) `allpass.filt~` is an allpass filter that you can set its order with the first argument (needs to be a multiple of 2).

- :material-tune: [__ctl.in__](../objects/ctl.in.md) `ctl.in` extracts MIDI CC information from raw MIDI input or a connected MIDI device.
.

- :material-tune: [__rand.u__](../objects/rand.u.md) `rand.u` generates an unrepeated random values (from 0 to size-1).

- :material-tune: [__coll__](../objects/coll.md) `coll` stores/edits any messages at given addresses (an integer or a symbol).

- :material-tune: [__pitch.shift~__](../objects/pitch.shift~.md) `pitch.shift~` is a pitch shifter abstraction based on granulation.

- :material-tune: [__rint__](../objects/rint.md) `rint` takes floats and rounds them to the nearest integer value.
.

- :material-tune: [__record~__](../objects/record~.md) `record~` records up to 64 signal channels into arrays.

- :material-tune: [__pick~__](../objects/pick~.md) `pick~` picks a channel from a multichannel connection.

- :material-tune: [__trunc__](../objects/trunc.md) `trunc` truncates floats and lists towards zero, that means only the integer value is considered, like in vanilla's `int`.
.

- :material-tune: [__train~__](../objects/train~.md) `train~` generates a pulse signal alternating from on (1) to off (0) at a period given in ms.

- :material-tune: [__pulse~__](../objects/pulse~.md) `pulse~` is a pulse train oscillator (alternates between 1 and 0, or on/off) that accepts negative frequencies, has inlets for pulse width, phase sync and phase modulation.

- :material-tune: [__norm~__](../objects/norm~.md) `norm~` is a normalizer abstraction based on `mov.rms~`.

- :material-tune: [__amean__](../objects/amean.md) `amean` creates a list of arithmetic means.

- :material-tune: [__mtr__](../objects/mtr.md) `mtr` records any messages in different tracks and plays them back.

- :material-tune: [__level~__](../objects/level~.md) `level~` is a convenient abstraction for adjusting a signal's gain in dB.

- :material-tune: [__float2imp~__](../objects/float2imp~.md) `float2imp~` converts floats to impulses with sample accuracy.

- :material-tune: [__bicoeff__](../objects/bicoeff.md) `bicoeff` is a GUI that generates coefficients for vanilla's `biquad~` according to different filter types ("eq" filter by default as in the example below).

- :material-tune: [__loadbanger__](../objects/loadbanger.md) `loadbanger` works with both kinds of bangs.

- :material-tune: [__midi2note__](../objects/midi2note.md) `midi2note` converts a MIDI pitch value to note names (such as Eb3).

- :material-tune: [__offer__](../objects/offer.md) `offer` stores a x/y integer number pair and accesses the 'y' value from the corresponding 'x' (after retrieving, the pair is deleted).
.

- :material-tune: [__combine__](../objects/combine.md) `combine` collects messages (with one or more elements) into a single list if they come within a certain given amount of time, but not if greater than it.

- :material-tune: [__sig2float~__](../objects/sig2float~.md) `sig2float~` converts signals to floats.

- :material-tune: [__trough__](../objects/trough.md) `trough` compares the input to a 'trough' (minimum) value.

- :material-tune: [__note.in__](../objects/note.in.md) `note.in` extracts MIDI Pitch information from external "raw" MIDI data or an internally connected device.

- :material-tune: [__select~__](../objects/select~.md) `select~` selects an input signal without crossfade and the signals can be of different channel sizes.

- :material-tune: [__repeat~__](../objects/repeat~.md) `repeat~` takes an input signal os any channel size and repeats it 'n' times.
.

- :material-tune: [__gain~__](../objects/gain~.md) `gain~` is a convenient mono gain abstraction for adjusting a signal's gain.

- :material-tune: [__power~__](../objects/power~.md) `power~` is a power function waveshaper for signals that extends the usual definition of exponentiation and returns -pow(-a, b) when you have a negative signal input.

- :material-tune: [__suspedal__](../objects/suspedal.md) `suspedal` holds MIDI Note Off messages when on and sends them out when it's switched off.

- :material-tune: [__substitute__](../objects/substitute.md) `substitute` will replace all recurring elements in a message, but if you have a 3rd argument, it operates in "first only" mode, where only the first element is replaced.
.

- :material-tune: [__knob__](../objects/knob.md) `knob` has an exponential and log feature just like the `rescale` object.

- :material-tune: [__dec2hex__](../objects/dec2hex.md) `dec2hex` converts decimal values to hexadecimal ones.

- :material-tune: [__lace__](../objects/lace.md) `lace` interleaves two or more lists.

- :material-tune: [__mpe.in__](../objects/mpe.in.md) `mpe.in` sends "cooked" MPE data from external "raw" MIDI data or an internally connected device.

- :material-tune: [__sfz~__](../objects/sfz~.md) `sfz~` also has microtonal capabilities.

- :material-tune: [__display__](../objects/display.md) `display` can display a message just like `print`.

- :material-tune: [__fold__](../objects/fold.md) `fold` folds between a low and high value.

- :material-tune: [__tabgen__](../objects/tabgen.md) `tabgen` is an abstraction that generates different functions for a given table name.
.

- :material-tune: [__sequencer__](../objects/sequencer.md) `sequencer` sends an element from a given sequence when banged.

- :material-tune: [__quantizer__](../objects/quantizer.md) `quantizer` approximates a value to step values defined by the argument.

- :material-tune: [__pick__](../objects/pick.md) `pick` picks an element from an input message according to an element number.

- :material-tune: [__svf~__](../objects/svf~.md) `svf~` implements Chamberlin's state-variable filter algorithm, which outputs lowpass, highpass, bandpass, and band reject (notch) simultaneously in parallel (in this order from left to right).
.

- :material-tune: [__hex2dec__](../objects/hex2dec.md) `hex2dec` converts hexadecimal values to decimal ones.

- :material-tune: [__saw2~__](../objects/saw2~.md) `saw2~` is a sawtooth wave oscillator that accepts negative frequencies, has inlets for phase sync and phase modulation.

- :material-tune: [__player~__](../objects/player~.md) `player~` is a convenient abstraction based on `sfload` (so it supports the same file formats, check it's help file) and `tabplayer~`.

- :material-tune: [__meter2~__](../objects/meter2~.md) `meter2~` is a convenient stereo VU-meter abstraction.

- :material-tune: [__pvoc.live~__](../objects/pvoc.live~.md) `pvoc.live~` is like `pvoc.player~`, but for live input.

- :material-tune: [__gmean__](../objects/gmean.md) `gmean` creates a list of geometric means.

- :material-tune: [__sum__](../objects/sum.md) `sum` sums a list of values.
.

- :material-tune: [__mono__](../objects/mono.md) `mono` takes note messages and handles them to emulate monophonic synth behaviour.

- :material-tune: [__voices__](../objects/voices.md) `voices` outputs a list with voice index, pitch, velocity and optional extra stuff.

- :material-tune: [__touch.out__](../objects/touch.out.md) `touch.out` formats and sends raw MIDI aftertouch messages to Pd's MIDI output and its outlet.

- :material-tune: [__samps2ms~__](../objects/samps2ms~.md) `samps2ms~` is a simple abstraction that converts time values number of samples to ms.

- :material-tune: [__midi.learn__](../objects/midi.learn.md) `midi.learn` is an abstraction based on `savestate` that learns and saves any MIDI input data.

- :material-tune: [__ptouch.in__](../objects/ptouch.in.md) `ptouch.in` extracts MIDI polyphonic aftertouch information from raw MIDI input (such as from `midiin`).
.

- :material-tune: [__bitsafe~__](../objects/bitsafe~.md) `bitsafe~` replaces NaN (not a number) and +/- infinity values of an incoming signal with zero, which is useful in conjunction with the bitwise operators in cyclone or any other situation where these values are possible.

- :material-tune: [__colors__](../objects/colors.md) `colors` can output color values specially for Pd Vanilla's GUI objects (aka iemgus) and Data Structures.

- :material-tune: [__pattern__](../objects/pattern.md) `pattern` is a rhythmic pattern sequencer.

- :material-tune: [__keymap__](../objects/keymap.md) `keymap` maps your computer keyboard to MIDI pitches and generates note on/off messages when keys get pressed and released.

- :material-tune: [__bitnormal~__](../objects/bitnormal~.md) `bitnormal~` replaces NaN (not a number), +/- infinity values and denormals of an incoming signal with zero (hence, it only lets 'normal' floats through.

- :material-tune: [__minimum__](../objects/minimum.md) `minimum` outputs the minimum of two or more values.

- :material-tune: [__router__](../objects/router.md) `router` routes a message from the left inlet to an outlet number specified by the float into the right inlet (if the number is out of range, the message is not output).
.

- :material-tune: [__lin2db~__](../objects/lin2db~.md) `lin2db~` converts amplitude values from linear to a deciBel Full Scale (dBFS) with support for multichannel signals.

- :material-tune: [__osc.parse__](../objects/osc.parse.md) `osc.parse` is similar to Vanilla's `oscparse` but the output is not a list and more closely related on how OSC messages are generally dealt with.

- :material-tune: [__prepend__](../objects/prepend.md) `prepend` will add messages set as argument to the beginning of any message sent to the input.

- :material-tune: [__notedur2ratio__](../objects/notedur2ratio.md) `notedur2ratio` converts from a note duration symbolic syntax to a ratio (either as fraction or float).

- :material-tune: [__db2lin__](../objects/db2lin.md) `db2lin` converts amplitude values from deciBel Full Scale (dBFS) to linear.

- :material-tune: [__autofade~__](../objects/autofade~.md) `autofade~` is an automatic fade in/out for multi inputs.

- :material-tune: [__note2midi__](../objects/note2midi.md) `note2midi` converts note names (such as 'C4') to MIDI pitch values.

- :material-tune: [__table__](../objects/table.md) `table` stores and edits a number array.

- :material-tune: [__greaterthan~__](../objects/greaterthan~.md) `greaterthan~` or `>~` outputs a 1 signal when the left input is greater-than the right input or argument and a 0 when it is less-than or equal-to the right input or argument.
.

- :material-tune: [__rand.i__](../objects/rand.i.md) `rand.i` generates random integer values for a given range when triggered with as bang.Use the seed message if you want a reproducible output.

- :material-tune: [__bend.out__](../objects/bend.out.md) `bend.out` formats and sends raw MIDI pitch bend messages to Pd's MIDI output and its outlet.

- :material-tune: [__op~__](../objects/op~.md) `op~` is a signal operator where the first argument defines the the type (for either comparison, bitwise, logic and modulus operations).

- :material-tune: [__get~__](../objects/get~.md) `get~` gets one or more channels from a multichannel connection.

- :material-tune: [__score2__](../objects/score2.md) `score2` has a 'tempo' syntax where 'tempo 60' sets the bpm to 60! The 'tempo' messages are output in the third 'data' outlet.

- :material-tune: [__autotune__](../objects/autotune.md) `autotune` receives a scale as a list of steps in cents and a base MIDI pitch value (default 60).

- :material-tune: [__note__](../objects/note.md) `note` is a GUI meant only to display text notes.

- :material-tune: [__bitshift~__](../objects/bitshift~.md) `bitshift~` can produce NaNs and +/-INFs - but denormals are zeroed out.

</div>