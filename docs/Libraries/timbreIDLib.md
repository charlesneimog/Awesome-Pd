# timbreIDLib

## `attackTime`

Read from a different array;

Specify your sample's sampling rate. (default: 44100)

Print the internal settings to the post window;

Specify the sample magnitude threshold that the signal

Specify the number of consecutive samples for which

Specify the maximum time in milliseconds before the

Creation argument is the name of the sample array to

Updated for timbreIDLib version 0.7;

July 2017;

See the real-time version for more information on attack

Outlet 1: attack time in milliseconds;

Outlet 2: attack onset starting sample index;

Outlet 3: attack onset peak sample index;

Analyze a window starting at sample 27264 that is 2000


## `attackTime~`

Inside a subpatch with re-blocking involving overlap

Specify the sample magnitude threshold that the signal

Print the internal settings to the post window;

Specify the number of consecutive samples for which

Here, the mag thresh is set to zero since the default

Specify the maximum time in milliseconds before the

Change analysis window size.;

This feature can be sent to the timbreID external in

When an onset is found, bang to output attack time

Outlet 1: attack time in milliseconds;

Outlet 2: attack onset starting sample index;

Outlet 3: attack onset peak sample index;

This uses [sampleBuffer~] to grab the same audio contained

Look inside [pd other-settings] for more information

Creation argument sets analysis window size in samples

[attackTime~] does not contain an onset detector,

Audio buffering is taken care of by the external,

Updated for timbreIDLib version 0.9.0;

June 2022;

When [attackTime~] receives a bang, it locates the


## `autoCorrPitch`

Bang to analyze the entire array.;

Read from a different array;

Specify your sample's sampling rate. (default: 44100)

Print current settings in the post window;

Set threshold for detecting correlation peak in percent

Move through the soundfile with the slider above,

Output value is pitch in MIDI units;

Updated for timbreIDLib version 0.9;

June 2022;

See the real-time version for more information on autocorrelation

Analyze a window starting at sample 24100 that is 2000

Creation argument is the name of the sample array to


## `autoCorrPitch~`

Print current settings in the post window;

Inside a subpatch with re-blocking involving overlap

Set threshold for detecting correlation peak in percent

Change analysis window size;

Bang repeatedly to keep refreshing..., f 21;

Bang to output pitch;

This feature can be sent to the timbreID external in

Updated for timbreIDLib version 0.9;

June 2022;

Creation argument is window size in samples., f 45

autoCorrPitch~ works by calculating the autocorrelation

Autocorrelation is a time-domain calculation. In order

Audio buffering is taken care of by the external,


## `bark`

Apply a loudness weighting curve to the Bark spectrum

With debug on, growth values will be posted for every

Print current settings in the post window.;

If your file uses a sample rate other than the default

Spew growth data on every frame.;

There is no "measure" function for the NRT version

Change windowing function. Rectangular (0), Blackman

Normalize spectrum (default: OFF);

Use power vs. magnitude spectrum (default: power).;

Block onset reports for a given number of milliseconds

If using the triangular Bark spaced filters, you

Rather than sum energy in the triangular Bark spaced

Ignore onsets that are below a certain amplitude threshold.

As with bonk~, the thresh message lets you specify

As with bonk~, you can specify a number of analysis

The spectral flux that goes on during the first few milliseconds

See the real-time version too:;

Creation arguments are the array to analyze, window

Use the "filter_range" message to specify a range of

Updated for timbreIDLib version 0.7;

bark is a non-real-time onset detector that makes use

Outlet 2: total energy growth;

Outlet 3: growth list per Bark band;

Outlet 1: onset location (seconds);

write to a text file and import as labels in Audacity

convert from seconds to samples before writing to attacks

Make the attacks table bigger as more attacks are found

Analyze the whole array, or a range given in seconds.

Turn on spew mode;

then analyze a time range that is relatively silent.

You can see from the results that this portion of the

July 2017;


## `barkSpec`

Bang to analyze the entire array.;

Creation arguments are the name of the sample array

Read from a different array;

Construct a new filterbank with a specific spacing.

Normalize spectrum (default: ON);

Specify your sample's sampling rate. (default: 44100)

Use power spectrum. (default: magnitude);

Change windowing function. Rectangular (0), Blackman

Print current settings in the post window;

If using the triangular Bark spaced filters, you

Rather than sum energy in the triangular Bark spaced

Change internal window size setting;

See the real-time version for more information on Bark

Move through the soundfile with the slider above;

Analyze a window starting at sample 44100 that is 2000

Updated for timbreIDLib version 0.7.6;

August 2018;

Prepend the "chain_fftData" message in front of the

[tID_fft~] outputs (N/2)+1 real values from the left

fftData <data> should consist of (window/2)+1 real

magSpec <data> should consist of (window/2)+1 magnitudes

The object in this help file accepts the chain_ messages

To minimize redundant calculations on the same window


## `barkSpecBrightness`

Bang to analyze the entire array.;

Read from a different array;

Specify your sample's sampling rate. (default: 44100)

Use power spectrum. (default: magnitude);

Rather than sum energy in the triangular Bark spaced

Print current settings in the post window;

Change windowing function. Rectangular (0), Blackman

Construct a new filterbank with a specific spacing.

If using the triangular Bark spaced filters, you

Change internal window size setting;

Analyze a window starting at sample 44100 that is 2000

Change the boundary point in Barks;

See the real-time version for more information on Bark

Creation arguments are the name of the sample array

Updated for timbreIDLib version 0.7.6;

August 2018;

Prepend the "chain_fftData" message in front of the

[tID_fft~] outputs (N/2)+1 real values from the left

fftData <data> should consist of (window/2)+1 real

magSpec <data> should consist of (window/2)+1 magnitudes

The object in this help file accepts the chain_ messages

To minimize redundant calculations on the same window

barkSpec <data> should consist of 50 Bark spectrum


## `barkSpecBrightness~`

Change window size.;

Bang to output brightness.;

Use power spectrum. (default: magnitude);

Print current settings in the post window;

Change windowing function. Rectangular (0), Blackman

Construct a new filterbank with a specific spacing.

Inside a subpatch with re-blocking involving overlap

If using the triangular Bark spaced filters, you

Rather than sum energy in the triangular Bark spaced

Set boundary point in Barks;

Updated for timbreIDLib version 0.7;

Creation arguments are window size in samples, filterbank

Bark Spectrum Brightness is the ratio of the sum of

Audio buffering and windowing are taken care of by

This feature can be sent to the timbreID external in

July 2017;


## `barkSpecCentroid`

Bang to analyze the entire array.;

Read from a different array;

Specify your sample's sampling rate. (default: 44100)

Use power spectrum. (default: magnitude);

Print current settings in the post window;

Change windowing function. Rectangular (0), Blackman

If using the triangular Bark spaced filters, you

Rather than sum energy in the triangular Bark spaced

Construct a new filterbank with a specific spacing.

Change internal window size setting;

See the real-time version for more information on Bark

Creation arguments are the name of the sample array

Analyze a window starting at sample 44100 that is 2000

Updated for timbreIDLib version 0.7.6;

August 2018;

Prepend the "chain_fftData" message in front of the

[tID_fft~] outputs (N/2)+1 real values from the left

fftData <data> should consist of (window/2)+1 real

magSpec <data> should consist of (window/2)+1 magnitudes

The object in this help file accepts the chain_ messages

To minimize redundant calculations on the same window

barkSpec <data> should consist of 50 Bark spectrum


## `barkSpecCentroid~`

Bang repeatedly...;

Construct a new filterbank with a specific spacing.

Use power spectrum. (default: magnitude);

Change windowing function. Rectangular (0), Blackman

Print current settings in the post window;

If using the triangular Bark spaced filters, you

Rather than sum energy in the triangular Bark spaced

Inside a subpatch with re-blocking involving overlap

Bang to output centroid;

Change analysis window size;

Creation arguments are window size in samples, and

Updated for timbreIDLib version 0.7;

This feature can be sent to the timbreID external in

Audio buffering and windowing are taken care of by

July 2017;

Bark spectrum centroid is the center of mass of the


## `barkSpecFlatness`

Bang to analyze the entire array.;

Read from a different array;

Specify your sample's sampling rate. (default: 44100)

Use power spectrum. (default: magnitude);

Print current settings in the post window;

Change windowing function. Rectangular (0), Blackman

If using the triangular Bark spaced filters, you

Rather than sum energy in the triangular Bark spaced

Construct a new filterbank with a specific spacing.

Change internal window size setting;

Creation arguments are the name of the sample array

See the real-time version for more information on Bark

Analyze a window starting at sample 44100 that is 2000

Updated for timbreIDLib version 0.7.6;

August 2018;

Prepend the "chain_fftData" message in front of the

[tID_fft~] outputs (N/2)+1 real values from the left

fftData <data> should consist of (window/2)+1 real

magSpec <data> should consist of (window/2)+1 magnitudes

The object in this help file accepts the chain_ messages

To minimize redundant calculations on the same window

barkSpec <data> should consist of 50 Bark spectrum


## `barkSpecFlatness~`

Use power spectrum. (default: magnitude);

Print current settings in the post window;

Change windowing function. Rectangular (0), Blackman

If using the triangular Bark spaced filters, you

Rather than sum energy in the triangular Bark spaced

Construct a new filterbank with a specific spacing.

Updated for timbreIDLib version 0.7;

This feature can be sent to the timbreID external in

Audio buffering and windowing are taken care of by

Activate a signal;

Creation arguments are window size in samples and filterbank

Bark spectrum flatness is the ratio of the geometric

