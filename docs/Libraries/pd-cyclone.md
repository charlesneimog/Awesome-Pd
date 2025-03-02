# pd-cyclone

## `accum`

`accum` accumulates a value by either adding an increment value to it or multiplying it by a given factor.

Plugdata users or those with ELSE can also use `else/add` as an alternative.


## `acos`

## `acosh`

- Input to hyperbolic arc-cosine function, this value is stored and updates the argument.


## `acosh~`

Use `acosh~` to output the hyperbolic arc-cosine of each input sample. For input values less than 1, the output is zero.


## `acos~`

Use `acos~` to output the arc-cosine of each input sample. The input range is from -1 to 1, and the output range is from 0 to pi. For input values outside the -1 to 1 range, the output is zero.


## `active`

`active` outputs 1 when a patch canvas becomes active (its title bar is highlighted and it's the front-most window), and outputs 0 when inactive.

Plugdata users or those with ELSE can also use `else/canvas.active` as an alternative.
## `allpass~`

Use `allpass~` for filtering and delay effects. The All Pass filter passes all frequencies without altering the gain but changes the frequencies' phase.

Plugdata users or those with ELSE can also use `else/allpass.rev~` as an alternative.

## `anal`

By default, `anal` creates a table of transition probabilities from one note to another (1st order Markov chain). This patch shows how to create transition probabilities from two notes to a third note (2nd order Markov chain).

- Maximum size: 16384 (128*128) because two MIDI values are combined into one.
- Output: transitions from 2-note pairs to other 2-note pairs.
- Weed out the "previous" note stored in the high 7-bits.
- Playback is based on transition probabilities from the two preceding notes, yielding less random results than using one note at a time.
- Feed the received two-note sequences to `prob` for a 1st order Markov chain.
- Three floats: `<previous number, current number, occurrence>`.

`anal` reports how many times it received a number pair. It is designed to serve as input to `prob` to implement Markov Chains. The output is composed of:
1. The previously received number.
2. Current input number.
3. Occurrence (how many times this number pair has been received).

Plugdata users or those with ELSE can also use `else/markov` as an alternative.
## `append`

`append` will add messages set as argument to the end of any message sent to the input.

## `asin`

## `asinh`

Use `asinh` to calculate and output the hyperbolic arc-sine of any given number.

## `asinh~`

Use `asinh~` to output the hyperbolic arc-sine of each input sample.

## `asin~`

Use `asin~` to output the arc-sine of each input sample. The input range is -1 to 1 and the output range is from -pi/2 to pi/2. For input values outside the -1 to 1 range, the output is zero.

## `atan2~`

Use `atan2~` to output the arc-tangent of two given values ("a" and "b") calculated as: Arc-tangent (a/b). Useful for mathematical calculations such as finding the phase from cartesian coordinates.

## `atanh`

Use `atanh` to calculate the hyperbolic arc-tangent of any given number.

## `atanh~`

Use `atanh~` to output the hyperbolic arc-tangent of each input sample. For input values <= -1 or >= 1, the output is zero.

## `atan~`

Use `atan~` to output the arc-tangent of each input sample.

## `atodb`

Use `atodb` to convert linear amplitude values to decibel Full Scale (dBFS) equivalents. Negative values convert to -inf if the input is 0. Conversion formula: `dbFS = log10(amp) * 20`.

Plugdata users or those with ELSE can also use `else/lin2db` as an alternative.

## `atodb~`

Use `atodb~` to convert a signal representing a linear amplitude value to a decibel Full Scale (dBFS) equivalent. Conversion formula: `dbFS = log10(amp) * 20` (minimum output value is -999).

Plugdata users or those with ELSE can also use `else/lin2db~` as an alternative.

## `average~`

Use `average~` for a signal running/moving average over the last 'n' given samples. The average is done in 3 modes: bipolar (default, an arithmetic mean), absolute (arithmetic mean over absolute values), and rms (moving RMS average).

Plugdata users or those with ELSE can also use `else/mov.avg~` and `mov.rms~` as alternatives.

## `avg~`

Use the `avg~` object to keep track of the absolute average from the input signal when receiving a bang. The output value is the sum of the absolute values of the input divided by the number of elapsed samples.

## `bangbang`

When it receives any input, `bangbang` outputs bang messages out of each outlet (in the usual right-to-left order). The number of outlets is determined by the argument.

## `bitand~`

`bitand~` compares the bits of two values with "Bitwise-AND" (bits are set to 1 if both are "1", 0 otherwise). It compares two signals or a signal to a given bitmask. It can produce NaNs and +/-INFs - but denormals are zeroed out and has 4 modes of comparison.

Plugdata users or those with ELSE can also use `else/op~ &` as an alternative.

## `bitnot~`

`bitnot~` takes a signal and performs a Bitwise NOT operation, also known as bitwise inversion or one's complement (all bit values of 1 are set to 0 and vice versa). The operation is done in two modes.

Signals are 32-bit floating point by default and their 32-bit representation is used for comparison. When converting a signal to integer, the floating point value is converted/truncated to an integer, and the 32-bit signed integer representation of this value is used for the operation.

Plugdata users or those with ELSE can also use `else/op~ ~` as an alternative.

## `bitor~`

`bitor~` compares the bits of two values with a Bitwise OR operation (bits are set to 1 if any of them is 1, 0 otherwise). It compares two signals or a signal to a given bitmask. It can produce NaNs and +/-INFs, but denormals are zeroed out and has 4 modes of comparison.

Signals are 32-bit floating point by default and their 32-bit representation is used for comparison. When converting a signal to integer, the floating point value is converted/truncated to an integer value and the 32-bit signed integer representation of this value is used for comparison.

Plugdata users or those with ELSE can also use `else/op~ |` as an alternative.

## `bitsafe~`

`bitsafe~` replaces NaN (not a number) and +/- infinity values of an incoming signal with zero, which is useful in conjunction with the bitwise operators in cyclone or any other situation where these values are possible. It also filters out denormals and turns them to zero.

Plugdata users or those with ELSE can also use `else/bitnormal~` as an alternative.

## `bitshift~`

`bitshift~` takes a signal and performs Bitwise Shifting (shift bit values to the left or right) depending on a shift value (positive values shift that number of bits to the left, while negative values shift to the right). The operation is done in two modes.

Signals are 32-bit floating point by default and their 32-bit representation is used for comparison. When converting a signal to integer, the floating point value is converted/truncated to an integer, and the 32-bit signed integer representation of this value is used for the operation.

Plugdata users or those with ELSE can also use `else/op~ >>` or `else/op~ <<` as alternatives.

## `bitxor~`

`bitxor~` compares the bits of two values with "Bitwise eXclusive OR" (bits are set to 1 if different, 0 otherwise). It compares two signals or a signal to a given bitmask. It can produce NaNs and +/-INFs, but denormals are zeroed out and has 4 modes of comparison.

Signals are 32-bit floating point by default and their 32-bit representation is used for comparison. When converting a signal to integer, the floating point value is converted/truncated to an integer value (e.g., 1.7 becomes 1) and the 32-bit signed integer representation of this value is used for comparison.

A float input into the second inlet is converted to int and updates the argument. If a signal is connected to the second inlet, the float input will still update the argument, but the signal input has priority over the argument or the float input.

Instead of an argument or float input, you can also specify a bitmask with the "bits" message. The given bitmask as the "bits" message overwrites the given argument, and a float input in the secondary inlet overwrites the bitmask. If a signal is connected to the second inlet, it has priority over the given bitmask.

Plugdata users or those with ELSE can also use `else/op~ ^` as an alternative.


## `bondo`

`bondo` synchronizes and outputs messages when any inlet gets a message. It can wait a time interval for input messages or send them automatically.

A second argument specifies a time interval to wait for incoming messages, so it is able to sync them and output them all at once. One element messages go to the corresponding outlet. If there are more than 1 element, they're parsed among the inlets unless the "n" argument is used.

Plugdata users or those with ELSE can also use `else/hot` as an alternative.


## `borax`

`borax` outputs information about incoming MIDI note messages, such as pitch, velocity, and channel.

Plugdata users or those with ELSE can also use `else/noteinfo` as an alternative.


## `bucket`

`bucket` outputs the input values in a rotational pattern, shifting from outlet to outlet.

- Output flag: <0> (default) holds the input and passes it on the next round, <1> outputs the input immediately.


## `buddy`

`buddy` synchronizes arriving data and outputs them only if messages have been sent to all inlets. The output is in the usual right to left order, and all input is cleared after that.


## `buffer~`

`buffer~` stores audio in a memory buffer (an array). It reads/writes multichannel audio files and can be used in conjunction with `play~` and other related objects.

- `read` - Reads a file specified by a symbol (.wav, .aif/.aiff, or .caf).
- `write` - Saves the contents of `buffer~` into an audio file.
- `replace` - Replaces the buffer with the sample size and number of channels.
- `readagain` - Reads and loads the previously opened file again.
- `apply gain` - Scales every sample by the given gain coefficient.
- `apply offset` - Adds the offset to every sample in the buffer.
- `fill` - Sets every sample in the `buffer~` to a specified value or function (sin, cos, sinc).

Plugdata users or those with ELSE can also use `else/sample~` and `else/tabgen` as alternatives.

## `buffir~`

`buffir~` is a table/buffer based FIR (finite impulse response) filter. An input signal is convolved with 'n' samples of a buffer.

The `buffir~` object works with any kind of array set in Pd, and not only from the `buffer~` object. In the case of a multi-channel `buffer~` object, `buffir~` can only read its first channel.

Plugdata users or those with ELSE can use the more powerful `else/conv~` for partitioned convolution as an alternative.


## `capture`

`capture` stores items in the received order for viewing, editing, and saving to a file. If the maximum number of items is exceeded, the earliest stored item is dropped.

Second arguments encode the way numbers are displayed (but not stored):
- no argument (default): ints are displayed as decimals
- "x": ints displayed as hexadecimals
- "m": ints less than 128 (as in MIDI values) are decimal, but larger are hexadecimals
- "a": only symbols are displayed

Floats are always stored as floats, and according to the given precision.

- `count`: outputs the number of received items since the last 'count' message
- `dump`: outputs stored elements sequentially (first in, first out)

You can set the display format for integer numbers with a second argument. The precision for floats can be set with the `@precision` attribute or message.


## `capture~`

`capture~` is designed for signal debugging/investigation, it captures samples into a text window or text file. `capture~`'s window holds limited data, so you can capture more than you can see. If so, write it to a text file and open elsewhere.

Optional flag "f" for "first mode" - where collecting data stops after receiving the specified number of samples. If not given, the default is "last mode", where it continues to collect data, throwing away old values if it has received more than the specified samples.


## `cartopol`

`cartopol` converts cartesian coordinates (real / imaginary) to polar coordinates (amplitude / phase).

Plugdata users or those with ELSE can also use `else/car2pol` as an alternative.


## `cartopol~`

Use the `cartopol~` object to convert signal values representing cartesian coordinates to a signal composed of polar coordinates - useful for spectral processing.

If the right outlet isn't connected to anything, the object won't compute the phase, saving you some CPU.

`cartopol~` is useful for spectral processing in the more intuitive polar form (with amplitude and phase values). This is because when performing spectral analysis in Pd, the signal is in the cartesian form, so we need `cartopol~` and `poltocar~` to convert to and from the polar form in order to perform the FFT and iFFT.

Plugdata users or those with ELSE can also use `else/car2pol~` as an alternative.


## `change~`

Use `change~` to detect if a signal is changing and its direction. It outputs "1" if the signal is increasing, "-1" if it's decreasing and "0" if it doesn't change.

Plugdata users or those with ELSE can also use `else/changed2~` and `else/changed~`.


## `click~`

`click~` generates an impulse when receiving a bang. An impulse is a single sample with a value of one followed by zeros, and this is the default impulse generated by `click~`, but you can also set an impulse with a different amplitude value or even as a list of values (for band-limited impulses - maximum is 256 sample values).

Plugdata users or those with ELSE can also use `else/impseq~`.


## `clip`

Use `clip` to constrain values from floats or lists between a range specified by a minimum and a maximum value.

Pd also has a vanilla object named `clip`. Cyclone avoids name clashing and overwriting an internal in Pd Vanilla, but for that, you need to use the cyclone namespace ("cyclone/" before the object name), as it's the common practice for cyclone's documentation.


## `clip~`

Use the `clip~` object to constrain input signals between two specified values (minimum and maximum). If the maximum value is less than the minimum, it becomes the minimum value and vice-versa.

Pd also has a vanilla object named `clip~`. Cyclone avoids name clashing and overwriting an internal in Pd Vanilla, but for that, you need to use the cyclone namespace ("cyclone/" before the object name), as it's the common practice for cyclone's documentation.

## `coll`

`coll` stores and edits any messages at given addresses (an integer or a symbol). If an input list starts with an int, it stores the other element(s) at that int address.


## `comb~`

If the delay time lies between two samples, a simple linear interpolation is performed.;

[comb~] is a comb filter, use it for filtering and delay effects.;

Plugdata users or those with ELSE can also use [else/comb.rev~] as an alternative, f 43;


## `comment`

When in edit mode, [comment] shows its inlet and an outline. The [comment] object below has a receive symbol, so you can send messages to it via a [send] object. In this case, the inlet is suppressed, so we don't see it. Besides the properties window, the receive symbol can be set with the receive message or the @receive attribute. If you set a receive name as "empty" then it it can't receive messages anymore and the inlet is show again., f 74;

Note: when in edit mode, you can click on the object to select it and then press <F5> to copy the comment from [cyclone/comment] into a Pd's comment box. So far, this is the only way to copy the text from comment into Pd (control+c / control+v doesn't work)., f 65;

[comment] uses "Dejavu Sans Mono" as its default font, just like Pd. But, as of version 0.51-3, Pd uses 'Menlo' as its default font for macOS, so [comment] also defaults to this font in macOS., f 62;

After setting a background color you can use the 'bg' attribute to turn it off or on again., f 62;

Cyclone's [comment] will attempt to open a font name that corresponds to your given name. If such a font name doesn't exist, it'll open some other font you have on your system instead that it thinks is best for what you requested, and you'll have no idea which one it is. So just be sure you have the fonts you want properly isntalled., f 62;

This object is fully compliant to Max 5 but not fully compliant to Max6+ versions (with all that 'bubble' stuff and more). It also has inconsistencies like different attributes than the original object in Max. It is also now based on [else/note], an object that was first based on [cyclone/comment]., f 65;

