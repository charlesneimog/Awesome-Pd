<div class="grid cards" markdown>
- :material-tune: [__tabplayer~__](../objects/tabplayer~.md) `tabplayer~` plays arrays with multichannel support.

- :material-tune: [__store__](../objects/store.md) `store` is an abstraction based on `text` that stores incoming messages sequentially.
.

- :material-tune: [__scales__](../objects/scales.md) `scales` generates scales as note names (default) or MIDI pitches.

- :material-tune: [__op__](../objects/op.md) `op` provides many operators and is most useful for lists, as there are objects in Pd Vanilla for most of these operations.
.

- :material-tune: [__equal__](../objects/equal.md) `equal` compares lists and outputs 1 if they're the same or 0 if they're not.

- :material-tune: [__midi.in__](../objects/midi.in.md) `midi.in` sends "cooked" MIDI data instead of "raw" data like `midiin` with MIDI data type symbol, values and channel (but a note output is sent as a simple numeric list).

- :material-tune: [__mtx.ctl__](../objects/mtx.ctl.md) `mtx.ctl` provides a user matrix interface control.

- :material-tune: [__wave~__](../objects/wave~.md) `wave~`'s input phase varies between 0 and 1, which in 32-bit floating point arithmetic has 24 bits of index resolution.

- :material-tune: [__pack2__](../objects/pack2.md) `pack2` is kinda similar to Pd Vanilla's `pack`, but any inlet triggers the output (though a "set" message avoids the output).

- :material-tune: [__slice__](../objects/slice.md) `slice` splits lists.

- :material-tune: [__tabwriter~__](../objects/tabwriter~.md) `tabwriter~` records up to 64 signal channels into arrays.

- :material-tune: [__stream__](../objects/stream.md) `stream` mode makes a list with the last N received items.
.

- :material-tune: [__osc.format__](../objects/osc.format.md) `osc.format` is similar to Vanilla's `oscformat`.

- :material-tune: [__merge__](../objects/merge.md) `merge` takes any type of messages in any inlet and combines them into a list message.

- :material-tune: [__del~__](../objects/del~.md) `del~` sets and writes to a delay line if created as `del~ in` (default) and reads from it (with interpolation) if created as `del~ out`.

- :material-tune: [__delace__](../objects/delace.md) `delace` deinterleaves a list according to the number of outlets.
.

- :material-tune: [__metronome__](../objects/metronome.md) `metronome` understands complex time signatures and outputs timeline data (bar, sub-bar, beat and sub-beat count) and phase output.

- :material-tune: [__scale2freq__](../objects/scale2freq.md) `scale2freq` gets a scale as a list of cents values, a base/fundamental pitch and outputs a list of frequency in hertz between a minimum and maximum value.

- :material-tune: [__datetime__](../objects/datetime.md) `datetime` gives us current/local date (right outlet) and time (left outlet) as lists.
.

- :material-tune: [__buffer~__](../objects/buffer~.md) `buffer~` stores audio in a memory buffer (an array).

- :material-tune: [__unite__](../objects/unite.md) `unite` unites and converts messages into a symbol message.
.

- :material-tune: [__histo__](../objects/histo.md) `histo` records how many times it received a positive integer (no floats allowed).

- :material-tune: [__var__](../objects/var.md) `var` is similar to `value` but it can set and recall more than one variable as lists.
.

- :material-tune: [__cycle~__](../objects/cycle~.md) `cycle~` is a linear interpolating oscillator* that reads repeatedly through one cycle of a waveform.

- :material-tune: [__anal__](../objects/anal.md) `anal` reports how many times it received a number pair.

- :material-tune: [__spell__](../objects/spell.md) `spell` takes any message and converts each containing digit and character to UTF-8 (Unicode) values (`spell` doesn't understand non-integer float messages).

- :material-tune: [__coll__](../objects/coll.md) `coll` stores/edits any messages at given addresses (an integer or a symbol).

- :material-tune: [__record~__](../objects/record~.md) `record~` records up to 64 signal channels into arrays.

- :material-tune: [__tabreader__](../objects/tabreader.md) `tabreader` accepts indexes from 0 to 1 by default and reads an array with different interpolation methods with multi channel support.

- :material-tune: [__offer__](../objects/offer.md) `offer` stores a x/y integer number pair and accesses the 'y' value from the corresponding 'x' (after retrieving, the pair is deleted).
.

- :material-tune: [__combine__](../objects/combine.md) `combine` collects messages (with one or more elements) into a single list if they come within a certain given amount of time, but not if greater than it.

- :material-tune: [__histogram__](../objects/histogram.md) `histogram` records into a table how many times it received a positive integer number (treated as indexes, floats are truncated).

- :material-tune: [__lace__](../objects/lace.md) `lace` interleaves two or more lists.

- :material-tune: [__tabgen__](../objects/tabgen.md) `tabgen` is an abstraction that generates different functions for a given table name.
.

- :material-tune: [__pick__](../objects/pick.md) `pick` picks an element from an input message according to an element number.

- :material-tune: [__mono__](../objects/mono.md) `mono` takes note messages and handles them to emulate monophonic synth behaviour.

- :material-tune: [__a.rotate__](../objects/a.rotate.md) The `a.rotate` object in Pure Data appends a number to the end of an array, making it useful for tracking or visualizing the history of sound parameters over time..

- :material-tune: [__voices__](../objects/voices.md) `voices` outputs a list with voice index, pitch, velocity and optional extra stuff.

- :material-tune: [__remove__](../objects/remove.md) `remove` removes one or more number elements from a list.

- :material-tune: [__colors__](../objects/colors.md) `colors` can output color values specially for Pd Vanilla's GUI objects (aka iemgus) and Data Structures.

- :material-tune: [__prepend__](../objects/prepend.md) `prepend` will add messages set as argument to the beginning of any message sent to the input.

- :material-tune: [__table__](../objects/table.md) `table` stores and edits a number array.

</div>