bang to output flatness;

Change window size;

July 2017;


## `barkSpecFlux`

Read from a different array;

Specify your sample's sampling rate. (default: 44100)

Use power spectrum. (default: magnitude);

Squared difference vs. Absolute value of difference.

Change windowing function. Rectangular (0), Blackman

Construct a new filterbank with a specific spacing.

Print current settings in the post window;

If using the triangular Bark spaced filters, you

Rather than sum energy in the triangular Bark spaced

Set separation in samples between analysis windows

Change internal window size setting;

Normalize spectrum. (default: OFF);

Use the natural logarithm of spectrum values. (default:

See the real-time version for more information on Bark

Creation arguments are the name of the sample array

Analyze a FORWARD window starting at sample 44100 that

Prepend the "chain_fftData" message in front of the

[tID_fft~] outputs (N/2)+1 real values from the left

The object in this help file accepts the chain_ messages

To minimize redundant calculations on the same window

Spectral flux is a special case, because measurements

fftData <data> should consist of (window/2)+1 real

magSpec <data> should consist of (window/2)+1 magnitudes

at the default Bark filterbank spacing of 0.5, barkSpec

Change modes to report flux, spectral growth only

Updated for timbreIDLib version 0.9.0;

June 2022;


## `barkSpecFlux~`

Activate a signal above and bang to output its flux.

Creation arguments are window size, filterbank spacing

In the [attack-detection] sub-patch, the left outlet

This feature can be sent to the timbreID external in

Audio buffering and windowing are taken care of by

Squared difference vs absolute value of difference

Change distance between analysis windows in samples

Construct a new filterbank with a specific spacing.

Use power spectrum. (default: magnitude);

Rather than sum energy in the triangular Bark spaced

If using the triangular Bark spaced filters, you

Print current settings in the post window;

Change windowing function. Rectangular (0), Blackman

Inside a subpatch with re-blocking involving overlap

Change window size;

Normalize spectrum (default: OFF);

Use the natural logarithm of spectrum values. (default:

barkSpecFlux~ reports the full list of per-Bark-band

Typically, spectral flux is the sum of squared differences

Change modes to report flux, spectral growth only

June 2022;

Updated for timbreIDLib version 0.9.0;

Turn on for continuous analysis;

For these purposes, we'll turn on "growth" mode so

Bark spectrum flux can be used for basic attack detection.

If 100 is too low or high, try a different threshhold.


## `barkSpecIrregularity`

Bang to analyze the entire array.;

Read from a different array;

Specify your sample's sampling rate. (default: 44100)

Use power spectrum. (default: magnitude);

Rather than sum energy in the triangular Bark spaced

If using the triangular Bark spaced filters, you

Print current settings in the post window;

Change windowing function. Rectangular (0), Blackman

Construct a new filterbank with a specific spacing.

Change internal window size setting;

Analyze a window starting at sample 44100 that is 2000

Creation arguments are the name of the sample array

See the real-time version for more information on Bark

Change between Jensen (0) and Krimphoff (1) algorithm

Updated for timbreIDLib version 0.7.6;

August 2018;

Prepend the "chain_fftData" message in front of the

[tID_fft~] outputs (N/2)+1 real values from the left

fftData <data> should consist of (window/2)+1 real

magSpec <data> should consist of (window/2)+1 magnitudes

The object in this help file accepts the chain_ messages

To minimize redundant calculations on the same window

barkSpec <data> should consist of 50 Bark spectrum


## `barkSpecIrregularity~`

Use power spectrum. (default: magnitude);

Change window size.;

Turn spectrum normalization on/off. This only matters

Change windowing function. Rectangular (0), Blackman

If using the triangular Bark spaced filters, you

Rather than sum energy in the triangular Bark spaced

Inside a subpatch with re-blocking involving overlap

Construct a new filterbank with a specific spacing.

Choose between Jensen (0) and Krimphoff (1) algorithms

Bang to output irregularity;

Updated for timbreIDLib version 0.7;

Creation arguments are window size in samples, filterbank

This feature can be sent to the timbreID external in

Audio buffering and windowing are taken care of by

July 2017;

Spectral Irregularity has two common definitions: one


## `barkSpecKurtosis`

Bang to analyze the entire array.;

Read from a different array;

Specify your sample's sampling rate. (default: 44100)

Use power spectrum. (default: magnitude);

Print current settings in the post window;

Change windowing function. Rectangular (0), Blackman

If using the triangular Bark spaced filters, you

Rather than sum energy in the triangular Bark spaced

Construct a new filterbank with a specific spacing.

Change internal window size setting;

Creation arguments are the name of the sample array

Analyze a window starting at sample 44100 that is 2000

See the real-time version for more information on Bark

Updated for timbreIDLib version 0.7.6;

August 2018;

Prepend the "chain_fftData" message in front of the

[tID_fft~] outputs (N/2)+1 real values from the left

fftData <data> should consist of (window/2)+1 real

magSpec <data> should consist of (window/2)+1 magnitudes

The object in this help file accepts the chain_ messages

To minimize redundant calculations on the same window

barkSpec <data> should consist of 50 Bark spectrum


## `barkSpecKurtosis~`

Bang repeatedly...;

Construct a new filterbank with a specific spacing.

Use power spectrum. (default: magnitude);

Change windowing function. Rectangular (0), Blackman

Print current settings in the post window;

If using the triangular Bark spaced filters, you

Rather than sum energy in the triangular Bark spaced

Inside a subpatch with re-blocking involving overlap

Change analysis window size;

Creation arguments are window size in samples, and

Updated for timbreIDLib version 0.7;

This feature can be sent to the timbreID external in

Audio buffering and windowing are taken care of by

Bark spectrum kurtosis measures the peakedness of a

Bang to output kurtosis;

July 2017;


## `barkSpecRolloff`

Bang to analyze the entire array.;

Read from a different array;

Specify your sample's sampling rate. (default: 44100)

Use power spectrum. (default: magnitude);

Rather than sum energy in the triangular Bark spaced

If using the triangular Bark spaced filters, you

Print current settings in the post window;

Change windowing function. Rectangular (0), Blackman

Construct a new filterbank with a specific spacing.

Change internal window size setting;

Analyze a window starting at sample 44100 that is 2000

See the real-time version for more information on Bark

Creation arguments are the name of the sample array

Change the concentration threshold (0 - 1.0), f 26

Updated for timbreIDLib version 0.7.6;

August 2018;

Prepend the "chain_fftData" message in front of the

[tID_fft~] outputs (N/2)+1 real values from the left

fftData <data> should consist of (window/2)+1 real

magSpec <data> should consist of (window/2)+1 magnitudes

The object in this help file accepts the chain_ messages

To minimize redundant calculations on the same window

barkSpec <data> should consist of 50 Bark spectrum


## `barkSpecRolloff~`

Change window size.;

Use power spectrum. (default: magnitude);

Print current settings in the post window;

Change windowing function. Rectangular (0), Blackman

Construct a new filterbank with a specific spacing.

Inside a subpatch with re-blocking involving overlap

If using the triangular Bark spaced filters, you

Rather than sum energy in the triangular Bark spaced

Updated for timbreIDLib version 0.7;

This feature can be sent to the timbreID external in

Creation arguments are window size in samples, filterbank

Change the concentration threshold, f 23;

Audio buffering and windowing are taken care of by

Output is the Bark frequency band below which most of

Bark spectrum rolloff is the Bark frequency below which

Bang to output rolloff;

July 2017;


## `barkSpecSkewness`

Bang to analyze the entire array.;

Read from a different array;

Specify your sample's sampling rate. (default: 44100)

Use power spectrum. (default: magnitude);

Print current settings in the post window;

Change windowing function. Rectangular (0), Blackman

If using the triangular Bark spaced filters, you

Rather than sum energy in the triangular Bark spaced

Construct a new filterbank with a specific spacing.

Change internal window size setting;

Creation arguments are the name of the sample array

Analyze a window starting at sample 44100 that is 2000

See the real-time version for more information on Bark

Updated for timbreIDLib version 0.7.6;

August 2018;

Prepend the "chain_fftData" message in front of the

[tID_fft~] outputs (N/2)+1 real values from the left

fftData <data> should consist of (window/2)+1 real

magSpec <data> should consist of (window/2)+1 magnitudes

The object in this help file accepts the chain_ messages

To minimize redundant calculations on the same window

barkSpec <data> should consist of 50 Bark spectrum


## `barkSpecSkewness~`

Bang repeatedly...;

Construct a new filterbank with a specific spacing.

Use power spectrum. (default: magnitude);

Change windowing function. Rectangular (0), Blackman

Print current settings in the post window;

If using the triangular Bark spaced filters, you

Rather than sum energy in the triangular Bark spaced

Inside a subpatch with re-blocking involving overlap

Change analysis window size;

Creation arguments are window size in samples, and

Updated for timbreIDLib version 0.7;

This feature can be sent to the timbreID external in

Audio buffering and windowing are taken care of by

Bang to output skewness;

July 2017;

Bark spectrum skewness measures the symmetry of a Bark


## `barkSpecSlope`

Bang to analyze the entire array.;

Analyze a window starting at sample 44100 that is 2000

Creation arguments are the name of the sample array

See the real-time version for more information on Bark

Read from a different array;

Construct a new filterbank with a specific spacing.

Normalize spectrum (default: ON);

Specify your sample's sampling rate. (default: 44100)

Use power spectrum. (default: magnitude);

Change windowing function. Rectangular (0), Blackman

Print current settings in the post window;

If using the triangular Bark spaced filters, you

Rather than sum energy in the triangular Bark spaced

Change internal window size setting;

Use the slider above to move through the audio file

Updated for timbreIDLib version 0.7.6;

August 2018;

Prepend the "chain_fftData" message in front of the

[tID_fft~] outputs (N/2)+1 real values from the left

fftData <data> should consist of (window/2)+1 real

magSpec <data> should consist of (window/2)+1 magnitudes

The object in this help file accepts the chain_ messages

To minimize redundant calculations on the same window

barkSpec <data> should consist of 50 Bark spectrum


## `barkSpecSlope~`

Change analysis window size;

Bang repeatedly...;

Bang to output slope;

Updated for timbreIDLib version 0.7;

Construct a new filterbank with a specific spacing.

Normalize spectrum (default: ON);

Use power spectrum. (default: magnitude);

Rather than sum energy in the triangular Bark spaced

If using the triangular Bark spaced filters, you

Print current settings in the post window;

Change windowing function. Rectangular (0), Blackman

Inside a subpatch with re-blocking involving overlap

This feature can be sent to the timbreID external in

Audio buffering and windowing are taken care of by

Bark spectrum slope is the slope of the best-fit line

July 2017;


## `barkSpecSpread`

Bang to analyze the entire array.;

Read from a different array;

Specify your sample's sampling rate. (default: 44100)

Use power spectrum. (default: magnitude);

Print current settings in the post window;

Change windowing function. Rectangular (0), Blackman

If using the triangular Bark spaced filters, you

Rather than sum energy in the triangular Bark spaced

Construct a new filterbank with a specific spacing.

Change internal window size setting;

Creation arguments are the name of the sample array

Analyze a window starting at sample 44100 that is 2000

See the real-time version for more information on Bark

Updated for timbreIDLib version 0.7.6;

August 2018;

Prepend the "chain_fftData" message in front of the

[tID_fft~] outputs (N/2)+1 real values from the left

fftData <data> should consist of (window/2)+1 real

magSpec <data> should consist of (window/2)+1 magnitudes

The object in this help file accepts the chain_ messages

To minimize redundant calculations on the same window

barkSpec <data> should consist of 50 Bark spectrum


## `barkSpecSpread~`

Bang repeatedly...;

Construct a new filterbank with a specific spacing.

Use power spectrum. (default: magnitude);

Change windowing function. Rectangular (0), Blackman

Print current settings in the post window;

If using the triangular Bark spaced filters, you

Rather than sum energy in the triangular Bark spaced

Inside a subpatch with re-blocking involving overlap

Change analysis window size;

Creation arguments are window size in samples, and

Updated for timbreIDLib version 0.7;

This feature can be sent to the timbreID external in

Audio buffering and windowing are taken care of by

Bark spectrum spread is a measure of the concentration

Bang to output spread;

July 2017;


## `barkSpec~`

Construct a new filterbank with a specific spacing.

Normalize spectrum (default: ON);

Use power spectrum. (default: magnitude);

Rather than sum energy in the triangular Bark spaced

If using the triangular Bark spaced filters, you

Print current settings in the post window;

Change windowing function. Rectangular (0), Blackman

Inside a subpatch with re-blocking involving overlap

Change analysis window size, f 16;

Creation arguments are window size in samples and filterbank

Bang repeatedly to keep refreshing...;

Bang to output Bark spectrum as a list;

Bark-frequency spectrum is a warping of normal magnitude

Audio buffering and windowing are taken care of by

This feature can be sent to the timbreID external in

Updated for timbreIDLib version 0.7;

July 2017;


## `bark~`

With debug on, growth values will be posted for every

With spew mode on, the list of growth per band and

Change windowing function. Rectangular (0), Blackman

Apply a loudness weighting curve to the Bark spectrum

Block onset reports for a given number of millseconds

Ignore onsets that are below a certain amplitude threshold.

Rather than sum energy in the triangular Bark spaced

If using the triangular Bark spaced filters, you

Turn "measure" on, then off after a few seconds to

Print current settings in the post window.;

Normalize spectrum (default: OFF);

Use power vs. magnitude spectrum (default: power).

If you use bark~ inside a subpatch with re-blocking

As with bonk~, the thresh message lets you specify

See the [pd other-messages-and-settings] subpatch for

As with bonk~, you can specify a number of analysis

The spectral flux that goes on during the first few milliseconds

bark~ is an onset detector that makes use of the perceptually

bark~ also features some convenient functions for the

Use the "filter_range" message to specify a range of

Updated for timbreIDLib version 0.7;

Creation arguments are window size in samples, hop

This array displays the growth in each Bark frequency

Outlet 1: "bang" for an onset;

Outlet 2: total energy growth;

Outlet 3: growth list per Bark band;

July 2017;


## `bfcc`

Bang to analyze the entire array.;

Creation arguments are the name of the sample array

Read from a different array;

Construct a new filterbank with a specific spacing.

Normalize spectrum (default: ON);

Specify your sample's sampling rate. (default: 44100)

Use power spectrum. (default: magnitude);

Change windowing function. Rectangular (0), Blackman

Print current settings in the post window;

If using the triangular Bark spaced filters, you

Rather than sum energy in the triangular Bark spaced

Change internal window size setting;

Move through the soundfile with the slider above,

See the real-time version for more information on Bark-frequency

Analyze a window starting at sample 44100 that is 2000

Updated for timbreIDLib version 0.7.6;

August 2018;

Prepend the "chain_fftData" message in front of the

[tID_fft~] outputs (N/2)+1 real values from the left

fftData <data> should consist of (window/2)+1 real

magSpec <data> should consist of (window/2)+1 magnitudes

The object in this help file accepts the chain_ messages

To minimize redundant calculations on the same window

barkSpec <data> should consist of 50 Bark spectrum


## `bfcc~`

Construct a new filterbank with a specific spacing.

Normalize spectrum (default: ON);

Use power spectrum. (default: magnitude);

Rather than sum energy in the triangular Bark spaced

If using the triangular Bark spaced filters, you

Print current settings in the post window;

Change windowing function. Rectangular (0), Blackman

Inside a subpatch with re-blocking involving overlap

Updated for timbreIDLib version 0.7;

Change analysis window size;

Creation arguments are window size in samples and filterbank

Bang repeatedly to keep refreshing...;

This feature can be sent to the timbreID external in

Bang to output BFCCs as a list;

July 2017;

Bark-frequency cepstrum is much different than raw cepstrum.

Audio buffering and windowing are taken care of by


## `binWrangler`

To clear memory, send the "clear" message. Note that

Also see:;

Creation arguments are the number of frames to expect

[binWrangler] accumulates a database of lists sent

If the optional "spew" mode is activated, featureAccum

Updated for timbreIDLib version 0.7;

After the specified number of frames have been accumulated

July 2017;


## `cepstrum`

Bang to analyze the entire array.;

Read from a different array;

Specify your sample's sampling rate. (default: 44100)

Use power spectrum. (default: magnitude);

Change windowing function. Rectangular (0), Blackman

Print current settings in the post window;

Report power cepstrum (default: magnitude);

Add 1 to the power or magnitude spectrum before the

Change internal window size setting;

Move through the soundfile with the slider above;

See the real-time version for more information on cepstrum

clip to graph bounds because first value in cepstrum

Creation argument is the name of the sample array to

Analyze a window starting at sample 44100 that is 2000

Updated for timbreIDLib version 0.7.6;

August 2018;

Prepend the "chain_fftData" message in front of the

[tID_fft~] outputs (N/2)+1 real values from the left

fftData <data> should consist of (window/2)+1 real

magSpec <data> should consist of (window/2)+1 magnitudes

The object in this help file accepts the chain_ messages

To minimize redundant calculations on the same window


## `cepstrumPitch`

Bang to analyze the entire array.;

Read from a different array;

Specify your sample's sampling rate. (default: 44100)

Change windowing function. Rectangular (0), Blackman

Print current settings in the post window;

Set threshold for detecting cepstral peak. In standard

Set the expected pitch range (MIDI) to determine where

Use power spectrum. (default: power);

Report power cepstrum (default: magnitude);

Add 1 to the power or magnitude spectrum before the

Updated for timbreIDLib version 0.7;

Move through the soundfile with the slider above,

July 2017;

See the real-time version for more information on cepstrum

Output value is pitch in MIDI units;

Analyze a window starting at sample 24100 that is 2000

Creation arguments are the name of the sample array


## `cepstrumPitch~`

Print current settings in the post window;

Change windowing function. Rectangular (0), Blackman

Inside a subpatch with re-blocking involving overlap

Use power spectrum. (default: power);

Set the expected pitch range (MIDI) to determine where

Use power cepstrum (default: magnitude);

Set threshold for detecting cepstral peak. In standard

Add 1 to magnitude or power spectrum before cepstrum

Updated for timbreIDLib version 0.7;

Change analysis window size;

Bang repeatedly to keep refreshing..., f 21;

July 2017;

Bang to output pitch;

Creation arguments are window size in samples and the

This feature can be sent to the timbreID external in

Audio buffering and windowing are taken care of by

Cepstrum analysis can be used for pitch tracking by


## `cepstrum~`

Use power spectrum. (default: magnitude);

Print current settings in the post window;

Change windowing function. Rectangular (0), Blackman

Inside a subpatch with re-blocking involving overlap

Report power cepstrum (default: magnitude);

Add 1 to the power or magnitude spectrum before the

Updated for timbreIDLib version 0.7;

Change analysis window size, f 17;

Bang repeatedly to keep refreshing...;

This feature can be sent to the timbreID external in

Creation argument is window size in samples, f 23

Bang to output cepstrum as a list;

clip to graph bounds because first value in cepstrum

Audio buffering and windowing are taken care of by

Real cepstrum is defined as the real portion of the

July 2017;


## `chroma`

Bang to analyze the entire array.;

Read from a different array;

Specify your sample's sampling rate. (default: 44100)

Change windowing function. Rectangular (0), Blackman

Print current settings in the post window;

Change internal window size setting;

Use power spectrum. (default: ON);

pitch tolerance in MIDI units;

Normalize pitch energy profile (default: OFF);

spectral energy threshold. energy below this thresh

Microtonal offset in cents for adapting to tuning systems

Use semitone, half-semitone, or third-semitone

analysis frequency range in Hz;

Move through the soundfile with the slider above,

Analyze a window starting at sample 44100 that is 2000

Prepend the "chain_fftData" message in front of the

[tID_fft~] outputs (N/2)+1 real values from the left

fftData <data> should consist of (window/2)+1 real

The object in this help file accepts the chain_ messages

To minimize redundant calculations on the same window

magSpec <data> should consist of (window/2)+1 magnitudes

See the real-time version for more information on pitch

In "half" or "third" mode, there are 24 or 36 elements

Creation arguments are: the name of the sample array

Updated for timbreIDLib version 0.9.0;

June 2022;


## `chroma~`

Print current settings in the post window;

Change windowing function. Rectangular (0), Blackman

Inside a subpatch with re-blocking involving overlap

Normalize pitch energy profile (default: OFF);

Use power spectrum. (default: ON);

pitch tolerance in MIDI units;

spectral energy threshold. energy below this thresh

Microtonal offset in cents for adapting to tuning systems

Use semitone, half-semitone, or third-semitone

analysis frequency range in Hz;

Change analysis window size, f 17;

Bang repeatedly to keep refreshing...;

This feature can be sent to the timbreID external in

Bang to output magnitude spectrum as a list;

Audio buffering and windowing are taken care of by

Pitch chroma indicates how much spectral energy is associated

Various aspects of the process can be adjusted with

In "half" or "third" mode, there are 24 or 36 elements

Creation arguments are: window size in samples, low

Updated for timbreIDLib version 0.9.0;

June 2022;


## `dct`

Bang to analyze the entire array.;

Read from a different array;

Specify your sample's sampling rate. (default: 44100)

Change windowing function. Rectangular (0), Blackman

Print current settings in the post window;

Normalize (default: ON);

Updated for timbreIDLib version 0.7;

Move through the soundfile with the slider above,

Creation argument is the name of the sample array to

See the real-time version for more information on the

July 2017;

Analyze a window starting at sample 44100 that is 2000


## `dct~`

Normalize spectrum (default: ON);

Print current settings in the post window;

Change windowing function. Rectangular (0), Blackman

Inside a subpatch with re-blocking involving overlap

Updated for timbreIDLib version 0.7;

Change analysis window size, f 17;

Bang repeatedly to keep refreshing...;

This feature can be sent to the timbreID external in

Creation argument is window size in samples, f 23

Bang to output DCT results as a list;

July 2017;

Audio buffering and windowing are taken care of by

The discrete cosine transform (DCT) multiplies an incoming


## `energy`

Bang to analyze the entire array.;

Read from a different array;

Specify your sample's sampling rate. (default: 44100)

Normalize the energy total according to the current

Output energy as power instead of RMS (default: OFF)

Report result in dB units instead of linear. 100 dB

Creation argument is the name of the sample array to

Analyze a window starting at sample 44100 that is 2000

Updated for timbreIDLib version 0.9.0;

June 2022;

See the real-time version for more information on signal


## `energyEntropy`

Bang to analyze the entire array.;

Read from a different array;

Specify your sample's sampling rate. (default: 44100)

Set the number of sub-windows per mid-term window;

Set the number of samples in each sub-window of mid-term

Analyze a window starting at sample 44100 that is 2000

Updated for timbreIDLib version 0.9.0;

June 2022;

Creation arguments are the name of the sample array

See the real-time version for more information on energy


## `energyEntropy~`

This feature can be sent to the timbreID external in

Updated for timbreIDLib version 0.9.0;

Creation arguments:;

Output energy entropy continuously;

Inside a subpatch with re-blocking involving overlap

Set the number of sub-windows per mid-term window;

Set the number of samples in each sub-window of mid-term

Each bang sent to [energyEntropy~] processes a mid-term

Here, because we're using 1024 (a quarter of the

compressed speech;

drum loop;

percussion samples;

June 2022;

Click one of the radio buttons to play a test signal

2) number of sub-windows per mid-term window, f 26

1) sub-window size (samples);