By default, [comment] has a maximum width limit of 425 pixels (like Pd's comment). If it exceeds this limit, the comment will break into a new line with the last word that did not fit. But when in edit mode you can see a bar to the right that allows you to resize the object. If you click and drag it, you'll set a new maximum width to the point where you release the mouse button., f 66;

And when you have more than one line, you can set three kinds of justification parametrers: left (0: default), center (1) and right (2). This does not affect comments with just one line., f 66;

Note you can use backslash to escape symbols like '$', commas and semicolons., f 19;

Comment also takes characters from different alphabets like elsewhere in Pd (such as in messages or comments)., f 29;

@fontname <symbol> (default: 'dejavu sans mono' or 'menlo' for mac) | @fontsize <float> (default patch's) | @textjustification <float> (default 0) | @textcolor <f, f, f> (default 0 0 0) | @bgcolor <f, f, f> (default 255 255 255) @bg <float> (default 0) | @text <anything>: sets comment (default "comment") | @underline | @bold | @italic | @receive <symbol> (default 'empty'), f 80;

[comment] is a GUI meant to be only a comment (a label or a note) that can be typed directly into it when in Edit mode. Unlike pd vanilla's comments, it allows you to set font, size, color, background color, bold, italic, underline and justification. This object is not being fully compliant to Max6+ versions! It is also now related to [else/note]. Since Cyclone 0.7-1 this object is being considered DEPRECATED., f 83;


## `cosh`

- input to hyperbolic cosine function, this value is stored and updates the argument;


## `cosh~`

Use [cosh~] to output the hyperbolic cosine function of each input sample (probably only useful for mathematical calculations).;


## `cosx~`

Like [cyclone/sinx~] & [cyclone/tanx~], [cosx~] expects input values in radians. Thus, unlike [cos~] (from Pd vanilla and max/msp), it's not designed to work with [phasor~]'s output (from 0 to 1) and used for mathematical operations., f 68;


## `counter`

sets direction to shift between up/down when reaching limits, f 63;

1st float sets 'carryflag': 0 (carryint), 1 (carrybang). 2nd sets 'compatmode' mode: 0 (current), 1 (ancient), f 56;

sets counter's next value (considering direction) - no output, f 63;

sets @carryflag attribute: (0 = carryint, 1 = carrybang), f 63;

----------------------------------------------------------------------------------, f 82;

sets to "carryint" mode (default): sends "1" at the end of a count round, "0" at the start of the next round, f 63;

sets counter to that value and outputs it - values outside the range are ignored, f 63;

(in any inlet) prints current settings state on the Pd window, f 63;

sets direction, 0: up, 1: down, 2: updown (alternating), f 60;

when max is reached (if 'carrybang' is set & counting up), f 61;

when min is reached (if carrybang is set & counting down), f 61;

sets counter value and outputs it - if outside the range, it resets min/max according to compatmode (see example above);

@compatmode: 0 for current (default) / 1 for ancient (see example above), f 72;

The 'compatmode' message or attribute sets to "current" or "ancient" mode. In both modes, a float input into the 3rd inlet sets the counter value but does not output it and a float input into the 4th inlet sets the counter value and outputs it. But its behaviour is diffetent.;

In the default current mode ('compatmode 0') - a number outside the range sets the minimum or maximum value just once, reverting to the original range after a round. But in 'compatmode 1' ('ancient mode', for max 3.x compatibility), it always sets the minimum value.;

The 'flags' message sets both attributes at once, the 1st argument is for carrymode (0: carryint, 1: carrybang) and the 2nd is for compatmode (0: current, 1: ancient).;

The 'carrybang'mode sends just one bang when reaching maximum (3rd outlet) and minimum (2nd outlet);

The 'carrymode' sets how [counter] responds at the end of a round (when it reaches the upper limit when counting up or the lower limit when counting down).;

The default mode is 'carryint'. When counting up, it outputs '1' when reaching the maximum value out the 3rd outlet, and outputs '0' after leaving the maximum value. And when counting down, it outputs '1' when reaching the minimum value out the 2nd outlet and outputs '0' after leaving it.;

You can set the carrymode with the messages 'carryint' and 'carrybang', but also with the @carryflag attribute or message - 'carryflag 0' sets to 'carryint' (the default) and 'carryflag 1' to 'carrybang';

The 'state'message reports the current settings of [counter] on the Pd window.;

A float in the leftmost inlet is the same as a bang, so you can bcount how many floats have been received.;

An example of usage: - Setup a [metro] to turn [counter] into a step sequencer, such as the 8-step example below.;

x_mincount: - the minimum value; x_maxcount: - the maximum value; x_direction: - the direction mode: 0/1/2 (up/down/updown); x_curcount: - the current count value; x_curdir: - the current direction: 0/1 (up/down); x_carrycount: - how many times it reached the maximum; x_carry: - carryint value (0/1) when counting up; x_under: - carryint value (0/1) when counting down; x_carrymode: - carrymode: 0/1 (carryint/carrybang); x_compat: - compatmode: 0/1 (current/ancient); x_startup: - '1' if still in the startup value, '0' if not; x_inletnum: - inlet number that the state message came in;, f 60;

sets counter value with no output - if outside the range, it resets min/max according to compatmode (see example above);

If there are no arguments, the direction is up, the minimum is 0, and the maximum is 6.777.216 (2^24), the largest integer possible in Pd (in Max is 2^31 - 1).;

A bang or a 'next' message makes counter go to the next value. Note that it starts from the minimum (which is 0 in the example below).;

Only one argument sets the maximum value, so it counts from 0 to that value. Two arguments set the minimum and maximum value (in any order: the smaller of the 2 is always the minimum, and the greater is the maximum).;

Given three arguments, the 1st sets the direction (0: up, 1: down, 2: updown) and 2nd and 3rd the min/max (also in any order).;

If the direction is up and you reach the maximum, it restarts from the minimum. The 'carrycount' output (rightmost outlet) counts how many times the maximum was reached (but it doesn't count if the direction is down)., f 61;

If the direction is down and you reach the minimum, it restarts from the maximum value. When in "updown" mode, at the end of each count round (reaching maximum or minimum) it swiches the direction., f 61;

A bang in the 2nd inlet switches the direction from up to down or vice versa (it switches from mode 0 to 1 or from 1 to 0, but only changes the direction in mode 2)., f 61;

You can also set the direction with the messages "up", "down" and "updown" or a float input in the 2nd inlet, see below., f 61;

The jam message sets the counter value and outputs it. Values outside the range are ignored. The 'inc' & 'dec' messages are used to count up or down from the last output regardless of the direction.;

The set message sets the next value (values outside the range are also ignored) without outputting it, so it needs a 'next' or bang message afterwards. As the direction is considered, don't change the direction before sending the next message. The 'goto' message is the same as 'set'.;

The 'min' message sets a minimum value and otputs it. The 'setmin' message only sets it (no output). The 'max' message sets a new maximum value but doesn't output it (it's the same as a float input in the 5th inlet).;

A bang in the 3rd inlet sets the next value as the minimum. A bang in the 4th inlet sets to the minimum and outputs it. A bang in the 5th inlet sets to the maximum and outputs it.;

Careful, you shouldn't set the minimum greater than the maximum or the maximum lesser than the minimum! If so, [counter] gets stuck, but you can set the minimum/maximum back to a proper value., f 63;

IMPORTANT: All numbers that set the counter's value or range are integers, so all floats are converted to integers by disconsidering (truncating) the decimal part.;

1 float: max / 2 floats: min & max / 3 floats: direction (0: up / 1: down / 2: updown), min & max - default values: direction = 0 (up), min = 0, max = 2^24.;

1 when min is reached, 0 when next round starts (if carryint is set and counting down), f 61;

1 when max is reached, 0 when next round starts (and 'carryint' is set and counting up), f 61;

Plugdata users or those with ELSE can also use [else/count] as an alternative, f 39;


## `count~`

A signal input can trigger count with sample accuracy. A non-zero value turns the counter on, a zero value stops it.;

[count~] outputs a signal increasing by 1 for each sample elapsed. It starts at a given minimum and it can loop at a given maximum value (which is actually that value - 1).;

Plugdata users or those with ELSE can also use [else/comb.rev~] as an alternative, f 43;


## `cross~`

It has two outlets for lowpass (left) and highpass (right) filters that you can use separately or in combination to form a crossover filter.;

Plugdata users or those with ELSE can also use [else/crossover~] as an alternative, f 42;


## `curve~`

Try different curve factor values (from -1 to 1). The closer to 0 the curve parameter is, the closer the curve is to a straight line, and the farther away the parameter is from 0, the steeper the curve., f 54;

The object's approximation of the exponential becomes better when the block size is smaller, but the object also becomes more computationally expensive., f 33;

you can set the parameter with: - the second argument: - the third inlet: - the "factor message": - the third value in a list., f 54;

- curve duration in ms - works only if a float is sent into the left inlet after, and it works only once.;

Similar to [cyclone/line~], but [curve~] produces curved (non linear) ramp signals. Below, when receiving 2 triples (of destination, time & curve factor), [curve~] generates a simple Attack-Release envelope., f 79;

- up to 42 triplets composed of: 1) destination value, 2) time (ms) & 3) curve factor (from -1 to 1)., f 56;

- jumps immediately to that value (unless the duration is set before to other than 0 in the mid inlet);

Plugdata users or those with ELSE can also use [else/envgen~] as an alternative, f 41;


## `cycle`

Each incoming number is sent to the next outlet, wrapping around to the first outlet after the last has been reached, completing a cycle in a "round-robin scheduling" way.;

- any message type. Messages with more than one element outputs each element to a different outlet;

Examples of separate events include messages with delays between them, and messages triggered by successive mouse clicks or MIDI events.;

A stream of items separated by commas in a message box is considered a single event.;

In the event sensitive mode (set with the second argument or with the "tresh" message), any new event will restart the output from the leftmost outlet. In the default mode (0), the values cycle through all the outlets, regardless of whether they are attached to separate events or not.;


## `cycle~`

This is different than the "set" message or setting the array name as the second argument, in which cases [cycle~] only reads 512 points from the buffer. This is because [cycle~] could historically only read 512, so it still works that way for backwards compatibility issues.;

This attribute allows other buffer sizes than 512 points (when using the set message or by specifying the buffer as the second argument) or the entire array (via the setall message or the buffer attribute).;

Thus, the @buffer_sizeinsamps attribute (also setable via the "buffer_sizeinsamps" message) sets to size values in powers of two from 16 to 65536 (13 values from 2^4 to 2^16).;

Possible values; - 16; - 32; - 64; - 128; - 256; - 512;

- 1024; - 2048; - 4096; - 8192; - 16384; - 32768; - 65536;

The @buffer_offset attribute (also as the "buffer_offset" message) followed by a float sets the sample offset into the buffer. If your offset is too large and close to the end of the table), the remainder is filled with zeros.;

The @buffer attribute (also setable via the "buffer" message) is analogous to the "setall" message. This means that the buffer attribute followed by an array name sets that entire array to be used as the waveform., f 60;

Other possible values are: "-1", which sets to the entire buffer's length, and "0", which sets to 512 samples.;

Below we have [cycle~] reading 4096 points from the buffer with an offset of 1 sample. This means it doesn't read the first and the last 2 samples from this 4099 points buffer, which are, by the way, the guardpoints generated by the "sineseum" command for interpolation in the other subpatch ([pd set/setall]).;

Other attributes are: @frequency (nothing special about it) and @phase (see the next subpatch example on phase)., f 33;

The second inlet in [cycle~] can set a phase offset with values between 0 and 1 (but values over this boundaries are wrapped internally to the 0-1 range)., f 56;

[cycle~] conveniently allows phase modulation with its second inlet.;

The phase is also resset in many operations in edit mode - so nevermind if you hear "clicks" when editing the patch!, f 43;

You can't resset the phase of [cycle~] as you can with [osc~], but note that the the phase gets resseted to the beggining of the cycle when you turn the DSP off and then on again, f 46;

[cycle~] is a linear interpolating oscillator* that reads repeatedly through one cycle of a waveform. The default internal waveform is one cycle of a cosine wave (16k in size, 64 bits), but you can set other waveforms from given arrays., f 69;

sets array used as the wavetable (but only reads 512 points from the buffer), default: internal cosine table, f 55;

The [cycle~] object works with any kind of array set in Pd as well with arrays set in the [buffer~] object. In the case of a multi channel [buffer~], [cycle~] will only read its first channel.;

The set message with no arguments sets the internal waveform (16k cosine, 64 bits). A set message followed by a symbol sets the array to be used as a waveform. After the name, you can also optionally set an offset for that table.;

If you have an array with more than 512 samples, you can scroll through the array with an offset index value, but it'll only read 512 samples from it. If not enough table points are available (as if you have a table smaller than 512 samples or if your offset is too large and close to the end of the table), the remainder is filled with zeros. Below we have a table with 4099 points to use with [cycle~].;

With the set message, [cycle~] reads only 512 points in a table (because historically it could only deal with 512 points tables - other new messages allow more points).;

The "setall" message behaves the same as the buffer method or attribute. Hence, followed by an array name, it sets that entire array to be used as a waveform (a 4099 points wavetable in this case). This is quite different than the "set" message or the second argument, which only reads 512 points from the buffer.;

Plugdata users or those with ELSE can also use [else/wavetable~] as a more powerful alternative, f 34;


## `cyclone`

You can also find alphanumeric versions of these objects (with the same name alias as in Max/MSP) as single separate binaries, they are:, f 70;

Note that even though the non-alphanumeric versions come from a single binary pack, it is also possible to load them with the "cyclone/" prefix., f 56;

The binary is also loaded as the cyclone object. This also loads the library, but you shouldn't load it this way! The object only accepts the "about" message, which prints basic information (objects, version, release date) on the terminal and the "version" message that outputs the cyclone version as a list of major, minor, bugfix., f 71;

The cyclone library also automatically loads cyclone's path to Pd so you can load the separate binaries (but this doesn't guarantee search priority). Objects from the cyclone library are mostly a set of separate binaries, but also contains a few abstractions. You can load the cyclone library via "Startup" and "Path" (to guarantee search priority). Alternatively, you can use [declare] as follows:, f 71;

Click and open "how to install" link from the repository for more details =>, f 39;

The cyclone's single binary pack contains non-alphanumeric operator objects that need to be loaded as a library to avoid issues. For more information, check:, f 71;


## `dbtoa`

Use [dbtoa] to convert decibel values to corresponding linear amplitude.;

Plugdata users or those with ELSE can also use [else/db2lin] as an alternative, f 40;


## `dbtoa~`

[atodb~] takes any given signal representing a dBFS amplitude value and outputs a signal which is a linear amplitude conversion of the input.;

Plugdata users or those with ELSE can also use [else/db2lin~] as an alternative, f 41;


## `decide`

[decide] alternates randomly from 1 to 0 (the sequence depends on the seed value).;

sets the seed for the random number generator. 0 will use a random seed, any other integer float is the seed, f 55;

This is a very silly object, since you cabn just do this instead:, f 21;


## `decode`

If the input is higher than the number of given outlets, then "1" is sent to the rightmost outlet. But if it's less than 0, then "1" is sent to the leftmost outlet.;

The right inlet is the master disable switch. If it is on, all outlets are switched off.;

The middle inlet is a submaster switch. If the right inlet switch is off, this enables all unmatched outlets to be switched on or off.;

Therefore, the left inlet can turn on a single outlet on or off only if the submaster and master switches are off!;

As for the left inlet behaviour, here's a similar vanilla implementation as an alternative., f 21;

[decode] receives a number and looks for a corresponding outlet (numbered from left to right, starting at 0) to switch it on (output: 1) and the others off (output: 0).;


## `degrade~`

[degrade~] takes any given signal and reduces the sampling rate and bit-depth as specified/desired.;

Plugdata users or those with ELSE can also use [else/crusher~] as an alternative, f 42;


## `delay~`

[delay~] delays a signal by a number of samples (thus the delay time depends on the sample rate).;

[delay~] in max can set its delay time with max's time format syntax, that depends on a global transport or [transport] objects, which is not implemented in cyclone as of yet.;

With a float input, values are truncated to integer values. Thus, [delay~] doesn't interpolate.;

You can use a signal to specify the delay time with interpolation, but that also adds an extra sample delay., f 53;

Thus, when the delay time is controlled by a signal, the input is always delayed at least 1 sample., f 53;

You can change the maximum delay size with the "maxsize" message.;

The ramp message sets a ramp time to a new target value, so when you send it a float message it takes that long to reach the new target. In this case, it does interpolate during the ramp time.;

If you set a new target while a ramp is still happening, it'll wait until the target is reached before going to the next target. A new ramp time is also only set after a ramp is finished.;

Plugdata users or those with ELSE can also use [else/ffdelay~] as an alternative, f 42;


## `deltaclip~`

- The input signal is sent out, with its change limited by the delta minimum and maximum values., f 55;

[deltaclip~] limits the change between samples in an incoming signal. This is also known as 'slew limiting'. It has a negative maximum delta for when the signal decays and a positive maximum delta for when it rises. When they're both 0, the signal doesn't shift. Below we divide by the sample rate to get the max amplitude shift per second isntead of per sample., f 71;

Plugdata users or those with ELSE can also use [else/slew2~] as an alternative, f 31;


## `delta~`

What's the increment between successive samples of a phasor output at 10 Hz?, f 20;

[delta~] outputs the difference between each incoming sample and the previous sample. So, if the input signal contains 1, 0.5, 2, 0.5, the output would be 1, -0.5, 1.5, -1.5;

A simple Vanilla alternative is to use [rzero~ 1] instead., f 29;


## `downsamp~`

[downsamp~] samples and holds a signal received in the left inlet at a rate expressed in samples. No interpolation of the output is performed.;

You can specify the number of samples with floating-point values, but the downsamp~ object will sample the input at most as frequently as the current sampling rate (1 sample).;

Plugdata users or those with ELSE can also use [else/downsample~] as an alternative, f 42;


## `drunk`

[drunk] generates random numbers within a given step range from the current number (generating a "drunk walk"). The random number is from 0 to a given maximum and differs from the previous number by a random value less than the given step size.;

Plugdata users or those with ELSE can also use [else/drunkard] as an alternative, f 42;


## `edge~`

[edge~] detects signal transitions from zero to non-zero and vice versa and reports bangs accordingly.;

Plugdata users or those with ELSE can also use [else/status~] as an alternative, f 42;


## `equals~`

[equals~] or [==~] outputs a signal that is "1" when the left input is equal to the right input/argument or "0" when it isn't.;

Plugdata users or those with ELSE can also use [else/op~] as a better alternative., f 28;


## `flush`

Like a "panic button", [flush] keeps track of Note-on messages that weren't switched off and "flushes" them by sending corresponding note-offs when it receives a bang.;

Note, however, that if you're using [poly] (as in the [pd polysynth] abstraction above), you can use the "flush" message.;

Plugdata users or those with ELSE may also be using objects that also have built in 'flush' options, such as [else/voices], [else/midi] and [else/keyboard]., f 32;


## `forward`

The [forward] object can send messages to different destinations and also control the sending order. See equivalent examples below.;

You can also do all that with semicolons in messages anyway:, f 20;

[forward] is similar to [send], but the destination can change with each message (like a semicolon in a message in Pd/Max) - it also sends to anything that a [send] does (like to an array, to "pd", etc..).;


## `frameaccum~`

It can also automatically wrap at phase boundaries (from -pi to pi) via an argument.;

For each block, the first sample of its output will be the sum of all of the first samples in each signal block it has received, the second sample of its output will be the sum of all the second samples in each signal vector, and so on...;

[frameaccum~] was specially designed to compute a running phase of FFT frames by keeping an accumulated sum of the values in each sample of an incoming signal block.;

It can keep a running phase of an FFT because the FFT size is equal to the signal block size.;

- "1" enables phase wrapping between -PI and PI. "0" (default) disables and values are accumulated without bounds.;


## `framedelta~`

For each signal block, the first sample of its output will be the first sample in the current block minus the first sample in the previous block, the second sample of its output will be the second sample in the current block minus the second sample in the previous block, and so on.;

The [framedelta~] object was designed specially to compute a running phase deviation of a FFT analysis by subtracting values in each position of its previously received signal block from the current signal block. When used in a FFT subpatch, it can keep a running phase deviation of the FFT because the FFT size is equal to the block size.;


## `fromsymbol`

Below we convert a symbol composed of 3 floats (separated by spaces) into a list of 3 floats. Note [cyclone/tosymbol] is used as a handy way to convert any message to a symbol., f 47;

If you want convert a given symbol composed of elements that start with a symbol, you need to include the "list" selector in the symbol if you want it to be converted to a list, otherwise it'll convert to an "anything". Try it below:;

Note that a list with only one symbloic element is automatically converted to a symbol in pd, just as one float lists are converted to floats., f 50;

If you send a symbol message to [fromsymbol], it removes the "symbol" selector and converts the message to "anything" (composed of one element).;

