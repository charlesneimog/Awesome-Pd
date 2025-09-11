---
search:
    exclude: true
---

# timbreIDLib
`timbreIDLib` is a library of audio analysis externals for Pure Data. The classification external `timbreID` accepts arbitrary lists of audio features and attempts to find the best match between an input feature and previously stored training instances. The library can be used for a variety of real-time and non-real-time applications, including sound classification, sound searching, sound visualization, automatic segmenting, ordering of sounds by timbre, key and tempo estimation, and concatenative synthesis.
<h2>Contributors</h2>

<div id="libcontributors"></div>

<p align="center">
<i>People who contribute to this project.</i>
</p>


<script>
async function updateList() {
    const repoOwner = 'wbrent';
    const repoName = 'timbreIDLib';
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
- :material-tune: [__attackTime__](../objects/descriptors/attackTime.md) The `attackTime` object analyzes a specified segment of a sound sample array to determine its attack time.
- :material-tune: [__attackTime~__](../objects/descriptors/attackTime~.md) The `attackTime~` object calculates the attack time of an audio event in milliseconds.
- :material-tune: [__autoCorrPitch__](../objects/descriptors/autoCorrPitch.md) The autoCorrPitch object performs offline pitch tracking on a specified audio sample array using an autocorrelation algorithm.
- :material-tune: [__autoCorrPitch~__](../objects/descriptors/autoCorrPitch~.md) The autoCorrPitch~ object calculates the fundamental pitch of an incoming audio signal using autocorrelation, converting the result to Hertz and MIDI units.
- :material-tune: [__bark__](../objects/descriptors/bark.md) The bark object is a non-real-time audio onset detector that identifies musical attacks by analyzing spectral changes.
- :material-tune: [__barkSpec__](../objects/descriptors/barkSpec.md) The `barkSpec` object calculates the Bark spectrum of an audio sample or a specified segment within a sample array.
- :material-tune: [__barkSpecBrightness__](../objects/descriptors/barkSpecBrightness.md) The `barkSpecBrightness` object calculates the brightness of an audio sample by analyzing its Bark spectrum.
- :material-tune: [__barkSpecBrightness~__](../objects/descriptors/barkSpecBrightness~.md) The barkSpecBrightness~ object calculates the brightness of an audio signal's Bark spectrum.
- :material-tune: [__barkSpecCentroid__](../objects/descriptors/barkSpecCentroid.md) The barkSpecCentroid object computes the Bark spectrum centroid, a psychoacoustically weighted measure of an audio signal's spectral balance.
- :material-tune: [__barkSpecCentroid~__](../objects/descriptors/barkSpecCentroid~.md) The `barkSpecCentroid~` object calculates the Bark spectrum centroid, representing the "center of mass" of an audio signal's energy distribution on the Bark frequency scale.
- :material-tune: [__barkSpecFlatness__](../objects/descriptors/barkSpecFlatness.md) The `barkSpecFlatness` object calculates the spectral flatness of an audio signal within Bark-scaled frequency bands.
- :material-tune: [__barkSpecFlatness~__](../objects/descriptors/barkSpecFlatness~.md) The `barkSpecFlatness~` object calculates the spectral flatness of an incoming audio signal within the Bark frequency scale, outputting a value between 0.0 and 1.0 that indicates how noise-like the spectrum is.
- :material-tune: [__barkSpecFlux__](../objects/descriptors/barkSpecFlux.md) The barkSpecFlux object calculates the spectral flux between two audio windows (forward and back) based on their Bark band energy differences.
- :material-tune: [__barkSpecFlux~__](../objects/descriptors/barkSpecFlux~.md) The `barkSpecFlux~` object calculates the spectral flux of an audio signal based on Bark-band energy differences.
- :material-tune: [__barkSpecIrregularity__](../objects/descriptors/barkSpecIrregularity.md) The barkSpecIrregularity object computes the Bark spectrum irregularity of an audio signal, a descriptor indicating the noisiness or irregularity of its spectral envelope.
- :material-tune: [__barkSpecIrregularity~__](../objects/descriptors/barkSpecIrregularity~.md) The `barkSpecIrregularity~` object calculates the spectral irregularity of an audio signal's Bark spectrum.
- :material-tune: [__barkSpecKurtosis__](../objects/descriptors/barkSpecKurtosis.md) The barkSpecKurtosis object calculates the kurtosis of the Bark spectrum, serving as an audio descriptor within the timbreIDLib.
- :material-tune: [__barkSpecKurtosis~__](../objects/descriptors/barkSpecKurtosis~.md) The barkSpecKurtosis~ object calculates the kurtosis (peakedness) of an audio signal's Bark spectrum.
- :material-tune: [__barkSpecRolloff__](../objects/descriptors/barkSpecRolloff.md) The barkSpecRolloff object calculates the spectral rolloff of an audio signal based on its Bark scale spectrum.
- :material-tune: [__barkSpecRolloff~__](../objects/descriptors/barkSpecRolloff~.md) The `barkSpecRolloff~` object calculates the Bark spectrum rolloff, which is the Bark frequency below which a specified concentration of spectral energy is located.
- :material-tune: [__barkSpecSkewness__](../objects/descriptors/barkSpecSkewness.md) The `barkSpecSkewness` object calculates the skewness of the Bark spectrum of an audio sample.
- :material-tune: [__barkSpecSkewness~__](../objects/descriptors/barkSpecSkewness~.md) The `barkSpecSkewness~` object calculates the skewness of an audio signal's Bark spectrum, quantifying the symmetry of its energy distribution across frequency bands.
- :material-tune: [__barkSpecSlope__](../objects/descriptors/barkSpecSlope.md) The barkSpecSlope object calculates the slope of the Bark spectrum for a given audio segment.
- :material-tune: [__barkSpecSlope~__](../objects/descriptors/barkSpecSlope~.md) The `barkSpecSlope~` object calculates the slope of the best-fit line through the data points of a Bark spectrum.
- :material-tune: [__barkSpecSpread__](../objects/descriptors/barkSpecSpread.md) The barkSpecSpread object calculates the Bark spectrum spread, a measure of the spectral width of an audio signal based on the Bark scale.
- :material-tune: [__barkSpecSpread~__](../objects/descriptors/barkSpecSpread~.md) The barkSpecSpread~ object calculates the spread of an audio signal's Bark spectrum, indicating the concentration of energy around its centroid.
- :material-tune: [__barkSpec~__](../objects/descriptors/barkSpec~.md) The `barkSpec~` object analyzes incoming audio to compute its Bark-frequency spectrum, which warps the normal spectrum to the Bark scale, emphasizing low-frequency detail.
- :material-tune: [__bark~__](../objects/descriptors/bark~.md) The `bark~` object is a real-time onset detector for Pure Data, which analyzes spectral growth using the perceptually-based Bark frequency scale.
- :material-tune: [__bfcc__](../objects/descriptors/bfcc.md) The bfcc object computes Bark-frequency Cepstral Coefficients, which are a common audio descriptor used to characterize timbre.
- :material-tune: [__bfcc~__](../objects/descriptors/bfcc~.md) The `bfcc~` object computes Bark-frequency cepstral coefficients (BFCCs) from an audio input, emphasizing lower spectral content and using a Discrete Cosine Transform.
- :material-tune: [__binWrangler__](../objects/descriptors/binWrangler.md) The `binWrangler` Pure Data object accumulates a specified number of feature vector frames, such as BFCCs, and then outputs the time-varying information organized by bin number as a concatenated list.
- :material-tune: [__cepstrum__](../objects/descriptors/cepstrum.md) The `cepstrum` object computes the cepstrum of an audio signal from a specified sample array.
- :material-tune: [__cepstrumPitch__](../objects/descriptors/cepstrumPitch.md) The cepstrumPitch object performs offline pitch tracking on an audio sample array using cepstral analysis.
- :material-tune: [__cepstrumPitch~__](../objects/descriptors/cepstrumPitch~.md) The `cepstrumPitch~` object performs real-time pitch tracking of an audio signal using cepstrum analysis.
- :material-tune: [__cepstrum~__](../objects/descriptors/cepstrum~.md) The cepstrum~ object computes the real cepstrum of an audio signal, derived from the Inverse Fourier Transform of the log magnitude spectrum.
- :material-tune: [__chroma__](../objects/descriptors/chroma.md) The `chroma` object performs non-real-time pitch chroma analysis on audio data stored in a Pure Data array.
- :material-tune: [__chroma~__](../objects/descriptors/chroma~.md) The `chroma~` object analyzes incoming audio to determine the spectral energy present in each of the 12 musical pitch classes, regardless of octave.
- :material-tune: [__dct__](../objects/descriptors/dct.md) The `dct` object computes the Discrete Cosine Transform (DCT) of a specified portion or the entirety of a Pure Data array.
- :material-tune: [__dct~__](../objects/descriptors/dct~.md) The `dct~` object computes the Discrete Cosine Transform (DCT) of an incoming audio window, outputting a list of real numbers representing its spectral characteristics.
- :material-tune: [__energy__](../objects/descriptors/energy.md) The `energy` object from the `timbreIDLib` library calculates the energy of a specified audio sample array or a segment within it.
- :material-tune: [__energyEntropy__](../objects/descriptors/energyEntropy.md) The `energyEntropy` object calculates the energy entropy of an audio sample array.
- :material-tune: [__energyEntropy~__](../objects/descriptors/energyEntropy~.md) The `energyEntropy~` object measures abrupt changes in the energy of an audio signal.
- :material-tune: [__energy~__](../objects/descriptors/energy~.md) The `energy~` object from `timbreIDLib` continuously calculates the energy of an audio signal, offering output in power, RMS, or decibels with adjustable window sizing and normalization.
- :material-tune: [__featureAccum__](../objects/descriptors/featureAccum.md) The `featureAccum` object accumulates incoming lists of feature frames, processing them into a single output based on a specified mode.
- :material-tune: [__featureDelta__](../objects/descriptors/featureDelta.md) The `featureDelta` object calculates the difference between corresponding attributes of two incoming feature lists, such as audio descriptors.
- :material-tune: [__featureNorm__](../objects/descriptors/featureNorm.md) The `featureNorm` object normalizes incoming feature lists, scaling their values to a specified range (either 0 to 1 by default, or -1 to 1).
- :material-tune: [__harmonicRatio__](../objects/descriptors/harmonicRatio.md) The 'harmonicRatio' object calculates the harmonic ratio of a specified audio sample array or a window within it.
- :material-tune: [__harmonicRatio~__](../objects/descriptors/harmonicRatio~.md) The `harmonicRatio~` object calculates the harmonic ratio of an audio signal, providing an indicator of its periodicity.
- :material-tune: [__magSpec__](../objects/descriptors/magSpec.md) The `magSpec` object from the `timbreIDLib` library performs non-real-time spectral analysis on a given audio sample array.
- :material-tune: [__magSpec~__](../objects/descriptors/magSpec~.md) The magSpec~ object calculates the magnitude spectrum of an incoming audio signal over a specified window.
- :material-tune: [__maxSample__](../objects/descriptors/maxSample.md) The `maxSample` object analyzes a specified portion of a Pure Data array (typically containing audio samples) to find the maximum sample value and its corresponding index within that segment.
- :material-tune: [__maxSampleDelta__](../objects/descriptors/maxSampleDelta.md) The `maxSampleDelta` object analyzes a specified segment of a sample array to identify the largest absolute difference between consecutive samples.
- :material-tune: [__maxSampleDelta~__](../objects/descriptors/maxSampleDelta~.md) The `maxSampleDelta~` object analyzes an audio stream to find the largest absolute difference between adjacent samples within a specified window.
- :material-tune: [__maxSample~__](../objects/descriptors/maxSample~.md) The `maxSample~` object reports the maximum sample value and its corresponding index within a specified audio window.
- :material-tune: [__melSpec__](../objects/descriptors/melSpec.md) The 'melSpec' object computes a Mel-scaled spectrogram from an audio sample, providing a time-frequency representation of sound.
- :material-tune: [__melSpec~__](../objects/descriptors/melSpec~.md) The `melSpec~` object computes the Mel-frequency spectrum of an incoming audio signal, transforming the linear frequency scale to the perceptually-motivated mel scale.
- :material-tune: [__mfcc__](../objects/descriptors/mfcc.md) The `mfcc` object calculates Mel-Frequency Cepstral Coefficients (MFCCs) from an audio sample array, providing a compact representation of the spectral envelope.
- :material-tune: [__mfcc~__](../objects/descriptors/mfcc~.md) The `mfcc~` object computes Mel-Frequency Cepstral Coefficients from an audio signal, emphasizing lower spectral content and using a Discrete Cosine Transform.
- :material-tune: [__minSample__](../objects/descriptors/minSample.md) The `minSample` object analyzes a specified window within a Pure Data array, typically containing audio samples.
- :material-tune: [__minSampleDelta__](../objects/descriptors/minSampleDelta.md) The minSampleDelta object analyzes a specified window within a sample array to find the smallest absolute difference between consecutive samples.
- :material-tune: [__minSampleDelta~__](../objects/descriptors/minSampleDelta~.md) The `minSampleDelta~` object calculates the minimum absolute difference between adjacent samples within a specified audio window.
- :material-tune: [__minSample~__](../objects/descriptors/minSample~.md) The `minSample~` object reports the value and index of the smallest sample within a configurable N-sample window of incoming audio.
- :material-tune: [__nearestPoint__](../objects/descriptors/nearestPoint.md) The nearestPoint object identifies the closest point(s) within a stored dataset to a given input point in a multi-dimensional space.
- :material-tune: [__peakSample__](../objects/descriptors/peakSample.md) The `peakSample` object analyzes a specified audio array or a segment of it to find the maximum sample value and its corresponding index.
- :material-tune: [__peakSample~__](../objects/descriptors/peakSample~.md) The `peakSample~` object identifies the sample with the largest magnitude within a defined window of an incoming audio signal, outputting both its value and index.
- :material-tune: [__phaseSpec__](../objects/descriptors/phaseSpec.md) The `phaseSpec` object from `timbreIDLib` calculates the phase spectrum of a specified window within an audio sample array.
- :material-tune: [__phaseSpec~__](../objects/descriptors/phaseSpec~.md) The `phaseSpec~` object calculates and outputs the phase spectrum of an audio signal.
- :material-tune: [__sampleBuffer~__](../objects/descriptors/sampleBuffer~.md) The `sampleBuffer~` object buffers incoming audio, providing a windowed segment of the audio stream for real-time analysis.
- :material-tune: [__specBrightness__](../objects/descriptors/specBrightness.md) The specBrightness object from the timbreIDLib analyzes the spectral brightness of an audio sample.
- :material-tune: [__specBrightness~__](../objects/descriptors/specBrightness~.md) The `specBrightness~` object calculates the spectral brightness of an audio signal, defined as the ratio of high-frequency spectral magnitudes to total spectral magnitudes.
- :material-tune: [__specCentroid__](../objects/descriptors/specCentroid.md) The `specCentroid` object calculates the spectral centroid of an audio array, providing a measure of the 'brightness' or 'timbral richness' of a sound.
- :material-tune: [__specCentroid~__](../objects/descriptors/specCentroid~.md) The `specCentroid~` object calculates the spectral centroid, a low-level timbre feature representing the "center of mass" of an audio signal's magnitude spectrum.
- :material-tune: [__specFlatness__](../objects/descriptors/specFlatness.md) The `specFlatness` object calculates the spectral flatness of an audio array, providing a measure of its noisiness.
- :material-tune: [__specFlatness~__](../objects/descriptors/specFlatness~.md) The `specFlatness~` object calculates the spectral flatness of an incoming audio signal, providing a measure of how noise-like a sound is.
- :material-tune: [__specFlux__](../objects/descriptors/specFlux.md) The `specFlux` object calculates spectral flux, a measure of how quickly the spectrum of a sound is changing.
- :material-tune: [__specFlux~__](../objects/descriptors/specFlux~.md) The `specFlux~` object calculates the spectral flux of an audio signal, quantifying how quickly its spectrum changes over time.
- :material-tune: [__specHarmonicity__](../objects/descriptors/specHarmonicity.md) The `specHarmonicity` object calculates the spectral harmonicity and inharmonicity of an audio sample.
- :material-tune: [__specHarmonicity~__](../objects/descriptors/specHarmonicity~.md) The `specHarmonicity~` object quantifies the harmonic alignment of spectral peaks in an audio signal, outputting both harmonicity and inharmonicity values between 0 and 1.
- :material-tune: [__specIrregularity__](../objects/descriptors/specIrregularity.md) The `specIrregularity` object calculates the spectral irregularity of an audio signal, providing a numerical descriptor of its timbral characteristics.
- :material-tune: [__specIrregularity~__](../objects/descriptors/specIrregularity~.md) The `specIrregularity~` object calculates the spectral irregularity of an audio signal, indicating how jagged or smooth its frequency spectrum is.
- :material-tune: [__specKurtosis__](../objects/descriptors/specKurtosis.md) The `specKurtosis` object calculates the spectral kurtosis of an audio array, serving as a non-real-time spectral descriptor.
- :material-tune: [__specKurtosis~__](../objects/descriptors/specKurtosis~.md) The `specKurtosis~` object calculates the spectral kurtosis of an audio signal, quantifying the peakedness of its spectrum.
- :material-tune: [__specRolloff__](../objects/descriptors/specRolloff.md) The `specRolloff` object calculates the spectral rolloff of an audio signal, identifying the frequency below which a specified percentage of the total spectral energy lies.
- :material-tune: [__specRolloff~__](../objects/descriptors/specRolloff~.md) The specRolloff~ object calculates the spectral rolloff frequency of an audio signal, representing the frequency below which a specified percentage of the total spectral energy is concentrated.
- :material-tune: [__specSkewness__](../objects/descriptors/specSkewness.md) The `specSkewness` object from the `timbreIDLib` calculates the spectral skewness of an audio sample array.
- :material-tune: [__specSkewness~__](../objects/descriptors/specSkewness~.md) The `specSkewness~` object calculates the spectral skewness of an audio signal, providing a measure of the asymmetry of its spectral envelope.
- :material-tune: [__specSlope__](../objects/descriptors/specSlope.md) The `specSlope` object calculates the spectral slope of an audio sample, quantifying the average decrease in amplitude across increasing frequencies.
- :material-tune: [__specSlope~__](../objects/descriptors/specSlope~.md) The `specSlope~` object calculates the spectral slope of an incoming audio signal, representing the slope of the best-fit line through its magnitude spectrum.
- :material-tune: [__specSpread__](../objects/descriptors/specSpread.md) The `specSpread` object calculates the spectral spread, a measure of the dispersion of the spectrum around its centroid, for an audio signal stored in a Pure Data array.
- :material-tune: [__specSpread~__](../objects/descriptors/specSpread~.md) The `specSpread~` object calculates the spectral spread of an audio signal, quantifying the concentration of its energy around the spectral centroid in Hz.
- :material-tune: [__tID-conversion__](../objects/descriptors/tID-conversion.md) This Pure Data object provides essential conversion utilities for audio frequency analysis.
- :material-tune: [__tID_fft__](../objects/descriptors/tID_fft.md) The tID_fft object performs an offline Fast Fourier Transform (FFT) on a specified segment of an audio sample array in Pure Data.
- :material-tune: [__tID_fft~__](../objects/descriptors/tID_fft~.md) The `tID_fft~` object computes the complex Fast Fourier Transform (FFT) of an audio signal, triggered by a bang.
- :material-tune: [__tID_mean__](../objects/descriptors/tID_mean.md) The `tID_mean` object calculates the arithmetic mean of a list of numbers.
- :material-tune: [__tID_std__](../objects/descriptors/tID_std.md) The tID_std object calculates the standard deviation of a list of numbers, requiring at least two elements.
- :material-tune: [__tabletool__](../objects/descriptors/tabletool.md) The `tabletool` object provides a comprehensive set of functionalities for manipulating, analyzing, and querying data stored in Pure Data tables.
- :material-tune: [__timbreID__](../objects/descriptors/timbreID.md) The timbreID object stores, clusters, and classifies audio feature vectors, enabling tasks like sound identification and timbre ordering.
- :material-tune: [__waveNoise__](../objects/descriptors/waveNoise.md) The `waveNoise` object analyzes a specified sample array to quantify its "noisiness" or the rate of change in its waveform direction.
- :material-tune: [__waveNoise~__](../objects/descriptors/waveNoise~.md) The `waveNoise~` object measures the noisiness of an audio signal by counting the number of times the signal changes direction within a specified window.
- :material-tune: [__waveSlope__](../objects/descriptors/waveSlope.md) The waveSlope object analyzes the slope of a waveform stored in a Pure Data array.
- :material-tune: [__waveSlope~__](../objects/descriptors/waveSlope~.md) The `waveSlope~` object calculates the slope of the best-fit line through the absolute value of audio samples within a configurable analysis window.
- :material-tune: [__zeroCrossing__](../objects/descriptors/zeroCrossing.md) The `zeroCrossing` object calculates the zero-crossing rate of a specified audio array or a segment of it.
- :material-tune: [__zeroCrossing~__](../objects/descriptors/zeroCrossing~.md) The `zeroCrossing~` object measures the noisiness or frequency-related characteristics of an audio signal by counting how many times it crosses the zero amplitude point within a specified window.
</div>