Energy entropy is a measure of abrupt changes in the

Note that lower entropy values are produced for abrupt


## `energy~`

Inside a subpatch with re-blocking involving overlap

Normalize the energy total according to the current

Output energy as power instead of RMS (default: OFF)

Report result in dB units instead of linear. 100 dB

This feature can be sent to the timbreID external in

Creation argument is window size in samples;

Audio buffering is taken care of by the external,

June 2022;

Updated for timbreIDLib version 0.9.0;

Output signal energy continuously;

Change window size;

As an alternative to Pd's built-in [env~] object,


## `featureAccum`

To clear memory, send the "clear" message. Note that

Also see:;

Updated for timbreIDLib version 0.7.6;

August 2018;

In "concat" mode, feature frames are accumulated until

In "sum" mode, incoming feature frames are accumulated

The "mean" mode behaves similarly to "sum" mode,

A simple moving average can be computed using "sma"

See more details about the behavior of the "concat"

If the optional "spew" feature is activated in the

<< see inside;

Creation arguments are the number of frames to expect

[featureAccum] accumulates a database of lists sent


## `featureDelta`

Also see:;

Analyze the most recent frame of audio and one from

[featureDelta] calculates the difference between each

Updated for timbreIDLib version 0.8.2;

January 2020;

Creation arguments are the length of the feature,