And, as presented in the previous example, a symbol composed of more than one element without a list selector is converted to "anything" (with more than one element). Just making it really clear..., f 52;

Since the [fromsymbol] object removes the "symbol" selector, if you have a "symbol bang" message, it converts it to a bang:;

The separator message/attribute allows you to split a symbol into different elements by setting the character that separates one element from the other. The default separator is a "space".;

[fromsymbol] converts a symbol message to anything (any kind of message). Start by typing a float in the atom symbol box below and see how it converts to a float message, then check more examples to the right.;

Plugdata users or those with ELSE can also use [else/symbol2any] and [else/separate] as alternatives, f 34;


## `funbuff`

on a "next" message, the difference with the previous x value, f 61;

When using the next message, the midle outlet outputs the difference from the current 'x' value to the previous one. The right outlet sends a bang when reaching the end of the buffer. The next message needs a pointer position, this can be set by giving it an 'x' value or by the 'goto' message.;

The value '18' is compared to 'x' values in funbuff and is found in between the values 10 and 30 If you consider the difference from 30 to 10 (which is 20) to 100%, the value 18 is 40% over 10 and 60% under 30;

The corresponding 'y' value from 18 is also an interpolated value from the corresponding 'y' values of 10 and 30, which are 100 and 200, so it should be 140 (40% of the way from 100 to 200). Click and check.;

selects 5 elements staring from element 3 - the region from pointer 3 to 3 + 5 (8). Used for clipboard operations: cut, copy and paste., f 47;

A cut/copy operation can be pasted onto a different [funbuff] object!, f 34;

The 'find' message looks for 'x' values that correspond to the given 'y'.;

You can save the stored values of a [funbuff] into the patch with the 'embed' message. If you send it 'embed 1', when you save the patch, it also save the currently stored values into [funbuff]. If you send it 'embed 0' and save the patch, it won't save the contents and also clear if it had its contents saved.;

You can also save (with the 'write' message) and load (with the 'read' message) from files. The argument sets a file name to load and read from at startup. The 'read' and 'write' messages without a filename symbol opens a dialog box to open/save files.;

There can only be one 'x' value and a corresponding 'y'value. So you can rewrite a 'y' value by sending another pair message.;

The set message can add several pairs at once. The clear message erases all set pairs from the memory. The dump message dumps all pairs to the middle (y value) and left (x value) outlets;

If there's no matching 'x', [funbuff] uses the closest smaller 'x' and outputs its corresponding 'y' value., f 60;

if one float is given, deletes a pair for a matching 'x' value, if two floats are given, deletes a matching x/y pair, f 68;

copies the selected x/y pair to the clipboard and deletes it, f 68;

non-0 value saves the contents of the buffer when the patch is saved, f 68;

dumps all pairs to the middle (y value) and left (x value) outlets, f 68;

sets the buffer pointer to the specified <float> buffer element, f 68;

if a given 'x' doesn't exist, interpolates the 'y' value from 2 neighbouring x/y pair, f 68;

sends the lowest 'y' value in the buffer to the left outlet, f 68;

sends the highest 'y' value in the buffer to the left outlet, f 68;

reads buffer contents from the file name specified by the symbol. If no symbol is given, a file open box is shown, f 68;

writes buffer contents to the file name specified by the symbol. If no symbol is given, a file open box is shown, f 68;

sets x/y pairs in the buffer (more than one pair is allowed), f 68;

outputs the y value of the buffer element and goes to next pointer, f 68;

finds the 'x' values which have a 'y' that matches the given number, f 68;

same as interp, but uses the table specified by the symbol <s>, f 68;

selects a number of x/y pairs (specified by the 2nd float) starting from an index (specified by the 1st float) - for copy/cut/paste, f 68;

If a 'y' value is sent to the right inlet, the next input to the left inlet sets the value of 'x' and the pair is stored, otherwise an 'x' input does output its corresponding 'y'.;

x value of a x/y pair - saves the x/y pair if a y value was sent before to the right inlet, outputs a y value otherwise, f 60;


## `funnel`

[funnel] receives data from many inlets and funnels them to an outlet. The incoming data is tagged with an inlet number to be retrieved with [route] or [cyclone/spray]. It can also be used to store values into a table/coll.;

the second argument sets a starting offset (other than 0) for the inlet number output to let you combine multiple funnels more easily;


## `gate`

[gate] routes a message from the second inlet to one of 'n' specified outlets or none of them.;

Plugdata users or those with ELSE can also use [else/selector] as an alternative, f 42;


## `gate~`

You can set the outlet number with a signal input, this allows gate to be controlle with sample accuracy. Signal values are truncated to integers.;

[gate~] routes an input signal from the second inlet to one of 'n' specified outlets or none of them. If an outlet is not selected, it outputs zero values.;

outlet number to route to - values are truncated to integers and clipped from 0 to number of outlets, f 52;

Plugdata users or those with ELSE can use the much better [else/xgate~] or [else/xgate~] objects instead (see also their multichannel variations)., f 38;


## `grab`

messages in the inlet are sent to receive objects named by this symbol. In this case, there's no rightmost outlet.;

[grab] sends a message to another object and "grabs" its output, sending it through its outlet(s) isntead of the grabbed object.;

A 1st float argument sets the number of outputs, so you can connect to an object that has more than one output and grab all of them., f 52;

[grab] sets the value of GUIs but also grabs its ouotput. See how when you send it number values, the number box is set but doesn't output anything., f 26;

A 2nd symbol argument sets the name of a corresponding receive object to send a message to. The "set" message can change the name. This way, it grabs from the object connected to the [receive] object., f 54;

This is an extra feature for cyclone that is not available in MAX. Since Pd has built in receive names for atom boxes and other GUIs, [grab] in cyclone can also grab values from them., f 62;

First, let's have a look at how things work for GUIs without a built-in receive name, but that are connected to a [receive] object., f 62;

And now let's check how it is the same with a built-in receive name in the number box., f 62;

This works for all GUI objects in Pd Vanilla and can work even with GUI externals that have built-in receive names.;

When used with receive names, [grab] can be useful to retrieve and store data that can then be recalled as a preset.;

Plugdata users or those with ELSE can also use [else/retrieve] as an alternative with limited functionality, f 42;


## `greaterthaneq~`

[greaterthaneq~] or [>=~] outputs a 1 signal when the left input is greater-than or equal-to the right input or argument and a 0 when it is less-than the right input or argument.;

Plugdata users or those with ELSE can also use [else/op~] as a better alternative., f 28;


## `greaterthan~`

[greaterthan~] or [>~] outputs a 1 signal when the left input is greater-than the right input or argument and a 0 when it is less-than or equal-to the right input or argument., f 62;

Plugdata users or those with ELSE can also use [else/op~] as a better alternative., f 28;


## `histo`

[histo] can be helfull to use random "quantile" messages to make probabilistic choices based on past history.;

[histo] records how many times it received a positive integer (no floats allowed). An input number is sent out the left outlet and its occurrence at the right outlet. A number in the right inlet checks and outputs that number's histogram., f 62;

Plugdata users or those with ELSE can also use [else/histogram] as an alternative, f 42;


## `index~`

Please check the [buffer~] object for multichannel buffers =>, f 61;

Internally, it creates buffers with the above mentioned naming convention.;

The [index~] object also works with multi channel arrays (maximum 64). In this example we have 4 channels, which can be accessed as an argument or a float input into the right inlet. No argument loads the first channel by default.;

The name convention for multi channel arrays is the table name preceded by the channel number (starting from zero) and "-", such as: "0-", "1-", "2-", "3-", and so on...;

Since there's no interpolation, you can only play a sample at original speed. Using [cyclone/count~] for this purpose is very convenient - [index~] is less useful for general sample playback tasks than other objects such as [cyclone/play~] and [cyclone/wave~].;

[index~] reads an array without interpolation. The input signal specifies the table index. It's like [tabread~] but works with multi channel arrays and index values are rounded isntead of being truncated.;

Plugdata users or those with ELSE can also use [else/status~] as an alternative, f 42;


## `iter`

[iter] is similar to [unnpack], it splist a message (to floats/symbols) but outputs them sequentially in the given order.;

Plugdata users or those with ELSE can also use [else/iterate] as an alternative, f 41;


## `join`

[join] takes any type of messages (anything, float, symbol, list) in any inlet and combines them all into an output list.;

You can specify which outlets will trigger (make the inlet "hot") an output with the @triggers attribute. Just include a list of input numbers that match the inlet number. The first (left) inlet is 0, the second is 1 and so on (-1 makes all inlets "hot").;

define a list of input numbers that trigger an output (make the inlet "hot"): 0 is the first inlet, 1 the second and so on (-1 makes all inlets "hot"), f 53;

Plugdata users or those with ELSE can also use [else/merge] as an alternative, f 41;


## `kink~`

Distort [phasor~] with [kink~]. If the phase input times the slope is less than 0.5, the value is output. Otherwise, a complentary slope is used that goes from 0.5 to 1 (creating a bend or a "kink").;

Plugdata users or those with ELSE can also use [else/function~] and [else/function] as an alternative, f 43;


## `lessthaneq~`

[lessthaneq~] or [<=~] <~ outputs a 1 signal when the left input is greater-than or equal-to the right input or argument and a 0 when it is less-than the right input or rgument.;

Plugdata users or those with ELSE can also use [else/op~] as a better alternative., f 28;


## `lessthan~`

[lessthan~] or [<~] <~ outputs a 1 signal when the left input is less-than the right input or argument and a 0 when it is greater-than or equal-to the right input or argument.;

Plugdata users or those with ELSE can also use [else/op~] as a better alternative., f 28;


## `linedrive`

[linedrive] scales numbers from one range to another with an exponential curve. First argument is the input range (127 means from -127 to 127), second is output range (1 is from -1 to 1), third is exponential factor and fourth is the time (to be used with line~).;

The exponential formula is the same used in the classic mode of [cyclone/scale]! A value of "1" gives you a linear scale (no exponential). Values greater than one gives you an exponential curve, with larger values leading to steeper exponential curves. A typical value for this mode is "1.06". Below we have classic mode with expnential values from "1" (linear) to "1.2".;

you can use either [line~] from vanilla or [line~] from cyclone:;

The [linedrive] object was designed to work with the [line~] object. Here it is used to exponentially change gain values.;


## `line~`

- sets the time for the next float send to the left inlet, f 60;

- jumps immediately to that value unless duration is set to other than 0 via the second inlet, f 60;

- stops and clears pending target-time parameter triples (but continues outputting its last value), f 60;

- pairs that specify target value and duration (in ms) to reach it (maximum is 128 target-time pairs). For an odd number of elements, the last element is treated as another pair with 0 ms duration., f 60;

And still create the vanilla object from vanilla without namespaces as:;

Pd also has a vanilla object named [line~]. Cyclone avoids name clashing and overwriting an internal in Pd Vanilla, but for that you need to use the cyclone namespace ("cyclone/" before the object name), as it's the common practice for cyclone's documentation. So you create it as:;

[cyclone/line~] generates signal ramps or envelopes. It takes a target and a duration (in ms) values and generates a ramp from its current value to the target value in that period. Target and duration can be set as a list or in different inlets., f 64;

If you send it a list with an odd number of elements, the last element is treated as a target and the duration to get there is considered to be 0 ms. A single float value will similarly jump immediately to that value in 0 ms - unless a duration is set to other than "0" via the second inlet., f 64;

Plugdata users or those with ELSE can also use [else/envgen~] as an alternative, f 41;


## `listfunnel`

The second argument sets an index offset (other than 0) for the inlet number output to let you combine multiple funnels more easily;

[listfunnel] receives any message and indexes the elements in the format: [index] [element].;

Plugdata users or those with ELSE can also use [else/order] as an alternative, f 39;


## `loadmess`

- set followed by any message sets the message held by loadmess without any output;

@defer <0/1> (default: 0): when enabled, the output of the loadmess object is deferred (a loadmess with @defer 0 will be sent before and have priority over @defer 1);

- the loaded message (when the patch is loaded or when banged/clicked);

[loadmess] outputs a message automatically when the patch is loaded, or when the patch is an abstraction of another patch that is opened. Note that if you start Pd with the "-noloadbang" flag, [loadmess] will not output values when you load a patch, f 68;

Plugdata users or those with ELSE can also use [else/initmess] as an alternative, f 42;


## `lookup~`

This also allows other functionalities. For example, an LFO sine wave can scan through an audio sample forward and reverse, accelerating and decelerating, resulting in a turntable scratch effect. Check below.;

Input values (from -1 to 1) are mapped to table indexes. The default table size is 512 points, so the default start and end points are, respectively, 0 and 511 (since the table indexes are from 0 to 511).;

You can specify another table size by setting an endpoint that corresponds to the last index (table size - 1).;

If you raise the starting point, note that the table size will decrease. Also, if the start point is greater than the end point, then the indexes are reversed. Test it below:;

The minimum starting point is the index 0, and the maximum ending point is equal to the greatest index in the table. If you specify less or more than that, the actual value will be clipped to those min/max values.;

The [lookup~] object works with any kind of array set in Pd, and not only from the [buffer~] object. In the case of a multi channel [buffer~] object, [lookup~] can only read its first channel.;

[lookup~] uses arrays as transfer functions for waveshaping distortion, in which signal input values (from -1 to 1) are mapped to the table's indexes.;

Here we have a sound file going through a couple of transfer functions for waveshaping distortion. The "linear" function doesn't do anything to the audio input. The "clipping" function is a hard limiter and also adjusts the gain four times as much. For last, we have an exponential "s"-curve like transfer function.;

Plugdata users or those with ELSE can also use [else/shaper~] as more powerful alternative;


## `lores~`

[lores~] implements an inexpensive resonant lowpass filter. The first argument or middle inlet sets the cutoff frequency, and the resonance is set by the second argument or the right inlet. Below, we use a LFO to control the cutoff, resulting in a filter sweep effect., f 67;

- resonance (default 0): minimum is 0 (a little bit sharp) and maximum is 1 (as sharp as possible and also LOUD);

Since it is a recursive filter, you may need to use the "clear" message if it blows up., f 60;

The equation of the filter is <yn = scale * xn - c1 * yn-1 + c2 * yn-2>, where scale, c1, and c2 are parameters calculated from the cutoff frequency and resonance factor.;

Plugdata users or those with ELSE can also use [else/lowpass~] an alternative, f 39;


## `match`

When the input is a list, if a portion of the list matches the arguments, that part of the list is output.;

When the input is a sequence of single elements, the data is output when a sequence matches the arguments.;

The symbol 'nn' can be used as a wildcard for any number input.;

[match] can be used with just one element. Below, only the number 12 goes through...;


## `matrix~`

sets to "non-binary" mode and the gain value for connections. If not provided, "binary" mode is on;

in binary mode: <inlet#, outlet#, on/off>. In non binary mode: <inlet#, outlet#, gain, ramp>, f 51;

on <dump> messages, rightmost outlet dumps a list with all connections: <inlet#, outlet#, gain>, f 49;

outputs current state of all connections in the rightmost outlet a list: <inlet#, outlet#, gain>, f 51;

connects any inlet specified by the 1st value to outlet(s) specified by remaining value(s), f 51;

disconnects any inlet specified by the 1st value to outlet(s) specified by the remaining value(s);

- "non-binary" mode is set when there is a third argument (that also specifies the default gain for all connections)., f 62;

In non-binary mode, you can set gain values and ramp time (optional), f 36;

- In "binary" mode, connections are either on or off. This can cause audible clicks when routing., f 62;

- In this mode, connections formed with the <connect> message always have the gain specified by the third argument. However, list messages can alter the gain of connections formed with the <connect> message. So, if you want to specify the gain of each connection in "non-binary" mode, you must use list messages (see below)., f 62;

- A list message allows an arbitrary gain value set by the 3rd float. This mode also allows a 4th optional list item that sets the ramp time (for fade in/out or crossfading)., f 62;

- The 'dump' and 'dumptarget' are the same in this mode. The 'print' message is also the same but prints on the terminal isntead., f 62;

- The dump message in non-binary mode gives you the current gain state. The 'print' message is the same but prints on the terminal isntead. The 'dumptarget' message gives you the target gain and may not be the same as the current state because of the ramp time., f 62;

outputs target state of all connections in the rightmost outlet a list: <inlet#, outlet#, gain>, f 51;

only in non-binary mode (that is, if all 3 arguments are given, you can include a ramp value as an attribute) - default is 10 ms, f 43;

[matrix~] routes signals from any inlets to one or more outlets. If an outlet connects to more than one inlet, they are summed., f 64;

Plugdata users or those with ELSE can also use [else/mtx~] as an alternative., f 39;


## `maximum`

- value to compare maximum with left inlet (updates argument), f 61;

[maximum] outputs the maximum of two or more values. The right outlet outputs the index of the maximum. If given a float, it can compare to a 2nd value in the right inlet or argument. If given a list, the maximum of the list is given., f 69;


## `maximum~`

[maximum~] outputs a signal which is the maximum of two input signals, or the maximum of an input signal and a given argument.;


## `mean`

[mean] calculates a running/moving average of all received numbers (the sum of all received values by the number of received elements).;

Plugdata users or those with ELSE can also use [else/mov.avg] as an alternative., f 42;


## `midiflush`

Like a "panic button", [midiflush] keeps track of raw Note-on messages that weren't switched off and "flushes" them by sending corresponding note-offs when it receives a bang.;

Plugdata users or those with ELSE can also use [else/panic] as an alternative, f 42;


## `midiformat`

[midiformat] receives different MIDI information in each inlet and formats to a raw MIDI message output.;

using [midiformat] to get note messages from a [makenote] object and send it to a [seq] object;

[midiformat] is the counterpart of the [midiparse] object. Please check it too.;

