# pd-else

## `above`


## `above~`


## `abs.pd~`

This object is still experimental and limited to just 2 ins and 2 outs, but more features are planned. If you give it an argument, it automatically loads/starts the sub-process. In order for this to happen, both sub and super processes have their DSP state automatically set to on. If you don't want anything to start at loading the patch, just don't give it any arguments and then send it a start message.;

[abs.pd~] loads a pd file into a subprocess via [pd~] and makes things more convenient like making the subprocess able to receive MIDI data from MIDI devices connected to the parent process (thanks to [sendmidi]). Also, you can open the subprocess patch by clicking on the object., f 77;


## `abstraction-1`


## `add`


## `add~`


## `adsr.m~`

This polyphonic ADSR envelope takes multichannel signals for gate input in the left inlet and retrigger in the 2nd inlet (a bang input in the left inlet also retriggers). The other inlets are audio CV controlls for attack, decay, sustain and release that pass through attenuverters and are added to the knob controls. Attack, decay and release values are in ms, sutain point is a ratio of the gate input., f 76;

This is a wrapper around [adsr~] from ELSE, check it out., f 18;

The release output value can be used to set the release parameter in [voices~], f 28;

The 2nd inlet is for retriggering with impulses. Here's an example with [mono~]. A bang works as a control rate version of this., f 48;


## `adsr~`

[adsr~] accepts any gate value, positive or negative and above 1 or below -1, so you can use it to control anything besides amplitude.;

Here we have randomly generated notes into a sustain pedal and then feeding a [voice] object with 2 voices. Also see that each voice subpatch has [adsr~]'s status outlet to control a DSP switch for that subpatch - open and check it. You should also try pd's [clone] object for managing polyphonic synths.;

You can use the [timed.gate~] object to create a timed gate so you can trigger the envelope with an impulse., f 54;

[adsr~] has a right outlet that sends a status value (1 when the envelope starts and 0 when it ends). This can be useful for different things, but particularly to turn on and off the DSP processing of a subpatch or abstraction with [switch~]., f 62;

In the case of turning [switch~] on or off, this only works for control data input, because if the audio engine is off you can't use it to turn it on., f 62;

You can retrigger the envelope with a bang or with a float value. With float values you don't need to turn the gate off before retriggering the envelope, so even repeated values make the envelope restart the attack ramp. Try it below or on the right.;

A bang considers the last non zero float value as the gate value, and the default value is "127"!, f 60;

Note: the [envgen~] object has a retrigger mode which allows you to set a retrigger time in ms. Hence, if you want to have a more versatile ADSR object with this functionality, please use this more general and all purpose envelope generator. Check its help file for more details on how its retrigger mode works.;

At a signal rate, you can retrigger the envelope with impulses or gates via the second inlet., f 60;

The [adsr~] object can operate in "lin" (linear) mode, set with the -lin flag or "lin" message. By defqult, [adsr~] is logarithmic, which implements a one pole filter, much like the [lag~] object. This non-liner mode simulates how analog gear work in general. The attack or release time represent how long it takes for the signal to converge to within 0.01% of the target value., f 68;

3) float - sustain amplitude ratio to gate value (default 1), f 61;

Control gate is possible in 2 ways. With a float value the MIDI velocity range is considered, so 0-127 is the same as 0-1 in signal values (float values and values outside this range is possible). Moreover, a 'gate' message sets the actual gate value in the normal range at control rate., f 63;

At a gate on (transition from 0 to any value), the attack ramp is generated, then a decay ramp goes to the sustain point (specified as a ratio of the gate value). A gate off (transition from any value to 0) makes [adsr~] go to 0 at the specified release time in ms. A gate is possible in the leftmost inlet via dignal and control values., f 65;

If [adsr~] has a multichannel left input, it outputs the same number of channels, one for each gate signal. Secondary inlets must have the same number of channels if bigger than 1, in which case each channel gets its own parameter, otherwise the single channel input is copied to all channels., f 68;

[adsr~] is an attack/decay/sustain/release gated envelope. The object has multichannel support., f 69;


## `allpass.2nd~`

This filter has zeroes fixes at +1 and -1 on the z-plane, which means both 0Hz and Nyquist are always filtered out.;

Change the parameters and check the filter response below. The graph considers a sample rate of 44.1Khz.;

a0, a1, a2, b1 and b2 are calculated as a function of center frequency 'f' in hz and 'q' as follows;;

omega = f * PI/nyquist; alphaQ = sin(omega) / (2*q); b0 = alphaQ + 1; a0 = (1 - alphaQ) / b0; a1 = -2*cos(omega) / b0; a2 = 1; b1 = 2*cos(omega) / b0; b2 = (alphaQ - 1) / b0;;

The equation is from the "Cookbook formulae for audio EQ biquad filter coefficients" by Robert Bristow-Johnsonc [1], and it is: y[n] = a0 * x[n] + a1 * x[n-2] + a2 * x[n-2] + b1 * y[n-1] + b2 * y[n-2];

[1] found in https://webaudio.github.io/Audio-EQ-Cookbook/audio-eq-cookbook.html, f 80;

By default, the resonance parameter is the filter 'q', but you can also set it as bandwidth in octaves. This is done with the -bw flag.;

Alternatively, you can switch from 'q' to 'bw' with the message methods.;

2) float - resonance (default 1), either in 'Q' (default) or 'bw', f 65;

APF; - b1 = 2*cos(w) / b0; - b2 = (alphaQ - 1) / b0; - a0 = (1 - alphaQ) / b0; - a1 = -2*cos(w) / b0; - a2 = 1; - b0 = 1 + alphaQ; - alphaQ = sin(w) / (2*Q);

In this example, we add the phase shifted signal to the original, which cancels frequencies by phase opposition., f 69;

In the [allpass.2nd~] object, the phase is shifted from 0 (at 0 hz) to 360Âº (at the Nyquist frequency). The frequency at which it shifts to 180Âº is specified as the filter's frequency and the steepness of the curve is determined by the Q parameter (see graph below)., f 69;


## `allpass.filt~`

[allpass.filt~] is an allpass filter that you can set its order with the first argument (needs to be a multiple of 2). This is an abstraction that stacks many [allpass.2nd~] objects in cascade., f 63;


## `allpass.rev~`

Negative values of t60 generate negative feedback of the same absolute value as its absolute input., f 60;

An "All Pass Filter" passes all frequencies without altering their gain, but affects the phase response., f 44;

The [apass2~] object performs a simple linear interpolation for delay time that falls in between sample values.;

By default, the 'a' coefficient is calculated in [apass2~] from the decay time parameter (t60) and delay time (D) according to the expression: a = exp(log(0.001) * D/t60).;

1) float - maximum and initial delay time in ms (default 0), f 60;

By default, the reverberation/decay time is in "t60", which is the time in ms that the impulse takes to fall 60dB in energy. You can change this parameter to a gain coefficient value with the third argument, where a non zero value sets to "gain mode". You can also change that with the "gain" message., f 72;

Use [allpass.rev~] as a reverberator, allpass filter and delay. By default, you can set a delay time and a reverberation/decay time in ms ("t60"), which is the time the impulse takes to fall 60dB in energy (but you can change this parameter to a gain coefficient)., f 67;


## `amean`

[amean] creates a list of arithmetic means. It takes a start point, an end point and the number of steps from start to end., f 64;

The number of steps is the output list length - 1 and represents the number of values until reaching the end. The minimum number of steps is "1"., f 64;


## `any2symbol`


## `args`


## `asr~`

[asr~] accepts any gate value, positive or negative and above 1 or below -1, so you can use it to control anything besides amplitude.;

Here we have randomly generated notes into a sustain pedal and then feeding a [voice] object with 2 voices. Also see that each voice subpatch has [asr~]'s status outlet to control a DSP switch for that subpatch - open and check it. You should also try pd's [clone] object for managing polyphonic synths.;

You can use the [timed.gate~] object to create a timed gate so you can trigger the envelope.;

This only works for control data such as MIDI, and is possible because the float input of [adsr~] will always turn the status on, so you can use it to start the DSP. See below., f 62;

[asr~] has a right outlet that sends a status value (1 when the envelope starts and 0 when it ends). This can be useful for different things, but particularly to turn on and off the DSP processing of a subpatch or abstraction with [switch~].;

The [asr~] object can operate in "lin" (linear) mode, set with the -lin flag or "lin" message. By defqult, [adsr~] is logarithmic, this mode implements a one pole filter, much like the [lag~] object. This is a non-liner mode that simulates how analog gear work. The attack or release time represent how long it takes for the signal to converge to within 0.01% of the target value., f 68;

Control gate is possible in 2 ways. With a float value the MIDI velocity range is considered, so 0-127 is the same as 0-1 in signal values (float values and values outside this range is possible). Moreover, a 'gate' message sets the actual gate value in the normal range at control rate., f 63;

If [asr~] has a multichannel left input, it outputs the same number of channels, one for each gate signal. Secondary inlets must have the same number of channels if bigger than 1, in which case each channel gets its own parameter, otherwise the single channel input is copied to all channels., f 68;

[asr~] is an attack/sustain/release gated envelope. At a gate on (transition from 0 to any value), [asr~] goes from 0 to that value at the specified attack time in ms. A gate off (transition from any value to 0) makes [asr~] go to 0 at the specified release time in ms. The object has multichannel support., f 69;


## `autofade.mc~`

fade types <quartic, sin, sqrt, hann, lin, hannsin, linsin>, f 42;

There are two "constant power" curves, which have a crossing point at -3dB., f 33;

We have the "sin" (sine) function above and a "sqrt" (square root) function below., f 33;

The "sin" function is 1/4 of the cycle of a sine function., f 33;

The "sqrt" function is the same as extracting the square root of the input., f 33;

As a compromise between the functions that cross between -3 and -6dB, we have a crossing point at -4.5 dB., f 37;

This can be achieved with a geometric mean between such functions. Here we have a mean between the "hann" and the "sin" function above, and a mean between the "lin" and "sin" function below., f 37;

There are two "constant voltage" curves, which have a crossing point at -6dB., f 33;

We have the "hann" function above and a linear transfer function below, f 33;

The "hann" function is half the cycle of a "cosine" function., f 33;

The "lin" function does nothing, it is the same as the input., f 33;

The default curve is "quartic", which is the same as raising the input to the power of 4, f 31;

Open the subpatches on the right for more details on the fading curves ----> available, f 39;

(optional) fade types <quartic, sin, sqrt, lin, hann, lin, hannsin, linsin> (default: quartic), f 47;

[autofade.mc~] is an automatic fade in/out for multichanne inputs. It responds to a gate control and uses internal lookup tables just like [fader~]. A gate on happens when the last input value was zero or less and the incoming value isn't. A gate off happens when the last value was greater than zero value and the incoming value isn't! The maximum gain depends on the gate on level., f 80;


## `autofade2.mc~`

fade types <quartic, sin, sqrt, hann, lin, hannsin, linsin>, f 42;

There are two "constant power" curves, which have a crossing point at -3dB., f 33;

We have the "sin" (sine) function above and a "sqrt" (square root) function below., f 33;

The "sin" function is 1/4 of the cycle of a sine function., f 33;

The "sqrt" function is the same as extracting the square root of the input., f 33;

As a compromise between the functions that cross between -3 and -6dB, we have a crossing point at -4.5 dB., f 37;

This can be achieved with a geometric mean between such functions. Here we have a mean between the "hann" and the "sin" function above, and a mean between the "lin" and "sin" function below., f 37;

There are two "constant voltage" curves, which have a crossing point at -6dB., f 33;

We have the "hann" function above and a linear transfer function below, f 33;

The "hann" function is half the cycle of a "cosine" function., f 33;

The "lin" function does nothing, it is the same as the input., f 33;

The default curve is "quartic", which is the same as raising the input to the power of 4, f 31;

Open the subpatches on the right for more details on the fading curves ----> available, f 39;

(optional) fade types <quartic, sin, sqrt, lin, hann, lin, hannsin, linsin> (default: quartic), f 47;

[autofade2.mc~] is an automatic fade in/out for multichanne inputs. It responds to a gate control and uses internal lookup tables just like [fader~]. A gate on happens when the last input value was zero or less and the incoming value isn't. A gate off happens when the last value was greater than zero value and the incoming value isn't! The maximum gain depends on the gate on level., f 80;


## `autofade2~`

fade types <quartic, sin, sqrt, hann, lin, hannsin, linsin>, f 42;

There are two "constant power" curves, which have a crossing point at -3dB., f 33;

We have the "sin" (sine) function above and a "sqrt" (square root) function below., f 33;

The "sin" function is 1/4 of the cycle of a sine function., f 33;

The "sqrt" function is the same as extracting the square root of the input., f 33;

As a compromise between the functions that cross between -3 and -6dB, we have a crossing point at -4.5 dB., f 37;

This can be achieved with a geometric mean between such functions. Here we have a mean between the "hann" and the "sin" function above, and a mean between the "lin" and "sin" function below., f 37;

There are two "constant voltage" curves, which have a crossing point at -6dB., f 33;

We have the "hann" function above and a linear transfer function below, f 33;

The "hann" function is half the cycle of a "cosine" function., f 33;

The "lin" function does nothing, it is the same as the input., f 33;

The default curve is "quartic", which is the same as raising the input to the power of 4, f 31;

Open the subpatches on the right for more details on the fading curves ----> available, f 39;

(optional) fade types <quartic, sin, sqrt, lin, hann, lin, hannsin, linsin> (default: quartic), f 47;

[autofade2~] is an automatic fade in/out for multi inputs. It responds to a gate control and uses internal lookup tables just like [fader~]. A gate on happens when the last input value was zero or less and the incoming value isn't. A gate off happens when the last value was greater than zero value and the incoming value isn't! The maximum gain depends on the gate on level., f 80;


## `autofade~`

fade types <quartic, sin, sqrt, hann, lin, hannsin, linsin>, f 42;

There are two "constant power" curves, which have a crossing point at -3dB., f 33;

We have the "sin" (sine) function above and a "sqrt" (square root) function below., f 33;

The "sin" function is 1/4 of the cycle of a sine function., f 33;

The "sqrt" function is the same as extracting the square root of the input., f 33;

As a compromise between the functions that cross between -3 and -6dB, we have a crossing point at -4.5 dB., f 37;

This can be achieved with a geometric mean between such functions. Here we have a mean between the "hann" and the "sin" function above, and a mean between the "lin" and "sin" function below., f 37;

There are two "constant voltage" curves, which have a crossing point at -6dB., f 33;

We have the "hann" function above and a linear transfer function below, f 33;

The "hann" function is half the cycle of a "cosine" function., f 33;

The "lin" function does nothing, it is the same as the input., f 33;

The default curve is "quartic", which is the same as raising the input to the power of 4, f 31;

Open the subpatches on the right for more details on the fading curves ----> available, f 39;

(optional) fade types <quartic, sin, sqrt, lin, hann, lin, hannsin, linsin> (default: quartic), f 47;

[autofade~] is an automatic fade in/out for multi inputs. It responds to a gate control and uses internal lookup tables just like [fader~]. A gate on happens when the last input value was zero or less and the incoming value isn't. A gate off happens when the last value was greater than zero value and the incoming value isn't! The maximum gain depends on the gate on level., f 80;


## `autotune`

[autotune] receives a scale as a list of steps in cents and a base MIDI pitch value (default 60). It then retunes incoming MIDI pitches to the closest step in the scale., f 67;


## `autotune2`

[autotune2] receives a scale as a list of steps in cents and then retunes incoming cents values to the closest step in the scale., f 67;


## `avg`


## `balance~`

The '-mc' flag sets to output a multichannel audio containing both stereo signals. Balance signal is still a single channel., f 50;


## `bandpass~`

a0, a2, b1 and b2 are calculated as a function of center frequency 'f' in hz and 'q' as follows;;

omega = f * PI/nyquist; alphaQ = sin(omega) / (2*q); b0 = alphaQ + 1; a0 = alphaQ / b0; a2 = -a0; b1 = 2*cos(omega) / b0; b2 = (alphaQ - 1) / b0;;

The equation is from the "Cookbook formulae for audio EQ biquad filter coefficients" by Robert Bristow-Johnsonc [1], and it is:;

This filter has zeroes fixes at +1 and -1 on the z-plane, which means both 0Hz and Nyquist are always filtered out.;

Change the parameters and check the filter response below. The graph considers a sample rate of 44.1Khz.;

[1] found in https://webaudio.github.io/Audio-EQ-Cookbook/audio-eq-cookbook.html, f 80;

By default, the resonance parameter is the filter 'q', but you can also set it as bandwidth in octaves. This is done with the -bw flag.;

Alternatively, you can switch from 'q' to 'bw' with the message methods.;

2) float - resonance (default 1), either in 'Q' (default) or 'bw', f 65;

[bandpass~] is a 2nd order bandpass resonant filter. Unlike [else/resonant~], it has a maximum and constant gain at 0dB.;


## `bandstop~`

This filter has zeroes fixes at +1 and -1 on the z-plane, which means both 0Hz and Nyquist are always filtered out.;

Change the parameters and check the filter response below. The graph considers a sample rate of 44.1Khz.;

a0, a1, a2, b1 and b2 are calculated as a function of center frequency 'f' in hz and 'q' as follows;;

omega = f * PI/nyquist; alphaQ = sin(omega) / (2*q); b0 = alphaQ + 1; a0 = 1 / b0; a1 = -2*cos(omega) / b0; a2 = a0; b1 = -a1; b2 = (alphaQ - 1) / b0;;

The equation is from the "Cookbook formulae for audio EQ biquad filter coefficients" by Robert Bristow-Johnsonc [1], and it is: y[n] = a0 * x[n] + a1 * x[n-2] + a2 * x[n-2] + b1 * y[n-1] + b2 * y[n-2];

[1] found in https://webaudio.github.io/Audio-EQ-Cookbook/audio-eq-cookbook.html, f 80;

By default, the resonance parameter is the filter 'q', but you can also set it as bandwidth in octaves. This is done with the -bw flag.;

Alternatively, you can switch from 'q' to 'bw' with the message methods.;

2) float - resonance (default 1), either in 'Q' (default) or 'bw', f 65;

[bandstop~] is a 2nd order band reject filter, it can also be used as a 'notch' filter.;


## `bang2imp~`

[bang2imp~] converts bangs to impulses with sample accuracy, it is an abstraction based on [vline~]. The default impulse value is '1' and can be set via the argument or right inlet., f 66;


## `bangdiv`


## `batch.rec~`

clicking on the object opens dialog box to set a file to save to, f 65;

[batch.rec~] is a convenient abstraction based on [writesf~] and the 'fast-forward' message to pd that batch records to a sound file - that you can load with objects like [sample~], [play.file~], [player~] and others.;

record for given amount in ms. If no float is given, the last set value is used., f 52;


## `batch.write~`


## `beat~`

[beat~] makes use of different Onset detection methods, which are:, f 70;

Mode 0 --> "hfc": High-Frequency content (Default); - Computes the High Frequency Content (HFC) of the input spectral frame. This is efficient at detecting percussive onsets. Reference: Paul Masri. Computer modeling of Sound for Transformation and Synthesis of Musical Signal. PhD dissertation, University of Bristol, UK, 1996, f 82;

Mode 1 --> "energy": Energy based distance; - Calculates the local energy of the input spectral frame., f 82;

Mode 2 --> "complex": Complex domain; - Suited for complex signals such as polyphonic recordings. Reference: Christopher Duxbury, Mike E. Davies, and Mark B. Sandler. Complex domain onset detection for musical signals. In Proceedings of the Digital Audio Effects Conference, DAFx-03, pages 90-93, London, UK, 2003, f 82;

Mode 3 --> "phase": Phase based detection; Suited for complex signals such as polyphonic recordings. Reference: Juan-Pablo Bello, Mike P. Davies, and Mark B. Sandler. Phase-based note onset detection for music signals. In Proceedings of the IEEE International Conference on Acoustics Speech and Signal Processing, pages 441Â­444, Hong-Kong, 2003, f 82;

Mode 5 --> "specdiff": Spectral difference; Reference: Jonhatan Foote and Shingo Uchihashi. The beat spectrum: a new approach to rhythm analysis. In IEEE International Conference on Multimedia and Expo (ICME 2001), pages 881Â­884, Tokyo, Japan, August 2001, f 82;

Mode 6 --> "specflux": Spectral flux; Reference: Simon Dixon, Onset Detection Revisited, in ``Proceedings of the 9th International Conference on Digital Audio Effects'' (DAFx-06), Montreal, Canada, 2006, f 82;

Mode 8 --> "mkl": Modified Kulback-Liebler function; Reference: Paul Brossier, 'Automatic annotation of musical audio for interactive systems', Chapter 2, Temporal segmentation, PhD thesis, Centre for Digital music, Queen Mary University of London, London, UK, 2006, f 82;

Mode 7 --> "kl": Kulback-Liebler function; Reference: Stephen Hainsworth and Malcolm Macleod. Onset detection in music audio signals. In Proceedings of the International Computer Music Conference (ICMC), Singapore, 2003, f 82;

[beat~] takes an input signal and outputs a detected BPM value., f 52;


## `bend.in`

An argument sets the channel number. If so, only MIDI messages that correspond to that channel are sent. If no channel is given, it loads "0" as the default and the object operates in omni mode, where the objects outputs values from all channels and the channel number is output in the right outlet. You can also change the channel with the right inlet (0 sets to omni)., f 67;

Port number is encoded as the channel number. Channels 1 to 16 are for port 1, channels 17 to 32 is the same as channels 1 to 16 for port 2, channels 33 to 48 represents channels 1 to 16 in port 3, and so on..., f 63;

With the -raw flag, the pitch bend values are output as integers from 0 to 16383, whereas the default behaviour is a normalized output (floats from -1 to 1), f 67;

The object automatically listens to whatever is connected as a MIDI device in Pd. So it's like it has a built in [midiin] object feeding it. This is considered to be an "internal" source.;

The left inlet provides and "external" source of raw MIDI data input. This is needed if you have, for instance, the [midi] object from ELSE reading a MIDI file or something. If, by any chance, you just want the object to receive from this external source and not listen to the internal connected device, you can use the '-ext' flag or 'ext' message, to force only the external input.;

[bend.in] extracts MIDI Pitch Bend information from raw MIDI input (or a connected MIDI device. By default, output values are normalized to floats from -1 to 1, but you can change it to "raw" mode (output integers from 0 to 16383)., f 69;


## `bend.out`

With the -raw flag, the input pitch bend values are from 0 to 16383, whereas the default behaviour is a normalized output (floats from -1 to 1), f 57;

[bend.out] formats and sends raw MIDI pitch bend messages to Pd's MIDI output and its outlet. By default, it takes normalized values (floats from -1 to 1). An argument sets channel number (the default is 1)., f 66;

The object automatically outputs to whatever is connected as a MIDI device in Pd. So it's like it has a built in [midiout] object. If, by any chance, you just want the object to output to the outlet (for feeding a [midi] object or something), you can use the '-ext' flag or 'ext' message., f 61;


## `bicoeff`

The range is logarithmic in MIDI pitch (horizontal axis) and dB (vertical axis). The horizontal line is for 0 dB and the vertical lines represent and set the bandwidth or slope (for the shelving filters). You can click anywhere on the object to set frequency by moving through the horizontal axis, but if you click on the vertical lines you can set bandwidth instead. The Y axis sets gain for 3 filter types: "eq, lowshelf and highshelf).;

Note: if you closk and drag too quickly you might get some clicks. Use [morph~] in this case with a short grain size.;

[bicoeff2] produces the same filter coefficients as [bicoeff], but without any GUI.;

The [else/biplot] object below plots filter information with more detail for any biquad coefficient (so it's a great companion to [bicoeff2])., f 55;

The ELSE library carries related objects with all the filter types from the biquad coefficient generators and with the same name! These have signal inlets to control all the parameters. Here they are -------->, f 43;

[bicoeff] is a GUI that generates coefficients for vanilla's [biquad~] according to different filter types ("eq" filter by default as in the example below). Click on it and drag it around., f 66;

sets filter type: <allpass, lowpass, highpass, bandpass, resonant, bandstop, eq, lowshelf, highshelf>., f 57;


## `bicoeff2`


## `bin.shift~`


## `biplot`


## `biquads~`


## `bitnormal~`

[bitnormal~] replaces NaN (not a number), +/- infinity values and denormals of an incoming signal with zero (hence, it only lets 'normal' floats through. This is useful in conjunction with the bitwise operators in [else/op~], [expr~] or any other situation where these values are possible. It has support for multhichannel sgnals., f 66;


## `bl.imp2~`

By default, frequency input is in hertz, but if you use the 'midi' message or '-midi' flag you can change it to MIDI pitch input, where it is not really bound to the 0 to 127 range, neither it has to be integers. This is just like using [mtof~]...;

If the oscillator has a multichannel input, it outputs the same number of channels. You can initialize the object with multichannel if you give it a list of frequencies with the -mc flag. A list input also works if no signal is connected to set it to multichannel with a list of frequency input., f 75;

[bl.imp2~] is a two sided impulse oscillator like [else/imp2~], but it is bandlimited., f 63;

-mc <list>: sets multichannel output with a list of frequencies, f 63;


## `bl.imp~`

[bl.imp~] is an impulse oscillator like [else/imp~], but it is bandlimited.;

By default, frequency input is in hertz, but if you use the 'midi' message or '-midi' flag you can change it to MIDI pitch input, where it is not really bound to the 0 to 127 range, neither it has to be integers. This is just like using [mtof~]...;

If the oscillator has a multichannel input, it outputs the same number of channels. You can initialize the object with multichannel if you give it a list of frequencies with the -mc flag. A list input also works if no signal is connected to set it to multichannel with a list of frequency input., f 75;

-mc <list>: sets multichannel output with a list of frequencies, f 63;


## `bl.osc~`

Here's an example with hard sync via impulses and phase modulation of a band limited square wave. Note that hard sync and phase modulation cause aliasing.;

[bl.osc~] is a bandlimited oscillator based on [else/wavetable~]. It has wavetables built with a variable number of partials for different waveforms: 'saw', 'saw2', 'tri', 'square' and 'imp'., f 67;

There are 2 versions of sawtooth waveforms (see else/saw~ and else/saw2~), plus a triangular waveform (see else/tri~), a square (see else/square~) and impulse (see else/imp~). Setting the number of partials rewrites all internal tables (whatch for clicks)., f 75;

By default, frequency input is in hertz, but if you use the 'midi' message or '-midi' flag you can change it to MIDI pitch input, where it is not really bound to the 0 to 127 range, neither it has to be integers. This is just like using [mtof~]...;

Syncing the phase with control messages is useful for LFOs and control with MIDI. A sync with audio is useful for the "hard sync" technique, where an oscillator is synced according to the frequency of a master frequency., f 50;

The second inlet resets the phase, but unlike [saw~], it has no way to set with control data. This is because that is more suited to low ferquencies., f 41;

You can then reset the oscillator with an impulse signal. The impulse values need to be > 0 and <= 1 (otherwise ignored). Because phase is cyclical, the value of 1 represents the "phase 0" of the cycle, where the impulse occurs. Send it impulses above and check the result., f 41;

Soft sync is also possible with the '-soft' flag or the "soft" message, where it alternates between positive and negative frequencies and sounds less harsh., f 50;

The "phase sync" inlet is quite different from the "phase offset" inlet. They are completely independent!, f 43;

sets waveform (obligatory): saw, saw2, tri, square and imp);

The second argument sets an initial phase (or "phase offset"). This is also settable with the third inlet. This allows you to control two oscillators with the same frequency falling in and out of phase. Another feature is phase modulation., f 53;

The phase values are wrapped into the 0-1 range, since the phase cycle is from 0 to 1 (where 1 is also the start of another cycle)., f 33;

Note that out of phase sawtooth waveforms do not cancel each other, f 23;


## `bl.saw2~`

By default, frequency input is in hertz, but if you use the 'midi' message or '-midi' flag you can change it to MIDI pitch input, where it is not really bound to the 0 to 127 range, neither it has to be integers. This is just like using [mtof~]...;

A variable sawtooth waveform oscillator that also becomes a triangular osccilator., f 43;

This is the waveform of this oscillator. Not really like this because it is band-limited., f 44;

Syncing the phase with control messages is useful for LFOs and control with MIDI. A sync with audio is useful for the "hard sync" technique, where an oscillator is synced according to the frequency of a master frequency., f 50;

You can then reset the oscillator with an impulse signal. The impulse values need to be > 0 and <= 1 (otherwise ignored). Because phase is cyclical, the value of 1 represents the "phase 0" of the cycle, where the impulse occurs. Send it impulses above and check the result., f 41;

Soft sync is also possible with the '-soft' flag or the "soft" message, where it alternates between positive and negative frequencies and sounds less harsh., f 50;

The "phase sync" inlet is quite different from the "phase offset" inlet. They are completely independent!, f 43;

The second inlet resets the phase, but unlike [saw2~], it has no way to set with control data. This is because that is more suited to low ferquencies., f 41;

The second argument sets an initial phase (or "phase offset"). This is also settable with the third inlet. This allows you to control two oscillators with the same frequency falling in and out of phase. Another feature is phase modulation., f 53;

The phase values are wrapped into the 0-1 range, since the phase cycle is from 0 to 1 (where 1 is also the start of another cycle)., f 33;

Note that out of phase sawtooth waveforms do not cancel each other, f 23;

[bl.saw2~] is a sawtooth oscillator like [else/saw2~], but it is bandlimited. Use [saw2~] mostly if you need a perfect sawtooth, which is usually the case when you want a LFO. The [bl.saw2~] version is for proper synthesis as it is anti-aliased. This version also has input for pitch in MIDI and no way to sync at control rate., f 77;


## `bl.saw~`

By default, frequency input is in hertz, but if you use the 'midi' message or '-midi' flag you can change it to MIDI pitch input, where it is not really bound to the 0 to 127 range, neither it has to be integers. This is just like using [mtof~]...;

Syncing the phase with control messages is useful for LFOs and control with MIDI. A sync with audio is useful for the "hard sync" technique, where an oscillator is synced according to the frequency of a master frequency., f 50;

The second inlet resets the phase, but unlike [saw~], it has no way to set with control data. This is because that is more suited to low ferquencies., f 41;

You can then reset the oscillator with an impulse signal. The impulse values need to be > 0 and <= 1 (otherwise ignored). Because phase is cyclical, the value of 1 represents the "phase 0" of the cycle, where the impulse occurs. Send it impulses above and check the result., f 41;

Soft sync is also possible with the '-soft' flag or the "soft" message, where it alternates between positive and negative frequencies and sounds less harsh., f 50;

The "phase sync" inlet is quite different from the "phase offset" inlet. They are completely independent!, f 43;

A variable sawtooth waveform oscillator that also becomes a triangular osccilator., f 43;

This is the waveform of this oscillator. Not really like this because it is band-limited., f 44;

The second argument sets an initial phase (or "phase offset"). This is also settable with the third inlet. This allows you to control two oscillators with the same frequency falling in and out of phase. Another feature is phase modulation., f 53;

The phase values are wrapped into the 0-1 range, since the phase cycle is from 0 to 1 (where 1 is also the start of another cycle).;

Note that out of phase sawtooth waveforms do not cancel each other, f 23;

[bl.saw~] is a sawtooth oscillator like [else/saw~], but it is bandlimited. Use [saw~] mostly if you need a perfect sawtooth, which is usually the case when you want a LFO. The [bl.saw~] version is for proper synthesis as it is anti-aliased. This version also has input for pitch in MIDI and no way to sync at control rate. The object has support for multichannel signals., f 75;

If the oscillator has a multichannel left input, it outputs the same number of channels. If the secondary inlets have a signal with a single channel for sync and phase modulation, the single value is applied to all channels. If a secondary inlet is also a multichhanel signal, then each channel gets its sync or phase deviation value. Note, however, that the number of multichannels in secondary inlets need to match the same number of channels from the left input., f 76;

You can initialize the object with multichannel if you give it a list of frequencies with the -mc flag (you can't set phases though). A list input also works if no signal is connected to set it to multichannel with a list of frequency input., f 49;

-mc <list>: sets multichannel output with a list of frequencies, f 63;


## `bl.square~`

By default, frequency input is in hertz, but if you use the 'midi' message or '-midi' flag you can change it to MIDI pitch input, where it is not really bound to the 0 to 127 range, neither it has to be integers. This is just like using [mtof~]...;

The pulse width is set via the first argument or the second inlet.;

The pulse width parameter controls how much of the cycle is "1" or "-1". A pulse width of 0.5 means the first half is "1" and the last half is "-1".;

A pulse width of 0 has the first sample is "1" and the rest is "-1". Conversely, a pulse width of 1 has the opposite situation (the entire period is "1" except the last sample, which is "-1").;

The phase values are wrapped into the 0-1 range, since the phase cycle is from 0 to 1 - where 1 is also the start of another cycle., f 36;

The third argument sets an initial phase (or "phase offset"). This is also settable with the fourth inlet. In such a way, you have two objects with the same frequency falling out and back in sync. Another feature is phase modulation., f 51;

Syncing the phase with control messages is useful for LFOs and control with MIDI. A sync with audio is useful for the "hard sync" technique, where an oscillator is synced according to the frequency of a master frequency., f 50;

You can then reset the oscillator with an impulse signal. The impulse values need to be > 0 and <= 1 (otherwise ignored). Because phase is cyclical, the value of 1 represents the "phase 0" of the cycle, where the impulse occurs. Send it impulses above and check the result., f 41;

Soft sync is also possible with the '-soft' flag or the "soft" message, where it alternates between positive and negative frequencies and sounds less harsh., f 50;

The "phase sync" inlet is quite different from the "phase offset" inlet. They are completely independent!, f 43;

The third inlet resets the phase, but unlike [square~], it has no way to set with control data. This is because that is more suited to low ferquencies., f 41;

[bl.square~] is a square oscillator like [else/square~], but it is bandlimited. Use [square~] mostly if you need a perfect square wave, which is usually the case when you want a LFO. The [bl.square~] version is for proper synthesis as it is anti-aliased. This version also has input for pitch in MIDI and no way to sync at control rate., f 71;

-mc <list>: sets multichannel output with a list of frequencies, f 63;

If the oscillator has a multichannel left input, it outputs the same number of channels. If the secondary inlets have a signal with a single channel for sync and phase modulation, the single value is applied to all channels. If a secondary inlet is also a multichhanel signal, then each channel gets its sync or phase deviation value. Note, however, that the number of multichannels in secondary inlets need to match the same number of channels from the left input., f 76;

You can initialize the object with multichannel if you give it a list of frequencies with the -mc flag (you can't set phases though). A list input also works if no signal is connected to set it to multichannel with a list of frequency input., f 49;


## `bl.tri~`

By default, frequency input is in hertz, but if you use the 'midi' message or '-midi' flag you can change it to MIDI pitch input, where it is not really bound to the 0 to 127 range, neither it has to be integers. This is just like using [mtof~]...;

Syncing the phase with control messages is useful for LFOs and control with MIDI. A sync with audio is useful for the "hard sync" technique, where an oscillator is synced according to the frequency of a master frequency., f 50;

The second inlet resets the phase, but unlike [saw~], it has no way to set with control data. This is because that is more suited to low ferquencies., f 41;

You can then reset the oscillator with an impulse signal. The impulse values need to be > 0 and <= 1 (otherwise ignored). Because phase is cyclical, the value of 1 represents the "phase 0" of the cycle, where the impulse occurs. Send it impulses above and check the result., f 41;

Soft sync is also possible with the '-soft' flag or the "soft" message, where it alternates between positive and negative frequencies and sounds less harsh., f 50;

The "phase sync" inlet is quite different from the "phase offset" inlet. They are completely independent!, f 43;

The second argument sets an initial phase (or "phase offset"). This is also settable with the third inlet. This allows you to control two oscillators with the same frequency falling in and out of phase. Another feature is phase modulation., f 53;

The phase values are wrapped into the 0-1 range, since the phase cycle is from 0 to 1 (where 1 is also the start of another cycle).;

[bl.tri~] is a triangle oscillator like [else/tri~], but it is bandlimited. Use [tri~] mostly if you need a perfect triangular wave, which is usually the case when you want a LFO. The [bl.tri~] version is for proper synthesis as it is anti-aliased. This version also has input for pitch in MIDI and no way to sync at control rate., f 75;

If the oscillator has a multichannel left input, it outputs the same number of channels. If the secondary inlets have a signal with a single channel for sync and phase modulation, the single value is applied to all channels. If a secondary inlet is also a multichhanel signal, then each channel gets its sync or phase deviation value. Note, however, that the number of multichannels in secondary inlets need to match the same number of channels from the left input., f 76;

You can initialize the object with multichannel if you give it a list of frequencies with the -mc flag (you can't set phases though). A list input also works if no signal is connected to set it to multichannel with a list of frequency input., f 49;

-mc <list>: sets multichannel output with a list of frequencies, f 63;


## `bl.vsaw~`

By default, frequency input is in hertz, but if you use the 'midi' message or '-midi' flag you can change it to MIDI pitch input, where it is not really bound to the 0 to 127 range, neither it has to be integers. This is just like using [mtof~]...;

[bl.vsaw~] is a variable sawtooth waveform oscillator that also becomes a triangular osccilator just like [else/vsaw~], but it is bandlimited. Use [vsaw~] mostly if you need a wave form, which is usually the case when you want a LFO. The [bl.vsaw~] version is for proper synthesis as it is anti-aliased. This version also has input for pitch in MIDI and no way to sync at control rate., f 71;

A width of 0 or 1 makes it a sawtooth like waveform, while between 0 and 1 makes it triangular variants., f 53;

For a width parameter of 1, the waveform is of an inverted sawtooth., f 68;

The waveform can change/vary to different waveforms according to the width parameter.;

The start and end of the cycle is always an amplitude value of "-1" for all waveforms, except when the width parameter is = 0, which is the default and when the waveform is the same of [saw~], (see "\$0-saw1" above on the left)., f 54;

For a parameter of "0.5", the waveform is similar to [bl.tri~], (see "\$0-default-triangle" above in the middle). Note that they have a phase difference of 0.25 between each other., f 63;

The phase values are wrapped into the 0-1 range, since the phase cycle is from 0 to 1 - where 1 is also the start of another cycle., f 36;

The third argument sets an initial phase (or "phase offset"). This is also settable with the fourth inlet. In such a way, you have two objects with the same frequency falling out and back in sync. Another feature is phase modulation., f 51;

Syncing the phase with control messages is useful for LFOs and control with MIDI. A sync with audio is useful for the "hard sync" technique, where an oscillator is synced according to the frequency of a master frequency., f 50;

You can then reset the oscillator with an impulse signal. The impulse values need to be > 0 and <= 1 (otherwise ignored). Because phase is cyclical, the value of 1 represents the "phase 0" of the cycle, where the impulse occurs. Send it impulses above and check the result., f 41;

Soft sync is also possible with the '-soft' flag or the "soft" message, where it alternates between positive and negative frequencies and sounds less harsh., f 50;

The "phase sync" inlet is quite different from the "phase offset" inlet. They are completely independent!, f 43;

The third inlet resets the phase, but unlike [vsaw~], it has no way to set with control data. This is because that is more suited to low ferquencies., f 41;

-mc <list>: sets multichannel output with a list of frequencies, f 63;

If the oscillator has a multichannel left input, it outputs the same number of channels. If the secondary inlets have a signal with a single channel for sync and phase modulation, the single value is applied to all channels. If a secondary inlet is also a multichhanel signal, then each channel gets its sync or phase deviation value. Note, however, that the number of multichannels in secondary inlets need to match the same number of channels from the left input., f 76;

You can initialize the object with multichannel if you give it a list of frequencies with the -mc flag (you can't set phases though). A list input also works if no signal is connected to set it to multichannel with a list of frequency input., f 49;


## `bl.wavetable~`

The "phase sync" inlet is quite different from the "phase offset" inlet. This means that the are completely independent., f 43;

The second inlet resets the phase ands behaves in the same way for control data as objects like [osc~] and [tabosc4~] in Pd. A number input resets the oscillator and restarts the cycle with an initial phase that corresponds to the input number, so the internal phase is synced to the given value. The phase values are from 0 to 1 and values beyond that are wrapped within this range.;

Additionally, you can reset the oscillator with an impulse signal. The impulse values need to be > 0 and <= 1 (otherwise ignored). Because phase is cyclical, the value of 1 represents the "phase 0" of the cycle, where the impulse occurs., f 62;

Syncing the phase with control messages is useful for LFOs and control with MIDI. A sync with audio is useful for the "hard sync" technique, where an oscillator (called slave) is synced according to the frequency of a master oscillator, f 58;

Soft sync is also possible with the '-soft' flag or the "soft" message, where it alternates between positive and negative frequencies and sounds less harsh., f 58;

The phase values are wrapped into the 0-1 range, since the phase cycle is from 0 to 1 (where 1 is also the start of another cycle).;

The second float argument sets an initial phase (or "phase offset"). This is also settable with the third inlet. This allows you to control two oscillators with the same frequency falling in and out of phase. Another feature is phase modulation., f 53;

By default, [bl.wavetebale~] uses the spline interpolation method but you can set it to linear, cosine, lagrange or no interpolation at all. For more details, check the subsection 'interpolation' of chapter 28 (buffer) in the live elctronics tutorial., f 35;

By default, frequency input is in hertz, but if you use the 'midi' message or '-midi' flag you can change it to MIDI pitch input, where it is not really bound to the 0 to 127 range, neither it has to be integers. This is just like using [mtof~]...;

-none/-lin/-cos/-lagrange: set interpolation mode (default spline), f 67;

-midi: sets frequency input in MIDI pitch (default hertz), f 64;

[bl.wavetable~] is a bandlimited wavetable oscillator abstraction that uses the upsampling/filtering techniquelike, which makes the object quite inefficient CPU wise. This object also minimizes aliasing caused by hard sync and phase modulation. No wavetable scanning here though..., f 71;

table <symbol> - sets an entire array to be used as a waveform, f 63;

Besides the first argument, the "table" message followed by an array name sets an entire array to be used as a waveform. If no name is given or if you send a name that doesn't correspond to an exist array, then the output is silent., f 63;


## `blip~`

If the fundamental frequency input is '100', the number of harmonics is 2 and the lowest harmonic is 1, then you have '100' and '200' as the partial's frequencies. Now, if the lowest harmonic is 2, then you have '200' and '300'., f 34;

The spectral multiplier 'm' is a factor that scales each successive harmonic by. If m = 0.5 and you start with 1st harmonic and ask for 4 harmonics, you get 1, 0.5, 0.25 and 0.125 as the amplitude list. A factor of 1 creates an impulse like waveform. Negative values and values outside the -1 and 1 range is possible., f 34;

This example also uses the 2nd inlet for hard sync and 3rd inlet for phase modulation. Note that both of these generate aliasing., f 45;

[blip~] uses DSF (Discrete-Summation Formulae) to generate waveforms as a sum of cosines. It takes a frequency in hertz for the fundamental, a number of harmonics, a multiplier for the partials after the first one and the lowest harmonic number (by default it generates an impulse waveform). This object is based on Csound's 'gbuzz' opcode., f 82;

By default, frequency input is in hertz, but if you use the 'midi' message or '-midi' flag you can change it to MIDI pitch input, where it is not really bound to the 0 to 127 range, neither it has to be integers. This is just like using [mtof~]...;

Syncing the phase with control messages is useful for LFOs and control with MIDI. A sync with audio is useful for the "hard sync" technique, where an oscillator is synced according to the frequency of a master frequency., f 50;

The second inlet resets the phase, but unlike [saw~], it has no way to set with control data. This is because that is more suited to low ferquencies., f 41;

You can then reset the oscillator with an impulse signal. The impulse values need to be > 0 and <= 1 (otherwise ignored). Because phase is cyclical, the value of 1 represents the "phase 0" of the cycle, where the impulse occurs. Send it impulses above and check the result., f 41;

Soft sync is also possible with the '-soft' flag or the "soft" message, where it alternates between positive and negative frequencies and sounds less harsh., f 50;

The "phase sync" inlet is quite different from the "phase offset" inlet. They are completely independent!, f 43;

The phase values are wrapped into the 0-1 range, since the phase cycle is from 0 to 1 (where 1 is also the start of another cycle)., f 33;

The third inlet sets "phase offset", which allows you to control two oscillators with the same frequency falling in and out of phase. Another feature is phase modulation., f 53;


## `blocksize~`


## `bpbank~`

Here a ramp time is given to set a transition time in ms between parameter changes of resonant frequency, Q and amplitude. By default, this is set to 10 ms. You can also send a list of ramp time for each filter in the bank.;

The "-mc" flag or message sets to multichannel output, where each filter in the bank is in a different channel., f 30;

-rampall <float>: sets ramp time for all filters (default 10), f 61;

[bpbank~] is a bank made of [bandpass~] objects. The number of filters is set via the parameter list size (such as the frequency list). There's also support for multichannel output., f 72;


## `bpm`


## `brane.m~`

if the number is not a power of 2, it rounds to the nearest power of two below that number.;

This is something you can only specify through messages sent to the patch. You can click on the "steps" number box in the patch and it will generate an equal division scale based on that number of steps, but you can't specify which interval ratio will be divided. So it will always divide to the ratio that was set by this message. In the case this value wasn't set by a message, the default interval value loaded on the patch depends on the loaded scale on the preset;

Makes the shiffting value of harmony-voice to be in an interval relation to the root-voice shift;

list of numbers: scale steps in cents (needs to star with zero). This allows ANY Kind of scale to be loaded into the patch! The scales are also stored on the presets. It doesn't need to be equal nor end in an octave. The highest value will be interpreted as the new starting point of the next scale cycle. It is also the default interval value that you can divide into equal steps;

Target duration (or real duration of buffer according to speed) in min.sec/ms (like time number box)*;

converts seconds to minutes (integer part) and seconds/ms (decimal part);

The presets include just about every control that's relevant to be saved on your patch.;

LOADING AND SAVING PRESETS; There's a presets folder that stores a preset file whenever you save a preset. You can load this file into any preset number afterwards. The file is stored with the preset name and the file extension .brn;

Preset numbers are from 1 to 94, but only units from 1 to 4 are good (1 to 4, 11 to 14, 21 to 24 and so on). Thus, there are 10 groups of presets and a total of 40 presets. If you insert a number that doesn't correspond to a preset, the default preset (number 1) will be loaded.;

Aditional optional arguments can be "preset name" (if symbol), "preset number" (if float) or both (in any order).;

optinal argument, preset name (gets file with same name in ./presets subfolder)., f 41;

optinal argument, preset number where to load the preset file, f 32;

* the load command only loads the preset and does not store it. But the hint is that, when you have 2 arguments, you can store it afterwards by inserting a "store" command message after a comma, like this:;

optional 2nd argument: sound file's sample rate in Khz - this is needed if different than the one Pd is running at, since a sample rate compensation is needed both for pitch and time-stretch;

normalizes after recording is finished; (if not playing simultaneously);

** Note that the help file has this sample that runs at 96Khz and is 4839 ms long. If you're running Pd at the sample rate of 44.1Khz and record on top of this buffer, the buffer time will be updated to 10535 ms to match the 44.1Khz sample rate.;

buffer length in min (integer part) and sec/ms (decimal part) - min 100 ms / max 60 min (ms are rounded);

1st argument: sound file (no 2nd argument means that sample rate is the same as Pd's), f 90;

open command with no arguments: Choose sound file from computer (sets sample rate according to Pd's), f 100;

Messages can change every single GUI control of the abstraction. Some extra features are only possible via messages and are marked here as:, f 51;

Check bellow all message groups. The controls will become clearer then..., f 51;

This is an extra module which consist of a ganulator sampler with stretch/compress and a harmonizer pitch shifter. The sampler records or plays mono files and runs two Pitch Shifters for a "root" and a "harmony" voice. An autotuner can quantize pitches to any scale (and has a built-in scale generator based on Equal Divisions). You have automatic looping, bouncing, freeze and selection of audio slices, and also a granulator and random playing settings. You can load/store 40 presets., f 83;

Being an extra M.E.R.D.A module, it doesn't have state saving and has its own preset system management., f 24;


## `break`


## `brickwall~`


## `brown`

Pseudo random number generators aren't true random number generators. Instead, an algorithm is used to provide a sequence of numbers that seems random. The same sequence can be reproduced if you set a "seed" value, which can be any integer number., f 52;

Seeds are kept locally, which means that if two [brown] objects are seeded the same they will have the same output. Conversely, you can seed the same [brown] object twice with the same seed to repeat the output., f 52;

You can set a seed with the '-seed' flag. If you don't supply it, each object gets its own seed internal seed. If you send a 'seed' message without float, the object also gets a unique seed value., f 52;

seed <float> - a float sets seed, no float sets a unique internal, f 65;

[brown] is implemented as a bounded random walk whose default maximum step up or down is 0.125 (as a ratio of the whole range), so if it tries to step outside the bounds, it just gets folded back inside it. You can set another maximum step value via the first argument or a float input., f 54;

[brown] is a control brownian motion generator. It is a bounded random walk (based on a pseudo random number generator algorithm). By default, the maximum step is "0.125", which is a ratio of the whole range (and the output range is from 0 to 127). If it tries to step outside the bounds, it just gets folded back., f 79;


## `brown~`

seed <float> - a float sets seed, no float sets a unique internal, f 65;

[brown~] is implemented as a bounded random walk whose default maximum step is 0.125 (up or down, with 50% chance for each case). If it tries to step outside the bounds -1 to 1, it just gets reflected (or folded) back in (so 1.02 becomes 0.98, for instance). You can set another maximum step value (maximum 1). The higher the step, the more it sounds like white noise, the lower, the less bright the sound becomes. You can set the step with the argument or a float input., f 76;

[brown~] is a brown noise generator (aka brownian noise or red noise), whose spectral energy drops 6dB per octave (sounding less hissy than white noise). It is implemented as a bounded random walk (based on a pseudo random number generator algorithm). By default, the maximum step is 0.125, but you can set that. If a signal is connected, non zero values generate new random steps., f 76;

When a signal is connected to [brown~], non zero values generate new random steps. This way you can use impulses to generate new steps., f 48;

Pseudo random number generators aren't true random number generators. Instead, an algorithm is used to provide a sequence of numbers that seems random. The same sequence can be reproduced if you set a "seed" value, which can be any integer number., f 52;

You can set a seed with the '-seed' flag. If you don't supply it, each object gets its own seed internal seed. If you send a 'seed' message without float, the object also gets a unique seed value., f 52;

Seeds are kept locally, which means that if two [brown~] objects are seeded the same they will have the same output. Conversely, you can seed the same [brown~] object twice with the same seed to repeat the output., f 52;


## `buffer`


## `button`

-bgcolor <f, f, f>: background color in RGB (default 255 255 255), f 66;

-fgcolor <f, f, f>: fore ground color in RGB (default 255 255 255), f 66;

[button] is a GUI button that opearets in three modes: latch (default), where it responds to mouse clicks and release, and 'bang' and 'toggle' mode., f 69;

A bang in the bang mode activates the button and outputs a bang. In the other cases it changes the internal state., f 49;

A float input only works when not in the bang mode. For the other cases it sets the state (if different than the internal one) and outputs the value ("1" for on state and "0" for off state). A non zero value input sets the state to on and outputs "1" (even it the non zero value is different than 1)., f 49;

A set message is like a float message and it also doesn't work in the bang mode, but only sets the visual state instead (no output)., f 49;

Here we have a [button] object in toggle mode that also sets the name and color of a [note] object as an example to design more sophisticated buttons with labels for on/off state., f 52;

when in bang mode, activates bang, change state otherwise, f 47;


## `canvas.active`

The [canvas.active] reports this subpatch's window activity., f 43;

Note that the depth is not only for subpatches, but also abstractions!!, f 37;

With the depth argument of 1, this [canvas.active] reports the parent patch activity., f 35;

The [canvas.active] object outputs activity status. It sends 1 if the window is active (when it's the front-most window) and 0 when inactive. It can also query the parent status with the depth argument (1 goes up to the parent patch, 2 queries the parent's parent and so on)., f 71;

With the -name flag it outputs the active window's name (in which case depth argument is ignored). You can use this as a send symbol to do things like dynamic patching with the active window or get messages from an active window., f 71;

This is more for dynamic patching ninjas. Use the canvas name to receive and send information to the active canvas., f 33;


## `canvas.bounds`


## `canvas.edit`


## `canvas.gop`


## `canvas.mouse`

Below, the object gets information when you interact with the parent window., f 62;

An optional argument sets the depth level and can query the parent patch's directory, or granparent's and so on. This way, "1" gets the directory of the parent's patch, "2" the grandparent's and so on. The depth gets clipped to the maximum level. If you do not specify a float as the first argument, the default level is "0" (which is the current patch's directory)., f 66;

A second optional argument sets to "position-mode", which resets the position coordinates according to the position of the subpatch/abstraction in the parent patch. Therefore, this option only makes sense if the depth level is more than zero., f 59;

This is particularly useful for a graph on parent subpatch or abstraction, because the (0, 0) coordinates correspond to the top left corner of the graph. See below., f 59;

[canvas.mouse] gets mouse click and mouse coordinates when your mouse is interacting with the canvas window. An optional argument sets the depth level. A second optional argument sets to "position-mode", which resets the position coordinates according to the position of the subpatch/abstraction in the parent patch. By default, there's no output in edit mode, but a non zero third argument allows output even in edit mode., f 69;


## `canvas.name`

You can set a level number to query for the name of the parent patch (1) or parent's parent patch (2) and so on...;

when you set to '-env' you get the environment's name, which is the same as the main patch window. The depth also works here to get an owning patch's environment name.;

[canvas.name] gives you the window name symbol, useful for dynamic patching ninjas.;

In this example we use the window name to set the receive name of [receiver] and get all messages from this window.;


## `canvas.pos`


## `canvas.setname`

[canvas.setname] sets a symbol name to a canvas so you can send it messages. It's similar to [namecanvas] but it also allows you to set the name of a parent patch with the second optional depth argument - (1) is parent patch (2) is parent's parent patch and so on..., f 64;

The third argument sets how the level argument works. By default it is the parent canvas ("subpatch" mode) but a non zero value names the main window of parent patch (aka "the canvas root") - this is called "abstraction mode" because a "level 1" guarantees that it's gonna name the abstraction owner no matter in which canvas the object is.;


## `canvas.vis`


## `canvas.zoom`


## `car2pol`


## `car2pol~`

[car2pol~] is useful for spectral processing in the more intuitive polar form (with amplitude and phase values). This is because when performing spectral analysis in Pd, the signal is in the cartesian form, so we need [car2pol~] and [pol2car~] to convert to and from the polar form in order to perform the FFT and iFFT. Here's the general idea:, f 57;

[car2pol~] converts cartesian coordinates (real / imaginary) to polar coordinates (amplitude / phase). It has support for multichannel signals.;

Multichannel support example. The number of channels need to match!, f 43;


## `ceil`


## `ceil~`

[ceil~] is a ceil math function for signals. It has support for multichannel connections., f 63;


## `cents2frac`


## `cents2ratio`

Use [cents2ratio] to convert list of intervals in cents to intervals as rational numbers (expressed as floating point decimals). The conversion formula is: ratio = pow(2, (cents/1200))., f 72;


## `cents2ratio~`

Using an LFO rescaled to a new range in cents (-500 to 700) abd then converted to ratios for pitch modulation.;

Use [cents2ratio~] to convert a signal representing an interval in cents to an interval represented as a decimal rational number. It has support for multichannel connections. The conversion formula is; ratio = pow(2, (cents/1200)), f 69;


## `cents2scale`

Use [cents2scale] to convert a list of intervals defined as cents to a scale defined as scale steps in semitones.;


## `chance`


## `chance~`

If no argument is given, the chances are 50/50! Moreover, you get a float inlet to set the chance as a percentage value.;

If just one argi, emt is given, it is also considered a percentage value and the second inlet changes it as well., f 47;

list of probabilities (default 50 50). Check [pd default] for more info if only one float is given;

When [chance~] receives an impulse, it outputs it to an outlet according to its chance (probability weight). The total number of chances is the sum of all arguments., f 62;

Pseudo random number generators aren't true random number generators. Instead, an algorithm is used to provide a sequence of numbers that seems random. The same sequence can be reproduced if you set a "seed" value, which can be any integer number., f 52;

You can set a seed with the '-seed' flag. If you don't supply it, each object gets its own seed internal seed. If you send a 'seed' message without float, the object also gets a unique seed value., f 52;

Seeds are kept locally, which means that if two [chance~] objects are seeded the same they will have the same output. Conversely, you can seed the same [chance~] object twice with the same seed to repeat the output., f 52;

When you give it two or more arguments, it is considered as a histogram and [chance~] creates outlets according to the number of given arguments. In this case, [chance] takes a list that updates all arguments. Values are not percentage anymore but a histogram, so below you have, by default, "7 out of 8" on the left outlet and "1 out of 8 on the right outlet., f 56;


## `changed`

You can use [changed] to filter out a repeated random number and trigger a new value., f 32;

[changed] passes its data input through only when it changed from the last receive message or the message that was set via arguments or messages. Unlike [change] from Pd Vanilla, it accepts any kind of messages., f 67;


## `changed2~`

[changed2~] sends an impulse whenever an input value changes its direction. The right outlet sends the status information (1 when increasing, -1 when decreasing and 0 for no change).;


## `changed~`


## `chorus.m~`

This is just a wrapper around [chorus~] from ELSE, check it out., f 22;

this is still a simple module, with no CV input yet, so kinda like a pedal still., f 22;


## `chorus~`

[chorus~] is a simple mono chorus effect abstraction. It uses an internal comb filter and has only one extra voice.;


## `chrono`


## `circle`

If you send it a list of x/y coordinates, the [circle] object will clip it inside its range and output it.;

The "set" message behaves similarly, it just doesn't output the incoming value. You can send a bang to force output., f 56;

By default, the slider output range is from -1 to 1, but you can change it with the -range flag or the range message, which sets the range for both x and y dimensions. But you can also set independent range for both x and y with the -xrange, -yrange or xrange, yrange messages. Note that a bang rescales the last output according to the new range., f 64;

You can set the size with the '-size' flag or with the 'size' message., f 25;

You can set background colors (different colors for inside and outside the circle) and frontground colors with 'bgcolor1' (inside circle) / 'bgcolor2' (outside circle) / 'fgcolor' messages and '-bgcolor1' / '-bgcolor2' / '-fgcolor' flags. You can also set both background colors with the '-fgcolor' flag or 'fgcolor' message., f 83;

You can set the size with the '-size' flag or with the 'size' message., f 25;

-fgcolor <f, f, f>: sets frontground color in RGB (default 0 0 0), f 76;

-bgcolor1 <f, f, f>: sets in bounds back color in RGB (default 255 255 255), f 76;

-bgcolor2 <f, f, f>: sets out of bounds color in RGB (default 255 255 255), f 76;

-bgcolor <f, f, f>: sets both background colors in RGB (default 255 255 255), f 76;

You can also set send/receive names with the 'send'/'receive' messages or '-send'/'-receive' flags., f 61;

Make sure to escape "\$0" properly with backslashes (as in: "\\\$0")., f 38;

There are 3 modes of display, by default is "cartesian" (mode 1), but you can also set it to "polar" (mode 2). Alternatively, you camn switch both modes off and just have a single point (mode 0). You can set the mode with the 'mode' message or '-mode' flag., f 40;

There's also a grid visibility option (visible by default). You can set it with the 'grid' message or '-grid' flag., f 40;

With the 'clip' message or '-clip' flag, you can set it to clip inside the circle bounds. A value of "1" clips (default) and "0" does not., f 46;

With the 'savestate' message or '-savestate' flag, the GUI operates in 'save state mode', where it saves the state from the last time the patch was saved. Note that this is only useful for patches and not abstractions. For abstractions oyou should use [savestate] instead, and also have a look at [presets]. Unlike iemguis, the value is not output when loading the patch, use [loadbang] for that.;

[circle] is a two dimensional slider GUI abstraction with a circular area (see also [else/slider2d)., f 52;


## `circle-gui`


## `circuit~`

In real life, the circuit would self-oscillate from environment noise. Since our simulation doesn't have environment noise, we need to send a click into it to start the feedback loop, f 53;

You could also build the analog LFO, but this should give basically the same result;

Voltage source for batteries or audio input. volt may be variable like $s0/$s1/etc, f 85;

Voltage probe, use for audio output. This will also lead to the creation of an outlet, f 85;

When assigning numbers, the number 0 has a special meaning as it always represents ground., f 99;

Do note that this simulation is not 100% accurate for every single circuit out there. There is a chance that some circuits just won't work. Also, experimenting with the circuit could lead to loud pops, so be careful!, f 99;

opamp (amp, optional) (supply volt, optional) [in+] [in-] [out] -->, f 67;

bjt (1=pnp, 0=npn) [base] [emitter] [collector] ------------------>, f 67;

diode [anode] [cathode] ------------------------------------------>, f 67;

inductor (henries) [pin1] [pin2] --------------------------------->, f 67;

capacitor (farad) [pin1] [pin2] ---------------------------------->, f 67;

current (ampere) [pin1] [pin2] ----------------------------------->, f 67;

gyrator (gyration resistance) [in+] [in-] [out+] [out-] ---------->, f 67;

triode [plate] [grid] [cathode] ---------------------------------->, f 67;

probe [+] [-] ---------------------------------------------------->, f 67;

voltage (volt) [+] [-] ------------------------------------------->, f 67;

resistor (ohm) [pin1] [pin2] ------------------------------------->, f 67;

jfet (1=pnp, 0=npn) [gate] [source] [drain] ---------------------->, f 67;

mosfet (1=pnp, 0=npn) [[gate] [source] [drain] ------------------->, f 67;

Circuits need to be described as following; You need to assign each component pin a number, based on the wire that is connected to it. Every set of wires that are directly connected to each other, share the same number. They are one network with no resistance between it at all. So if 2 wires touch at the same pin of a component, those wires share the same number. By filling in all the components in your circuit, and assigning the pin numbers like that, you should be able to create a working circuit., f 99;

transformer (ratio) [primary+] [primary-] [secondary+] [secondary]->, f 68;

potmeter (position, 0-1) (max ohm) [+] [wiper] [-] --------------->, f 67;

opamp2 [in+] [in-] [out] [supply+] [supply-] --------------------->, f 67;

pentode [plate] [grid] [cathode] [screen] ------------------------>, f 67;

2N2222, 2N2222A, 2N3904, 2N5088, 2N5089, 2N5210, 2N4401, MPSA13, MPSA18, 2SC1815, 2SC2240, BC107, BC107A, BC107B, BC108A, BC108B, BC108C, BC109B, BC109C, BC549B, BC549C, AC127, AC128, 2N2907, 2N3906, 2N4125, 2N5087, 2SA1015, MPSA43, MPSA56, MPSA92, MPS8599, BC239A, BC239B, BC239C;

Si, Ge, Zener, Red, Green, Blue, 1N4001, 1N914, 1N4148, MA150, 1N4448, 1N4739A, 1N4742A, 1N916, 1N4733, 1N34A;

[circuit~] can also simulate models of specific electrical components, instead of generic ones. The model can specified by passing "-model MODEL_NAME" with the object description. Supported models include:, f 61;

LM308, 3404A, 4558, UA741, OP27, OP42, OP134, AD746, AD826, TL06x, TL07x, TL08x, f 56;

6L6GC-JJ, 6V6GTA, EL34-JJ, EL84-JJ, 6550, KT88-JJ, f 56;

[circuit~] simulates analog circuitry from a text description of the circuit separated by semicolons. Voltage, current, resistance and potmeter can be modulated by an input signal by passing '$sn' as the first (where 'n' is the inlet number indexed from 1). To create an audio input, use a voltage source with a modulatable parameter. An audio outlet will be created for every probe component. The object can be quite CPU intensive!, f 78;

text description of the circuit separated by semicolon. See syntax details and examples above., f 55;


## `click`


## `clock`


## `coeff2pz`


## `colors`


## `comb.filt~`


## `comb.rev~`

Here's the delay lines diagram of [comb.rev~] and equation:, f 34;

The [comb.rev~] object performs a simple linear interpolation for delay time that falls in between sample values., f 61;

1) float - maximum and initial delay time in ms (default 0), f 60;

Use [comb.rev~] as a reverberator, comb filter and delay., f 67;


## `combine`


## `complex`

Several different Lua modules named 'complex' are available, for example: http://philippe.castagliola.free.fr/LUA/complex.html;

If they fail the paths searched will be shown in the Pd console.;


## `compress~`

[compress~] is an abstraction that performs compression. It attenuates an input signal above a given threshold., f 57;


## `conv~`

Change partition size (and latency) in samples. It must be a power of 2! Small partition sizes have less latency and are more expensive. Change it and check balow, f 48;

If no arguments are given, the input sound is bypassed without latency., f 36;

[conv~] performs partitioned convolution. It takes a partition size and Impulse Response table as arguments., f 65;


## `cosine~`

Syncing the phase with control messages is useful for LFOs and control with MIDI. A sync with audio is useful for the "hard sync" technique, where an oscillator is synced according to the frequency of a master frequency., f 56;

The "phase sync" inlet is quite different from the "phase offset" inlet. They are completely independent!, f 43;

Soft sync is also possible with the '-soft' flag or the "soft" message, where it alternates between positive and negative frequencies and sounds less harsh.;

The second inlet resets the phase ands behaves in the same way for control data as objects like [osc~] and [phasor~] in Pd. A number input resets the oscillator and restarts the cycle with an initial phase that corresponds to the input number, so the internal phase is synced to the given value. The phase values are from 0 to 1 and values beyond that are wrapped within this range. The control message reset is meaningful for LFOs.;

Additionally, you can reset the oscillator with an impulse signal. Inputs that are > 0 and <= 1 reset the phase Pd expects an impulse signal for syncing. The impulse values need to be > 0 and <= 1 (otherwise ignored). Because phase is cyclical, the value of 1 represents the "phase 0" of the cycle, where the impulse occurs. Send it impulses above and check the result. Use a multiplier to reset to another phase value.;

The second argument sets an initial phase (or "phase offset"). This is also settable with the third inlet. This allows you to control two oscillators with the same frequency falling in and out of phase. Another feature is phase modulation., f 53;

The phase values are wrapped into the 0-1 range, since the phase cycle is from 0 to 1 (where 1 is also the start of another cycle).;

By default, frequency input is in hertz, but if you use the 'midi' message or '-midi' flag you can change it to MIDI pitch input, where it is not really bound to the 0 to 127 range, neither it has to be integers. This is just like using [mtof~]...;

-midi: sets frequency input in MIDI pitch (default hertz), f 58;

If the oscillator has a multichannel left input, it outputs the same number of channels. If the secondary inlets have a signal with a single channel for sync and phase modulation, the single value is applied to all channels. If a secondary inlet is also a multichhanel signal, then each channel gets its sync or phase deviation value. Note, however, that the number of multichannels in secondary inlets need to match the same number of channels from the left input., f 76;

You can initialize the object with multichannel if you give it a list of frequencies with the -mc flag (you can't set phases though). A list input also works if no signal is connected to set it to multichannel with a list of frequency input., f 49;

-mc <list>: sets multichannel output with a list of frequencies, f 63;

[cosine~] is a cosine oscillator that accepts negative frequencies, has inlets for phase sync and phase modulation. It also has support for multichannels., f 67;


## `count`


## `crackle~`


## `crossover~`


## `crusher.m~`

This is just a wrapper around [crusher~] from ELSE, check it out., f 22;


## `crusher~`

[crusher~] is a bit-crusher/reducer and decimator abstraction based on the objects [quantizer~] and [downsample~], where an input signal is resampled and quantized., f 62;


## `ctl.in`

An argument sets the channel number. If so, only MIDI messages that correspond to that channel are sent. If no channel is given, it loads "0" as the default and the object operates in omni mode, where the objects outputs values from all channels and the channel number is output in the right outlet. You can also change the channel with the right inlet (0 sets to omni)., f 67;

Two arguments set the control and channel number. If MIDI channel is OMNI, all control number messages are sent. But if a control number and channel are set, only values from that control number and channel pass through. A control number of "-1" lets all controllers come out., f 67;

Port number is encoded as the channel number. Channels 1 to 16 are for port 1, channels 17 to 32 is the same as channels 1 to 16 for port 2, channels 33 to 48 represents channels 1 to 16 in port 3, and so on..., f 63;

one value sets sets channel number (default 0 - OMNI). Two values set control number (default -1 - ALL) and channel number., f 54;

The left inlet provides and "external" source of raw MIDI data input. This is needed if you have, for instance, the [midi] object from ELSE reading a MIDI file or something. If, by any chance, you just want the object to receive from this external source and not listen to the internal connected device, you can use the '-ext' flag or 'ext' message, to force only the external input.;

The object automatically listens to whatever is connected as a MIDI device in Pd. So it's like it has a built in [midiin] object feeding its inlet. This is considered to be an "internal" source., f 59;

[ctl.in] extracts MIDI CC information from raw MIDI input or a connected MIDI device., f 61;


## `ctl.out`

1 float sets channel number (default 1). Two floats set control# (default 1) and channel, f 51;

[ctl.out] formats and sends raw MIDI control messages to Pd's MIDI output and its outlet. An argument sets channel number (the default is 1)., f 64;

The object automatically outputs to whatever is connected as a MIDI device in Pd. So it's like it has a built in [midiout] object. If, by any chance, you just want the object to output to the outlet (for feeding a [midi] object or something), you can use the '-ext' flag or 'ext' message., f 61;


## `cusp~`

[cusp~] is a chaotic generator using the difference equation; y[n] = a - b * sqrt(abs(y[n-1]));

If there's a multichannel input, the object outputs the same number of channels. You can initialize the object with multichannel if you give it a list of frequencies with the -mc flag (you can't set phases though). A list input also works if no signal is connected to set it to multichannel with a list of frequency input., f 76;

The output rate of the equation is given in hertz (default: nyquist). Thebject is based on SuperCollider's "CuspN" UGEN and has support for multichannel..;

-mc <list>: sets multichannel output with a list of frequencies, f 63;


## `damp.osc~`

And now for some computer music clichÃ© with random generators..., f 32;

This example shows thw difference between both outputs. The oscillation on the left outlet starts at cosine initial phase, while right one starts at sine., f 41;

Below we have a sequence of impulse values, we can then see how the impulse value determines the amplitude/intensity. A trigger happens when there is a 0 to non 0 transition, and this values determines the maximum amplitude., f 46;

By default, the frequency input is in Hertz, but you can set it to MIDI pitch with the 'midi' message or 'midi' flag., f 44;

You can use lists for a MIDI/control input. It takes note on messages to trigger it (note offs are just ignored) with pitch and velocity (values from 0 to 127 is normalized to 0 to 1 range (float values and values outside this range is possible). You can get note on list messages with objects like [keyboard], [makenote2] and [note.in]., f 52;

[damp.osc~] is an abstraction based [reonant2~] and also very very similar to it (to the point I think it wasn't worth having two objects with such subtle differences). It takes frequency in hertz or midi and a decay time in ms. It is triggered by signals at zero to non zero transitions or by lists at control rate., f 74;


## `datetime`


## `db2lin`


## `db2lin~`

1) float, minimum value (default -100, can be as low as "-inf"), f 63;

[db2lin~] converts amplitude values from deciBel Full Scale (dBFS) to linear. By default, a minimum value of -100 becomes zero - in theory, sero is minus infinity and an argument sets another minimum dB value to correspond to minus ininity. Conversion expression is: amp = pow(10, dBFS / 20). It has support for multichannel signals., f 67;


## `dec2frac`


## `dec2hex`

[dec2hex] converts decimal values to hexadecimal ones. The output is preceded by "0x" and the letters in the hexadecimal values are upper case., f 67;


## `decay2~`

Note: if the attack time is equal to the decay time, then the signal cancels out. Moreover, if the attack time is greater than the decay time, then the polarity is inverted., f 61;

Note also that, unlike in the patch above, the output is normalized according to the impulse. Therefore, if you feed it an impulse of "1", as above, the maximum amplitude will be 1 as well!, f 61;

For last, the overall duration still depends on the decay time. The attack time doesn't really correspond to the time it takes to reach the maximum value (which is always shorter, so it's just an alternative to minimize the harsh attack of [decay~])., f 61;

[decay2~] is based on the difference of two [decay~] objects, like the pacth below, but with a normalized output., f 62;

[decay2~] can also be used with control rate messages, such as bangs and float input. A bang will trigger the object with the last received float input (which is 1 by default).;

[decay2~] is similar to [decay~] but also has an attack time parameter.;


## `decay~`

[decay~] can also be used with control rate messages, such as bangs and float input. A bang will trigger the object with the last received float input (which is 1 by default).;

[decay~] is based on SuperCollider's "Decay" UGEN. It is a one pole filter that creates an exponential decay from impulses. The decay time (in ms) is how long it takes for the signal to decay 60dB. The same filter is also used in other objects from the ELSE library (asr~/adsr~/lag~/lag2~)., f 63;


## `default`


## `deg2rad`


## `delace`

The '-z' flag adds zeros for the case where output lists are not of the same size. This way, zero are added in the place of missing elements., f 50;

[delace] deinterleaves a list according to the number of outlets., f 53;


## `delace~`

[delace~] deinterleaves a multichannel signal according to the number of outlets., f 45;

signals - multichannel signal lists to delace/deinterleave, f 59;

The '-z' flag adds zeros for the case where output multichannel signals are not of the same size in number of channels. This way, zero are added in the place of missing channels to match the size of the multichannel signal with most channels., f 50;


## `delay.m~`

This is just a wrapper around [filterdelay~] from ELSE, check it out., f 22;

This is still a simple module, with no CV input yet, so kinda like a pedal still., f 22;


## `delete`

[delete] deletes one or more elements from an input message. The mid inlet or 1st argument sets the element index indexed from 1 (so 0 means no items are deleted) and negative values are wrapped (so -1 is the last element and so on). The rightmost inlet or 2nd argument sets number of elements to delete. Right outlet outputs deleted item(s) and left outlet the remaining elements from the list. Right outlet sends a bang if index and/or n elements are out of range., f 81;


## `del~`

The -samps flag sets time value to samples instead of ms (default), f 34;

(besides the first optional argument that defines "in" or "out", f 64;

- sets delay line name (optional: default internal name relative to patch), f 74;

Define a delay line and write to it. If neither "in" or "out" is specified as the first argument, the default it [del~ in]., f 64;

The second argument also defines the maximum delay amount a corresponding [del~ out] has., f 44;

For more information on messages and inlet/outlet for both "in" and "out", see:, f 50;

The -samps flag sets time value to samples instead of ms (default), f 34;

(besides the first optional argument that defines "in" or "out", f 64;

We can force the order of execution as this example shows. If we don't do this, it's hard to guarantee we can read from the delay line without having a minimum delay of a block size. This is the same issue with [delwrite~] and [delread~] objects and other objects like [send~]/[receive~]. But the [del~] object provides another structure, because [del~ in] has a dummy outlet to force the order of execution. This way you only need a subpatch to include [del~ out] objects.;

Note that the same "order of execution" issue also applies to [del~]:, f 39;

- sets delay line name (optional: default internal name relative to patch), f 74;

Read from a delay line. It uses a cubic (4 point) interpolation called spline and considers the buffer to be circular (so index 0 to table size is accepted)., f 70;

[del~] sets and writes to a delay line if created as [del~ in] (default) and reads from it (with interpolation) if created as [del~ out]. It's quite similar to [delread~]/[delread4~], but with more features., f 72;


## `detect~`


## `dir`

For example, "open samples" looks for a subdirectory named 'samples' relative to the current directory. More than one level of subdirectories (like "open samples/wav") can be given., f 77;

To open the parent directory you can use "open ..", and "open ." will just reopen the same directory. You can also use "./" or "../", and using "../../" will open the grandparent folder and so on. If you ask for "../sounds", then it looks for a subfolder named "sounds" in the parent directory. This is how Pd handles relative directories in general anyway, so nothing really new here..., f 77;

(If a directory can't be opened, the previously opened remains), f 63;

The 'open' message expects a symbol defining a directory. If the symbol starts with "/" (non windows machines) or "c:" (for instance, in windows machines) then it means the symbol specifies an absolute path. Otherwise, [dir] will look for directories relative to the current directory., f 77;

When using the open message, the rightmost outlet sends an open flag ("1" if the directory has been successfully opened, and 0 otherwise)., f 77;

Opening a directory also loads its contents so you can query for files. If you change the contents of your directory, you need to use the 'reopen' message to reload the direcory's contents., f 79;

Open without a symbol opens a dialog for you to choose a directory., f 37;

(optional) relative directory level, 0 is current patch's directory, 1 is parent's patch's, 2 parent's parent's and so on (default 0), f 54;

If [dir] is used inside an abstraction, the first optional argument sets the abstraction's depth level and can be used to query the parent patch's directory. for instance, "0" (the default) is the current patch level, but "1" sets the default directory to the parent's patch., f 70;

A depth level outside the possible range is ignored. For instance, in this example we ask for the parent's directory, but this patch is not an abstraction, so it loads the patch's directory instead., f 70;

The second symbol argument (which can also be the first, since the first float argument is optional) specifies a directory to open. The directory can be an absolute path, otherwise it's a path relative to the default directory (the current patch's directory, depending on the level argument). For instance, if the default current patch's folder is loaded, a 'x' symbol searches for a 'x' subfolder in it. You can also use '..' to specify a parent patch (more about this syntax in the [pd open] subpatch). Note that '~' expands to the home directory., f 75;

[dir] accesses files from directories. it's an abstraction based on [file] and [else/store]., f 46;

Note that the files are sorted with case sensitivity, in the same way as in the shell/terminal. This means upper case letters are sorted before lower case letters., f 66;

The 'n' message outputs the number of found files in the opened directory in the 3rd outlet. The seek message can search for a file according to a number. If the seek number is greater than the number of files, then the search is wrapped according to the number of files. The seek number is indexed from '1' and clipped to '1' if < 1!, f 74;

The 'next' message increments the seek value and will also wrap according to the number of files. The 'random' message selects a random file from the given possibilities. Note you cannot have a random 'seed' in this case, but you can use a more sophisticated method for that with [rand.i] as in the example below., f 74;

Changing the extension reopens and reloads the directory's contents. Therefore, the contents get updated if they've changed and you don't need a 'reopen' message for that., f 42;

You can ask [dir] to access only files of a certain extension, all files, all files and folder or only folders. This can be set via a flag or the 'ext' message. By default, [dir] accesses all files and folders., f 41;


## `dispatch`

[dispatch] gets a list and sends each element to a given address (order is left to right).;


## `dispatchertest`


## `display`

[display] can display a message just like [print]. The 1st argument specifies a fixed number of characters to display. If "0" or no argument is given, the display automatically resizes according to the input message. If a message is larger than the fixed number of characters, the displayed message is truncated., f 67;


## `dollsym`


## `downsample~`


## `drive.m~`

This is just a wrapper around [drive~] from ELSE (default mode only), check it out., f 22;


## `drive~`

By default (mode 0), the operation mode applies a tanh function:;

Mode 1 is the same as the [expr~] equation below, but for drive factors < 1, the output is input * drive factor. Also, input values outside the -1 to 1 range are clipped.;

The above is somewhat related to this power waveshaper object ===>, f 33;

Mode 2 is the same as the [expr~] equation below, the drive factor sets a threshold (and is limited from 0 to 1). Absolute input values below the threshold are passed through while others are soft clipped. When set to 1, any input above 1 or below -1 is hard clipped., f 69;

[drive~] simulates an analog "soft clipping" distortion by applying non-linear transfer functions.;


## `dropzone`

-dim <f, f>: set horizontal and vertical dimensions (default 127, 127), f 72;

[dropzone] is a drag-and-drop target. If you drag a file or some text onto it, it will output the file path or text content., f 69;


## `drum.seq`

Here's an example on how to use [drum.seq] for a drum pattern sequencer patch. You can also see how some of the messages work (note that tracks and slots are indexed from 1)., f 42;

The import message also sets the number of slots and tracks., f 42;

[drum.seq] provides a drum grid so you can activate cells to represent attacks., f 65;


## `drunkard`


## `drunkard~`


## `duck~`


## `dust2~`

Pseudo random number generators aren't true random number generators. Instead, an algorithm is used to provide a sequence of numbers that seems random. The same sequence can be reproduced if you set a "seed" value, which can be any integer number., f 57;

You can set a seed with the '-seed' flag. If you don't supply it, each object gets its own seed internal seed. If you send a 'seed' message without float, the object also gets a unique seed value., f 57;

Seeds are kept locally, which means that if two [dust2~] objects are seeded the same they will have the same output. Conversely, you can seed the same [dust2~] object twice with the same seed to repeat the output., f 57;

The -ch flag or message sets the number of output channels. This is only meaningful if you have a single channel input., f 42;

If you have a multichannel connection in the frequency input, [dust2~] generates a signal with the same number of channels and the 'ch' message or flag is meaningless. The multichannel input is the density for each output., f 44;

[dust~] is based on SuperCollider's "Dust2" UGEN and outputs random impulse values (from -1 to 1) at random times according to a density parameter. At high frequencies there's a good chance of consecutive non zero values. To the extreme, it becomes white noiset. It has support for multichannels., f 68;


## `dust~`

Pseudo random number generators aren't true random number generators. Instead, an algorithm is used to provide a sequence of numbers that seems random. The same sequence can be reproduced if you set a "seed" value, which can be any integer number., f 57;

You can set a seed with the '-seed' flag. If you don't supply it, each object gets its own seed internal seed. If you send a 'seed' message without float, the object also gets a unique seed value., f 57;

Seeds are kept locally, which means that if two [dust~] objects are seeded the same they will have the same output. Conversely, you can seed the same [dust~] object twice with the same seed to repeat the output., f 57;

The -ch flag or message sets the number of output channels. This is only meaningful if you have a single channel input, either as a float or a signal., f 42;

If you have a multichannel connection or a list input in the inlet, [dust~] generates a signal with the same number of channels and the 'ch' message or flag is meaningless. The multichannel input is the density for each output (you can also use the -mc flag to initialize)., f 44;

[dust~] is based on SuperCollider's "Dust" UGEN and outputs random impulse values (only positive values up to 1) at random times according to a density parameter. At high frequencies there's a good chance of consecutive non zero values. To the extreme, it becomes white noise with a DC offset. It has support for multichannels., f 71;

-mc <list>: sets multichannel output with a list of densities, f 63;


## `e`

[e] can take a [value] name as the second argument or as the first argument (since the first float argument is optional). You can then retrieve this value in another [value] or [var] object or inside an expressionin [expr], f 58;

[e] calculates and outputs the value of 'e'. It receives a multiplier value via the argument or second inlet, which needs to be greater than 0 (otherwise it's considered as 1).;

[e] outputs the result when loading a patch and also when receiving a bang.;


## `echo.rev~`

[echo.rev~] is an echo/reverb abstraction. It only contains feedforward lines and can be used to produce early reflections in a reverb algorithm. But it can also be used on its own., f 62;

You can set the number of echo stages with the first argument and the room size with the second argument/inlet. A typical value is the default. The number of stages are up to 20, but you can see how that generates extreme results., f 62;


## `else`

The ELSE library is mostly a set of separate binaries and abstractions that you can load via "Preferences => Path" or, alternatively, with [declare]. Nonetheless, ELSE must also be loaded as a library, which you must do via [declare] or "Preferences => Startup". See the [declare] example below., f 76;

- ELSE version (major, minor, bugfix, status, status number);

If created as an object, it accepts the "about" message, which prints the same basic library information as when you load the library on the terminal (with version, release date, etc). The object also accepts the "version" message that outputs the version information of ELSE as a list as well as Pd's running version and flavor. Loading the binary as a library is still important for the lua loader and the rest, so you need to do it even if you want to use the [else] object just to check the version., f 81;

Now, finally, there's also a possibility to load [else] as an object, see:;

To use the browser plugin, right click on an empty space on the patch canvas and check entry menus for 'vanilla' and 'else', which will allow you to choose and add the desired object in the spot you right clicked on. The objects are separated by categories and is a nice way to check the objects in ELSE., f 52;

By loading the library, some basic information about the ELSE library is printed on Pd's window, object browser plugins are loaded and you also register a loader that allows Pd externals written in Lua (with the "*.pd_lua" extension)., f 76;


## `envelope~`


## `envgen~`

[envgen~] has a right outlet that sends a status value (1 when the envelope starts and 0 when it ends). This can be useful for different things, but particularly to turn on and off the DSP processing of a subpatch or abstraction with [switch~]., f 62;

You should also check try pd's [clone] object for managing polyphonic synths.;

This is only pertinent for control triggers, such as floats and bangs., f 62;

But if you have an odd number of elements, the first float sets a staring point. In practical terms, it's like this number is a target paired with a "0" duration value., f 36;

If you give [envgen~] just a float as the argument, it initializes the object to output that value as a starting point. You can also use the -init flag instead., f 34;

Being an all purpose line/envelope generator, you can use it to create complex envelope lines as below., f 35;

The line segments in [envgen~] are set in pairs of duration (in ms) and target value (this is the opposite order of the [line] family of objects in Pd Vanilla)., f 36;

A list only sets the envelope. You need a bang to run the envelope., f 36;

You can pause the envelope at any point with the "pause" message, after which the "resume" message restarts the envelope., f 46;

The [envgen~] object works also as an all purpose line generator such as [vline~]. This means you can have multiple line segments and in any range. Note that the maximum number of segments is 256! Use multiple messages and use the right outlet bang to change them if you need more than that., f 49;

A non-zero input triggers the envelope as a "gate on" message and sets an overall gain (which is 1 by default). A zero value is ignored if there's no sustain point., f 57;

When you set a sustain point, with the sustain message or flag, then [envgen~] holds at the given point until it receives a 0 or release message., f 39;

By default, [envgen~] has no sustain point, which means it also doesn't have a release ramp and generates the whole envelope at "one-shot" when triggered., f 57;

An even number of elements makes [envgen~] operate in legato mode, where retriggering restarts the attack ramp from the current amplitude level - check below., f 42;

An odd number of elements sets the first float as a starting point, where a retrigger restarts from this point. Therefore it doesn't operate in legato mode. But you can force a legato mode with the legato message or flag, which ignores this first point - try it below., f 46;

When not in legato mode, you can set a retrigger time in ms with the "retrigger" message or flag. This adds an extra ramp to the starting point and is useful if you do not want to play in legato mode but want to avoid clicks. A small amount such as 10 ms is already usually enough for this non legato effect., f 50;

The time duration is set in ms but is converted to number of samples and is rounded to the nearest integer sample duration. For instance, durations >= 1.5 and < 2.5 is rounded to 2 samples., f 57;

A minimum line size is of 2 samples, meaning that its time duration is 1 sample. Hence, the line is 2 samples long, where the first point is the start and it jumps to the target value in the next sample. A line duration of 0 jumps immediately and multiple lines with 0 duration next to each other get ignored (and values less than 0 are clipped to 0).;

Note that [function] always sends an odd number of elements, so you can use "legato" mode or not, and also set a retrigger time if you will., f 65;

You can use [function] with [envgen~]. Since [function] is always outputting a list you can plug it directly into [envgen~] to set the envelope. Check the help file of [function] for more details on how it works., f 65;

The following subpatch shows how to create "S" like curves:, f 35;

The exponential factor is the same as used in [else/rescale] and [else/rescale~]. Check them out as well:;

The 'exp' message or flag also sets an exponential factor after the duration value. The 'expl' message sets exponential factors for each segment (by default, they're "1" (linear). The 'expi' message sets a single exponential factor. For values >= 0, it's like raising to the power of the given exponential. Negative values are accepted and offer a mirrored/reversed curve. Check below., f 70;

a float sets an initial output value, a list of floats sets the envelope (default 0 0), f 44;

sets an exponential for a line segment specified by the first float indexed from 0, f 51;

sets envelope with an extra exponential element for each segment, f 51;

sets envelope with pairs of duration & target (if odd number of elements, first is start point), f 51;

-exp <list> sets function with an extra exponential element for each segment | -init <float> (default 0) | -retrigger <float> (default 0) | -legato (sets to legato mode on, default is off) | -suspoint <float> (default 0), f 78;

The [envgen~] object can also be triggered by audio. For a one shot envelope (without sustain points), you can use impulses to trigger it., f 47;

But a gate is needed for envelopes with sustain points. Note that float input is not ignored when there's a signal connection and can also retrigger the envelope., f 47;

When the gate is on, you can also retrigger the envelope with impulses in the right inlet., f 29;

The object has multichannel support. In which case the right outlet is non functional. If [envgen~] has a multichannel left input, it outputs the same number of channels, one for each gate signal. The right inlet must have the same number of channels if bigger than 1, in which case each channel gets is retriggered independently, otherwise the single channel input retriggers all channels., f 46;

The status ----> outlet considers all channels, so it waits until all are finished to turn it off., f 16;

[envgen~] is an envelope (and an all purpose line) generator (here it creates a 1000 ms line to 1 and then a 500 ms line to 0). It has multichannel support., f 34;


## `eqdiv`


## `equal`

[equal] compares lists and outputs 1 if they're the same or 0 if they're not. The arguments set the right input., f 65;


## `eq~`

Change the parameters and check the filter response below. The graph considers a sample rate of 44.1Khz.;

The equation is from the "Cookbook formulae for audio EQ biquad filter coefficients" by Robert Bristow-Johnsonc [1], and it is: y[n] = a0 * x[n] + a1 * x[n-2] + a2 * x[n-2] + b1 * y[n-1] + b2 * y[n-2];

a0, a1, a2, b1 and b2 are calculated as a function of frequency 'f' in hz, 'Q' and 'db' gain as follows; w = f * PI/nyquist; G = pow(10, db/40); alphaQ = sin(w) / (2*Q); b0 = alphaQ/G + 1; a0 = (1 + alphaQ*G) / b0; a1 = a1 = -2*cos(w) / b0; a2 = (1 - alphaQ*G) / b0; b1 = 2*cos(w) / b0; b2 = (alphaQ/G - 1) / b0;;

[1] found in https://webaudio.github.io/Audio-EQ-Cookbook/audio-eq-cookbook.html, f 80;

2) float - resonance (default 1), either in 'Q' (default) or 'bw', f 65;

By default, the resonance parameter is the filter 'q', but you can also set it as bandwidth in octaves. This is done with the -bw flag.;

Alternatively, you can switch from 'q' to 'bw' with the message methods.;

[eq~] is a 2nd order parametric equalizer filter, it can be used as a peak and a notch filter.;


## `errors`


## `euclid`


## `expand~`

[expand~] is an abstraction that performs expanding. It attenuates an input signal below a given threshold.;


## `f2s~`

[float2sig~] (or [f2s~] for short) is an abstraction that converts floats to signals or lists to multichannel signals. The conversion is smoothened by a ramp time in ms., f 67;


## `factor`


## `fader~`

There are two "constant power" curves, which have a crossing point at -3dB., f 33;

We have the "sin" (sine) function above and a "sqrt" (square root) function below., f 33;

The "sin" function is 1/4 of the cycle of a sine function., f 33;

The "sqrt" function is the same as extracting the square root of the input., f 33;

As a compromise between the functions that cross between -3 and -6dB, we have a crossing point at -4.5 dB., f 37;

This can be achieved with a geometric mean between such functions. Here we have a mean between the "hann" and the "sin" function above, and a mean between the "lin" and "sin" function below., f 37;

There are two "constant voltage" curves, which have a crossing point at -6dB., f 33;

We have the "hann" function above and a linear transfer function below, f 33;

The "hann" function is half the cycle of a "cosine" function., f 33;

The "lin" function does nothing, it is the same as the input., f 33;

The default curve is "quartic", which is the same as raising the input to the power of 4, f 31;

Open the subpatch below for more details on the fading curves available, f 32;

[fader~] is a waveshaper. It takes input from 0 to 1 and uses internal lookup tables for 7 different fading curves.;

fade types <quartic, sin, sqrt, hann, lin, hannsin, linsin> (default: quartic), f 47;

fade types <quartic, sin, sqrt, hann, lin, hannsin, linsin>, f 47;

Here's how you can combine different fade in and out curves with a crossfading slider., f 27;


## `fbdelay~`

Negative values of t60 generate negative feedback of the same absolute value as its absolute input., f 60;

[fbdelay~] is just simple feedback delay line, whose diagram and equation is:, f 34;

By default, the 'a' coefficient is calculated in [fbdelay~] from the decay time parameter (t60) and delay time (D) according to the expression: a = exp(log(0.001) * D/t60).;

The [fbdelay~] object performs a 4 point interpolation (just like ffdelay~) for delay time that falls in between sample values.;

By default, the reverberation/decay time is in "t60", which is the time in ms that the impulse takes to fall 60dB in energy. You can change this parameter to a gain coefficient value with the third argument, where a non zero value sets to "gain mode" or with the -gain flag. You can also change that with the "gain" message., f 72;

Use [fbdelay~] for delay effects, reverberation and comb filtering. By default, you can set a delay time and a reverberation/decay time in ms ("t60"), which is the time the impulse takes to fall 60dB in energy (but you can change this parameter to a gain coefficient)., f 67;

sets delay size (default 1000 ms or first argument's value if given), f 49;

Alternatively, with the -samps flag, you can set it to operate in time units specified by the number of samples. In the same way, this affects both delay time and delay size., f 64;

By default, all time units in [fbdelay~] is in ms. This affects not only the delay time, but also the delay size., f 64;

By default, the delay size is 1 sample, but if you give it an argument, it sets both the delay time and also the delay size., f 64;

If you need a larger delay size than specified by a first argument, you can use the -size flag/message., f 64;

You can freeze the delay line with the 'freeze' message, where zero freezes, zero unfreezes. When frozen, it stops writing into it. Note that unlike [ffdelay~], the input still goes through., f 52;


## `fbsine2~`


## `fbsine~`

Syncing the phase with control messages is useful for LFOs and control with MIDI. A sync with audio is useful for the "hard sync" technique, where an oscillator is synced according to the frequency of a master frequency., f 44;

The "phase sync" inlet is quite different from the "phase offset" inlet. This means that the are completely independent., f 43;

Additionally, you can reset the oscillator with an impulse signal. Inputs that are > 0 and <= 1 reset the phase Pdexpects an impulse signal for syncing. The impulse values need to be > 0 and <= 1 (otherwise ignored). Because phase is cyclical, the value of 1 represents the "phase 0" of the cycle, where the impulse occurs. Send it impulses above and check the result. Use a multiplier to reset to another phase value.;

The third inlet resets the phase and behaves in the same way for control data as the phase sync inlet of other objects like [else/sine~]. A number input resets the oscillator and restarts the cycle with an initial phase that corresponds to the input number, so the internal phase is synced to the given value. The phase values are from 0 to 1 and values beyond that are wrapped within this range.;

The phase values are wrapped into the 0-1 range, since the phase cycle is from 0 to 1 - where 1 is also the start of another cycle., f 36;

The third argument sets an initial phase (or "phase offset"). This is also settable with the fourth inlet. In such a way, you have two objects with the same frequency falling in and out of phase. Another feature is phase modulation.;

The feedback parameter controls how much of the signal output is fed back to the phase input of [fbsine~]. The phase input is normalized from 0-1. For a detailed implementation, please check the [pd fbsine] subpacth, where the same code/algorithm is implemented as a pd patch., f 62;

[fbsine~] has no limits for the feedback values, and negative values are also allowed, but note that this parameter easily turns the output into chaotic noise. Common values are usually in the -1 to 1 range., f 62;

For more details, you can check the subpatch [pd fbsine~ filtered~] for a patch implementation of this oscillator with the filter included., f 67;

See how you can go to a feedback index of 0.5 and still hold a tonal character when the filter is on. Then test without the filter for comparison., f 67;

[fbsine~] has a filter in the feedback loop that is turned on by default. This is a simple mean average filter that takes the average of 2 samples and cuts very high frequencies. This filter has been used in some yamaha synthesizers to smoothen out the output of a self modulating oscillator. FM8, by Native Instruments (a DX7 clone) uses it too., f 67;

[fbsine~] is a sinusoidal oscillator with phase modulation feedback. Like [else/sine~], it accepts negative frequencies, has inlets for phase modulation, phase sync and multichannel support. Additionally, it has a feedback value input., f 61;

If [fbsine~] has a multichannel left input, it outputs the same number of channels. If the secondary inlets have a signal with a single channel for feedback, sync and phase modulation, the single value is applied to all channels. If a secondary inlet is also a multichhanel signal, then each channel gets its feedback, sync or phase deviation value. Note, however, that the number of multichannels in secondary inlets need to match the same number of channels from the left input., f 70;


## `fdn.rev~`

-time <float>: t60 reverberation time in seconds (default 4), f 64;

[fdn.rev~] uses a householder reflection feedback matrix. The main parameters are the reverberation decay time (t60), which is the time it takes to decrease 60dB in seconds. The damping parameter controls the decay of higher frequencies, the higher the damping, the less higher frequencies reverberate., f 47;

A list of values sets the matrix. The size of the list sets the size of the matrix and needs to be a multiple of 4! Each float sets the delay time for each delay line., f 47;

The set message sets the size of the matrix with the first element, the two extra elements set the minimum and maximum delay times. By default they are spaced linearly, but they can be exponentially spaced with the "exp" message., f 47;

[fdn.rev~] is a feedback delay network reverberator which can be used for late reflections (a.k.a reverb tail). The main parameters are: decay time (t60) and high frequency damping., f 66;


## `ffdelay~`

A couple of examples with some delay effects fun you can have :, f 63;

The [ffdelay~] object uses a cubic (4 point) interpolation called 'spline', but between 0 and 1, it uses a regular linear interpolation., f 47;

sets delay size, which defines the delay's maximum time (default 1000 ms or argument's value if given);

By default, all time units in [ffdelay~] is in ms. This affects not only the delay time, but also the delay size., f 64;

Alternatively, with the -samps flag, you can set it to operate in time units specified by the number of samples. In the same way, this affects both delay time and delay size., f 64;

By default, the delay size is 1000 ms, but if you give it an argument, it sets both the delay time and also the delay size., f 64;

If you need a larger delay size than specified by a first argument, you can use the -size flag/message, f 64;

You can freeze the delay line, in which case it stops writing into it. Non zero freezes, zero unfreezes., f 47;


## `filterdelay~`

[filterdelay~] is a high level delay unit that goes thgouh a resonant lowpass filter, a soft clipper and a DC filter. The processed delay output is also fed back into the delay line., f 70;

The freeze parameter stops recording the input into the delay line and the feedback value is set to 1 (if >= 0) or -1 (if negative). Delay time modulation and filtering is still possible., f 50;

The filter is a 2nd order lowpass filter much like [lowpass~]. Note that it gets bypassed when the cutoff is 20 khz or more. The resonance parameter is from 0 to 1, where at 0 there's no resonance. Since the filter output can be fed back into the delay line, the resonance behaves as an increasing feedback parameter around this center frequency. This is minimized by a soft clipping stage (an atan function just like in the [drive~] object)., f 50;

The feedback parameter can be positive or negative and there are no restrains, hence you can have values over 1 or below -1, but the soft clipping also takes care of high feedback values. A DC block filter is also present to prevent other artifacts from the processing., f 50;

For a better idea of this module diagram, check this version in a patch:, f 41;

This patch is quite similar to [filterdelay~] and is given here for didactical reasons. The only thing missing is the freeze toggle., f 27;


## `flanger.m~`

This is just a wrapper around [flanger~] from ELSE, check it out., f 22;

this is still a simple module, with no CV input yet, so kinda like a pedal still., f 22;


## `flanger~`


## `float2bits`


## `float2sig~`

[float2sig~] (or [f2s~] for short) is an abstraction that converts floats to signals or lists to multichannel signals. The conversion is smoothened by a ramp time in ms., f 67;


## `floor`


## `floor~`

[floor~] is a floor math function for signals. It has support for multichannel connections.;


## `fm~`

The object has multichannel support. If the left input has more than one channel, it outputs the same number of channels in both outlets. If the secondary inlets have a signal with a single channel, the single value is applied to all channels. If a secondary inlet is also a multichhanel signal, then each channel gets its own value. Note, however, that the number of multichannels in secondary inlets need to match the same number of channels from the left input., f 70;

[fm~] is a simple frequency modulation unit consisting of a pair of sinusoidal oscillators, where one modulates the frequency input of another. The modulation frequency is set as a ratio of the carrier and the modulation index is multiplied by this resulting frequency. The object has support for multichannels., f 66;


## `fold`

[fold] folds between a low and high value. This is like a mirroring function, where an out of bounds value folds back until it is in the given range., f 68;

floats set fold's range, 2 floats sets minimum and maximum. No arguments loads default values (0 and 1). 1 float sets maximum value (and lowest value is set to 0). If the maximum value is less than the minimum, the maximum becomes the minimum and vice-versa.;


## `fold~`

floats set fold's range, 2 floats sets minimum and maximum. No arguments loads default values (-1 and 1). 1 float sets maximum value (and lowest value is set to 0). If the maximum value is less than the minimum, the maximum becomes the minimum and vice-versa.;

If the object has a multichannel left input, it outputs the same number of channels. If the secondary inlets have a signal with a single channel, the single value is applied to all channels. If a secondary inlet is also a multichhanel signal, then each channel gets its min or max value. Note, however, that the number of multichannels in secondary inlets need to match the same number of channels from the left input., f 76;

[fold~] folds between a low and high value. This is like a mirroring function, where an out of bounds value folds back until it is in the given range. It has multichannel support.;


## `fontsize`


## `format`

A symbol may be received in any inlet that corresponds to a %s variable, but if sent to another type, a conversion error is given in Pd's window. A float will give an error only if no variables are given (which is probably an error since it makes the object useless).;

In the example below we have a space escaped by a backslash, so we format a symbol that contains a space.;

The symbol argument in [format] is used to format a message. Inlets are created for any possible variables (like %d or %f) - note that symbol variables (%s) are initialized empty and numeric variables (all of the rest) are initialized as "0".;

As usua in Pd, a list input in the left inlet spreads the values to the following inlets., f 34;

The correct exact result ('4294967294') is only possible in Pd compiled with double precision (aka Pd64), f 56;

%%: is converted to a literal "%". This prevents it from being interpreted as a pattern. In the example below, we have '%d' which is an integer specifier as we'll see later. this specifier gets the value of the "100" float input. Next we have "%%", which becomes a literal "%" in the output., f 39;

By the way, you can also perform the opposite conversion (from a character symbol to a float) by using the [list fromsymbol] object., f 48;

This format specifier allows you to convert from a float (actually integers from 0 to 255) to a character symbol. A symbol input is converted to '0' (and this is also true for any other specifier besides '%s' and '%p')., f 48;

Both '%d' and '%i' are the same. This format specifier allows you to insert a signed (negative or positive) decimal integer into a symbol. Note that floats with a decimal point are truncated., f 61;

Note that there's a default precision of 6 digits after the decimal point and before 'e'/'E'. You can change this precision as shown later. Also note that trailing zeros (zeros to the right of the decimal point) are always shown. This means you're always aware of the given precision., f 52;

This format specifier allows you to insert a float number with scientific notation into a symbol. The '%e' or '%E' pattern specify respectively whether the exponential character is lower (e) or upper (E) case. Also, it prints 'NAN' and 'INF' in all CAPS for %A, while '%a' uses lowercase., f 53;

Note that this is the format pattern used by Pd to display numbers in comments, message boxes and also GUI boxes and iemgui's [nbx] (with the same default precision of 6 significant digits). Also, it prints 'NAN' and 'INF' in all CAPS for %A, while '%a' uses lowercase., f 69;

Unlike %f' and '%e'/'%E', this format specifier doesn't show trailing zeros. Therefore, values without significant digits after the decimal point come out looking like integers (as there's not dot at the end). The scientific notation is used in negative form if the exponent value is lower than '-4'. For the positive form, it's used only if the exponent is equal to or higher than the precision value (again this is '6' by default and can be changed later). The '%g' or '%G' pattern specify respectively whether the exponential character is lower (e) or upper (E) case. Also, it prints 'NAN' and 'INF' in all CAPS for %A, while '%a' uses lowercase., f 69;

This format specifier allows you to insert an unsigned (only positive) octal integer into a symbol. Floats are truncated., f 42;

This format specifier allows you to insert a symbol, but note it also works for float messages. You can set a precision as shown later, but there's no default precision., f 52;

This format specifier is the same as "%d" or "%i", but it is unsigned (only positive). Floats are truncated to integers., f 44;

This format specifier allows you to insert a signed (only positive) hexadecimal integer into a symbol. Floats are truncated. The '%x' or '%X' specify respectively whether the the characters are lower or upper case., f 51;

For "%x" and "%X", the number is preceded by "0x" (if %x) or "0X" (if %X)., f 43;

For %g and %G, the decimal point and trailing zeroes are not removed. Note that this flag can be combined with '+' or 'space' flags., f 36;

The '#' (hash) flag presents an alternate form of some numeric types. For "%o", the number is preceded by a "0".;

For "%a" and "%A", the number has a decimal point even if there is no fractional part., f 43;

The width field can alternatively take the optional preceding '0' flag, which fills the extra characters with leading zeroes instead of spaces., f 52;

You can also combine the width field with the preceding +/space/# flags where pertinent., f 46;

The width field takes an integer that sets the number of minimum characters and adds spaces to fill them (justifying the format to the right). This works for all types but the floating point numbers '%f' and '%e'/'%E' ('%g'/'%G' works). An optional '-' flag justifies to the left., f 55;

For symbol srtrings (%s), the precision sets a maximum character limit. Below, we have a maximum of 4 characters, hence, the symbol "abcde" gets truncated. There's no default precision by the way., f 58;

In this case, the width field can be preceded to set a minimum of characters filled with spaces. The example below also makes use of the optional '-' flag to justify it to the left., f 48;

For integer types ('%d'/'%i'/'%o'/'%u'/'%x'/'%X'), the precision field does not set a maximum number of characters. Instead, it sets a fixed number of digits and adds zeroes to the left as a fill. This is slightly different than setting a width field with a '0' flag. The difference is only observed for numbers of different signs as below (and without the "+" flag). Note how the width field will suppress a zero to include a minus (-) character., f 64;

For '%g', the precision field sets the maximum number of significant digits, not counting leading zeros. Note that there's a default of 6 digits. Also note that this affects the resolution and can cause the number to be rounded. This setting also specifies how it chooses to show the scientific notation when positive, as the exponent value needs to be needs to equal to or higher than the precision number (for negative values, the scientific notation is always chosen if the exponent is less the '-4')., f 78;

In the case of '%f' and '%e'/'%E', the precision field sets the maximum number of digits to the right of the decimal point. The same is actually true for '%a'/'%A', but it's the number of hexadecimal digits instead. Note that there's a default of 6 digits. Also note that this affects the resolution and can cause the number to be rounded., f 82;

The precision field behaves differently according to the type (strings, integers of floats). The syntax of this field is specified by a "." and is followed by the precision number. See subpatches below for the examples., f 51;

The "+" flag prepends a plus sign for positive signed numeric types (%d/%i/%e/%E/%f/%g/%G). The space (which can be used if escaped by a backslash) uses a space for positive values., f 47;

The types can be preceded by optional fields. The sequence syntac is <flags><width><precision><type>. See details below:;

By the way, the range precision for signed integers according to its bits size is -2Ë(bits-1) to 2Ë(bits-1) -1, whereas for unsigned is 0 to 2Ë(bits) -1 - for example, for 32 bits we have:, f 62;

Signed: -2Â³Â¹ (-2.147.483.648) to 2Â³Â¹ - 1 (2.147.483.647), f 57;

The type modifiers (aka length specifiers) are placed before the format specifier and adjust how the data is to be interpreted regarding its size. This is only for integer and float types., f 66;

For integer types (%d, %i, %x, %o, '%u'/'%x'/'%X'), the default is 32-bit precision. You can only represent integers correctly with this precision if you're using Pd compiled for 64 bits (aka Pd64). This is because Pd uses 32 bit floats otherwise, which can only represent integers up to 2^24., f 66;

For float types (%a/%A, %f/%F, %e/%E and %g/%G) the default is 64-bit precision, but it gets truncated to 32-bit if you're using the single precision version of Pd. Again, you can only truly represent these values in double precision if you're using Pd64., f 66;

The 'h' length modifier is used for integers to specify shorter precisions. You should probably not need this anyway since this is better suited for representing and matching this specifier to a data type and in Pd these can't be shorter than 32-bit. A single 'h' specifies 16-bit precision and 'hh' is 8-bit precision., f 66;

On the other hand, the 'l' modifier specifies a higher precision of 64-bit for integers, which Pd can't represent even in Pd64 as the maximum integer is 2^53 in this case., f 66;

The 'L' modifier is for float types and specifies a higher precision than 64-bits, but Pd has a limit of 64-bits in Pd64 and 32 bits otherwise - hence, it shouldn't be used., f 66;

These are all the valid patterns available, note they are in in the C-Style of the printf function, but in a limited set. You can also use flags "+" and "#", plus a precision field. See examples below for more details., f 61;

This format specifier allows you to represent a floating point number in hexadecimal form. The '%a' or '%A' specify respectively whether the the characters are lower or upper case. Also, it prints 'NAN' and 'INF' in all CAPS for %A, while '%a' uses lowercase. The number is preceded with "0x" (if %a) or "0X" (if %A). The 'p' character represents the power of 2 exponent (so it separates the fractional hexadecimal part from the exponent in base 2).;

This format specifier allows you to format a float into a symbol without scientific notation. Note that there's a default precision of 6 digits after the decimal point. You can change this precision as shown later. As in 'e'/'E', trailing zeros are always shown. The '%F' variant just prints 'NAN' and 'INF' in all CAPS, while '%f' uses lowercase., f 50;

float/symbol atoms to format variables, or a bang to define an empty string, f 51;

atoms that may contain '%' variables (obrigatory, no default), f 36;

[format] formats symbols similarly to [makefilename], but it accepts more than one '%' variable, where each corresponds to an inlet., f 53;


## `frac.add`


## `frac.mul`


## `frac2cents`


## `frac2dec`


## `free.rev~`


## `freeze~`

[freeze~] is an abstraction based on [sigmund~] (analysis & ressynthesis). It contains a bank with oscillators., f 58;


## `freq.shift~`


## `freq2midi`


## `function`

Here's an example on how to use [function] with [function~]. In this case it's probably desired to have a constant output to update the function internally.;

Note also that you can have any kind of breakpoints function and also draw something like a waveform in the range from -1 to 1 as below!;

Here's an example on how to use [function] with [envgen~]. Check the help file of [envgen~] for more details on how it works., f 47;

You can also set different minimum/maximum points min/max messages or flags, but the values are clipped to the given minimum and maximum points of the lines so the points are never outside the graph bound., f 78;

The [function] serves as an all purpose line generator interface. This means you can have line segments in any range. By default, the range is from 0 to 1, but if a list input is given with points outside that range, the minimum and maximum points are updated accordingly so the line segments fit into the GUI display., f 78;

The duration message or flag resizes the duration of each line segment so the overall duration is the same as the given value in ms., f 36;

The resize message resizes the graph bounds to the min/max values., f 35;

In this example we convert the function output to signals with a ramp and use it to control the amplitude. But you can just use it as a control message instead., f 70;

Additionally, you can also use the "i" message, followed by a float. This float value is then tereated as the actual index in the table. The number of index is the same as the envelope dursation. A linear interpolation is performed with both a float input and using 'i'., f 70;

Alternatively, you can have a float input from 0 to 1 into [function] and they'll be treatet as indexes and the amplitude value will then be output. This is useful if you want to control a function with a slider input, for instance. Another option is to use [line] to drive it or [phasor]., f 70;

You can also set send/receive names with the 'send'/'receive' messages or '-send'/'-receive' flags. Make sure to escape "\$0" properly with backslashes (as in: "\\\$0") when using messages. Setting these to 'empty' removes the send/receive symbols., f 67;

Note that when you set a receive or send symbol, the corresponding inlet/outlet does not get drawn when you're in edit mode. This is an indicative that the object has a send or receive symbol., f 66;

[function] is a breakpoints function GUI, mainly used with [function~] or [envgen~]. You can click and drag on it or send it lists., f 59;

An odd list of at least 3 floats sets the envelope function. The syntax is the same as the [function~] object (point1, period, point2, period, point3, etc.) - an output is then generated with the list values for [envgen~] or [function~]. A bang forces an output of the stored line function.;

Please get into and out of edit mode to see how [function] creates an inlet and an outlet when you're in edit mode. Note that when you set a receive or send symbol, the corresponding inlet/outlet does not get drawn when you're in edit mode. This is an indicative that the object has a send or receive symbol., f 58;

A list of 2 floats sets the point number specified by the first number (counting from 0) with the value specified by the second number of the list., f 55;

You can also generate an output via the interface, when you click on a point and drag it around (if shift is pressed, the point is moved with fine tuning). A point is removed if you click on it and hit delete. Click anywhere in the graph where there's not a point and you create a new one., f 61;

Click on a dot to move it. If shift is pressed, it moves with fine tuning. If you click anywhere else than a dot, a new dot/line is created. You can delete a dot if you click on a dot and press delete key., f 26;

With the 'savestate' message or '-savestate' flag, the GUI operates in 'save state mode', where it saves the state from the last time the patch was saved. Note that this is only useful for patches and not abstractions. For abstractions you should use [savestate] instead, and also have a look at [presets]. Unlike iemguis, the value is not output when loading the patch, use [loadbang] for that.;

-height <float> (default 100) | -width <float> (default 200) | -send <symbol> (default none) | -receive <symbol> (default none) | -bgcolor <f, f, f> | -fgcolor <f, f, f> | -resize <float> | -min <float> (default 0) | -max <float> (default 1) | -savestate | -set <list> (default 0 1000 0)., f 67;


## `function~`


## `gain2~`

You can also set a ramp time for the slider value to act on the signal input, the default is 20 ms and the minimum is 5 ms. This also affects the slider value set via the 'set' message., f 40;

[gain2~] has 3 scaling modes for its slider (the default is "quartic"). You can set a linear gain multiplier, which needs to be greater than zero and also represents the maximum linear gain achieved., f 40;

The graph to the left shows us how the scaling modes work. A linear scaling doesn't really do anything, the input is the same as the output. We have then two non linear modes:;

dB: This mode adopts a decibel scale with a range of 100 dB (using the [dbtorms~] object)., f 55;

Quartic (default): This mode just gets the slider values to the power of 4 (so, for instance, an input slider value of 0.5 becomes 0.125)., f 57;

The gain value is a simple multiplier to the output value of the slider and determines the maximum linear gain output regardless of the scaling mode. For example, "2" will output the double of the input amplitude, and "0.5" half of it. This is useful if your input isn't loud enough, if it is too high or even if you're using multiple [gain~] and they're all adding up to the same output.;

-max <float>: sets max gain (needs to be > 0, default 1), f 75;

-mode <float>: sets scaling mode: 0 (quartic, default), 1 (dB) or 2 (linear), f 76;

[gain2~] is a convenient stereo gain abstraction, so you can adjust a stereo signal's gain. It has controls for ramp time, maximum gain, scaling mode and init., f 55;

With the 'savestate' message or '-savestate' flag, the GUI operates in 'save state mode', where it saves the state from the last time the patch was saved. Note that this is only useful for patches and not abstractions. For abstractions oyou should use [savestate] instead, and also have a look at [presets]. Unlike iemguis, the value is not output when loading the patch, use [loadbang] for that.;

If you send the 'learn' message or "alt+click" the object, it learns a MIDI controller so you can control the gain. You can also forget it with the 'forget' message or "alt+shift+click".;

The object has built in [sum~] objects, so it takes and mixes MC input., f 30;


## `gain~`

[gain~] has 3 scaling modes for its slider (the default is "quartic"). You can set a linear gain multiplier, which needs to be greater than zero and also represents the maximum linear gain achieved., f 40;

You can also set a ramp time for the slider value to act on the signal input, the default is 20 ms and the minimum is 5 ms. This also affects the slider value set via the 'set' message., f 40;

The graph to the left shows us how the scaling modes work. A linear scaling doesn't really do anything, the input is the same as the output. We have then two non linear modes:;

dB: This mode adopts a decibel scale with a range of 100 dB (using the [dbtorms~] object)., f 55;

Quartic (default): This mode just gets the slider values to the power of 4 (so, for instance, an input slider value of 0.5 becomes 0.125)., f 57;

The gain value is a simple multiplier to the output value of the slider and determines the maximum linear gain output regardless of the scaling mode. For example, "2" will output the double of the input amplitude, and "0.5" half of it. This is useful if your input isn't loud enough, if it is too high or even if you're using multiple [gain~] and they're all adding up to the same output.;

-mode <float>: sets scaling mode: 0 (quartic, default), 1 (dB) or 2 (linear), f 76;

[gain~] is a convenient mono gain abstraction for adjusting a signal's gain. It has controls for ramp time, maximum gain, scaling mode and init. It has support for multichannel signals., f 61;

With the 'savestate' message or '-savestate' flag, the GUI operates in 'save state mode', where it saves the state from the last time the patch was saved. Note that this is only useful for patches and not abstractions. For abstractions you should use [savestate] instead, and also have a look at [presets].;

If you send the 'learn' message or "alt+click" the object, it learns a MIDI controller so you can control the gain. You can also forget it with the 'forget' message or "alt+shift+click".;


## `gate2imp~`


## `gatehold`

In this example we have a gate controlling two independent envelopes (one that controls the phase modulation index and another that controls the amplitude). The envelope that controls the amplitude has its sustain period enlarged by 500 ms because of the [gatehold~] object.;

[gatehold] allows one gate to have a different duration to control a separate parameter., f 59;

[gatehold] holds a gate value for a certain amount of time (specified in ms) after the gate has closed. If a new gate starts before the hold time is finished, the object is retriggered., f 70;


## `gatehold~`

In this example we have a gate controlling two independent envelopes (one that controls the phase modulation index and another that controls the amplitude). The envelope that controls the amplitude has its sustain period enlarged by 500 ms because of the [gatehold~] object.;

[gatehold~] allows one gate to have a different duration to control a separate parameter.;

[gatehold~] holds a gate value for a certain amount of time (specified in ms) after the gate has closed. If a new gate starts before the hold time is finished, the object is retriggered. The object has support for multichannel signals., f 55;


## `gaterelease`

[gaterelease] allows you to release one gate in your patch while you still hold another. [gaterelease] releases a gate value after a given amount of time (specified in ms) after the gate has opened. If the gate is closed before the release time, the object is reset. If the release time is 0 or less, the object is bypassed., f 75;


## `gaterelease~`

[gaterelease~] allows you to release one gate in your patch while you still hold another. [gaterelease~] releases a gate value after a given amount of time (specified in ms) after the gate has opened. If the gate is closed before the release time, the object is reset. If the release time is 0 or less, the object is bypassed. The object has support for multichannels, f 68;


## `gaussian~`

The width parameter controls the width of the bell shape. The higher the value, the narrower the shape is, so it's closer to an impulse. Usable values are usually from 0 to 1, but can be higher in the case of low frequencies., f 62;

Syncing the phase with control messages is useful for LFOs and control with MIDI. A sync with audio is useful for the "hard sync" technique, where an oscillator is synced according to the frequency of a master frequency., f 44;

The "phase sync" inlet is quite different from the "phase offset" inlet. This means that the are completely independent., f 43;

Additionally, you can reset the oscillator with an impulse signal. Inputs that are > 0 and <= 1 reset the phase Pdexpects an impulse signal for syncing. The impulse values need to be > 0 and <= 1 (otherwise ignored). Because phase is cyclical, the value of 1 represents the "phase 0" of the cycle, where the impulse occurs. Send it impulses above and check the result. Use a multiplier to reset to another phase value.;

The third inlet resets the phase and behaves in the same way for control data as the phase sync inlet of other objects like [else/sine~]. A number input resets the oscillator and restarts the cycle with an initial phase that corresponds to the input number, so the internal phase is synced to the given value. The phase values are from 0 to 1 and values beyond that are wrapped within this range.;

The phase values are wrapped into the 0-1 range, since the phase cycle is from 0 to 1 - where 1 is also the start of another cycle., f 36;

The third argument sets an initial phase (or "phase offset"). This is also settable with the fourth inlet. In such a way, you have two objects with the same frequency falling out and back in sync. Another feature is phase modulation., f 54;

-midi: sets frequency input in MIDI pitch (default hertz), f 58;

-mc <list>: sets multichannel output with a list of frequencies, f 63;

By default, frequency input is in hertz, but if you use the 'midi' message or '-midi' flag you can change it to MIDI pitch input, where it is bound to the 0 to 127 range (but they don't have to be integers) - this is kinda like using [mtof~]...;

If the oscillator has a multichannel left input, it outputs the same number of channels. If the secondary inlets have a signal with a single channel for sync and phase modulation, the single value is applied to all channels. If a secondary inlet is also a multichhanel signal, then each channel gets its sync or phase deviation value. Note, however, that the number of multichannels in secondary inlets need to match the same number of channels from the left input., f 76;

You can initialize the object with multichannel if you give it a list of frequencies with the -mc flag (you can't set phases though). A list input also works if no signal is connected to set it to multichannel with a list of frequency input., f 49;

[gaussian~] is a gaussian oscillator. It accepts negative frequencies, has inlets for width, phase sync and phase modulation. It also has support for multichannels., f 70;


## `gbman~`

[gbman~] is a gingerbread man map chaotic generator, the output is from the difference equation => y[n] = 1 + abs(y[n-1]) - y[n-2], but the output is filtered to remove DC offset and rescaled for a proper audio range. This object was first based on SuperCollider's "GbmanN" UGEN. The given reference is: Devaney, R. L. "The Gingerbreadman." Algorithm 3, 15-16, Jan. 1992, f 76;

The output rate of the equation is given in hertz, and the initial value is the nyquist frequency. By default, the initial feedback values of y[n-1] and y[n-2] are 1.2 and 2.1, respectively, but can be changed via arguments or as a list input., f 76;

If there's a multichannel input, the object outputs the same number of channels. You can initialize the object with multichannel if you give it a list of frequencies with the -mc flag (you can't set phases though). A list input also works if no signal is connected to set it to multichannel with a list of frequency input., f 76;

-mc <list>: sets multichannel output with a list of frequencies, f 63;


## `gcd`


## `gendyn.m~`

This is just a wrapper around [gendyn~] from ELSE, check it out., f 29;

Controls; - Bandwidth in cents (up and down center input frequency; - 'n' number of points in the waveform; - interpolation type; - maximum frequency step (percentage of bandwisth); - maximum amplitude step (percentage)., f 30;


## `gendyn~`

You can set the maximum amplitude step with the 'amp_step' message or '-amp_step' flag. This is also set in percentage, where 100% means that the amplitude deviation is up to a value of '2'. Note that if the amplitude goes out of the -1 to 1 bounds, it is folded back - same is true for frequency deviation outside the frequency range. The higher the amplitude step, the closest the sound is to white noise., f 69;

By default, the points in the waveform are linearly interpolated (1) from one point to the next. You can set it to no interpolation (0) or cosine interpolation (2) with the 'interp' message or 'interp' flag. Cosine makes more of a difference in lower frequencies, linear creates triangle like shapes and no interpolation is squarish., f 69;

You can set the number of points in the waveform with the 'n' message or '-n' flag. The higher the number, the brighter the sound is. Each point will then change (both in amplitude and frequency) according to a random walk as in the [brown]/][brown~] objects. The maximum amplitude and frequency steps are given as percentages., f 69;

The frequency percentage is in respect to a given bandwidth above and below a center frequency, which is set via a float or signal input. The bandwidth can be either in hertz or cents. By default, the center frequency is 440 and the bandwidth is 1200 cents. If the bandwidth is set in cents, the steps are then logarithmic, otherwise it's linear. Use the 'bw' message or flag to set the bandwidth and the 'cents' message to set if the bandwidth is in cents or not., f 69;

Alternatively, you can set the minimum and maximum frequencies with the 'frange' message or '-frange' flag. This sets the frequency steps to be linear. Hence the bandwidth is calculated in hertz and you can change the center frequency., f 69;

The frequency deviation step is set via the 'freq_step' message or '-freq_step' flag. This is the maximum random step set in percentage, where 100% means that the frequency deviation is up to the frequency range (maximum frequency minus minimum frequency)., f 69;

Check the patch implementation and how the parameter value affects the transfer function:, f 41;

Check the patch implementation and how the parameter value affects the transfer function:, f 41;

The function behaves like a transfer function for the uniform distribution. The parameter goes from a linear transfer function as the minimum value (which is much like a uniform distribution) to a curve that favors values in the middle., f 41;

Check the patch implementation and how the parameter value affects the function., f 41;

Check the patch implementation and how the parameter value affects the transfer function:, f 41;

By default, the random number is generated via a uniform distribution, but you can set it to specific distribution functions below, which are used for step generation for both amplitude and frequency. All functions have a parameter and the details for each are given in the subpatches below., f 79;

Similar to cauchy, the parameter for a logistic distribution goes from a linear transfer function as the minimum value (which is much like a uniform distribution) to a curve that favors values in the middle., f 50;

Check the patch implementation and how the parameter value affects the function., f 41;

You can set the distribution and parameters with the 'dist' message of '-dist' flag, which take 4 float arguments. The first two set the distribution number and function parameter for the amplitude, the next two for the frequency. The distribution numbers are: 0 (uniform), 1 (cauchy), 2 (logistic), 3 (hyperbcos), 4 (arcsine) and 5 (expon)., f 79;

Pseudo random number generators aren't true random number generators. Instead, an algorithm is used to provide a sequence of numbers that seems random. The same sequence can be reproduced if you set a "seed" value, which can be any integer number., f 52;

You can set a seed with the '-seed' flag. If you don't supply it, each object gets its own seed internal seed. If you send a 'seed' message without float, the object also gets a unique seed value., f 27;

Seeds are kept locally, which means that if two [gendyn~] objects are seeded the same they will have the same output. Conversely, you can seed the same [gendyn~] object twice with the same seed to repeat the output., f 52;

[gendyn~] implements "Dynamic Strochastic Synthesis" based on Xenakis' 'GenDyn' algorithm. The waveform has a given number of points (linearly interpolated by default). The period of each point and its value changes according to a random walk (a.k.a. brownian motion) with given distributions., f 79;

- non zero (default) sets bandwidth in cents instead of hz, f 59;

-n <f> | -bw <f> | -cents <f> | -frange <f f> | -freq_step <f> | -amp_step <f> | -interp <f> | -seed <f> | -dist <f f f f> |, f 64;


## `get~`

[get~] gets one or more channels from a multichannel connection. The channels are indexed from 1 (0 or less gives "none", the max channel number value is clipped to the input's channel size). You can give it lists to build or remap the signal arbitrarily like you'd do with dollar signs in a message., f 77;


## `giga.rev~`

- damp: Controls the high frequency damping and affects the response of the early reflections and the decay of the late reflections. The higher the value, the less intense is the reverb., f 60;

- bw: Controls the input bandwidth, which is like a "tone" control. Small values cause a smaller frequency range to be processed. In general, the effect of this control can be heard in the treble band. Smaller values cause a "muffled" and less bright reverb., f 60;

- late: Controls the late reflections level (a.k.a. "reverb tail"). It determines the amount of the hall effect of the reverb and determines how intense the reverb appears to be., f 60;

- wet: Controls a master gain for both early and late reflections., f 60;

- early: Controls the early reflections level, which are similar to slapback echoes. Though they are not responsible for the typical hall effect generally linked with reverb, they contain lots of acoustic information about the setup in which the sound occurs. Generally, early reflections about 10-20 dB higher than the late reflections gives a typical reverb effect. By setting it considerably smaller than the late reflections level, you can simulate a distance between the source and the listener.;

- size: Controls the overall characteristics and influences both the early and late reflections. The initial maxsize is 300 squared meters, but if initialize the object with a room size bigger than that (with the -size flag), it becomes the maximum limit. You can specify an even larger maximum size with the -maxsize flag.;

- decay: Controls the approximate time decay duration of the reverb. In general, it affects the late reflections;

This example patch brings a few presets to the right. You can also open [pd controls] to test each parameter independently and read a bit more about how they affect the reverb unit., f 42;

[giga.rev~] is based on the well known "Gigaverb" algorithm by Juhana Sadeharju., f 64;

-maxsize <float>: maximum room size in square meters (default 300), f 66;


## `glide`


## `glide2`


## `glide2~`

[glide2~] is just like [glide~] but has distinct ramp times for both up and down.;

You can set exponential factors, much like as in [rescale~]. Check it out as well., f 33;

If [glide2~] has a multichannel left input, it outputs the same number of channels. If the secondary inlets have a single channel for the up/down glide times, the single value is applied to all channels. If a secondary inlet is also a multichhanel signal, then each channel gets its own glide time value. Note, however, that the number of multichannels in secondary inlets need to match the same number of channels from the left input., f 65;


## `glide~`

You can set exponential factors, much like as in [rescale~]. Check it out as well., f 33;

If [glide~] has a multichannel input, it outputs the same number of channels. If the right inlet has a single channel for the glide time in ms, the value is applied to all channels. If the right inlet is also a multichhanel signal, then each channel gets its own time value. Note, however, that the number of multichannels in the right inlet needs to match the same number of channels from the left input., f 65;

[glide~] generates a glide/portamento from its signal input changes. The glide time in ms. There's support for multichannel signals., f 53;


## `gmean`

[gmean] creates a list of geometric means. It takes a start point, an end point and the number of steps from start to end., f 64;

The number of steps is the output list length - 1 and represents the number of values until reaching the end. The minimum number of steps is "1"., f 64;


## `grain.live~`

Here we have different messages with all the setable parameters. The pan range is from -1 (left) to 1 (right) and the position in the delay line is set proprtionally (0 is the beginning of the delay line and 1 is the end of the delay line). Note that the length end of the delay line can only be set at creation time with the '-length <float>' flag. By default, the length is 5000 ms as in this example. Therefore "0" means no delay and "1" means 5000 ms delay., f 70;

The 'rev' message sets the probability in percentage that the grain will be played backwards, so, for 0, we have all grains played forward. For 50, we have a 50/50 chance, and for 100, all grains are reversed., f 70;

Try some of the presets and also try dfferent parameters from the settings here, where we can change to synchronous mode and also the density (number of grains).;

By default, we have an asynchronous mode, and that means that the interval between grains are random. On the other hand, synchronous mode spaces the grains equally within a cloud event. This is more noticeable if you have less density. You can set the object to sync mode at creation with the -sync flag., f 58;

By default, the envelope is a sine shape, like the default in the [envelope~] object. You can set other envelope function types, namely 'tri', 'hann' and 'gauss' (also like in the [envelope~] object). The gaussian envelope takes a float argument that sets the width., f 48;

You can also give it a list of values in the same syntax as taken by [function~] (which is used internally). This syntax is also given by the [function] GUI object., f 48;

The autotune message retunes the transposition values, see [else/autotune2] for reference., f 28;

[grain.live~] is a live input granulator that generates clouds of grains.;

scale <list> - scale to autotune to in cents (default equal temperament), f 74;

autotune <f> - non-zero autotunes to a given scale (default 0), f 74;

transp <f, f> - sets min/max transpositin in cents (default -1200 to 1200), f 75;

size <f, f> - sets min/max grain sizes in ms (default 50 to 450), f 73;

amp <f, f> - sets min/max amplitude values (default 0.1 to 1), f 72;

pan <f, f> - sets left/right pan boundaries (default -1 to 1), f 72;

pos <f, f> - sets min/max position in delay line (default 0 to 1), f 72;

rev <float> - sets probability in % of grain being reversed (default 0), f 73;

env <any> - envelope type (sin, hann, tri, gauss) or function list, f 71;

float - number of grains in the event (default 16 min 1, max 256), f 67;

-n <float> (number of grains) | -dur <f> | -size <f, f> | -picth <f, f> | -autotune <f> | -pan <f, f> | -amps <f, f> | -scale <list> | -base <f> | -rev <float> | -env <any> | -length <f>: delay length in ms (default 5000) | -sync, f 78;


## `grain.sampler~`

scale <list> - scale to autotune to in cents (default equal temperament), f 74;

pan <f, f> - sets left and right pan boundaries (default -1 to 1), f 72;

autotune <f> - non-zero autotunes to a given scale (default 0), f 74;

The autotune message retunes the reading speed to match a given scale, see [else/autotune] for reference., f 32;

Here we have different messages with all the setable parameters. The pan range is from -1 (left) to 1 (right) and the position in the sample is set proprtionally (0 is the beginning of the sample and 1 is the end). The 'rev' message sets the probability in percentage that the grain will be played backwards, so, for 0, we have all grains played forward. For 50, we have a 50/50 chance, and for 100, all grains are reversed., f 65;

Try some of the presets and also try dfferent parameters from the settings here, where we can change to synchronous mode and also the density (number of grains).;

By default, we have an asynchronous mode, and that means that the interval between grains are random. On the other hand, synchronous mode spaces the grains equally within a cloud event. This is more noticeable if you have less density. You can set the object to sync mode at creation with the -sync flag., f 58;

If a sample has a dfferent sample rate than Pd's, you can set it with the 'sr' message so the player adjusts the reading speed., f 49;

By default, the envelope is a sine shape, like the default in the [envelope~] object. You can set other envelope function types, namely 'tri', 'hann' and 'gauss' (also like in the [envelope~] object). The gaussian envelope takes a float argument that sets the width., f 48;

You can also give it a list of values in the same syntax as taken by [function~] (which is used internally). This syntax is also given by the [function] GUI object., f 48;

[grain.sampler~] is a sample based granulator that generates clouds of grains., f 78;

size <f, f> - sets min/max grain sizes in ms (default 50 to 450), f 73;

pos <f, f> - sets min/max grain position (default 0 to 1), f 72;

amp <f, f> - min/max amplitude values (default 0.1 to 1), f 72;

transp <f, f> - sets min/max transposition in cents (default -1200 to 1200), f 75;

rev <float> - sets probability in % of grain being reversed (default 0), f 73;

sr <float> - sets sample rate for reading the buffer (default Pd's), f 72;

env <any> - envelope type (sin, hann, tri, gauss) or function list, f 71;

n <float> - number of grains in cloud event (minimum 1, maximum 256), f 70;

-n <f> | -t <symbol> (table name) | -dur <f> | -size <f, f> | -transp <f, f> | -pan <f, f> | -sync | -env <any> | -amps <f, f> | -pos <f, f> | -autotune <f> | -scale <list> | -rev <float>, f 79;

float - number of grains in cloud event (minimum 1, maximum 256), f 64;


## `grain.synth~`


## `gran.player~`

(optional) channels (default 1 if no file is given, or sound file's if given, max 64), f 44;

opens a file with the symbol name (no symbol opens dialog box) and starts playing, f 52;

float - <1> is the same as "start", "0" is the same as "stop", f 61;

reload - reloads the file into the buffer and starts playing, f 62;

set <symbol> - sets a file to open (needs a reload message), f 68;

range <f, f> - sets sample's playing range (from 0 to 1), f 68;

If you give an optional float argumewnt as the first argument, it specifies the number of channels. If no float argument and no sound file are given, then the default number of channels is 1 (mono). But if the first optional argument is not given and a file name is given, then the number of channels is the same as the sound file's. The maximum number is 64 channels.;

If you have a file with less channels than specified (like a mono file in a stereo buffer player), the extra channels are silent. Conversely, a file with more channels than specified (like a stereo file in a mono buffer player) has its remaining channels ignored.;

[gran.player~] is like [player~] but provides independent time stretching and pitch shifting via granulation (just like [pvoc.player~]). Like [player~], it is based on [sfload] and support the same file formats (check its help file)., f 78;


## `graph~`

[graph~] is a very simple but convenient abstraction for visualizing audio signals.;


## `gray~`

seed <float> - a float sets seed, no float sets a unique internal, f 65;

Pseudo random number generators aren't true random number generators. Instead, an algorithm is used to provide a sequence of numbers that seems random. The same sequence can be reproduced if you set a "seed" value, which can be any integer number., f 52;

Seeds are kept locally, which means that if two [gray~] objects are seeded the same they will have the same output. Conversely, you can seed the same [gray~] object twice with the same seed to repeat the output., f 52;

You can set a seed with the '-seed' flag. If you don't supply it, each object gets its own seed internal seed. If you send a 'seed' message without float, the object also gets a unique seed value., f 52;

[gray~] generates noise based on "gray code" or reflected binary code (RBC), which results from flipping random bits (sot is is based on a pseudo random number generator algorithm.). "Gray Code" is named after Frank Gray, the owner of the patent of gray codes. This type of noise has a high RMS level relative to its peak to peak level. The spectrum is emphasized towards lower frequencies. It has support for multuchannels., f 79;

The -ch flag or message sets the number of output channels. You can also use the '-mc' flag., f 33;


## `group`

A bang message sends the remaining stored elements that haven't reached the group size yet. So you can send a bang afterwards to force an output. A group size of zero keeps regrouping indefinitely until a bang is given., f 67;

[group] groups messages according to a group size. When the input is smaller than the group size, it needs to reach the group size before it's sent out. If the input list is bigger than the group size, the remainder gets grouped in further lists., f 67;


## `hann~`


## `hello`

Right click to open the source file if your system has a known application for it., f 43;

This is a simple help file for the 'hello' external written in lua that is loaded with the [pdlua] library. This is just an example on how you can provide help files for your externals. Just create a "objectname-help.pd" file and it'll be called when you right click on it and ask for help., f 62;


## `henon~`


## `hex2dec`

[hex2dec] converts hexadecimal values to decimal ones. It takes symbols whose format allows lower and upper case letters and can also include "0x" or "0X" prefixes (necessary in the case of lists and arguments to avoid confusion with floats, which are ignored). List and symbol selectors aren't necessary., f 71;


## `highpass~`

This filter has zeroes fixes at +1 and -1 on the z-plane, which means both 0Hz and Nyquist are always filtered out.;

Change the parameters and check the filter response below. The graph considers a sample rate of 44.1Khz.;

a0, a1, a2, b1 and b2 are calculated as a function of center frequency 'f' in hz and 'q' as follows;;

omega = f * PI/nyquist; alphaQ = sin(omega) / (2*q); b0 = alphaQ + 1; a0 = (1+cos(omega)) / (2*b0); a1 = -(1+cos(omega)) / b0; a2 = (1+cos(omega)) / (2*b0); b1 = 2*cos(omega) / b0; b2 = (alphaQ - 1) / b0;;

The equation is from the "Cookbook formulae for audio EQ biquad filter coefficients" by Robert Bristow-Johnsonc [1], and it is: y[n] = a0 * x[n] + a1 * x[n-2] + a2 * x[n-2] + b1 * y[n-1] + b2 * y[n-2];

[1] found in https://webaudio.github.io/Audio-EQ-Cookbook/audio-eq-cookbook.html, f 80;

By default, the resonance parameter is the filter 'q', but you can also set it as bandwidth in octaves. This is done with the -bw flag.;

Alternatively, you can switch from 'q' to 'bw' with the message methods.;

2) float - resonance (default 1), either in 'Q' (default) or 'bw', f 65;


## `highshelf~`

Change the parameters and check the filter response below. The graph considers a sample rate of 44.1Khz.;

The equation is from the "Cookbook formulae for audio EQ biquad filter coefficients" by Robert Bristow-Johnsonc [1], and it is: y[n] = a0 * x[n] + a1 * x[n-2] + a2 * x[n-2] + b1 * y[n-1] + b2 * y[n-2];

a0, a1, a2, b1 and b2 are calculated as a function of frequency 'f' in hz, slope 'S' and 'db' gain as follows; w = f * PI/nyquist; G = pow(10, db/40); alphaS = sin(w) * sqrt((G*G + 1) * (1/S - 1) + 2*G); b0 = (G+1) - (G-1)*cos(w) + alphaS; a0 = G*(G+1 + (G-1)*cos(w) + alphaS) / b0; a1 = -2*G*(G-1 + (G+1)*cos(w)) / b0; a2 = G*(G+1 + (G-1)*cos(w) - alphaS) / b0; b1 = -2*(G-1 - (G+1)*cos(w)) / b0; b2 = -(G+1 - (G-1)*cos(w) -alphaS) / b0;;

[1] found in https://webaudio.github.io/Audio-EQ-Cookbook/audio-eq-cookbook.html, f 80;


## `hip.bw~`


## `histogram`

[histogram] creates an internal table that you can export, but you can also use the left output to treat the data and write into an external table., f 50;

If you set a table name to [histogram] you can use it in [rand.d], for instance., f 41;

embed <float> - non zero embeds histogram data with the patch, f 64;

[histogram] records into a table how many times it received a positive integer number (treated as indexes, floats are truncated). A list input is treated as MIDI note messages and only note ons are recorded., f 68;


## `hot`


## `hz2rad`

[hz2rad] converts a frequency in Hertz to "Radians per Sample" - which depends on the patch's sample rate (sr). The conversion formula is; rad = (hz * 2*pi / sr)., f 71;


## `ikeda~`


## `impseq~`

When receiving a signal trigger (0 to non-0 transition) or a bang, [impseq~] sends an impulse from a given sequence.;

Impulses can be used as rhythmic triggers. As such, a sequence value of "0" works as a rest.;

The [impseq~] object can be used to convert floats to impulses., f 35;


## `impulse`


## `impulse2~`

A pulse width of 0 has the smallest size (the first sample is equal to 1, the second is equal to -1 and the rest is 0), while a pulse width of 1 has the largest (the first sample is 1, the last sample is -1 and the others are 0).;

The phase values are wrapped into the 0-1 range, since the phase cycle is from 0 to 1 (where 1 is also the start of another cycle).;

The third argument sets an initial phase (or "phase offset"). This is also settable with the fourth inlet. This allows you to control two oscillators with the same frequency falling in and out of phase. Another feature is phase modulation., f 53;

-midi: sets frequency input in MIDI pitch (default hertz), f 58;

-mc <list>: sets multichannel output with a list of frequencies, f 63;

Syncing the phase with control messages is useful for LFOs and control with MIDI. A sync with audio is useful for the "hard sync" technique, where an oscillator is synced according to the frequency of a master frequency., f 56;

The "phase sync" inlet is quite different from the "phase offset" inlet. They are completely independent!, f 43;

Soft sync is also possible with the '-soft' flag or the "soft" message, where it alternates between positive and negative frequencies and sounds less harsh.;

Additionally, you can reset the oscillator with an impulse signal. Inputs that are > 0 and <= 1 reset the phase Pd expects an impulse signal for syncing. The impulse values need to be > 0 and <= 1 (otherwise ignored). Because phase is cyclical, the value of 1 represents the "phase 0" of the cycle, where the impulse occurs. Send it impulses above and check the result. Use a multiplier to reset to another phase value.;

The third inlet resets the phase ands behaves in the same way for control data as objects like [osc~] and [phasor~] in Pd. A number input resets the oscillator and restarts the cycle with an initial phase that corresponds to the input number, so the internal phase is synced to the given value. The phase values are from 0 to 1 and values beyond that are wrapped within this range. The control message reset is meaningful for LFOs.;

By default, frequency input is in hertz, but if you use the 'midi' message or '-midi' flag you can change it to MIDI pitch input, where it is bound to the 0 to 127 range (but they don't have to be integers) - this is kinda like using [mtof~]...;

If the oscillator has a multichannel left input, it outputs the same number of channels. If the secondary inlets have a signal with a single channel for sync and phase modulation, the single value is applied to all channels. If a secondary inlet is also a multichhanel signal, then each channel gets its sync or phase deviation value. Note, however, that the number of multichannels in secondary inlets need to match the same number of channels from the left input., f 76;

You can initialize the object with multichannel if you give it a list of frequencies with the -mc flag (you can't set phases though). A list input also works if no signal is connected to set it to multichannel with a list of frequency input., f 49;

A variant of [else/impulse~], [impulse2~] (or [imp2~] for short) is a two-sided impulse oscillator that accepts negative frequencies, has inlets for pulse width, phase sync and phase modulation. It also has support for multichannels., f 67;


## `impulse~`

Since it deals with negative frequencies, the impulse is only sent when leaping from one phase cycle to the next (in either direction). How this happens is probably better understood if you check the [pimp~] object and its help file - [pimp~] is a variant of [imp~] which also carries an extra outlet for phase output.;

[imp~]/[impulse~] may be used as an oscillador but also to periodically trigger processes such as with [sh~] below.;

The second inlet resets the phase ands behaves in the same way for control data as objects like [osc~] and [phasor~] in Pd. A number input resets the oscillator and restarts the cycle with an initial phase that corresponds to the input number, so the internal phase is synced to the given value. The phase values are from 0 to 1 and values beyond that are wrapped within this range.;

Syncing the phase with control messages is useful for LFOs and control with MIDI. A sync with audio is useful for the "hard sync" technique, where an oscillator is synced according to the frequency of a master frequency., f 50;

The "phase sync" inlet is quite different from the "phase offset" inlet. This means that the are completely independent., f 43;

Additionally, you can reset the oscillator with an impulse signal. Inputs that are > 0 and <= 1 reset the phase Pdexpects an impulse signal for syncing. The impulse values need to be > 0 and <= 1 (otherwise ignored). Because phase is cyclical, the value of 1 represents the "phase 0" of the cycle, where the impulse occurs. Send it impulses above and check the result. Use a multiplier to reset to another phase value.;

Soft sync is also possible with the '-soft' flag or the "soft" message, where it alternates between positive and negative frequencies., f 50;

The second argument sets an initial phase (or "phase offset"). This is also settable with the third inlet. This allows you to control two oscillators with the same frequency falling in and out of phase. Another feature is phase modulation., f 53;

The phase values are wrapped into the 0-1 range, since the phase cycle is from 0 to 1 (where 1 is also the start of another cycle).;

The [impulse~] object (or [imp~] for short) is an impulse oscillator that accepts negative frequencies, has inlets for phase sync and phase modulation. It also has support for multichannels., f 70;

By default, frequency input is in hertz, but if you use the 'midi' message or '-midi' flag you can change it to MIDI pitch input, where it is not really bound to the 0 to 127 range, neither it has to be integers. This is just like using [mtof~]...;

If the oscillator has a multichannel left input, it outputs the same number of channels. If the secondary inlets have a signal with a single channel for sync and phase modulation, the single value is applied to all channels. If a secondary inlet is also a multichhanel signal, then each channel gets its sync or phase deviation value. Note, however, that the number of multichannels in secondary inlets need to match the same number of channels from the left input., f 78;

You can initialize the object with multichannel if you give it a list of frequencies with the -mc flag (you can't set phases though). A list input also works if no signal is connected to set it to multichannel with a list of frequency input., f 51;

-midi: sets frequency input in MIDI pitch (default hertz), f 58;

-mc <list>: sets multichannel output with a list of frequencies, f 63;


## `initmess`


## `insert`


## `interpolate`


## `iterate`

[iterate] splits a message to individual elements (floats/symbols)


## `keyboard`

Note that the velocity depends on where you click on the vertical axis. The lower you click, the higher the velocity is., f 48;

Nonetheless, you can set a normalized velocity value for all clicks with the 'norm' message. It takes values from 0 to 127, so if you set to a value different than zero, that value is set for all generated note on messages. but if you set it to '0', then the there's no normalization and velocity depends where you click., f 48;

You can set send/receive names with the -send/-receive flags or the 'send'/'receive' messages - make sure to escape "\$0" properly with backslashes (as in: "\\\$0"). Setting these to 'empty' removes the send/receive symbols., f 67;

This way you don't need to use both inlets and just rely on the built in receive symbol, f 45;

Note that inside the properties window you don't need to escape the special characters of "$" and also spaces, both of which are allowed. Also note that other special characters are not allowed, such as braces, backslashes, commas and semicolons., f 69;

Note that when you set a receive or send symbol, the corresponding inlets/outlet does not get drawn when you're in edit mode. This is an indicative that the object has a send or receive symbol., f 41;

-width <float>: width in pixels (default 17) | -height <float>: height in pixels (default 80) | -oct <float>: number of octaves (default 4) | -lowc <float>: number of lowest C (default 3 - that is "C3") | -tgl sets to toggle mode (default non toggle) | -norm <float>: velocity normalization value (default 0) | -send <symbol>: sets send symbol (default 'empty') | -receive <symbol>: sets receive symbol (default 'empty') |, f 77;

For instance, below, we have$0 used in the send symbol. Using something like "\$1" is also possible and useful if you're using the object in an abstraction, then you can load a value passed as an argument into a parameter., f 80;

This is the default [keyboard] object. Please get into and out of edit mode so you can see how the [keyboard] object creates two inlets and an outlet when you're in edit mode. The bluish "C" note indicates it is C4 (Midi note "60")., f 62;

Note that when you set a receive or send symbol, the corresponding inlets/outlet do not get drawn when you're in edit mode. This is an indicative that the object has a send or receive symbol., f 80;

Also note that all the parameters that you can set by inserting a value into a field in the properties window can also load dollar sign arguments (\$0,$1,$2, and so on). Namely, these parameters are: key width, height, normalization, and send/receive symbols., f 80;

This example uses [spread] to split notes from [keyboard] so you can route them to different synths., f 46;

[keyboard] takes MIDI notes and also generates them via clicking., f 27;

Try clicking and dragging, it also works and slides through chromatically!, f 52;

hint: you can also create a list of <note, velocity> and send to the left inlet. In the same way as other pd object, this distributes to both inlets.;

In this example [keyboard] displays randomly generated notes and driving 4 voices. Also see that each voice subpatch has [adsr~]'s status outlet to control the DSP status for that subpatch - open and check it. You should also try pd's [clone] object for managing polyphonic synths as well as [synth~] from ELSE., f 72;

In toggle mode, you need to click on a note to set it On or Off. Dragging doesn't work., f 43;

When in toggle mode, you can flush hanging Note On messages. Note that the flush message also flushes hanging notes from messages from the inlets., f 43;

In regular nome ("non toggle: mode), you can also toggle notes by pressing the shift key when you click on the notes to set them on and off. This way you can have the two options. The flush message also flushes hanging notes from shift clicking., f 65;

The 'on' message expects a list of MIDI pitches that are set as note on messages with a velocity of 127, while 'off' send note of messages for its list of pitches., f 69;

If you're on toggle mode you can click on the notes that are on to set them off. If not in toggle mode you can use shift+click instead., f 69;

The 'play' message is like the 'on' message preceded by 'flush', so it flushes hanging notes and sets the pitches on the given list On., f 35;

The 'play' message is like the 'on' message preceded by 'flush', so it flushes hanging notes and sets the pitches on the given list On., f 35;


## `keycode`

[keycode] outputs key codes from your keyboard based on their physical location, so it is layout independent (but please don't change layout after loading Pd and the object, this is problematic specially on Windows.. The right outlet outputs the code and the left output the key status (1 for pressed / 0 for released). The codes correspond to USB HID usage tables from <https://github.com/depp/keycode>., f 82;


## `keymap`

Note that some hardware keyboards can't correctly handle several simultaneous key presses. This means you can't go crazy with polyphony. One way to deal with this is with the 'toggle' mode, where a key press turns the note on and a second press is required to turn it off., f 57;

[keymap] maps your computer keyboard to MIDI pitches and generates note on/off messages when keys get pressed and released. It works for any keyboard layout. It does not work when in edit mode and autorepeated keys get filtered., f 71;

The map has 2 rows, a lower one from the letter 'z' (in qwerty) that corresponds by default to C3 ('s' being C#3). The other row starts from 'q' and is an octave higher (C4 by default, and the number '2' is C#4)., f 71;


## `keypress`

In toggle mode you have "1" for when the learned key is pressed and 0 when it is released., f 40;

[keypress] uses key presses of a single computer keyboard key by sending a bang or a toggle. You can set the key symbol as an argument or ask the object to "learn" a pressed key (useful for keys like "shift" and stuff), which is then saved as an argument. Note that autorepeated keys are filtered! Key presses in edit mode are also filtered!, f 77;

Whenever the abstraction learns something new, you'll be prompted to save your patch when you close it so it gets saved. After sending "learn", press a key to teach the object., f 42;


## `knob`

[knob] has an exponential and log feature just like the [rescale] object. For more details, check the help file of [rescale]. Note that sometimes you may need to use [rescale] as well, like when knob receives data from MIDI controllers (see example to the left)., f 42;

The example to the left has an initial quartic function setting and a range from 0 to 1 (well suited for setting a volume gain, for instance). There are 2 ticks to indicate start and end position., f 48;

In log mode, the range cannot reach or cross a value of 0! This mode supersedes the 'exp' mode, so the 'exp' value is ignored., f 68;

The log mode is well suited for setting things like frequencies. To the right we have a frequency range that is from 110 to 1760, which covers 4 octaves from A2 to A6. The mid point is A4 (440 hz)., f 33;

You can change the exp value via message or set via a flag. Note that setting The 'exp' factor to '1', '0' or '-1' makes it linear., f 48;

You can set to log mode with the 'log' message or flag. You can also set it via the properties window., f 33;

Note that you can also use arrows to navigate the knob and in this case the step change is discrete as well., f 13;

Besides the angular range, you can also set an angle offset to shift the start position. The example below is similar to the above, but the shift is 90 degrees the motion is circular, there is an arc and we have an outline. Additionally, note that there's a canvas in the background so you can set yet a 4th color in the scheme., f 41;

You can set to discrete mode with a number of steps and also show tick marks for them as below (where we have 11 steps from 0 to 10 and the numbers are comments). Note that, when displayed, the first and last ticks are a bit thicker and wider., f 44;

You can see that how when the knob reaches the mid point of the knob you have '440' as the mid value between 110 and 1760! You can also double click to go directly to this mid value. Other usages include a frequency or gain multiplier, from 0.5 to 2 for instance, where 1 is the mid point., f 33;

sets the arc background color in hexadecimal or RGB list (default: #afafaf);

sets background color in hexadecimal or RGB list (default: #dfdfdf), f 56;

sets foreground color in hexadecimal or RGB list (default: #000000), f 56;

When in edit mode, [knob] shows its inlet/outlet. The inlet will always be hidden if you have a receive symbol, same with the outlet if you have a send symbol. You can set a send symbol above to send messages to a matching [receive] object. A receive symbol makes [send] objects communicate to it., f 57;

If you set send/receive names to "empty" then the symbols are cleared and inlet/outlet are shown again (same if you give an actual empty symbol). Note you need to escape dollar signs with backslashes to set send receive names via messages or flags, but not via properties!, f 57;

The 'param' message sets a symbol name before the value, so you can directly control a parameter in an object without the need to pass through a message box. An "empty" symbol clears it., f 40;

<-- Unlike iemguis, [knob] doesn't have a 'label' but you can use [note] for that, f 27;

Use "var' to set a variable and send values to variables in [value] or [var] objects. Note that you also can do that if you have a send name that matches a variable name, but with the 'var' symbol you bypass sending to a [receive] object and just set the variable directly. Like send/receive, you need to escape dollar signs in messages.;

This is particularly useful if you have a 'param' name, in which case you cannot send values to a [value] object with the same 'send' name, for instance., f 60;

HINT: use [var] with [savestate] objects to save the current state of GUIs.;

Use the "learn" message or "Ctrl+Click" ("command+click" on mac) for "MIDI learn". This mechanism sends a bang to a given send name followed by "-learn". Below, the object has a "\$0-knob2" send name, so it goes to "\$0-knob2-learn". You can use this to connect to a [midi.learn] object that actually offers a "MIDI Learn" mechanism. Try it below. Anyway, even if you're not sending values anywhere, the send name is needed for this. The MIDI forget follows the same mechanism and is triggered by the 'forget' message or "Shift+Ctrl+Click". Note that the shortcuts don't work in 'read only' mode., f 59;

The 'size' message sets size in pixels. The bgcolor, arccolor and fgcolor parameters set background, arc background and foreground color with a hex symbol or a list of RGB values (3 values from 0 to 255)., f 35;

By default, the angular range is 320 degrees. The object also draws an 'arc' by default with its own color, which is useful to display the initial and final position. You can change this with the 'arc' or 'angle' messages, properties or flags. A full 360 degree is possible and the arc is then useful to differentiate from the fully turned down (background color) to the turned up [knob] (foreground color). The default range is from 0 to 127, but you can change that in the same way. A float sets and outputs values, which get clipped to the [knob]'s range. A 'set' message only sets the value (no output)., f 65;

You can also set the motion to 'circular' and in this case the [knob] follows the angular position of your mouse motion, which allows for a 'looped' or 'infinite' knob (which makes more sense if the angular range is 360 degrees). Using arrow keys also make it loop around., f 56;

Click and dragging on the [knob] works both in vertical and horizontal axis - dragging down or left decreases values, while dragiing up or right increases them. If shift is pressed before clicking, the mouse dragging or arrow keys increment/decrement by a factor of a hundredth., f 55;

The 'load' message sets the initial value for when the object is loaded. A 'load' message without float saves the current value as the load value. In 'savestate' mode, when you save the patch, the current knob's value becomes the 'load' value. Note that the [savestate] object is needed if you use [knob] in an abstraction. In 'loadbang' mode (default), the load value is output at load time., f 65;

by default, the knob has an outter square area, with the same background color. There's a second mode without the square or any outline, in which the knob circle increases in size. Use the "square 0" message or the '-nosquare' flag to change the display mode. You can also set it via properties. When you don't have the square, note that when you are in edit mode the [knob] shows just a square outline around as to indicate you're in edit mode and where you can connect the object. Inlets and outlets are hidden in run mode but also appear in edit mode., f 55;

double click or alt+click (or option+click on mac) to restore to arc start state (same as 'reset'), f 25;

The 'arcstart' value is where the arc starts, just 'arcstart' sets the current value as the start value. double clicking or alt+clicking (or option+clicking on mac) on the object restores to the 'arcstart' value, so does the 'reset' message., f 65;

- sets coordinates relative to object (default: 6, -15), f 58;

Allowing to display a number can be quite useful to monitor the value from dragging and typing. It's like having a built in attached number box. The Color of the number is the same as the foreground color and you don't have much configuring options other than font size and position., f 65;

When you can click on the [knob] it gets activated by showing a tiny center circle. Clicking outside the object deactivates it. When active, you can use the up/down or left/right arrow keys to increment and decrement values. Note you can press shift before activating the object, in which case the arrow keys will also increase or decrease in hundreths like if you'd just drag the mouse while clicking., f 66;

When active, hitting enter outputs the current value. You can also type a number value and hit enter to set it. When the number is displayed, you can see the number you're typing followed by '|'. The activity status and numbers you type are sent to receive names that match the send name followed by "-active" and "-typing". Check in the example below, which has the "\$0-number" send name. The usefulness of this is discussed on the right., f 66;

For more sophisticated GUI display you can use the [note] object from ELSE, which can offer you a different font, a different color and you can also interact with the 'active' and 'typing' send names to configure the object., f 65;

Open the [pd guts] subpatches for details. In the examples above, we use [makefilename] to format the number value with custom units. You can do something like that for any unit you are controlling on your patch, like ms, dB, hz and whatnot. The first example to the left uses percentage and the number value goes bold when the object is active., f 59;

The one in the middle is for transposition and the number label goes red when active. The one to the right is a bit more complex and displays panning values (displaying 'center' in the middle position) and is underlined when active., f 59;

In all examples above you can type in values when the knob is active and the [note] objects will display the values because we have receive objects listening to what you type. The value you type is only effective when you press enter.;

HINT: You can also use the 'active' send name to configure the knob itself and change its color, or change the color of the other knobs in your patch so the current knob is highlighted., f 59;

There are 4 different modes for number display. The default is '0', which never displays it. In mode "1", the number is always shown. Mode '2' shows the number value when the object is active. Mode "3" only shows the number when the object is active and you're typing a number., f 65;

'read only' disables all clicking activities and the object only responds to messages to set it. The 'active' message activates or deactivates the object in any case., f 25;

sets number display modes: '0'-never, '1'-always, '2'-when active, '3'-when typing (default 0), f 56;

-size <float> | -range <float, float> | -bgcolor <list> | -arccolor <list> | -fgcolor <list> | -arcstart <float> | -noarc | -nosquare | -angle <float> | -circular | -jump | -discrete | -number <float> | -numbersize <float> | -numberpos <f, f> | -receive <symbol> | -send <symbol> | -param <symbol> | -var <symbol> | -log | -exp <f> | -ticks <float> | -offset <float> | -savestate | -noloadbang | -readonly |, f 77;


## `lace`

The '-z' flag adds zeros for the case where lists are not of the same size. This way, zero are added in the place of missing elements to match the size of the biggest list., f 50;

[lace] interleaves two or more lists. A bang is considered an empty list., f 38;


## `lace~`

The '-z' flag adds zeros for the case where multichannel signals are not of the same size in number of channels. This way, zero are added in the place of missing channels to match the size of the multichannel signal with most channels., f 50;


## `lag2~`

[lag2~] is like [lag~] but has a different time for ramp up and ramp down. The lag time in ms is how long it takes for the signal to converge to within 0.01% of the target value. Note that the rising ramp is different than the descending ramp, unlike [glide2~]., f 73;

If [lag2~] has a multichannel left input, it outputs the same number of channels. If the secondary inlets have a single channel for the up/down lag times, the single value is applied to all channels. If a secondary inlet is also a multichhanel signal, then each channel gets its own lag time value. Note, however, that the number of multichannels in secondary inlets need to match the same number of channels from the left input., f 65;


## `lag~`

[lag~] is a one pole filter that creates an exponential glide/portamento for its signal input changes. The lag time in ms is how long it takes for the signal to converge to within 0.01% of the target value. Note that the rising ramp is different than the descending ramp, unlike [glide~]. the same kind of filter is used in other objects from the ELSE library (decay~/asr~/adsr~)., f 73;

If [lag~] has a multichannel input, it outputs the same number of channels. If the right inlet has a single channel for the lag time in ms, the value is applied to all channels. If the right inlet is also a multichhanel signal, then each channel gets its own time value. Note, however, that the number of multichannels in the right inlet needs to match the same number of channels from the left input., f 64;


## `lastvalue`


## `lastvalue~`


## `latoocarfian~`


## `lcm`


## `ldelay`


## `ldelay2`


## `ldemux`


## `level.m~`

This is a simple gain module that adjusts the gain in dB., f 16;


## `level~`

[level~] is a convenient abstraction for adjusting a signal's gain in dB (from -24 to 24 dB). It has support for multichannel signals., f 67;


## `lexpr`

First come variable names, then -> surrounded by spaces, then an expression (in Lua syntax).;

Messages can change the expression (provided inlet count stays the same). This resets the state of all variables. Note: weird tricks are needed for commas in messages :(;

Eaxh inlet supports a "hot <float>" method, that makes the inlet hot or not. By default only the first inlet is hot. Sending a bang to the first inlet always performs the calculation, no matter if that inlet is set to be cold.;

Multiple outlets are supported, with multiple expressions separated by commas.;

New in lexpr for pdlua-0.5: outputs can be symbols too. The inital "" is to make sure that we have a string.;


## `lfloat2bytes`

The optional argument sets the number of significant digits (default = 6).;

[lfloat2bytes] spits out the characters of a string representation of a float as bytes.;


## `lfnoise`


## `lfnoise~`


## `lfo`


## `lfo.m~`

This LFO module has singal inlets for FM and PWM (for square and vsaw wave) with attenuverters plus a sync inlet that takes impulses., f 29;


## `limit`

[limit] only allows messages through if a given time has elapsed since the previous input/output. Otherwise, it waits until that time passes and then sends the last received message since the previous output (ignoring the others).;

The second argument sets two ignore modes. In this case, messages received before the time limit are ignored and not sent after the period is done - instead, they are sent to the right outlet.;

In ignore mode "1", when it receives a message before the time limit, the clock restarts and only passes a message to the left outlet when the time interval between the two events is greater than the limit.;

In ignore mode "2", the clock is not restarted and new messages passes through and restarts the clock after the time interval from the first event that triggered the object., f 37;


## `lin2db`


## `lin2db~`

[lin2db~] converts amplitude values from linear to a deciBel Full Scale (dBFS) with support for multichannel signals. Conversion expression: "dbFS = log10(amp) * 20"., f 61;


## `lincong~`


## `list-pak`

Like [pack] for any kind of type. Argument specifies number of inlets. All inlets are hot as in Max' [pak].;


## `list-unpack`

Like [unpack] for any kind of type. Argument specifies number of outlets. Pointers untested rsp. not supported;


## `list.inc`

Use [list.inc] to generate a list by giving it a start value, a step value and number of elements. In 'ratio' mode the step is considered a ratio step that it multiplies to, otherwise it's just a regular linear addition., f 68;


## `list.seq`


## `llist-drip`


## `llist-rdrip`


## `loadbanger`

This makes it possible to create abstractions with variable inlets/outlets via dynamic patching, which simply does not work if you're using [loadbang] instead.;

So, by default, [loadbanger] uses the "load" type of bang when loading the patch. As said before, if you change it to "-init" mode, the bang will be sent first in subpatches and abstractions. Not only that, but the bang is sent also before the connections are made in the parent patch.;

Important Note: If you're using [loadbanger] inside an abstraction and need it to send a control data throughout an outlet to a parent patch, you cannot use the -init flag. That's because, as stated, these are triggered before the connections are made, so a value is not sent out.;

In ELSE, these abstraction uses [loadbanger] with the "-init" flag for that purpose, so it can have a variable number of inlets/outlets depending on the first optional float argument (1 by default).;

[loadbanger] (or [lb]) sends "bangs" (from right to left) when loading the patch and also sends bangs when receiving any message or clicked on. The number of outputs is defined by the argument (1 by default). [lb] can also be useful for dynamic patching (for creating inlets/outlets) in init mode.;

Pure Data can send two different kind of bangs when loading the patch. The [loadbang] object in Pd Vanilla sends a bang when the patch has been loaded. Let's name this type of bang as "load"., f 61;

[loadbanger] works with both kinds of bangs. By default, it sends the "load" bang, but if you can change to "init mode" with the "-init" flag., f 61;

If you check pd's terminal window after loading this help file, you'll see that the [loadbanger] object with the -init flag is sent before the others., f 61;

But there is also another type of bang that Pd can send, aka "init" bang. This second type is sent before "load". A famous external that just uses this kind of bang is [initbang] from the iemguts library., f 61;

As said, "init" bangs are sent before "load" bangs. It is also sent first inside subpatches and abstractions than in parent patches. In the case of abstractions, this is mostly useful for dynamic patching, because you can initialize it with a dynamic number of inlets/outlets., f 61;

The '-fin' flag is useful to 'finalize' the patch loading. It is actually the same as using a [delay 0] after a loadbang but more convenient this way.;


## `logistic~`


## `loop`


## `lop.bw~`


## `lop2~`

Change the parameters and check the filter response below. The graph considers a sample rate of 44.1Khz., f 39;

As you reach nyquist, it is like the filter has no action and the output is the same as the input., f 32;

Unlike [lop~] from Vanilla, this filter has a zero fixed at -1 on the z-plane, which means Nyquist is always filtered out., f 39;


## `lorenz~`

By default, the initial s, r, b and h values are 10, 28, 2.667 and 0.05 respectively, but can be changed via arguments or via the "coeffs" message.;

The system is based on these differential equations; x' = x + h * s * (y - x); y' = y + h * (x * (r - z) - y); z' = z + h * (x * y) - (b * z), f 32;

The [lorenz~] is a strange attractor discovered by Edward N. Lorenz while studying mathematical models of the atmosphere. It is a 3D model and we just get the 'x' dimension out for listening., f 67;

Which are evaluated at a given rate and the results are interpolated., f 32;


## `lowpass~`

This filter has zeroes fixes at +1 and -1 on the z-plane, which means both 0Hz and Nyquist are always filtered out.;

Change the parameters and check the filter response below. The graph considers a sample rate of 44.1Khz.;

omega = f * PI/nyquist; alphaQ = sin(omega) / (2*q); b0 = alphaQ + 1; a0 = (1-cos(omega)) / (2*b0); a1 = (1-cos(omega)) / b0; a2 = (1-cos(omega)) / (2*b0); b1 = 2*cos(omega) / b0; b2 = (alphaQ - 1) / b0;;

a0, a1, a2, b1 and b2 are calculated as a function of center frequency 'f' in hz and 'q' as follows;;

The equation is from the "Cookbook formulae for audio EQ biquad filter coefficients" by Robert Bristow-Johnsonc [1], and it is: y[n] = a0 * x[n] + a1 * x[n-2] + a2 * x[n-2] + b1 * y[n-1] + b2 * y[n-2];

[1] found in https://webaudio.github.io/Audio-EQ-Cookbook/audio-eq-cookbook.html, f 80;

Alternatively, you can switch from 'q' to 'bw' with the message methods., f 56;

By default, the resonance parameter is the filter 'q', but you can also set it to 'bw' or 't60'. The 'bw' means resonance as bandwidth in octaves and you can set it with the -bw flag or 'bw' message, whereas 't60' means decay time in 't60' (time it takes for the signal to resonate and decay 60db in ms)., f 56;

Here we have the resonance as bandwith in octaves. The value is 0.25, so a quarter of an octave, which is a major third width., f 56;

2) float - resonance (default 1), either in 'Q' (default) or 'bw', f 65;


## `lowshelf~`

Change the parameters and check the filter response below. The graph considers a sample rate of 44.1Khz.;

The equation is from the "Cookbook formulae for audio EQ biquad filter coefficients" by Robert Bristow-Johnsonc [1], and it is: y[n] = a0 * x[n] + a1 * x[n-2] + a2 * x[n-2] + b1 * y[n-1] + b2 * y[n-2];

a0, a1, a2, b1 and b2 are calculated as a function of frequency 'f' in hz, slope 'S' and 'db' gain as follows; w = f * PI/nyquist; G = pow(10, db/40); alphaS = sin(w) * sqrt((G*G + 1) * (1/S - 1) + 2*G); b0 = (G+1) - (G-1)*cos(w) + alphaS; a0 = G*(G+1 - (G-1)*cos(w) + alphaS) / b0; a1 = 2*G*(G-1 - (G+1)*cos(w)) / b0; a2 = G*(G+1 - (G-1)*cos(w) - alphaS) / b0; b1 = 2*(G-1 + (G+1)*cos(w)) / b0; b2 = -(G+1 + (G-1)*cos(w) - alphaS) / b0;;

[1] found in https://webaudio.github.io/Audio-EQ-Cookbook/audio-eq-cookbook.html, f 80;


## `lpaths`

postpath and load use _canvaspath, postpathx and loadx use _loadpath:;

Here load will be the same as loadx and postpathx will be the same as postpath because the directory the help patch is in is the same as the directory that this lpaths.pd_lua is loaded from.;

This lpaths.pd_lua is loaded from the 'subdir' directory, so postpathx and loadx will give that directory while postpath and load will still reference the directory that this help file is in.;

There is a copy of lpaths.pd_lua in the directory of this help patch, and in the 'subdir' folder. There are 2 different hello.txt files with different contents in both directories, that are loaded and printed with 'load' and 'loadx' messages, corresponding to _canvaspath and _loadpath respectively.;

This example demonstrates the use of self._canvaspath and self._loadpath. _canvaspath will give the directory of the canvas that the object is created in, whereas _loadpath will give the directory that the .pd_lua file is loaded from. Both have trailing slashes added for convenience.;


## `lpipe`


## `lreceive`


## `lsend`


## `lsymbol-drip`


## `lsymbol2bytes`


## `ltabdump`


## `ltabfill`

[ltabfill] is a clone of [lexpr] that writes a function to a table. The first argument and inlet is the name of the table, then the usual [lexpr] stuff follows. There is an additional implicit parameter to the expression, named 'x', which ranges from [0..1) no matter the size of the array. Note: you might have to close/reopen the table displays for them to refresh correctly.;


## `ltextfile-drip`

ltextfile-drip reads a text file. Incoming bangs cause it to spit out sentences from the file in sequence.;


## `lua`

ELSE distributes a modified version of "pdlua" - by Claude Heiland-Allen (2008), Martin Peach et al (2014) - which is distributed under the GNU License. This simplified/streamlined version discards the actual [pdlua] and [pdluax] objects. You can then consult the original documentation of [pdlua] for details on how to code objects in lua, which should be the same, but discard the information on how to use [pdlua] and [pdluax]., f 76;

ELSE uses a modified version of "pdlua" by Tim Schoen for PlugData, which also allows graphics. This is not paired up with the original and last released version of "pdlua" yet., f 76;

A couple of GUI abstractions in ELSE are using this feature, namely [circle] and [scope3d~]. Hence, the 'else' binary needs to be loaded so they can be used. The [hello] object below is a minimal example of an object coded in Lua. Note you can also provide help files for your object and right click on it to ask for them. Right click also allows you to open the .pd_lua file if your system has a known application for it., f 76;

When you load 'ELSE' via startup or [declare], it registers a loader that allows Pd externals written in Lua (with the "*.pd_lua" extension) to be loaded. One such object provided in ELSE is the lua object that allows you to load scripts into an object., f 80;

The [lua] object allows inline scripting in Lua and is one example of an object that is coded in lua. It is still an experimental object though that is not really functional and ready yet. So stay tuned!, f 80;


## `luametro`

Like [metro] in Pd, but allows more than one period. The periods will be evaluated in sequence from left to right as default. Min. period length is 0.01 msec.;

With "mode" you can set the mode the metro uses to select delay periods. Four modes are available:;

3: sequence - select in sequence from left to right (default mode);

4: rota - go left to right, then turn around and select right to left.;


## `lurn`

Clone of the Max object [urn]. Stops when all values have been chosen and bangs right outlet. Send "clear" message to make it start over.;

Use the second outlet to make the urn refill automatically if it gets empty as show in the second example with a combined "clear, bang" message.;


## `mag`


## `mag~`

the "power" argument gets the power magnitude result, that is the sum of the squares of the real and imaginary part.;

[mag~] gets the spectrum magnitudes (amplitudes) from cartesian coordinates (real / imaginary). This is much like the amplitude output of [car2pol~], but you can also get the power magnitudesinstead with the 1st argument., f 63;

This object is useful for spectral processing that doesn't require the phase values. It has support for multichannel connections., f 63;


## `makenote2`

Similarly to [makenote], [makenote2] takes a list with pitch, velocity and duration. Extra information is possible in this list, like a float for MIDI channel or whatever, but a list with at least 3 elements is necessary. The duration is in beats and the BPM is set via the argument or right inlet. The first item on the list (pitch) can be a symbol (like 'C4'). If you want the duration to specify a value in ms, use '60.000' as the bpm value!, f 75;

Extra arguments after the first one become part of the Note Off message., f 37;


## `markov`

This example creates a monophonic chain from MIDI input. Here you can also try to increase the order. An order of "2" means that the next note depends on the preceding two values. This makes it a lot less random, so the more you increase the order, the more it looks like the original input. After changing the order you need to recreate the chain. For this happy birthday example, an order of 5 outputs the original tune., f 54;

In this example you can use a MIDI keyboard to feed the [markov] object. With the [combine] object you can generate lists for chords., f 37;

[markov] creates Markov chains of any order out of progressions of floats, symbols or lists (which can be used to create polyphonic chains). You can change the order and recreate the chain. You can keep feeding information after the chain was created and recreate with the new information. You can also clear the memory to restart from scratch. State saving is possible with the 2nd argument, where the chain is saved with the patch., f 75;

Pseudo random number generators aren't true random number generators. Instead, an algorithm is used to provide a sequence of numbers that seems random. The same sequence can be reproduced if you set a "seed" value, which can be any integer number., f 42;

You can set a seed with the '-seed' flag. If you don't supply it, each object gets its own seed internal seed. If you send a 'seed' message without float, the object also gets a unique seed value., f 42;

Seeds are kept locally, which means that if two [markov] objects are seeded the same they will have the same output. Conversely, you can seed the same [markov] object twice with the same seed to repeat the output., f 42;

Sync [markov] objects fed with the same data objects with a seed value., f 37;

The objects to the right were saved with the chain data because of the savestate 2nd argument, which saves the markov chain with the patch when you save the file. You can also use the "savestate" message to set the object into "savestate" mode., f 42;


## `match~`


## `maxpeak~`

[maxpeak~] returns the maximum peak amplitude so far. A bang in the right inlet resets the maximum value. The right outlet sends bangs when the input is clipped., f 61;


## `median`


## `median~`


## `merge`

any message type to merged into another, a bang represents an empty list., f 48;

a message composed of the merged messages, an empty list is a bang., f 51;

[merge] takes any type of messages in any inlet and combines them into a list message. A bang is considered an empty message., f 52;


## `merge~`

[merge~] merges different signals of different channel lengths. The number of inlets is set via the argument.;


## `message`


## `messbox`

Like a regular message box, a comma will split the message in different ones inside the same box., f 50;

It can also deal with semicolons, which turn the message box into a send object. Note that unlike a message box, "\$0" gets expanded!, f 48;

When you have '\$1', '\$2', it takes the values of list messages, floats or symbols., f 28;

-fontsize <float> (default: patch's) | -size <float, float> (default: patch's fontsize * 15, patch's fontsize * 5) | fgcolor <f, f, f> (default 0 0 0) | -bgcolor <f, f, f> (default 235 235 235) | -bold (default "normal") |, f 77;

The [messbox] object is an object you can type in messages while in run mode. It's like atom boxes but does all that a message box does. Any message type is possible. It deals with dollar signs, comma and semicolons in the same way as regular message boxes. See [pd syntax] for more details., f 68;


## `meter`


## `meter2~`

list is: rms of left, peak of left, rms of right, peak of right, f 36;

[meter2~] is a convenient stereo VU-meter abstraction. See also [meter~], [meter4~] and [meter8~]., f 54;


## `meter4~`

[meter4~] is a convenient qudraphonic VU-meter abstraction, see also: [meter~], [meter2~] and [meter8~].;


## `meter8~`

[meter4~] is a convenient qudraphonic VU-meter abstraction, see also: [meter~], [meter2~] and [meter4~].;


## `meter~`

Using [else/meter~] in conjunction with [else/gain~] and [dac~], f 35;

[meter~] is a convenient mono VU-meter abstraction. See also [meter2~], [meter4~] and [meter8~]., f 52;


## `metronome`


## `metronome~`


## `midi`

A stop message also flushes hanging note on messages, but a "pause" message doesn't. The continue message keeps playing from where it was paused!, f 46;

The "start" message sets to 'slave' mode and expects an external clock input, such as from [midi.clock] or [tempo]. This allows you to synchronize with an external clock source device. The standard is 24 clock ticks per quarter note., f 46;

You can directly record from raw MIDI data with [midiin] using the 'record' message (note you don't need the stop message when switching from recording and playing). Then use 'save <symbol>' to save to a specific file, or just 'save' to save to a MIDI file with the dialog box., f 63;

You can record from specialized MIDI objects such as [notein], [makenote] or [keyboard] - just use the [note.out] object to convert the messages to raw MIDI., f 63;

raw MIDI data to record. when not recording: play <1>, stop <0>, f 54;

You can import and export to text files, just use the .txt extension to open and save. The format of the file is compatible to the [text sequence] object. Check the example to the right., f 38;

[midi] plays/records raw MIDI streams and can save/read MIDI files or import/export to txt files., f 55;


## `midi.clock`


## `midi.in`

The [midi.in] object is useful in conjunction to [route] if you need to collect more than one type of MIDI data.;

[midi.in] sends "cooked" MIDI data instead of "raw" data like [midiin] with MIDI data type symbol, values and channel (but a note output is sent as a simple numeric list). It can take a raw MIDI input via its inlet but it also listens to your connected MIDI device., f 72;

An argument sets the channel number. If so, only MIDI messages that correspond to that channel are sent. If no channel is given, it loads "0" as the default and the object operates in omni mode, where the objects outputs values from all channels and the channel number is output in the right outlet. You can also change the channel with the right inlet (0 sets to omni)., f 67;

Port number is encoded as the channel number. Channels 1 to 16 are for port 1, channels 17 to 32 is the same as channels 1 to 16 for port 2, channels 33 to 48 represents channels 1 to 16 in port 3, and so on..., f 63;

The object automatically listens to whatever is connected as a MIDI device in Pd. So it's like it has a built in [midiin] object feeding it. This is considered to be an "internal" source.;

The left inlet provides and "external" source of raw MIDI data input. This is needed if you have, for instance, the [midi] object from ELSE reading a MIDI file or something. If, by any chance, you just want the object to receive from this external source and not listen to the internal connected device, you can use the '-ext' flag or 'ext' message, to force only the external input.;


## `midi.learn`

A symbol argument (as the first or second argument) sets a send name. You can also set or change it with the 'set' message., f 41;

[midi.learn] is an abstraction based on [savestate] that learns and saves any MIDI input data. Activate it via bang or click and send it MIDI data so it learns where it comes from. The information gets stored in the owning patch., f 73;

The Learned control/program change are followed by numbers that specify 'control/program number' and 'channel' or just a 'channel number' for note and bend messages (touch and polytouch are not supported)., f 73;

An optional non zero argument sets the object to "abstraction" mode, which is needed if you want to use it inside an abstraction. This is for advanced users and the trick is to use it in conjunction with [savestate] and here's the mechanism I use for the MERDA modules., f 45;

Whenever the abstraction learns something new, you'll be prompted to save your patch when you close it, so it'll remember when you reopen it., f 38;


## `midi.out`

Control message (control value, control number and channel), f 31;

The object automatically outputs to whatever is connected as a MIDI device in Pd. So it's like it has a built in [midiout] object. If, by any chance, you just want the object to output to the outlet, you can use the '-ext' flag or 'ext' message., f 61;

[midi.out] sends MIDI data from "cooked" data, instead of "raw" data like [midiout]. It takes data type symbol, values and channel (but a note output is received as a simple numeric list). It outputs raw MIDI data but it also sends out to the connected MIDI device. A float argument or right input sets a single channel (0 is omni)., f 72;


## `midi2freq`


## `midi2note`

anything is possible, you can even use "x" and "bb" for double sharp/flats, f 21;

The "-unicode" flag sets to unicode mode, where sharps and flats are represented by the unicode characters "â¯" and "â­" (which are supported by Pd's default font).;

The "-list" flag sets to list output mode, where the output is a list with the note symbol and octave number. You can combine both flags of course (in any order).;

The float input values are quantized to quarter tones, so yeah, there's support for quarter tones. The syntax is the same as found in [note2midi] where '+' is a quarter tone sharp and '-' is a quarter tone flat. The quarter tone character can be combined with regular sharps and flats., f 73;

The 'chromatic', 'sharp' and 'flat' modes work the same way and you can set a list of arbitrary symbols with 24 elements to set quarter tones output., f 52;

[midi2note] converts a MIDI pitch value to note names (such as Eb3). The names end with an octave number, in a way that middle C (MIDI pitch = 60) represents C4 represents. Float inputs are rounded to quarter tones (yes, there's support for quarter tones)., f 68;


## `mix2~`

[mix2~] has 3 scaling modes for its slider (the default is "quartic"). The rightmost inlet sets scaling mode, gain and pan values., f 60;

The graph to the left shows us how the scaling modes work. A linear scaling doesn't really do anything, the input is the same as the output. We have then two non linear modes:;

dB: This mode adopts a decibel scale with a range of 100 dB (using the [dbtorms~] object)., f 55;

Quartic (default): This mode just gets the slider values to the power of 4 (so, for instance, an input slider value of 0.5 becomes 0.125)., f 57;

[mix2~] is a convenient 2 channel mixer abstraction with gain and panning.;


## `mix4~`

[mix4~] has 3 scaling modes for its slider (the default is "quartic"). The rightmost inlet sets scaling mode, gain and pan values., f 60;

The graph to the left shows us how the scaling modes work. A linear scaling doesn't really do anything, the input is the same as the output. We have then two non linear modes:;

dB: This mode adopts a decibel scale with a range of 100 dB (using the [dbtorms~] object)., f 55;

Quartic (default): This mode just gets the slider values to the power of 4 (so, for instance, an input slider value of 0.5 becomes 0.125)., f 57;

[mix4~] is a convenient 4 channel mixer abstraction with gain and panning.;


## `mono`

mode <float> - sets priority mode: <0> last, <1, high>, <2, low>, f 70;

legato <float> - non zero sets to legato mode, zero restores default, f 72;

flush - sends a note off for the hanging note and clears memory, f 63;

When the priority is set to "high", a new note on goes through only when it is higher than the existing ones - and when you release it, it recalls the next highest note that is still on., f 35;

When the priority is set to "low", a new note on goes through only when it is lower than the existing ones - and when you release it, it recalls the next lowest note that is still on., f 37;

You can set the mode via a flag or via the mode message. The default priotiy mode is "last" So whenever you play a new note when you're still holding other notes, it goes through - and when you release it, the last note you had played before that is still on gets recalled., f 35;

The exanple to the right also implements a portamento with the [glide~] object. For every new attack, there's no portamento, but for other subsequent played notes, you have a portamento time of 100 ms., f 40;

Here's a patch where you can test [mono] with a keyboard GUI from the ELSE library that generates MIDI notes., f 21;

By default, new notes resend/retrigger the velocity value. But in legato mode, a new velocity value is only sent if a first note on is given., f 51;

[mono] takes note messages and handles them to emulate monophonic synth behaviour. Its internal memory can remember up to the last 10 input voices *and pitches need to be >= 0)., f 66;


## `mono.rev~`

[mono.rev~] is a reverb abstraction with mono input but stereo output. It's based on a feedback delay network like vanilla's [rev3~] object, but it offers a "room size" parameter whose typical value is around 0.5, values closer to 0 and 1 may create unusual results. Changing size values may generates unusual artifacts (you can clear the delay buffers when you do it to prevent it, but you may get clicks)., f 70;


## `mono~`

mode <float> - sets priority mode: <0> last, <1, high>, <2, low>, f 70;

legato <float> - non zero sets to legato mode, zero restores default, f 72;

flush - sends a note off for the hanging note and clears memory, f 63;

When the priority is set to "high", a new note on goes through only when it is higher than the existing ones - and when you release it, it recalls the next highest note that is still on., f 35;

When the priority is set to "low", a new note on goes through only when it is lower than the existing ones - and when you release it, it recalls the next lowest note that is still on., f 37;

You can set the mode via a flag or via the mode message. The default priotiy mode is "last" So whenever you play a new note when you're still holding other notes, it goes through - and when you release it, the last note you had played before that is still on gets recalled., f 35;

The 1st argument sets portamento in ms, this is based on the example given in the help file of [mono]., f 27;

By default, new notes send their velocity value, but in legato mode, a new velocity value is only sent if a first note on is given., f 49;

[mono~] emulates monophonic synth behaviour and is much like [mono], but can also glide the pitch output with a portamento setting., f 68;


## `morph`


## `morph~`

[morph~] allows you to make a spectral crossfade between the amplitudes and phases of two inputs. You can then do cross synthesis and spectral morphing., f 76;


## `mouse`


## `mov.avg`


## `mov.avg~`


## `mov.rms~`

'n' number of last samples to apply the average to (if different than the last, the filter is cleared), f 51;

The first argument specifies 'n' number of samples to take the RMS. This also sets the buffer size if no size flag is given. Float or signals into the right inlet also sets 'n'. The default and minimum value is "1"., f 61;

By default, the buffers size 1024 samples long. You can also set the maximum value with the -size flag or message., f 61;

[mov.rms~] gives you a running/moving RMS (Root Mean Square) over a time window of samples. At each sample, the RMS of the last 'n' sample is given.;


## `mpe.in`

The data types are Note On, Note Off, Channel Pressure, Slide (Control #74) and Pitch Bend. Note On and Note Off messages are also output as lists with <pitch>, <on velocity> and <off velocity>., f 75;

You can route each voice or connect it directly to a [clone] object which will route the rest of the list internally., f 28;

You can then furtherly route the different data types inside clone or whatever., f 28;

[mpe.in] automatically listens to whatever is connected as a MIDI device in Pd. So it's like it has a built in [midiin] object feeding it. Hence, if you have a MPE aware device connected to Pd, you don't need to worry about anything and just get the data from it. This is considered to be an "internal" source., f 55;

The inlet provides and "external" source of raw MIDI data input. This is needed if you have, for instance, the [midi] object from ELSE reading a MIDI file or something. If, by any chance, you just want the object to receive from this external source and not listen to the internal connected device, you can use the '-ext' flag or 'ext' message, to force only the external input., f 55;

[mpe.in] sends "cooked" MPE data from external "raw" MIDI data or an internally connected device. It outputs most common MIDI messages prepended with a voice number indexed from 0 (which depends on MIDI channel in this case)., f 69;

The right outlet outputs port number. The argument sets the port number to listen to, as well as the right inlet. By default, the value is '0', which means "omni", that is, listen to all ports., f 57;


## `ms2samps`


## `ms2samps~`

[ms2samps] is a simple abstraction that converts time values from ms to number of samples. It has support for multichannel signals., f 53;


## `mtx.ctl`

[mtx.ctl] provides a user matrix interface control. The cells in the grid can be either on or off. The output is a list with 3 floats that specify: column, row and status., f 69;


## `mtx.mc~`

Test below the [mtx.ctl] object to control [mtx.mc~]. In this example you can test all messages the object accepts.;

[mtx.mc~] routes a channel signal from a multichannel input to one or more channels of a multichannel output., f 71;


## `mtx~`

[mtx~] routes signals from any inlets to one or more outlets. If more than one inlet connects to an outlet, the output is the sum of the inlets' signals., f 78;

Test below the [mtx.ctl] object to control [mtx~]. In this example you can test all messages the object accepts., f 59;


## `multi.vsl`

By default, the sliders' output range is from 0 to 127, but you can change it with the -range flag or the range message, which sets the range for all sliders., f 56;

Note that when you change the range, all values are updated internally to the new range before you ever change them by clicking and dragging or the set message or whatever., f 48;

You can set the x/y dimensions with the -dim flag or message., f 30;

You can set background, foreground ad line colors with the 'bgcolor', 'fgcolor' and 'linecolor' messages or '-bgcolor', '-fgcolor' and '-linecolor' flags., f 62;

You can set to "jump on click" mode with the '-jump' flag or 'jump' message. Non zero sets to jump on click mode and zero (default) is "steady on click" mode. These are the same as in Vanilla's sliders.;

In jump on click mode, it behaves kinda like arrays in Pd when you clicck and drag around, but it'll clip according to the rang. Note that prssing shift for fine tuning doesn't work for "jump on click", but you can press "alt"/"option" to lock on a slider.;

-range <float, float>: sets slidrs' range (default: 0, 127), f 72;

-jump <float>: non zero sets jump on click mode (default: 0), f 72;

-dim <float, float>: sets x/y dimensions (default: 200 127), f 72;

-bgcolor <f, f, f>: sets background color in RGB (default: 255 255 255), f 72;

-fgcolor <f, f, f>: sets frontground color in RGB (default: 220 220 220), f 72;

-linecolor <f, f, f>: sets line color in RGB (default: 0 0 0), f 72;

-set <list>: sets slider's values (default: 0 0 0 0 0 0 0 0), f 72;

In the default mode, you can use [route] to route values from the multi slider. You can also use [clone] and feed the output directly to it., f 30;

In the list output mode you can use [order] to connect to [clone], but in this case we also send it to [sine~] as it generates MC signals with it., f 35;

You can also set send/receive names with the 'send'/'receive' messages or '-send'/'-receive' flags., f 31;

Setting these to 'empty' removes the send/receive symbols., f 32;

Make sure to escape "\$0" properly with backslashes (as in: "\\\$0")., f 24;

press shift for fine tuning and alt/option for locking on a slider, f 11;

Press shift for fine tuning just like in vanilla's sliders., f 21;

If you press "alt" or "option" (for mac), it locks on a given slider, so if you scroll to a different slider, it keeps affecting the locked one, f 21;

The import message sets the number of sliders according to the number of numbers. It sets and outputs the sliders' values., f 44;

The multi slider object has an internal array that stores the data so you can access it. You can set its internal array name at initialization with the '-name' flag and name it or rename it with the 'rename' message.;

You can then use other objects in Pd to access its values as below. Just be sure to escape the$0 with a bacslash if you're using it., f 59;

slider number / slider value in the default mode or all values as a list in the "list mode", f 51;

set slider 3, 4, 5, 6 to "10", "20", "30" and "40", f 25;

The "setall" message sets a float to all the sliders. The "set" message will set one or more sliders counting from the slider number defined in the first float., f 67;

If you send it a list of values, it updates and outputs the sliders counting from the first one. If the list is shorter than the number of sliders, just the first sliders are updated. If it is longer, the extra ones are ignored., f 67;

With the 'savestate' message or '-savestate' flag, the GUI operates in 'save state mode', where it saves the state from the last time the patch was saved. Note that this is only useful for patches and not abstractions. For abstractions oyou should use [savestate] instead, and also have a look at [presets]. Unlike iemguis, the value is not output when loading the patch, use [loadbang] for that.;


## `mutator`


## `nchs~`

[nchs~] gets the number of channels from a multi-channel connection, as provided by [snake~ in], [clone] or other objects. The object outputs values whenever the DSP chain gets updated and you can also query for the number of channels with a bang message. It also works in subpatches or abstractions because [inlet~] is also multi-channel aware., f 59;


## `nmess`


## `noisegate~`

[noisegate~] is a noise gate abstraction. It takes a threshold in dBFS in which it only audio through that has a RMS value over that threshold., f 62;


## `nop`


## `nop~`

[nop~] does no operation, that is, it does nothing. It's mostly useful for managing signal cords in your patch.;


## `norm~`

[norm~] is a normalizer abstraction based on [mov.rms~]. It takes a normalization value in dBFS and a window analysis size., f 60;


## `note`

After setting a background color you can use the 'bg' flag to turn it off or on again., f 62;

[note] uses "Dejavu Sans Mono" as its default font, just like Pd. But, as of version 0.51-3, Pd uses 'Menlo' as its default font for macOS, so [note] also defaults to this font in macOS., f 62;

[note] will attempt to open a font name that corresponds to your given name. If such a font name doesn't exist, it'll open some other font you have on your system instead that it thinks is best for what you requested, and you'll have no idea which one it is. So just be sure you have the fonts you want properly installed., f 62;

When in edit mode, [note] shows its inlet and an outline. You can always see the outline if you use the "outline" message or flag. The [note] object below has a receive symbol, so you can send messages to it via a [send] object. In this case, the inlet is suppressed, so we don't see it. Besides the properties window, the receive symbol can be set with the receive message or the @receive attribute. If you set a receive name as "empty" then it it can't receive messages anymore and the inlet is show again., f 74;

Note: when in edit mode, you can click on the text to select it and then press <F5> to copy the text from [else/note] into a vanilla comment box. So far, this is the only way to copy the text from note into Pd (control+c / control+v doesn't work)., f 53;

By default, [note] has an unfixed limit but has a maximum width limit of 425 pixels (like Pd's comment). Hence, it will resize if you keep typing in it but if it exceeds this limit [note] breaks into a new line (with the last word that did not fit in). When in edit mode you can see a handle bar to the right that allows you to resize the object. If you click and drag it, you'll set a new maximum width to the point where you release the mouse button. You can also set the width with the "width" message or "-width" flag. If you give it a value of '0', then you get back to the default (where you have an unfixed limit but a maximum width of 525)., f 85;

You can also set three kinds of justification parametrers: left (0: default), center (1) and right (2).;

You can use backslash to escape symbols like '$', commas and semicolons., f 22;

[note] also takes characters from different alphabets like elsewhere in Pd (such as in messages or comments)., f 29;

[note] is a GUI meant only to display text notes. This is basically the same of Pd's comment but with the advantage of being able to set the font, size, color, background color, bold, italic, underline and justification., f 68;

-font <symbol> (default: 'dejavu sans mono' or 'menlo' for mac) | -bold | -italic | -size <float> (default patch's) | -just <float> (default 0) | -color <f, f, f> (default 0 0 0) | -bgcolor <f, f, f> (default 255 255 255) | -bg | -outline | -note <anything>: sets note (default "note") | -underline | -receive <symbol> (default 'empty') | -width <float> (default 0), f 77;


## `note.in`

An argument sets the channel number. If so, only MIDI messages that correspond to that channel are sent. If no channel is given, it loads "0" as the default and the object operates in omni mode, where the objects outputs values from all channels and the channel number is output in the right outlet. You can also change the channel with the right inlet (0 sets to omni)., f 67;

Port number is encoded as the channel number. Channels 1 to 16 are for port 1, channels 17 to 32 is the same as channels 1 to 16 for port 2, channels 33 to 48 represents channels 1 to 16 in port 3, and so on..., f 63;

Release velocity is very rare in today's controllers, but it used to be a real thing., f 44;

The '-both' flag outputs both note on and off velocities in a list. The 1st element is the pitch, the 2nd is the on velocity and the 3rd is the off velocity., f 29;

Nowadays, MIDI Note Messages are basically just "Note On" messages, and a velocity of 0 is considered a "Note Off" message. Nonetheless, there's a special Note Off MIDI message which also carries a velocity (known as "release velocity). By default, [note.in] only outputs 'Note On' messages, where a velocity of zero is commonly considered a Note Off message. If it then receives a proper Note Off message with release velocity, it gets converted to a '0' velocity.;

The '-rel' flag creates a mid outlet to output only proper Note Off messages with release velocity., f 51;

[note.in] extracts MIDI Pitch information from external "raw" MIDI data or an internally connected device. It deals with both NoteOn and NoteOff messages (with release velocity)., f 70;

The object automatically listens to whatever is connected as a MIDI device in Pd. So it's like it has a built in [midiin] object feeding it. This is considered to be an "internal" source.;

The left inlet provides and "external" source of raw MIDI data input. This is needed if you have, for instance, the [midi] object from ELSE reading a MIDI file or something. If, by any chance, you just want the object to receive from this external source and not listen to the internal connected device, you can use the '-ext' flag or 'ext' message, to force only the external input.;


## `note.out`

Release velocity is very rare in today's controllers, but it used to be a real thing., f 54;

Nowadays, MIDI Note Messages are basically just "Note On" messages, and a velocity of 0 is considered a "Note Off" message. Nonetheless, there's a special Note Off MIDI message which also carries a velocity (known as "release velocity). With the -rel or both flag, the object can format Note Off messages., f 62;

[note.out] formats and sends raw MIDI pitch messages to Pd's MIDI output and its outlet. An argument sets channel number (the default is 1)., f 66;

The object automatically outputs to whatever is connected as a MIDI device in Pd. So it's like it has a built in [midiout] object. If, by any chance, you just want the object to output to the outlet (for feeding a [midi] object or something), you can use the '-ext' flag or 'ext' message., f 61;

-both: sets the object to output both note on and off messages, f 62;


## `note2midi`

More importantly, these musical symbols are supported by Pd's default font, so you should be able to see them if nothing is wrong in your system/setup/installation., f 63;

Please note the object also supports special unicode characters for "sharp" and "flat" from the Miscellaneous Symbols block. You can the easily available characters from regular keyboards: "#" (number sign, ASCII value 35) and "b" (lower case b letter) instead, but the object also supports "â¯" and "â­"., f 63;

In list mode, [note2midi] expects that every note name is represented as a list of two elements, the note name and the octave number., f 50;

[note2midi] converts note names (such as 'C4') to MIDI pitch values. All enharmonic names are included (even unusual ones like Cb and double sharps/flats). There's also support for quarter tones (syntax is '+' for quarter tone sharp and '-' for quarter tone flat). It takes symbols, lists or anythings that end with an octave number, in a way that C4 represents middle C (MIDI pitch = 60). Octave range is from '0' to '8'., f 85;

Unfortunately Pd's default font doesn't have the appropriate unicode symbols for double sharps and double flats, which are rarely used anyway. So, in this object's notation, you can use "x" for double sharps and "bb" for double flats., f 63;

Microtones unicode symbols aren't supported either by Pd's default font. The [note2midi] object has support for quarter tones and the syntax is '+' for quarter tone sharp and '-' for quarter tone flat. The quarter tone accident character must be the last one in the note name symbol and it can and be combined with the sharp and flat symbols., f 63;


## `notedur2ratio`

1nd - whole note duplet/dotted (3/2 = 1.5); 1n - Whole note (1/1 = 1); 1nn - Whole note nonuplet (8/9 = 0.888889); 1nq - Whole note quintuplet (4/5 = 0.8); 1nt - Whole note triplet (2/3 = 0.6666); 2nd - Half note duplet/dotted (3/4 = 0.75); 2ns - Half note septuplet (4/7 = 0.571429); 2n - Half note (1/2 = 0.5); 2nn - Half note nonuplet (4/9 = 0.444444); 2nq - Half note quintuplet (2/5 = 0.4); 4nd - Quarter note duplet/dotted (3/8 = 0.375); 2nt - Half note triplet (1/3 = 0.3333); 2ns - Half note septuplet (2/7 = 0.285714); 4n - Quarter note (1/4 = 0.25); 4nn - Quarter note nonuplet (2/9 = 0.222222); 4nq - Quarter note quintuplet (1/5 = 0.2); 8nd - Eighth note duplet/dotted (3/16 = 1.1875); 4nt - Quarter note triplet (1/6 = 0.166667); 4ns - Quarter note septuplet (1/7 = 0.166667); 8n - Eighth note (1/8 = 0.125); 8nn - Eighth note nonuplet (1/9 = 0.111111); 8nq - Eighth note quintuplet (1/10 = 0.1); 16nd - Sixteenth note duplet/dotted (3/16 = 0.09375); 8nt - Eighth note triplet (1/12 = 0.0833333); 8ns - Eighth note septuplet (1/14 = 0.0714286); 16n - Sixteenth note (1/16 = 0.0625); 16nn - Sixteenth note nonuplet (1/18 = 0.0555556); 16nq - Sixteenth note quintuplet (1/20 = 0.05); 32nd - Thirty-second note duplet/dotted (3/64 = 0.046875); 16nt - Sixteenth note triplet (1/24 = 0.0416667); 16ns - Sixteenth note septuplet (1/48 = 0.0357143); 32n - Thirty-second note (1/32 = 0.03125); 32nn - Thirty-second note nonuplet (1/36 = 0.0277778); 32q - Thirty-second note quintuplet (1/40 = 0.025); 64nd - Sixty-fourth note duplet/dotted (3/128 = 0.0234375); 32nt - Thirty-second note triplet (1/48 = 0.0208333); 32ns - Thirty-second note septuplet (1/56 = 0.0178571); 64n - Sixty-fourth note (1/64 = 0.015625); 64nn - Sixty-fourth note nonuplet (1/72 = 0.0138889); 64nq - Sixty-fourth note quintuplet (1/80 = 0.0125); 64ns - Sixty-fourth note septuplet (1/112 = 0.00892857); 128n - One-hundred-twenty-eighth note (1/128 = 0.0078125);;

Here's a table with the main note durations in order of longer to shorter durations, with fracions and float values:, f 45;

'd' for duplet; 't' for triplet; 'q' for quintuplet; 's' for septuplet; 'n' for nonuplet.;

You can explicitly specify what the exact tuplet is in the [x:y] format, where [3:2] is a triplet, for instance. Since you already can use abbreviations for the most common tuplets, this is useful when you wanna go crazier., f 81;

<== dotted tuplets are also possible as in here (you can't use 's' in this case and you can use 'd' instead of "." as well as ".."/"dd" for double dotted), f 54;

Dotted notes are possible with ".", which is also the same as 'd' (for duplet), so you can consider 'd' as an abreviattion for 'dotted' as well. Double dotted notes are possible with ".." or "dd" (for 'double dotted).;

You can tie as many notes you want with "_", the overall duration will be given.;

[notedur2ratio] converts from a note duration symbolic syntax to a ratio (either as fraction or float). The syntax is: '1n' for whole note, '2n' for half note, '4n' for quarter note, '8n' for eighth note (and so on down to 128n). Dotted notes are possible and you can add tuplets to the symbol in the [x:y] format or you can add the following letters to specify most common tuplets: 'd' for duplet, 't' for triplet, 'q' for quintuplet, 's' for septuplet and 'n' for nonuplet. Tied notes are also possible with "_". Details in the examples below., f 80;


## `noteinfo`


## `numbox~`

-fgcolor <f, f, f>: sets frontground color in RGB (default 0 0 0), f 71;

-range <float, float>: dragging range (default: 0, 0 - unlimited), f 71;

-bgcolor <f, f, f>: sets background color in RGB (default 255 255 255), f 71;

-rate <float>: sets refresh rate in ms (default 100, minimum 15), f 71;

-ramp <float>: sets ramp time in ms (default 10, minimum 0), f 71;

-width <float>: sets digit width (default: 6, minimum 1), f 71;

[numbox~] is a signal GUI number box. It can be used to display/monitor signal values at a fixed rate or generate them with a ramp time., f 71;

sets initialization and generating value with given float or sets current value if no float is given., f 51;

[numbox~] goes into monitor mode when there's a signal connected to it. The input signal is then passed through and it displays the input values at a given rate in ms, set via the '-rate' flag, 'rate' message or via properties. In this mode you can't click to interact with it., f 65;

When in generating mode, you can click to activate the box and type in a number then hit enter. You can also drag the mouse up or down or use up/down arrows to increment/decrement values. If shift is pressed when clicking on the box the mouse dragging or up/down arrows incremente/decrement in hundredths., f 61;

You can set a lower and upper range that limits values, but only for dragging and using up/down arrows. This is set via the 'range' message, -range flag or via properties., f 61;

If no signal is connected, [numbox~] generates signal values with a smoothening ramp in ms (or no ramp if ms is 0) set via the '-ramp' flag, 'ramp' message or via properties. In this mode you can also set values with a float input. The 'load' message or '-load' flag sets generating value at load time (aka initialization value). If you only send 'load', then [numbox~] saves the current state by capturing the current value as the load value. You can also set the load value via properties. Alt+clicking on the object restores this initial load state., f 61;

These are visual parameters that are also set via properties and flags. Size sets font size in pixels, which affects height (4 pixels bigger) and width. The width parameter sets the number of displayed digits and affects overall width. The bgcolor/fgcolor parameters set background and foreground color with a hex symbol., f 62;


## `nyquist~`

Unlike [samplerate~], [sr~] always gives you the global sample rate as defined in Pd's audio settings instead of the up/downsampling rate running in the patch due to [block~]., f 56;

[nyquist~] reports the nyquist (which is half the sample rate) as a frequency or period. It sends it when loading the patch 'init' time (that is before [loadbang]), when receiving a bang or when the sample rate changes. It reports it either in hz or khz and the period either in seconds os milliseconds. like [else/sr~], it doesn't report up/down sampling rates., f 79;

[sr~] can take a [value] name as an argument. You can then retrieve this value in another [value] or [var] object or inside an expressionin [expr];


## `op`

The '%' (modulo) operator calls the 'fmod' function also found in the expr family of objects. Note that it doesn't correspond neither to [%] or [mod] objects from Vanilla., f 31;

For any other operations on lists that are not present in [op] and other objects from the ELSE library, just do something like this below, where you can use any object. You can also use [expr] for more complex operations and even conversion formulas (with more than two variables, etc.), f 64;

[op] provides many operators and is most useful for lists, as there are objects in Pd Vanilla for most of these operations., f 61;

If list sizes mismatch, the same thing that happens with multichannel signals in math objects like [*~] applies, where the smaller list wraps and repeats until reaching the size of the longer list., f 56;


## `openfile`


## `op~`

Note that [op~] does not have the same operators as [op] because Pd Vanilla already provides many objects for the same operations (such as [+~], [log~], etc...)., f 33;

The '%' (modulo) operator calls the 'fmod' function also found in the expr family of objects. Note that it doesn't correspond neither to [%] or [mod] objects from Vanilla., f 39;

[op~] is a signal operator where the first argument defines the the type (for either comparison, bitwise, logic and modulus operations). This is more efficient than using [expr~] (which also contains all these operators). Moreover, it has support for multichannel signals., f 69;

signal(s) - secondary operator value (ignored for not and bitnot), f 66;

All of these functions work with multichannel signals. If both inputs have the same amoun of channels, then operations are done at each corresponding channels. In case the number mismatch, the input with less channels wrap around and copy the first channels until reaching the number of channels of the other input. This is specially useful to apply all values of a multisignal connection to a single channel value (or a float)., f 69;


## `order`

If an input list is smaller than the given size, the list is output anyway. If the last bit of the broken list is smaller than the split size, it is also output.;

[order] splits a list into successive lists of a given size (default 1 element) and tags each of them with ordered indexes. This is useful for sending values to all instances of an object loaded in [clone]!;

The [order] object is used inside objects in the else library that use the [clone] object, such as:, f 47;


## `osc.format`

[osc.format] is similar to Vanilla's [oscformat]. This is still way too simple and experimental. It is used in the [osc.send] abstraction and can be used for edge and lower level cases. It takes anything messages or lists whose first element is an address that start with "/". The type of data for each element in the message is either a float or a string only depenfing on the atom type, so there are only these options (so far). You can't send bundles either. Use the original Vanilla [oscformat] or mrpeach's packOSC object for more complete objects., f 78;


## `osc.parse`

[osc.parse] is similar to Vanilla's [oscparse] but the output is not a list and more closely related on how OSC messages are generally dealt with. It is still in the [osc.receive] abstraction and you can use the object for more edge and lower level cases., f 70;


## `osc.receive`

[osc.receive] receives OSC messages from network connections and is an abstraction based on [osc.parse] and [netreceive]. You can use to receive OSC messages from an [osc.send] object with a matching port., f 67;


## `osc.route`

Addresses are specified with the "/" separator and [osc.route] is able to break this message and route them. Note how the '/slider' address matches input messages that start with '/slider' but have further sub addresses with following "/"., f 42;

A list message also works if the 1st element is an OSC path, f 30;

You can use an address and a sub address in the router so you don't need more than one [osc.route] object in cascade to deal with further addresses as below in the middle. Note that if no further sub address is given, [route] can also do the same job by the way!, f 50;

[osc.route] routes OSC messages received from [osc.receive]. It follows the same logic as Vanilla's [route] where arguments set the number of outlets and an extra is created for no matches. The difference is that it manages OSC addresses instead, specified with the "/" separator. Note how the '/hz' address matches input messages that start with '/hz' even if it has further sub addresses., f 80;

characters separated by a minus sign in brackets indicate the range of characters to match to, f 48;

an exclamation in the beginning of brackets negates the list and matches to any other character, f 34;

It's hard to deal with commas and curly braces in Pd, specially curly braces since you can't type them or paste them. You may wonder how I was able to generate a message with it as above. If you are ninja enough you can create them with [list tosymbol] as below, then use "set$1" to imprint it in a message. Ninja tricks aside, you may get such a message from the OSC sender anyway and dal with it in Pd with [osc.route]., f 56;

An OSC address with a comma-separated list of strings enclosed in curly braces matches any of the strings in the list., f 40;

'*' is a wildcard, here it matches any single address. It can also be used, f 74;

The OSC specifications have special characters that behave in particular ways when you send or receive messages. Here we show how [osc.route] is able to deal with such specifications. If you send OSC messages from Pd, the receiver application should also comply to these specifications., f 78;


## `osc.send`

[osc.send] sends OSC messages over the network and is an abstraction based on [osc.format] and [netsend]. A connect message expects a list with address and port. The port is a symbol (either 'localhost' or an IP address) but it's optional. If no address is given, it defaults to 'localhost'. A connect message will disconnect and reconnect to the new address/port and a 'disconnect' message closes the connection. The [osc.send] object sends OSC messages to [osc.receive] objects with a matching port., f 70;


## `oscbank~`

Another way to deal with the partial list is to make it a frequency list in hertz and then treat the input as a ratio mulitiplier. By default, this multiplier is '1', by the way., f 53;

The lists can be updated via the inlet and there is a ramp time in ms to transition between the changes of partial, decay and amplitude lists. By default, this ramp is set to 10 ms., f 53;

-amp <list>: sets list of amplitudes for all oscillators (default all 1), f 73;

-phase <list>: sets list of phases for all oscillators (default all 0), f 73;

-rampall <float>: sets a ramp time for all oscillators (default all 10), f 73;

The "-mc" flag or message sets to multichannel output, where each oscillator in the bank is in a different channel., f 30;

[oscbank~] is a bank made of [sine~] objects. It has a list of partials for each oscillator and a frequency multiplier in the inlet (which can be thought of as the fundamental). If you use flags, the number of elements in the list (such as amplitude list) sets the number of oscillators in the bank, and you must not use regular arguments in this case. There's also support for multichannel output., f 81;

There are two ways to deal with the frequency multiplier, the main one is to make it the fundamental as in here, f 38;

-partial <list>: sets list of partials for all oscillators (default all 1), f 74;


## `osci3d~`


## `oscnoise~`

Syncing the phase with control messages is useful for LFOs and control with MIDI. A sync with audio is useful for the "hard sync" technique, where an oscillator is synced according to the frequency of a master frequency., f 56;

Additionally, you can reset the oscillator with an impulse signal. Inputs that are > 0 and <= 1 reset the phase Pdexpects an impulse signal for syncing. The impulse values need to be > 0 and <= 1 (otherwise ignored). Because phase is cyclical, the value of 1 represents the "phase 0" of the cycle, where the impulse occurs. Send it impulses above and check the result. Use a multiplier to reset to another phase value.;

The "phase sync" inlet is quite different from the "phase offset" inlet. They are completely independent!, f 43;

Soft sync is also possible with the '-soft' flag or the "soft" message, where it alternates between positive and negative frequencies and sounds less harsh.;

The second inlet resets the phase ands behaves in the same way for control data as objects like [osc~] and [phasor~] in Pd. A number input resets the oscillator and restarts the cycle with an initial phase that corresponds to the input number, so the internal phase is synced to the given value. The phase values are from 0 to 1 and values beyond that are wrapped within this range. The control message reset is meaningful for LFOs.;

The second argument sets an initial phase (or "phase offset"). This is also settable with the third inlet. This allows you to control two oscillators with the same frequency falling in and out of phase. Another feature is phase modulation., f 53;

The phase values are wrapped into the 0-1 range, since the phase cycle is from 0 to 1 (where 1 is also the start of another cycle).;

By default, frequency input is in hertz, but if you use the 'midi' message or '-midi' flag you can change it to MIDI pitch input, where it is not really bound to the 0 to 127 range, neither it has to be integers. This is just like using [mtof~]...;

[oscnoise~] is an oscillator that accepts negative frequencies, has inlets for phase sync and phase modulation. The waveform is a table filled with white noise. A bang updates the noise table., f 64;


## `out.mc~`

- scaling mode: 0 (quartic, default), 1 (dB) or 2 (linear), f 60;

You can also set a ramp time for the slider value, the default is 20 ms and the minimum is 5 ms. This also affects the slider value input in the right outlet.;

The left inlet also sets several controls: slider value, mute, DSP on and off, scaling modes, maximum gain and ramp time.;

[out.mc~] allows you to switch the DSP engine on or off, [dac~] output on or off and mute/unmute without any clicks!;

If the DSP is on when you load [out.mc~], it checks the DSP state and loads the GUI accordingly.;

[out.mc~] has 3 scaling modes for its slider (the default is "quartic"). You can set a linear gain multiplier, which needs to be greater than zero and also represents the maximum linear gain achieved.;

- scaling mode: 0 (quartic, default), 1 (dB) or 2 (linear), f 60;

The graph to the left shows us how the scaling modes work. A linear scaling doesn't really do anything, the input is the same as the output. We have then two non linear modes:;

dB: This mode adopts a decibel scale with a range of 100 dB (using the [dbtorms~] object)., f 55;

Quartic (default): This mode just gets the slider values to the power of 4 (so, for instance, an input slider value of 0.5 becomes 0.125)., f 57;

The gain value is a simple multiplier to the output value of the slider and determines the maximum linear gain output regardless of the scaling mode. For example, "2" will output the double of the input amplitude, and "0.5" half of it. This is useful if your input isn't loud enough, if it is too high or even if you're using multiple [out1~] routed to the same channel output as they all add up.;

By default, [out.mc~] routes from [dac~ 1], but you can change it with the -ch flag to route it from other outputs., f 52;

[out.mc~] takes multichannel signals and outputs them from given [dac~] channel output (default 1). It has controls for mute, DSP on/off, ramp time, maximum gain and scaling mode., f 65;


## `out4~`

- scaling mode: 0 (quartic, default), 1 (dB) or 2 (linear), f 60;

The rightmost inlet sets several controls: slider value, mute, DSP on and off, scaling modes, maximum gain and ramp time.;

You can also set a ramp time for the slider value, the default is 20 ms and the minimum is 5 ms. This also affects the slider value input in the right outlet.;

[out4~] allows you to switch the DSP engine on or off, dac~ output on or off and mute/unmute without any clicks!;

If the DSP is on when you load [out4~], it checks the DSP state and loads the GUI accordingly.;

[out4~] has 3 scaling modes for its slider (the default is "quartic"). You can set a linear gain multiplier, which needs to be greater than zero and also represents the maximum linear gain achieved.;

- scaling mode: 0 (quartic, default), 1 (dB) or 2 (linear), f 60;

The graph to the left shows us how the scaling modes work. A linear scaling doesn't really do anything, the input is the same as the output. We have then two non linear modes:;

dB: This mode adopts a decibel scale with a range of 100 dB (using the [dbtorms~] object)., f 55;

Quartic (default): This mode just gets the slider values to the power of 4 (so, for instance, an input slider value of 0.5 becomes 0.125)., f 57;

The gain value is a simple multiplier to the output value of the slider and determines the maximum linear gain output regardless of the scaling mode. For example, "2" will output the double of the input amplitude, and "0.5" half of it. This is useful if your input isn't loud enough, if it is too high or even if you're using multiple [out4~] objects as they all add to the same output.;

[out4~] is a convenient quadraphonic input/output abstraction. It has controls for mute, DSP on/off, ramp time, maximum gain and scaling mode. Note that you need to specify at least 4 output channels in preferences => audio., f 62;


## `out8~`

- scaling mode: 0 (quartic, default), 1 (dB) or 2 (linear), f 60;

The rightmost inlet sets several controls: slider value, mute, DSP on and off, scaling modes, maximum gain and ramp time.;

You can also set a ramp time for the slider value, the default is 20 ms and the minimum is 5 ms. This also affects the slider value input in the right outlet.;

[out8~] allows you to switch the DSP engine on or off, dac~ output on or off and mute/unmute without any clicks!;

[out8~] has 3 scaling modes for its slider (the default is "quartic"). You can set a linear gain multiplier, which needs to be greater than zero and also represents the maximum linear gain achieved.;

If the DSP is on when you load [out8~], it checks the DSP state and loads the GUI accordingly.;

- scaling mode: 0 (quartic, default), 1 (dB) or 2 (linear), f 60;

The graph to the left shows us how the scaling modes work. A linear scaling doesn't really do anything, the input is the same as the output. We have then two non linear modes:;

dB: This mode adopts a decibel scale with a range of 100 dB (using the [dbtorms~] object)., f 55;

Quartic (default): This mode just gets the slider values to the power of 4 (so, for instance, an input slider value of 0.5 becomes 0.125)., f 57;

The gain value is a simple multiplier to the output value of the slider and determines the maximum linear gain output regardless of the scaling mode. For example, "2" will output the double of the input amplitude, and "0.5" half of it. This is useful if your input isn't loud enough, if it is too high or even if you're using multiple [out8~] objects as they all add to the same output.;

[out8~] is a convenient octaphonic input/output abstraction. It has controls for mute, DSP on/off, ramp time, maximum gain and scaling mode. Note that you need to specify at least 8 output channels in preferences => audio., f 62;

- incoming signals (routed to [dac~ 2, 3, 4, 5, 6, 7, 8]), f 60;


## `out~`

- scaling mode: 0 (quartic, default), 1 (dB) or 2 (linear), f 60;

The rightmost inlet sets several controls: slider value, mute, DSP on and off, scaling modes, maximum gain and ramp time.;

You can also set a ramp time for the slider value, the default is 20 ms and the minimum is 5 ms. This also affects the slider value input in the right outlet.;

[out~] allows you to switch the DSP engine on or off, dac~ output on or off and mute/unmute without any clicks!;

If the DSP is on when you load [out~], it checks the DSP state and loads the GUI accordingly.;

[out~] has 3 scaling modes for its slider (the default is "quartic"). You can set a linear gain multiplier, which needs to be greater than zero and also represents the maximum linear gain achieved.;

- scaling mode: 0 (quartic, default), 1 (dB) or 2 (linear), f 60;

The graph to the left shows us how the scaling modes work. A linear scaling doesn't really do anything, the input is the same as the output. We have then two non linear modes:;

dB: This mode adopts a decibel scale with a range of 100 dB (using the [dbtorms~] object)., f 55;

Quartic (default): This mode just gets the slider values to the power of 4 (so, for instance, an input slider value of 0.5 becomes 0.125)., f 57;

The gain value is a simple multiplier to the output value of the slider and determines the maximum linear gain output regardless of the scaling mode. For example, "2" will output the double of the input amplitude, and "0.5" half of it. This is useful if your input isn't loud enough, if it is too high or even if you're using multiple [out~] objects as they all add to the same output.;

[out~] is a convenient mono/stereo input and stereo output abstraction. It has controls for mute, DSP on/off, ramp time, maximum gain and scaling mode.;

Connecting a second source to the right inlet makes it a stereo input again and vice-versa., f 38;

[out~] has a built in [sum~] object, so it can take multichannel signals and sum them together for each input., f 37;

If you have just one left input connection into [out~], it sends it to both outputs. This is true either for a single mono channel or a multichannel input., f 33;

So you don't need to bother and connect the same source into the two inlets., f 33;


## `pack2`

the number of elements defines the number of inlets. A float or a symbol will define an initial value (default: two floats set to '0'), f 51;

[pack2] is kinda similar to Pd Vanilla's [pack], but any inlet triggers the output (though a "set" message avoids the output). It can also initialize a symbol value and an element that was initialized as a float can become a symbol and vice versa., f 75;

As other objects in Pd, a list input in the leftmost inlet spreads elements thgoufh the inlets., f 61;


## `pad`


## `pan.mc~`

[pan.mc~] pans an input signal to 'n' specified channels in a multichannel output with equal power crossfading between adjacent channels according to a spread parameter. The speakers are supposedly disposed in a circular setting with equidistant angles. The output selection can then be considered an azimuth angle input whose range is normalized from 0 to 1, where 1 goes back to 0!, f 67;

-radians: set azimuth input to radians (default linear from 0-1), f 64;

1) float - number of output channels (default/min 2, max 4096), f 67;

Spread values greater than 1 spreads the signal to more than 2 adjacent channels. A spread value of two will spread the input to the 2 adjacent channels (to the right and to the left) with an amplidute of the square root of 0.5! Values smaller than 1 narrows the crossfading point closer to the selected channel. A value of 0.5 provides no actual crossfading, meaning that 2 adjacent channels get muted at the mid point. Values smaller than 0.5 are possible and it narrows down even more at the channel center., f 71;

note you can also use signals to set the gain and spread parameters., f 24;

The Sine/Cosine function is used for crossfading and the default spread value of 1 means the usual equal power crossfade between 2 adjacent channels, where the mid point between the 2 channels means both have the same amplitude at square root of 0.5 (0.707107). The gain inlet sets an overall output gain and defaults to 1 if nothing is connected to it., f 71;

The example uses [circle] and an input in radians. It also sets an angle offset., f 41;


## `pan2~`

The '-mc' flag sets to output a multichannel audio containing both stereo signals.;


## `pan4~`

The '-mc' flag sets to output a multichannel audio containing all channels., f 23;


## `panic`

Like a "panic button", [panic] keeps track of raw Note-on messages that weren't switched off and "flushes" them by sending corresponding note-offs when it receives a bang.;


## `pan~`

[pan~] pans an input signal to 'n' specified outlets with equal power crossfading between adjacent channels according to a spread parameter. The speakers are supposedly disposed in a circular setting with equidistant angles. The output selection can then be considered an azimuth angle input whose range is normalized from 0 to 1, where 1 goes back to 0!, f 70;

1) float - number of output channels (default/min 2, max 4096), f 67;

-radians: set azimuth input to radians (default linear from 0-1), f 64;

Spread values greater than 1 spreads the signal to more than 2 adjacent channels. A spread value of two will spread the input to the 2 adjacent channels (to the right and to the left) with an amplidute of the square root of 0.5! Values smaller than 1 narrows the crossfading point closer to the selected channel. A value of 0.5 provides no actual crossfading, meaning that 2 adjacent channels get muted at the mid point. Values smaller than 0.5 are possible and it narrows down even more at the channel center., f 71;

note you can also use signals to set the gain and spread parameters., f 24;

The Sine/Cosine function is used for crossfading and the default spread value of 1 means the usual equal power crossfade between 2 adjacent channels, where the mid point between the 2 channels means both have the same amplitude at square root of 0.5 (0.707107). The gain inlet sets an overall output gain and defaults to 1 if nothing is connected to it., f 71;

The example uses [circle] and an input in radians. It also sets an angle offset., f 41;


## `parabolic~`

The second inlet resets the phase ands behaves in the same way for control data as objects like [osc~] and [phasor~] in Pd. A number input resets the oscillator and restarts the cycle with an initial phase that corresponds to the input number, so the internal phase is synced to the given value. The phase values are from 0 to 1 and values beyond that are wrapped within this range.;

Syncing the phase with control messages is useful for LFOs and control with MIDI. A sync with audio is useful for the "hard sync" technique, where an oscillator is synced according to the frequency of a master frequency., f 44;

The "phase sync" inlet is quite different from the "phase offset" inlet. This means that the are completely independent., f 43;

Additionally, you can reset the oscillator with an impulse signal. Inputs that are > 0 and <= 1 reset the phase Pdexpects an impulse signal for syncing. The impulse values need to be > 0 and <= 1 (otherwise ignored). Because phase is cyclical, the value of 1 represents the "phase 0" of the cycle, where the impulse occurs. Send it impulses above and check the result. Use a multiplier to reset to another phase value.;

The second argument sets an initial phase (or "phase offset"). This is also settable with the third inlet. This allows you to control two oscillators with the same frequency falling in and out of phase. Another feature is phase modulation., f 53;

The phase values are wrapped into the 0-1 range, since the phase cycle is from 0 to 1 (where 1 is also the start of another cycle).;

Note: When used to modulate the phase, a parabolic oscillator acts like a triangular wave modulating the frequency., f 50;

-midi: sets frequency input in MIDI pitch (default hertz), f 58;

-mc <list>: sets multichannel output with a list of frequencies, f 63;

By default, frequency input is in hertz, but if you use the 'midi' message or '-midi' flag you can change it to MIDI pitch input, where it is not really bound to the 0 to 127 range, neither it has to be integers. This is just like using [mtof~]...;

If the oscillator has a multichannel left input, it outputs the same number of channels. If the secondary inlets have a signal with a single channel for sync and phase modulation, the single value is applied to all channels. If a secondary inlet is also a multichhanel signal, then each channel gets its sync or phase deviation value. Note, however, that the number of multichannels in secondary inlets need to match the same number of channels from the left input., f 76;

You can initialize the object with multichannel if you give it a list of frequencies with the -mc flag (you can't set phases though). A list input also works if no signal is connected to set it to multichannel with a list of frequency input., f 49;

[parabolic~] is a parabolic oscillator that accepts negative frequencies, has inlets for phase sync and and phase modulation. A parabolic waveform is similar to a sinusoid but it is not band limited (has aliasing). This oscillator has support for multichannels., f 73;


## `pattern`

You can set tempo as a flag, and the '-i' flag outputs the index of the note durations (positive and negative), which you can use to query for a sequence in the [sequencer] object, for instance., f 50;

Please also check [score2] where you can set durations and pitches (or whatever you want) in a single object., f 40;

The right outlet gives the following information; 'stop' - when the sequence stops; 'start' - when it (re)starts; 'bar <float, float>' - bar number and total number of tempos; 'dur <float>' - duration of notes (negative when it's a rest), f 62;

The note durations are specified either as fractions of a whole note or the resulting float value itself. Hence: 1/4 (or 0.25) is a fourth note and 1/8 (0.125) is an eight note and so on. Tuplets are defined as, for instance, 1/6 (a fourth note triplet). Hence, 1/12 is an eight note triplet. More about tuplets and stuff in the next subpatch on the parent., f 69;

Note that tempos don't need to add to integer values so you can use tuplets arbitrarily., f 30;

Any crazy thing goes, you can have '1.23/(7.78/2.33)' or whatever. It'll work even if you don't have a clue on what the result is., f 67;

You can also see and read more about note durations in the help files of [metronome] and [score]., f 72;

Besides multiples of '2' as the denumberator you can also use other values. For instance '2/3' means two beats of '1/3' of a whole note. This would then be the same as a triplet of a half note. On the other hand '3/5' is 3 beats of a 4th note quintuplet., f 64;

If you wish you can use the actual float values, where '0.375' is one beat and a half (the same as a dotted 4th note). One way to define this as a fraction is '3/8' (which represents three 8th notes). You can use non integers as part of fractions such as '1/2.66667', which is also equal to 0.375! You can also have a fraction in the denominator in parenthesis, such as '1/(8/3)', which is also equal to '0.375'., f 64;

The example above is the same as a '2:3' tuplet for 4th notes, which is, again, the same as a dotted 4th note. To get the fraction value, we multiply the '2:3' ratio by 4 (because we want a 4th note tuplet) and get "8/3"! So 1/(8/3) is what you want, which is the same as 3/8. A simpler way is to inverse things and just multiply 1/4 by 3/2!, f 64;

Now let's use an 8:9 tuplet for 8th notes (where we have eight 8th notes in the space of nine 8th notes). So we multiply 8 by "9:8" and get 9/64., f 64;

Nested tuplets are also possible, where 1/15 is a quintuplet inside a triplet (so we multiply '3' by '5' and get '15'). What if you want to have 7 eight notes in the space of 5? Then you have 5 eight notes (5/8) divided by 7, which is the same as 5/(8*7), so you have 5/56 for each of these notes. You can also have a fraction with the nominator in parenthesis so (5/8). Another way is just do the same as the tuplets above and multiply 1/8 by 5/7! 5 in the space of 3 is then 1/8 * 3/5, which is 3/40., f 67;

[pattern] is a rhythmic pattern sequencer. The note durations are specified as floats or fractions (where '1' is a whole note), negative values are rests! A '|' separates into different bars. When you set a new pattern via the right inlet, it only starts when the previous one ends., f 78;


## `pdlink`

[pdlink] allows you to communicate to/from different Pd instances over local network, as different versions and even forks of Pure Data (such as plugdata). It works like [send]/[receive] (or [else/sender]/[else/receiver]) as it just needs a symbol address. It works via network but it's simpler as it doesn't require network or OSC configuration! It also allows you to communicate to a [pd~] subprocess., f 80;

The '-local' flag only connect over localhost, which means only Pd applications on the same computer. By default, it connects to any Pd application that it can find in your network.;

For troubleshotting, if [pdlink] is not sending or receiving messages, here's some things you can try:, f 53;

- Make sure you don't have multiple active network adapters as [pdlink] may pick the wrong one;

- Disable any firewalls you have enabled, either on your computer or router, f 59;

- Check if a regular OSC connection does work. If so, please report a bug!, f 59;

The '-debug' flag prints information for you to debug and check the connection status and other important info., f 58;


## `pdlink~`

The '-local' flag only connect over localhost, which means only Pd applications on the same computer. By default, it connects to any Pd application that it can find in your network.;

For troubleshotting, if [pdlink] is not sending or receiving messages, here's some things you can try:, f 53;

- Make sure you don't have multiple active network adapters as [pdlink] may pick the wrong one;

- Disable any firewalls you have enabled, either on your computer or router, f 59;

- Check if a regular OSC connection does work. If so, please report a bug!, f 59;

The '-debug' flag prints information for you to debug and check the connection status and other important info., f 58;

If audio has too much latency, try a smaller value for the -bufsize, flag (like 128 or 256). If audio has too many dropouts or clicks, try a larger bufsize value (like 2048 or 4096). If your network connection cannot keep up with the traffic, try passing in the -compress flag, which helps., f 58;

You can set the buffer size with the -buffer flag, where higher values increase latency but also improve connection stability.;

[pdlink~] allows you to send/receive audio streans to/from different Pd instances, as different versions, platforms and even forks of Pure Data (such as PlugData). It works like [send~]/[receive~] as it just needs a symbol address. It works via network but it's simpler as it doesn't require network configuration! It also allows you to communicate to a [pd~] subprocess. You can make up to 16 sends to a single receive, but you can receive as many times as you like., f 78;


## `pdlua`

[pdlua] registers a loader that allows Pd externals written in Lua (with the .pd_lua extension) to be loaded. To guarantee Pd will load these externals, you should load [pdlua] as a library, either at startup or with [declare]:, f 80;

The [hello] object above is loaded from a 'hello.pd_lua' file. You can also provide help files for it and right click on it to ask for them. Right click also allows you to open the .pd_lua file if your system has a known application for it., f 80;

If you also create [pdlua] as an object as below, a global interface is created to load and run "*.lua" files via the 'load' message. Make sure that Pd is aware of the paths where your .pd_lua externals and .lua files are - you can also use declare for this (see that above we also include '-path pdlua' so it finds the 'hello' external and its help file)., f 80;

The Lua loader included in -lib pdlua allows externals for Pd to be written in the Lua programming language. (www.lua.org), f 65;

If you try to create an object [foo] in Pd, Pd checks if the class "foo" exists. If it doesn't, it tries to load an external file that "probably" will contain code for "foo". The Lua loader adds support for loading "foo.pd_lua" when you try to create [foo]., f 65;

This creates a new Pd class called "foo". The 'local' declaration is optional, but recommended -- without it, 'foo' is global, which means any Lua code can modify it (possibly by accident)., f 61;

The first expression/statement in the text file "foo.pd_lua" should be of the form:;

Then you can add methods to the Pd class. The most important one is 'initialize', which is executed when a new object is created:, f 65;

'sel' is the class name, 'atoms' are the creation arguments in a Lua table. For example a Pd object, f 61;

Being a method, 'initialize' has a 'self' variable (which is the object to be created), and if you want your objects to have inlets or outlets you need need to set those fields in this method (Pd doesn't support changing the number of inlets or outlets after an object is created):;

The return value of 'initialize' is used to allow objects to fail to create (for example, if the creation arguments are bad). Most of the time you will 'return true', but if you really can't create then you can 'return false'.;

The 'finalize' method is called when the object is deleted by Pd. You can clean up stuff here if needed. The default implementation does nothing.;

Remember to clean up your receivers in object:finalize(), or weird things will happen., f 57;

You can bind methods to clocks, for timing based on Pd's logical clock.;

Remember to clean up your clocks in object:finalize(), or weird things will happen.;

You can bind methods to receivers, to get messages from [send receiver]., f 52;

Each inlet should have at least one method that will be called when an item it can handle arrives at that input.;

The name of the method is constructed as "in_n_selector" where n is the inlet number (starting from 1) and selector is a type such as "float" or "bang", or a selector name such as "start". Here is a float method for [foo] inlet 1:;

pd.send("receiver", "selector", {"a", "message", 1, 2, 3});

If you need to do things after the Pd object is created, but before control is returned to Pd, (such as registering receivers or clocks) you can use the 'postinitialize' method:;

This will allow the object to be highlighted from Pd's menu using Find->Find Last Error.;

(modified from doc/examples/pdlua/lua.txt by mrpeach 2011/10/06), f 64;

Find basic instructions/examples below on how to write externals in Lua. For further details, see 'pd-lua-intro.pdf' in the 'pdlua/tutorial' folder. You can also find this tutorial online at: https://agraef.github.io/pd-lua/tutorial/pd-lua-intro.html, f 66;

You can receive mouse events by defining the "mouse_down", "mouse_up", "mouse_move" and "mouse_drag" functions. Both pass the x, y coordinates as arguments. For example:;

pdlua's graphics allow you to draw basic vector graphics and receive mouse events on pure-data and plugdata. Drawing functions need to be called on the graphics context class, which is passed into the paint() function as the first argument., f 72;

Graphics mode is enabled automatically by defining the paint method, see below. You can also set the size in the constructor (or in any other function), like this:;

pd:Class:mouse_down(x, y); pd:Class:mouse_up(x, y); pd:Class:mouse_move(x, y); pd:Class:mouse_drag(x, y);; pd:Class:set_size(w, h); width, height = pd:Class:get_size();; pd:Class:repaint(); pd:Class:paint(g);; g:set_color(r, g, b, a=1.0);; g:fill_ellipse(x, y, w, h); g:stroke_ellipse(x, y, w, h, line_width); g:fill_rect(x, y, w, h); g:stroke_rect(x, y, w, h, line_width); g:fill_rounded_rect(x, y, w, h, corner_radius); g:stroke_rounded_rect(x, y, w, h, corner_radius, line_width);; g:draw_line(x1, y1, x2, y2); g:draw_text(text, x, y, w, fontsize);; g:fill_all();; g:translate(tx, ty); g:scale(sx, sy); g:reset_transform();; p = Path(x, y); p:line_to(x, y); p:quad_to(x1, y1, x2, y2); p:cubic_to(x1, y1, x2, y2, x3, y); p:close_path();; g:stroke_path(p, line_width); g:fill_path(p);, f 58;

-- Mouse down callback, called when the mouse is clicked; -- Mouse up callback, called when the mouse button is released; -- Mouse move callback, called when the mouse is moved while not being down; -- Mouse drag callback, called when the mouse is moved while also being down;; -- Set object size; -- Get object size;; -- Request a repaint, after this the "paint" callback will occur; -- Paint callback The argument "g" is the graphics context that you can call these drawing functions on:; -- Sets the color for the next drawing operation. Colors are in range 0-255, optional alpha is in range 0-1;; -- Draws a filled ellipse at the specified position and size.; -- Draws the outline of an ellipse at the specified position and size.; -- Draws a filled rectangle at the specified position and size.; -- Draws the outline of a rectangle at the specified position and size.; -- Draws a filled rounded rectangle at the specified position and size.; -- Draws the outline of a rounded rectangle at the specified position and size.;;; -- Draws a line between two points.; -- Draws text at the specified position and size.;; -- Fills the entire drawing area with the current color. Also will draw an object outline in the style of the host (ie. pure-data or plugdata);; -- Translates the coordinate system by the specified amounts.; -- Scales the coordinate system by the specified factors. This will always happen after the translation; -- Resets current scale and translation;; -- Initiates a new path at the specified point.; -- Adds a line segment to the current path.; -- Adds a quadratic Bezier curve to the current path.; -- Adds a cubic Bezier curve to the current path.; -- Closes the current path.;; -- Draws the outline of the current path with the specified line width.; -- Fills the current path.;, f 115;


## `peak~`

The optional creation arguments are the analysis window size in samples, and the 'hop' period (the number of samples between analyses). The hop size only affects the result output frequency. With a smaller hop period, you get more frequent updates.;

It's common that both of these parameters are multiples of the DSP block size, and that the hop size is a fraction of the window size, although none of this is enforced.;

Nonetheless, the shortest output period (hop size) won't effectively be less than the block size, and, obviously, the output can only happen at block boundaries, not in between. Another constrain is that there is a minimum hop period that depends on the window size. It'll always be at least one block bigger than 1/32 of the window size. This is all also true for [env~], by the way.;

The set message changes the analysis parameters and takes up to 2 arguments, which are, like in the object creation, the window and hop size. The default values are also the same as creating the object, so if you give it only one value for the window size, half of it will be the hop size. Note that it won't let you set the window or hop size to anything smaller than the current block size.;

The [peak~] object is based on [env~] and has a similar analytical structure.;

[peak~] is similar to Pd Vanilla's [env~], but it reports the peak amplitude value in linear (default) or dBFS.;


## `peekbag`

The bag object takes (value, flag) pairs. If the flag is true (nonzero), the value is added to the collection; if false, it's removed. The collection may have many copies of the same value. You can output the collection (and empty it) with a "flush" message, or just empty it with "clear." You can use this to mimic a sustain pedal, for example.;

Use a "bang" to take a peek at the bag's content without clearing it, use "aslist" to get the bag's elements in a single list.;


## `perlin~`

seed <float> - a float sets seed, no float sets a unique internal, f 65;

Pseudo random number generators like [white~] aren't true random number generators. Instead, an algorithm is used to provide a sequence of numbers that seems random. The same sequence can be reproduced if you set a "seed" value, which can be any integer number., f 52;

You can set a seed to [perlin~]'s [white~] noise. Seeds are kept locally, which means that if two objects are seeded the same they will have the same output. Conversely, you can seed the same object twice with the same seed to repeat the output., f 52;

You can also set a seed with the argument. If you don't supply it, each object gets its own internal seed. If you send a 'seed' message without float, the object also gets a unique seed value., f 52;

[perlin~] is an abastraction that implements 1-dimensional Perlin Noise (a type of gradient noise developed by Ken Perlin). It uses [white~] as a noise source into a sample and hold function and generates smoothened functions according to a frequency value in hertz (values under 0 and above nyquist are aliased)., f 71;


## `pgm.in`

An argument sets the channel number. If so, only MIDI messages that correspond to that channel are sent. If no channel is given, it loads "0" as the default and the object operates in omni mode, where the objects outputs values from all channels and the channel number is output in the right outlet. You can also change the channel with the right inlet (0 sets to omni)., f 67;

Port number is encoded as the channel number. Channels 1 to 16 are for port 1, channels 17 to 32 is the same as channels 1 to 16 for port 2, channels 33 to 48 represents channels 1 to 16 in port 3, and so on..., f 63;

The left inlet provides and "external" source of raw MIDI data input. This is needed if you have, for instance, the [midi] object from ELSE reading a MIDI file or something. If, by any chance, you just want the object to receive from this external source and not listen to the internal connected device, you can use the '-ext' flag or 'ext' message, to force only the external input.;

The object automatically listens to whatever is connected as a MIDI device in Pd. So it's like it has a built in [midiin] object feeding its inlet. This is considered to be an "internal" source., f 59;

[pgm.in] extracts MIDI Program information from raw MIDI input or a connected MIDI device. Unlike vanilla's [pgmin] and [pgmout], the program change values are from 0 to 127!, f 68;


## `pgm.out`

[pgm.out] formats and sends raw MIDI program messages to Pd's MIDI output and its outlet. An argument sets channel number (the default is 1). Unlike vanilla's [pgmin] and [pgmout], the program change values are from 0 to 127!, f 72;

The object automatically outputs to whatever is connected as a MIDI device in Pd. So it's like it has a built in [midiout] object. If, by any chance, you just want the object to output to the outlet (for feeding a [midi] object or something), you can use the '-ext' flag or 'ext' message., f 61;


## `phaser.m~`

This is just a wrapper around [phaser~] from ELSE, check it out., f 22;

this is still a simple module, with no CV input yet, so kinda like a pedal still., f 22;


## `phaser~`

[phaser~] is a mono phaser effect abstraction. You can set the number of stages with the first argument, which sets the order of the internal allpass filter (needs to be a multiple of 2). It requires a signal LFO to control the frequency sweep., f 71;


## `phaseseq~`

[phaseseq~] takes a list of thresholds and outputs impulses when reaching the threshold values., f 62;

You can also use [pimp~] so you can have a separate impulse for the head of the tempo, but note that a value of '0' also works for that in [phaseseq~]., f 51;


## `phasor`


## `pi`

[pi] calculates and outputs the value of pi. It receives a multiplier value via the argument or second inlet, which needs to be greater than 0 (otherwise it's considered as 1).;

[pi] can take a [value] name as the second argument or as the first argument (since the first float argument is optional). You can then retrieve this value in another [value] or [var] object or inside an expressionin [expr], f 58;

[pi] outputs the result when loading a patch and also when receiving a bang. Since it's an abstraction with [loadbang], it load output comes before other [loadbang] objects in the patch.;


## `pic`

Note that when you set a receive or send symbol, the corresponding inlet/outlet does not get drawn when you're in edit mode. This is an indicative that the object has a send or receive symbol., f 57;

You can set send/receive names with the -send/-receive flags or the 'send'/'receive' messages - make sure to escape "\$0" properly with backslashes (as in: "\\\$0"). Setting these to 'empty' removes the send/receive symbols., f 67;

Note that inside the properties window you don't need to escape the special characters of "$" and also spaces, both of which are allowed. Also note that other special characters are not allowed, such as braces, backslashes, commas and semicolons., f 69;

Using [pic] to create toggle on/off buttons. See subpatch below:, f 35;

NOTE: you can also connect the bang output into a counter and make it go through a sequence of images and emulate an animated gif for instance., f 37;

Another idea is that you can also adapat the patch above to behave like a bang with a flash time. See below., f 41;

The examples to the left are using pic in the default "bang mode"., f 36;

Below we have the [pic] object into the 'latch' mode, where it sends 1 when clicking into the object and a 0 when you release the mouse button. This way you can program it to load different images for each state., f 36;

Now please get into and out of edit mode so you can see how the [pic] object creates an outline and inlet/outlet when you're in edit mode., f 50;

When you have an empty filename or an error opening a file (via properties window, flag or message), [pic] loads a default image of a question mark:, f 51;

Note that once you have a loaded image, setting the filename to "empty doesn't draw the question mark image back., f 50;

For instance, below, we have$0 used in the send symbol. Using something like "\$1" is also possible and useful if you're using the object in an abstraction, then you can load a value passed as an argument into a parameter., f 59;

Note that when you set a receive or send symbol, the corresponding inlet/outlet does not get drawn when you're in edit mode. This is an indicative that the object has a send or receive symbol., f 52;

Also note that all the parameters that you can set by inserting a symbol into a field in the properties window can also load dollar sign arguments (\$0,$1,$2, and so on). Namely, these parameters are: name and send/receive symbols., f 59;

You can always have an outline of the picture (and not only while in edit mode) if you set the outline mode with the 'outline' message, the -outline flag or via properties window, in which case a non zero value sets to outline mode.;

You can set [pic] to report the image size after it loads with the -size' flag or 'size' message. In this case, it sends a list of width and height.;

[pic] loads image pictures that you can interact with. It only works with file types: .gif, .ppm & .pgm. you click on the picture and it sends a bang (default) or 1 when clicking and 0 when releasing (when in latch mode)., f 68;

The open and set messages are basically the same, but opening a file will make pd ask you if you want to save changes when you close the patch. Since this can be an undesired annoyance, you can use the 'set' message instead.;

Nonetheless, inside the properties window you don't need to escape spaces with backslashes. Also note that other special characters are not allowed in the properties window, such as braces, backslashes, commas and semicolons., f 59;

Note you can use backslash to escape spaces in a message so you can open file names that contain spaces. You can also open an image by typing a new file name into the properties window.;

The offset message takes x/y coordinates in pixets to offset the imagem, f 28;


## `pick`

[pick] picks an element from an input message according to an element number. Negative values count from last to the first element. If you ask for an element number out of the range, nothing is output., f 63;


## `pick~`

[pick~] picks a channel from a multichannel connection. The channel is specified via argument or float input and is indexed from 1 (0 gives "none"). Negative values count from last to the first element. If you ask for an element number out of the range, you also get "none"., f 70;


## `pimp`


## `pimpmul~`


## `pimp~`

An impulse oscillator as the input forces hard sync to the phase output., f 51;

The second inlet resets the phase ands behaves in the same way as in [phasor~]. A number input resets the oscillator and restarts the cycle with an initial phase that corresponds to the input number, so the internal phase is synced to the given value. The phase values are from 0 to 1 and values beyond that are wrapped within this range.;

Additionally, you can reset the oscillator with an impulse signal. Inputs that are > 0 and <= 1 reset the phase Pdexpects an impulse signal for syncing. The impulse values need to be > 0 and <= 1 (otherwise ignored). Because phase is cyclical, the value of 1 represents the "phase 0" of the cycle, where the impulse occurs. Send it impulses above and check the result. Use a multiplier to reset to another phase value.;

The "phase sync" inlet is quite different from the "phase offset" inlet. This means that the are completely independent., f 44;

Soft sync is also possible with the '-soft' flag or the "soft" message, where it alternates between positive and negative frequencies and sounds less harsh., f 51;

The second argument sets an initial phase (or "phase offset"). This is also settable with the third inlet. This allows you to control two objects with the same frequency falling in and out of phase. Another feature is phase modulation., f 53;

The phase input values are wrapped into the 0-1 range, since the phase cycle is from 0 to 1 (where 1 is also the start of another cycle).;

[pimp~] is a combination of [phasor~] and [else/imp~] (alias of [else/impulse~]). It's [imp~] with an extra phase output (left outlet). The impulse happens at every phase period start (in both negative or positive frequencies/directions). It also has inlets for phase sync and phase modulation like [imp~].;

[pimp~] is very convenient for both driving a process with its phase output (such as reading a sample or envelope) and also triggering at period transitions other objects or processes (such as with [sh~] below)., f 54;

Since it deals with negative frequencies, the impulse is only sent when leaping from one phase cycle to the next (in either direction). Try smoothly changing the frequency from positive to negative in the slider to the left, pay close attention to the phase output below and litsen to when the impulse happens., f 53;

By default, frequency input is in hertz, but if you use the 'midi' message or '-midi' flag you can change it to MIDI pitch input, where it is not really bound to the 0 to 127 range, neither it has to be integers. This is just like using [mtof~]...;

-midi: sets frequency input in MIDI pitch (default hertz), f 58;

If [pimp~] has a multichannel left input, it outputs the same number of channels. If the secondary inlets have a signal with a single channel for sync and phase modulation, the single value is applied to all channels. If a secondary inlet is also a multichhanel signal, then each channel gets its sync or phase deviation value. Note, however, that the number of multichannels in secondary inlets need to match the same number of channels from the left input., f 76;

You can initialize the object with multichannel if you give it a list of frequencies with the -mc flag (you can't set phases though). A list input also works if no signal is connected to set it to multichannel with a list of frequencies input., f 49;

-mc <list>: sets multichannel output with a list of frequencies, f 63;


## `ping.pong~`


## `pink~`

seed <float> - a float sets seed, no float sets a unique internal, f 65;

You can set the number of frequency bands in octaves. A value of 1 makes it a single band which is plain white noise. For each extra octave, the bandwidth is split in half and the new octaves are 3dB lower than the next lower octave., f 68;

The maximum number of octaves is 40 and the default depends on the sample rate, and it is so that the lowest octave starts close to 20hz. For a sample rate of 44100 this gives us 12 octaves. The more octaves you have, the less bright the overall sound is., f 68;

You can set the number of octaves with the 2nd argument or a float input.;

1) float - number of octaves (default depends on sample rate), f 62;

Pseudo random number generators aren't true random number generators. Instead, an algorithm is used to provide a sequence of numbers that seems random. The same sequence can be reproduced if you set a "seed" value, which can be any integer number., f 52;

You can set a seed with the '-seed' flag. If you don't supply it, each object gets its own seed internal seed. If you send a 'seed' message without float, the object also gets a unique seed value., f 52;

Seeds are kept locally, which means that if two [pink~] objects are seeded the same they will have the same output. Conversely, you can seed the same [pink~] object twice with the same seed to repeat the output., f 52;

The -ch flag or message sets the number of output channels. You can also use the '-mc' flag., f 33;

[pink~] is a pink noise generator, which sounds less hissy than white noise (but not as less as brown~). White noise has constant spectral power, but pink noise has constant power per octave and it decrease 3dB per octave. Like other noise objects, this is based on a pseudo random number generator algorithm. It has support for multuchannels., f 71;


## `pipe2`

[pipe2] is similar to vanilla's pipe. It takes all kinds of messages and delays them., f 68;


## `pitch.shift~`

[pitch.shift~] is a pitch shifter abstraction based on granulation. You can set a transposition factor in cents and a grain size in ms., f 56;


## `plaits.m~`

This is a wrapper around [plaits~] from ELSE, check it out., f 27;

Signal inlets; 0- frequency in midi; 1- trigger; 2- Level; 3- Frequency Modulation; 4- Timbre Modulation; 5- Harmonics Modulation; 6- Morph Modulation;, f 54;

Left inlet also takes the following control messages; - list: if 2 items, 1st sets frequency and 2nd sets trigger and level. 3 elements set <freq, trig, level; - mode <float>: set synth mode (from 0-23); - up: increment mode up; - down: decrement mode down; - left: move mode to the left column; - right: move mode to the right column; - freq: set frequency shift knob in MIDI (-24 to 24); - timbre: set timbre knob; - harmonics: set harmonics knob; - morph: set morph knob; - cuttof: set cuttof knob; - decay: set decay knob; - fm_att: set fm_att knob; - timbre_att: set timbre_att knob; - harm_att: set harm_att knob; - morph_att: set morph_att knob; - midi <float>: set midi toggle; - voices <float>: set number of voices in MIDI mode; - trigger <float>: set trigger toggle in MIDI mode; - level <float>: set level toggle in MIDI mode; - print: print settings on terminal, f 54;

When not in MIDI Mode, you need to feed it signals and if you connect to the trigger input (2nd inlet) you force it into Trigger Mode. Connect to the 3rd inlet sets to level mode input instead. Both Modes make use of an internal LPG (LowPass Gate) with settings for Cutoff and Decay., f 69;

In MIDI mode, you have to enable the Trigger and Level modes via toggles. In this mode you need to set the number of voices for polyphony in the module. When not in MIDI mode, the number of voices is set via the number of channels in the signal input (as usual with MERDA modules)., f 66;

The Trigger Mode sets a percussive envelope and Level mode can sustain while the gate is on., f 26;

Some synthesis modes use both Trigger/Level inputs, they are: 7, 11-15, 18-20 and 23! The LPG only works for modes 7 and 23 out of these and is controlled by the Level input in both cases. More details on each mode in another subpatch., f 27;

Other inlets are for modulations and are controlled by the attenuverter knobs. Unlike the original object, you don't need to activate the modulations via messages. When you connect to these inlets, the modulation becomes active automatically., f 47;

This engine consists of Dust noise processed by networks of all-pass or band-pass filters., f 45;

Sets filter type â reverberating all-pass network below 0.5, then increasingly resonant band-pass filters above., f 57;

Try settings here. Use trigger and level toggles to enable the LPG settings with cutoff and decay., f 34;

Please refer to the Rings manual for more information about modulated/inharmonic string synthesis, and modal resonators., f 45;

This engine and the next one is like a mini-Rings (another module from Mutable Instruments)!, f 39;

Plaits uses a less powerful processor than Rings, limited to 3 voices in inharmonic string modeling mode. Plaits does not allow you to control the position of the excitation, which is set to 25% of the length of the string/bar/tube., f 94;

This mode does not have LPG settings. When the trigger is not enabled, the string/resonator is excited by dust (particle) noise. In trigger mode the string is excited by a short burst of filtered white noise, or by a low-pass filtered click., f 61;

If the level mode is also enabled, the level input controls the accent. If the trigger is disabled and the level input is enabled, it controls the amplitude envelope as usual., f 61;

Please refer to the Rings manual for more information about modulated/inharmonic string synthesis, and modal resonators., f 45;

This engine and the previous one is like a mini-Rings (another module from Mutable Instruments)!, f 41;

Note that Plaits uses a less powerful processor than Rings, limited to 1 voice with 24 partials in modal resonator mode. Plaits does not allow you to control the position of the excitation, which is set to 25% of the length of the string/bar/tube., f 98;

This mode does not have LPG settings. When the trigger is not enabled, the string/resonator is excited by dust (particle) noise. In trigger mode the string is excited by a short burst of filtered white noise, or by a low-pass filtered click., f 61;

If the level mode is also enabled, the level input controls the accent. If the trigger is disabled and the level input is enabled, it controls the amplitude envelope as usual., f 61;

Emulation of another classic bass drum circuit using a frequency-modulated triangle VCO, turned into a sine with a pair of diodes, and shaped by a dirty VCA., f 54;

No fancy acronyms or patented technology here... Just behavioral simulation of circuits from classic drum machines! The emulated drum machine employs a bridged T-network excited by a nicely shaped pulse. The physical and drum models employ their own decay envelope and filter. The internal LPG is disabled for them., f 70;

This mode does not have LPG settings. Use trigger mode for percussive sounds, otherwise you'll get a continuous tone. If just the level mode is enabled, it controls the on/off gate of the continuous tone and its velocity. If both trigger and level mode are on, the level controls the accent., f 57;

Another emulation based on a pair of frequency-modulated sine VCO, mixed with high-pass filtered noise.;

The drum machine emulation employs a bunch of bridged T-networks, one for each mode of the shell, excited by a nicely shaped pulse plus some band-pass filtered noise. The physical and drum models employ their own decay envelope and filter. The internal LPG is disabled for them., f 71;

This mode does not have LPG settings. Use trigger mode for percussive sounds, otherwise you'll get a continuous tone. If just the level mode is enabled, it controls the on/off gate of the continuous tone and its velocity. If both trigger and level mode are on, the level controls the accent., f 57;

Uses three pairs of square oscillators ring-modulating each other, and a clean, linear VCA., f 54;

The recipe is similar for both OUT and AUX: a bunch of square oscillators generate a harsh, metallic tone. The resulting signal is mixed with clocked noise, sent to a HighPass Filter, then to a VCA. OUT uses 6 square oscillators and a dirty transistor VCA. The physical and drum models employ their own decay envelope and filter. The internal LPG is disabled for them., f 67;

This mode does not have LPG settings. Use trigger mode for percussive sounds, otherwise you'll get a continuous tone. If just the level mode is enabled, it controls the on/off gate of the continuous tone and its velocity. If both trigger and level mode are on, the level controls the accent., f 57;

Controls Pulse Width from narrow pulse to full square to hardsync formants, f 38;

Sum of two hardsyncâed waveforms, the shape of which is controlled by MORPH and detuning by HARMONICS. A narrow pulse or wide notch results in silence!, f 52;

This engine is a virtual-analog synthesis of classic waveforms., f 32;

Sets variable saw, from triangle to saw with an increasingly wide notch (this is the 'CSAW' oscillator from the Braids module by Mutable Instruments.;

Try settings here. Use trigger and level toggles to enable the LPG settings with cutoff and decay., f 34;

This engine is an asymmetric triangle waveform processed by a waveshaper and a wavefolder., f 47;

Try settings here. Use trigger and level toggles to enable the LPG settings with cutoff and decay., f 34;

This engine is a simulation of formants and filtered waveforms through the multiplication, addition and synchronization of segments of sine waves., f 63;

Simulation of filtered waveforms by windowed sine waves â a recreation of Braidsâ Z*** models. HARMONICS controls the filter type (Peaking, LowPass, BandPass, HighPass) with smooth variation from one response to another., f 70;

Try settings here. Use trigger and level toggles to enable the LPG settings with cutoff and decay., f 34;

This engine is an additive mixture of harmonically-related sine waves., f 37;

A variant including only the subset of harmonics present in the drawbars of a Hammond organ., f 49;

Controls bump shape from flat and wide to peaked and narrow., f 48;

Try settings here. Use trigger and level toggles to enable the LPG settings with cutoff and decay., f 34;

This engine is wavetable oscillator with 4 banks of 8x8 waveforms, accessed by row and column, with or without interpolation, f 66;

Sets bank selection*. 4 interpolated banks followed by the same 4 banks, in reverse order, without interpolation.;

*Bank A: harmonically poor waveforms obtained by additive synthesis (sine harmonics, drawbar organ waveforms);; Bank B: harmonically rich waveforms obtained by formant synthesis or waveshaping;; Bank C: wavetables from the Shruthi-1 / Ambika, sampled from classic wavetable or ROM playback synths;; Bank D: a joyous semi-random permutation of waveforms from the other 3 banks;;

Sets row index. Within a row, the waves are sorted by spectral brightness, except for bank D which is a mess!, f 57;

Try settings here. Use trigger and level toggles to enable the LPG settings with cutoff and decay., f 34;

This engine outputs Four-note chords, played by Virtual Aanalog or wavetable oscillators. The virtual analogue oscillators emulate the stack of harmonically-related square or sawtooth waveforms generated by vintage string & organ machines., f 66;

Sets waveform. The first half goes through a selection of string-machine like raw waveforms (different combinations of the organ and string "drawbars"), the second half of scans a small wavetable containing 16 waveforms., f 58;

Sets chord type: octave, fifth, sus4, minor, minor 7th, minor 9th, minor 11th, 69, Major 9th, Major 7th, Major.;

Try settings here. Use trigger and level toggles to enable the LPG settings with cutoff and decay., f 34;

Controls crossfading between formant filtering, SAM, and LPC vowels, then goes through several banks of LPC words., f 57;

Sets phoneme or word segment selection. A trigger input triggers the utterance of a word., f 56;

If the FM and timbre modulation input is not active you can use the FM attenuverter to control the intonation and the MORPH attenuverter to control speed of words., f 31;

Try settings here. In this mode, the level input controls the LPG and the trigger triggers the utterance of a word., f 37;

This granular synthesis engine outputs a cloud of grains formed by a swarm of 8 enveloped sawtooth waves., f 57;

Controls grain duration and overlap. grain duration and overlap. When fully up, the grains merge into each other resulting in a stack of eight randomly frequency-modulated waveforms.;

Note: To get a nice "supersaw" waveform, try a moderate amount of pitch randomization and grain density, with full grain overlap.;

Try settings here. Use trigger and level toggles to enable the LPG settings with cutoff and decay., f 34;

Controls the filter response, from LowPass to BandPass to HighPass., f 43;

A variant processed by two band-pass filters, with their separation controlled by HARMONICS., f 46;

This engine is variable-clock white noise processed by a resonant filter. The cutoff frequency of the filter is controlled by the frequency input., f 59;

Try settings here. Use trigger and level toggles to enable the LPG settings with cutoff and decay., f 34;

Sets resonance and filter character - gentle 24dB/octave below 0.5, harsh 12dB/octave above., f 48;

This engine consists of classic waveshapes with filtering., f 59;

Try settings here. Use trigger and level toggles to enable the LPG settings with cutoff and decay., f 34;

Try settings here. Use trigger and level toggles to enable the LPG settings with cutoff and decay., f 34;

Terrain height interpreted as phase distortion (sin(y+z))., f 29;

This engine performs Wave terrain synthesis with continuous interpolation between eight 2D terrains. The output is the direct terrain height (z).;

Try settings here. Use trigger and level toggles to enable the LPG settings with cutoff and decay., f 34;

This engine is a String machine emulation with stereo filter and chorus. Output is predominantly voices '1' & '3'.;

Try settings here. Use trigger and level toggles to enable the LPG settings with cutoff and decay., f 34;

This engine consists of four variable square voices for chords or arpeggios.;

Try settings here. The level mode enables the LPG settings with cutoff and decay. The arpeggiator works when in trigger mode, which supersedes the level mode and notes change at every trigger.;

In trigger mode, The TIMBRE attenuverter controls the envelope shape, where values farther from 0 are shorter., f 40;

This engine consists of two sine wave oscillators modulating each otherâs phase., f 43;

Sets feedback amount. Values above 0.5 sets operator 2 modulating its own phase. Below 0.5 sets operator 1âs phase.;

Try settings here. Use trigger and level toggles to enable the LPG settings with cutoff and decay., f 34;

This engine consists of a 2-voices / 6-operator FM synth with 32 presets for basses/synths, keyboards/plucked, strings/percussions and organs/pads/strings/brass., f 57;

This mode does not have the internal LPG enabled. In trigger mode, the two voices are alternatively triggered and a gate signal in the trigger input controlls the attack and release envelopes (with a sustained sound when the gate is on). If the level mode is also enabled it controls loudness or timbre depending on how each preset is programmed (and if it's disabled it's like this parameter is set to "0.5")., f 74;

If not in trigger mode, a single voice plays as a drone and the MORPH knob allows time-travel along the envelopes and modulations. The level mode can also act in this case., f 74;

This engine consists of 2-voice, 6-operator FM synth with 32 presets for basses/synths, keyboards/plucked, strings/percussions and organs/pads/strings/brass., f 54;

This mode does not have the internal LPG enabled. In trigger mode, the two voices are alternatively triggered and a gate signal in the trigger input controlls the attack and release envelopes (with a sustained sound when the gate is on). If the level mode is also enabled it controls loudness or timbre depending on how each preset is programmed (and if it's disabled it's like this parameter is set to "0.5")., f 74;

If not in trigger mode, a single voice plays as a drone and the MORPH knob allows time-travel along the envelopes and modulations. The level mode can also act in this case., f 74;

This engine consists of 2-voice, 6-operator FM synth with 32 presets for basses/synths, keyboards/plucked, strings/percussions and organs/pads/strings/brass., f 54;

This mode does not have the internal LPG enabled. In trigger mode, the two voices are alternatively triggered and a gate signal in the trigger input controlls the attack and release envelopes (with a sustained sound when the gate is on). If the level mode is also enabled it controls loudness or timbre depending on how each preset is programmed (and if it's disabled it's like this parameter is set to "0.5")., f 74;

If not in trigger mode, a single voice plays as a drone and the MORPH knob allows time-travel along the envelopes and modulations. The level mode can also act in this case., f 74;

This is the link for the original manual from Mutable Instruments:, f 33;

The 3rd row with the last 8 modes are better described here:, f 33;

(But this module has polyphonic capabilities and is much friendlier)., f 37;

This example uses a MIDI Input, note the MIDI toggle on. You then need to set the number of voices (1 voice makes it like [mono]) and can then use the toggles to set Trigger or Level mode. To use signals for Trigger and Level, see below., f 45;


## `plaits~`

This engine consists of Dust noise processed by networks of all-pass or band-pass filters., f 45;

Sets filter type â reverberating all-pass network below 0.5, then increasingly resonant band-pass filters above., f 57;

Try settings here. Use trigger and level toggles to enable the LPG settings with cutoff and decay., f 34;

Please refer to the Rings manual for more information about modulated/inharmonic string synthesis, and modal resonators., f 45;

This engine and the next one is like a mini-Rings (another module from Mutable Instruments)!, f 39;

Plaits uses a less powerful processor than Rings, limited to 3 voices in inharmonic string modeling mode. Plaits does not allow you to control the position of the excitation, which is set to 25% of the length of the string/bar/tube., f 94;

This mode does not have LPG settings. When the trigger is not enabled, the string/resonator is excited by dust (particle) noise. In trigger mode the string is excited by a short burst of filtered white noise, or by a low-pass filtered click., f 61;

If the level mode is also enabled, the level input controls the accent. If the trigger is disabled and the level input is enabled, it controls the amplitude envelope as usual., f 61;

Please refer to the Rings manual for more information about modulated/inharmonic string synthesis, and modal resonators., f 45;

This engine and the previous one is like a mini-Rings (another module from Mutable Instruments)!, f 41;

Note that Plaits uses a less powerful processor than Rings, limited to 1 voice with 24 partials in modal resonator mode. Plaits does not allow you to control the position of the excitation, which is set to 25% of the length of the string/bar/tube., f 98;

This mode does not have LPG settings. When the trigger is not enabled, the string/resonator is excited by dust (particle) noise. In trigger mode the string is excited by a short burst of filtered white noise, or by a low-pass filtered click., f 61;

If the level mode is also enabled, the level input controls the accent. If the trigger is disabled and the level input is enabled, it controls the amplitude envelope as usual., f 61;

Emulation of another classic bass drum circuit using a frequency-modulated triangle VCO, turned into a sine with a pair of diodes, and shaped by a dirty VCA., f 54;

No fancy acronyms or patented technology here... Just behavioral simulation of circuits from classic drum machines! The emulated drum machine employs a bridged T-network excited by a nicely shaped pulse. The physical and drum models employ their own decay envelope and filter. The internal LPG is disabled for them., f 70;

This mode does not have LPG settings. Use trigger mode for percussive sounds, otherwise you'll get a continuous tone. If just the level mode is enabled, it controls the on/off gate of the continuous tone and its velocity. If both trigger and level mode are on, the level controls the accent., f 57;

Another emulation based on a pair of frequency-modulated sine VCO, mixed with high-pass filtered noise.;

The drum machine emulation employs a bunch of bridged T-networks, one for each mode of the shell, excited by a nicely shaped pulse plus some band-pass filtered noise. The physical and drum models employ their own decay envelope and filter. The internal LPG is disabled for them., f 71;

This mode does not have LPG settings. Use trigger mode for percussive sounds, otherwise you'll get a continuous tone. If just the level mode is enabled, it controls the on/off gate of the continuous tone and its velocity. If both trigger and level mode are on, the level controls the accent., f 57;

Uses three pairs of square oscillators ring-modulating each other, and a clean, linear VCA., f 54;

The recipe is similar for both OUT and AUX: a bunch of square oscillators generate a harsh, metallic tone. The resulting signal is mixed with clocked noise, sent to a HighPass Filter, then to a VCA. OUT uses 6 square oscillators and a dirty transistor VCA. The physical and drum models employ their own decay envelope and filter. The internal LPG is disabled for them., f 67;

This mode does not have LPG settings. Use trigger mode for percussive sounds, otherwise you'll get a continuous tone. If just the level mode is enabled, it controls the on/off gate of the continuous tone and its velocity. If both trigger and level mode are on, the level controls the accent., f 57;

Controls Pulse Width from narrow pulse to full square to hardsync formants, f 38;

Sum of two hardsyncâed waveforms, the shape of which is controlled by MORPH and detuning by HARMONICS. A narrow pulse or wide notch results in silence!, f 52;

This engine is a virtual-analog synthesis of classic waveforms., f 32;

Sets variable saw, from triangle to saw with an increasingly wide notch (this is the 'CSAW' oscillator from the Braids module by Mutable Instruments.;

Try settings here. Use trigger and level toggles to enable the LPG settings with cutoff and decay., f 34;

This engine is an asymmetric triangle waveform processed by a waveshaper and a wavefolder., f 47;

Try settings here. Use trigger and level toggles to enable the LPG settings with cutoff and decay., f 34;

This engine is a simulation of formants and filtered waveforms through the multiplication, addition and synchronization of segments of sine waves., f 63;

Simulation of filtered waveforms by windowed sine waves â a recreation of Braidsâ Z*** models. HARMONICS controls the filter type (Peaking, LowPass, BandPass, HighPass) with smooth variation from one response to another., f 70;

Try settings here. Use trigger and level toggles to enable the LPG settings with cutoff and decay., f 34;

This engine is an additive mixture of harmonically-related sine waves., f 37;

A variant including only the subset of harmonics present in the drawbars of a Hammond organ., f 49;

Controls bump shape from flat and wide to peaked and narrow., f 48;

Try settings here. Use trigger and level toggles to enable the LPG settings with cutoff and decay., f 34;

This engine is wavetable oscillator with 4 banks of 8x8 waveforms, accessed by row and column, with or without interpolation, f 66;

Sets bank selection*. 4 interpolated banks followed by the same 4 banks, in reverse order, without interpolation.;

*Bank A: harmonically poor waveforms obtained by additive synthesis (sine harmonics, drawbar organ waveforms);; Bank B: harmonically rich waveforms obtained by formant synthesis or waveshaping;; Bank C: wavetables from the Shruthi-1 / Ambika, sampled from classic wavetable or ROM playback synths;; Bank D: a joyous semi-random permutation of waveforms from the other 3 banks;;

Sets row index. Within a row, the waves are sorted by spectral brightness, except for bank D which is a mess!, f 57;

Try settings here. Use trigger and level toggles to enable the LPG settings with cutoff and decay., f 34;

This engine outputs Four-note chords, played by Virtual Aanalog or wavetable oscillators. The virtual analogue oscillators emulate the stack of harmonically-related square or sawtooth waveforms generated by vintage string & organ machines., f 66;

Sets waveform. The first half goes through a selection of string-machine like raw waveforms (different combinations of the organ and string "drawbars"), the second half of scans a small wavetable containing 16 waveforms., f 58;

Sets chord type: octave, fifth, sus4, minor, minor 7th, minor 9th, minor 11th, 69, Major 9th, Major 7th, Major.;

Try settings here. Use trigger and level toggles to enable the LPG settings with cutoff and decay., f 34;

Controls crossfading between formant filtering, SAM, and LPC vowels, then goes through several banks of LPC words., f 57;

Sets phoneme or word segment selection. A trigger input triggers the utterance of a word., f 56;

If the FM and timbre modulation input is not active you can use the FM attenuverter to control the intonation and the MORPH attenuverter to control speed of words., f 31;

Try settings here. In this mode, the level input controls the LPG and the trigger triggers the utterance of a word., f 37;

This granular synthesis engine outputs a cloud of grains formed by a swarm of 8 enveloped sawtooth waves., f 57;

Controls grain duration and overlap. grain duration and overlap. When fully up, the grains merge into each other resulting in a stack of eight randomly frequency-modulated waveforms.;

Note: To get a nice "supersaw" waveform, try a moderate amount of pitch randomization and grain density, with full grain overlap.;

Try settings here. Use trigger and level toggles to enable the LPG settings with cutoff and decay., f 34;

Controls the filter response, from LowPass to BandPass to HighPass., f 43;

A variant processed by two band-pass filters, with their separation controlled by HARMONICS., f 46;

This engine is variable-clock white noise processed by a resonant filter. The cutoff frequency of the filter is controlled by the frequency input., f 59;

Try settings here. Use trigger and level toggles to enable the LPG settings with cutoff and decay., f 34;

Sets resonance and filter character - gentle 24dB/octave below 0.5, harsh 12dB/octave above., f 48;

This engine consists of classic waveshapes with filtering., f 59;

Try settings here. Use trigger and level toggles to enable the LPG settings with cutoff and decay., f 34;

Try settings here. Use trigger and level toggles to enable the LPG settings with cutoff and decay., f 34;

Terrain height interpreted as phase distortion (sin(y+z))., f 29;

This engine performs Wave terrain synthesis with continuous interpolation between eight 2D terrains. The output is the direct terrain height (z).;

Try settings here. Use trigger and level toggles to enable the LPG settings with cutoff and decay., f 34;

This engine is a String machine emulation with stereo filter and chorus. Output is predominantly voices '1' & '3'.;

Try settings here. Use trigger and level toggles to enable the LPG settings with cutoff and decay., f 34;

This engine consists of four variable square voices for chords or arpeggios.;

Try settings here. The level mode enables the LPG settings with cutoff and decay. The arpeggiator works when in trigger mode, which supersedes the level mode and notes change at every trigger.;

In trigger mode, The TIMBRE attenuverter controls the envelope shape, where values farther from 0 are shorter., f 40;

This engine consists of two sine wave oscillators modulating each otherâs phase., f 43;

Sets feedback amount. Values above 0.5 sets operator 2 modulating its own phase. Below 0.5 sets operator 1âs phase.;

Try settings here. Use trigger and level toggles to enable the LPG settings with cutoff and decay., f 34;

This engine consists of a 2-voices / 6-operator FM synth with 32 presets for basses/synths, keyboards/plucked, strings/percussions and organs/pads/strings/brass., f 57;

This mode does not have the internal LPG enabled. In trigger mode, the two voices are alternatively triggered and a gate signal in the trigger input controlls the attack and release envelopes (with a sustained sound when the gate is on). If the level mode is also enabled it controls loudness or timbre depending on how each preset is programmed (and if it's disabled it's like this parameter is set to "0.5")., f 74;

If not in trigger mode, a single voice plays as a drone and the MORPH knob allows time-travel along the envelopes and modulations. The level mode can also act in this case., f 74;

This engine consists of 2-voice, 6-operator FM synth with 32 presets for basses/synths, keyboards/plucked, strings/percussions and organs/pads/strings/brass., f 54;

This mode does not have the internal LPG enabled. In trigger mode, the two voices are alternatively triggered and a gate signal in the trigger input controlls the attack and release envelopes (with a sustained sound when the gate is on). If the level mode is also enabled it controls loudness or timbre depending on how each preset is programmed (and if it's disabled it's like this parameter is set to "0.5")., f 74;

If not in trigger mode, a single voice plays as a drone and the MORPH knob allows time-travel along the envelopes and modulations. The level mode can also act in this case., f 74;

This engine consists of 2-voice, 6-operator FM synth with 32 presets for basses/synths, keyboards/plucked, strings/percussions and organs/pads/strings/brass., f 54;

This mode does not have the internal LPG enabled. In trigger mode, the two voices are alternatively triggered and a gate signal in the trigger input controlls the attack and release envelopes (with a sustained sound when the gate is on). If the level mode is also enabled it controls loudness or timbre depending on how each preset is programmed (and if it's disabled it's like this parameter is set to "0.5")., f 74;

If not in trigger mode, a single voice plays as a drone and the MORPH knob allows time-travel along the envelopes and modulations. The level mode can also act in this case., f 74;

This is the link for the original manual from Mutable Instruments:, f 33;

The 3rd row with the last 8 modes are better described here:, f 33;

Based on "plaits" by Mutable Instruments, [plaits~] has 24 different synthesis engines., f 29;

The reason that these inputs need to be activated if you want to perform modulation is because these controls can also set syhesis parameters in mode 7 and 23! In Mode 7 (Vowel & Speech Synthesis), the FM attenuverter controls intonation and MORPH attenuverter controls speed of words. In mode 23 (Chiptune), The timbre attenuverter controls the envelope shape. This is explained in details in the next section.;

The frequency modulation is on top of the set frequency. It is exponential FM and goes up or down 5 ocatves in the signal range from -1 to 1 when the attenuverter goes up to the maximum., f 30;

Note you can just use the frequency input to set linear FM instad or perform exponential FM with more accurate controls., f 47;

The other secondary inlets are for signal input modulatios for FREQUENCY, TIMBRE, HARMONICS and MORPH. For Timbre, morph and harmonics, the modulation is above (if positive) and below (if negative) the given settings (0.5 by default). The signal input in these cases are divided by 2 if the attenuverters are set to 1 (so a signal of 1 adds 0.5). There are attenuverter controls for Frequency, Timbre and Morph (but no harmonics, so it's like it's always set to 1). Attenuverters control the amount of signal modulation is applied and the range is from -1 to 1 and negative values invert the polarity. For the cases where you have attenuverters, you need to activate the modulation input (which is off by default) via messages., f 64;

The harmonics inlet is for modulating the 'harmonics' setting and there's no attenuverter or need to activate the signal modulation input., f 48;

(You can also use the '-model' flag to set a model at load time), f 33;

Plaits has an auxiliary audio output with a different sound also depending on the model used. The 'model' message is used to choose between these options., f 82;

The object has 24 synthesis techniques (or 'models'/'engines'). It also contains a built-in LPG (Low-Pass Gate) with cutoff and decay settings (this is explained in the next subpatch). The most basic controls (besides pitch input of course) for all modes are: 'Harmonics', 'Timbre' and 'Morph' and the way they act depends on the chosen engine. Later in this documentation, there are details and examples for every and each mode. Here's just a general operation for fun. Note that whn you choose a mode, the mode name is outut via the rightmost outlet., f 82;

[plaits~] takes signal input for frequency in each mode and you can use it to perform FM. If you have a 'midi' input as above to the right, you get 'exponential FM'. Alternatively, you can have linear FM. Note, however, that [plaits~] has a FM signal inlet input that is explained later in 'modulations'., f 82;

The [plaits~] object is not a 100% faithful port of PLAITS to Pure Data, some changes and adaptations were made. One first and basic changes is that it doesn't just have V/octave input and has 3 distinct frequency input modes instead. By default, the pitch input is in Hertz, but you can change to "midi", "cv" (control voltage). In '-cv' the incoming signal is treated as "volts" and the reference value of 0 volts is "middle C" ("60" in MIDI pitch). The signal is then normalized as if the input from -1 to 1 corresponds to the standard of -5V to +5V and we also consider the "Volts per octave" standard, so you can go down and up 5 octaves with a signal from -1 to +1 (every change of 0.2 is an octave). In MIDI mode, a value input of 0 or less becomes a frequency of 0hz. Use flags to set to a different mode at load time or the messages to change between settings., f 82;

-timbre_active/-freq_active/-morph_active: enable modulation inputs (default disabled), f 87;

-tr_active/-lvl_active: enable trigger/level input (default disabled), f 71;

The 'trigger' message or flag enables 'trigger' mode, where you can feed pulses into the 2nd inlet to trigger a built in LPG (LowPass Gate) with a percussive one shot envelope with no sustain and just a decay stage (see below to the right). The LPG has a frequency cutoff setting and a decay parameter that you can control via messages. Note you can also trigger the object with a list of note on and off messages, as given by [keyboard], [note.in] and [makenote2], for instance (see below to the left). This mode is useful for generating a kind of a percussive sound., f 71;

You can also enable level mode instead, which takes signals in the 3rd inlet or list messages as well. In this case you have a sustained note while the level is active. The level input controls the LPG and provides an attack and sustain stage. The level mode offers a velocity control and the trigger mode doesn't (you can use some hack though like [trighold~] for level control)., f 73;

The 'midi_active" message or flag forces MIDI input to prevail even if there are signals connected for pitch, trigger and level input. A list input of 2 items takes the 2nd item for both the trigger and level values, but you can have a list of 3 values to set both trigger (2nd element) and level (3rd element) independently., f 84;

In modes 11 to 15, the level sets velocity as usual but if the trigger mode is also enabled the level works as an "accent" parameter that shapes the timbre while the trigger triggers a percussive decay envelope., f 62;

In FM modes 18 to 20 you have attack and release envelopes that are controlled by trigger input with a gate on and off, this means that in this case the trigger input can hold a sustained sound when the gate is on. The level input controls loudness or timbre depending on how each preset is programmed., f 62;

The level mode supersedes trigger mode but there are some execptions and in some cases both work together. See the next subpatch for details on each mode and particular examples for each and every one of them. Here's a summary of the exceptions; In mode 23 (Chiptune), only the level input controls the LPG and the trigger mode triggers an arppegiator and supersedes the level mode; In mode 7 (vowel and speech synthesis), The level input controls the LPG and velocity while the trigger mode can work toghether to trigger the utterance of a word; In other modes where trigger and level work together, the LPG is actually disabled (so decay and cutoff settings are ignored). These modes are: 11 (inharmonic string modeling), 12 (modal resonator), 13 (bass drum), 14 (snare drum), 15 (hi hat) and the '6 Op FM' modes (18, 19 and 20)., f 73;

Check the [plaits.m~] module from M.E.R.D.A, which is a much more friendlier object, with a graphical interface, state saving and other conveniences., f 65;


## `plate.rev.m~`

This is just a wrapper around [plate.rev~] from ELSE, check it out., f 29;

this is still a simple module, with no CV input yet, so kinda like a pedal still., f 22;


## `plate.rev~`

[plate.rev~] is a reverb abstraction based on a patch by Tom Erbe implementing the plate reverb model by Dattorro. It has a mono input and stereo output.;


## `play.file~`

If you have a file with less channels than specified (like a mono file in a stereo sampler), the extra channels are silent. Conversely, a file with more channels than specified (like a stereo file in a mono sampler) has its remaining channels ignored.;

If you give an optional float argumewnt as the first argument, it specifies the number of channels. If no float argument and no sound file are given, then the default number of channels is 1 (mono). But if the first optional argument is not given and a file name is given, then the number of channels is the same as the sound file's. The maximum number is 64 channels.;

(optional) channels (default 1 if no file is given, or sound file's if given, max 64), f 44;

[play.file~] reads/plays files from your computer similarly to Vanilla's [readsf~], but it supports more file formats (officialy AAC, AIF, CAF, FLAC, MP3, OGG, OPUS & WAV). It can also browse and play files from web links! Note that the file sample needs to be at the same sample rate as Pd's., f 72;

The browse message loads files from an internet link, this one takes a little while of course..., f 35;

stops if it's playing and opens a file with the symbol name (no symbol opens dialog window), f 54;

streams a file from a link on the web (works for uploaded files as well as live streaming radios and stuff).;


## `player~`

(optional) channels (default 1 if no file is given, or sound file's if given, max 64), f 44;

If you give an optional float argumewnt as the first argument, it specifies the number of channels. If no float argument and no sound file are given, then the default number of channels is 1 (mono). But if the first optional argument is not given and a file name is given, then the number of channels is the same as the sound file's. The maximum number is 64 channels.;

If you have a file with less channels than specified (like a mono file in a stereo buffer player), the extra channels are silent. Conversely, a file with more channels than specified (like a stereo file in a mono buffer player) has its remaining channels ignored.;

Test the main message methods of [player~]. For more details you can also check the documentation of:;

Note that [player~] has a way of knowing the sample rate of the file and adjust the reading speed accordingly if it's different thamn the sample rate Pd is running. The above sound file has a sample rate of 88200 Hz., f 73;

This is because [player~] is completely based on it plus [soundfiler].;

if no float is given, plays whole file. 1st float sets start, 2nd sets end (in ms) and 3rd sets speed rate, f 57;

- non zero enables looping, <0> disables it (default 0), f 59;

-speed <float> (default 100) | -range <f, f> (default 0 1) | -fade <float> (default 0) | -xfade: xfade mode on | -loop: loop mode on, f 74;

[player~] is a convenient abstraction based on [sfload] (so it supports the same file formats, check it's help file) and [tabplayer~]. It's much more versatile than [play.file~]. For instance, you can play in different speeds and backwards., f 74;


## `pluck.m~`

This is just a wrapper around [pluck~] from ELSE, check it out., f 29;

This example uses a MIDI Input, note the MIDI toggle on. You then need to set the number of voices (1 voice makes it like [mono])., f 46;

You can also use signals for pitch in MIDI and trigger. Use [voices~] and [mono~] for that., f 46;


## `pluck~`

The decay time is actually a feedback parameter. Since negative feedback values are allowed, you can insert a negative decay time value. Note that a negative parameter changes the tonal quality significantly.;

And now for some computer music clichÃ© with random generators..., f 32;

The [pluck~] object uses an internal white noise generator as the excitation signal. But if a "-in" flag is given, [pluck~] creates an extra right outlet for the excitation signal. Here we use an impulse instead of the white noise.;

The filter used in the loop is a [lop2~], a 1-pole / 1-zero lowpass filter. By default, the cuttoff frequency is about 7020 hz, which in a 44100 sample rate puts the pole at zero, leaving only a zero at nyquist. This setting is the same as an average of two samples, which was the original filter in the original Karplu-Strong Algorithm. When reaching nyquist for the cutoff, you have no filter action, so it's as if it's been disabled., f 51;

[pluck~] is a Karplus-Strong algorithm with a 1st order lowpass filter in the feedback loop. It takes frequency in hertz or midi, a decay time in ms and a cutoff frequency in hz for the filter. It is triggered by signals at zero to non zero transitions or by lists at control rate., f 77;

Below we have a sequence of impulse values, we can then see how the impulse value determines the amplitude/intensity. A trigger happens when there is a 0 to non 0 transition, and this values determines the maximum amplitude., f 46;

By default, the frequency input is in Hertz, but you can set it to MIDI pitch with the 'midi' message or 'midi' flag., f 44;

You can use lists for a MIDI/control input. It takes note on messages to trigger it (note offs are just ignored) with pitch and velocity (values from 0 to 127 is normalized to 0 to 1 range (float values and values outside this range is possible). You can get note on list messages with objects like [keyboard], [makenote2] and [note.in], f 52;

A list input only works properly if there is no signal connected into the 1st and 2nd inlets. Nonetheless, you can enable 'midi mode' and force a list input even with signal inputs connected in the 1st and 2nd inlets., f 55;


## `pm2~`

Similarly, you also have 'pan' and 'vol' messages and flags. This sets panning (from -1 to 1) for each oscillator or linear volume gain for each oscillator.;

Note that panning and volume levels generate internal ramps of 10 ms at signal rate to reach the values., f 30;

You can set the ratio of each operator with messages, as in 'ratio1' (for operator 1) or 'ratio2' (for operator 2). The 'ratio' or flag message accepts a list for all operators. Similarly the 'detune1' message sets the detuning for operator 1 and so on, and the 'detune' message or flag sets detuning in hz for all as well., f 71;

The operators are sine wavetables oscillators. The input frequency is in hertz but each operator has its own ratio factor according to the input frequency. The default ratio value is "1", so it's the same as the input frequency. You can also define a 'detune' parameter in hz for each operator., f 71;

You can set the modulation index for all possible interactions, which include the operator modulating itself or each other. Use messages 'i'to'j' to set oprator 'i' modulating the input of 'j'. Note that for feedback modulation, there's a mean average filter of 2 samples being applied., f 65;

The 'idx' message or flag sets the modulation index for all values in the modulation matrix. The list is:, f 31;

Here's an example with GUI controls for you to have fun. You can set ratio, detune, level and pan for each operator. The modulation matrix sets the modulation index value for all possibilities. The gray diagonal row represents the 2 operators and the modulation index on how each modulator modulates itself. The bottom left number represents feed forward modulation from operaor 1 to operator 2, while the other right top number sets feedback modulation from operator 2 to operator 1!, f 66;

There are signal inputs to adjust the levels of each operator. use this to include things like envelopes that controls the amplitude of each operator., f 44;

[op2~] is a 2 operators FM (actually phase modulation) synthesizer. Each oscillator can modulate itself and each other., f 69;

The object has multichannel support. If the left input has more than one channel, it outputs the same number of channels in both outlets. If the secondary inlets have a signal with a single channel for the operator's master level, the single value is applied to all channels. If a secondary inlet is also a multichhanel signal, then each channel gets its master level value. Note, however, that the number of multichannels in secondary inlets need to match the same number of channels from the left input., f 70;


## `pm4~`

Similarly, you also have 'pan' and 'vol' messages and flags. This sets panning (from -1 to 1) for each oscillator or linear volume gain for each oscillator.;

Note that panning and volume levels generate internal ramps of 10 ms at signal rate to reach the values., f 30;

You can set the ratio of each operator with messages, as in 'ratio1' (for operator 1) or 'ratio2' (for operator 2). The 'ratio' or flag message accepts a list for all operators. Similarly the 'detune1' message sets the detuning for operator 1 and so on, and the 'detune' message or flag sets detuning in hz for all as well., f 71;

The operators are sine wavetables oscillators. The input frequency is in hertz but each operator has its own ratio factor according to the input frequency. The default ratio value is "1", so it's the same as the input frequency. You can also define a 'detune' parameter in hz for each operator., f 71;

You can set the modulation index for all possible interactions, which include the operator modulating itself or each other. Use messages 'i'to'j' to set oprator 'i' modulating the input of 'j'. Note that for feedback modulation, there's a mean average filter of 2 samples being applied., f 65;

The 'idx' message or flag sets the modulation index for all values in the modulation matrix. The list is:, f 48;

"1to1", "2to1", "3to1", "4to1", "1to2", "2to2", "3to2", "4to2", "1to3", "2to3", "3to3", "4to3", "1to4", "2to4", "3to4", "4to4", f 31;

Here's an example with GUI controls for you to have fun. You can set ratio, detune, level and pan for each operator. The modulation matrix sets the modulation index value for all possibilities. The gray diagonal row represents all 6 operators and the modulation index on how each modulator modulates itself. The bottom left half portion represents feed forward modulation, from operaor 1 to operator 6, while the other right top half sets feedback modulation from operator 6 to operator 1!, f 66;

There are signal inputs to adjust the levels of each operator. use this to include things like envelopes that controls the amplitude of each operator., f 44;

[op4~] is a 4 operators FM (actually phase modulation) synthesizer. Each oscillator can modulate itself and each other., f 69;

The object has multichannel support. If the left input has more than one channel, it outputs the same number of channels in both outlets. If the secondary inlets have a signal with a single channel for the operator's master level, the single value is applied to all channels. If a secondary inlet is also a multichhanel signal, then each channel gets its master level value. Note, however, that the number of multichannels in secondary inlets need to match the same number of channels from the left input., f 70;


## `pm6.m~`

Set modulation index int the matrix. The gray diagonal row represents each oscillator and the index value in this row is for self feedback modulation. The bottom left number boxes are for feedforwad modulation and the top right half is for feedback., f 31;

The left inlet is for pitch in MIDI, the other inlets are for Level inputs of each oscillator and the rightmost if for the master level. If nothing is connected, the level is set to 1 for all secondary inleys but you can connect signals from envelopes and what not., f 31;

A Six Sinusoidal Operators FM (phase modulation) a la DX7 with stereo output!, f 31;

Set ratio for each oscillator, output level of each and their panning for a stereo output. Level and index values are from 0-100. There's also a pitch transposition knob., f 31;


## `pm6~`

Similarly, you also have 'pan' and 'vol' messages and flags. This sets panning (from -1 to 1) for each oscillator or linear volume gain for each oscillator.;

Note that panning and volume levels generate internal ramps of 10 ms at signal rate to reach the values., f 30;

You can set the ratio of each operator with messages, as in 'ratio1' (for operator 1) or 'ratio2' (for operator 2). The 'ratio' or flag message accepts a list for all operators. Similarly the 'detune1' message sets the detuning for operator 1 and so on, and the 'detune' message or flag sets detuning in hz for all as well., f 71;

The operators are sine wavetables oscillators. The input frequency is in hertz but each operator has its own ratio factor according to the input frequency. The default ratio value is "1", so it's the same as the input frequency. You can also define a 'detune' parameter in hz for each operator., f 71;

You can set the modulation index for all possible interactions, which include the operator modulating itself or each other. Use messages 'i'to'j' to set oprator 'i' modulating the input of 'j'. Note that for feedback modulation, there's a mean average filter of 2 samples being applied., f 65;

The 'idx' message or flag sets the modulation index for all values in the modulation matrix. The list is:, f 55;

"1to1", "2to1", "3to1", "4to1", "5to1", "6to1", "1to2", "2to2", "3to2", "4to2", "5to2", "6to2", "1to3", "2to3", "3to3", "4to3", "5to3", "6to3", "1to4", "2to4", "3to4", "4to4", "5to4", "6to4", "1to5", "2to5", "3to5", "4to5", "5to5", "6to5", "1to6", "2to6", "3to6", "4to6", "5to6", "6to6"., f 47;

Here's an example with GUI controls for you to have fun. You can set ratio, detune, level and pan for each operator. The modulation matrix sets the modulation index value for all possibilities. The gray diagonal row represents all 6 operators and the modulation index on how each modulator modulates itself. The bottom left half portion represents feed forward modulation, from operaor 1 to operator 6, while the other right top half sets feedback modulation from operator 6 to operator 1!, f 66;

There are signal inputs to adjust the levels of each operator. use this to include things like envelopes that controls the amplitude of each operator., f 44;

[op6~] is a 6 operators FM (actually phase modulation) synthesizer. Each oscillator can modulate itself and each other., f 69;

The object has multichannel support. If the left input has more than one channel, it outputs the same number of channels in both outlets. If the secondary inlets have a signal with a single channel for the operator's master level, the single value is applied to all channels. If a secondary inlet is also a multichhanel signal, then each channel gets its master level value. Note, however, that the number of multichannels in secondary inlets need to match the same number of channels from the left input., f 70;


## `pm~`

The rightmost input is a phase modulation input for the modulator oscillator., f 41;

The object has multichannel support. If the left input has more than one channel, it outputs the same number of channels in both outlets. If the secondary inlets have a signal with a single channel, the single value is applied to all channels. If a secondary inlet is also a multichhanel signal, then each channel gets its own value. Note, however, that the number of multichannels in secondary inlets need to match the same number of channels from the left input., f 70;

[pm~] is a very basic and simple phase modulation unit, which consists of a pair of sinusoidal oscillators, where one modulates the phase input of another. The modulator frequency parameter is set as a ratio of the carrier frequency. The object has support for multichannel., f 65;


## `pol2car`


## `pol2car~`

[pol2car~] converts polar coordinates (amplitude / phase) to cartesian coordinates (real / imaginary)., f 58;

[pol2car~] is useful for spectral processing in the more intuitive polar form (with amplitude and phase values). This is because when performing spectral analysis in Pd, the signal is in the cartesian form, so we need [car2pol~] and [pol2car~] to convert to and from the polar form in order to perform the FFT and iFFT. Here's the general idea:, f 57;

Multichannel support example. The number of channels need to match!, f 43;


## `polymetro`


## `polymetro~`


## `popmenu`

sets background color in hexadecimal or RGB list (default: #dfdfdf), f 56;

sets foreground color in hexadecimal or RGB list (default: #000000), f 56;

For proper displacement, you need to click outside the menubutton area, near the outline. Another strategy is to select the object and use arrow keys or select a group of objects that contains the [popmenu] and click on another object to move the group around., f 50;

By default, the loaded elements are saved with the patch. A float sets and outputs values, which get clipped to the index range. A "-1" index means no selection and loads a label that you can set (default " "). A 'set' message only sets the value (no output)., f 60;

A 'load' message sets the initial index value (default -1). A load message without a float saves the current index as the load value. In 'savestate' mode, when you save the patch, the current index value becomes the 'load' value. Note that the [savestate] object is needed if you're using [popmenu] in an abstraction for proper state saving in multiple intances. In 'loadbang' mode (default), the "load value" is output at load time.;

by default, [popmenu] has an outline with the same background color. Use "outline 0" message or the '-nooutline' flag to change the display mode. Note that when you are in edit mode the [popmenu] always shows the outline. Inlets and outlets are hidden in run mode but also appear in edit mode. In edit mode the [popmenu] is disabled. It is also disabled if the patch window is out of focus by the way (this is a tcl/tk thing I can't seem to control)., f 62;

The 'fontsize' message sets the font size of the item. The 'bg' and 'fg' parameters set background and foreground color with a hex symbol or a list of RGB values (3 values from 0 to 255). Symbols like "green", "white" and "gray70" is also accepted., f 49;

Note the clicking on the object and dragging can be problematic. I may change this object just so it uses a different strategy. Now it relies on this canvas for the menubutton which is always up front and, if you click on it in edit mode, you can't move like you regularly can while the mouse is held down. Instead it follows the mouse cursor after you release the button and you need to use 'esc' key to get rid of it., f 50;

By default [popmenu] keeps the selected item with the patch when it gets saved. A "keep 0" message or "-nokeep" flag prevents the object from saving the contents., f 31;

The 'mode' message sets the output mode. By default (mode 0), we have the index and in mode 1 we have the selected item (which can be a float or a symbol) and in mode 2 we have a list with both the index and item., f 31;

The 'pos' message sets the position of the popup menu. The default is 0, which is 'bottom' and tries to pop the menu below the button. Mode 1 is 'top', 2 is 'left', 3 is 'right' and 4 pops the menu directly over the button. In the case of below or above, the direction will be reversed if the menu would show offscreen., f 31;

-size <float> | -range <float, float> | -bg <list> | -fg <list> | -nooutline | -receive <symbol> | -send <symbol> | -param <symbol> | -var <symbol> | -load <float> | -pos <float> | -mode <float> | -savestate | -noloadbang | -nokeep, f 68;

When in edit mode, [popmenu] shows its inlet/outlet. The inlet will always be hidden if you have a receive symbol, same with the outlet if you have a send symbol. You can set a send symbol to send messages to a matching [receive] object. A receive symbol makes [send] objects communicate to it., f 58;

If you set send/receive names to "empty" then the symbols are cleared and inlet/outlet are shown again (same if you give an actual empty symbol). Note you need to escape dollar signs with backslashes to set send receive names via messages or flags., f 58;

The 'param' message sets a symbol name before the output message, so you can directly control a parameter in an object without the need to pass through a message box. An "empty" symbol clears it., f 47;

This is particularly useful if you have a 'param' name, in which case you cannot send values to a [value] object with the same 'send' name, for instance., f 42;

HINT: use [var] with [savestate] objects to save the current state of GUIs., f 42;

Use "var' to set a variable and send values to variables in [value] or [var] objects. Note that this is only possible in the default output mode (for index). Also note that you also can do that if you have a send name that matches a variable name, but with the 'var' symbol you bypass sending to a [receive] object and just set the variable directly. Like send/receive, you need to escape dollar signs in messages., f 47;

[popup] is a popup menu GUI. When you click on it, you get a popup menu to choose elements from (symbols or floats). You can choose by clicking on the selected item or via up/down arrow keys and hitting 'enter'. By default, the output is the index, but can also be the element or both., f 28;

- set oputput mode: 0-index (default), 1-item, 2-both, f 58;

depends on output mode: 0 (default) - index, 1 - item, 2 - list of index and item, f 44;

set popup position: 0-bottom (default), 1-top, 2-left, 3-right and 4-over), f 56;


## `power~`

[power~] is a power function waveshaper for signals that extends the usual definition of exponentiation and returns -pow(-a, b) when you have a negative signal input. This allows not only the output of negative values but also the exponentiation of negative values by noninteger exponents., f 68;


## `presets`

load from a preset number. If no float is given, the last set preset number is loaded, f 58;

save to a preset number. If no float is given, the last set preset is saved, f 58;

import presets from a file, no symbol opens dialog window, f 58;

You can set a morph time and a time grain between updates. This smoothens the transition between preset values and work for floats or lists of floats (no symbols, of course).;

The -morph flag and the 'morph' message set both the morph time (default 0) and grain time (default 20). When the time is 0, there's no morphing, so you can turn morphing on and off like this. Alternatively, you can use the -morphtime to just set the morph time., f 60;

You can also set an exponential factor for the interpolation with the -exp flag or 'exp' message.;

If you just want morph one or another preset parameter (that is, not all of them), or use different time/exponential factors, you can use the [morph] object connetected to it. This may also allow you to set different morph times to different parameters.;

You can set to interpolation mode with the 'interp' message or the -interp flag. In this mode, when you change the preset, you can interpolate to it by moving the slider to the opposite end. This works for floats and list of floats (not symbols, of course)., f 62;

You can also set an exponential factor for the interpolation with the -exp flag or 'exp' message., f 62;

If you just want interpolate one or another preset parameter (that is, not all of them), you can use the [interpolate] object connetected to it. Or you can do this if you want to set different exponential factors for each parameter. The interpolation in the [presets] object is performed with [interpolate] itself, so you can check its help file out., f 73;

See how the same abstraction has a different set of presets. You can set a different preset value, then save and reload this example to test it. By the way, the abstraction uses the helper example to use the shift key to change the behaviour of the horizontal radio button., f 63;

The [savestate] object is the Pd Vanilla's way of setting the state of abstractions. This is like setting a separate single 'preset' for each abstraction., f 63;

The [presets] object can be used with [savestate], which tenfolds its saving state possibilities, where each abstraction can have its own separate set of presets. Open an abstraction below to see how this is done with [presets] and [savestate]., f 63;

Below we have a helper subpatch that uses the shift key to change the radio GUI and use it for both a preset selector and a preset saver. If you press and hold "shift" before you click on the GUI, it saves the preset, otherwise it loads them., f 52;

The subpatches below show you how to perform 'morphing' and 'interpolation' between preset values., f 30;

The example below shows you how to use [presets] with abstractions., f 34;

without a float loads the last preset number that was set, f 30;

without a float saves the last preset number that was set, f 30;

The [presets] object is an abstraction based on [text], [savestate] and uses [else/retrieve] to communicate with [receive] objects. Note that it also works with [else/receiver] as in this example and also with built in receive names as shown in the later examples. The way it works is that it gets data from what's connected to [receive] or [receiver] objects that match its arguments and stores it as a preset. When loading the preset, it then sends the data back to the [receive]/[receiver] objects., f 96;

-morph <f, f>: sets morph time and grain (default: 0, 20), f 75;

-interp: sets to interpolation mode (default: no interpolation), f 69;

Preset numbers outside the range from 0 to n-1 are clipped to this range., f 26;

You can change the number of presets with the 'n' message or '-n' flag (the minimum value is 2). The flag initializes the object and give you "-empty-" slots. The 'n' resizes and adds empty slots if the new size is larger than the current number of presets, or deletes the information of the extra slots if smaller., f 80;

The other flags relate to interpolation and morphing. We'll see more about that in the next examples., f 54;

[presets] takes symbols as arguments that need to match receive names to get information from and send to what's connected to them. You need to escape the locality variable with a backslash (as in "\\\$0-n", instead of "\$0-n") because these symbols are also stored in the preset data as the send address., f 80;

By default, [presets] has 64 presets slots marked as "-empty-", which means there is no preset stored. By the way, if you try to load an empty preset, a bang comes out of the right outlet of [presets] to tell you the slot is empty., f 80;

If you load a text file with presets, the number of presets will be the same as it is stored in that file. You can load a file at initialization with the '-file' flag. You can also load a file with the 'read' message., f 80;

If no send address argument is given, [presets] can still load text files with send names to send the data to matching receive objects. But it won't be able to save them unless you give it send addresses via the 'args' message. This way you change the parameters group dynamically and have different presets with different addresses so a single [presets] object is able to manage different parameter groups., f 69;

Note that you could get the array values from vanilla's [array get], but it can't receive and set values, so [else/buffer] is quite useful to get/set preset values for arrays., f 75;

The matching [receive] objects can be connect to anything that is a compiled object (not an abstraction/subpatch) that takes a bang and outputs values. This means you can connect it to GUIs (examples: number or symbol boxes, sliders, else/function) and storage objects ([float], [symbol], [else/message], [else/buffer], etc)., f 76;

A trick to use abstractions or subpatches can be to use the [message] object as to the right. Of course you can have different receive names for each number box in the subpatch, but hey, I'm just giving ideas in case you want it and need it; ), f 43;

The [presets] object can also communicate to built-in receive names of compiled objects. This can be native objects like atom boxes and iemguis (bang, toggle, etc), but also externals (like else/function)., f 69;

In the case of subpatches or abstractions, things get a bit trickier. One thng to do would be to use [else/message] as shown in the last example, but we want to use built-in receive names here. Well, at least for GUI abstraction objects from the ELSE library, you can communicate to them with their built-in receive name thanks to the [else/default] object,, f 69;

The abstractions below are saved with built in receive names that match the [presets] object., f 34;

-exp <float>: sets exponential factor for morph/interpolation (default: 1), f 74;

[presets] manages presets for patches and abstractions and has interpolation and morphing features. Change the number and symbol below, save a preset and the patch, reopen to recall the presets. Use the "read" message to restore to this example's default., f 76;

clicking on the object opens data/edit window (same as 'show'), f 63;


## `presets.m`

Put [presets.m] by last in your patch, save it and reopen. Then you can use the radio buttons to set a preset number and hit bang to save a preset., f 38;

And just like that, via pure ninja magic, all parameters in the MERDA modules in your patch get saved and restored next time you open the patch. The presets get saved with the patch., f 35;


## `properties`


## `ptouch.in`

An argument sets the channel number. If so, only MIDI messages that correspond to that channel are sent. If no channel is given, it loads "0" as the default and the object operates in omni mode, where the objects outputs values from all channels and the channel number is output in the right outlet. You can also change the channel with the right inlet (0 sets to omni)., f 67;

Port number is encoded as the channel number. Channels 1 to 16 are for port 1, channels 17 to 32 is the same as channels 1 to 16 for port 2, channels 33 to 48 represents channels 1 to 16 in port 3, and so on..., f 63;

[ptouch.in] extracts MIDI polyphonic aftertouch information from raw MIDI input (such as from [midiin])., f 62;

The object automatically listens to whatever is connected as a MIDI device in Pd. So it's like it has a built in [midiin] object feeding it. This is considered to be an "internal" source.;

The left inlet provides and "external" source of raw MIDI data input. This is needed if you have, for instance, the [midi] object from ELSE reading a MIDI file or something. If, by any chance, you just want the object to receive from this external source and not listen to the internal connected device, you can use the '-ext' flag or 'ext' message, to force only the external input.;


## `ptouch.out`

[ptouch.out] formats and sends raw MIDI polyphonic aftertouch messages to Pd's MIDI output and its outlet.. An argument sets channel number (the default is 1)., f 66;

The object automatically outputs to whatever is connected as a MIDI device in Pd. So it's like it has a built in [midiout] object. If, by any chance, you just want the object to output to the outlet (for feeding a [midi] object or something), you can use the '-ext' flag or 'ext' message., f 61;


## `pulse`


## `pulsecount~`


## `pulsediv~`


## `pulse~`

The pulse width parameter controls how much of the cycle is "on" or "off". A pulse width of 0.5 means the first half is "on" and the lasr half is "off".;

A pulse width of 0 has the smallest "on" pulse size: a single sample - thus, just like an impulse oscillator!;

Conversely, a pulse width of 1 has the largest (the entire period except the last sample).;

The pulse width is set via the second argument or the second inlet.;

The phase values are wrapped into the 0-1 range, since the phase cycle is from 0 to 1 - where 1 is also the start of another cycle.;

The third argument sets an initial phase (or "phase offset"). This is also settable with the fourth inlet. In such a way, you have two objects with the same frequency falling out and back in sync. Another feature is phase modulation.;

-midi: sets frequency input in MIDI pitch (default hertz), f 58;

-mc <list>: sets multichannel output with a list of frequencies, f 63;

[pulse~] is a pulse train oscillator (alternates between 1 and 0, or on/off) that accepts negative frequencies, has inlets for pulse width, phase sync and phase modulation. It also has support for multichannels., f 66;

Syncing the phase with control messages is useful for LFOs and control with MIDI. A sync with audio is useful for the "hard sync" technique, where an oscillator is synced according to the frequency of a master frequency., f 56;

The "phase sync" inlet is quite different from the "phase offset" inlet. They are completely independent!, f 43;

Soft sync is also possible with the '-soft' flag or the "soft" message, where it alternates between positive and negative frequencies and sounds less harsh.;

Additionally, you can reset the oscillator with an impulse signal. Inputs that are > 0 and <= 1 reset the phase Pd expects an impulse signal for syncing. The impulse values need to be > 0 and <= 1 (otherwise ignored). Because phase is cyclical, the value of 1 represents the "phase 0" of the cycle, where the impulse occurs. Send it impulses above and check the result. Use a multiplier to reset to another phase value.;

The third inlet resets the phase ands behaves in the same way for control data as objects like [osc~] and [phasor~] in Pd. A number input resets the oscillator and restarts the cycle with an initial phase that corresponds to the input number, so the internal phase is synced to the given value. The phase values are from 0 to 1 and values beyond that are wrapped within this range. The control message reset is meaningful for LFOs.;

By default, frequency input is in hertz, but if you use the 'midi' message or '-midi' flag you can change it to MIDI pitch input, where it is bound to the 0 to 127 range (but they don't have to be integers) - this is kinda like using [mtof~]...;

If the oscillator has a multichannel left input, it outputs the same number of channels. If the secondary inlets have a signal with a single channel for sync and phase modulation, the single value is applied to all channels. If a secondary inlet is also a multichhanel signal, then each channel gets its sync or phase deviation value. Note, however, that the number of multichannels in secondary inlets need to match the same number of channels from the left input., f 76;

You can initialize the object with multichannel if you give it a list of frequencies with the -mc flag (you can't set phases though). A list input also works if no signal is connected to set it to multichannel with a list of frequency input., f 49;


## `pvoc.freeze~`


## `pvoc.live~`

[pvoc.live~] is like [pvoc.player~], but for live input. It provides independent time stretching and pitch shifting via granulation., f 69;


## `pvoc.player~`

(optional) channels (default 1 if no file is given, or sound file's if given, max 64), f 44;

opens a file with the symbol name (no symbol opens dialog box) and starts playing, f 52;

float - <1> is the same as "start", "0" is the same as "stop", f 61;

reload - reloads the file into the buffer and starts playing, f 62;

set <symbol> - sets a file to open (needs a reload message), f 68;

range <f, f> - sets sample's playing range (from 0 to 1), f 68;

If you give an optional float argumewnt as the first argument, it specifies the number of channels. If no float argument and no sound file are given, then the default number of channels is 1 (mono). But if the first optional argument is not given and a file name is given, then the number of channels is the same as the sound file's. The maximum number is 64 channels.;

If you have a file with less channels than specified (like a mono file in a stereo buffer player), the extra channels are silent. Conversely, a file with more channels than specified (like a stereo file in a mono buffer player) has its remaining channels ignored.;

[pvoc.player~] is like [player~] but provides independent time stretching and pitch shifting via a phase vocoder (kinda like [pvoc.player~]). Like [player~], it is based on [sfload] and support the same file formats (check its help file). NOTE: THIS OBJECT IS HEAVY ON THE CPU!!!, f 79;


## `pz2coeff`


## `quad~`


## `quantizer`


## `quantizer~`

approximation mode: 0 (round), 1 (int), 2 (floor) or 3 (ceil) - default 0, f 50;

You can set the mode with the second argument, the -mode flag or the mode message. Modes are: 0 (round), 1 (int), 2 (floor) or 3 (ceil) - the default mode is 0 (round)., f 62;

The above objects are like the different modes in [quantizer~] for a setp of 1!, f 40;

ELSE also has the [rint~] object, which quite similar to the 'round' function and is also present in [expr], but 0.5 rounds to 0 instead of 1!, f 62;

[quantizer~] approximates a value to step values defined by the argument. There are 4 approximation modes: round (default), int, floor & ceil. It has support for multichannel signals., f 64;

If the object has a multichannel left input, it outputs the same number of channels. If the secondary inlet has a signal with a single channel, the single value is applied to all channels. If thr secondary inlet is also a multichhanel signal, then each channel gets its quantizing value. Note, however, that the number of multichannels in the right inlet need to match the same number of channels from the left input., f 76;


## `rad2deg`


## `rad2hz`

Use [rad2hz] to convert a signal representing a frequency in "Radians per Sample" to Hertz. This depends on the patch's sample rate (sr). The conversion formula is: hz = rad * sr / 2pi., f 71;


## `rampnoise`


## `rampnoise~`

The [rampnoise~] object produces frequencies limited to a band from 0 up to the frequency it is running. It can go up to the sample rate, and when that happens, it's basically a white noise generator.;

[rampnoise~] can be used to control parameters of other objects. Here we control the frequency of an oscillator.;

Pseudo random number generators aren't true random number generators. Instead, an algorithm is used to provide a sequence of numbers that seems random. The same sequence can be reproduced if you set a "seed" value, which can be any integer number., f 52;

You can set a seed with the '-seed' flag. If you don't supply it, each object gets its own seed internal seed. If you send a 'seed' message without float, the object also gets a unique seed value., f 52;

Seeds are kept locally, which means that if two [rampnoise~] objects are seeded the same they will have the same output. Conversely, you can seed the same [rampnoise~] object twice with the same seed to repeat the output., f 52;

[rampnoise~] is a low frequency (band limited) noise generator with interpolation, therefore it ramps from one random value to another, resulting in random ramps. Random values are between -1 and 1 at a rate in hertz (negative frequencies accepted). Use the seed message if you want a reproducible output. It has support for multichannels., f 59;

-mc <list>: sets multichannel output with a list of frequencies, f 63;

The -ch flag or message sets the number of output channels. This is only meaningful if you have a single channel input., f 42;

You can initialize the object with multichannel if you give it a list of frequencies with the -mc flag (you can't set phases though). A list input also works if no signal is connected to set it to multichannel with a list of frequency input., f 62;

If you have a multichannel connection in the frequency input, [randpulse2~] generates a signal with the same number of channels and the 'ch' message or flag is meaningless. The multichannel input is the density for each output., f 44;


## `ramp~`

If one wants [ramp~] to output a signal with frequency in hertz (oscillating between min and max values), then the increment value should be (max - min) * freq / sr (where freq is the frequency in hz and sr is the sampling rate). Anyway, this makes it wrk like a [phasor~].;

The [ramp~] object loops automatically, you can set different loop points and a reset/restart value outside the loop., f 68;

[ramp~] is very convenient for driving [tabread4~] or [else/table~] as to read samples at different speeds. With an increment of "1", it reads at the original speed, at "2" it reads twice as fast, "0.5" half as fast, and so on. Note it can also play it backwards at different speeds with negative increment values., f 69;

increment = -0.001 / minimum = 0 / maximum = 127 / reset value = 63.5 (also the initial/staring value).;

Also, by default, [ramp~] automatically starts at loading the patch. You can change that with the -off flag (also see the example on the right)., f 49;

Note that the ramp is in wrap mode by default, where it automatically wraps between the min and max values. You can set it to clip mode or reset mode with the -mode flag or message as in the rightmost example., f 49;

You can have a reset point outside the minimum and maximum range. Below, the value is reset to -1, but it wraps around when it falls within the min/max range (when in wrap mode)., f 47;

You can change to "clip" mode, - where it'll clip (or "stop") at the min/max boundaries - or also "reset" mode - where it'll reset back to the reset point and stop after reaching the limits., f 49;

The "start" and "stop" messages starts and stops incrementing. The "reset" message stops and goes back to the reset point. The "set" message sets the reset value and a float input makes [ramp~] jump to that value.;

This examples uses a [*~] start and stop the ramp increment. This allows you to stop and start with sample accuracy. Additionally, we use [status~] to stop and reset the ramp as in the "reset" message, but with sample accurately.;

[ramp~] is a resettable linear ramp between a minimum and maximum value. You can trigger it with a bang or with a trigger signal (non-positive to positive transition)., f 65;


## `rand.dist`

Here we test the random distribution with different iterations. The function was created by [tabgen] and we use the output of [tand.dist] to generate a histogram. Note that the bigger the number of iterations, the closer we get to the original function., f 86;

By default, [rand.dist] loads a unique seed value based on system every time you open the patch. Each copy of the object has its own unique seed. You can set a specific seed that reproduces the same sequence with the 'seed' message or flag, which can be any integer number. A 'seed' message without a float resets the seed to a unique value based on the system time., f 89;

You can use [histogram] to populate a table to be used as a probability density function inside [rand.dist]. Start by feeding it notes., f 48;

An input from 0 to 127 outputs the table's quantile. This can be used to connect another random source, such as from [rampnoise]. Here we use a normal distribution (gaussian) function generated by [tabgen] for the probability density function. Values from [rampnoise] are then mapped to the given probability function and are centered around the middle of the curve., f 69;

[rand.dist] is an abstraction based on [array quantile] and generates random numbers that follow a probability density function (given by an array). A float input (like from an external random source) outputs the array quantile instead. The first argument is the table name containing the probability density function. The output range is from 0 to 127 by default, but you can change that with the 2nd and 3rd argument or the 2nd or 3rd inlet. The output resolution is the range divided by the table maximum index (127 in the example below, so the 0-127 range outputs integers)., f 86;


## `rand.f`

Pseudo random number generators aren't true random number generators. Instead, an algorithm is used to provide a sequence of numbers that seems random. The same sequence can be reproduced if you set a "seed" value, which can be any integer number., f 52;

You can set a seed with the '-seed' flag. If you don't supply it, each object gets its own seed internal seed. If you send a 'seed' message without float, the object also gets a unique seed value., f 27;

Seeds are kept locally, which means that if two [rand.f] objects are seeded the same they will have the same output. Conversely, you can seed the same [rand.f] object twice with the same seed to repeat the output., f 52;

[rand.f] generates random float values for a given range when triggered with a bang. Use the seed message if you want a reproducible output. You can also output lists., f 71;

The '-n' flag or message sets the number of elements to output (default 1)., f 40;


## `rand.f~`

[rand.f~] generates random float values for a given range when triggered. A trigger happens at positive to negative or negative to positive transitions. Use the seed message if you want a reproducible output.;

Pseudo random number generators aren't true random number generators. Instead, an algorithm is used to provide a sequence of numbers that seems random. The same sequence can be reproduced if you set a "seed" value, which can be any integer number., f 52;

You can set a seed with the '-seed' flag. If you don't supply it, each object gets its own seed internal seed. If you send a 'seed' message without float, the object also gets a unique seed value., f 27;

Seeds are kept locally, which means that if two [rand.f~] objects are seeded the same they will have the same output. Conversely, you can seed the same [rand.f~] object twice with the same seed to repeat the output., f 52;

The -ch flag or message sets the number of output channels. This is only meaningful if you have a single channel input., f 43;

If you have a multichannel connection in the trigger inlet, [rand.f~] generates a signal with the same number of channels and the 'ch' message or flag is meaningless., f 44;


## `rand.hist`

The example below, by default, generates a dodecaphonic series. It is the same as:, f 43;

-eq <float>: sets equal number of occurrences for all indexes (default 0), f 73;

By default, [rand.hist] loads a unique seed value based on system every time you open the patch. Each copy of the object has its own unique seed. You can set a specific seed that reproduces the same sequence with the 'seed' message or flag, which can be any integer number. A 'seed' message without a float resets the seed to a unique value based on the system time., f 59;

You can use [keyboard] and the "inc" message to feed and generate the internal histogram. The 'dec' message decreases it. The set message sets index and occurrence. The 'eq' message sets equal occurrences for all indexes. The clear message clears the histogram and is like the 'eq 0' message. The size message clears and resizes the histogram., f 68;

A list input sets a new histogram. Note can also use [histogram] to create a histogram from MIDI note inputs. Use the 'export' message to output a list of occurrences., f 56;

[rand.hist] generates weighted randomnumbers based on a histogram (which specifies how many times an index is output). Below to the left we have a random sequence where 0 has a 30% chance of occurring, 1 has 20% and 2 has 50%. A list sets a new histogram. In "unrepeat" mode, a random sequence is output without repetition, below to the right, the random sequence contains index 0 three times and index 1 twice. When the sequence is finished, a bang comes out the right outlet. In this case, the 'restart' message clears the memory so you can start a new sequence., f 82;


## `rand.i`

Pseudo random number generators aren't true random number generators. Instead, an algorithm is used to provide a sequence of numbers that seems random. The same sequence can be reproduced if you set a "seed" value, which can be any integer number., f 52;

You can set a seed with the '-seed' flag. If you don't supply it, each object gets its own seed internal seed. If you send a 'seed' message without float, the object also gets a unique seed value., f 27;

Seeds are kept locally, which means that if two [rand.i] objects are seeded the same they will have the same output. Conversely, you can seed the same [rand.i] object twice with the same seed to repeat the output., f 52;

The '-n' flag or message sets the number of elements to output (default 1)., f 40;

[rand.i] generates random integer values for a given range when triggered with as bang.Use the seed message if you want a reproducible output. You can also output lists., f 74;


## `rand.i~`

Pseudo random number generators aren't true random number generators. Instead, an algorithm is used to provide a sequence of numbers that seems random. The same sequence can be reproduced if you set a "seed" value, which can be any integer number., f 52;

You can set a seed with the '-seed' flag. If you don't supply it, each object gets its own seed internal seed. If you send a 'seed' message without float, the object also gets a unique seed value., f 27;

Seeds are kept locally, which means that if two [rand.i~] objects are seeded the same they will have the same output. Conversely, you can seed the same [rand.i~] object twice with the same seed to repeat the output., f 52;

The -ch flag or message sets the number of output channels. This is only meaningful if you have a single channel input., f 43;

If you have a multichannel connection in the trigger inlet, [rand.i~] generates a signal with the same number of channels and the 'ch' message or flag is meaningless., f 44;

[rand.i~] generates random integer values for a given range when triggered. A trigger happens at positive to negative or negative to positive transitions. Use the seed message if you want a reproducible output. There's support for multichannels., f 70;


## `rand.list`


## `rand.u`

[rand.u] generates an unrepeated random values (from 0 to size-1). After the whole sequence is output, a bang is sent in the right outlet., f 72;


## `randpulse`


## `randpulse2`


## `randpulse2~`

By default, gate values in [randopulse2~] are "1", but you can set it to random mode with the second argument (non zero value), where it gives you random positive and negative values (in the range from -1 to 1). You can also use the "rand" message to change this.;

Pseudo random number generators aren't true random number generators. Instead, an algorithm is used to provide a sequence of numbers that seems random. The same sequence can be reproduced if you set a "seed" value, which can be any integer number., f 57;

You can set a seed with the '-seed' flag. If you don't supply it, each object gets its own seed internal seed. If you send a 'seed' message without float, the object also gets a unique seed value., f 57;

Seeds are kept locally, which means that if two [randpulse2~] objects are seeded the same they will have the same output. Conversely, you can seed the same [randpulse2~] object twice with the same seed to repeat the output., f 57;

The -ch flag or message sets the number of output channels. This is only meaningful if you have a single channel input., f 42;

You can initialize the object with multichannel if you give it a list of frequencies with the -mc flag (you can't set phases though). A list input also works if no signal is connected to set it to multichannel with a list of frequency input., f 62;

If you have a multichannel connection in the frequency input, [randpulse2~] generates a signal with the same number of channels and the 'ch' message or flag is meaningless. The multichannel input is the density for each output., f 44;

[randpulse2~] is a random pulse train oscillator. It alternates at random intervals according to a "density" parameter, which controls the average frequency. It has support for multichannels., f 65;

-mc <list>: sets multichannel output with a list of frequencies, f 63;


## `randpulse~`

The pulse width parameter controls how much of the cycle is "on" or "off". A pulse width of 0.5 means the first half is "on" and the lasr half is "off".;

A pulse width of 0 has the smallest "on" pulse size: a single sample - thus, just like an impulse oscillator!;

Conversely, a pulse width of 1 has the largest (the entire period except the last sample).;

The pulse width is set via the second argument or the second inlet.;

An impulse into its right inlet forces [randpulse~] to generate a new random value and restart the cycle., f 38;

Pseudo random number generators aren't true random number generators. Instead, an algorithm is used to provide a sequence of numbers that seems random. The same sequence can be reproduced if you set a "seed" value, which can be any integer number., f 57;

You can set a seed with the '-seed' flag. If you don't supply it, each object gets its own seed internal seed. If you send a 'seed' message without float, the object also gets a unique seed value., f 57;

Seeds are kept locally, which means that if two [randpulse~] objects are seeded the same they will have the same output. Conversely, you can seed the same [randpulse~] object twice with the same seed to repeat the output., f 57;

[randpulse~] is a random pulse train oscillator (which alternates between a random value and 0, or on/off). It accepts negative frequencies, has inlets for pulse width and sync. It also has support for multichannels., f 65;

list/signal(s) - frequency in hz for one or more channels, f 67;

-mc <list>: sets multichannel output with a list of frequencies, f 63;

The -ch flag or message sets the number of output channels. This is only meaningful if you have a single channel input., f 42;

If you have a multichannel connection in the frequency input, [randpulse~] generates a signal with the same number of channels and the 'ch' message or flag is meaningless. The multichannel input is the density for each output., f 44;

You can initialize the object with multichannel if you give it a list of frequencies with the -mc flag (you can't set phases though). A list input also works if no signal is connected to set it to multichannel with a list of frequency input., f 49;

If the secondary inlets have a signal with a single channel for width ans sync, the single value is applied to all channels. If a secondary inlet is also a multichhanel signal, then each channel gets its width or sync value. Note, however, that the number of multichannels in secondary inlets need to match the same number of channels from the left input., f 76;


## `range`


## `range.hsl`


## `range~`


## `ratio2cents`

1) float - initial rational value, needs to be >= 0 (default 1), f 64;

Use [ratio2cents] to convert intervals described as rational numbers (expressed as float point decimal values) to intervals in cents. The conversion formula is: cents = log2(rational) * 1200, f 72;


## `ratio2cents~`

Use [ratio2cents~] to convert a signal representing a rational interval to an interval in cents. It has support for multichannel connections. The conversion formula is; cents = log2(ratio) * 1200;


## `rec`


## `rec.file~`

clicking on the object opens dialog box to set a file to save to, f 65;

rate <float> - sets sample rate of the file (default Pd's samplerate), f 69;

By default, [rec.file~] performs a fade in and fade out of 10 ms. This means that when you stop recording, it takes an extra 10 ms to finish recording the file. The outlet only outputs a bang after this fade out. You can change and set the fade to 0 ms (no fading) with the -fade flag or fade message., f 60;

You can also set a maximum recording time. In this case, the object automatically stops recording at that given time. Note, however, that the fade out will happen first. Say, for instance, you have a 1000 ms maximum recording time and a fade time of 50 ms, at 950 ms the fade out starts and the recording finishes at 1000 ms indeed.;

By default, [rec.file~] performs a fade in and fade out of 10 ms. This means that when you stop recording, it takes an extra 10 ms to finish recording the file. The outlet only outputs a bang after this fade out. You can change and set the fade to 0 ms (no fading) with the -fade flag or fade message., f 60;

A maximum time of 0 or less means no maximum time, and the recording goes on indefinitely. The maxtime needs to be at least twice the fade time, otherwise it is ignored and the recording goes on indefinitely as well.;

[rec.file~] is a convenient abstraction based on [writesf~], so it records sample files that you can load with other objects, such as [sample~], [play.file~], [player~] and others.;


## `rec2`

[record] records to a [text] object that is suitable for [text sequence]., f 73;


## `receiver`

[receiver] can have up to two receive names. Hence, it receives data sent for two different addresses. This is useful if you want to send a message to a group of objects and also individually., f 65;

[receiver] is kinda like vanilla's [receive]. It can have up to two names, has an inlet to set the receive names and at load time can expand dollar symbols according to parent patches., f 63;

I'm lazy to create an abstraction and prove this to you, but trust me, you can have a depth argument like in [dollsym] to expand dollar signs according to a parent patch. Check the help file of [dollsym] if you're too confused., f 65;

This allows you to get from within an abstraction values sent from loading patch.;

This is possible at load time and also when getting new dollar sign names to expand. This would be the same as using [dollsym]. Note that in this cases you need to escape dollar signs with a backslash., f 65;


## `remove`

[remove] removes one or more number elements from a list. The right inlet or arguments set the elements to remove., f 58;


## `repeat~`

[repeat~] takes an input signal os any channel size and repeats it 'n' times., f 56;

Here we use [reepat~] to copy an impulse so it triggers more than one channel in the generation of random integer numbers., f 42;


## `replace`


## `requirer`

TODO: some kind of "my location" necessary for .pd_lua scripts to access?;

If it fails a list of paths searched will appear in the Pd console.;


## `rescale`

You can set the minimum and maximum output via the rightmost inlets, but you can set minimum and maximum input with the 'in' message or flag. The third argument is for the exponential factor explained later., f 74;

The scaling can be inverted by reversing the min/max output values, f 21;

By default, [rescale] will clip the values to the given in and out range. You can use clip message to get in or out of the clip mode. The p the output into the output range. The -noclip flag initializes to non clip mode, where the object keeps scaling outside the given boundaries with the same conversion parameters., f 71;

The 3rd argument sets the exponential factor. You can also set this with the 'exp' message or flag. A value of '0' makes it linear (the default), but values of "1" or "-1" also make it linear.;

The log mode makes it behave like the 'log' mode in iemguis. This is useful for frequencies like, below, we have a range from 220 to 880 and the mid value is 440!, f 38;

For positive values, it's like raising to the power of the given exponential, try the example to the left with values from 0.1 to 10 The input from 0 to 127 is then mapped to 0-1 generating the exponential curves below., f 58;

Negative exponentials are allowed. In this case, it's like the curve shape has been mirrored in reverse., f 36;

The log mode supersedes the exp mode, so the exponential setting gets ignored and is only valid if the log mode is removed., f 32;

When in log mode, you cannot have or cross zero in the output range., f 32;

-in <float, float>: sets min/max input value (default 0, 127), f 61;

By default, [rescale] rescales input values from 0 to 127 (the MIDI range) into another range of values (0-1 by default). You can also set an exponential factor (1 by default - linear) or use a log mode as in iemguis. All these parameters can be changed by arguments., f 78;

The 'rlog' mode is "reverse log" and converts from log to linear., f 37;


## `rescale~`

-in <float, float>: sets min/max input value (default -1, 1), f 61;

You can set the minimum and maximum output via the rightmost inlets, but you can set minimum and maximum input with the 'in' message or flag. The third argument is for the exponential factor explained later., f 74;

The scaling can be inverted by reversing the min/max output values, f 21;

By default, [rescale~] will clip the values to the given in and out range. You can use clip message to get in or out of the clip mode. The p the output into the output range. The -noclip flag initializes to non clip mode, where the object keeps scaling outside the given boundaries with the same conversion parameters., f 71;

The 3rd argument sets the exponential factor. You can also set this with the 'exp' message or flag. A value of '0' makes it linear (the default), but values of "1" or "-1" also make it linear., f 77;

The log mode makes it behave like the 'log' mode in iemguis. This is useful for frequencies like, below, we have a range from 220 to 880 and the mid value is 440!, f 38;

For positive values, it's like raising to the power of the given exponential, try the example to the left with values from 0.1 to 10 The input from 0 to 127 is then mapped to 0-1 generating the exponential curves below., f 77;

Negative exponentials are allowed. In this case, it's like the curve shape has been mirrored in reverse., f 36;

The log mode supersedes the exp mode, so the exponential setting gets ignored and is only valid if the log mode is removed., f 32;

When in log mode, you cannot have or cross zero in the output range., f 32;

By default, [rescale~] rescales input values from -1 to 1 into another range of values (0-1 by default). You can also set an exponential factor (1 by default - linear) or use a log mode as in iemguis. All these parameters can be changed by arguments/flags or messages. There is support for multichannel signals., f 70;

If [rescale~] has a multichannel left input, it outputs the same number of channels. If the secondary inlets have a single channel for the min/max output values, the single value is applied to all channels. If a secondary inlet is also a multichhanel signal, then each channel gets its own min/max value. Note, however, that the number of multichannels in secondary inlets need to match the same number of channels from the left input., f 80;

The 'rlog' mode is "reverse log" and converts from log to linear., f 37;


## `resonant2~`

[resonant2~] is a resonator just like [resonant~], but you you can specify an attack time besides a decay time.;

The filter acts as a 'resonator', where it resonates at the resonant frequency for a period of time after the input signal has ceased., f 42;

The resonance parameter is specified by the decay time, like the [resonant~] object., f 44;

If the attack time is the same as the decay time, then the signal gets canceled out. If the attack time is greater than the decay time, then the polarity of the impulse response is inverted.;

The [resonant2~] object could be implemented from two [resonant~] objects, where the signal from the [resonant~] object that has the decay parameter is subtracted by the signal from another that has the attack paranmeter. The difference is that [resonant2~] has a gain adjustment so the maximum value is equal to the impulse., f 66;


## `resonant~`

a0, a2, b1 and b2 are calculated as a function of center frequency 'f' in hz and 'q' as follows;;

The equation is from the "Cookbook formulae for audio EQ biquad filter coefficients" by Robert Bristow-Johnsonc [1], and it is:;

This filter has zeroes fixes at +1 and -1 on the z-plane, which means both 0Hz and Nyquist are always filtered out.;

Change the parameters and check the filter response below. The graph considers a sample rate of 44.1Khz.;

omega = f * PI/nyquist; alphaQ = sin(omega) / (2*q); b0 = alphaQ + 1; a0 = alphaQ * q / b0; a2 = -a0; b1 = 2*cos(omega) / b0; b2 = (alphaQ - 1) / b0;;

[1] found in https://webaudio.github.io/Audio-EQ-Cookbook/audio-eq-cookbook.html, f 80;

By default, the resonance parameter is 'q', but you can also set to 't60' or 'bw'. In 'bw' the resonance is bandwidth in octaves. In 't60', it's the time in ms for an excitation signal (such as an impulse) to decay 60dB. Use the -t60/-bw flags to change from the default or the messages.;

If you compare the filter response of both [bandpass~] and [resonant~], you may notice how similar they are. In fact, the only difference is that [bandpass~] will have an automatic gain adjustment so the maximum gain value is constantly at 0 dB!;

Therefore, we can describe [bandpass~] as being a "constant gain filter", whereas [resonant~] is a constant skirt filter.;

The Q parameter affecting the gain of the filter makes it so that it acts as a 'resonator', where it will resonate at the resonant frequency for a period of time after the input signal has ceased.;

Thus, instead of a 'q' factor, the resonant parameter can be specified by a decay time. The decay time is given in "T60", which is the time it takes to decay 60 dB. You can convert from decay time to Q and vice versa with a formula implemented in the subpatch below.;

2) float - resonance (default 0), either in 't60' or 'Q' (default), f 66;

[resonant~] is a bandpass resonator filter like [bandpass~], but it doesn't have a maximum dB value of 0, so changing the Q increases the gain of the filter. Besides 'Q' and 'bw' you can also set the resonance as 't60' (like with [resonator~])., f 75;


## `resonator2~`

As mentioned, the filter produces a very high output for other singal inputs., f 35;

This example shows the difference between both outputs. By feeding an impulse you get an oscillation on the left outlet starts at cosine initial phase, while right one starts at sine. Note that this can be used as a very simplified "Spring Model"., f 44;

[resonator2~] is a wrap around [cpole~]. It is very similar to [vcf~], which is also a wrap around [cpole~], but has no constant maximum gain at 0dB - so it works like [resonator~] with a constant skirt. Like [resonator~], it takes a decay time for resonance. Unlike [resonant~], you shouldn't excite it with noise as the filter produces very high gain output, so it's really suited just to be excited by impulses. By the way, this filter is the basis of [damp.osc~] and [resonbank2~]., f 83;


## `resonator~`

The 't60' resonance specifies the time in ms it takes for the resonant signal to decay 60dB after it's been excited. Hence, it resonates at the resonant frequency for a period of time after the input/excitation signal has ceased.;

You can convert from decay time to Q and vice versa with a formula implemented in the subpatch below., f 40;

[resonator~] is just like [resonant~], but the resonance parameter is defined as resonance time in 't60'. Note that a t60 value of 0 bypasses the input! For a bank of [resonator~] objects, see [resonbank~]. For another similar filter, see [resonator2~]., f 78;


## `resonbank2~`

-decay <list>: sets list of decay time for the resonators, f 69;

The "-mc" flag or message sets to multichannel output, where each resonator in the bank is in a different channel., f 30;

-partial <list>: sets list of partials for the resonators's frequencies, f 71;

Here we have an input from [keyboard]. We use the partial as a ratio list and the leftmost input as the fundamental frequency. The velocy controls the impulse value, but besides the amplitude, we use the velocity to control how much it resonates with the decay multiplier, so not only you have a louder sound when the velocity is high, but you also make the sound sustain for longer., f 65;

There are two ways to deal with the frequency multiplier, the main one is to make it the fundamental as in here:, f 45;

Another way to deal with the partial list is to make it a frequency list in hertz and then treat the left input as a ratio mulitiplier. By default, this multiplier is '1', by the way. The decay time multiplier, by default, is also 1 and can be used in the same both ways (so the decay list can be either a ratio list or a list of dureations)., f 57;

The lists can be updated via the leftmost inlet and there is a ramp time in ms to transition between the changes of partial, decay and amplitude lists. By default, this ramp is set to 10 ms., f 57;

[resonbank2~] is a bank of resonators made of [resonator2~] objects. The design and structure here is different than [resonator2~] in order to make it better suited for sound synthesis. It has the same design as [resonbank~] and has a list of partials for each resonator and a frequency multiplier in the left inlet, kinda like [oscbank~]. The mid inlet the trigger (or excitation) signal (kinda like [pluck~]) - this must be an impulse since noise sources and noise bursts generate very loud outputs! The rightmost inlet is a time multiplier for the decay times. The number of filters is set via the parameter list size (such as the partial list). There's also support for multichannel output., f 80;


## `resonbank~`

-decay <list>: sets list of decay time for the resonators, f 69;

The "-mc" flag or message sets to multichannel output, where each resonator in the bank is in a different channel., f 30;

-partial <list>: sets list of partials for the resonators's frequencies, f 71;

Here we have an input from [keyboard]. We use the partial as a ratio list and the leftmost input as the fundamental frequency. The velocy controls a decay envelope, but besides the amplitude, we use the velocity to control how much it resonates with the decay multiplier, so not only you have a louder sound when the velocity is high, but you also make the sound sustain for longer., f 65;

[resonbank~] is a bank of resonators made of [resonator~] objects. The design and structure here is different than [resonator~] in order to make it better suited for sound synthesis. It has a list of partials for each resonator and a frequency multiplier in the left inlet, kinda like [oscbank~]. The mid inlet the trigger (or excitation) signal (kinda like [pluck~]) and the rightmost inlet is a time multiplier for the decay times. The number of filters is set via the parameter list size (such as the partial list). There's also support for multichannel output., f 81;

There are two ways to deal with the frequency multiplier, the main one is to make it the fundamental as in here:, f 45;

Another way to deal with the partial list is to make it a frequency list in hertz and then treat the left input as a ratio mulitiplier. By default, this multiplier is '1', by the way. The decay time multiplier, by default, is also 1 and can be used in the same both ways (so the decay list can be either a ratio list or a list of dureations)., f 57;

The lists can be updated via the leftmost inlet and there is a ramp time in ms to transition between the changes of partial, decay and amplitude lists. By default, this ramp is set to 10 ms., f 57;


## `retrieve`


## `retune`

[retune] receives a scale as a list of steps in cents and a base MIDI pitch value (default 60). It then remaps the incoming MIDI ptches (as integers) and retunes the pitches above or below the base value according to the scale., f 65;


## `revalue`

Interface to Pd's native [value]. Behaves like [value] but with a settable name, and another outlet to report if there is no [value] with the current name.;


## `revdelay~`

[revdelay~] is a reverse delay effect. It takes a size amount in ms to play backwards from a delay line (default 1000 ms)., f 61;


## `reverb-calculator`


## `reverse`


## `rint`

[rint] takes floats and rounds them to the nearest integer value., f 67;


## `rint~`

[rint~] takes a float input and rounds it to the nearest integer value.;


## `rm.m~`

This is just a wrapper around [rm~] from ELSE, check it out., f 22;

this is still a simple module, with no CV input yet, so kinda like a pedal still., f 22;


## `rms~`

[rms~] is similar to Pd Vanilla's [env~], but it reports the RMS value in linear amplitude (default) or in dBFS., f 62;

The [rms~] object is based on [env~] and has the same analytical structure. The analysis is "Hanning" (raised cosine) windowed, which makes the RMS output more stable.;

The optional creation arguments are the analysis window size in samples, and the 'hop' period (the number of samples between analyses). The hop size only affects the result output frequency. With a smaller hop period, you get more frequent updates.;

It's common that both of these parameters are multiples of the DSP block size, and that the hop size is a fraction of the window size, although none of this is enforced.;

Nonetheless, the shortest output period (hop size) won't effectively be less than the block size, and, obviously, the output can only happen at block boundaries, not in between. Another constrain is that there is a minimum hop period that depends on the window size. It'll always be at least one block bigger than 1/32 of the window size. This is all also true for [env~], by the way.;

The set message changes the analysis parameters and takes up to 2 arguments, which are, like in the object creation, the window and hop size. The default values are also the same as creating the object, so if you give it only one value for the window size, half of it will be the hop size. Note that it won't let you set the window or hop size to anything smaller than the current block size.;


## `rm~`

[rm~] is a Ring Modulation abstraction. It takes a modulation frequency input as the argument or via the control right inlet. A modulation frequency of 0 Hz bypasses the input signal., f 63;


## `rotate`


## `rotate.mc~`

[rotate.mc~] performs equal power rotation for any number of channels given by a multichannel signal input. It takes a position control in which a full cycle is from 0 to 1, negative values from 0 to -1 are wrapped., f 69;


## `rotate~`

[rotate~] performs equal power rotation for 'n' channels (default 2). It takes a position control in which a full cycle is from 0 to 1, negative values from 0 to -1 are wrapped., f 69;


## `route2`


## `routeall`


## `router`

[router] routes a message from the left inlet to an outlet number specified by the float into the right inlet (if the number is out of range, the message is not output)., f 65;


## `routetype`


## `sample~`

Just the 'open' message opens a dialog for you to choose a sound file. Then the buffer is resized and reinitialized according to the sample size and its number of channels. If you give the open message a file name, same thing happens, but note that after the sample name you can also define optional arguments. The 1st optional argument sets the start read position in samples in the file, the 2nd the buffer duration in ms and the 3rd the number of channels in the buffer. This way you can reconfigure the buffer size and its number of channels., f 65;

The 'load' needs a file name and it loads this file into the sample buffer according to the previously set buffer size and number of channels. Just 'load' opens a dialog., f 65;

The "save" message saves the contents of [sample~] into an audio file and needs a symbol with the file name to save to (in which case the file is saved in the current patch's folder). If no file name is given, a file dialog is opened for naming it and you can save it anywhere in your computer., f 65;

You can set an array name as the first argument. The second argument sets a sound file to open. The size and number of channels from given sound file prevails, unless the -size, -ms and -ch flags are given, in which case the sound file loads into these parameters., f 65;

The [sample~] object supports 'wav', 'aif/aiff' and 'caf' sound files for opening and saving and in both cases the file extension needs to be set. If you don't specify a format for saving, [sample~] will save in same format of the most recently opened audio file and by default it saves in .wav format., f 65;

The "depth" message sets the bit depth for writing files, it accepts 16, 24, 32 and 64 (use double precision Pd for this one). The "sr" message also sets a sample rate for saving a file., f 65;

* Note that if you specify a buffer size that is smaller than the file you're loading, the file size that is output will be clipped to the buffer size. On the other hand, if you set a buffer that is bigger than a sample you're loading, then the sample size is the original sample size and smaller than the buffer size in ms., f 67;

-ch <float> - sets number of channels (default 1 or samples's), f 62;

load a file into existing buffer size and number of channels (just 'open' opens dialog box to open a file), f 56;

sample size in samples, sample rate, buffer size in ms, channels and bits, f 36;

You can use pd vanilla's objects (such as [tabreceive~], [tabplay~], [tabread4~] and so on) to access the internal arrays of a buffer. In the case of a multi channel buffer, you have to give it the right table name according to a specific channel.;

For multichannel samples, ELSE has other objects that follow the same naming convention, so they work nicely together, see:, f 58;

The objects above work with mono or multi channel samples. When trying to access the first channel of a buffer, they look for a table name with the same name as the argument (for single channel sample compatibility). If not found, then they look for the first channel of a multi channel [sample~] (the buffer name preeceded by "0-").;

But [sample~] is also able to define multi channel arrays (up to 64). The convention for channel ordering is the sample name preceded by the channel number (from 0) and "-". For instance, a 4 channel [sample~] named "test" has arrays named as: "0-test", "1-test", "2-test" and "3-test"!, f 54;

On the other hand, for single or "mono" buffers, a buffer named "test" has an internal array also named: "test"., f 54;

The [tabplayer~] is specially nicely integrated with [sample~] because it is automatically aware of the sample rate of the loaded file and adjusts accordingly., f 58;

Hence, all of them can also access single channel arrays specified with a [table] or [array] object!, f 58;

[sample~] is an abstraction that creates an audio buffer which you can use to load a sample or record into. It can load and save multichannel files. It is based on [sfload] and [soundfiler]., f 70;

takes a filename to open - just 'open' opens dialog box to open a file, f 56;


## `samps2ms`


## `samps2ms~`

[samps2ms~] is a simple abstraction that converts time values number of samples to ms. It has support for multichannel signals., f 53;


## `saw2~`

-midi: sets frequency input in MIDI pitch (default hertz), f 58;

-mc <list>: sets multichannel output with a list of frequencies, f 63;

Syncing the phase with control messages is useful for LFOs and control with MIDI. A sync with audio is useful for the "hard sync" technique, where an oscillator is synced according to the frequency of a master frequency., f 56;

The "phase sync" inlet is quite different from the "phase offset" inlet. They are completely independent!, f 43;

Soft sync is also possible with the '-soft' flag or the "soft" message, where it alternates between positive and negative frequencies and sounds less harsh.;

The second inlet resets the phase ands behaves in the same way for control data as objects like [osc~] and [phasor~] in Pd. A number input resets the oscillator and restarts the cycle with an initial phase that corresponds to the input number, so the internal phase is synced to the given value. The phase values are from 0 to 1 and values beyond that are wrapped within this range. The control message reset is meaningful for LFOs.;

Additionally, you can reset the oscillator with an impulse signal. Inputs that are > 0 and <= 1 reset the phase Pd expects an impulse signal for syncing. The impulse values need to be > 0 and <= 1 (otherwise ignored). Because phase is cyclical, the value of 1 represents the "phase 0" of the cycle, where the impulse occurs. Send it impulses above and check the result. Use a multiplier to reset to another phase value.;

The second argument sets an initial phase (or "phase offset"). This is also settable with the third inlet. This allows you to control two oscillators with the same frequency falling in and out of phase. Another feature is phase modulation., f 53;

The phase values are wrapped into the 0-1 range, since the phase cycle is from 0 to 1 (where 1 is also the start of another cycle)., f 45;

By default, frequency input is in hertz, but if you use the 'midi' message or '-midi' flag you can change it to MIDI pitch input, where it is bound to the 0 to 127 range (but they don't have to be integers) - this is kinda like using [mtof~]...;

If the oscillator has a multichannel left input, it outputs the same number of channels. If the secondary inlets have a signal with a single channel for sync and phase modulation, the single value is applied to all channels. If a secondary inlet is also a multichhanel signal, then each channel gets its sync or phase deviation value. Note, however, that the number of multichannels in secondary inlets need to match the same number of channels from the left input., f 76;

You can initialize the object with multichannel if you give it a list of frequencies with the -mc flag (you can't set phases though). A list input also works if no signal is connected to set it to multichannel with a list of frequency input., f 49;

[saw2~] is a sawtooth wave oscillator that accepts negative frequencies, has inlets for phase sync and phase modulation. It also has support for multichannels., f 72;

A variable sawtooth waveform oscillator that also becomes a triangular osccilator., f 43;


## `saw~`

-midi: sets frequency input in MIDI pitch (default hertz), f 58;

-mc <list>: sets multichannel output with a list of frequencies, f 63;

Syncing the phase with control messages is useful for LFOs and control with MIDI. A sync with audio is useful for the "hard sync" technique, where an oscillator is synced according to the frequency of a master frequency., f 56;

The "phase sync" inlet is quite different from the "phase offset" inlet. They are completely independent!, f 43;

Soft sync is also possible with the '-soft' flag or the "soft" message, where it alternates between positive and negative frequencies and sounds less harsh.;

The second inlet resets the phase ands behaves in the same way for control data as objects like [osc~] and [phasor~] in Pd. A number input resets the oscillator and restarts the cycle with an initial phase that corresponds to the input number, so the internal phase is synced to the given value. The phase values are from 0 to 1 and values beyond that are wrapped within this range. The control message reset is meaningful for LFOs.;

Additionally, you can reset the oscillator with an impulse signal. Inputs that are > 0 and <= 1 reset the phase Pd expects an impulse signal for syncing. The impulse values need to be > 0 and <= 1 (otherwise ignored). Because phase is cyclical, the value of 1 represents the "phase 0" of the cycle, where the impulse occurs. Send it impulses above and check the result. Use a multiplier to reset to another phase value.;

The second argument sets an initial phase (or "phase offset"). This is also settable with the third inlet. This allows you to control two oscillators with the same frequency falling in and out of phase. Another feature is phase modulation., f 53;

The phase values are wrapped into the 0-1 range, since the phase cycle is from 0 to 1 (where 1 is also the start of another cycle)., f 45;

By default, frequency input is in hertz, but if you use the 'midi' message or '-midi' flag you can change it to MIDI pitch input, where it is bound to the 0 to 127 range (but they don't have to be integers) - this is kinda like using [mtof~]...;

If the oscillator has a multichannel left input, it outputs the same number of channels. If the secondary inlets have a signal with a single channel for sync and phase modulation, the single value is applied to all channels. If a secondary inlet is also a multichhanel signal, then each channel gets its sync or phase deviation value. Note, however, that the number of multichannels in secondary inlets need to match the same number of channels from the left input., f 76;

You can initialize the object with multichannel if you give it a list of frequencies with the -mc flag (you can't set phases though). A list input also works if no signal is connected to set it to multichannel with a list of frequency input., f 49;

A variable sawtooth waveform oscillator that also becomes a triangular osccilator., f 43;

[saw~] is a sawtooth wave oscillator that accepts negative frequencies, has inlets for phase sync and phase modulation. It also has support for multichannels., f 71;


## `scala`


## `scale2cents`

Use [scale2cents] to convert a scale defined as scale steps in semitones to cents.;


## `scale2freq`

-range <float float>: sets min/max frequency range in Hz (default 20 20000), f 75;

By default, the generated scale uses a base (fundamental) pitch of 60 (middle C). The scale is generated upwards and downwards from this pitch until reaching minimum and maximum bounds (20 to 20000 hz by default)., f 72;

You can change the base and range with messages or flags. Microtonal base pitch is also possible. You can also use [ftom] to set a base value according to a hertz input (or also [mtof] for range input). After setting new base/range values you have to send a bang to generate a new list., f 51;

[scale2freq] gets a scale as a list of cents values, a base/fundamental pitch and outputs a list of frequency in hertz between a minimum and maximum value. Below we use [eqdiv] to generate a scale. Use it to feed values to things like [resonbank~], [oscbank2~] or [pvretune~]., f 71;


## `scales`

Scales are set as a list of semitones that define each step of the scale., f 37;

You can set the output mode to 'pitch' and have the output as pitch in MIDI instead. This is done with the '-pitch' flag or the 'pitch' message., f 45;

[scales] generates scales as note names (default) or MIDI pitches. The scale is set as a list of semitones that define each step of the scale (major by default). The note symbol can also contain the octave number, otherwise you have to set the octave via the 2nd inlet ot argument. If you bang the object without setting anything, the default is 'C 1'., f 66;


## `schmitt`


## `schmitt~`


## `scope3d~`

"nlines" sets the number of lines in the display. The number of samples represented by each line is set by "nsamples". Therefore, the total number of samples (or period) displayed in the scope is equal to: nsamples * nlines. You can also set both parameters with a list input., f 63;

[scope3d~] displays signals in 3D. This is an object coded in Lua and is very very experimental and likely to change and break., f 26;

The object below has a receive symbol, so you can send messages to it via a [send] object (but not audio). The receive symbol can be set with the receive message or the -receive flag. Dollar signs must be escaped. If you set a receive name as "empty" then it can't receive messages anymore., f 69;

You can use mouse to rotate the display in 2 dimensions, just click and drag. You can use the "drag 0" message to disable mouse dragging. You can also use 'rotate', 'rotatex' and 'rotatey' messages for rotatation., f 57;

To the left we have basic appaerance messages to set dimension sizes, line width, zoom and grid., f 57;

To perspective setting enhances the 3D effect and changes the 'depth feel'. Increasing it appear more dramatically different in size based on their distance.;

RGB colors (values from 0-255) for fgcolor (front/signal), bgcolor (background) & grid (gridcolor)., f 35;


## `scope~`

When in X-Y mode, [scope~] plots points whose horizontal axis (X) corresponds to the signal's values coming into the left inlet and whose vertical axis (Y) corresponds to the signal's values coming into the right inlet. If the two signals are identical and in phase, a straight line increasing from left to right will be seen. If the two signals are identical and 180 degrees out of phase, a straight line decreasing from left to right will be seen. Other combinations may produce circles, ellipses, and Lissajous figures.;

When in X-Y mode, there's an averaging algorithm for the calccount parameter, where a representative sample from this period is used. So it requires small values for a better representation (only 2 in the examples below).;

If signals are connected to both the left and right inlets, [scope~] operates in X-Y mode.;

Change the phase of the oscillator to check how it affects the plot, then try different frequencies.;

RGB colors (values from 0-255) for fgcolor (front/signal), bgcolor (background) & grid (gridcolor)., f 35;

You can set the vertical (signal amplitude) range and the onset delay (time between displays) with messages.;

There's also a "dim" message/flag for setting the size of your [scope~]., f 41;

And as noted, if you right click on it (in edit mode or not) you can access its properties., f 50;

When you click on [scope~] with your mouse, the display freezes for as long as you hold the mouse button down.;

When in edit mode, you can resize the object by clicking and dragging on its bottom right corner., f 51;

If a signal is only fed to the second inlet, [scope~] displays in "Y Mode" only., f 31;

You can send any kind of message that [scope~] accepts. Note that if you send it a list of two floats. Then the values are spread via both inlets and set samples per line and lines per buffer, respectively., f 38;

When in edit mode, [scope~] shows its inlets. The [scope~] object below has a receive symbol, so you can send messages to it via a [send] object (but not audio). In this case, the inlets are suppressed, so we don't see it. The receive symbol can be set with the receive message or the -receive flag. Dollar signs must be escaped. If you set a receive name as "empty" then it can't receive messages anymore and the inlets are shown., f 75;

Therefore, the total number of samples (or period) displayed in the scope is equal to: nsamples * nlines. This total number of samples also affects the time between displays. If the number of samples is small, the refresh rate speed is high, so you may want to use the "delay" message to increase the speed between displays., f 49;

You can also set both parameters with a list input. Lets check the example to the left with two settings. Both have the same display period in samples (2560), but one is displayed as a buffer made of 10 lines and 256 samples per line and the other as a buffer made of 256 lines and 10 samples per line., f 49;

"nlines" sets the number of lines in the display (possible values from 8 to 256 - default is 8). The number of samples represented by each line is set by "nsamples" (possible values from 2 to 8192 - default is 256). For each line, the maximum and minimum values within the period in samples are used to generate the line. So the smallest line is 2 samples/points long., f 49;

The default mode is "trigger 0", which is "none mode", where the signal is displayed the way it is., f 57;

"trigger 1" is "up mode", in which - following the delay period - a new display is triggered only when the signal goes from below the trigger level to being equal to it or above it.;

"trigger 2" sets to down mode, in which - following the delay period - a new display is shown only when the signal goes from above the trigger level to being equal to it or below it., f 57;

The "triglevel <float>" message sets the threshold for the trigger modes "1" (up) and "2" (down). In these cases, as described above, the waveform must increase or decrease past this value to trigger a new display. If you are displaying a periodic waveform, some changes to the trigger level will shift the waveform to the left or right., f 57;

The delay onset period determines when to display a new waveform. The trigger mode determines when a new waveform trace begins (following the delay period).;

- sets number of samples per line (2-8192, default 256), f 58;

-fgcolor <f f f> | -bgcolor <f f f> | -gridcolor <f f f> | -range <f f> | -trigger <f> | -triglevel <f> | -nsamples <f> | -nlines <f> | -delay <f> | -dim <f f> | -receive <sym>, f 62;

[scope~] displays signals in the style of an oscilloscope. It works up to two dimensions., f 40;


## `score`

clicking on the object opens data/edit window (same as 'open'), f 63;

import score from a file, no symbol opens dialog window, f 58;

[score] is an abstraction based on [text] with its own syntax. A variation of the object ([score2]) has the same rhythmic notation syntax as [pattern]., f 76;

The "|" symbol is the syntax for bars - like in [else/sequence] and [else/pattern]. This sets a bar number which is output at the 'data' outlet along with 'tempo' messages and whatever else that you specify in the score that is not a list starting with a number (which are treated as timestamps)., f 68;

[score] has a 'tempo' syntax where 'tempo 60' internally sets the bpm to 60! The 'tempo' messages are output in the mid 'data' outlet., f 68;

Here we also use a [metronome] object so we can have a 'click track' and we get the 'timesig' and 'tempo' messages directly from the score via the 'data' outlet., f 68;

The 'timesig' message is necessary to specify the time signature and allow [score] to count the number of beats in a bar. It must be specified in the beginning of the score right after the bar symbol. Time signature changes are possible and need to be specified after any bar symbol. The 'timesig' message has the same format as in the [metronome] object and as other messages come out in the mid outlet., f 68;

Note events are specified as lists that start with a number that represent the tempo head within the bar. So "1" means the head of the first beat, 1.5 is an eight note after the first beat and so on. Whatever follows the first number comes out in the 'event' left outlet and you can treat it in any way you want to. If nothing follows the number, a bang comes out as in this example., f 68;

In this example, the event data is a symbol that represents a note pitch and its duration in beats (as floats and fractional symbols). A bang is sent at the rightmost outlet when the sequence is over., f 102;

Note that since each note event can have a different duration, you can have polyphonic events, because one note can keep playing while others come in and out., f 102;

You can also set tempo changes. For example 'tempo 90 3' goes from whatever bpm setting you currently have to '90' in three beats (accelerating or deaccelerating). When changing the tempo speed, tempo values for each beat are also output via the data outlet. This example also connects to a [metronome] to show us how it can also change its speed with the tempo output information., f 102;

For the duration, we get the value in ms of the current tempo. We're actually playing 90% of the note duration because of [* 0.9]., f 30;

In this patch we're combining the floats with [combine] and split the list with [unpack]. This is because we don't really need [makenote], [poly] or [else/voices] as the duration is set in the [decay~] object inside [pd voice]., f 41;

The last example showed us how we can have polyphony since each event can have its own specified duration. But you can also specify polyphonic events that happen at the same time as in 'chords'. One way is to split messages with commas. In this way, you can also have a list for each event, each with a different duration like the last example. But in this example we just have a single float that represents pitch values., f 76;

Another way is to simply specify another event with the same timestamp and it will also be output right after the previous one. One little techicality is that when you're using commas they do come out together as the same event as a loop. One way to prove this is with the [combine] object that can combine these values with a combine time of "0". Otherwise you need to specify a very short time amount, like "0.001" ms here. Test it below., f 76;


## `score2`

clicking on the object opens data/edit window (same as 'open'), f 63;

import score from a file, no symbol opens dialog window, f 58;

[score2] is a variant of [score] that has the same rhythmic notation syntax as [pattern]., f 75;

This is the same score and example as before, but we're now sending information to a [metronome] object, which understands the 'timesig' message and can also get tempo information to give us a "click track"., f 45;

Chord polyphony is possible if you split messages with commas. Open the score to see how it works. In this patch we're combining the floats with [combine] and split the list with [unpack]. This is because we don't really need [makenote], [poly] or [else/voices] as the duration is given in the score., f 75;

A bang is sent at the rightmost outlet when the sequence is over., f 39;

In this example, the event data is just a float, which is treated as pitch in MIDI., f 39;

Use "|" as a syntax for bars - the same as [else/sequence] and [else/pattern]. This sets a bar number which is output at the third outlet along with 'tempo' messages and whatever else that you specify in the score that is not an 'event' (such as 'timesig 3/4' in this example)., f 39;

Note events are specified with lists that start with a float or a fraction (which represent fractions of a whole note). Negative values are rests so nothing should follow it. Whatever follows the fraction is the 'event data' and is sent out at the left outlet., f 39;

The duration in ms is output in the second outlet. Negative values are also output so they can be filtered out and specify rests., f 39;

Any crazy thing goes, you can have '1.23/(7.78/2.33)' or whatever. It'll work even if you don't have a clue on what the result is., f 66;

You can also see and read more about note durations in the help files of [metronome] and [pattern]., f 66;

You can also have a fraction with the nominator in parenthesis so (5/8)/7 is allowed, as well as (3/8)/5., f 66;

The example above is a '2:3' tuplet for quarter notes, which is the same as a dotted quarter note. To get the value, we multiply the 2:3 ratio by 4 (because we want a quarter note tuplet) and get "8/3"! So 1/(8/3) is what you want., f 66;

When the first element of a list is either a float or a fraction it represents the duration of a note. The values are in relation to a whole note, so "1" (or "1/1") is a whole note and "1/4" (or "0.25") is a quarter note, '1/8' is an eight note and so on..., f 66;

Besides multiples of '2' as the denumberator, which is common in music notation, you can also use other values. For instance '2/3' means two beats of '1/3' of a whole note. This would then be the same as a triplet of a half note. On the other hand '3/5' is three beats of a quarter note quintuplet. Again, if you wish you can use the actual float values., f 66;

You can also have a fraction in the denominator in parenthesis, such as '1/(8/3)', which is also equal to '0.375'. Sometimes the usage of fraction is better to avoid periodic sequences and approximations., f 66;

Note that 1/15 is a nested tuplet (a quintuplet inside a triplet), which is also possible. For other arbitrary tuplets, you need to work on your math. If you want to have 7 eight notes in the space of 5, then you have 5 eight notes (5/8) divided by 7, which is the same as 5/(8*7), so you have 5/56 for each of these notes. 5 in the space of 3 is (3/8)/5, which is the same as 3/(8*5) = 3/40., f 66;

Non integers are possible on their own or as part of a fraction. So '0.375' is one beat and a half (the same as a dotted quarter note) and one way to define this as a fraction is '3/8' (which represents three 8th notes) - but you can also specify this as '1/2.66667', which is also equal to 0.375 in the end., f 66;

Let's get a bit crazier now and use an 8:9 tuplet for 8th notes (where we have eight 8th notes in the space of nine 8th notes). So we multiply "8:9" by 8 (cause we want 8th note tuplets) and get 1/(64/9). If you want quarter note tuplets it's 8:9 x 4, which is 2/(64/9) or 1/(32/9)., f 66;

For more details on how fractions determine the note duration, see the subpatch below:, f 33;

[score2] has a 'tempo' syntax where 'tempo 60' sets the bpm to 60! The 'tempo' messages are output in the third 'data' outlet. You can also set 'tempo 90 3' as in this example and it will accelerate or deaccelerate, going from whatever bpm setting you have to '90' in three beats. When changing the tempo speed, tempo values for each beat are also output., f 39;


## `scramble`


## `selector`

[selector] outputs data from the selected inlet according to the float into the rightmost inlet.;


## `select~`

[select~] selects an input signal without crossfade and the signals can be of different channel sizes. The number of inputs is set via the 1st argument. The 2nd argument sets the initial input (indexed from 1). The selection is clipped to the number of inputs., f 71;


## `send2~`

[send2~] is like send but automatically resizes according to the number of input channels., f 48;


## `sender`

[sender] can have up to two send names. Hence, it sends data to two different addresses. To get a second send symbol you need to give it two send names as arguments. An inlet is then created to set each symbol name. An empty symbol clears the send name and the sent message goes anywhere., f 65;

[sender] is much like vanilla's [send], but can have up to two names and at load time can expand dollar symbols according to parent patches., f 62;

I'm lazy to create an abstraction and prove this to you, but trust me, you can have a depth argument like in [dollsym] to expand dollar signs according to a parent patch. Check the help file of [dollsym] if you're too confused., f 65;

This allows you to send from within an abstraction values to the loading patch., f 50;

This is possible at load time and when giving a new name with a dollar sign to expand. This would be the same as using [dollsym]. Note that in this cases you need to escape dollar signs with a backslash., f 65;


## `sendmidi`

[sendmidi] is a helper abstraction to send MIDI messages to the [pd~] object, which cannot listen to the connected MIDI devices in Pd.;


## `separate`


## `seq8.m~`


## `sequencer`

Use [count] if you want to also have the sequence being read in different directions., f 29;

A sequence of frequencies with pauses and the last note tied., f 16;

You can use pitch names and convert to MIDI pitch with [note2midi]., f 28;

<== you can use [combine] to join elements sent at the same time. This may also add a symbol/list selector., f 42;

convert to MIDI pitch if you have a sequence with note names., f 33;

set element number in sequence (indexed from 1) note that barlines don't count!, f 39;

[sequencer] sends an element from a given sequence when banged. Elements joined by "-" are sent at the same time but separately (allowing chords). A single "-" is treated as a rest. A "_" is ignored and can be thought as "tie". A "|" represents a barline. Symbol elements are sent without a symbol selector (and can be note names or anything else). A "bang" comes out as a proper "bang"., f 82;

see also [score2], which is able to combine both objects into one., f 24;

You can use [pattern] to query for a sequence in the [sequencer] object., f 37;


## `sequencer~`


## `setdsp~`

[setdsp~] is a convenient abstraction to display and set Pd's audio engine (aka 'DSP') state. You can just click on it to change it to On/Off via its toggle interface. This object is commonly found in the documentation of the ELSE library audio objects, at the top right corner., f 74;

By default, the [setdsp~] object will check the current DSP state and load accordingly (on or off). But you can give it an argument to set it on/off., f 74;

float - sets dsp status: non-0 turns it on and 0 turns it off, f 63;

a non-0 value forces the status to be on, while a 0 value forces it to be off. If no argument is given, the default behaviour is to check the current DSP state and load the GUI interface accordingly (on or off), f 61;


## `sfinfo`

- Base Note // MIDI note number 0-127; - Detune // Detune in cents (-50 to +50); - lowNote // MIDI note number 0-127; - highNote // MIDI note number 0-127; - lowVelocity // MIDI velocity 1-127; - highVelocity // MIDI velocity 1-127; - gain // Gain in dB; - sustain loop // 0-2; - loop start point; - loop end start point; - release loop // 0-2; - loop start point; - loop end start point;;

Aif files can contain "Instrument" Metadata, in which the list of 13 output numeric values are:, f 48;

[sfinfo] supports all files that [sfload] and [play.file~] support and can be used to query file sample information but so far only channels and 'inst' info for aif files (this object is still very experimental)., f 71;


## `sfload`

when loading mono or multichannel files with [sfload], it searches for arrays that is preceded by "x-" (where 'x' is the channel number indexed from 0). If found, it has loading priority, if it fails it searches for an array with the exact given name instead., f 72;

You can optionally give a channel number to load from the file (indexed from 0). In the case of multichannel arrays, it will also try to match the channel number from the array. You can force a channel swap if you specifically set the array channel., f 33;

You can use [tabplayer~] to play multichannel arrays. --------------->, f 37;

(downloading from an internet link, this one takes a little while of course...), f 42;

By default [sfload] works in threaded mode, which guarantees order of execution. If you wanna load larg files and would like to not choke Pd's audio you can try loadubg files in threaded mode, but this ruins order of execution (and you can use the output of [sfload] to know when it is done loading)., f 49;

load <symbol, float> - file to load and optional channel number, f 67;

[sfload] is similar to [soundfiler] supports more file formats (officialy AAC, AIF, CAF, FLAC, MP3, OGG, OPUS & WAV). It can also load into multichannel arrays and download files from web links!, f 65;

download <symbol, float> - link to download and optional channel number, f 71;


## `sfont.m~`

by default it loads into all channels but channel 10 and you can't set programs into channel 10 (document this)., f 41;

generaluser_GS has a drum soundfont in channel 10 and I can't overwrite the program in this channel., f 36;

The [sfont.m~] object should be saved with the pgm and ch info. Add bank/pgm/channel number to the preset message, f 43;

Can I make it so that loading a program loads into all channels? OMNI?, f 40;


## `sfont~`

SoundFont is a file format for sample-based instrument sounds. If you are not familiar with it, check:, f 44;

Play notes with either 'note' or list messages, whose arguments are: MIDI Pitch, Velocity and optional channel number (counting from 1). If no channel number is given, then a default channel 1 is used. The minimum and default number of channels is 16 but you can set up to 256 with the '-ch' flag., f 67;

If the verbosity flag is given (-v), [sfont~] prints the version when loading the object (same goes for the 'version' message). The "dump" message outputs the soundfont name, its banks, programs and preset names on the rightmost outlet - this is also printed on Pd's window with the 'info' message. In verbosity mode, the terminal window also prints bank, program and preset name when you load a a file/program or if it fails. Verbosity is also set by the "verbose" message. The preset name is also output as a 'preset' message in the rightmost "info" outlet., f 67;

Some files - like the "waves.sf2" file used here - include different bank numbers with different programs in each. A different program means a different timbre. A program is set with the 'pgm' message. You can optionally set a channel to load the program into (channel 1 by default). You can use the note message with different channels to access different programs., f 70;

Similarly, you can choose a different bank of programs into a channel (if no channel is given, channel 1 is used). The 'bank' message sets the bank number and loads the previously set program number from the new bank. You can set another program number right next with the 'pgm' message or you can also use the control change messages as explained later in the next subpatch (in this case it only sets the bank number and doesn; t set the program until you load it with a 'pgm' message)., f 70;

Using Vanilla's MIDI input objects for specific MIDI messages., f 47;

All messages take a final channel argument. If this last element of the message is not given, then a default channel 1 is used., f 64;

Note that vanilla's [pgmin] object is indexed from 1 so you need to subtract 1 to use it on [sfont~], which is indexed from 0 ([pgm.in] from ELSE is also indexed from 0 by the way). The example below emulates a bend wheel, maybe an extra object for the future...;

A specific sysex message can be set via a 'sysex' message or via raw input. Sysex messages are useful for advanced settings. One example is "mts-tuning" standards used in this example, where you can retune MIDI pitches, but [sfont~] also has microtonal capabilities so this is not needed., f 62;

The control change parameters are programmed in a given synthesizer, but if usually follows some standards like the messages where using here., f 72;

CC0 and CC32 set the bank number (calculated as CC0*128 + CC32). Note that you need to first set CC0 and then CC32., f 24;

We've seen the list message which acts in the same way as a 'note' message, we've also seen the 'pgm' (program change) message and these two are MIDI messages. Other MIDI messages are:;

- 'ctl' for 'control change; - 'bend' for Pitch Bend; - 'touchin' for channel aftertouch; - 'polytouchin' for key aftertouch; - 'sysex' for Sysex messages;

The bank message is not a proper MIDI message on its own but it is usually given by the control message number 0 - control change is also responsible for other usual parameters as we'll see in this example., f 61;

Raw MIDI is also possible via float input, so you can use Pd vanilla's [midiin] object or play a MIDI file from [midi]. Sysex messages is also possible via a 'sysex' message or raw MIDI input from a MIDI file or the [sysexin] object. You can also use vanilla's other MIDI objects like [pgmin] of course or the ones from ELSE, such as [pgm.in], see [pd MIDI-input] below., f 61;

-ch <float>: set number of channels from 16 (default) to 256, f 61;

unselect a tuning from a channel (or from all channels if no float is given), f 55;

scale in cents to retune (12-tone temperament if no list is given), f 51;

loads soundfont file (.sf2/.sf3 extensions implied) if no symbol is given, dialog window opens (same as click), f 55;

The control change parameters are programmed in a given synthesizer, but if usually follows some standards like the messages where using here., f 72;

Generates 8 scales and loads them in different program numbers (0-127) on bank 0 and different channels (1-8). These are equal divisions of the octave from 13 to 20 steps. A scale name is also generated. Set a different input channel to play each scale on the parent patch., f 47;

The remap message allows you to set MIDI Pitches for each key. This patch generates random values for each key., f 31;

There are banks and programs just for tunings. You can load a tuning with the 'scale' message followed by a list of intervals in cents. Here we're initially loading an eighth note scale (by default, it goes into bank 0, program 0 and channel 1).;

Set fundamental (starting point of the scale in MIDI Pitch), f 31;

Open [pd tuning] for more details. Note that this example uses the [eqdiv] object to generate scales with equal divisions and starts with an eighth tone scale., f 62;

The 'set-tuning' message sets a tuning bank, a program number (both from 0-127), a MIDI channel and a tuning name - default values are (0, 0, 0, custom-tuning). The 'scale' message then sets the tuning into the bank/program and loads it into the channel for use. If you don't want to load the scale into any channel and just set it into a bank/program, use '0', while '-1' loads it into all channels., f 68;

The 'sel-tuning' message selects a bank/program in a given channel. The scale name is then output in the right outlet. If no scale is set, "Unnamed" is output. To unselect a tuning from a channel (say "2"), use 'unsel-tuning 2', or just 'unsel-tuning' to clear all channels (this loads the default 12 tone temperament back)., f 68;

[sfont~] also has microtonal capabilities. The 'scale' message sets a scale in cents and you can previously set a base value with the 'base' message, which sets the scale fundamental in MIDI pitch (60 by default, which is "C4"). Just 'scale' sets to the regular 12 tone temperament. Scales can have steps different that 12 and may not be based on the octave (such as the bohlen-Pierce scale). If picthes fall out of the 0-127 range, the keys are muted. This behaves similarly to the [retune] object. A "remap" message sets 128 MIDI Pitch values (from 0 to 127) for each MIDI key, so you can have a scale that doesn't repeat (decimal values are possible, so 60.5 is a quarter tone above middle C)., f 69;

If no extension is given, it searches for both ".sf2" and ".sf3" extensions. This is the same for the argument., f 38;

This is a big (6.8 MB) General MIDI soundbank that comes with ELSE for Pd Vanilla and is also available in PlugData., f 42;

[sfont~] is a sampler synthesizer that plays SoundFont files. It is based on FluidLite, a light version of FluidSynth., f 74;

outputs lists with soundfont name followed by lists that represent: <bank>, <program>, <preset name>, f 51;


## `sfz~`

Note that vanilla's [pgmin] object is indexed from 1 so you need to subtract 1 to use it on [sfz~], which is indexed from 0 ([pgm.in] from ELSE is also indexed from 0 by the way). The example below emulates a bend wheel, maybe an extra object for the future...;

Using Vanilla's MIDI input objects for specific MIDI messages. the channel values are not needed!, f 49;

The control change parameters are programmed in a given synthesizer, but if usually follows some standards like the messages where using here., f 72;

- 'note' for Note messages; - 'ctl' for Control Change; - 'pgm' for Program Change; - 'bend' for Pitch Bend; - 'touchin' for Channel Aftertouch; - 'polytouchin' for Key Aftertouch;

In the example of the parent patch, the list message as given by [keyboard] acts in the same way as a 'note' message., f 53;

Raw MIDI is also possible via float input, so you can use Pd Vanilla's [midiin] object or play a MIDI file from [midi]. You can also use vanilla's other MIDI objects like [pgmin] of course or the ones from ELSE, such as [pgm.in], see [pd MIDI-input] below., f 53;

This example uses the [eqdiv] object to generate scales with equal divisions and starts with an eighth tone scale., f 40;

The 'base' message sets the scale fundamental in MIDI pitch (60 by default, which is "C4"). Just 'scale' sets to the regular 12 tone temperament. Scales can have steps different that 12 and may not be based on the octave (such as the bohlen-Pierce scale). If picthes fall out of the 0-127 range, the keys are muted. This behaves similarly to the [retune] object.;

[sfz~] also has microtonal capabilities. The 'scale' message sets a scale in cents and you can previously set a base value with the 'base' message. See [pd scale] for more details., f 41;

The 'scala' message opens files in the scala format. See also:, f 41;

Play notes with either 'note' or list messages, whose arguments are: MIDI Pitch, Velocity and optional channel number., f 65;

There are also other MIDI like messages, such as 'ctl' for Control Change., f 29;

The [sfz~] object is based on 'sfizz', a SFZ player for the SFZ format. The SFZ format defines how a collection of samples are arranged for performance. It is quite different than a soundfont, which includes both the samples and the definitions of sample behavior in the same binary file, while SFZ is a file format which only defines the behavior of musical instruments and does not include the sample content., f 92;

A â.sfzâ file is just a text file, which can be created by any text editor (though for more complex cases with hundreds or thousands of samples, there are dedicated SFZ creation tools). The ".sfz" file can also not contain any samples and use internal oscillators and also internal processors, which makes the SFZ a hybrid synthesizer for samples and more., f 92;

* The .sfz extension is implied for both the open message and the argument., f 40;

Check the 'synth.sfz' file shipped with ELSE and used in this help file, it doesn't really use any existing sample but internal oscillators and other definitions like ADSR settings and a lowpass filter controlled by a LFO. The next subpatch shows this better., f 92;

scale in cents to retune (12-tone temperament if no list is given), f 52;

loads sfz file (.sfz extension implied) if no symbol is given, dialog window opens (same as click), f 52;

[sfz~] is a samole synthesizer for 'SFZ' instruments. For details on the SFZ format, players and instruments for download, see:, f 73;

The 'set' message allows you to load a whole .sfz file script. This is well suited for experts who really know what they're doing, but here are some basic examples., f 62;

Here we load the example file into a [text] object just so you can check it out. You can also use [text] to manipulate a string loaded as a file and send it to [sfz~] if you're a real nerd.;

Here we add a second sine oscillator. The envelope is set as a 'group' for both oscillators. The 2nd oscillator is a sine oscillator transposed an octave down., f 57;

Now we add a lowpass resonant filter (Q=10, Cuttof=1500, f 29;

Now we set MIDI Controller #1 to set an offset for the cutoff frequency, f 37;

Use the slider on the parent patch to change the control number value, f 38;

Here we finally have examples with samples, which are called from a path relative to the file's path., f 35;

When you load a string with samples. By default, the path relative to the patch is considered. If you want to use a custom relative patch you can use the 'path' message, which needs to come before the 'set' message., f 48;

The message below is the same as loading the 'sfz/synth2.sfz' file., f 23;

Note you can use [else/dir], [openpanel], [file cwd] and and [file patchpath] as in this example to help get to a desired custom path., f 29;


## `shaper~`

Here's an example of waveshaping with a given transfer function, but on a sine wave as a synthesis technique., f 56;

This particular transfer function generates a DC Offset, but [shaper~] filters out the DC component (0Hz) with an internal high pass filter set at 5 hz. This filter is on by default, but you can turn it off with the -filter flag or message., f 56;

[shaper~] also allows other functionalities besides waveshaping. For example, an LFO sine wave can scan through an audio sample forward and reverse, accelerating and decelerating, resulting in a turntable scratch effect. Check below., f 65;

[shaper~] performs waveshaping with transfer functions, in which signal input values (from -1 to 1) are mapped to the the transfer function's indexes. Values outside the -1 to 1 range are wrapped inside it., f 65;

You can set an array for [shaper~], as in this example, or use its internal transfer function for Chebyshev polynomials., f 65;

a symbol sets array/table name to be used for lookup, but a list of floats sets harmonic weights for internal transfer function (default 1)., f 55;

-dc: sets DC offset for internal transfer function (default 0), f 62;

If you don't give [shaper~] an array with a transfer function, it uses an internal one by default. This internal transfer function represents a summation of Chebyshev polynomials., f 70;

You can give a list of coefficients for each nth order polynomial. For a sine wave input, these represent the amplitudes for the harmonics generated by the transfer function, starting with the fundamental., f 70;

By default, [shaper~] loads a transfer function with the argument "1", which is the first order polynomial, which is just a linear function. Hence, it represents the fundamental., f 70;

The list of coefficients can be given as an argumnent or as a list input. The object, by default, normalizes the transfer function to output values between -1 and 1, but you can change that with the "norm" message or flag., f 70;

For non normalized outputs, you can also set a DC value, or 0th order polynomoal. This can also be set for a normalized function, but doesn't affect it. Clearly, the internal filter needs to be off as well., f 70;


## `shared`


## `sh~`


## `sig.m~`


## `sig2float~`

A bang will reset and sync the conversion rate. Each time you set a new rate interval in the right inlet, it'll also force a sync. If you do not want to sync, you can use the "set" message, in which case the new conversion rate will only be valid at the next conversion.;

[sig2float~] converts signals to floats. The conversion occurs at a time rate defined by the 1st argument or right inlet. It has support for multichannel signals., f 62;

Multichannel support example. When [sig2float~] takes a mutlichannel signal connection it outputs a list of floats with values for all channels., f 49;


## `sigs~`

[sigs~] is like vanilla's [sig~] but generates multichannel signals from an argument list and creates separate inlets for each argument (minimum size is 2)., f 62;


## `simplecounter`


## `sine~`

Syncing the phase with control messages is useful for LFOs and control with MIDI. A sync with audio is useful for the "hard sync" technique, where an oscillator is synced according to the frequency of a master frequency., f 56;

The "phase sync" inlet is quite different from the "phase offset" inlet. They are completely independent!, f 43;

Soft sync is also possible with the '-soft' flag or the "soft" message, where it alternates between positive and negative frequencies and sounds less harsh.;

The second inlet resets the phase ands behaves in the same way for control data as objects like [osc~] and [phasor~] in Pd. A number input resets the oscillator and restarts the cycle with an initial phase that corresponds to the input number, so the internal phase is synced to the given value. The phase values are from 0 to 1 and values beyond that are wrapped within this range. The control message reset is meaningful for LFOs.;

Additionally, you can reset the oscillator with an impulse signal. Inputs that are > 0 and <= 1 reset the phase Pd expects an impulse signal for syncing. The impulse values need to be > 0 and <= 1 (otherwise ignored). Because phase is cyclical, the value of 1 represents the "phase 0" of the cycle, where the impulse occurs. Send it impulses above and check the result. Use a multiplier to reset to another phase value.;

The second argument sets an initial phase (or "phase offset"). This is also settable with the third inlet. This allows you to control two oscillators with the same frequency falling in and out of phase. Another feature is phase modulation., f 53;

The phase values are wrapped into the 0-1 range, since the phase cycle is from 0 to 1 (where 1 is also the start of another cycle).;

By default, frequency input is in hertz, but if you use the 'midi' message or '-midi' flag you can change it to MIDI pitch input, where it is not really bound to the 0 to 127 range, neither it has to be integers. This is just like using [mtof~]...;

-midi: sets frequency input in MIDI pitch (default hertz), f 58;

If the oscillator has a multichannel left input, it outputs the same number of channels. If the secondary inlets have a signal with a single channel for sync and phase modulation, the single value is applied to all channels. If a secondary inlet is also a multichhanel signal, then each channel gets its sync or phase deviation value. Note, however, that the number of multichannels in secondary inlets need to match the same number of channels from the left input., f 76;

You can initialize the object with multichannel if you give it a list of frequencies with the -mc flag (you can't set phases though). A list input also works if no signal is connected to set it to multichannel with a list of frequency input., f 49;

[sine~] is a sinusoidal oscillator that accepts negative frequencies, has inlets for phase sync and phase modulation. It also has support for multichannels., f 69;

-mc <list>: sets multichannel output with a list of frequencies, f 63;


## `sin~`

[sin~] is similar to [cos~], it outputs the sine of two pi times its signal input. It has support for multichannel signals.;


## `slew`


## `slew2`


## `slew2~`

[slew2~] is like [slew~] but has independent values for upwards & downwards ramps. It takes an amplitude limit per second and generates a line towards the incoming value. The difference between [slew~] and [glide~] is that [slew~] has a fixed speed, not a fixed period. A limit of zero stops the line generation and a negative value turns the limiter off (but again, up and down limits are independent)., f 75;

When new values come in, the object limits the change to a maximum step until it reaches the new value. A speed of "1" means that it takes one second to move to a difference of 1 in amplitue. The actual step between subsequent changes depend on this speed and the sample rate., f 61;

If you have a sample rate of 44100 samples per second, then a second has 44100 steps. If the speed is then "1", this means that the step value is 1/44100 (2.26757e-05). So a shift between 0 and 1 takes 44100 steps of 2.26757e-05 and a second to reach 1!, f 61;

If [slew2~] has a multichannel left input, it outputs the same number of channels. If the secondary inlets have a single channel for the up/down slew limit, the single value is applied to all channels. If a secondary inlet is also a multichhanel signal, then each channel gets its own limit value. Note, however, that the number of multichannels in secondary inlets need to match the same number of channels from the left input., f 65;


## `slew~`

When new values come in, the object limits the change to a maximum step until it reaches the new value. A speed of "1" means that it takes one second to move to a difference of 1 in amplitue. The actual step between subsequent changes depend on this speed and the sample rate., f 61;

If you have a sample rate of 44100 samples per second, then a second has 44100 steps. If the speed is then "1", this means that the step value is 1/44100 (2.26757e-05). So a shift between 0 and 1 takes 44100 steps of 2.26757e-05 and a second to reach 1!, f 61;

[slew~] takes an amplitude limit per second and an incoming value to be 'slew limited'. It then generates a line towards the incoming value. The difference between [slew~] and [glide~] is that [slew~] has a fixed speed, not a fixed period. A limit of zero stops the line generation and a negative value turns the limiter off. There's support for multichannel signals., f 71;

If [slew~] has a multichannel input, it outputs the same number of channels. If the right inlet has a single channel for the slew limit, the value is applied to all channels. If the right inlet is also a multichhanel signal, then each channel gets its own limit value. Note, however, that the number of multichannels in the right inlet needs to match the same number of channels from the left input., f 65;


## `slice`

[slice] splits lists. The 'n' split point is set via argument or right inlet. If you slice at 'n', the left outlet spits the first 'n' elements and the right outlet sends the remaining elements. If you slice at '-n', the right outlet spits the last 'n' elements and the left outlet sends the first elements. If the number of elements is less than the split point, the whole list is output to the left if 'n' is positive, and to the right if negative. Symbols and floats are also taken., f 81;


## `slice~`

[slice~] splits a multichannel signal. The 'n' split point is set via argument or float input. If you slice at 'n', the left outlet spits the first 'n' channels and the right outlet sends the remaining channels. If you slice at '-n', the right outlet spits the last 'n' channels and the left outlet sends the first channels. If the number of channels is less than the split point, the whole signal is output to the left if 'n' is positive (and the right outlet outputs zeros), and to the right if negative (and the left outlet outputs zeros)., f 76;


## `slider2d`

If you send it a list of x/y coordinates, the [slider3d] object will clip it inside its range and output it.;

The "set" message behaves similarly, it just doesn't output the incoming value., f 56;

By default, the slider output range is from 0 to 127, but you can change it with the -range flag or the range message, which sets the range for both x and y dimensions. But you can also set independent range for both x and y with the -xrange, -yrange or xrange, yrange messages. Note that a bang rescales the last output according to the new range., f 64;

You can set the size with the '-size' flag or with the 'size' message., f 25;

You can also set x and y dimensions independently with the 'width'/'height' messages., f 49;

Or you can set the both with the '-dim' flag or with the 'dim' message., f 28;

You can set background and frontground colors with 'bgcolor'/'fgcolor' messages and '-bgcolor'/'-fgcolor' flags., f 40;

You can set the 'line' visibility with the line message or '-line' flag. Line is visible by default., f 40;

There's also a grid visibility option (invisible by default). You can set it with the 'grid' message or '-grid' flag., f 40;

You can set the size with the '-size' flag or with the 'size' message., f 25;

-range: sets x/y range <float, float> (default: 0, 127), f 70;

-bgcolor <f, f, f>: sets background color in RGB (default 255 255 255), f 70;

-fgcolor <f, f, f>: sets frontground color in RGB (default 0 0 0), f 70;

-grid <float>: non zero sets grid visibility (default: 0), f 70;

-dim <float, float>: sets x/y sizes independently (default: 127), f 70;

You can also set send/receive names with the 'send'/'receive' messages or '-send'/'-receive' flags., f 31;

Setting these to 'empty' removes the send/receive symbols., f 32;

Make sure to escape "\$0" properly with backslashes (as in: "\\\$0")., f 24;

[slider3d] is a two dimensional slider GUI abstraction (see also [else/circle)., f 42;

With the 'savestate' message or '-savestate' flag, the GUI operates in 'save state mode', where it saves the state from the last time the patch was saved. Note that this is only useful for patches and not abstractions. For abstractions oyou should use [savestate] instead, and also have a look at [presets]. Unlike iemguis, the value is not output when loading the patch, use [loadbang] for that.;


## `sort`


## `spectrograph~`

[spectrograph~] is an abstraction for visualizing FFT amplitudes from 0hz to Nyquist. It uses a hann table for the analysis., f 64;

When you set the graph rate to 0, it stops graphing, but you can then use the bang message to graph the input., f 52;


## `speed`


## `spread`

The extra mode makes it split to the left if it less or equal than the argument, or to he right if greater than the argument., f 57;

The default mode is like [moses] where it spreads at the split point and divides to the left if the first element in the list is smaller than the argument (so it spreads to the right if it's equal or greater than the argument)., f 57;

-mode <float>: sets mode, 0 (default) and 1 (in reverse to [moses]), f 67;

Similar to [moses], [spread] compares an incoming float as the 1st element of a list to the arguments and spreads to different outputs. One difference to [moses] is that it takes multiple arguments and has an extra mode., f 76;

This example uses [spread] to split notes from [keyboard] so you can route them to different synths., f 46;


## `spread.mc~`

[spread.mc~] spreads any number of input channels across any number of output channels with equal power panning according to a spread parameter. It takes and outputs a multichannel signal., f 62;

The algorithm is basically the same as [pan~] where each input gets it's location according proportional to the output. In the first example below, the signals "1" and "3" correspond exactly to the outer channels, but "2" sits in between the two middle outputs, so the signal is panned to both at mid point via the usual Sine/Cosine equal power function. This is considering the default spread value of 1!, f 71;

Spread values greater than 1 spreads the signal to more channels while smaller than 1 narrows the crossfading point closer to the selected channel. In the example below, if you give it a spread value of 0.5, "2" doesn't reach any of the outputs while "1" and "3" still match the exact spot of the outer outputs. Values greater than one will spread "1" and "3 to adjacent channels (and it spreads circularly like [pan~])., f 71;

Try also the other exanmple by setting 'n' to '5' to see if you can figure this out., f 70;


## `spread~`

[spread~] spreads any number of input channels across any number of output channels with equal power panning according to a spread parameter.;

The algorithm is basically the same as [pan~] where each input gets it's location according proportional to the output. In the first example below, [sig~ 1] and [sig~ 3] correspond exactly to the outer channels, but [sig~ 2] sits in between the two middle outputs, so the signal is panned to both at mid point via the usual Sine/Cosine equal power function. This is considering the default spread value of 1!, f 71;

Spread values greater than 1 spreads the signal to more channels while smaller than 1 narrows the crossfading point closer to the selected channel. In the example below, if you give it a spread value of 0.5, [sig~ 2] doesn't reach any of the outputs while [sig~ 1] and [sig~ 3] still match the exact spot of the outer outputs. Values greater than one will spread [sig~ 1] and [sig~ 3] to adjacent channels (and it spreads circularly like [pan~])., f 71;

Try also the other exanmple at the bottom and see if you can figure this out., f 70;


## `square~`

The pulse width is set via the first argument or the second inlet.;

The pulse width parameter controls how much of the cycle is "1" or "-1". A pulse width of 0.5 means the first half is "1" and the last half is "-1".;

A pulse width of 0 has the first sample is "1" and the rest is "-1". Conversely, a pulse width of 1 has the opposite situation (the entire period is "1" except the last sample, which is "-1").;

The phase values are wrapped into the 0-1 range, since the phase cycle is from 0 to 1 - where 1 is also the start of another cycle., f 36;

The third argument sets an initial phase (or "phase offset"). This is also settable with the fourth inlet. In such a way, you have two objects with the same frequency falling out and back in sync. Another feature is phase modulation., f 51;

[square~] is a square oscillator that accepts negative frequencies, has inlets for pulse width, phase sync and phase modulation. It also has support for multichannels., f 67;

Syncing the phase with control messages is useful for LFOs and control with MIDI. A sync with audio is useful for the "hard sync" technique, where an oscillator is synced according to the frequency of a master frequency., f 56;

The "phase sync" inlet is quite different from the "phase offset" inlet. They are completely independent!, f 43;

Soft sync is also possible with the '-soft' flag or the "soft" message, where it alternates between positive and negative frequencies and sounds less harsh.;

Additionally, you can reset the oscillator with an impulse signal. Inputs that are > 0 and <= 1 reset the phase Pd expects an impulse signal for syncing. The impulse values need to be > 0 and <= 1 (otherwise ignored). Because phase is cyclical, the value of 1 represents the "phase 0" of the cycle, where the impulse occurs. Send it impulses above and check the result. Use a multiplier to reset to another phase value.;

The third inlet resets the phase ands behaves in the same way for control data as objects like [osc~] and [phasor~] in Pd. A number input resets the oscillator and restarts the cycle with an initial phase that corresponds to the input number, so the internal phase is synced to the given value. The phase values are from 0 to 1 and values beyond that are wrapped within this range. The control message reset is meaningful for LFOs.;

By default, frequency input is in hertz, but if you use the 'midi' message or '-midi' flag you can change it to MIDI pitch input, where it is bound to the 0 to 127 range (but they don't have to be integers) - this is kinda like using [mtof~]...;

If the oscillator has a multichannel left input, it outputs the same number of channels. If the secondary inlets have a signal with a single channel for sync and phase modulation, the single value is applied to all channels. If a secondary inlet is also a multichhanel signal, then each channel gets its sync or phase deviation value. Note, however, that the number of multichannels in secondary inlets need to match the same number of channels from the left input., f 76;

You can initialize the object with multichannel if you give it a list of frequencies with the -mc flag (you can't set phases though). A list input also works if no signal is connected to set it to multichannel with a list of frequency input., f 49;

-midi: sets frequency input in MIDI pitch (default hertz), f 58;

-mc <list>: sets multichannel output with a list of frequencies, f 63;


## `sr~`

Unlike [samplerate~], [sr~] always gives you the global sample rate as defined in Pd's audio settings instead of the up/downsampling rate running in the patch due to [block~]., f 56;

[sr~] can set the sample rate and also reports the sample rate frequency or period when loading the patch, when receiving a bang or when it changes. It also outputs the value at 'init' time (that is before [loadbang]). The frequency is reported either in hz or khz and the period either in seconds os milliseconds. Unlike [samplerate~], it doesn't report up/down sampling rates. The default output is the sample rate frequency in hertz., f 76;

[sr~] can take a [value] name as an argument. You can then retrieve this value in another [value] or [var] object or inside an expressionin [expr];


## `stack`


## `standard~`


## `status`


## `status~`


## `stepnoise`


## `stepnoise~`

The [stepnoise~] object produces frequencies limited to a band from 0 up to the frequency it is running. It can go up to the sample rate, and when that happens, it's basically a white noise generator., f 73;

[stepnoise~] can be used to control parameters of other objects. Here we control the frequency of an oscillator.;

Pseudo random number generators aren't true random number generators. Instead, an algorithm is used to provide a sequence of numbers that seems random. The same sequence can be reproduced if you set a "seed" value, which can be any integer number., f 52;

You can set a seed with the '-seed' flag. If you don't supply it, each object gets its own seed internal seed. If you send a 'seed' message without float, the object also gets a unique seed value., f 52;

Seeds are kept locally, which means that if two [stepnoise~] objects are seeded the same they will have the same output. Conversely, you can seed the same [stepnoise~] object twice with the same seed to repeat the output., f 52;

[stepnoise~] is a low frequency (band limited) noise generator without interpolation, therefore it holds at a random value, resulting in random steps. Random values are between -1 and 1 at a rate in hertz (negative frequencies accepted). Use the seed message if you want a reproducible output. It has support for multichannels., f 73;

The -ch flag or message sets the number of output channels. This is only meaningful if you have a single channel input., f 42;

You can initialize the object with multichannel if you give it a list of frequencies with the -mc flag (you can't set phases though). A list input also works if no signal is connected to set it to multichannel with a list of frequency input., f 62;

If you have a multichannel connection in the frequency input, [randpulse2~] generates a signal with the same number of channels and the 'ch' message or flag is meaningless. The multichannel input is the density for each output., f 44;

-mc <list>: sets multichannel output with a list of frequencies, f 63;


## `stereo.rev~`

[mono.rev~] is a stereo input/output reverb abstraction, a variant of [mono.rev~] with two independent reverb channels.;


## `store`

The [store] object is based on Pd Vanilla's [text] object. You can open its window with the 'show' message and close it with the 'hide' message. Clicking on the object also opens it. This also means you can manually edit the contents of stack!;

You can store messages with the object if it has a non zero argument., f 39;

A dump message outputs all stored messages, the information is kept., f 34;

[store] is an abstraction based on [text] that stores incoming messages sequentially., f 73;

float - non-zero sets to store elements with the patch (default 0), f 66;


## `stream`


## `stretch.shift~`

[stretch.shift~] is like [gran.player~], but for live input. It provides independent time stretching and pitch shifting via granulation., f 69;


## `sum`


## `sum~`

[sum~] takes a multisignal connection and sums them into a single mono channel.;


## `susloop~`

You can use [susloop~] to read samples with or without given loop points., f 31;

[susloop~] generates a control signal designed to read buffers and loop at a given section. It responds to a gate input (float or signal).;

gate: 0 to non-0 transition: trigger (starts from 0 and loops). Non-0 to 0 transition: release (loop is off);

- stops and goes back to 0, expects a trigger to restart, f 57;


## `suspedal`

[suspedal] holds MIDI Note Off messages when on and sends them out when it's switched off. It has two sustain modes, 'regular' (default) and 'tonal' - as in the design of modern pianos., f 63;

You can directly connect the [notein] object to access MIDI note messages from an external controller and access the MIDI message from an actual sustain pedal (which is normally controller number 64) and feed it to the [suspedal] object.;

The default sustain mode - used in this example - holds any note off messages when it is on. Below, we use [suspedal] in a patch with 2-voice polyphonic synth controlled by random notes. This example uses [voices] but you can also use vanilla's [poly].;

[suspedal] has 4 different modes of handling repeated notes. These are for either 'regular' or 'tonal' modes, and they are:, f 62;

'free first' - sends a note off before retriggering a repeated note, f 59;

The above objects interact well with [suspedal] and its retrigger modes., f 18;

'free later' - keeps a history of all received Note-Ons and sends note off messages for all of them when the pedal is switched off (unlike mode 1, which only sends one not off);

In the 'tonal' mode, as in the design of piano sustain pedals, you can sustain notes that are currently on but not the new ones after you switch it on., f 62;

This allows you to sustain a bass/chord while being able to use both hands to play further notes. This is useful for [poly] or [voices], but also [mono]., f 62;

-retrig <float> - sets retriger mode <0, 1, 2 or 3> (default 0), f 63;


## `svfilter~`


## `swap2`


## `swarm`


## `symbol2any`


## `synth~`

[synth~] is based on [clone] and [mono]/[voices]. If you set the number of voices to 1 the synth is monophonic and uses [mono] with the default setting of going back to the "last" voice., f 71;

If you use the "load" message, you can give an optional 2nd float argument to set the number of voices. If you don't, the previously set number of voices prevails. A "voices" message can change the number of voices., f 71;

If you set the number of voices to 2 or more the synth is polyphonic and uses [voices] with the default settings and "voice stealing"., f 39;

[synth~] expects list values for pitch and velocity, as given by the [else/keyboard] object., f 52;

There's also the 'mc' message/flag that we'll see later and custom messages that we'll see next., f 41;

[synth~] is multichannel aware and can send a multichannel signal out with the '-mc' flag or message., f 34;

The multichannel output carries a number of channels that is the same as the number of voices, and each voice is part of a single channel., f 34;

Hence, for a monophonic synth the number of output channels is only one either way. Two voices give you a stereo connection, four voices a quadraphonic and so on., f 34;

You can have several custom messages taken by your abstraction. In the template we have the "adsr" message that sets the parameter of an [adsr~] object, for instance. Click and open the template to check it out and also note that the release parameter from within the abstraction we're sending the release value to the parent [synth~] abstraction. This sets the 'release' value of [voices] and is only useful for polyphonic synths., f 66;

The idea of [synth~] is to generate synth voices involving basic units of oscillators, envelopes and synth techniques such as FM and stuff. You can also have some FX modules such as reverbs or whatever inside the abstraction, but such things are way more reasonable to have outside the cloned abstraction for processing the overall sound, as in the example to the left where we add a plate reverb., f 48;

By sending the 'adsr' message, the loaded abstraction also sets the release value of [voices]., f 41;

Extra arguments besides abstraction name and number of voices are sent to the abstraction. Open to check it., f 37;

The [synth~] object loads synth abstractions that follow a simple template. It is just a wrapper over [clone] and [mono]/[voices] but may provide some convenience, specially to newbies. One convenience is the ability to open/load different abstractions in runtime. The arguments are abstraction name and number of voices. If no arguments are given, a default and simple abstraction is loaded as a template and basis to build new synths. Clicking on the object opens the loaded abstraction. Shift click opens a panel to choose an abstraction., f 81;


## `sysrt.in`


## `sysrt.out`


## `tabgen`

[tabgen] is an abstraction that generates different functions for a given table name., f 65;

The 'gauss <float>' message creates a gaussian function and the argument sets the sigma value (from 0 to 1). You can also use the 'apply' command to apply an envelope existing values in a table., f 63;

The 'sin <list>' message creates a series of sinusoids. Each sinusoid is specified by 3 values, which are; - number of cycles; - initial phase (0-1); - amplitude - default;, f 56;

half a cycle (doesn't have to be integers) starting at phase 0.5, f 64;

for a single sinusoid - that is a list of only 3 values - the phase and amplitude are optional and the default values are, respectively, 0 and 1, but for more than 2 sinusoids, all arguments are necessary.;

You can also use the 'apply' command to apply an envelope existing values in a table. In this case the 'sin' command takes only two values which is the number of cycles and initial phase of a single sinusoid (the amplitude is always 1)., f 49;

The 'sinc <list>' message draws a sinc function. The 1st argument sets the number of times the function reaches zero on both sides. An additional optional non zero argument considers only the right side.;

These commands draw FFT window functions, for now only 'hanning' and 'hamming'., f 41;

The kaiser window takes an alpha value argument (default 6), f 32;

You can also use the 'apply' command to apply an envelope existing values in a table with all these windowing functions., f 46;

* gaussian and sine can also be used to generate FFT windows., f 62;

The 'trapezoid <float, float>' message creates a trapezoid. It has a default value of 0.1 and 0.9 and these parameters control, respectively, the phase points where the upwards ramp ends and the downwards curve starts. You can also use the 'apply' command to apply an envelope existing values in a table., f 76;

The 'vsaw <float>' message creates a variable triangle. It has a default value of 0.5, which controls the phase point with the maximum value. You can also use the 'apply' command to apply an envelope existing values in a table.;

commands to generate functions: (details in [pd examples]), f 41;


## `tabplayer~`

Multi channel playback is possible (up to 64 channels) when you specify it with a second argument. The number of channels defines the number 'n' of outlets - where the first outlets are the channel inputs and the rightmost is the bang outlet.;

If more than one channel is set, the name convention for multi channel arrays is the table name preceded by the channel number (starting from zero) and "-", such as: "0-", "1-", "2-", "3-", and so on...;

You can manually set multi channel arrays in Pd like that or use the [sample~] object, which does this internally.;

If the [sample~] object has fewer channels than the number of output channels in [tabplayer~], the extra channels output a zero signal.;

A signal input is used to play the table at the audio rate. By default we have a 'gate' mode, where it works just like a toggle (non zero starts playing, zero stops)., f 53;

Alternativelly, in 'trigger' mode, an impulse can be used as a bang (use the 'tr' message or the '-tr' flag for it). In practice, this just ignores when the signal goes back to 0 so you can also use a pulse input instead., f 53;

The loop message takes a float, where a non-zero value enables looping and, 0 disables it (default is disabled). You can set it to loop with the -loop flag., f 37;

same as 'zero': stops playing and outputs 0 (cannot be resumed), f 33;

The 'play' message can also take up to 3 floats that specify; 1) starting point in the array (in ms); 2) end point (in ms); 3) speed rate percentage; If no floats are given, then it plays with the previous given settings. Use 'reset' if needed., f 50;

- sets start and end point range proportionally (from 0 to 1), f 61;

- sets position proportionally within range (from 0 to 1), f 61;

The pos message, from 0 to 1, sets a point within the set range and starts playing from it. But if you retrigger the object to play again with a bang, it doesn't restart from that point anymore, but the previously set point (which is the start point if speed is positive or end if the speed is negative). When already playing, if you send a 'pos' message, it jumps to that point and keeps playing from it.;

You can set a fade in and fade out time in ms with the 'fade' message or '-fade' flag. This fades in from the start point and fades out to reach the end point., f 54;

When you are looping, you can set to crossfade mode with the 'xfade' message or '-xfade' flag. This way, when it fades out, it starts fading before the the loop restarts. The crossfade is a sine/cosine equal power function., f 54;

- sets to crossfade mode when looping (default no crossfade), f 61;

- non zero enables looping, <0> disables it (default 0), f 61;

- sets sample rate of sample (default, Pd's sample rate), f 61;

start playing - optional 1st float sets start (ms), 2nd sets end (in ms) and 3rd sets speed rate, f 59;

gate on or impulse starts playing, gate off stops if not in trigger mode, which is the default mode;

- non zero sets to trigger mode, zero sets to gate mode, f 61;

[tabplayer~] plays arrays with multichannel support. It can play backwards, in different speeds and loop., f 52;

-fade <float> | -speed <float> | -tr: sets to trigger mode | -loop: sets to loop mode -xfade: sets to crossfade mode | -sr <float> | -range <f, f> | -lagrange: sets to lagrange interpolation mode (default spline), f 75;

You can change Pd's sample rate and see how the file always plays at the same speed., f 27;

By default, [tabplayer~] uses 'spline' interpolation, but you can set to lagrange instead. For more details, check the subsection 'interpolation' of chapter 28 (buffer) in the live elctronics tutorial., f 65;

You can set the sample rate of the loaded sound file. This allows [tabplayer~] to adjust the reading rate to correspond to the sound file's sample rate. Note, however, that this is not need if you're using [sample~]., f 63;

In the example below we have a sound file whose sample rate is 88200 Hz. If Pd's sample rate is at 44100 (the default one), then playing this file at Pd's sample rate would read it at half speed. Since the file is loaded with [sample~], the sample rate is internally and automatically retrieved. Note that the [sample~] object also outputs the sample rate, and so does [soundfiler]., f 63;


## `tabreader`

set <symbol> - sets an entire array to be used as a waveform, f 62;

By default, [tabreader] uses the 'spline' interpolation, but you can set it to other interpolation types and even none. For more details on the available interpolation methods, check the subsection 'interpolation' of chapter 28 (buffer) in the "Live Elctronics Tutorial" that comes with ELSE., f 56;

In ELSE, multichannel arrays follow a naming convention where the table name is preceded by the channel number (starting from zero) and "-", such as: "0-", "1-", "2-", "3-", and so on..., f 61;

This happens, for instance, when you load a sample with the [sample~] object, but you can also crete arrays manually this way (as in this example). You can then change and set the channel with the "channel" message. By default, it loads "channel 1", but you can set a different channel with the 'ch' flag at creation (as in this example)., f 61;

In indexed mode you have to feed the actual index number and it goes from zero to the table size minus 1 (0 to 511 in this example). You san set it to indexed mode with the 'index' flag or the 'index' message., f 47;

The buffer is considered to be circular in loop mode, so when you reach 1 is the same going back to 0 when not in indexed mode. If you're in indexed mode, then the table undex range is from 0 to the table size (512) in this example, where the table size index (512) is the same as the table start (0). You san set it to indexed mode with the 'index' flag or the 'index' message., f 48;

If you connect a [phasor] into [tabreader], it becomes a low frequency wavetable oscillator. Note that besides the first argument, the "set" message followed by an array name sets an array to be read., f 47;

[tabreader] accepts indexes from 0 to 1 by default and reads an array with different interpolation methods with multi channel support. There's no need to have guard points in the array as these are taken care of internally., f 77;


## `tabreader~`

set <symbol> - sets an entire array to be used as a waveform, f 62;

By default, [tabreader] uses the 'spline' interpolation, but you can set it to other interpolation types and even none. For more details on the available interpolation methods, check the subsection 'interpolation' of chapter 28 (buffer) in the "Live Elctronics Tutorial" that comes with ELSE.;

In ELSE, multichannel arrays follow a naming convention where the table name is preceded by the channel number (starting from zero) and "-", such as: "0-", "1-", "2-", "3-", and so on..., f 61;

This happens, for instance, when you load a sample with the [sample~] object as in this example (but you can also crete arrays manually this way). You can then change and set the channel with the "channel" message. By default, it loads "channel 1", but you can set a different channel with the 'ch' flag or 2nd argument (as in this example)., f 61;

[tabreader] accepts indexes from 0 to 1 by default and reads an array with different interpolation methods with multi channel support. There's no need to have guard points in the array as these are taken care of internally., f 63;

If you connect a [phasor~] into [tabreader~], in loop mode, it becomes a wavetable oscillator like [tabosc4~] or [else/wavetable~]. Note that besides the first argument, the "set" message followed by an array name sets an array to be read., f 47;

The buffer is considered to be circular in loop mode. When not in indexed mode, if you reach "1" it is the same as going back to "0". If you're in indexed mode, then the table index range is from 0 to the table size (512 in this example) if you're in loop mode. This way, the table size index (512) is the same as the table start (0). You can set it to indexed mode with the 'index' flag or the 'index' message., f 48;

In indexed mode you have to feed the actual index number and it goes from zero to the table size minus 1 (0 to 511 in this example). You can set it to indexed mode with the 'index' flag or the 'index' message., f 47;


## `tabwriter~`

If more than one channel is set, the name convention for multi channel arrays is the table name preceded by the channel number (starting from zero) and "-", such as: "0-", "1-", "2-", "3-", and so on..., f 60;

Multi channel recording is possible (up to 64 channels) when you specify it with a second argument. The number of channels defines the number 'n' of inlets - where the first outlets are the channel inputs and the two rightmost are the range inlets.;

You can manually set multi channel arrays in Pd like that or use the [sample~] object, which does this internally.;

You can change the start and end points in ms with the 'start'/'end' messages. The range message sets end/start points proportionally. The continue, loop, start and end can be indicated also as flags., f 69;

- sets start and end point range proportionally (from 0 to 1), f 61;

- gate to start recording (default) or index to record to, f 59;

[tabwriter~] records up to 64 signal channels into arrays. You can trigger it or set index to write to with sample accuracy., f 63;

By default, the right inlet is a gate at audio rate to start/stop recording., f 40;

In indexed mode, the outlets are non functional and the loop/continue modes are useless, because you set the index input to record to directly. This is a lower level option that can be useful if you wanna go a bit crazy or implement some complex algorithm., f 48;


## `tap`


## `tempo`


## `tempo~`


## `timed.gate`


## `timed.gate~`

A bang will trigger the object to generate a gate. By default, the initial gate value is "1", but you can change that with the second argument. A bang will also output the last received gate value from a signal or float input., f 53;

By default, a gate needs to finish before another one is triggered, but you can change to "retrigger" mode, where a new timed gate starts before the last was finished., f 53;

You can set to retrigger mode with the retrigger message or the third argument., f 53;

When receiving an impulse or a float, [timed.gate~] sends a timed gate (with the value of the impulse/float for the given duration, 0 otherwise). The length of the gate is given in ms, if 0 or less is given, no gate is output.;


## `toggleff~`


## `touch.in`

An argument sets the channel number. If so, only MIDI messages that correspond to that channel are sent. If no channel is given, it loads "0" as the default and the object operates in omni mode, where the objects outputs values from all channels and the channel number is output in the right outlet. You can also change the channel with the right inlet (0 sets to omni)., f 67;

Port number is encoded as the channel number. Channels 1 to 16 are for port 1, channels 17 to 32 is the same as channels 1 to 16 for port 2, channels 33 to 48 represents channels 1 to 16 in port 3, and so on..., f 63;

The object automatically listens to whatever is connected as a MIDI device in Pd. So it's like it has a built in [midiin] object feeding it. This is considered to be an "internal" source.;

The left inlet provides and "external" source of raw MIDI data input. This is needed if you have, for instance, the [midi] object from ELSE reading a MIDI file or something. If, by any chance, you just want the object to receive from this external source and not listen to the internal connected device, you can use the '-ext' flag or 'ext' message, to force only the external input.;

[touch.in] extracts MIDI Aftertouch information from raw MIDI input or a connected MIDI device., f 61;


## `touch.out`

[touch.out] formats and sends raw MIDI aftertouch messages to Pd's MIDI output and its outlet. An argument sets channel number (the default is 1)., f 66;

The object automatically outputs to whatever is connected as a MIDI device in Pd. So it's like it has a built in [midiout] object. If, by any chance, you just want the object to output to the outlet (for feeding a [midi] object or something), you can use the '-ext' flag or 'ext' message., f 61;


## `tremolo~`

The [tremolo~] abstraction performs amplitude modulation. It takes a signal input, a tremolo frequency and a tremolo depth. Classic amplitude modulation is achieved with a depth of 1!, f 61;


## `trig.delay2~`


## `trig.delay~`


## `trig2bang`


## `trig2bang~`


## `trighold~`


## `tri~`

-midi: sets frequency input in MIDI pitch (default hertz), f 58;

-mc <list>: sets multichannel output with a list of frequencies, f 63;

Syncing the phase with control messages is useful for LFOs and control with MIDI. A sync with audio is useful for the "hard sync" technique, where an oscillator is synced according to the frequency of a master frequency., f 56;

The "phase sync" inlet is quite different from the "phase offset" inlet. They are completely independent!, f 43;

Soft sync is also possible with the '-soft' flag or the "soft" message, where it alternates between positive and negative frequencies and sounds less harsh.;

The second inlet resets the phase ands behaves in the same way for control data as objects like [osc~] and [phasor~] in Pd. A number input resets the oscillator and restarts the cycle with an initial phase that corresponds to the input number, so the internal phase is synced to the given value. The phase values are from 0 to 1 and values beyond that are wrapped within this range. The control message reset is meaningful for LFOs.;

Additionally, you can reset the oscillator with an impulse signal. Inputs that are > 0 and <= 1 reset the phase Pd expects an impulse signal for syncing. The impulse values need to be > 0 and <= 1 (otherwise ignored). Because phase is cyclical, the value of 1 represents the "phase 0" of the cycle, where the impulse occurs. Send it impulses above and check the result. Use a multiplier to reset to another phase value.;

The second argument sets an initial phase (or "phase offset"). This is also settable with the third inlet. This allows you to control two oscillators with the same frequency falling in and out of phase. Another feature is phase modulation., f 53;

The phase values are wrapped into the 0-1 range, since the phase cycle is from 0 to 1 (where 1 is also the start of another cycle)., f 45;

By default, frequency input is in hertz, but if you use the 'midi' message or '-midi' flag you can change it to MIDI pitch input, where it is bound to the 0 to 127 range (but they don't have to be integers) - this is kinda like using [mtof~]...;

If the oscillator has a multichannel left input, it outputs the same number of channels. If the secondary inlets have a signal with a single channel for sync and phase modulation, the single value is applied to all channels. If a secondary inlet is also a multichhanel signal, then each channel gets its sync or phase deviation value. Note, however, that the number of multichannels in secondary inlets need to match the same number of channels from the left input., f 76;

You can initialize the object with multichannel if you give it a list of frequencies with the -mc flag (you can't set phases though). A list input also works if no signal is connected to set it to multichannel with a list of frequency input., f 49;

[tri~] is a triangular wave oscillator that accepts negative frequencies, has inlets for phase sync and phase modulation. It also has support for multichannels., f 73;


## `trunc`

[trunc] truncates floats and lists towards zero, that means only the integer value is considered, like in vanilla's [int]., f 63;


## `trunc~`

[trunc~] truncates a signal towards zero, that means only the integer value is considered. It has support for multichannel connections.;


## `unite`


## `unmerge`

number of outlets from 2-512 (default 2), there's an extra outlet for the extra elements, f 50;

[unmerge] separates the elements of a message in groups of any size (default 1). Each group is sent out a separate outlet, extra elements are sent to an extra rightmost outlet., f 69;


## `unmerge~`

[unmerge~] separates the channels of a multichannel signal in groups of any size (default 1). Each group is sent out a separate outlet, extra elements are sent to an extra rightmost outlet. If the number of channels is less than the number of outlets, zeroes are output., f 71;

number of outlets, there's an extra outlet for the extra channels, f 50;


## `var`

Like [value], [var] gets a value if you send a value to a named variable with [send] and other sending mechanisms available in the Pd Vanilla objects [float, [int] and [value] intself. Unlike these other objects, [var] does not have a 'send' message though., f 57;

Note that [var] also shares variables with [value]. You can also set or retrieve [var] values in [expr]., f 35;

[var] is similar to [value] but it can set and recall more than one variable as lists., f 64;


## `vca.m~`

This mono VCA module has a signal input and a CV control to set the VCA level., f 23;

This module has support for MultiChannels and the VU displays the average sum of all channels., f 24;


## `vcf.m~`

This Lowpass module takes a single channel input, cutoff in Hz and Reson in Q., f 28;

The signal CV inlets for Cutoff and Reson depend on the attenuverter controls and add to the values set by the knobs., f 28;


## `vco.m~`

This VCO module has a polyphonic MIDI pitch input. Other inlets are CV signals to set FM (Frequency Modulation), PM (Phase Modulation), PWM (for square wave and variable saw) and a sync inlet that takes impulses., f 23;


## `velvet~`

Pseudo random number generators aren't true random number generators. Instead, an algorithm is used to provide a sequence of numbers that seems random. The same sequence can be reproduced if you set a "seed" value, which can be any integer number., f 57;

You can set a seed with the '-seed' flag. If you don't supply it, each object gets its own seed internal seed. If you send a 'seed' message without float, the object also gets a unique seed value., f 57;

Seeds are kept locally, which means that if two velvet~] objects are seeded the same they will have the same output. Conversely, you can seed the same [velvet~] object twice with the same seed to repeat the output., f 57;

The -ch flag or message sets the number of output channels. This is only meaningful if you have a single channel input or a float input., f 42;

If you have a multichannel connection in the frequency input, [velvet~] generates a signal with the same number of channels and the 'ch' message or flag is meaningless. The multichannel input is the frequency for each output., f 48;

For multichannel output, if the secondary inlets have a signal with a single channel for bias and regularity, the single value is applied to all channels. If a secondary inlet is also a multichhanel signal, then each channel gets its sync or phase deviation value. Note, however, that the number of multichannels in secondary inlets need to match the same number of output channels., f 78;

The polarity bias controls the chance that the impulse is positive or negative. The default value is 0.5, which means that both have equal (50-50) chance. For a bias of '0', only positive impulses appear, while you have only negative at a bias of '1'.;

A time regularity reduces the time randomness and centers it to the beggining of the period. At full regularity (1) the impulse becomes fully steady at the beggining of the period.;

For instance, a bias of 0 and regularity of 1, the velvet noise becomes the same as [impulse~]., f 60;

An amplitude irregularity parameter forces random impulse values towards lower values., f 60;

Values up to the sample rate are possible, which outputs non zero values for all samples. Note that at the sample rate and without time regularity, the object becomes a clipped white noise, like you get with [white~ -clip]. On the other hand, with full amplitude irregularity, it becomes pure white noise.;

[velvet~] is a velvet noise generator, which randomly chooses either positive (1) or negative (-1) impulses at random positions in a given period set in Hz. A polarity bias is possible to set the amount of positive and negative impulses. A time regularity parameter forces a impulses with less randomness. An amplitude irregularity forces random values (different than 1 or -1). The object has support for multichannel., f 77;


## `vibrato~`

[vibrato~] is a pitch shifter abstraction with an LFO controlling the pitch deviation in cents., f 54;


## `vocoder~`

[vocoder~] is classic cross synthesis channel vocoder abstraction., f 67;

list of frequency in MIDI for each channel (default: equally dividing the range in MIDI from 28 and 108 for the number of channels);


## `voices`

[voices] has 3 different retrigger modes, which are ways of handling repeated note on messages. In this context, a repeated note on is a note that hasn't had a note off message to free its voice allocation. The modes are:, f 56;

don't retrigger and send repeated notes ons to "extra" outlet, f 48;

In retrigger mode 2, repeated notes go to the extra outlet. Here we have [suspedal] in retrig mode 3 again, which sends note off for all repeated note ons when the sustain is switched off.;

Below we emulate a repeated Note On with [pipe] and we have a release time of 250 ms. The repeated note goes to the extra outlet., f 50;

Below we emulate a repeated Note On with [pipe] and we have a release time of 250 ms. The repeated note goes to another voice allocation number., f 50;

In retrigger mode 0 (default), a repeated note goes to another voice allocation number. Here we have [suspedal] in retrigger mode 3, which sends Note Off messages for all given Note Ons. You can see that "extra" Note Off messages go to the "extra" outlet., f 45;

Here we use [suspedal] in mode "1", which does not send a Note Off message and produces repeated Note On messages. It then outputs a single note off message when turned off., f 62;

Below we emulate a repeated Note On with [pipe] and we have a release time of 250 ms. The repeated note comes before the release time is finished and goes to the same voice allocation number., f 44;

In retrigger mode 1, [voices] sends repeated note on messages to the same voice number. One case possible is when you have a Note Off message with a release time. This can also happen without a Note Off message and in this case no Note Off is given prior to the repeated Note On., f 62;

You can set a release time to prevent a note off from freeing a voice allocation. This keeps it allocated for that period of time after a note off is sent., f 65;

This is useful if you want to wait for a release envelope to finish before using that voice allocation for a new note. Set the release time in ms with the '-rel' flag, 'rel' message or right inlet., f 65;

-retrig <float>: sets retrigger mode <0, 1 or 2> (default 0), f 66;

The list input expects at least two elements, which would be "note" and "velocity", and you can have more elements. Note that the first element does not need to be a float. This works well for regular MIDI note messages as given by [keyboard] or more complex Note On and Note Off messages as possible with [makenote2] (check its help file).;

anything - other custom messages to route to active voices, f 62;

Other ("anything") messages are treated as custom messages and are sent out according to the voice allocation. Say for instance you want to send poliphonic aftertouch to an active voice. See an example below for that where we have a MIDI Note message (pitch 60) activating voice number 0, then you can click on the message to the right to generate a polyphonic message for the same pitch., f 64;

A message like this will be routed to the same voice allocation if the first element in the list after the selector corresponds to an allocated pitch (float or symbol)., f 64;

[voices] does voice allocation for polyphonic synths similarly to Vanilla's [poly], but with more functionalities. It outputs the voice information as a list with at least: voice index, pitch and velocity. The rightmost outlet sends messages for the extra voices., f 75;

According to the voice index (the first element in the list sent by [voices]), the MIDI note messages are routed to different instances of "voice.pd"., f 43;

check clone's help file and click on in to open the patch., f 43;

Here [voices] feeds [clone], which loads 4 instances of a patch named "voice.pd"., f 43;

After a voice is allocated, the object needs to receive a corresponding note-off message so that the voice can be used again., f 51;

[voices] is quite useful with [clone] to implement polyphonic synths., f 31;

You can set the object to "voice stealing" mode with the second argument or the "steal" message/flag. This mode forces a note off message (pitch and a velocity of 0) on the first allocated voice so the extra incoming voice "steals" it (just like [poly])., f 63;

[voices] outputs a list with voice index, pitch, velocity and optional extra stuff. You can set the number of voices with the first argument or '-n' flag, and you can change the number of voices with the "n" message, which causes the object to flush and clear its memory. The index offset is 0 by default and you can set a different one with the "offset" message or flag., f 51;


## `voices~`

[voices~] is an abstraction based on [voices] and generates multichannel signals that can be used to control pitch and gate with polyphony., f 66;


## `vsaw~`

A width of 0 or 1 makes it a sawtooth like waveform, while between 0 and 1 makes it triangular variants., f 53;

For a width parameter of 1, the waveform is of an inverted sawtooth., f 49;

The waveform can change/vary to different waveforms according to the width parameter.;

For a parameter of "0.5", the waveform is similar to [triangular~], (see "\$0-default-triangle" above in the middle). Note that they have a phase difference of 0.25 between each other.;

The start and end of the cycle is always an amplitude value of "-1" for all waveforms, except when the width parameter is = 0, which is the default and when the waveform is the same of [saw~], (see "\$0-saw1" above on the left)., f 54;

-midi: sets frequency input in MIDI pitch (default hertz), f 58;

-mc <list>: sets multichannel output with a list of frequencies, f 63;

Syncing the phase with control messages is useful for LFOs and control with MIDI. A sync with audio is useful for the "hard sync" technique, where an oscillator is synced according to the frequency of a master frequency., f 56;

The "phase sync" inlet is quite different from the "phase offset" inlet. They are completely independent!, f 43;

Soft sync is also possible with the '-soft' flag or the "soft" message, where it alternates between positive and negative frequencies and sounds less harsh.;

Additionally, you can reset the oscillator with an impulse signal. Inputs that are > 0 and <= 1 reset the phase Pd expects an impulse signal for syncing. The impulse values need to be > 0 and <= 1 (otherwise ignored). Because phase is cyclical, the value of 1 represents the "phase 0" of the cycle, where the impulse occurs. Send it impulses above and check the result. Use a multiplier to reset to another phase value.;

The third inlet resets the phase ands behaves in the same way for control data as objects like [osc~] and [phasor~] in Pd. A number input resets the oscillator and restarts the cycle with an initial phase that corresponds to the input number, so the internal phase is synced to the given value. The phase values are from 0 to 1 and values beyond that are wrapped within this range. The control message reset is meaningful for LFOs.;

The phase values are wrapped into the 0-1 range, since the phase cycle is from 0 to 1 (where 1 is also the start of another cycle)., f 45;

The third argument sets an initial phase (or "phase offset"). This is also settable with the rightmost inlet. This allows you to control two oscillators with the same frequency falling in and out of phase. Another feature is phase modulation., f 53;

By default, frequency input is in hertz, but if you use the 'midi' message or '-midi' flag you can change it to MIDI pitch input, where it is bound to the 0 to 127 range (but they don't have to be integers) - this is kinda like using [mtof~]...;

If the oscillator has a multichannel left input, it outputs the same number of channels. If the secondary inlets have a signal with a single channel for sync and phase modulation, the single value is applied to all channels. If a secondary inlet is also a multichhanel signal, then each channel gets its sync or phase deviation value. Note, however, that the number of multichannels in secondary inlets need to match the same number of channels from the left input., f 76;

You can initialize the object with multichannel if you give it a list of frequencies with the -mc flag (you can't set phases though). A list input also works if no signal is connected to set it to multichannel with a list of frequency input., f 49;

[vsaw~] is a variable sawtooth waveform oscillator that also becomes a triangular osccilator. It accepts negative frequencies, has inlets for width, phase sync and phase modulation. It also has support for multichannels., f 71;


## `vu~`


## `wavetable~`

The "phase sync" inlet is quite different from the "phase offset" inlet. This means that the are completely independent., f 43;

The second inlet resets the phase ands behaves in the same way for control data as objects like [osc~] and [tabosc4~] in Pd. A number input resets the oscillator and restarts the cycle with an initial phase that corresponds to the input number, so the internal phase is synced to the given value. The phase values are from 0 to 1 and values beyond that are wrapped within this range.;

Additionally, you can reset the oscillator with an impulse signal. The impulse values need to be > 0 and <= 1 (otherwise ignored). Because phase is cyclical, the value of 1 represents the "phase 0" of the cycle, where the impulse occurs., f 62;

Syncing the phase with control messages is useful for LFOs and control with MIDI. A sync with audio is useful for the "hard sync" technique, where an oscillator (called slave) is synced according to the frequency of a master oscillator, f 58;

Soft sync is also possible with the '-soft' flag or the "soft" message, where it alternates between positive and negative frequencies and sounds less harsh., f 58;

The phase values are wrapped into the 0-1 range, since the phase cycle is from 0 to 1 (where 1 is also the start of another cycle).;

The second float argument sets an initial phase (or "phase offset"). This is also settable with the third inlet. This allows you to control two oscillators with the same frequency falling in and out of phase. Another feature is phase modulation., f 61;

By default, [wavetebale~] uses the spline interpolation method but you can set it to linear, cosine, lagrange or no interpolation at all. For more details, check the subsection 'interpolation' of chapter 28 (buffer) in the live electronics tutorial., f 34;

-none/-lin/-cos/-lagrange: set interpolation mode (default spline), f 67;

-midi: sets frequency input in MIDI pitch (default hertz), f 67;

By default, frequency input is in hertz, but if you use the 'midi' message or '-midi' flag you can change it to MIDI pitch input, where it is not really bound to the 0 to 127 range, neither it has to be integers. This is just like using [mtof~].;

The [wavetable~] object needs an array name in Pd to load the wavetable. You can also use [sample~] to load a wavefile into an array as this one used in this example and in the parent patch. The array name is the first argument.;

Besides the first argument, the "set" message followed by an array name sets an entire array to be used as a waveform. If no name is given or if you send a name that doesn't correspond to an exist array, then the output is silent. Below we use [tabgen] to generate a wavetable. You can get more wavetable files -->, f 76;

With the '-n' flag or 'n' message you can set a number of slices to split the wavetable into. This way you can have multilple waveforms in a single array/file., f 81;

The rightmost inlet scans through the different frames applying a linear crossfad between two adjacent frames. The range is from 0 to 1 and in this example it means that 0 is the first frame and going to 0.25 crossfades to the second frame., f 81;

table <symbol> - sets an entire array to be used as a waveform, f 64;

-mc <list>: sets multichannel output with a list of frequencies, f 67;

If the oscillator has a multichannel left input, it outputs the same number of channels. If the secondary inlets have a signal with a single channel for sync and phase modulation, the single value is applied to all channels. If a secondary inlet is also a multichhanel signal, then each channel gets its sync or phase deviation value. Note, however, that the number of multichannels in secondary inlets need to match the same number of channels from the left input., f 76;

You can initialize the object with multichannel if you give it a list of frequencies with the -mc flag (you can't set phases though). A list input also works if no signal is connected to set it to multichannel with a list of frequency input., f 49;

[wavetable~] is an interpolating wavetable oscillator like [tabosc4~], but has more features like more interpolation options, inlets for phase sync, phase modulation and also an inlet for scanning through slices. It also has support for multichannels., f 74;


## `white~`

seed <float> - a float sets seed, no float sets a unique internal, f 65;

In clipped mode, the output is cliped to values that are either -1 or 1 (aka "clip noise"). This produces the maximum energy and peak to peak amplitude. Set it to clip mode with the '-clip' flag or "clip" message., f 53;

Pseudo random number generators aren't true random number generators. Instead, an algorithm is used to provide a sequence of numbers that seems random. The same sequence can be reproduced if you set a "seed" value, which can be any integer number., f 52;

You can set a seed with the '-seed' flag. If you don't supply it, each object gets its own seed internal seed. If you send a 'seed' message without float, the object also gets a unique seed value., f 52;

Seeds are kept locally, which means that if two [white~] objects are seeded the same they will have the same output. Conversely, you can seed the same [white~] object twice with the same seed to repeat the output., f 52;

The -ch flag or message sets the number of output channels. You can also use the '-mc' flag., f 33;

[white~] is a white noise generator from a pseudo random number generator algorithm. It has support for multuchannels., f 64;


## `wrap2`

floats set wrap2's range, 2 floats sets minimum and maximum. No arguments loads default values (0 and 1). 1 float sets maximum value (and lowest value is set to 0). If the maximum value is less than the minimum, the maximum becomes the minimum and vice-versa.;


## `wrap2~`

floats set wrap's range, 2 floats sets minimum and maximum. No arguments loads default values (-1 and 1). 1 float sets maximum value (and lowest value is set to 0). If the maximum value is less than the minimum, the maximum becomes the minimum and vice-versa.;

If the object has a multichannel left input, it outputs the same number of channels. If the secondary inlets have a signal with a single channel, the single value is applied to all channels. If a secondary inlet is also a multichhanel signal, then each channel gets its min or max value. Note, however, that the number of multichannels in secondary inlets need to match the same number of channels from the left input., f 76;

[wrap2~] wraps between a low and high value. It has multichannel support.;


## `wt2d~`

The "phase sync" inlet is quite different from the "phase offset" inlet. This means that the are completely independent., f 43;

The second inlet resets the phase ands behaves in the same way for control data as objects like [osc~] and [tabosc4~] in Pd. A number input resets the oscillator and restarts the cycle with an initial phase that corresponds to the input number, so the internal phase is synced to the given value. The phase values are from 0 to 1 and values beyond that are wrapped within this range.;

Additionally, you can reset the oscillator with an impulse signal. The impulse values need to be > 0 and <= 1 (otherwise ignored). Because phase is cyclical, the value of 1 represents the "phase 0" of the cycle, where the impulse occurs., f 62;

Syncing the phase with control messages is useful for LFOs and control with MIDI. A sync with audio is useful for the "hard sync" technique, where an oscillator (called slave) is synced according to the frequency of a master oscillator, f 58;

Soft sync is also possible with the '-soft' flag or the "soft" message, where it alternates between positive and negative frequencies and sounds less harsh., f 58;

The phase values are wrapped into the 0-1 range, since the phase cycle is from 0 to 1 (where 1 is also the start of another cycle).;

The second float argument sets an initial phase (or "phase offset"). This is also settable with the third inlet. This allows you to control two oscillators with the same frequency falling in and out of phase. Another feature is phase modulation., f 61;

By default, [wt2d~] uses the spline interpolation method but you can set it to linear, cosine, lagrange or no interpolation at all. For more details, check the subsection 'interpolation' of chapter 28 (buffer) in the live electronics tutorial., f 39;

-none/-lin/-cos/-lagrange: set interpolation mode (default spline), f 67;

-midi: sets frequency input in MIDI pitch (default hertz), f 67;

By default, frequency input is in hertz, but if you use the 'midi' message or '-midi' flag you can change it to MIDI pitch input, where it is not really bound to the 0 to 127 range, neither it has to be integers. This is just like using [mtof~].;

The [wt2d~] object needs an array name in Pd to load the wavetable. You can also use [sample~] to load a wavefile into an array as this one used in this example and in the parent patch. The array name is the first argument.;

Besides the first argument, the "set" message followed by an array name sets an entire array to be used as a waveform. If no name is given or if you send a name that doesn't correspond to an exist array, then the output is silent. Below we use [tabgen] to generate a wavetable. You can get more wavetable files -->, f 76;

-n <list>: sets number of x and y slices (default 1, 1), f 67;

With the '-n' flag or 'n' message you can set a number of slices to split the wavetable into. You need to give it 2 values, the first is for the number of horizontal slices (or 'columns') and the second is for the number of vertical slices (or 'rows'). The total number of slices is the number of columns times the number of rows. In this example we initialize the object with 2 columns and 2 rows, slicing it in 4 frames., f 64;

you can scan through the frames with the 4th and 5th inlet, both input are from 0 to 1 and crossfade, respectively, with through the number of columns and rows. Using a 2D slider can be fun here., f 64;

Note that if you set 'n' values to '4 1' you only get a horizontal scan, and it'd be just like [wavetable~]., f 66;

n <f, f> - sets number of x and y slices to scan through, f 58;

table <symbol> - sets an entire array to be used as a waveform, f 62;

-mc <list>: sets multichannel output with a list of frequencies, f 67;

If the oscillator has a multichannel left input, it outputs the same number of channels. If the secondary inlets have a signal with a single channel for sync and phase modulation, the single value is applied to all channels. If a secondary inlet is also a multichhanel signal, then each channel gets its sync or phase deviation value. Note, however, that the number of multichannels in secondary inlets need to match the same number of channels from the left input., f 76;

You can initialize the object with multichannel if you give it a list of frequencies with the -mc flag (you can't set phases though). A list input also works if no signal is connected to set it to multichannel with a list of frequency input., f 49;

[wt2d~] is an interpolating wavetable oscillator like [wt~], but besides a horizontal dimension, it can also scan through a vertical dimension of a sliced wavetable. As other oscilltors in ELSE, it has input for phase modulation and sync. It also has support for multichannels., f 74;


## `xfade.mc~`

[xfade.mc~] crossfades between two multichannel sources. By default, it performs equal power crossfade, but can also do linear.;


## `xfade~`

1) float - number of 'n' channels for each source (default 1), f 61;

[xfade~] crossfades between two sources (that can have 1 to 64 channels each). By default, it performs equal power crossfade, but can also do linear., f 63;


## `xgate.mc~`

[xgate.mc~] routes to a channel output in a multichannel connection.;

The object can also take multichannel inputs. In this case, the total output channels are actually the number of outputs set by the argument times the number of input channels, which actually become the number of grouped channels. Then, the channel selection routes to the given group., f 73;

Hint: you can use [unmerge~] to route a multichannel input to a separate outlet if you need it. See below., f 29;


## `xgate2.mc~`

An example on how to change the route output channel without crossfading at signal rate., f 37;

The Sine/Cosine function is used for crossfading and the default spread value of 1 means the usual equal power crossfade between 2 adjacent channels, where the mid point between the 2 channels means both have the same amplitude at square root of 0.5 (0.707107)., f 71;

Spread values greater than 1 spreads the signal to more than 2 adjacent channels. A spread value of two will spread the input to the 2 adjacent channels (to the right and to the left) with an amplidute of the square root of 0.5! Values smaller than 1 narrows the crossfading point closer to the selected channel. A value of 0.5 provides no actual crossfading, meaning that 2 adjacent channels get muted at the mid point. Values smaller than 0.5 are possible and it narrows down even more at the channel center., f 71;

note you can also use signals to set the spread parameter., f 21;

At indexed mode the output channel selection is by channel number (not normalized from 0 to 1), where channels are indexes by 0 to 'n - 1'. Values above or below fade out to silence (same is true for non indexed mode).;

1) float - number of output channels (default/min 2, max 512), f 69;

[xgate2.mc~] routes an input signal to 'n' specified channels in a multichannel output with crossfading between adjacent channels according to a spread parameter., f 73;


## `xgate2~`

An example on how to change the route output channel without crossfading at signal rate., f 37;

The Sine/Cosine function is used for crossfading and the default spread value of 1 means the usual equal power crossfade between 2 adjacent channels, where the mid point between the 2 channels means both have the same amplitude at square root of 0.5 (0.707107)., f 71;

Spread values greater than 1 spreads the signal to more than 2 adjacent channels. A spread value of two will spread the input to the 2 adjacent channels (to the right and to the left) with an amplidute of the square root of 0.5! Values smaller than 1 narrows the crossfading point closer to the selected channel. A value of 0.5 provides no actual crossfading, meaning that 2 adjacent channels get muted at the mid point. Values smaller than 0.5 are possible and it narrows down even more at the channel center., f 71;

note you can also use signals to set the spread parameter., f 21;

At indexed mode the output channel selection is by channel number (not normalized from 0 to 1), where channels are indexes by 0 to 'n - 1'. Values above or below fade out to silence (same is true for non indexed mode).;

1) float - number of output channels (default/min 2, max 512), f 69;

[xgate2~] routes an input signal to 'n' specified outlets with crossfading between adjacent channels according to a spread parameter., f 62;


## `xgate~`

You can use the off status report from the right outlet to turn a subpatch off. But in order to turn it on you need to use the float input. Open the subpatches below to see how this works., f 43;

[xgate~] routes between multiple outputs with equal power crossfading. It has support for multichannel signals.;

For a version that outputs a single multichannel connection, see:, f 37;


## `xmod2~`

[xmod2~] performs is a variant of [xmod~], but only performs frequency modulation (so far) and uses a different and cheap sine waveform that promotes more chaotic and cool sounds., f 63;


## `xmod~`

You can find the details on how [xmod~] is implemented in with the subpatches below, compare., f 32;

-pm: sets to phase modulation (default is frequency modulation), f 63;

[xmod~] performs cross modulation of two sine oscillators. It can perform either frequency (default) or phase modulation., f 61;


## `xselect.mc~`

[xselect.mc~] selects between multiple channels from a multichannel connection (maximum 512 channels) with equal power crossfading., f 67;

Hint: you an use [merge~] to generate a multisignal input from different multichannel sources., f 37;

The '-n' flag or 'n' message can be used to set the number of output channels. This also sets the input channel numbers into groups of the same size., f 35;


## `xselect2.mc~`

At indexed mode the output channel selection is by channel number (not normalized from 0 to 1), where channels are indexes by 0 to 'n - 1'. Values outside this range are possible but fade out to silence (same is true for non indexed mode)., f 59;

In circular mode, the selection input from 0 to 1 is circular, meaning that 1 goes back to 0! If in indexed mode as well, values are from 0 to 'n', where 'n' goes back to 0! Values outside the range wrap around. Note how this mode makes this object the 'inverse' of [pan.mc~]., f 62;

An example on how to change the input channel at signal rate., f 32;

The Sine/Cosine function is used for crossfading and the default spread value of 1 means the usual equal power crossfade between 2 adjacent channels, where the mid point between the 2 channels means both have the same amplitude at square root of 0.5 (0.707107)., f 71;

Spread values greater than 1 spreads the signal to more than 2 adjacent channels. A spread value of two will spread the input to the 2 adjacent channels (to the right and to the left) with an amplidute of the square root of 0.5! Values smaller than 1 narrows the crossfading point closer to the selected channel. A value of 0.5 provides no actual crossfading, meaning that 2 adjacent channels get muted at the mid point. Values smaller than 0.5 are possible and it narrows down even more at the channel center., f 71;

note you can also use signals to set the spread parameter., f 21;

[xselect2.mc~] selects from 'n' inputs with crossfading between adjacent channels according to a spread parameter., f 72;


## `xselect2~`

At indexed mode the output channel selection is by channel number (not normalized from 0 to 1), where channels are indexes by 0 to 'n - 1'. Values outside this range are possible but fade out to silence (same is true for non indexed mode).;

In circular mode, the selection input from 0 to 1 is circular, meaning that 1 goes back to 0! If in indexed mode as well, values are from 0 to 'n', where 'n' goes back to 0! Values outside the range wrap around. Note how this mode makes this object the 'inverse' of [pan~]., f 62;

An example on how to change the input channel at signal rate., f 32;

1) float - number of output channels (default/min 2, max 512), f 69;

The Sine/Cosine function is used for crossfading and the default spread value of 1 means the usual equal power crossfade between 2 adjacent channels, where the mid point between the 2 channels means both have the same amplitude at square root of 0.5 (0.707107)., f 71;

Spread values greater than 1 spreads the signal to more than 2 adjacent channels. A spread value of two will spread the input to the 2 adjacent channels (to the right and to the left) with an amplidute of the square root of 0.5! Values smaller than 1 narrows the crossfading point closer to the selected channel. A value of 0.5 provides no actual crossfading, meaning that 2 adjacent channels get muted at the mid point. Values smaller than 0.5 are possible and it narrows down even more at the channel center., f 71;

note you can also use signals to set the spread parameter., f 21;

[xselect2~] selects from 'n' inputs with crossfading between adjacent channels according to a spread parameter., f 61;


## `xselect~`

[xselect~] selects between multiple inputs with equal power crossfading.;

You can use the off status report from the right outlet to turn a subpatch off. But in order to turn it on you need to use the float input. Open the subpatches below to see how this works., f 43;


## `zbiplot`


## `zerocross~`