## `featureNorm`

Also see:;

June 2019;

Creation arguments are the length of the feature and

mode 1: -1 to 1 normalization;

mode 0: 0 to 1 normalization;

Provide minimum value and maximum value lists in the

Provide feature minimum and maximum attribute lists.

[featureNorm] takes in raw feature lists and normalizes

Updated for timbreIDLib version 0.8.0;


## `harmonicRatio`

Bang to analyze the entire array.;

Read from a different array;

Turn normalization on or off. With normalization on

Analyze a window starting at sample 44100 that is 2000

Updated for timbreIDLib version 0.9.0;

June 2022;

See the real-time version for more information on harmonic

Creation argument is the name of the sample array to


## `harmonicRatio~`

Change window size.;

Inside a subpatch with re-blocking involving overlap

Turn normalization on or off. With normalization on

This feature can be sent to the timbreID external in

Creation argument is window size in samples, f 23

Audio buffering is taken care of by the external,

June 2022;

Updated for timbreIDLib version 0.9.0;

Bang to output harmonic ratio;

Bang repeatedly to keep refreshing...;

Harmonic ratio is an indicator of the periodicity of

Turn on the metro at left to activate constant analysis


## `magSpec`

Bang to analyze the entire array.;

Read from a different array;

Normalize spectrum (default: ON);

Specify your sample's sampling rate. (default: 44100)

Use power spectrum. (default: magnitude);

Change windowing function. Rectangular (0), Blackman

Print current settings in the post window;

Change internal window size setting;

Move through the soundfile with the slider above,

Creation argument is the name of the sample array to

See the real-time version for more information on magnitude

Analyze a window starting at sample 44100 that is 2000

Updated for timbreIDLib version 0.7.6;

August 2018;

Prepend the "chain_fftData" message in front of the

[tID_fft~] outputs (N/2)+1 real values from the left

fftData <data> should consist of (window/2)+1 real

The object in this help file accepts the chain_ messages

To minimize redundant calculations on the same window


## `magSpec~`

Normalize spectrum (default: ON);

Use power spectrum. (default: magnitude);

Print current settings in the post window;

Change windowing function. Rectangular (0), Blackman

Inside a subpatch with re-blocking involving overlap

Updated for timbreIDLib version 0.7;

Change analysis window size, f 17;

Bang repeatedly to keep refreshing...;

This feature can be sent to the timbreID external in

Creation argument is window size in samples, f 23

Bang to output magnitude spectrum as a list;

July 2017;

Audio buffering and windowing are taken care of by

Magnitude spectrum can be measured with a combination


## `maxSample`

Bang to analyze the entire array.;

Read from a different array;

Specify your sample's sampling rate. (default: 44100)

Creation argument is the name of the sample array to

Analyze a window starting at sample 44100 that is 2000

Updated for timbreIDLib version 0.7;

July 2017;

See the real-time version too.;

Outlet 1: maximum sample value;

Outlet 2: maximum sample index relative to the analysis


## `maxSampleDelta`

Bang to analyze the entire array.;

Read from a different array;

Specify your sample's sampling rate. (default: 44100)

Creation argument is the name of the sample array to

Analyze a window starting at sample 44100 that is 2000

Updated for timbreIDLib version 0.7;

See the real-time version for more information on sample

July 2017;

Outlet 1: maximum sample delta value, f 31;

Outlet 2: maximum sample delta index relative to the


## `maxSampleDelta~`

Change window size.;

Inside a subpatch with re-blocking involving overlap

Updated for timbreIDLib version 0.7;

This feature can be sent to the timbreID external in

Creation argument is window size in samples;

July 2017;

Bang to output maximum sample delta magnitude of most