By default, [midiformat] receives a low resolution 7 bit (values from 0 to 127) for Pitch Bend messages, but the 'hires' message or attribute sets to a high resolution of 14 bits, which has been the usual resolution for Pitch Bend messages for a long time.;

The first one determines it's a Pitch Bend message and it is 224 for channel 1 (225 for channel 2, and so on up to 239 for channel 16).;

Then we have the two subsequent numbers that decode the Pitch Bend Value. First there's the Least Significant Byte and then the Most Significant Byte.;

The possible values are 0 (default, 7 bits), 1 (14 bit as float values from -1 to 1) and 2 (14 bits as integer values from -8192 to 8191). The [midiparse] object, which is the counterpart, also has the same parameters.;

@hires <0, 1, 2> - pitch bend precision (see example above);

Plugdata users or those with ELSE can use dedicated objects like [else/note.out] as alternatives, f 33;


## `midiparse`

[midiparse] receives raw MIDI data and retrieves different MIDI messages from it.;

[midiparse] is very useful to retrieve MIDI data from the [seq] object.;

The first one determines it's a Pitch Bend message and it is 224 for channel 1 (225 for channel 2, and so on up to 239 for channel 16).;

Then we have the two subsequent numbers that decode the Pitch Bend Value. First there's the Least Significant Byte and then the Most Significant Byte.;

By default, [midiparse] retrieves a low resolution 7 bit (values from 0 to 127) for Pitch Bend messages, but the 'hires' message or attribute sets to a high resolution of 14 bits, which has been the usual resolution for Pitch Bend messages for a long time.;

The possible values are 0 (default, 7 bits), 1 (14 bit as float values from -1 to 1) and 2 (14 bits as integer values from -8192 to 8191). The [midiformat] object, which is the counterpart, also has the same parameters.;

@hires <0, 1, 2> - pitch bend precision (see example above);

Plugdata users or those with ELSE can use dedicated objects like [else/note.in] as alternatives, f 33;


## `minimum`

- Numbers in a list are compared with each other, not with the argument!;

- The minimum number in a list is output in the left outlet, its index (from 0) is output in the right outlet. The next minimum updates the argument.;

- value to compare minimum with left inlet (updates argument), f 61;

[minimum] outputs the minimum of two or more values. The right outlet outputs the index of the minimum. If given a float, it can compare to a 2nd value in the right inlet or argument. If given a list, the minimum of the list is given., f 71;


## `minimum~`

[minimum~] outputs a signal which is the minimum of two input signals, or the minimum of an input signal and a given argument.;


## `minmax~`

[minmax~] outputs the minimum and maximum values (as signals and floats) of an input signal since the startup or a reset.;

Plugdata users or those with ELSE can also use [else/range~] as an alternative., f 42;


## `modulo~`

[modulo~] or [%~] is a signal remainder operator. The left signal is divided by the right inlet input (or argument), and the remainder is output.;

Plugdata users or those with ELSE can also use [else/op~] as a better alternative., f 28;


## `mousefilter`

[mousefilter] doesn't let messages through when the mouse button is down/clicked (but the last received message is output when the mouse button is released).;


## `mousestate`

- poll position data automatically when mouse cursor moves, f 61;

Mode 0 (default) uses "screen-relative coordinates", where (0, 0) is the top left corner of the primary display.;

There are 3 different modes in [mousestate] that define what the coordinate (0, 0) of the (x, y) position point is in relation to.;

Mode 1 uses "patch-relative coordinates", where (0, 0) is the top left corner of the patch area where the object is.;

Mode 2 uses "front-most patch-relative coordinates", where (0, 0) is the top left corner of the front patch - try by selectring the parent patch for example.;

- sets current position to (0, 0) of Pd's coordinate system, f 61;

[mousestate] reports click status, cursor position coordinates and cursor delta. The click report is always given (and sampled every 50 ms), the rest needs to be polled.;

sets mode, which defines the coordinate (0, 0) point in relation to (0: screen, 1: patch window, 2: front most window), f 62;

Plugdata users or those with ELSE can also use [else/mouse] as an alternative, f 42;


## `mstosamps~`

[mstosamps~] takes time in milliseconds and converts to a corresponding number of samples (depending on sample rate).;

It works with floats and signals. A signal input will convert only to the signal outlet, but a float input converts to both float and signal outlets. When a signal input is present, the float input is ignored.;

Plugdata users or those with ELSE can also use [else/samps2ms~] and else/samps2ms] as alternatives., f 33;


## `mtr`

[mtr] records any messages in different tracks and plays them back. Each track records what comes into its inlet and plays it back through the outlet directly below., f 63;

in left inlet: sets a delay value in ms for all tracks to start playing. In other inlets: sets a delay time to that track only, f 77;

in left inlet: opens a previously saved file with the symbol name (or opens a dialog box if no symbol is given). In other inlets: opens a file containing only the track that corresponds to the inlet, f 77;

in left inlet: clears all tracks. If followed track numbers, clears those track(s). In other inlets: clears corresponding track, f 77;

in left inlet: waits a given time in ms after a play message is received before playing back. Unlike delay, first does not alter the delta time value of the first event in a track, it just waits a certain time (in addition to the first delta time) before playing back from the beginning. In other inlets: waits only corresponding track, f 77;

in left inlet: mutes all tracks while still playing. If followed by track numbers, it mutes those track(s). In other inlets: mutes corresponding track, f 77;

in left inlet: causes each track to output only the next message in its recorded sequence (the track number and the delta time of each message being output are sent out the leftmost outlet as a list). If followed track numbers, outputs the next message stored in those tracks. In other inlets: outputs the next message stored on corresponding track, f 77;

in left inlet: plays recorded tracks out the corresponding outlets in the same rhythm/speed as recorded. If followed by track numbers, it plays those tracks. In other inlets: plays corresponding track, f 77;

in left inlet: begins recording all messages received in the other inlets. If followed by track numbers, it begins recording those tracks. In other inlets: begins recording corresponding track, f 77;

in left inlet: goes to start of recorded sequence. Can be used when using the 'next' message. If [mtr] is playing or recording, a stop message should precede it. If followed by track numbers, it rewinds those tracks. In other inlets: rewinds corresponding track, f 77;

in left inlet: stops all recording/playing tracks. If followed by track numbers, it stops those tracks. In other inlets: stops corresponding track, f 77;

in left inlet: Unmutesd all muted tracks. If followed by track numbers, it unmutes those tracks. In other inlets: unmute corresponding track, f 77;

in left inlet: saves a file with the symbol name (or opens a dialog box if no symbol is given). In other inlets: saves corresponding track, f 77;

There are many messages from MAX 7 not yet implemented, like: addevent, cleareventat, deleteeventat, playat, playatms, touch, touchenable, touchdisable and definelengthandstop. These or some of these may get into the next releases but other messages won't make it, like: dictionary, dump and info/bang, because it deals with dictionary stuff that cyclone misses, writejson, because no json please, no, and timescale because it is stupid as MAX recognizes., f 63;

See also attributes in the parent patch for more possible messages., f 68;

- track number & duration (when receiving the "next" message), f 61;

sets multiplier to the speed of all tracks, which allows adjust globally on top of individual track speeds. This only works as a message on the left inlet., f 82;

When set to 1, recorded data for all tracks is saved with the patch. Note that recording, changing, or clearing data does not cause the patch to be dirtied., f 82;

sets speed for all tracks (1 is originally speed, 2 twice as fast, etc). Same if set as a message to the left inlet but in other inlets set individual track speeds, f 82;

Turns looping on (1) or off (0) for all tracks. Same if set as a message to the left inlet but in other inlets set individual track looping., f 82;

Cyclone won't implement attribute related to "transport" stuff, like: tramsport, sync, bindto, autostart, autostarttime and quantize. There are other attributes that maybe can get into the next releases, they are: length, selection, mode and nextmode., f 69;

Plugdata users or those with ELSE can also use [else/rec] as an alternative, f 39;


## `next`

[next] sends a bang to the left outlet when an incoming message is not part of the same "logival event" as the previous message, and a bang out its right outlet otherwise. An "event" is a single message, a mouse click, key press, MIDI event.;

[next] checks if a message is part of the same logical event as the previous one.;

For example, if you click on a bang twice, or if you have a bang going through a delay (as in the parent patch), the two bangs are not part of the same logical event.;

But if you send it a bang also connected other bangs, or use the uzi object to send bangs in a row, these bangs are part of the same logical event.;

Thus, [next] is useful for doing something once per object message dump, be it via a message or a dump from an object such as [uzi] or [coll].;


## `notequals~`

[notequals~] or [!=~] outputs a 1 signal when the left input is not-equal to the right input or argument and a 0 when it is equal to the right input or argument.;

Plugdata users or those with ELSE can also use [else/op~] as a better alternative., f 28;


## `number~`

If the DSP is off, you may be able to change numbers while in the signal monitor mode, but this doesn't do anything. You should only set numbers in the interface when in the "signal generator" mode anyway...;

You cannot use [number~] to monitor a signal and pass it through! The generated signal has nothing to do with the monitored signal and vice-versa. Just use it for one function or the other., f 60;

Below, we use [number~] to generate a signal, send the value though a mathematical operation and then display the result.;

Change the ramp time and see how it generates a ramp line (as in the [line~] object) that takes that amount of time to reach the target.;

A bang message switches between the modes. The 'interval' message sets the time interval in ms that [number~] displays values (default is 100)., f 39;

The 'set' message sets a number but doesn't generate the signal. A list sets a value and a ramp time. The 'ft1' message sets ramp time., f 35;

The 'min' and 'max' message sets the minimum and maximum possible values., f 36;

The 'bgcolor' and 'textcolor' messages set, respectively, background and foreground colors in RGB., f 29;

The "tilde" symbol refers to monitor mode, and if you click on it, it changes to generator mode (marked with a down arrow, where you can click/drag and enter numbers). Clicking on the arrow switches it to monitor mode., f 69;

@monitormode <float>: nonzero sets monitor mode (default 1), f 61;

@interval <float>: display time interval in ms(default 0), f 58;

Use [number~] to monitor or generate signals. This is an abstraction with limited functionality, not a proper clone. If you want a proper and decent GUI object, may I suggest you [else/numbox~] instead!, f 69;

just use [sig~] and [cyclone/snapshot~] or [else/numbox~], f 20;


## `offer`

[offer] stores a x/y integer number pair and accesses the 'y' value from the corresponding 'x' (after retrieving, the pair is deleted)., f 69;

- 'x' value: outputs the corresponding 'y' value and deletes the x/y pair. Sets the 'x' value of a x/y pair if the 'y' value was previously set in the right inlet.;


## `onebang`

a non-0 value allows the first bang on left inlet through, f 60;

[onebang] allows a bang in the left inlet to pass through the left outlet once ONLY if a bang has been previously received in the right inlet. The bang goes to the right outlet otherwise.;

Detect the first time that middle C is played, but ignore subsequent occurrences until reset occurs., f 35;

Plugdata users or those with ELSE can also use [else/nmess] as an alternative, f 39;


## `onepole~`

This filter is very efficient and useful for gently rolling off harsh high end and for smoothing out control signals.;

Similar to Pd vanilla's [lop~], [onepole~] implements the simplest of IIR filters, providing a 6dB per octave attenuation.;

[onepole~] has three different modes (set by messages or argument) for mapping input values onto cutoff frequency. These are mainly for convenience, but they may also slightly improve efficiency.;

- The 'hz' mode is simply an input in hertz, as in our main example in the parent patch.;

- The 'radians' mode lets you set the center frequency of the equation directly, while the input has the same range as linear (0-1), the output has a curved frequency response that is closer to the exponential pitch scale of the human ear. Compare the difference below.;

But please note that the effective cutoff frequency in hertz is the sample rate frequency divided by 4, or half the Nyquist frequency.;

- The 'linear' mode is just a scaled version of the standard hertz mode with values in the 0-1 range isntead 0 and half the Nyquist.;

Plugdata users or those with ELSE can also use [else/lop2~] as an alternative, f 39;


## `overdrive~`

[overdrive~] simulates the "soft clipping" of and overdriven tube-based circuit by applying a non-linear transfer function to the incoming signal. If the "drive factor" is 1, the signal is unchanged. Increasing the "drive" increases the amount of distortion. If the "drive" is less than 1, then it causes a different kind of distortion. If the "drive" is less than 0, VERY LOUD distortion can result, so be careful (here we use [clip~])!, f 71;

Plugdata users or those with ELSE can also use [else/drive~] as an alternative, f 40;


## `pak`

[pak] (pronounced "pock") is much like pack, but any inlet triggers the output of a list. The message set avoid the output and a bang triggers the output.;

elements create corresponding inlets and set their type: 'f' sets to float (initially 0), 'i' sets to int (initially 0), any other symbol sets to symbol type with (initially to that symbol). A float sets to float (initially to that float) - default is two ints set to '0';

the elements of a message update the inlet's value they're connected to and the subsequent inlets according to the remaining elements - it doesn't force an output;

Plugdata users or those with ELSE can also use [else/pack2] as an alternative, f 40;


## `past`

clears last input, so a new input may trigger if >= the threshold, f 33;

The numbers of an input list can be compared to a list of thresholds set via arguments or a "set" message, but only if they have the same length.;

A bang is output if all elements in the list are greater than (or 'past') the corresponding thresholds. If any of the input values fall bacl equal to or below a corresponding threshold, another bang may be output again when the values are greater.;

[past] bangs when an input is greater than a threshold value and the last value was below or equal to it. The input needs to fall back to a value equal or below the threshold for another bang to be output when it goes past it again.;

Plugdata users or those with ELSE can also use [else/above] as an alternative, f 40;


## `peak`

[peak] compares the input to a 'peak' (maximum) value. If it's greater, the input becomes the new peak and is sent out. The middle outlet sends 1 when a new peak is set and 0 otherwise. The right outlet sends 1 when the input is not greater than the peak and 0 otherwise., f 72;

[peak] can take a list of two values as an input. In this case, the 2nd value is set as a new peak value and output. Then, the first value is input. Check the examples below:;

20 is set as a new peak and is output, then 30 is sent to the object and comes out because it's greater than the current peak and becomes the new peak value.;

70 is set as a new peak and is output, then 60 is sent to the object but doesn't come out as it is smaller than the current peak.;

Note: In Pd, [cyclone/peak] only deals with floats, not ints., f 62;


## `peakamp~`

Use the [peakamp~] object to report the absolute value of the peak amplitude of a signal since the last time it was reported. It outputs the peak amplitude when banged or via its own internal clock.;

- sets the internal clock, the interval in milliseconds to output the peak amplitude. If it is 0 (default), the clock isn't used and it only outputs when receiving a bang.;

Plugdata users or those with ELSE can also use [else/peak~] as an alternative, f 40;


## `peek~`

Please check the [buffer~] object for multichannel buffers =>, f 61;

Internally, it creates buffers with the above mentioned naming convention.;

The name convention for multi channel arrays is the table name preceded by the channel number (starting from zero) and "-", such as: "0-", "1-", "2-", "3-", and so on...;

The [peek~] object also works with multi channel arrays (maximum 64). In this example we have 4 channels, which can be accessed as an argument or a float input into the right inlet. No argument loads the first channel by default.;

index to read from table, or index to write to table if a value was previously sent to the middle inlet, f 54;

[peek~] reads (without interpolation) and writes values to an array via messages. Thus, not a proper signal object as it can't handle signals and works even when the DSP is off!;

Plugdata users or those with ELSE can also use [else/tabreader] as an alternative., f 34;


## `phaseshift~`

APF; - b1 = 2*cos(w) / b0; - b2 = (alphaQ - 1) / b0; - a0 = (1 - alphaQ) / b0; - a1 = -2*cos(w) / b0; - a2 = 1; - b0 = 1 + alphaQ; - alphaQ = sin(w) / (2*Q);

In this example, we add the phase shifted signal to the original, which cancels frequencies by phase opposition., f 79;

[phaseshift~] is a 2nd allpass filter, which keeps the gain and only alters the phase from 0 (at 0 hz) to 360Âº (at the Nyquist frequency). The frequency at which it shifts to 180Âº is specified as the filter's frequency (minimum 1o hz) and the steepness of the curve is determined by the Q parameter - see graph below., f 79;

Plugdata users or those with ELSE can also use [allpass.2nd~] as an alternative., f 42;


## `phasewrap~`

A signal of increasing or decreasing value outputs a sawtooth like waveform with -Ï and Ï as lower and upper values.;

Use [phasewrap~] ro wrap the input between Ï (pi) and -Ï (-pi) - useful for wrapping phase values. When the input exceeds Ï (around 3.14159), the output signal value is "wrapped" to a range whose lower bound is -Ï (around -3.14159)., f 54;

Plugdata users or those with ELSE can also use [else/wrap~2~] as an alternative, f 42;


## `pink~`

[pink~] generates pink noise. This is not an actual MAX clone but an object that is borrowed from ELSE which has more functionalities and is backwards compatible to MAX's object since the original just outputs pink noise!, f 75;

Pseudo random number generators aren't true random number generators. Instead, an algorithm is used to provide a sequence of numbers that seems random. The same sequence can be reproduced if you set a "seed" value, which can be any integer number., f 52;

You can also set a seed with the argument. If you don't supply it, each object gets its own seed internal seed. If you send a 'seed' message without float, the object also gets a unique seed value., f 52;

Seeds are kept locally, which means that if two [pink~] objects are seeded the same they will have the same output. Conversely, you can seed the same [pink~] object twice with the same seed to repeat the output., f 52;

White noise has constant spectral power, but pink noise has constant power per octave and it decrease 3dB per octave., f 75;

