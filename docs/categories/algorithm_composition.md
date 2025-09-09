<div class="grid cards" markdown>
- :material-tune: [__out~__](../objects/out~.md) `out~` has a built in `sum~` object, so it can take multichannel signals and sum them together for each input.
.

- :material-tune: [__xmod2~__](../objects/xmod2~.md) `xmod2~` performs is a variant of `xmod~`, but only performs frequency modulation (so far) and uses a different and cheap sine waveform that promotes more chaotic and cool sounds.
.

- :material-tune: [__biquads~__](../objects/biquads~.md) `biquads~` is a series of biquad filters in cascade.
.

- :material-tune: [__white~__](../objects/white~.md) `white~` is a white noise generator from a pseudo random number generator algorithm.

- :material-tune: [__spectrograph~__](../objects/spectrograph~.md) `spectrograph~` is an abstraction for visualizing FFT amplitudes from 0hz to Nyquist.

- :material-tune: [__store__](../objects/store.md) `store` is an abstraction based on `text` that stores incoming messages sequentially.
.

- :material-tune: [__bl.imp2~__](../objects/bl.imp2~.md) `bl.imp2~` is a two sided impulse oscillator like `else/imp2~`, but it is bandlimited.
.

- :material-tune: [__touch.in__](../objects/touch.in.md) `touch.in` extracts MIDI Aftertouch information from raw MIDI input or a connected MIDI device.
.

- :material-tune: [__op__](../objects/op.md) `op` provides many operators and is most useful for lists, as there are objects in Pd Vanilla for most of these operations.
.

- :material-tune: [__loop__](../objects/loop.md) `loop` is a loop counter, but it can also loop bangs like `until` (using the -b flag).

- :material-tune: [__wave~__](../objects/wave~.md) `wave~`'s input phase varies between 0 and 1, which in 32-bit floating point arithmetic has 24 bits of index resolution.

- :material-tune: [__gray~__](../objects/gray~.md) `gray~` generates noise based on "gray code" or reflected binary code (RBC), which results from flipping random bits (sot is is based on a pseudo random number generator algorithm.).

- :material-tune: [__vocoder~__](../objects/vocoder~.md) `vocoder~` is classic cross synthesis channel vocoder abstraction.
.

- :material-tune: [__slice__](../objects/slice.md) `slice` splits lists.

- :material-tune: [__note.out__](../objects/note.out.md) `note.out` formats and sends raw MIDI pitch messages to Pd's MIDI output and its outlet.

- :material-tune: [__changed__](../objects/changed.md) `changed` passes its data input through only when it changed from the last receive message or the message that was set via arguments or messages.

- :material-tune: [__button__](../objects/button.md) `button` is a GUI button that opearets in three modes: latch (default), where it responds to mouse clicks and release, and 'bang' and 'toggle' mode.
.

- :material-tune: [__sampstoms~__](../objects/sampstoms~.md) `sampstoms~` works with floats and signal.

- :material-tune: [__peak__](../objects/peak.md) `peak` compares the input to a 'peak' (maximum) value.

- :material-tune: [__merge__](../objects/merge.md) `merge` takes any type of messages in any inlet and combines them into a list message.

- :material-tune: [__scale__](../objects/scale.md) `scale` maps an input range to an output range.

- :material-tune: [__phaseshift~__](../objects/phaseshift~.md) `phaseshift~` is a 2nd allpass filter, which keeps the gain and only alters the phase from 0 (at 0 hz) to 360º (at the Nyquist frequency).

- :material-tune: [__sort__](../objects/sort.md) `sort` sorts messages in ascending or descending order.
.

- :material-tune: [__osc.receive__](../objects/osc.receive.md) `osc.receive` receives OSC messages from network connections and is an abstraction based on `osc.parse` and `netreceive`.

- :material-tune: [__pad__](../objects/pad.md) `pad` is a GUI object that reports mouse coordinates over its area and click status.

- :material-tune: [__xfade~__](../objects/xfade~.md) `xfade~` crossfades between two sources (that can have 1 to 64 channels each).

- :material-tune: [__delace__](../objects/delace.md) `delace` deinterleaves a list according to the number of outlets.
.

- :material-tune: [__lag~__](../objects/lag~.md) `lag~` is a one pole filter that creates an exponential glide/portamento for its signal input changes.

- :material-tune: [__togedge__](../objects/togedge.md) `togedge` sends a bang in the left outlet for "zero to non-zero" transitions, and a bang in the right outlet for "non-zero to zero" transitions.
.

- :material-tune: [__scale2freq__](../objects/scale2freq.md) `scale2freq` gets a scale as a list of cents values, a base/fundamental pitch and outputs a list of frequency in hertz between a minimum and maximum value.

- :material-tune: [__brown~__](../objects/brown~.md) `brown~` is a brown noise generator (aka brownian noise or red noise), whose spectral energy drops 6dB per octave (sounding less hissy than white noise).

- :material-tune: [__unmerge__](../objects/unmerge.md) `unmerge` separates the elements of a message in groups of any size (default 1).

- :material-tune: [__mouse__](../objects/mouse.md) `mouse` grabs mouse interaction (click and coordinates).
.

- :material-tune: [__any2symbol__](../objects/any2symbol.md) `any2symbol` converts any message to a symbol message.
.

- :material-tune: [__function__](../objects/function.md) `function` is a breakpoints function GUI, mainly used with `function~` or `envgen~`.

- :material-tune: [__unite__](../objects/unite.md) `unite` unites and converts messages into a symbol message.
.

- :material-tune: [__envelope~__](../objects/envelope~.md) `envelope~` provides 6 different envelopes, which are generated via a phase input.
.