Outlet 1: maximum sample delta magnitude value;

Outlet 2: index of maximum sample delta magnitude relative

[maxSampleDelta~] takes the absolute value of the difference

Audio buffering is taken care of by the external,


## `maxSample~`

Print current settings in the post window;

Inside a subpatch with re-blocking involving overlap

Updated for timbreIDLib version 0.7;

Change analysis window size, f 17;

Bang repeatedly to keep refreshing...;

This feature can be sent to the timbreID external in

Creation argument is window size in samples, f 23

July 2017;

Bang to output maximum sample value and index;

[maxSample~] reports the value and index of the largest

Audio buffering is taken care of by the external,


## `melSpec`

Bang to analyze the entire array.;

Read from a different array;

Construct a new filterbank with a specific spacing.

Normalize spectrum (default: ON);

Specify your sample's sampling rate. (default: 44100)

Use power spectrum. (default: magnitude);

Change windowing function. Rectangular (0), Blackman

Print current settings in the post window;

Rather than sum energy in the triangular mel spaced

If using the triangular mel spaced filters, you can

Change internal window size setting;

Move through the soundfile with the slider above,

See the real-time version for more information on mel

Creation arguments are the name of the sample array

Analyze a window starting at sample 44100 that is 2000

Updated for timbreIDLib version 0.7.6;

August 2018;

Prepend the "chain_fftData" message in front of the

[tID_fft~] outputs (N/2)+1 real values from the left

fftData <data> should consist of (window/2)+1 real

magSpec <data> should consist of (window/2)+1 magnitudes

The object in this help file accepts the chain_ messages

To minimize redundant calculations on the same window


## `melSpec~`

Construct a new filterbank with a specific spacing.

Normalize spectrum (default: ON);

Use power spectrum. (default: magnitude);

Print current settings in the post window;

Change windowing function. Rectangular (0), Blackman

Inside a subpatch with re-blocking involving overlap

Rather than sum energy in the triangular mel spaced

If using the triangular mel spaced filters, you can

Updated for timbreIDLib version 0.7;

Change analysis window size, f 17;

Bang repeatedly to keep refreshing...;

This feature can be sent to the timbreID external in

Creation arguments are window size in samples and filterbank

Bang to output mel spectrum as a list;

July 2017;

Audio buffering and windowing are taken care of by

Mel-frequency spectrum is a warping of normal magnitude


## `mfcc`

Bang to analyze the entire array.;

Read from a different array;

Construct a new filterbank with a specific spacing.

Normalize spectrum (default: ON);

Specify your sample's sampling rate. (default: 44100)

Use power spectrum. (default: magnitude);

Change windowing function. Rectangular (0), Blackman

Print current settings in the post window;

Rather than sum energy in the triangular mel spaced

If using the triangular mel spaced filters, you can

Change internal window size setting;

Move through the soundfile with the slider above,

Creation arguments are the name of the sample array

See the real-time version for more information on mel-frequency

Analyze a window starting at sample 44100 that is 2000

Updated for timbreIDLib version 0.7.6;

August 2018;

Prepend the "chain_fftData" message in front of the

[tID_fft~] outputs (N/2)+1 real values from the left

fftData <data> should consist of (window/2)+1 real

magSpec <data> should consist of (window/2)+1 magnitudes

The object in this help file accepts the chain_ messages

To minimize redundant calculations on the same window

melSpec <data> should consist of 38 mel-spectrum energy


## `mfcc~`

Construct a new filterbank with a specific spacing.

Normalize spectrum (default: ON);

Use power spectrum. (default: magnitude);

Print current settings in the post window;

Change windowing function. Rectangular (0), Blackman

Inside a subpatch with re-blocking involving overlap

Rather than sum energy in the triangular mel spaced

If using the triangular mel spaced filters, you can

Updated for timbreIDLib version 0.7;

Change analysis window size, f 16;

Bang repeatedly to keep refreshing...;

This feature can be sent to the timbreID external in

Creation arguments are window size in samples and filterbank

Bang to output MFCCs as a list;

July 2017;

Audio buffering and windowing are taken care of by

Mel-frequency cepstrum is much different than raw cepstrum.


## `minSample`

Bang to analyze the entire array.;

Read from a different array;

Specify your sample's sampling rate. (default: 44100)

Creation argument is the name of the sample array to

Analyze a window starting at sample 44100 that is 2000

Updated for timbreIDLib version 0.7;

July 2017;

See the real-time version too.;

Outlet 1: minimum sample value;

Outlet 2: minimum sample index relative to the analysis


## `minSampleDelta`

Bang to analyze the entire array.;

Read from a different array;

Specify your sample's sampling rate. (default: 44100)

Creation argument is the name of the sample array to

Analyze a window starting at sample 44100 that is 2000

Updated for timbreIDLib version 0.7;

See the real-time version for more information on sample

July 2017;

Outlet 1: minimum sample delta value, f 25;

Outlet 2: minimum sample delta index relative to the


## `minSampleDelta~`

Change window size.;

Inside a subpatch with re-blocking involving overlap

Updated for timbreIDLib version 0.7;

This feature can be sent to the timbreID external in

Creation argument is window size in samples;

July 2017;

Outlet 1: minimum sample delta magnitude value;

Outlet 2: index of minimum sample delta magnitude relative

Bang to output minimum sample delta magnitude of most

[minSampleDelta~] takes the absolute value of the difference

Audio buffering is taken care of by the external,


## `minSample~`

Print current settings in the post window;

Inside a subpatch with re-blocking involving overlap

Updated for timbreIDLib version 0.7;

Change analysis window size, f 17;

Bang repeatedly to keep refreshing...;

This feature can be sent to the timbreID external in

Creation argument is window size in samples, f 23

July 2017;

[minSample~] reports the value and index of the smallest

Bang to output minimum sample value and index;

Audio buffering is taken care of by the external,


## `nearestPoint`

Clear the current set of points.;

Change dimensionality.;

The index of the nearest point comes out the left outlet

Generate a random point in space.;

nearestPoint accepts members from a set of points in

Updated for timbreIDLib version 0.7;

Output the N nearest matches to the test point;

July 2017;

This object exists in order to enable the timbreID timbre-space


## `peakSample`

Bang to analyze the entire array.;

Read from a different array;

Specify your sample's sampling rate. (default: 44100)

Creation argument is the name of the sample array to

Analyze a window starting at sample 44100 that is 2000

Updated for timbreIDLib version 0.7;

July 2017;

See the real-time version too.;

Outlet 1: peak sample value;

Outlet 2: peak sample index relative to the analysis


## `peakSample~`

Print current settings in the post window;

Inside a subpatch with re-blocking involving overlap

Change analysis window size, f 16;

Bang repeatedly to keep refreshing...;

This feature can be sent to the timbreID external in

Creation argument is window size in samples, f 23

Audio buffering and windowing are taken care of by

Bang to output peak sample value and location;

June 2022;

Updated for timbreIDLib version 0.9.0;

[peakSample~] reports the value and index of the sample


## `phaseSpec`

Bang to analyze the entire array.;

Read from a different array;

Specify your sample's sampling rate. (default: 44100)

Change windowing function. Rectangular (0), Blackman

Print current settings in the post window;

Change internal window size setting;

Move through the soundfile with the slider above,

Creation argument is the name of the sample array to

Analyze a window starting at sample 44100 that is 2000

-pi;

Updated for timbreIDLib version 0.7.6;

August 2018;

Prepend the "chain_fftData" message in front of the

[tID_fft~] outputs (N/2)+1 real values from the left

fftData <data> should consist of (window/2)+1 real

The object in this help file accepts the chain_ messages

To minimize redundant calculations on the same window

See the real-time version for more information on phase


## `phaseSpec~`

Print current settings in the post window;

Change windowing function. Rectangular (0), Blackman

Inside a subpatch with re-blocking involving overlap

Change analysis window size, f 17;

Bang repeatedly to keep refreshing...;

This feature can be sent to the timbreID external in

Creation argument is window size in samples, f 23

Audio buffering and windowing are taken care of by

-pi;

Updated for timbreIDLib version 0.7.6;

August 2018;

Bang to output spectrum phases as a list;

The phase spectrum is calculated by taking the arctangent


## `sampleBuffer~`

Print current settings in the post window;

Inside a subpatch with re-blocking involving overlap

Updated for timbreIDLib version 0.7;

Change analysis window size, f 16;

Bang repeatedly to keep refreshing...;

This feature can be sent to the timbreID external in

Creation argument is window size in samples, f 23

July 2017;

Bang to output the most recent N samples as a list,

[sampleBuffer~] contains the same audio buffering routine

Audio buffering is taken care of by the external,


## `specBrightness`

Bang to analyze the entire array.;

See the real-time version for more information on spectral

Read from a different array;

Specify your sample's sampling rate. (default: 44100)

Use power spectrum. (default: magnitude);

Set boundary frequency (default: 1200);

Change windowing function. Rectangular (0), Blackman

Change internal window size setting;

Analyze a window starting at sample 44100 that is 2000

Creation arguments are the name of the sample array

Updated for timbreIDLib version 0.7.6;

August 2018;

Prepend the "chain_fftData" message in front of the

[tID_fft~] outputs (N/2)+1 real values from the left

fftData <data> should consist of (window/2)+1 real

magSpec <data> should consist of (window/2)+1 magnitudes

The object in this help file accepts the chain_ messages

To minimize redundant calculations on the same window


## `specBrightness~`

Change window size.;

Set boundary freq.;

Bang to output brightness.;

Spectral Brightness is the ratio of the sum of magnitudes