You can set the number of frequency bands in octaves. A value of 1 makes it a single band which is plain white noise. For each extra octave, the bandwidth is split in half and the new octaves are 3dB lower than the next lower octave., f 68;

The maximum number of octaves is 40 and the default depends on the sample rate, and it is so that the lowest octave starts close to 20hz. For a sample rate of 44100 this gives us 12 octaves. The more octaves you have, the less bright the overall sound is., f 68;

You can set the number of octaves with the 2nd argument or a float input.;

seed <float> - a float sets seed, no float sets a unique internal, f 65;

Plugdata users can just use the original object from ELSE instead (same with those with ELSE)., f 33;


## `play~`

Multi channel playback is possible (up to 64 channels) when you specify it with a second argument. The number of channels defines the number 'n' of outlets - where the first outlets are the channel inputs and the righmost is the bang outlet.;

If more than one channel is set, the name convention for multi channel arrays is the table name preceded by the channel number (starting from zero) and "-", such as: "0-", "1-", "2-", "3-", and so on...;

You can manually set multi channel arrays in Pd like that or use the [buffer~] object, which does this internally.;

If the [buffer~] being played has fewer channels than the number of output channels in [play~], the extra channels output a zero signal.;

Inconsistency: In Max, if [buffer~] has more channels than [play~], the channels are mixed. This could be implemented in cyclone if the [buffer~] object ever becomes a compiled object.;

- non zero plays the array in original speed, <0> stops it, f 60;

A signal input can be used as the position in ms to read into the array. You can use any signal such as from a [line~] object or a LFO. A signal offers the ability to read the array at a varying speed as the example below.;

'non zero' plays the array in original speed, <0> 'stops' it, f 30;

same as 'zero': stops playing and outputs 0 (cannot be resumed), f 33;

Start message with arguments: 'start' takes 3 floats that specify: 1) starting point in the array (in ms), 2) end point (in ms) and 3) duration (in ms). You can then select different portions of the array and set also a different duration to read a sample with transposition (and interpolation)., f 62;

Default values are: 0, array length in ms, original duration., f 62;

- loop: a non-zero enables looping at any given portion of the array, 0 disables it (default is disabled), f 62;

- loopinterp: a non-zero enables crossfading when looping, 0 disables it (default is disabled). This prevents clicks at looping points, the fade in happens in the start point of the loop and the fade out after the end point of the loop., f 62;

- interptime: the crossfade time in ms when loop and loopinterp are enable (default is 50 ms), larger times introduce other effects besides preventing clicks., f 62;

[play~] plays any part of an array, it can play at different speeds (with interpolation) and backwards. It may also loop with optional crossfading. The interpolation is the same as [tabread4~]'s.;

sets <beginning, end, duration> in ms and starts playing, default values are the whole array in original speed, f 58;

Plugdata users or those with ELSE can also use [else/tabplayer~] or the more convenient [else/player~] as alternatives, f 44;


## `plusequals~`

- signal value is accumulated. Accumulated value is output only if a signal is connected;

[plusequals~] or [+=~] accumulates the received values. Each input sample is added to the previous ones for a running sum. So, started at 0, a signal consisting of 1 values outputs the sequence (1, 2, 3, 4, etc...).;

The internal sum can be reset to 0 with a bang (left inlet) or a signal different than 0 in the right inlet (with sample accuracy) - or also set to any value (with the set message).;

Plugdata users or those with ELSE can also use [else/add~] as an alternative, f 42;


## `poke~`

You can use control messages isntead of signals. In this way, [poke~] behaves similarly to the [peek~] object. Note, however, that the left two inlets are reversed on [poke~] when compared to [peek~].;

The name convention for multi channel arrays is the table name preceded by the channel number (starting from zero) and "-", such as: "0-", "1-", "2-", "3-", and so on...;

The [poke~] object also works with multi channel arrays (maximum 64). In this example we have 4 channels, which can be accessed as an argument or a float input into the right inlet. No argument loads the first channel by default., f 60;

Please check the [buffer~] object for multichannel buffers =>, f 61;

Internally, it creates buffers with the above mentioned naming convention.;

[poke~] writes signals to an array at indexes specified by a signal.;

index to record to (if negative or larger than the buffer, no data is written), f 54;

Plugdata users or those with ELSE can also use [else/tabwriter~~] as an alternative, f 42;


## `poltocar`

[poltocar] converts polar coordinates (amplitude / phase) to cartesian coordinates (real / imaginary).;

Plugdata users or those with ELSE can also use [else/pol2car] as an alternative, f 33;


## `poltocar~`

Use the [cartopol~] object to convert signal values representing cartesian coordinates to a signal composed of polar coordinates - useful for spectral processing.;

[poltocar~] is useful for spectral processing in the more intuitive polar form (with amplitude and phase values). This is because when performing spectral analysis in Pd, the signal is in the cartesian form, so we need [cartopol~] and [poltocar~] to convert to and from the polar form in order to perform the FFT and iFFT. Here's the general idea:;

Plugdata users or those with ELSE can also use [else/pol2car~] as an alternative, f 33;


## `pong`

Use [pong] to fold, wrap or clip its input within a given low-high range., f 38;

maximum range is always the highest value & minimum range is always the lowest value. Wrap mode is useful for modulo arithmetic.;

Plugdata users or those with ELSE can also use [else/fold] and [else/wrap2] as alternatives, f 33;


## `pong~`

Use [pong~] to fold, wrap or clip its input signal within a given low-high range. Wrap mode is useful for modulo arithmetic., f 65;

Plugdata users or those with ELSE can also use [else/fold~] and [else/wrap2~] as alternatives, f 33;


## `pow~`

[cyclone/pow~] has the inlets'functionality reversed in comparison to pd vanilla's [pow~], other than that, it's quite the same!;

[cyclone/pow~] raises the base value (set in the right inlet) to the power of the exponent (set in the left inlet). Either inlet can receive a signal or float.;

[cyclone/pow~] can be useful for generating curves from [line~] as in the example below to the right.;

And still create the vanilla object from vanilla without namespaces as:;

Pd also has a vanilla object named [pow~]. Cyclone avoids name clashing and overwriting an internal in Pd Vanilla, but for that you need to use the cyclone namespace ("cyclone/" before the object name), as it's the common practice for cyclone's documentation. So you create it as:;

Other ways to load [pow~] is with a capital letter, either with or without 'cyclone/' such as:;


## `prepend`

[prepend] will add messages set as argument to the beginning of any message sent to the input. This is a rather redundanct object object, and quite similar to Vanilla's [list prepend]., f 65;

Plugdata users or those with ELSE can also use [else/insert] as an alternative, f 33;


## `prob`

[prob] outputs a weighted series of random numbers (1st order markov chain). It accepts lists of 3 numbers where the 3rd represents the weight/chance of going from value 1 to value 2, a bang will force [prob] to output. See below:;

When it receives a bang, [prob] makes a random jump from its current state to another state based on its current weighting of transitions. If a transition can be made, the new state is sent out the left outlet. If not, a bang is sent out the right outlet., f 62;

The matrix below just goes from 0 to 3 and has no rule for when it reaches 3, so it gets stuck. You can use the "reset" message to set a value for whenever [prob] gets stuck.;

* embed <1> will set the [prob] object to store the probability matrix table within the patch when the patch is saved, so the next time you open the patch it already has that table initialized - embed <0> (the default) disables it.;

For any state, the weights of all possible transition states are summed, and the probability percentage is the weight value divided by that sum x 100 So, if you have the messages "0 1 80" and "0 2 20", the sum is 100 and the percentage is 80% and 20%., f 62;

Below, we have the weights 3 4 and 1, the sum is 8 and the first weight (3) represents a 37.5% chance, the second (4) represents 50% and the third (1) represents 12.5%. Note that any state can make a transition to itself, such as the last list above (0 0 1).;

The [anal] object was designed to feed [prob], check its help file.;

an integer sets (but doesn't output) the current number, the next value depends on the probability matrix., f 56;

Plugdata users or those with ELSE can also use [else/markov] as an alternative, f 40;


## `pv`

The best practice is to initialize the message of only of the related [pv] objects, because another [pv] object with also another initialized message means that one message will overwrite the other, and you don't have control of which one will be stored.;

And it can be initialized with any message as an argument, but after the symbol that specifies the name of [pv].;

the messages stored and retrieved below are shared with the parent patch and the other subpatch., f 44;

the messages stored and retrieved below are shared only within this subpatch.;

you can also retrieve a variable in a subpatch that was stored in the parent patch. Conversely, the value stored here in the subpatch can be retrieved in the parent patch.;

And since the parent patch also has a [pv] with the same name, the value stored here is also shared with other subpatches.;

But if you have a [pv] with a variable name that is not present in a parent patch, the stored messages will only be shared within this subpatch, even if other subpatches have [pv] objects with the same variable name - to check it, open the [pd pv_in_a_subpatch_2] subpatch in the parent patch.;

[pv] is similar to pd's [value], but stores any message as a variable name, which can be shared within a patch or its subpatch if it has another [pv] object with the same variable name. It won't share with other patches!, f 76;

In Max, you cannot create [pv], [send] and [value] objects with the same name. In Pd, you can create [send] and [value] objects and they will communicate to each other.;

Cyclone allows you to create a [pv] object with the same name used in a [send]/[value] object, but note that [pv] name variables are completely independent and do not communicate to pd vanilla's [send] or [value] objects.;

Therefore, you can have both [pv] and [value] with the same name in the same patch that they do not affect each other! In practice they are completely different variables!;

posts information in the Pd window about related [pv] objects in the patch, f 57;

NOTE: This is a rather redundanct object that could arguably just be deprecated., f 23;


## `rampsmooth~`

[rampsmooth~] smooths a signal across 'n' samples. Each time an incoming value changes, it begins a linear ramp of the given 'n' samples to reach this value. It is also useful for envelope following and lowpass filtering., f 72;

Plugdata users or those with ELSE can also use [else/glide2~] as an alternative, f 42;


## `rand~`

you can use [rand~] at a low frequency to generate random ramps up and down to control several parameters. Below, it generates random glissandi.;

[rand~] generates random values between -1 and 1 at a given frequency, interpolating linearly between the generated values. The resulting sound is a bandlimited noise.;

Plugdata users or those with ELSE can also use [else/rampnoise~] as an alternative., f 33;


## `rdiv`

[rdiv] or [!/] divides a number by the incoming value on the left inlet. Functions like the [/] object, but the inlets' functions are reversed.;


## `rdiv~`

[rdiv~] or [!/~] divides a number by the incoming value on the left inlet. Functions like the [/~] object, but the inlets' functions are reversed.;


## `record~`

If more than one channel is set, the name convention for multi channel arrays is the table name preceded by the channel number (starting from zero) and "-", such as: "0-", "1-", "2-", "3-", and so on...;

You can manually set multi channel arrays in Pd like that or use the [buffer~] object, which does this internally.;

Multi channel recording is possible (up to 64 channels) when you specify it with a second argument. The number of channels defines the number 'n' of inlets - where the first outlets are the channel inputs and the two righmost are the range intlets.;

Append, loop, loopstart and loopend can be indicated as attributes/messages.;

sync output: signal from 0 (at start point) to 1 (at end point). When not recording, a zero signal is output;

non-zero enables loop (keep recording at start point when reaching the end), 0 disables it (default), f 56;

non-zero enables append (records from where was last stopped), 0 disables it (default), f 56;

resets loop points to default values (0 to whole array) and restarts recording if recording is on, f 56;

[record~] records up to 64 signal channels into arrays. By default, recording stops when the array is filled., f 68;

Plugdata users or those with ELSE can also use [else/tabwriter~] as an alternative, f 42;


## `reson~`

[reson~] is a bandpass resonant filter. All parameters can be set as float or signals.;

Since it is a recursive filter, you may need to use the "clear" message if it blows up.;

The equation of the filter is: y[n] = a0 * (x[n] - r * x[n-2]) + b1 * y[n-1] + b2 * y[n-2] - where r, b1, and b2 are calculated from 'Q' and center frequency.;

Plugdata users or those with ELSE can also use [else/bandpass~] an alternative, f 33;


## `rminus`

[rminus] or [!-] is like the [-] object, but the inlets' functions are reversed.;


## `rminus~`

[rminus~] or [!-~] is like the [-~] object, but the inlets' functions are reversed.;


## `round`

- value to round to (whose multiple values will be approximated to);

It works in two modes, rounding to the nearest multiple (default) or to the approximating to the truncated multiple value., f 76;

- "nearest" followed by 0 sets to "truncate mode", non zero number sets to "round to nearest mode" (default);

[round] approximates positive and negative numbers to an integer multiple of any given number that is greater or equal to 0 (0 makes no approximation, so the original input is output unchanged)., f 76;

Plugdata users or those with ELSE can also use [else/quantizer] as an alternative., f 33;


## `round~`

- value to round to (whose multiple values will be approximated to);

It works in two modes, rounding to the nearest multiple (default) or to the approximating to the truncated multiple value., f 68;

[round~] approximates positive and negative numbers to an integer multiple of any given number that is greater or equal to 0 (0 makes no approximation - so the original input is output unchanged)., f 68;

- "nearest" followed by 0 sets to "truncate mode", non zero number sets to "round to nearest mode" (default);

Plugdata users or those with ELSE can also use [else/quantizer~] as an alternative., f 33;


## `sah~`

Sample and hold random values from a noise input, rescaled to 500 - 1100 Hz range:;

When a trigger signal raises above a given threshold, [sah~] captures a value ("samples") from the input and continually outputs it ("hold") until the trigger signal rises again above the threshold after having dropped below it. This usually synchronizes one signal to the behavior of another.;

Here we're passing the signal of a [phasor~] (a periodic ramp from 0-1) through the [sah~] object. The trigger signal is from the [train~] object, which goes from 0 to 1 at a period given in ms, and from 1 to 0 at half this period. When [train~] goes from 0 to 1, it triggers the [sah~] object., f 67;

When the period of the [phasor~] and [train~] are out of synchrony, you may get interesting arpeggio effects. You can try other waveforms for the input to the [sah~]., f 67;

The [samphold~] object in Pd vanilla was designed to work with [phasor~]. Conversely, [sah~] doesn't work well with [phasor~] and works better synchronizing with a signal like a square wave, or an impulse for example.;

Plugdata users or those with ELSE can also use [else/sh~] as a better alternative., f 42;


## `sampstoms~`

Use the [sampstoms~] object to convert a time value in samples to milliseconds (depending on the sample rate)., f 67;

[sampstoms~] works with floats and signal. A signal input converts only to the signal outlet, but a float input converts to both float and signal output. When a signal input is present, the float input is ignored., f 67;

Plugdata users or those with ELSE can also use [else/ms2samps~] and else/ms2samps] as alternatives., f 33;


## `scale`

Originally in Max/MSP, "classic mode" is buggy as hell and cycling 74 is aware. We have a reasonably good version, but you shouldn't really bother to use it, just saying...;

If the input value is outside the input range, [scale] will not clip the values to the output range but keep scaling outside that boundary with the same conversion parameters.;

The scaling can be inverted by reversing one of the ranges (input or output);

[scale] maps an input range to an output range. Values larger or smaller than the input range will not be clipped to the output range. The mapping can be inverted and/or exponential., f 81;

Fifth argument or sixth inlet specifies the exponential factor. In modern mode (default), exponential values must be greater than 0, where 1 also gives you linear scaling (no exponential). It's like raising to the power of the given exponential, try it below (with values from 0.1 to 10).;

You can set the exponential mode with the @classic attribute, "@classic 1" is classic mode and "@classic 0" is "modern mode".;

The [scale] first appeared in Max 4.2 and had a "classic" exponential, using a function compatible with old IRCAM patchers. This is very buggy in Max and we encourage not to use it. A new "modern" mode (from Max 6.0) was introduced to [scale], but it still has the "classic" mode by default.;

The [scale~] object (also introduced in Max 6.0), has the modern mode by default. This is an inconsistency that looks like a bug. But we didn't want cyclone's versions of [scale] and [scale~] to be inconsistent between then. And since classic mode is buggy, we've made modern mode as the default.;

For the classic mode, the exponential must be greater than "1". A value of "1" gives you a linear mapping (no exponential). Values greater than one gives you an exponential curve, with larger values leading to steeper exponential curves. A typical value for this mode is "1.06". Below we have classic mode with expnential values from "1" (linear) to "1.2".;

BEWARE: let's state it clear again, "classic mode" in Max/MSP is buggy as hell (and cycling 74 is aware of it). We have a reasonably good version, but you shouldn't really bother to use it, just saying...;

In Max, modern mode had the exponent inverted in relation to current max and cyclone prior to Max 6.0.4! Thus, with an exponent of 2, the object behaved like it had an exponent of 0.5 (and vice versa). Max/MSP patches from versions prior to 6.0.4 may require updating to work properly in modern mode. But since this is the first version of this object in cyclone, it doesn't have backwards compatibility issues in Pd!;

Plugdata users or those with ELSE can also use the much simpler and more powerful [else/rescale] as an alternative., f 42;


## `scale~`

Originally in Max/MSP, "classic mode" is buggy as hell and cycling 74 is aware. We have a reasonably good version, but you shouldn't really bother to use it, just saying...;

If the input value is outside the input range, [scale] will not clip the values to the output range but keep scaling outside that boundary with the same conversion parameters.;

The scaling can be inverted by reversing one of the ranges (input or output);

[scale~] maps an input range to an output range. Values larger or smaller than the input range will not be clipped to the output range. The mapping can be inverted and/or exponential.;

Fifth argument or sixth inlet specifies the exponential factor. In modern mode (default), exponential values must be greater than 0, where 1 also gives you linear scaling (no exponential). It's like raising to the power of the given exponential, try it below (with values from 0.1 to 10).;

