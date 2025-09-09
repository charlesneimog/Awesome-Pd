<div class="grid cards" markdown>
- :material-tune: [__quantizer~__](../objects/quantizer~.md) `quantizer~` approximates a value to step values defined by the argument.

- :material-tune: [__grab__](../objects/grab.md) `grab` sets the value of GUIs but also grabs its ouotput.

- :material-tune: [__canvas.setname__](../objects/canvas.setname.md) `canvas.setname` sets a symbol name to a canvas so you can send it messages.

- :material-tune: [__circle__](../objects/circle.md) `circle` is a two dimensional slider GUI abstraction with a circular area (see also [else/slider2d).
.

- :material-tune: [__equal__](../objects/equal.md) `equal` compares lists and outputs 1 if they're the same or 0 if they're not.

- :material-tune: [__autotune2__](../objects/autotune2.md) `autotune2` receives a scale as a list of steps in cents and then retunes incoming cents values to the closest step in the scale.
.

- :material-tune: [__loop__](../objects/loop.md) `loop` is a loop counter, but it can also loop bangs like `until` (using the -b flag).

- :material-tune: [__mtx.ctl__](../objects/mtx.ctl.md) `mtx.ctl` provides a user matrix interface control.

- :material-tune: [__pack2__](../objects/pack2.md) `pack2` is kinda similar to Pd Vanilla's `pack`, but any inlet triggers the output (though a "set" message avoids the output).

- :material-tune: [__above~__](../objects/above~.md) The `above~` object in Pure Data monitors a signal input and outputs impulses based on a threshold.

- :material-tune: [__urn__](../objects/urn.md) `urn` generates random numbers in a range defined by the 'n' size (from 0 to n-1) without repeating them.

- :material-tune: [__maximum__](../objects/maximum.md) `maximum` outputs the maximum of two or more values.

- :material-tune: [__round__](../objects/round.md) `round` approximates positive and negative numbers to an integer multiple of any given number that is greater or equal to 0 (0 makes no approximation, so the original input is output unchanged).
.

- :material-tune: [__changed__](../objects/changed.md) `changed` passes its data input through only when it changed from the last receive message or the message that was set via arguments or messages.

- :material-tune: [__stream__](../objects/stream.md) `stream` mode makes a list with the last N received items.
.

- :material-tune: [__button__](../objects/button.md) `button` is a GUI button that opearets in three modes: latch (default), where it responds to mouse clicks and release, and 'bang' and 'toggle' mode.
.

- :material-tune: [__sampstoms~__](../objects/sampstoms~.md) `sampstoms~` works with floats and signal.

- :material-tune: [__peak__](../objects/peak.md) `peak` compares the input to a 'peak' (maximum) value.

- :material-tune: [__sort__](../objects/sort.md) `sort` sorts messages in ascending or descending order.
.

- :material-tune: [__pad__](../objects/pad.md) `pad` is a GUI object that reports mouse coordinates over its area and click status.

- :material-tune: [__canvas.mouse__](../objects/canvas.mouse.md) `canvas.mouse` gets mouse click and mouse coordinates when your mouse is interacting with the canvas window.

- :material-tune: [__pimpmul~__](../objects/pimpmul~.md) `pimpmul~` is a "pimp~" multiplier.

- :material-tune: [__metronome__](../objects/metronome.md) `metronome` understands complex time signatures and outputs timeline data (bar, sub-bar, beat and sub-beat count) and phase output.

- :material-tune: [__above__](../objects/above.md) The `above` object in Pure Data monitors a float input and triggers events based on a threshold.

- :material-tune: [__togedge__](../objects/togedge.md) `togedge` sends a bang in the left outlet for "zero to non-zero" transitions, and a bang in the right outlet for "non-zero to zero" transitions.
.

- :material-tune: [__sh~__](../objects/sh~.md) `sh~` samples and holds a value from the left inlet.
.

- :material-tune: [__drunkard~__](../objects/drunkard~.md) `drunkard~` generates random nvalues within a given step range from the last output.

- :material-tune: [__delete__](../objects/delete.md) `delete` deletes one or more elements from an input message.

- :material-tune: [__mouse__](../objects/mouse.md) `mouse` grabs mouse interaction (click and coordinates).
.

- :material-tune: [__any2symbol__](../objects/any2symbol.md) `any2symbol` converts any message to a symbol message.
.

- :material-tune: [__phaseseq~__](../objects/phaseseq~.md) `phaseseq~` takes a list of thresholds and outputs impulses when reaching the threshold values.
.

- :material-tune: [__gaterelease__](../objects/gaterelease.md) `gaterelease` allows you to release one gate in your patch while you still hold another.

- :material-tune: [__setdsp~__](../objects/setdsp~.md) `setdsp~` is a convenient abstraction to display and set Pd's audio engine (aka 'DSP') state.

- :material-tune: [__group__](../objects/group.md) `group` groups messages according to a group size.

- :material-tune: [__ramp~__](../objects/ramp~.md) `ramp~` is a resettable linear ramp between a minimum and maximum value.

- :material-tune: [__pic__](../objects/pic.md) `pic` loads image pictures that you can interact with.

- :material-tune: [__pol2car~__](../objects/pol2car~.md) `pol2car~` converts polar coordinates (amplitude / phase) to cartesian coordinates (real / imaginary).
.

- :material-tune: [__var__](../objects/var.md) `var` is similar to `value` but it can set and recall more than one variable as lists.
.

- :material-tune: [__bitand~__](../objects/bitand~.md) `bitand~` compares the bits of two values with "Bitwise-AND" (bits are set to 1 if both are "1", 0 otherwise).

- :material-tune: [__osc.send__](../objects/osc.send.md) `osc.send` sends OSC messages over the network and is an abstraction based on `osc.format` and `netsend`.

- :material-tune: [__gatehold__](../objects/gatehold.md) `gatehold` holds a gate value for a certain amount of time (specified in ms) after the gate has closed.

- :material-tune: [__ctl.in__](../objects/ctl.in.md) `ctl.in` extracts MIDI CC information from raw MIDI input or a connected MIDI device.
.

- :material-tune: [__coll__](../objects/coll.md) `coll` stores/edits any messages at given addresses (an integer or a symbol).

- :material-tune: [__rint__](../objects/rint.md) `rint` takes floats and rounds them to the nearest integer value.
.

- :material-tune: [__osc.route__](../objects/osc.route.md) `osc.route` routes OSC messages received from `osc.receive`.

- :material-tune: [__pick~__](../objects/pick~.md) `pick~` picks a channel from a multichannel connection.

- :material-tune: [__trunc__](../objects/trunc.md) `trunc` truncates floats and lists towards zero, that means only the integer value is considered, like in vanilla's `int`.
.

- :material-tune: [__loadbanger__](../objects/loadbanger.md) `loadbanger` works with both kinds of bangs.

- :material-tune: [__offer__](../objects/offer.md) `offer` stores a x/y integer number pair and accesses the 'y' value from the corresponding 'x' (after retrieving, the pair is deleted).
.

- :material-tune: [__combine__](../objects/combine.md) `combine` collects messages (with one or more elements) into a single list if they come within a certain given amount of time, but not if greater than it.

- :material-tune: [__trough__](../objects/trough.md) `trough` compares the input to a 'trough' (minimum) value.

- :material-tune: [__note.in__](../objects/note.in.md) `note.in` extracts MIDI Pitch information from external "raw" MIDI data or an internally connected device.

- :material-tune: [__suspedal__](../objects/suspedal.md) `suspedal` holds MIDI Note Off messages when on and sends them out when it's switched off.

- :material-tune: [__substitute__](../objects/substitute.md) `substitute` will replace all recurring elements in a message, but if you have a 3rd argument, it operates in "first only" mode, where only the first element is replaced.
.

- :material-tune: [__lace__](../objects/lace.md) `lace` interleaves two or more lists.

- :material-tune: [__display__](../objects/display.md) `display` can display a message just like `print`.

- :material-tune: [__pick__](../objects/pick.md) `pick` picks an element from an input message according to an element number.

- :material-tune: [__hex2dec__](../objects/hex2dec.md) `hex2dec` converts hexadecimal values to decimal ones.

- :material-tune: [__bitsafe~__](../objects/bitsafe~.md) `bitsafe~` replaces NaN (not a number) and +/- infinity values of an incoming signal with zero, which is useful in conjunction with the bitwise operators in cyclone or any other situation where these values are possible.

- :material-tune: [__colors__](../objects/colors.md) `colors` can output color values specially for Pd Vanilla's GUI objects (aka iemgus) and Data Structures.

- :material-tune: [__pattern__](../objects/pattern.md) `pattern` is a rhythmic pattern sequencer.

- :material-tune: [__keymap__](../objects/keymap.md) `keymap` maps your computer keyboard to MIDI pitches and generates note on/off messages when keys get pressed and released.

- :material-tune: [__bitnormal~__](../objects/bitnormal~.md) `bitnormal~` replaces NaN (not a number), +/- infinity values and denormals of an incoming signal with zero (hence, it only lets 'normal' floats through.

- :material-tune: [__minimum__](../objects/minimum.md) `minimum` outputs the minimum of two or more values.

- :material-tune: [__router__](../objects/router.md) `router` routes a message from the left inlet to an outlet number specified by the float into the right inlet (if the number is out of range, the message is not output).
.

- :material-tune: [__keycode__](../objects/keycode.md) `keycode` outputs key codes from your keyboard based on their physical location, so it is layout independent (but please don't change layout after loading Pd and the object, this is problematic specially on Windows..

- :material-tune: [__notedur2ratio__](../objects/notedur2ratio.md) `notedur2ratio` converts from a note duration symbolic syntax to a ratio (either as fraction or float).

- :material-tune: [__autofade~__](../objects/autofade~.md) `autofade~` is an automatic fade in/out for multi inputs.

- :material-tune: [__greaterthan~__](../objects/greaterthan~.md) `greaterthan~` or `>~` outputs a 1 signal when the left input is greater-than the right input or argument and a 0 when it is less-than or equal-to the right input or argument.
.

- :material-tune: [__rand.i__](../objects/rand.i.md) `rand.i` generates random integer values for a given range when triggered with as bang.Use the seed message if you want a reproducible output.

- :material-tune: [__op~__](../objects/op~.md) `op~` is a signal operator where the first argument defines the the type (for either comparison, bitwise, logic and modulus operations).

- :material-tune: [__sender__](../objects/sender.md) `sender` is much like vanilla's `send`, but can have up to two names and at load time can expand dollar symbols according to parent patches.
.

- :material-tune: [__autotune__](../objects/autotune.md) `autotune` receives a scale as a list of steps in cents and a base MIDI pitch value (default 60).

- :material-tune: [__note__](../objects/note.md) `note` is a GUI meant only to display text notes.

</div>