Use power spectrum. (default: magnitude);

Change windowing function. Rectangular (0), Blackman

Inside a subpatch with re-blocking involving overlap

Updated for timbreIDLib version 0.7;

This feature can be sent to the timbreID external in

Audio buffering and windowing are taken care of by

Creation arguments are window size in samples, and

July 2017;


## `specCentroid`

Bang to analyze the entire array.;

See the real-time version for more information on spectral

Read from a different array;

Specify your sample's sampling rate. (default: 44100)

Use power spectrum. (default: magnitude);

Change windowing function. Rectangular (0), Blackman

Change internal window size setting;

Creation argument is the name of the sample array to

Analyze a window starting at sample 44100 that is 2000

Updated for timbreIDLib version 0.7.6;

August 2018;

Prepend the "chain_fftData" message in front of the

[tID_fft~] outputs (N/2)+1 real values from the left

fftData <data> should consist of (window/2)+1 real

magSpec <data> should consist of (window/2)+1 magnitudes

The object in this help file accepts the chain_ messages

To minimize redundant calculations on the same window


## `specCentroid~`

Change window size.;

Bang to output centroid.;

Spectral Centroid is the center of mass of magnitude

Use power spectrum. (default: magnitude);

Inside a subpatch with re-blocking involving overlap

Change windowing function. Rectangular (0), Blackman

Updated for timbreIDLib version 0.7;

This feature can be sent to the timbreID external in

Audio buffering and windowing are taken care of by

Creation argument is window size in samples;

July 2017;


## `specFlatness`

Bang to analyze the entire array.;

Read from a different array;

Specify your sample's sampling rate. (default: 44100)

Use power spectrum. (default: magnitude);

Change windowing function. Rectangular (0), Blackman

Change internal window size setting;

Creation argument is the name of the sample array to

Analyze a window starting at sample 44100 that is 2000

See the real-time version for more information on spectral

Updated for timbreIDLib version 0.7.6;

August 2018;

Prepend the "chain_fftData" message in front of the

[tID_fft~] outputs (N/2)+1 real values from the left

fftData <data> should consist of (window/2)+1 real

magSpec <data> should consist of (window/2)+1 magnitudes

The object in this help file accepts the chain_ messages

To minimize redundant calculations on the same window


## `specFlatness~`

Change window size.;

Use power spectrum. (default: magnitude);

Inside a subpatch with re-blocking involving overlap

Change windowing function. Rectangular (0), Blackman

Updated for timbreIDLib version 0.7;

This feature can be sent to the timbreID external in

Audio buffering and windowing are taken care of by

Creation argument is window size in samples;

Bang to output flatness;

July 2017;

Spectral Flatness is the ratio of the geometric mean


## `specFlux`

See the real-time version for more information on spectral

Read from a different array;

Specify your sample's sampling rate. (default: 44100)

Use power spectrum. (default: magnitude);

Squared difference vs. Absolute value of difference.

Change windowing function. Rectangular (0), Blackman

Set separation in samples between analysis windows

Change internal window size setting;

Normalize spectrum. (default: OFF);