You can set the exponential mode with the @classic attribute, "@classic 1" is classic mode and "@classic 0" is "modern mode".;

For the classic mode, the exponential must be greater than "1". A value of "1" gives you a linear mapping (no exponential). Values greater than one gives you an exponential curve, with larger values leading to steeper exponential curves. A typical value for this mode is "1.06". Below we have classic mode with expnential values from "1" (linear) to "1.2".;

BEWARE: let's state it clear again, "classic mode" in Max/MSP is buggy as hell (and cycling 74 is aware of it). We have a reasonably good version, but you shouldn't really bother to use it, just saying...;

The [scale~] object first appeared in Max 6, but it's control counterpart ([scale]) was there since Max 4.2!;

In Max, modern mode had the exponent inverted in relation to current Max and cyclone prior to Max 6.0.4! Thus, with an exponent of 2, the object behaved like it had an exponent of 0.5 (and vice versa). Max/MSP patches from versions prior to 6.0.4 may require updating to work properly in modern mode. But since this is the first version of this object in cyclone, it doesn't have backwards compatibility issues in Pd!;

In Max, even though [scale] has classic by default, [scale~] has a modern exponential mode by default, but also offers a classic mode, using a function compatible with old IRCAM patchers like [scale]. This is very buggy in Max and we encourage not to use it. To avoid inconsistencies, we've made both [scale] and [scale~] have a modern mode by default.;

Plugdata users or those with ELSE can also use the much simpler and more powerful [else/rescale~] as an alternative., f 42;


## `scope~`

When in X-Y mode, [scope~] plots points whose horizontal axis (X) corresponds to the signal's values coming into the left inlet and whose vertical axis (Y) corresponds to the signal's values coming into the right inlet. If the two signals are identical and in phase, a straight line increasing from left to right will be seen. If the two signals are identical and 180 degrees out of phase, a straight line decreasing from left to right will be seen. Other combinations may produce circles, ellipses, and Lissajous figures., f 47;

When in X-Y mode, there's an averaging algorithm for the calccount parameter, where a representative sample from this period is used. So it requires small values for a better representation (only 2 in the examples below)., f 47;

If signals are connected to both the left and right inlets, [scope~] operates in X-Y mode., f 47;

Change the phase of the oscillator to check how it affects the plot, then try different frequencies., f 47;

If a signal is only fed to the second inlet, [scope~] displays in "Y Mode" only., f 31;

The "drawstyle 1" message or attribute changes [scope~] to analternate drawing style, that affects some kinds of signals, such as this bandlimited square wave (try it with the range -1.2 1.2).;

You can set the vertical (signal amplitude) range and the onset delay (time between displays) with messages.;

There's a "dim" message/attribute, not available in the original MAX object, for setting the size of your [scope~]., f 39;

And as noted, if you right click on it (in edit mode or not) you can access its properties., f 50;

When you click on [scope~] with your mouse, the display freezes for as long as you hold the mouse button down.;

When in edit mode, you can resize the object by clicking and dragging on its bottom right corner., f 51;

[scope~] displays a signal in the style of an oscilloscope., f 29;

@fgcolor <f f f> | @bgcolor <f f f> | @gridcolor <f f f> | @range <f f> | @trigger <f> | @triglevel <f> | @bufsize <f> @calccount <f> | @delay <f> | drawstyle <f> | @dim <f f> | @receive <sym>, f 74;

You can send any kind of message that scope~ accepts. Note that if you send it a list of two floats. Then the values are spread via both inlets and set samples per line and lines per buffer, respectively., f 36;

When in edit mode, [scope~] shows its inlets. The [scope~] object below has a receive symbol, so you can send messages to it via a [send] object (but not audio). In this case, the inlets are suppressed, so we don't see it. The receive symbol can be set with the receive message or the @receive attribute. If you set a receive name as "empty" then it can't receive messages anymore and the inlets are shown., f 73;

The default mode is "trigger 0", which is "none mode", where the signal is displayed the way it is., f 43;

"trigger 1" is "up mode", in which - following the delay period - a new display is triggered only when the signal goes from below the trigger level to being equal to it or above it., f 43;

"trigger 2" sets to down mode, in which - following the delay period - a new display is shown only when the signal goes from above the trigger level to being equal to it or below it., f 43;

The "triglevel <float>" message sets the threshold for the trigger modes "1" (up) and "2" (down). In these cases, as described above, the waveform must increase or decrease past this value to trigger a new display. If you are displaying a periodic waveform, some changes to the trigger level will shift the waveform to the left or right., f 43;

The delay determines when to display a new waveform. In conjunction to it, the trigger mode determines when a new waveform trace begins (following the delay period)., f 43;

Therefore, the number of samples (or period) displayed in the oscilloscope is equal to: bufsize * calccount. The number of samples also affect the time between displays. If the number of samples is small, the refresh rate speed is high, so you may want to use the "onset delay" message to decrease the speed between displays.;

bufsize & calccount are similar, but they have different effects. Lets check the example in this subpatch with two settings. Both have the same display period in samples (2560), but one is displayed as a buffer made of 10 lines and 256 samples per line and the other as a buffer made of 256 lines and 10 samples per line.;

"bufsize" sets the number of lines in the display (possible values from 8 to 256 - default is 128). The number of samples represented by each line is set by "calccount" (possible values from 2 to 8192 - default is 256). For each line, the maximum and minimum values within the period in samples are used to generate the line. So the smallest line is 2 samples/points long.;

Old color messages for front / signal and background are, respectively, frgb and brgb - they are RGB with values from 0-255., f 52;

These are still included in Max and Pd for backwards compatibility. You can also set them as attributes (@frgb and @brgb). Check the messages below, f 52;

RGB colors (values from 0-1) for fgcolor (front/signal), bgcolor (background) & grid (gridcolor). In Max, these are RGBA, but the alpha channel is not implemented in Pd.;

Note that Plugdata users actually get a similar alternative from ELSE with the same name instead that is not 100% compatible., f 64;


## `selector~`

You can set the inlet number with a signal input, this allows [selector~] to be controlle with sample accuracy. Signal values are truncated to integers., f 51;

[selector~] selects one input signal from the 'n' specified inlets or none of them to an outlet. If no input is selected, it outputs zero values.;

inlet number to select - values are truncated to integers and clipped from 0 to number of channels, f 49;

Plugdata users or those with ELSE can use the much better [else/xselect~] or [else/xselect2~] objects instead (see also their multichannel variations)., f 38;


## `seq`

[seq] plays/records raw MIDI streams and can save/read MIDI sequence files. All tracks of a multi-track midi file are merged into one.;

Note that the 'start' message can only set the speed once (at the start of the sequence) - because every time we send the start message, it starts playing from the start! Thus, a bang or a 'start' message can also be used to 'restart' the sequence., f 37;

