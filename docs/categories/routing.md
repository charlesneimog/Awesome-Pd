<div class="grid cards" markdown>
- :material-tune: [__out~__](../objects/out~.md) `out~` has a built in `sum~` object, so it can take multichannel signals and sum them together for each input.
.

- :material-tune: [__unmerge~__](../objects/unmerge~.md) `unmerge~` separates the channels of a multichannel signal in groups of any size (default 1).

- :material-tune: [__out8~__](../objects/out8~.md) `out8~` is a convenient octaphonic input/output abstraction.

- :material-tune: [__xgate2~__](../objects/xgate2~.md) `xgate2~` routes an input signal to 'n' specified outlets with crossfading between adjacent channels according to a spread parameter.
.

- :material-tune: [__pdlink~__](../objects/pdlink~.md) `pdlink~` allows you to send/receive audio streans to/from different Pd instances, as different versions, platforms and even forks of Pure Data (such as PlugData).

- :material-tune: [__delace~__](../objects/delace~.md) `delace~` deinterleaves a multichannel signal according to the number of outlets.
.

- :material-tune: [__tabwriter~__](../objects/tabwriter~.md) `tabwriter~` records up to 64 signal channels into arrays.

- :material-tune: [__rotate~__](../objects/rotate~.md) `rotate~` performs equal power rotation for 'n' channels (default 2).

- :material-tune: [__matrix~__](../objects/matrix~.md) `matrix~` routes signals from any inlets to one or more outlets.

- :material-tune: [__spread.mc~__](../objects/spread.mc~.md) `spread.mc~` spreads any number of input channels across any number of output channels with equal power panning according to a spread parameter.

- :material-tune: [__score__](../objects/score.md) `score` has a 'tempo' syntax where 'tempo 60' internally sets the bpm to 60! The 'tempo' messages are output in the mid 'data' outlet.
.

- :material-tune: [__del~__](../objects/del~.md) `del~` sets and writes to a delay line if created as `del~ in` (default) and reads from it (with interpolation) if created as `del~ out`.

- :material-tune: [__numbox~__](../objects/numbox~.md) `numbox~` goes into monitor mode when there's a signal connected to it.

- :material-tune: [__unmerge__](../objects/unmerge.md) `unmerge` separates the elements of a message in groups of any size (default 1).

- :material-tune: [__xgate2.mc~__](../objects/xgate2.mc~.md) `xgate2.mc~` routes an input signal to 'n' specified channels in a multichannel output with crossfading between adjacent channels according to a spread parameter.
.

- :material-tune: [__mtx~__](../objects/mtx~.md) `mtx~` routes signals from any inlets to one or more outlets.

- :material-tune: [__xselect2.mc~__](../objects/xselect2.mc~.md) `xselect2.mc~` selects from 'n' inputs with crossfading between adjacent channels according to a spread parameter.
.

- :material-tune: [__ptouch.out__](../objects/ptouch.out.md) `ptouch.out` formats and sends raw MIDI polyphonic aftertouch messages to Pd's MIDI output and its outlet..

- :material-tune: [__receiver__](../objects/receiver.md) `receiver` is kinda like vanilla's `receive`.

- :material-tune: [__osc.route__](../objects/osc.route.md) `osc.route` routes OSC messages received from `osc.receive`.

- :material-tune: [__select~__](../objects/select~.md) `select~` selects an input signal without crossfade and the signals can be of different channel sizes.

- :material-tune: [__mtx.mc~__](../objects/mtx.mc~.md) `mtx.mc~` routes a channel signal from a multichannel input to one or more channels of a multichannel output.
.

- :material-tune: [__changed~__](../objects/changed~.md) The `changed~` object in Pure Data monitors an input signal and outputs an impulse whenever the signal changes by an amount equal to or greater than a specified threshold.

- :material-tune: [__mix2~__](../objects/mix2~.md) `mix2~` has support for multichannel input.
.

- :material-tune: [__send2~__](../objects/send2~.md) `send2~` is like send but automatically resizes according to the number of input channels.
.

- :material-tune: [__rotate.mc~__](../objects/rotate.mc~.md) `rotate.mc~` performs equal power rotation for any number of channels given by a multichannel signal input.

- :material-tune: [__speed__](../objects/speed.md) `speed` is somewhat related to `line`.

- :material-tune: [__noisegate~__](../objects/noisegate~.md) `noisegate~` is a noise gate abstraction.

- :material-tune: [__touch.out__](../objects/touch.out.md) `touch.out` formats and sends raw MIDI aftertouch messages to Pd's MIDI output and its outlet.

- :material-tune: [__xselect.mc~__](../objects/xselect.mc~.md) `xselect.mc~` selects between multiple channels from a multichannel connection (maximum 512 channels) with equal power crossfading.
.

- :material-tune: [__xselect2~__](../objects/xselect2~.md) `xselect2~` selects from 'n' inputs with crossfading between adjacent channels according to a spread parameter.
.

- :material-tune: [__mix4~__](../objects/mix4~.md) `mix4~` has support for multichannel input.
.

- :material-tune: [__router__](../objects/router.md) `router` routes a message from the left inlet to an outlet number specified by the float into the right inlet (if the number is out of range, the message is not output).
.

- :material-tune: [__keycode__](../objects/keycode.md) `keycode` outputs key codes from your keyboard based on their physical location, so it is layout independent (but please don't change layout after loading Pd and the object, this is problematic specially on Windows..

- :material-tune: [__out.mc~__](../objects/out.mc~.md) `out.mc~` takes multichannel signals and outputs them from given `dac~` channel output (default 1).

- :material-tune: [__slice~__](../objects/slice~.md) `slice~` splits a multichannel signal.

- :material-tune: [__sender__](../objects/sender.md) `sender` is much like vanilla's `send`, but can have up to two names and at load time can expand dollar symbols according to parent patches.
.

</div>