Use the natural logarithm of spectrum values. (default:

Creation arguments are the name of the sample array

Analyze a FORWARD window starting at sample 44100 that

Change modes to report flux, spectral growth only

Prepend the "chain_fftData" message in front of the

The object in this help file accepts the chain_ messages

To minimize redundant calculations on the same window

[tID_fft~] outputs (N/2)+1 real values from the left

fftData <data> should consist of (window/2)+1 real

Spectral flux is a special case, because measurements

magSpec <data> should consist of (window/2)+1 magnitudes

Updated for timbreIDLib version 0.9.0;

June 2022;


## `specFlux~`

Turn on for continuous analysis;

Spectral flux can be used for basic attack detection.

If 800 is too low or high, try a different threshhold.

For these purposes, we'll turn on "growth" mode so

Activate a signal above and bang to output its flux.

Change window size.;

Squared difference vs. Absolute value of difference.

Use power instead of magnitude;

Change distance between analysis windows in samples.

Inside a subpatch with re-blocking involving overlap

Change windowing function. Rectangular (0), Blackman

Normalize spectrum. Default: OFF.;

Use the natural logarithm of spectrum values;

Creation arguments are window size and separation in

specFlux~ reports the full list of differences (i.e.

Audio buffering and windowing are taken care of by

This feature can be sent to the timbreID external in

In the [attack-detection] sub-patch, the left outlet

Typically, spectral flux is the sum of squared difference

Change modes to report flux, spectral growth only

Updated for timbreIDLib version 0.9.0;

June 2022;


## `specHarmonicity`

Bang to analyze the entire array.;

Read from a different array;

Specify your sample's sampling rate. (default: 44100)

Use power spectrum. (default: magnitude);

Change windowing function. Rectangular (0), Blackman

Print current settings in the post window;

Threshold for detecting spectral peaks in percent relative

Maximum number of peaks to consider. (default: 24)

Minimum allowed fundamental frequency. (default: 30)

Maximum allowed fundamental frequency. (default: 4000)

Flag to use fundamental frequency data supplied to

Change internal window size setting;

Analyze a window starting at sample 44100 that is 2000

Move through the soundfile with the slider above;

Creation argument is the name of the sample array to

See the real-time version for more information on spectrum

Outlet 1: spectrum harmonicity;

Outlet 2: spectrum inharmonicity;

Inlet 2: fundamental frequency in Hz (not MIDI!). Only

Updated for timbreIDLib version 0.7.6;

August 2018;

Prepend the "chain_fftData" message in front of the

[tID_fft~] outputs (N/2)+1 real values from the left

fftData <data> should consist of (window/2)+1 real

magSpec <data> should consist of (window/2)+1 magnitudes

The object in this help file accepts the chain_ messages

To minimize redundant calculations on the same window


## `specHarmonicity~`

Use power spectrum. (default: magnitude);

Inside a subpatch with re-blocking involving overlap

Change windowing function. Rectangular (0), Blackman

Change window size.;

Print current settings in the post window;

Threshold for detecting spectral peaks in percent relative

Maximum number of peaks to consider. (default: 24)

Minimum allowed fundamental frequency. (default: 30)

Maximum allowed fundamental frequency. (default: 4000)

Flag to use fundamental frequency data supplied to

Updated for timbreIDLib version 0.7;

This feature can be sent to the timbreID external in

Audio buffering and windowing are taken care of by

Creation argument is window size in samples;

July 2017;

Bang to output harmonicity and inharmonicity, f 18

only show the first 1/8th of the spectrum;

If you choose to use the "input_fund" feature to specify

Outlet 1: spectrum harmonicity;

Outlet 2: spectrum inharmonicity;

Inlet 2: fundamental frequency in Hz (not MIDI!). Only

The two outlets supply separate harmonicity and inharmonicity

[specHarmonicity~] quantifies the harmonic alignment


## `specIrregularity`

Bang to analyze the entire array.;

Read from a different array;

Specify your sample's sampling rate. (default: 44100)

Use power spectrum. (default: magnitude);

Change windowing function. Rectangular (0), Blackman

Normalize spectrum. This only affects results when

Change internal window size setting;

Analyze a window starting at sample 44100 that is 2000

Creation arguments are the name of the sample array

See the real-time version for more information on spectral

Choose either Jensen (0) or Krimphoff (1) algorithm.

Updated for timbreIDLib version 0.7.6;

August 2018;

Prepend the "chain_fftData" message in front of the

[tID_fft~] outputs (N/2)+1 real values from the left

fftData <data> should consist of (window/2)+1 real

magSpec <data> should consist of (window/2)+1 magnitudes

The object in this help file accepts the chain_ messages

To minimize redundant calculations on the same window


## `specIrregularity~`

Use power spectrum. (default: magnitude);

Change windowing function. Rectangular (0), Blackman

Inside a subpatch with re-blocking involving overlap

Normalize spectrum. This only affects results when

Updated for timbreIDLib version 0.7;

This feature can be sent to the timbreID external in

Choose either Jensen (0) or Krimphoff (1) algorithm.

Audio buffering and windowing are taken care of by

Creation arguments are window size in samples, and

Bang to output irregularity;

Change window size;

July 2017;

Spectral Irregularity has two common definitions: one


## `specKurtosis`

Bang to analyze the entire array.;

Read from a different array;

Specify your sample's sampling rate. (default: 44100)

Use power spectrum. (default: magnitude);

Change windowing function. Rectangular (0), Blackman

Change internal window size setting;

Creation argument is the name of the sample array to

Analyze a window starting at sample 44100 that is 2000

See the real-time version for more information on spectral

Updated for timbreIDLib version 0.7.6;

August 2018;

Prepend the "chain_fftData" message in front of the

[tID_fft~] outputs (N/2)+1 real values from the left

fftData <data> should consist of (window/2)+1 real

magSpec <data> should consist of (window/2)+1 magnitudes

The object in this help file accepts the chain_ messages

To minimize redundant calculations on the same window


## `specKurtosis~`

Use power spectrum. (default: magnitude);

Inside a subpatch with re-blocking involving overlap

Change windowing function. Rectangular (0), Blackman

Updated for timbreIDLib version 0.7;

This feature can be sent to the timbreID external in

Audio buffering and windowing are taken care of by

Creation argument is window size in samples;

Bang continuously;

Spectral kurtosis measures the peakedness of a spectrum.

Change window size;

Bang to output kurtosis;

July 2017;


## `specRolloff`

Bang to analyze the entire array.;

Read from a different array;

Specify your sample's sampling rate. (default: 44100)

Use power spectrum. (default: magnitude);

Change windowing function. Rectangular (0), Blackman

Set concentration target (default: 0.85);

Change internal window size setting;

Analyze a window starting at sample 44100 that is 2000

Creation arguments are the name of the sample array

See the real-time version for more information on spectral

Updated for timbreIDLib version 0.7.6;

August 2018;

Prepend the "chain_fftData" message in front of the

[tID_fft~] outputs (N/2)+1 real values from the left

fftData <data> should consist of (window/2)+1 real

magSpec <data> should consist of (window/2)+1 magnitudes

The object in this help file accepts the chain_ messages

To minimize redundant calculations on the same window


## `specRolloff~`

Use power spectrum. (default: magnitude);

Change windowing function. Rectangular (0), Blackman

Inside a subpatch with re-blocking involving overlap

Updated for timbreIDLib version 0.7;

This feature can be sent to the timbreID external in

Audio buffering and windowing are taken care of by

Set energy concentration target;

Creation arguments are window size in samples, and

Bang to output rolloff frequency;

Change window size;

Output continuously;

Spectral Rolloff is the frequency below which a certain

July 2017;


## `specSkewness`

Bang to analyze the entire array.;

Read from a different array;

Specify your sample's sampling rate. (default: 44100)

Use power spectrum. (default: magnitude);

Change windowing function. Rectangular (0), Blackman

Change internal window size setting;

Creation argument is the name of the sample array to

Analyze a window starting at sample 44100 that is 2000

See the real-time version for more information on spectral

Updated for timbreIDLib version 0.7.6;

August 2018;

Prepend the "chain_fftData" message in front of the

[tID_fft~] outputs (N/2)+1 real values from the left

fftData <data> should consist of (window/2)+1 real

magSpec <data> should consist of (window/2)+1 magnitudes

The object in this help file accepts the chain_ messages

To minimize redundant calculations on the same window


## `specSkewness~`

Use power spectrum. (default: magnitude);

Inside a subpatch with re-blocking involving overlap

Change windowing function. Rectangular (0), Blackman

Updated for timbreIDLib version 0.7;

This feature can be sent to the timbreID external in

Audio buffering and windowing are taken care of by

Creation argument is window size in samples;

Bang continuously;

Change window size;

Bang to output skewness;

July 2017;

Spectral skewness measures the symmetry of a spectral


## `specSlope`

Bang to analyze the entire array.;

Analyze a window starting at sample 44100 that is 2000

Read from a different array;

Normalize spectrum (default: ON);

Specify your sample's sampling rate. (default: 44100)

Use power spectrum. (default: magnitude);

Change windowing function. Rectangular (0), Blackman

Print current settings in the post window;

Change window size;

Use the slider above to move through the audio file

Creation argument is the name of the sample array to

See the real-time version for more information on spectral

Updated for timbreIDLib version 0.7.6;

August 2018;

Prepend the "chain_fftData" message in front of the

[tID_fft~] outputs (N/2)+1 real values from the left

fftData <data> should consist of (window/2)+1 real

magSpec <data> should consist of (window/2)+1 magnitudes

The object in this help file accepts the chain_ messages

To minimize redundant calculations on the same window


## `specSlope~`

Change analysis window size;

Bang repeatedly...;

Bang to output slope;

Updated for timbreIDLib version 0.7;

Normalize spectrum (default: ON);

Use power spectrum. (default: magnitude);

Print current settings in the post window;

Change windowing function. Rectangular (0), Blackman

Inside a subpatch with re-blocking involving overlap

This feature can be sent to the timbreID external in

Spectrum slope is the slope of the best-fit line through

Audio buffering and windowing are taken care of by

July 2017;


## `specSpread`

Bang to analyze the entire array.;

Read from a different array;

Specify your sample's sampling rate. (default: 44100)

Use power spectrum. (default: magnitude);

Change windowing function. Rectangular (0), Blackman

Change internal window size setting;

Creation argument is the name of the sample array to

Analyze a window starting at sample 44100 that is 2000

See the real-time version for more information on spectral

Updated for timbreIDLib version 0.7.6;

August 2018;

Prepend the "chain_fftData" message in front of the

[tID_fft~] outputs (N/2)+1 real values from the left

fftData <data> should consist of (window/2)+1 real

magSpec <data> should consist of (window/2)+1 magnitudes

The object in this help file accepts the chain_ messages

To minimize redundant calculations on the same window


## `specSpread~`

Use power spectrum. (default: magnitude);

Inside a subpatch with re-blocking involving overlap

Change windowing function. Rectangular (0), Blackman

Updated for timbreIDLib version 0.7;

This feature can be sent to the timbreID external in

Audio buffering and windowing are taken care of by

Creation argument is window size in samples;

Bang continuously;

Change window size;

Bang to output spread;

fundamental;

waveshaper;

divide by fundamental;

range for table;

offset to middle of table;

C.F. relative;

to fundamental;

(MIDI units);

ring mod;

This is taken straight from Pd's built-in documentation

Spectral spread is a measure of the concentration of

July 2017;


## `tID-conversion`

timbreID conversion objects use the same functions in

Bark frequency is calculated as 6.0*asinh(freq/600.0)

Mel frequency is calculated as 1127*log(1+(freq/700))

Updated for timbreIDLib version 0.7.6;

August 2018;

Frequency is calculated as bin*R/N, and bin number


## `tID_fft`

Bang to analyze the entire array.;

Read from a different array;

Specify your sample's sampling rate. (default: 44100)

Change windowing function. Rectangular (0), Blackman

Change internal window size setting;

Print current settings in the post window;

Zero pad after the windowed signal content. A zero

Normalize spectrum (default: OFF);

Move through the soundfile with the slider above,

Creation argument is the name of the sample array to

Analyze a window starting at sample 44100 that is 2000

See the real-time version for more information on timbreID's

Updated for timbreIDLib version 0.8.0;

June 2019;


## `tID_fft~`

Print current settings in the post window;

Change windowing function. Rectangular (0), Blackman

Inside a subpatch with re-blocking involving overlap

Zero pad after the windowed signal content. A zero

Normalize spectrum (default: OFF);

Change analysis window size, f 17;

Bang repeatedly to keep refreshing...;

This feature can be sent to the timbreID external in

Creation argument is window size in samples, f 23

Audio buffering and windowing are taken care of by

Outlet 1: real components;

Outlet 2: imaginary components;

Bang to output complex Fourier transform data as a

The complex Fourier transform of a signal can be obtained

Updated for timbreIDLib version 0.8.0;

June 2019;


## `tID_mean`

Suppose you take 32 spectral centroid measurements over

Creating a larger feature vector composed of several

Also see:;

Taking the mean and standard deviation for each of these

[tID_mean] calculates the arithmetic mean (average) of

Updated for timbreIDLib version 0.7;

July 2017;


## `tID_std`

Suppose you take 32 spectral centroid measurements over

Creating a larger feature vector composed of several

The [tID_std] object calculates the standard deviation

Also see:;

Taking the mean and standard deviation for each of these

Updated for timbreIDLib version 0.7;

July 2017;


## `tabletool`

Dot product;

Euclidean distance;

Taxicab distance;

Pearson correlation;

Add value pairs by index., f 16;

Multiply value pairs by index.;

Divide value pairs by index.;

Subtract value pairs by index., f 15;

NOTE: data from the table specified in the message is

NOTE: the active table's data is divided by data from

These four methods operate between the active table and

These methods perform arithmetic on the active table

The "autocorr" method calculates cross correlation

Add a positive or negative offset to all values.;

Shift elements by index forward or back. The overflow

Multiply all values by a scalar;

Copy another table to the currently set table.;

Copy part of another table to the currently set table.

Like shift, but fill excess with zeros.;

Remove the value at a certain index, and send it

Starting at a certain index, insert a value. Remaining

Write a constant (\$1) to a range of the table from

Normalize to a range with a specified minimum (\$1)

Normalize so that all values are between 0 and 1,

Shuffle table elements in a random order.;

Reverse the order of all elements.;

Sort values from low to high and reorder. For high to

Swap a pair of values at certain indices.;

Replace all occurrences of the first value with the

Flip all values. Low becomes high and vice versa.;

Smooth out data by averaging with neighboring values.

Sort only a specific range between indices$1 and

Take the absolute value of the table data;

Raise table data to a given power;

Write common windowing functions to an array. Windows

Fill an array with random numbers in a certain range.

Shift drag to try different exponents.;

Generate a random walk. Arguments: starting value,

Generate a series of values between two points (\$1

Clip all values in table to lower and upper limits;

Set all values to the next highest integer;

Set all values to the next lowest integer;

Take the reciprocal of all values;

Bash any values above a threshold (\$1) to the given

Bash any values below a threshold (\$1) to the given

Round all values in table to a given resolution (\$1)

Convert all values from MIDI to frequency in Hz;

Convert from Bark to frequency in Hz;

Convert from frequency in Hz to Bark;

Convert all values from frequency in Hz to MIDI;

Convert all values from decibels to RMS amplitude;

Convert all values from RMS amplitude decibels;

<< MIDI range of a piano;

Convert from bin number to frequency based on a given

Convert from frequency to bin number based on a given

Between commands, you should re-fit the boundaries

The fit_bounds method finds the maximum and minimum values

Finally, you can also search for peaks based on min

You can search for valleys in a similar fashion based

Search for peaks based on changes in slope from positive

Search for any changes in the table. If any value has

Search for zero crossings. Left outlet reports the

Search for occurrences of a particular value, and

Search for values that are greater than a particular

Search for values that are less than a particular value

Look for values between two bounds (non-inclusive)

Minimum value in table.;

Maximum value in table.;

Nearest value in table.;

For these methods, the value itself appears at the

Find the k smallest values and output as a list;

Find the k largest values and output as a list;

Value and index of the item with the minimum/maximum

[tabletool] manipulates, searches, and provides

For non-real-time assembling of audio, the overlap_add

Here's a toy example where we grab random 8192-point

Arguments;$1: starting sample in source array;

Window function names; rectangular; blackman;

The permute method lists all permutations (with repetition)

Or concatenate the active table with another table.

Lace the active table with another table, sending

If table size == N, this creates a list of N values

This creates a list of N values where term_i = tablevalue_i

Take the arithmetic mean.;

Calculate standard deviation.;

Take the geometric mean. You will get NANs on negative

Return a copy of the table data as a set with no duplicate

Find the median value. The median will be output from

Find the mode. The mode will be output from the left

Sum all values.;

Find the range of the table data.;

Dump all values to a list at the right outlet.;

Ask for the length of the table.;

Specify the active table.;

Restore the stored values after you've messsed them

Wipe all memory.;

Store the table values to internal memory. Note that

Randomly select a value from the table. The index of

Iterate through the table and send each value out the

Dump values from index$1 through index$2 to a list

Arguments are: lower and upper indices to search between

Add some INHARMONIC partials to try and screw up the

Randomize the amplitudes;

Wait 100ms for the pitch transition to settle, then

If DSP is on, you can re-tune the fundamental of a

The index of the most likely fundamental peak is sent

Run the Harmonic Product Spectrum algorithm, which

When building a label file based on classifications

Updated for timbreIDLib version 0.9.0;

June 2022;


## `tempo~`

Inside a subpatch with re-blocking involving overlap

Change windowing function. Rectangular (0), Blackman

Change window size;

Use power instead of magnitude spectrum for the spectral

Change analysis hop and frame separation;

Use squared spectral difference vs. absolute value

Tempo range to search for (BPM);

Number of harmonics to search for in HPS algorithm

Reset the current maximum peak value and search for

Enable/disable updating of the maximum onset peak value

Onset peak threshold as percentage of the current maximum

Specify a limited frequency band in Hz to use in spectral

Specify a value that all onset data to be bashed to

Onset buffer size (ms). This duration is also resized

<< since spectral difference onset data has an unpredictable

Updated for timbreIDLib version 0.7.6;

While you can use the raw tempo results appearing at

Fill the tempo buffer with a particular BPM value;

Initialize the tempo buffer, filling it with -1's

Size of the buffer holding the latest tempo measurements

Activate debug mode;

Print internal settings and info to the Pd console

Some generally useful info:;

The slower your tempo, the longer your onset buffer

Don't set the "harmonics" setting too low (2) or too

If you can live with very high latency, try making

Tempo tracking works best on signals with a stable tempo

Tempo tracking is prone to "octave errors" (i.e.,

Onset peak data thresholding works based on a percent

Before running the HPS algorithm on the onset peak

Unlike pitch and onset tracking, tempo estimation

Use the "reset_max_onset_peak" method any time your

[tempo~] estimates the tempo (BPM) of an input signal.

There are many settings that affect the accuracy and

Outlets:;

4) Spectral growth onset data list;

Creation arguments:, f 20;

1) Window size in samples;

2) Analysis hop in samples;

2) Confidence in mode tempo (percent);