The 'start' message starts reading the loaded sequence and also allows you to control the playback speed set by the float after the 'start' message - the normal speed is set as 'start 1024', so 'start 512' is half the tempo (reads two times slower), 'start 2048' is twice the tempo (two times faster) and so on. If you send it just "start", it plays at the original speed (so it's the same as the bang message or 'start 1024')., f 37;

When you send it "start -1", it expects 'tick' messages as the clock, so you can use it to vary the playback tempo or to synchronize with another clock (such as incoming MIDI Clock messages). 24 clock ticks is a quarter note, you can convert BPM to time per clock tick as to the right., f 37;

The [seq] object in cyclone has two extra messages that the original does not have: pause and continue. It also misses the 'dump' message from the original MAX version, which is something that doesn't seem to be really useful in MAX., f 56;

Moreover, the [seq] object in cyclone can be clicked to open an edit window, while nothing like this is present in the MAX original. Nonetheless, this can be seen as a substitute for the purpose that the 'dump' message serves., f 56;

Since Max 7.3.2, there's support for MIDI Type 1 and you can save midi files in this format with separate tracks if you give a non zero argument to the 'write' message. Cyclone hasn't been updated to do this so it has the old behaviour from MAX that it always merges all tracks into one and always saves as format 1 as well., f 56;

Besides MIDI files, [seq] can load and save to .txt files, just use this extension isntead. The text file follows a format that is also present in the edit window of the [seq] object that opens when you click on the object (note that this edit window functionality is not present in the original MAX object)., f 67;

0 144 60 112; 1000 144 60 0; 1500 192 31; 1500 144 60 112; 2500 144 60 0;, f 17;

The text format displays the MIDI events in lines separated by semicolons, which consist of a start time in milliseconds (the time elapsed since the beginning of the sequence) followed by the raw bytes of the MIDI message., f 67;

This sequence plays the note middle C on channel 1 (with a velocity of 112) for one second, then half a second later changes to program number 31 and plays middle C again for one second., f 67;

You can edit and close/save changes to the sequence, but you need to write it to a file so it's saved., f 67;

For example, let's check this sequence ==> (also below):, f 42;

start/restart sequence at a given tempo (default '1024' - normal tempo), 'start -1' expects tick messages;

The 'hook' message multiplies all the event times by the given number, so '2' is twice as long and '0.5' is twice as fast. This is cumulative, so you can keep speeding up or slowing it down by sending the same message multiple times., f 79;

The 'print' message prints the first 16 events of the sequence in the Pd Window in the same format as the edit window., f 79;

Cyclone has extra messages: pause and continue do the obvious and only work when playing (not when recording)., f 79;

The delay message sets an onset delay time in ms to the start of the sequence. The addeventdelay message adds (or subtracts) to the onset delay and is cumulative (keeps adding/subtracting if you send the same message multiple times)., f 79;

Below, we play and stop with a toggle. At the end of the file, a bang out the 2nd outlet of [seq] makes it play again in a loop. When you stop it with the toggle, it also flushes possible hanging MIDI notes (with [midiflush]). We use [midiparse] to send note messages to our synth.;

Use 'write' to save to a MIDI file with the dialog box, or use 'write <symbol>' to save to a specific file., f 59;

You can directly record from raw MIDI data with [midiin]. Use the 'record' message to start recodring, you don't need the stop message to switch from recording/playing. Use 'append' to record from the point you stopped recording.;

You can record from [makenote] or specialized MIDI objects such as [notein] using the [midiformat] object to convert the messages to raw MIDI. Please check the help file of [midiparse], [midiformat] and [midiflush], which are useful with [seq]., f 55;

Use the 'read' message to open another file with the dialog box and 'read seq.mid' to re open the example. The 'delay' message adds a delay in ms before sending the first event.;

Plugdata users or those with ELSE can also use [else/midi] as an alternative., f 39;


## `sinh`

- input to hyperbolic sine function, this value is stored and updates the argument;


## `sinh~`

Use [sinh~] to output the hyperbolic sine function of each input sample (probably only useful for mathematical calculations).;


## `sinx~`

Like [cyclone/cosx~] & [cyclone/tanx~], [sinx~] is properly designed for mathematical operations. Thus, it expects an input in radians to calculate the sine of each input sample.;


## `slide~`

[slide~] filters an input signal logarithmically between changes in signal value. The formula is: y(n) = y(n-1) + ((x(n) - y(n-1))/slide)., f 70;

- sets the current output sample value to 0 (the next incoming value will smoothly transition from that 0);

Different than [rampsmooth~], [slide~] smooths audio transitions in a non linear way. It's also useful for envelope following and lowpass filtering., f 70;

Plugdata users or those with ELSE can also use [else/lag2~] as an alternative, f 17;


## `snapshot~`

[cyclone/snapshot~] converts signal samples to float when a bang is received or at a given interval in milliseconds.;

The active attribute can initially set the time report off as an argument. When you set a time interval, the default is that the report is on.;

You can convert one sample from each block, and you can specify which one with the offset message or argument.;

In the example below, we have [count~] generating a signal from 0 to 63 at each block. So it's like each sample is marked with the sample index value.;

The second argument sets the offset, the default is 0 (first sample). In the example below we move the offset to "10", which reflects on the output float that matches the argument.;

Cyclone avoids name clashing and overwriting an internal in Pd Vanilla, so you need to have the cyclone folder properly isntalled in Pd Vanilla's extra folder and create it as:;

So, if you still want the object from vanilla, you even if you created the objects above, you can still isntantiate it as:;

Pd also has a vanilla object named [snapshot~]. Though very similar, they're not compatible.;

Plugdata users or those with ELSE can also use the more powerful [else/sig2float~] as an alternative., f 42;


## `speedlim`

[speedlim] only allows messages through if a given time has elapsed since the previous input/output. Otherwise, it waits until that time passes and then sends the last received message since the previous output (ignoring the others).;

Plugdata users or those with ELSE can also use [else/limit] as an alternative., f 40;


## `spell`

Messages with more than one element will output a space character in between them (value 32). Below we have a minimum output size of 4 (1st argument), but since the input messages only have 3 elements (counting the space), the output is filled with a character value (32 by default).;

A 2nd argument sets the fill character value to other than 32, below we have "46" which corresponds to "." - a dot character.;

Since you can't input a float value, you can use [tosymbol] to convert a float to a symbol and then send it to the [spell] object.;

[spell] takes any message and converts each containing digit and character to UTF-8 (Unicode) values ([spell] doesn't understand non-integer float messages). The 1st argument sets the minimum output size. If the input doesn't "spell" to the minimum, the output is filled with characters (32 space character by default and specified by 2nd argumment)., f 75;


## `spike~`

[spike~] reports intervals of zero to non-zero transitions from the signal input. The refractory period is set at the second inlet, which defines how soon after detecting a transition the spike~ object will report the next instance.;

restarts the countdown of the refractory period from the time at which the bang was received;

interval in ms since last 0 to non-0 transition (including the refractory period, if one is set);

Plugdata users or those with ELSE can also use [else/status~] with as [else/detect~] an alternative., f 33;


## `split`

<in, min, max>, min/max are set first, then input is checked;

[split] splist numbers in a given range from numbers outside it. If an input is in between a min/max value or equal to them, the value is sent to the left outlet, or to the right outlet otherwise. Unlike MAX, it only deals with floats.;

Plugdata users or those with ELSE can also use [else/midi] as an alternative., f 39;


## `spray`

You can set an offset with the 2nd argument or the "offset" message (default is 0). This way, the first outlet is numbered after the offset value. Positive and nagetive values are allowed.;

By default, a list input is split and sprayed to the outlets. The first element in the list is the offset number.;

A non zero value as the third argument changes to the list output mode. In this mode, a list input will be output to the specified outlet. Symbols are accepted in both modes.;

[spray] accepts lists where the 1st value indicates the outlet number (starting at 0) and the 2nd element (float or symbol) is sent to that outlet - when not in list mode, subsequent elements are sent to subsequent outlets to the right, other wise (in list mode) the whole list is output at that outlet.;


## `sprintf`

the optional 'symout' argument formats a symbol message ('symout' itself not included), f 57;

For more details on these types, refer to a standard C library manual. For instance in the link below:, f 52;

The above reference has more information and parameters not really available for [sprintf]. Nonetheless, the length modifiers, the optional flags: "+", " ", "-" and "#", plus the width and precision fields are supported., f 47;

Inconsistencies: If a format type is not supported or invalid, [sprintf] doesn't create a corresponding inlet and prints an error isntead. The Max version creates an inlet for whatever inserted type, invalid or not, and only prints an error when trying to convert. The MAX original also doesn't support the "space" flag or %a/%A types. The length modifiers are supported but since Pd does not have an integer type, something like '%lld' won't work with full precision even if you're using Pd compiled for double precision (aka Pd64). Also, some values for a format like '%u' will only actually be possible to represent in Pd64 because they can exceed the 2Ë24 limit of 32-bit float., f 64;

output message with format types '%' (each changeable argument creates a corresponding inlet). For all possible types and details, see:;

float/symbol to match corresponding given type. Messages with more than one item spraed items to the next inlets.;

Based on C's "printf" function, [sprintf] formats messages, where each '%' format type corresponds to an inlet. By default you have each argument as a separate element in a message, but the 'symout' argument creates a symbol out of everything., f 66;

Plugdata users or those with ELSE can also use [else/format] as an alternative., f 42;

A symbol may be received in any inlet that corresponds to a %s argument. If sent to another inlet type, a conversion error is given in Pd's window.;

If a changeable number argument argument (such as %i or %f) does not receive an input, the default value is "0". If no value has been received for a changeable symbol argument (%s or %c), a blank space is the default., f 64;

for more details on supported specifiers, as most of them are shared between the two objects., f 21;

The arguments in [sprintf] format a message to be sent out and can be floats and symbols with or without changeable arguments (like %i for integers, %f for floats and %s for symbol strings) resembling the C programming language. The number of changeable arguments determines the number of inlets, with each inlet corresponding to a changeable argument, in order., f 64;

Messages with more than one item spreads items to the next inlets., f 23;

The optional 'symout' argument turns the whole output into a symbol message, which is useful for format strings with spaces, commas and other special characters. In this case you should not use backslash, as it is common in Pd to escape a space or another special symbol., f 48;

Nonetheless, note you can use backslashes to create symbols with special characters such as spaces without the 'symout' argument., f 44;

The MAX original has issues in dealing with spaces for symbol input that contains spaces. Similarly, there are also issues with the width field when it adds spaces and the 'space' flag. What happens is that atoms get split by the spaces when you don't have the 'symout' argument. The cyclone version also has the same issues., f 72;

* The correct exact result ('4294967294') is only possible in Pd compiled with double precision (aka Pd64), f 43;


## `substitute`

[substitute] exchanges an element (the first argument) in an input message to another one (second argument).;

[substitute] will replace all recurring elements in a message, but if you have a 3rd argument, it operates in "first only" mode, where only the first element is replaced., f 53;

set followed by 2 items sets the 1st element to be substituted by the 2nd (other elements are ignored);

sets the 1st element to be substituted by the 2nd, other elements are ignored (basically the same as "set");

Plugdata users or those with ELSE can also use [else/replace] as an alternative., f 43;


## `sustain`

[sustain] holds the note off messages while it is on and sends the held note off messages when it's switched off.;

Using the [sustain] object in a 2-voice polyphonic synth with random notes.;

You can directly connect the [notein] object and also access the MIDI message from an actual sustain pedal and feed it to the [sustain] object.;

[sustain] also accepts a list (pitch / velocity) as note messages. and you can also set the sustain parameter with the @sustain attribute or message;

There are three different modes to deal with repeated notes while the sustain pedal is on, set by the 'repeatmode' message or attribute. The options are; - 0 (historical); - 1 (re-trigger); - 2 (stop last);

0 (Historical mode - default): Playing the same note multiple times while the sustain pedal is on will output the Note On messages and hold the Note Off messages for all of them. When the sustain pedal is set off or the flush message is received, all of the held Note Off messages are sent in the order they were received.;

1 ('Re-trigger' mode): Playing a note that had already been played before and whose noteoff is being held will first send the corresponding Note Off before sending the new Note On message (and then hold the next Note Off). In other words, it re-triggers the note.;

2 ('Stop last' mode): Playing the same note multiple times will not re-trigger as in re-trigger mode, but when the sustain is off, only one Note Off message corresponding to a repeated note is sent, isntead of all of them.;

Plugdata users or those with ELSE can also use [else/suspedal] as a better alternative., f 44;


## `svf~`

- The 'hz' mode is simply an input in hertz, as in our main example in the parent patch.;

But please note that the effective cutoff frequency in hertz is the sample rate frequency divided by 4, or half the Nyquist frequency.;

- The 'linear' mode is just a scaled version of the standard hertz mode with values in the 0-1 range isntead 0 and half the Nyquist.;

[svf~] has three different modes (set by messages or arguments) for mapping input values onto cutoff/center frequency. These are mainly for convenience, but they may also slightly improve efficiency.;

- In this mode, input values from 0 to 1 are interpreted as radians, producing a quarter-cycle sinusoidal mapping to cutoff frequencies. This conforms the frequency mapping to a response that is closer to our logarithmic perception of pitch., f 63;

[svf~] implements Chamberlin's state-variable filter algorithm, which outputs lowpass, highpass, bandpass, and band reject (notch) simultaneously in parallel (in this order from left to right)., f 66;

Plugdata users or those with ELSE can also use [else/replace] as an alternative., f 34;


## `switch`

[switch] outputs data from the inlet that's "switched on". Just one inlet from 'n' inlets can send data, or none of them.;

Plugdata users or those with ELSE can also use [else/selector] as an alternative., f 42;


## `table`

opens a standard save file dialog for saving it in a text file format, f 78;

opens and reads data from a file specified by the symbol. If no symbol is given, an open dialog is shown, f 78;

sends the value stored at the address specified by the float to all [receive] objects with the symbol name name, f 78;

the first float specifies a starting address and the next numbers specify the values to be stored from that address on, f 78;

changes a stored number's bit values: 1st float is the address, 2nd is the starting bit location (0-31 from LSB to MSB), 3rd is how many from starting bit should be modified and 4th is the value (in decimal or hexadecimal form) to which those bits should be set, f 78;

cancels last right inlet input (so next left input outputs a number), f 78;

1st float is the address to query, 2nd is starting bit location (0-31 from LSB to MSB) and 3rd is how many bits to the right of starting bit should be sent (as a single decimal integer), f 78;

sends the value stored at the pointed address on left outlet and sets the pointer to the next address (wraps to 1st address when reaching the end), f 78;

similar to "next" message, but the decreases the pointer address (and wraps to last address when reaching start), f 78;

sets the number of values in the table (default: 128, indexed from 0 to 127), f 78;

sets the object to read from a named table specified by the symbol, f 78;

1 toggles saving the data as part of the patch - default 0 (don't save), f 78;

<1, 0> saves contents with the patch when it's saved, <0, 1> doesn't, f 78;

sends the address at which the sum of all values up to that address is >= to the the sum of all table values times the <float> (between 0 and 1), f 78;

sends the address at which the sum of the all values up to that address is >= the the sum of all table values times the <int> divided by 2^15 (32768), f 78;

sets to load mode: all numbers received in the left inlet are stored beginning at address 0 until the end (additional numbers are ignored) or taken out of load mode by a normal message., f 78;

changes from "load mode" to "normal" mode (see "load message"), f 78;

finds the first table value which is >= the float and sends its address, f 78;

And still create the vanilla object from vanilla without namespaces as:;

Pd also has a vanilla object named [table]. Cyclone avoids name clashing and overwriting an internal in Pd Vanilla, but for that you need to use the cyclone namespace ("cyclone/" before the object name), as it's the common practice for cyclone's documentation. So you create it as:;

sets value (y) to be stored at the index sent to left inlet, f 61;

[table] stores and edits a number array. You can graphically edit it by opening it or double clicking on it. There are also several message methods, check it below., f 65;

The [table] object has two modes of operation for loading values into it. The default is the "normal" mode, where it expects a "y" value in the right inlet and an index "x" in the left inlet.;

If you send it a "load" message, the object goes into "load" mode, where numbers in the left inlet are stored from index 0 to the end of the table. If more numbers than available indexes are given, then they're ignored. For you to populate the table again you need to first send the "load" message again.;

The "normal" message sets it back to the normal mode of operation.;

The [table] object takes an optional table name argument. If two or more [table] objects share the same name, then they also share the same values. Below we have two objects named "x", the first one is populated with values. Open the other one and see that it shares the same values.;

There is also a @name attribute that also sets a table name. You can also use the "name" message to set a table name.;

You can set the table size with the "@size" attribute, and also change the size afterwards with the size message.;

The embed method/attribute saves the contents of the table with the patch. Note that the patch needs to be saved for the contents to be stored.;

Click and open the edit window below and see that this table object has its contents stored.;

read/write can load and save files with contents of the table. If no file name is given, a dialog window opens;

If no value is given in the right inlet, the left input gives you the value from the specified index. But if a value has been previously set in the right inlet, then the left input stores that value at the given index., f 70;

Now, if a value is given in the right inlet, you can use the "cancel" message to make it "forget", so when you give it an index in the left inlet, it only outputs its current value and doesn't store anything., f 70;

sends the address at which the sum of the all values up to that address is >= the the sum of all table values times the input divided by 2^15 (32768), f 40;

same as quantile, but the input range is a float from 0 to 1, f 35;

finds the first table value which is >= the input and sends its address, f 37;

<= the refer message loads contents from another table object with that name, f 77;

same as the quantile message with a random number between 0 and 32768 as an argument (see quantile in [pd All_Messages]), f 61;

index (x): outputs its value or stores the value from the right inlet (if given) at that index, f 61;

sets table name - if two or more [table] objects share the same name, they also share the same values (default: none), f 61;

@size <float> (default 128) | @name <symbol> | @embed <float> (default 0), f 73;

Note that [cyclone/table] has inconsistencies to the original Max object. In cyclone the edit window is not a graph, but a list of numbers., f 55;

This makes attributes like @range, @Signed & @notename not relevsant, so they are missing. The @parameter sttribute also seems pointless in Pd., f 55;

The get/setbits messages are not actually implemented in cyclone yet, but it seems to be buggy in Max anyway.;

This makes attributes like @range, @signed & @notename not relevsant, so they are missing. The @parameter sttribute also seems pointless in Pd., f 55;


## `tanh`

[tanh] calculates the hyperbolic tangent function of a given number.;


## `tanh~`

[tanh~] calculates the hyperbolic tangent function of input sample. It is also useful for waveshaping, where it simulates analog distortion.;

[tanh~] will clip values between -1 and 1, but will do so not as "hard clipping" (which would be the case with the [clip~] object). It can actually be considered a waveshaper for soft clipping. This generates a distortion which is more closely related to how analog circuitry does clip a signal in overdrive.;

Plugdata users or those with ELSE can also use [else/drive~] for soft clipping based on the tanh function., f 38;


## `tanx~`

Like [cyclone/cosx~] & [cyclone/sinx~], [tanx~] is properly designed for mathematical operations. Thus, it expects an input in radians to calculate the tangent of each input sample.;


## `teeth~`

If the delay time lies between two samples, a simple linear interpolation is performed.;

[teeth~] is a comb filter with independent time control of feedforward and feedback delays.;

As an alternative, PlugData users and those with ELSE can can easily built this type of system with [else/ffdelay~] and [else/fbdelay~]., f 49;


## `thresh`

[thresh] collects numbers and lists into a single list if they come within a certain given amount of time. Each item or list is appended to the previous stored items. The time count is reset at each incoming item.;

Plugdata users or those with ELSE can also use [else/combine] as an alternative., f 42;


## `thresh~`

[thresh~] is a "Schmitt trigger". When the input is greater than or equal to the high threshold level, the output is 1 and becomes 0 when the signal is equal to or less than the reset level (low threshold).;

If low and high threshold are the same, the output is 1 until a sample in the input signal is less than the reset level (thus it works in the same way as [>=~]).;

Plugdata users or those with ELSE can also use [else/schmitt~] as an alternative., f 42;


## `togedge`

[togedge] sends a bang in the left outlet for "zero to non-zero" transitions, and a bang in the right outlet for "non-zero to zero" transitions., f 65;

switches the stored value from 0 to non-zero, or vice versa, and the change is reported by a corresponding bang output;

Plugdata users or those with ELSE can also use [else/status] as an alternative., f 42;


## `tosymbol`

When converting a message composed of elements separated by spaces, you can define a different "separator character", which will substitute the empty space on the converted symbol. This is done via the "separator" message or via the @separator attribute. Check below:;

But it's hard to convert message with more than one element (list or anything) to a symbol in Pd Vanilla. In Max, you can have any number of elements for a symbol message in a message box if you put it inside quotes (ex. "1 2 3" or "hi sir"). Since that is not the case in Pd, [tosymbol] really comes in handy for converting any message type to a symbol!;

Note: In Pd Vanilla, any message typed into an atom symbol box is treated as a symbol message, even if it contains spaces.;

Also note that 1 element lists are already automatically converted to symbols in Pd:;

[tosymbol] converts any kind of message to a symbol message (maximum of 2048 characters). Start by sending it a float with the number box below and see how it converts to a symbol message.;

Plugdata users or those with ELSE can also use [else/any2symbol] and [else/unite] as alternatives., f 33;


## `train~`

[train~] generates a pulse signal alternating from on (1) to off (0) at a period given in ms. It also sends a bang when going from 0 to 1, so it can be used as a metronome., f 57;

A pulse width of 0 has the smallest "on" pulse size (a single sample), while a pulse width of 1 has the largest (the entire period except the last sample). The "onset phase" delays the "on" portion by a fraction of the total pulse period.;

The original object in MAX/MSP has a very weird behaviour for the onset that just seems buggy so it was not ported to Cyclone - though we still have something similar.;

It is important to note that the onset does not behave as a "phase offset". The onset is from 0 to 1, so an onset of "1" will delay the [train~] object for one period long. You can use it to delay one object and make two of them out of sync.;

Plugdata users or those with ELSE can also use [else/pulse~] as an alternative., f 42;


## `trapezoid~`

[trapezoid~] is a trapezoidal wavetable that is read with phase values from 0 to 1 into the first inlet, so a [phasor~] input turns it into a wavetable oscillator. A second and third inlet change the position of ramp up/down points. The default lo/hi values are 0 and 1, but may be changed using the lo/hi messages or attributes to any given range., f 70;

Plugdata users or those with ELSE can also use [else/envelope~] as an alternative., f 42;


## `triangle~`

[triangle~] is a triangular wavetable that is read with phase values from 0 to 1 into the first inlet- a [phasor~] input turns it into a wavetable oscillator. A second inlet changes the position of the peak value (variable duty, from 0 to 1), going from sawtooth like waveforms to triangular ones. The default lo/hi points are -1 and 1, but may be changed using the lo/hi messages to any given range., f 70;

Plugdata users or those with ELSE can also use [else/vsaw~] as an alternative., f 40;


## `trough`

[trough] compares the input to a 'trough' (minimum) value. If it's smaller, the input becomes the new trough and is sent out. The middle outlet sends 1 when a new trough is set and 0 otherwise. The right outlet sends 1 when the input is not smaller than the trough and 0 otherwise., f 75;

[trough] can take a list of two values as an input. In this case, the 2nd value is set as a new trough value and output. Then, the first value is input. Check the examples below:;

70 is set as a new trough and is output, then 60 is sent to the object and comes out because it's lesser than the current trough and becomes the new trough value.;

20 is set as a new trough and is output, then 30 is sent to the object but doesn't come out as it is greater than the current trough.;

Note: In Pd, [cyclone/trough] only deals with floats, not ints., f 69;


## `trunc~`

[trunc~] truncates a signal towards zero, that means only the integer value is considered. This is not an actual MAX clone but an object that is borrowed from ELSE which has more functionalities (support for multichannel connections) and is backwards compatible to MAX's.;

Plugdata users can just use the original object from ELSE instead (same with those with ELSE)., f 33;


## `universal`

- sends any message to an object type, first element after "send" is the object name. Works for all objects, but it's specially needed for objects named as selectors (pd message types) such as [float], [symbol] and [list].;

- sends any message to an object type, first element of the message is the object name. Doesn't work for objects named as selectors (the "send" message is needed for that);

[universal] sends messages to all instances of the same object in a patch and/or in a subpatch window.;

the argument sets the mode: nonzero also sends to subpatches (but no parent patches), default is 0 (only sends to the same patch window/canvas).;

[universal] also works with GUIs, because all GUIs are actually just regular objects. But you need to know the object's name of the corresponding GUI.;

The object name is easily accessible in their help files, but you can also check it to the right. Below, we have [universal] sending messages to vertical sliders ([vsl] object).;

As with send/receive objects, the order in which the messages arrive is not defined.;

- mode: nonzero also sends to subpatches (but no parent patches), default is 0 (only sends to the same patch window/canvas);


## `unjoin`

number of group outlets (default 2, min 2 / max 255), there's also an extra outlet for the extra elements, f 54;

You can specify the number of elements per group with the "outsize" attribute/argument.;

any message whose elements will be separated into groups of elements, f 53;

[unjoin] separates a list's elements by groups of any size (default 1). Each group is sent out a separate outlet, extra elements are sent to an extra outlet.;

Plugdata users or those with ELSE can also use [else/unmerge] as an alternative, f 41;


## `urn`

- unrepeated random number output - when receiving a bang (if not all have been generated yet);

- if all random numbers have already been generated - when receiving a bang;

[urn] generates random numbers in a range defined by the 'n' size (from 0 to n-1) without repeating them. When all numbers have been output, a bang is sent to the right outlet and it stops generating numbers unless it receives a clear message., f 68;

A 2nd argument can set the seed. You can also set the seed via a message, but only after the sequence has finished or right after it was cleared. If you set it to 0, it's like the default, where an internal value is set.;

Plugdata users or those with ELSE can also use [else/rand.u] as a much more nicely designed as an alternative, f 37;


## `uzi`

[uzi] is useful for sweeping through arrays, using the counter as the index input.;

[uzi] iterates in a programming loop fashion. So, once it starts, it goes all the way to the end as fast as possible. In order to stop it, you need to break the loop with some logic as below, where we use [select] to pause [uzi] when the counter reaches "105".;

Thus, before breaking the loop, it sends 5 bangs (corresponding from 101 to 105 in the counter). You can then continue to output the remaining 5 bangs (from 106 to 110) with the "resume" message.;

This may be useful to perform a special oeration in the middle of the loop.;

You can also use "break" isntead of "pause" and "continue" isntead of "resume".;

After pausing [uzi], you can reset the offset value. This changes the total number of bangs being sent in the end. In the example below, if you break and continue without changing the offset, it goes from 1 to 5, then 6 to 10, but lets change the offset after the break and before continuing and see what happens.;

If you increase the offset from "1" to "11", the counter target is supposed to be "20", so it continues from 6 until reaching 20!;

But if you decrease the offset from "1" to "-9", the counter target is supposed to be "0". Imn this case, it cannot continue outputting any bangs, because the counter is already past the target, so it only outputs a bang in the middle outlet saying it's done!;

[uzi] loops firing a given number of bangs (left outlet) and outputs a count for each bang (right outlet). The middle outlet bangs after the loop is done. The 1st argument is the number of bangs. The counter starts from a given offset (2nd argument).;

Plugdata users or those with ELSE can also use [else/loop] as an alternative., f 39;


## `vectral~`

The [vectral~] object operates in 3 modes, which can be better understood if you already know how these three objects work:;

All of the three objects above can be used to smoothen (or "filter", cause it's also a kind of low pass filtering) signal changes. But hink now that the changes happen between frames rather than between samples.;

- rampsmooth: linear ramp; - deltaclip: also provides a linear ramp, but the parameter sets a minimum step change isntead of a target time; - slide: logarithmic ramp;;

By default, [vector~] just bypasses the input signal with no filtering. So you need to set the mode of operation and values in order for it to act. The last received message sets the current mode of operation. The modes are:;

The left and middle inlet are for output/input index sync, and they need to be from 0 to block size - 1! If the range of the sync signal input index is different than the output index, the incoming vector will be "bin-shifted" by the difference between the two signals.;

Other objects in cyclone that perform operations on frames in a similar way are:;

[vectral~] is useful for smoothening/filtering frame based signal data such as the output of [fft~], mostly for viewing purposes.;


## `wave~`

The cosine interpolator maps a cosine curve (from phase 0 to phase pi) to the values it is interpolating between. It is of limited use., f 76;

As indices in an array increase, there is less and less index resolution between integer index values. The low-quality linear interpolation maps the 0.0-1.0 phase range to the array range in single precision, which means that low index resolution later in the table can result in lower quality audio. The high-quality linear interpolation handles all index values as well as values read from the table in double precision, so that the 24-bit resolution between 0 and 1 is preserved no matter where in the table it reads from., f 76;

Modes 1 & 2 (High & Low Quality Linear Interpolation, respectively):, f 69;

there is no interpolation, this means that indexes are truncated to the sample point., f 73;

The advantage of Lagrange interpolation is that the curve drawn has low RMS error with respect to that of an ideal (sinc) interpolator. A disadvantage is that the first derivative (the isntantaneous slope of the curve) is not usually continuous at breakpoints, which can cause sharp corners in the curve (see examples in the parent patch)., f 75;

An Hermite interpolator addresses the first derivative problem with the Lagrange by deliberately making the first derivative continuous at breakpoints. It interpolates between b and c by finding a cubic polynomial curve that passes through b and c. The curve does not usually pass through a and d. Instead, the interpolator uses the pairs (a, c) and (b, d) to set the curve slope at points b and c, respectively., f 75;

To interpolate between points b and c, a Lagrange interpolator finds a cubic polynomial curve f(x) that passes through all four points a, b, c, and d, imagining a = f(-1), b = f(0), c = f(1), and d = f(2)., f 75;

This is the the kind of interpolation used in Pd's [tabread4~], as well as the cubic interpolating functions in csound. The output is f(m) (where m is the fractional index between 0 and 1)., f 75;

The most basic form of Hermite interpolator sets the curve slope at point b as the slope of the line passing through a and c, which is defined (c - a)/2. The curve slope at point c is set to (d - b)/2. In the examples, it is easy to see that there are no sharp corners. However, the second derivative is discontinuous, so there are occasional abrupt changes in concavity, e.g. at zero-crossings in the 4-period cosine example. There are no such abrupt changes in concavity with Lagrange interpolation. This type of interpolation is used in SuperCollider's interpolating functions., f 75;

The normal range for both tension and bias values is -1 to +1. Outside of that range the curves can be unpredictable., f 75;

The four cubic interpolators work differently from one another. They are discussed out of order here for the sake of clarity. For all examples, let us label the four points as: a, b, c, and d, with interpolation between points b and c., f 76;

Cubic interpolation draws a cubic polynomial curve between the two points it is interpolating between, and uses the points to the left and right of these two as extra information to draw these curves., f 76;

Other slope values can be used to accentuate or attenuate the shape of the curve. The "tension" setting in mode 6 adjusts the curve slope at breakpoints. At point b, the slope is (1 - tension)*((c - a)/2). A tension value of 0 is identical to the Catmull-Rom spline (Mode 5). When tension is +1, the slope is 0 (horizontal) at all breakpoints. Between 0 and 1, the slope at breakpoints is less than that for the Catmull-Rom spline, and the maxima and curve is shallower., f 75;

Tension values between 0 and -1 increase the slope at breakpoints and make the curve deeper. At tension = -1, the slope at breakpoints is double that of the Catmull-Rom spline, and the curve is identical to the "Cubic" interpolation (Mode 4). The period-8 cosine example in the [pd examples] subpatch is a good illustration of tension., f 75;

Bias is related to tension in that it changes slope at breakpoints and depth of curve, but it does so by giving one of the two points surrounding the breakpoint more control over the slope at that breakpoint than the other. Bias values between 0 and 1 give the left point more influence than the right, bias values between 0 and -1 do the opposite., f 75;

Though not referred in Max's documentation, the interpolation formulas for [wave~] almost certainly can found in <http://paulbourke.net/miscellaneous/interpolation>., f 82;

[wave~]'s input phase varies between 0 and 1, which in 32-bit floating point arithmetic has 24 bits of index resolution. All interpolators (except mode 2: low quality linear) use double-precision index mapping, so behavior should be the same in all parts of a table., f 82;

At the time of Max 4, [wave~] only had one cheaop linear interpolator. Earlier versions of cyclone included Pd's interpolator isntead. This is mode is now added as an extra mode 7 (and is also used in [tabread4~], [tabosc4~], and [vd~] or [delread4~])., f 82;

Please find more theoretical details for each mode in the subpatches below:, f 82;

Unlike [tabread4~], [wave~] does not use guard points for interpolating between the end and the beginning of the array, but isntead treats the range as a circular buffer, where phases 0 and 1 point to the first element of the table. Input phase is clipped to the 0-1 range. A bug from Max was fixed, where the 4-point interpolation modes did not wrap correctly., f 82;

Low-quality linear interpolation (found in MSP 1.x versions of [wave~], f 43;

The [wave~] object in cyclone offers 7 modes of interpolation, which can be set with the "interp" message/attribute., f 62;

The Hermite interpolation has extra parameters: 'bias' and 'tension', respectively set with the 'interp_bias' and 'interp_tension' messages/attributes.;

For more details in the theory of interpolation and some examples, please check the subopatches below:, f 58;

If more than one channel is set, the name convention for multi channel arrays is the table name preceded by the channel number (starting from zero) and "-", such as: "0-", "1-", "2-", "3-", and so on...;

You can manually set multi channel arrays in Pd like that or use the [buffer~] object, which does this internally.;

Multi channel playback is possible (up to 64 channels) when you specify it with a 4th argument. The number of channels defines the number 'n' of outlets.;

With a phase signal input (from 0 and 1), [wave~] reads a given table. It has many interpolation options and can set a start and end point in the array.;

@interp_bias <f> (default 0) | @interp_tension <f> (default 0), f 63;

Plugdata users or those with ELSE can also use the more powerful [else/loop] as an alternative., f 33;


## `xbendin`

sets channel number - if no channel is set (default), the object has an extra right outlet that outputs the MIDI channel number.;

[xbendin] retrieves 14-bit pitch bend messages from raw MIDI input data.;

Plugdata users or those with ELSE can also use dedicated [else/bend.in] instead if you really need the filter raw MIDI input, f 42;


## `xbendin2`

sets channel number - if no channel is set (default), the object has an extra right outlet that outputs the MIDI channel number.;

[xbendin2] retrieves the Most and Least Significant Byte (7-bits values) from pitch bend messages of incoming raw MIDI data. Both can be combined to generate a 14-bit value.;

Plugdata users or those with ELSE can also use dedicated [else/bend.in] instead if you really need the filter raw MIDI input, f 42;


## `xbendout`

[xbendout] formats and sends messages that occupy both bytes of the MIDI pitch bend message (14 bit from 0 - 16383).;

Plugdata users or those with ELSE can also use dedicated [else/bend.out] instead if you really need the raw MIDI output, f 42;


## `xbendout2`

[xbendout2] formats and sends pitch bend messages as two 7-bit messages (values from 0-127), the Most Significant Byte (MSB) and the Least Significant Byte (LSB).;

Plugdata users or those with ELSE can also use dedicated [else/bend.out] instead if you really need the raw MIDI output, f 42;


## `xnotein`

[xnotein] is more powerful than [notein] as it retrieves (from raw MIDI data streams) not only Note On Velocity but also Note Off (Release) velocity.;

sets channel number - if no channel is set, the object has an extra right outlet that outputs the MIDI channel number. The default is no channel set.;

Plugdata users or those with ELSE can also use [else/note.in] as a much more nicely designed as an alternative, f 38;


## `xnoteout`

[xnoteout] is more powerful than [noteout] as it send not only Note On Velocity but also Note Off (Release) velocity.;

Plugdata users or those with ELSE can also use [else/note.out] as a much more nicely designed as an alternative, f 38;


## `zerox~`

[zerox~] functions as a zero-crossing detector and/or a zero-crossing counter (for transient detection).;

Left outlet outputs a value that corresponds to the number of zero crossings per signal block - so it depends on the block size. Right outlet send an impulse at every zero crossing.;

Look at the difference between "ssss" and "aaa" or any noisy/transient input as opposed to a tonal and stable one., f 38;

Plugdata users or those with ELSE can also use [else/zerocross~] as an alternative, f 43;


## `zl`

'ecils' is 'slice' backwards, so it slices a list in reverse order. You can set the split point with an argument or with a float input into the right inlet, but also when you set the mode with the mode message. The default point is '0', which means no slicing.;

If you slice at 'n', the left outlet spits the last 'n' elements and the right outlet sends the first sliced elements.;

Plugdata users or those with ELSE can use [else/slice] as an alternative., f 37;

The input can have one or more elements, when the grouped elements reach the group size, the grouped list is sent out the left outlet. The remaining items are stored for next group.;

A bang message causes it to spit (and clear from the memory) the remaining stored elements (at the set group size).;

The group mode aggroups 'n' elements into a list, where 'n' cannot be higher than the maximum zl size. You can set 'n' (the group size) with an argument or with a float input into the right inlet, but also when you set the mode with the mode message. The default group size is 0, which means nothing gets grouped and output.;

Plugdata users or those with ELSE can use [else/group] as an alternative., f 37;

The iter mode breaks an input list in to successive lists of a given size. If an input list is smaller than the iter size, the lista is output anyway - if the last bit of the broken list is of a size smaller than the iter size, it is also output.;

The iter size can be set with an argument or with a float input into the right inlet, but also when you set the mode with the mode message. The minimum iter size is 1 and the default is '0', which means nothing happens.;

Plugdata users or those with ELSE can use [else/iterate] as an alternative., f 37;

The join mode joins two lists sent to each inlet (things in list 2 that are in list 1 are duplicated). A bang resends the last output or outputs a new list if the right inlet received something new. Subsequent arguments initialize the right list. The right outlet is inactive.;

Plugdata users or those with ELSE can use [else/merge] as an alternative., f 37;

The len mode outputs how many elements a lista has. A bang resends the last output. This mode has no arguments. The right inlet/outlet are inactive.;

The element that replaces the mth element in the right outlet is set as the 2nd argument. This is optional, no second argument (the default) does not replace the mth element by anything.;

The mth element is set as the 1st argument. The 1st element is treated as "0 '(the default). If you set the mth to a number greater than the input list, all the elements are sent to the right outlet, the same happens for negative mth values.;

The mode mth is the same as nth but starts counting from 0 isntead. It outputs the mth element of a message through the left outlet. The right outlet outputs the remaining elements, but the output can also replace the mth element by another.;

Plugdata users or those with ELSE can use [else/pick] as an alternative., f 37;

The element that replaces the nth element in the right outlet is set as the 2nd argument. This is optional, no second argument (the default) does not replace the nth element by anything.;

The mode nth is the same as mth but starts counting from 1 isntead. It outputs the nth element of a message through the left outlet. The right outlet outputs the remaining elements, but the output can also replace the nth element by another., f 61;

The nth element is set as the 1st argument. The 1st element is treated as "1", if you set it as 0 (the default) or to a number greater than the input list, all the elements are sent to the right outlet and nothing is sent via the left outlet., f 61;

Plugdata users or those with ELSE can use [else/pick] as an alternative., f 37;

The reg mode stores lists. The initially stored list is set as an argument and changed in the right inlet. The left inlet stores and outputs the list. A bang sends the last stored list. The right outlet is inactive.;

The rev mode reverses the elements of a list. A bang resends the last output. This mode has no arguments. The right inlet/outlet are inactive.;

Plugdata users or those with ELSE can use [else/reverse] as an alternative., f 37;

The mode rot does rotate a list. If the rotation point is a positive number 'n', the list is shifted to the right by 'n' positions, and the last 'n' elements are placed at the list start. If 'n' is negative, the rotation happens at the other direction.;

You can set the rotation point with an argument or with a float input into the right inlet, but also when you set the mode with the mode message. The default point is '0', which means no rotation.;

Plugdata users or those with ELSE can use [else/rotate] as an alternative., f 37;

The mode sect outputs the elements of an input list that are in common to another list (set as an argument or via the right inlet). The default is an empty list.;

The right outlet outputs a bang if there are no matching elements.;

A bang performs the operation in the last received list into the left inlet.;

The slice mode slices a list. You can set the split point with an argument or with a float input into the right inlet, but also when you set the mode with the mode message. The default point is '0', which means no slicing.;

If you slice at 'n', the left outlet spits the first 'n' elements and the right outlet sends the remaining elements.;

Plugdata users or those with ELSE can use [else/slice] as an alternative., f 37;

the sub mode searches for occurrences of the element(s) of the second list to the first list and outputs the number of occurrences in the right outlet and the position of such occurrences in the left outlet. If no occurrence is found, the right outlet outputs 0 and nothing is output on the left outlet. Subsequent arguments initialize the right list.;

Plugdata users or those with ELSE can use [else/substitute] as an alternative., f 40;

union the stuff in two lists (but does not duplicate things in list 2 that are in list 1). Subsequent arguments initialize the right list. The right outlet is inactive.;

The sort mode sorts the elements of a list. An additional argument specifies the order: "-1" sorts in descending order, and any other value sorts in ascending order (the default is "0"/ascending). This vis also specified in the right inlet.;

The left outlet outputs the sorted list, and the right outlet outputs the sorted indexes., f 57;

Plugdata users or those with ELSE can use [else/sort] as an alternative., f 38;

The change mode filters out list repetitions. The right outlet sends "1" when there's a new list and "0" when it is repeated. Arguments initialize the list to filter., f 56;

Plugdata users or those with ELSE can use [else/changed] as an alternative., f 37;

The compare mode compares two lists and sends "1" if it is the same or "0" if it is not. In the case on non equal lists, the right output sends the number of non equal indexes.;

Plugdata users or those with ELSE can use [else/equal] as an alternative., f 37;

filter removes items in a list, the items to filter are specified as the arguments or the right input. The right outlet outputs the unfiltered and output indexes.;

lace interleaves two lists. Subsequent arguments initialize the right list. The right outlet is inactive.;

lookup outputs the nth elements in a list. The arguments or right input sets the list to lookup and the left input sets the nth elements.;

Plugdata users or those with ELSE can use [else/pick] as an alternative., f 37;

Plugdata users or those with ELSE can use [else/median] as an alternative., f 37;

scramble scrambles the order of a list. The right input and arguments sets the list. The right outlet outputs the scrambled indexes.;

Plugdata users or those with ELSE can use [else/scramble] as an alternative., f 38;

The queue mode is a FIFO message storage (First In, First Out). A list input stores the elements sequenatially. A bang otuputs the stored elements in order. The right outlet outputs the size of the queue., f 63;

Plugdata users or those with ELSE can use [else/stack] as an alternative., f 37;

The stack mode is a LIFO message storage (Last In, First Out). A list input stores the elements sequenatially. A bang otuputs the stored elements in order. The right outlet outputs the size of the queue., f 63;

Plugdata users or those with ELSE can use [else/stack] as an alternative., f 38;

the stream mode makes a list with the last N items. The N is set as an argument or in the right inlet. A negative N inverts the list. The right outlet sends "1" if it reached the N number of elements and "0" otherwise. A bang resends the last output., f 62;

Plugdata users or those with ELSE can use [else/stream] as an alternative., f 38;

The mode sum sums the float values in a list, symbol elements are ignored. A bang performs the operation in the last received list. Right inlet/outlet don't do anything.;

Plugdata users or those with ELSE can use [else/sum] as an alternative., f 37;

unique removes items in a list, the items to filter are specified as the arguments or the right input. The right outlet is inactive.;

The thin mode remove all the duplicates from an input list. A bang performs the operation in the last received list. Right inlet/outlet don't do anything.;

In this mode, a list of indexes (0-based) in the right inlet or as arguments indicates the indexes to generate a new list from the received list in the left inlet. An index less than 0 or greater than/equal to the number of elements of the incoming list will be clamped to 0 - a bang performs the operation in the last received list.;

The right inlet or argument is a list of pair of indexes (0-based) to swap in the received list in the left inlet. A bang performs the operation in the last received list., f 57;

In the above example, the objects are initialized to a size of 512 but can be resized to the default (256)., f 54;

When not using a dot, the mode argument is obrigatory, otherwise an error is printed. This also implies there is no default mode. You can change mode as a message in any case, by the way. Check details about each mode in the subpatches on the right., f 55;

The default maximum size is 256 elements. When you're not using a dot to set the mode, you can change the maximum size with a first optional float argument. In this case you need a symbol argument that specifies the mode type. If you are using a dot you can only reset the maximum size with the '@zlmaxsize' attribute. The maximum size is also set via the 'zlmaxsize' attribute or message (and it can be up to 32767)., f 55;

- float: length of the grouped list (default is zlmaxsize), f 65;

- anything: elements to union to the first list (default none), f 65;

- anything: elements to join to the first list (default none), f 65;

- float: order "-1" is desending, ascending otherwise (default 0), f 65;

- anything: list to compare with left input (default none), f 65;

- anything: list to compare with left input (default none), f 65;

- anything: list to check if changed from left input (default none), f 67;

The modes: delace, len, median, queue, rev, stack, sum and thin don't have arguments. The other modes can have subsequent arguments as below. See also [pd examples] for more details on how they work., f 55;

sets mode (you can also set subsequent arguments) - check [pd examples] for more info;

@zlmaxsize <float> - max list size (1 - 32767, default 256), f 62;

mode (change, compare, delace, ecils, group, indexmap, iter, join, lace, len, lookup, median, mth, nth, queue, reg, rev, rot, sect, scramble, slice, sort, stack, stream, sub, sum, swap, thin, union or unique). Modes can have subsequent arguments, check:;

[zl] processes messages with one or more elements ("list messages' or "anything") according to a mode set via argument/message or in the object name after a '.' (dot)., f 74;

Plugdata users or those with ELSE can use dedicated objects for list manipulations as alternatives and related objects., f 34;

Note that MAX does not require a list selector, so this object can produce lists without the list selector. You can force a list selector output if you feed it a list with the list selector anyway., f 74;