- :material-tune: [__brown__](../objects/brown.md) `brown` is a control brownian motion generator.

- :material-tune: [__gaussian~__](../objects/gaussian~.md) `gaussian~` is a gaussian oscillator.

- :material-tune: [__group__](../objects/group.md) `group` groups messages according to a group size.

- :material-tune: [__receiver__](../objects/receiver.md) `receiver` is kinda like vanilla's `receive`.

- :material-tune: [__round~__](../objects/round~.md) `round~` approximates positive and negative numbers to an integer multiple of any given number that is greater or equal to 0 (0 makes no approximation - so the original input is output unchanged).
.

- :material-tune: [__spell__](../objects/spell.md) `spell` takes any message and converts each containing digit and character to UTF-8 (Unicode) values (`spell` doesn't understand non-integer float messages).

- :material-tune: [__allpass.filt~__](../objects/allpass.filt~.md) `allpass.filt~` is an allpass filter that you can set its order with the first argument (needs to be a multiple of 2).

- :material-tune: [__rand.u__](../objects/rand.u.md) `rand.u` generates an unrepeated random values (from 0 to size-1).

- :material-tune: [__pitch.shift~__](../objects/pitch.shift~.md) `pitch.shift~` is a pitch shifter abstraction based on granulation.

- :material-tune: [__norm~__](../objects/norm~.md) `norm~` is a normalizer abstraction based on `mov.rms~`.

- :material-tune: [__amean__](../objects/amean.md) `amean` creates a list of arithmetic means.

- :material-tune: [__float2imp~__](../objects/float2imp~.md) `float2imp~` converts floats to impulses with sample accuracy.

- :material-tune: [__bicoeff__](../objects/bicoeff.md) `bicoeff` is a GUI that generates coefficients for vanilla's `biquad~` according to different filter types ("eq" filter by default as in the example below).

- :material-tune: [__gatehold~__](../objects/gatehold~.md) `gatehold~` holds a gate value for a certain amount of time (specified in ms) after the gate has closed.

- :material-tune: [__sig2float~__](../objects/sig2float~.md) `sig2float~` converts signals to floats.

- :material-tune: [__substitute__](../objects/substitute.md) `substitute` will replace all recurring elements in a message, but if you have a 3rd argument, it operates in "first only" mode, where only the first element is replaced.
.

- :material-tune: [__dec2hex__](../objects/dec2hex.md) `dec2hex` converts decimal values to hexadecimal ones.

- :material-tune: [__bpbank~__](../objects/bpbank~.md) `bpbank~` is a bank made of `bandpass~` objects.

- :material-tune: [__mpe.in__](../objects/mpe.in.md) `mpe.in` sends "cooked" MPE data from external "raw" MIDI data or an internally connected device.

- :material-tune: [__sfz~__](../objects/sfz~.md) `sfz~` also has microtonal capabilities.

- :material-tune: [__display__](../objects/display.md) `display` can display a message just like `print`.

- :material-tune: [__tabgen__](../objects/tabgen.md) `tabgen` is an abstraction that generates different functions for a given table name.
.

- :material-tune: [__beat~__](../objects/beat~.md) `beat~` takes an input signal and outputs a detected BPM value.
.

- :material-tune: [__quantizer__](../objects/quantizer.md) `quantizer` approximates a value to step values defined by the argument.

- :material-tune: [__svf~__](../objects/svf~.md) `svf~` implements Chamberlin's state-variable filter algorithm, which outputs lowpass, highpass, bandpass, and band reject (notch) simultaneously in parallel (in this order from left to right).
.

- :material-tune: [__pvoc.live~__](../objects/pvoc.live~.md) `pvoc.live~` is like `pvoc.player~`, but for live input.

- :material-tune: [__gmean__](../objects/gmean.md) `gmean` creates a list of geometric means.

- :material-tune: [__sum__](../objects/sum.md) `sum` sums a list of values.
.

- :material-tune: [__ptouch.in__](../objects/ptouch.in.md) `ptouch.in` extracts MIDI polyphonic aftertouch information from raw MIDI input (such as from `midiin`).
.

- :material-tune: [__remove__](../objects/remove.md) `remove` removes one or more number elements from a list.

- :material-tune: [__xselect.mc~__](../objects/xselect.mc~.md) `xselect.mc~` selects between multiple channels from a multichannel connection (maximum 512 channels) with equal power crossfading.
.

- :material-tune: [__minimum__](../objects/minimum.md) `minimum` outputs the minimum of two or more values.

- :material-tune: [__osc.parse__](../objects/osc.parse.md) `osc.parse` is similar to Vanilla's `oscparse` but the output is not a list and more closely related on how OSC messages are generally dealt with.

- :material-tune: [__prepend__](../objects/prepend.md) `prepend` will add messages set as argument to the beginning of any message sent to the input.

- :material-tune: [__notedur2ratio__](../objects/notedur2ratio.md) `notedur2ratio` converts from a note duration symbolic syntax to a ratio (either as fraction or float).

- :material-tune: [__greaterthan~__](../objects/greaterthan~.md) `greaterthan~` or `>~` outputs a 1 signal when the left input is greater-than the right input or argument and a 0 when it is less-than or equal-to the right input or argument.
.

- :material-tune: [__conv~__](../objects/conv~.md) `conv~` performs partitioned convolution.

- :material-tune: [__score2__](../objects/score2.md) `score2` has a 'tempo' syntax where 'tempo 60' sets the bpm to 60! The 'tempo' messages are output in the third 'data' outlet.

</div>