3) Raw tempo estimate (BPM);

1) Mode of most recent tempo estimates (rounded BPM)

August 2018;


## `timbreID`

For more detailed examples, download the separate

The aim of this library is to provide a flexible set

Because there is a lot of flexibility, there are

This help patch provides a basic example of how to classify

BFCCs are used here, but [timbreID] can receive any

Some other feature extraction objects in the timbreIDLib

[timbreID] stores, clusters, and classifies feature

Detect onsets with bark~;

Doing the attack detection in a subpatch with the input

These were good onset detection settings for the audio

timbreIDLib comes with its own onset detection object:

The third outlet reports a questionable confidence measure

Specify a list of weights. Suppose you have a feature

If you need to look at the feature database values,

Write an OCTAVE data file in text data format. You can

Write an ARFF file for direct import into WEKA (www.cs.waikato.ac.nz/ml/weka).

Write a training database file for use with the FANN

[timbreID]'s default binary file format is .timid. This

Also note that "write_text" obeys the "attribute_order"

Write a MATLAB matrix file, that can be loaded with

The FANN method uses the current cluster index of each

"write_text" arguments; 1) the file name to be written

Arguments: 1) the file name to be written, 2) an

Note that as of timbreIDLib version 0.7, the text

Query the maximum and minimum instance lengths in the

Request a specific instance's full feature list;

Request a list of a specific attribute for all instances

Get a list of the K largest or smallest values for

Find out how many instances are in the database, f

Print information about [timbreID]'s internal memory

Spit out a list of the max or min values for all attributes

Apart from "print", these methods produce output at

Generate a similarity matrix. Arguments are starting

Arguments; 1) attribute index; 2) optional normalization

Arguments; 1) instance index; 2) optional normalization

Arguments; 1) k (number of values to output); 2)

These methods are only relevant when performing ID requests

Restrict the search to a neighborhood of instances around

Specify the center instance for searching within a neighborhood

With reorient on, the search_center will be constantly

With the "stutter_protect" option on, [timbreID] does

Set a probability between 0-1 that search center will

Turn on/off database search wrapping when using [timbreID]'s

The "max_matches" setting can have an impact on how

Another alternative to auto-clustering is "manual_cluster"

The text format that results from "write_clusters_text"

Find out what cluster a given database instance belongs

If you have clustered your instances, send the full

For small training datasets like the one in this help

Also note that [timbreID] does not check to see if

<< Methods designed for concatenative synthesis. They

Output the distances and instance (or cluster) IDs of

Manual step;

Inter-onset time;

Sorry, no envelope to make the transitions pretty...

1) Load the training sample to a table:;

3) Try an order starting from a particular instrument:

2) Load a list of attack locations in samples:;

Auto-play through timbre order, f 18;

There are two options for timbre order requests: relative

See the timbre-ordering example in the examples package

Choose a distance metric.; 0 is Euclidean distance

Order attributes by variance, so that only the most

You can provide a list of symbolic names for attributes

You can retrieve the symbolic name, weight, and

Manually order the attributes. In conjunction with

<< A small example of how to order sounds by timbre

<< How to save cluster information;

Specify a restricted range of attributes to use in

Normalize all feature attributes to the 0-1 range.

Go back to regular attribute order;

This is only relevant if clustering has been performed.

If you prepend an input feature list with "worst_match"

Test with the given training/testing recordings. Turn

3rd inlet has specific functionality for concatenative

Several methods produce output at the fourth outlet

<< this sends timbre order results to a table in [pd

You can train on any combination of audio features.

June 2022;

Many more details inside >>;

Perform hierarchical clustering to find a given number

Wipe all instances to start over;

First outlet reports the index of the nearest match

During training, the first outlet reports the number

Second outlet reports the distance to the nearest match

Open this subpatch for a description of the object;

Read & write feature database (binary format);

Go back to reporting raw instance indices;

Updated for timbreIDLib version 0.9.0;


## `waveNoise`

Bang to analyze the entire array.;

Read from a different array;

Specify your sample's sampling rate. (default: 44100)

Creation argument is the name of the sample array to

Analyze a window starting at sample 44100 that is 2000

See the real-time version for more information on waveform

Updated for timbreIDLib version 0.9.0;

June 2022;

Note that with a real signal, low level noise will


## `waveNoise~`

Change window size.;

Inside a subpatch with re-blocking involving overlap

This feature can be sent to the timbreID external in

Bang repeatedly to keep refreshing...;

Audio buffering is taken care of by the external,

June 2022;

Updated for timbreIDLib version 0.9.0;

Similar to zero crossing, another time-domain measure


## `waveSlope`

Bang to analyze the entire array.;

Analyze a window starting at sample 44100 that is 2000

Updated for timbreIDLib version 0.7;

Read from a different array;

Specify your sample's sampling rate. (default: 44100)

Print current settings in the post window;

Normalize the waveform in the analysis window so that

Use the slider above to move through the audio file

Creation argument is the name of the sample array to

See the real-time version for more information on waveform

July 2017;

Note that quiet moments between sound events will produce


## `waveSlope~`

Change analysis window size;

Bang repeatedly...;

Bang to output slope;

Updated for timbreIDLib version 0.7;

Print current settings in the post window;

Inside a subpatch with re-blocking involving overlap

Normalize the waveform in the analysis window so that

This feature can be sent to the timbreID external in

With a real signal, quiet moments between sound events

July 2017;

Waveform slope is the slope of the best-fit line through

Audio buffering is taken care of by the external,


## `zeroCrossing`

Bang to analyze the entire array.;

Read from a different array;

Specify your sample's sampling rate. (default: 44100)

Normalize the zero crossing total according to the current

Creation argument is the name of the sample array to

Analyze a window starting at sample 44100 that is 2000

See the real-time version for more information on zero

Note that with a real signal, low level noise will

Updated for timbreIDLib version 0.9.0;

June 2022;


## `zeroCrossing~`

Change window size.;

Inside a subpatch with re-blocking involving overlap

Normalize the zero crossing total according to the

This feature can be sent to the timbreID external in

Creation argument is window size in samples;

Bang to output zero crossings;

A simple way to measure a signal's noisiness is to count

Audio buffering is taken care of by the external,

June 2022;

Updated for timbreIDLib version 0.9.0;


