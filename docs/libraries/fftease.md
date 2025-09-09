---
search:
    exclude: true
---

# fftease

<h2>Contributors</h2>

<div id="libcontributors"></div>

<p align="center">
<i>People who contribute to this project.</i>
</p>


<script>
async function updateList() {
    const repoOwner = 'ericlyon';
    const repoName = 'pd-fftease';
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
- :material-tune: [__burrow~__](../objects/burrow~.md) The `burrow~` object performs cross-filtering on an audio input, using a second audio input as a filter source.
- :material-tune: [__cavoc27~__](../objects/cavoc27~.md) The `cavoc27~` object generates audio spectra using a 27-rule cellular automaton.
- :material-tune: [__cavoc~__](../objects/cavoc~.md) The `cavoc~` object generates audio spectra using an 8-rule cellular automaton.
- :material-tune: [__centerring~__](../objects/centerring~.md) `centerring~` performs frequency-independent amplitude modulation, allowing for unique timbral effects.
- :material-tune: [__cross~__](../objects/cross~.md) The `cross~` object performs block convolution for cross-synthesis.
- :material-tune: [__dentist~__](../objects/dentist~.md) The `dentist~` object functions as a "spiky" filter, selectively allowing certain partials to pass while attenuating others.
- :material-tune: [__disarrain~__](../objects/disarrain~.md) The `disarrain~` object functions as a spectrum scrambler, reordering a specified number of frequency bins within an audio signal.
- :material-tune: [__disarray~__](../objects/disarray~.md) `disarray~` is a spectrum scrambler that reorders a specified number of frequency bins within an input signal's spectrum.
- :material-tune: [__drown~__](../objects/drown~.md) The `drown~` object performs spectral noise floor manipulation on audio signals using FFT.
- :material-tune: [__enrich~__](../objects/enrich~.md) The `enrich~` object performs additive synthesis by generating an oscillator bank.
- :material-tune: [__ether~__](../objects/ether~.md) `ether~` performs spectral compositing by selecting portions of two input signals based on a composite index.
- :material-tune: [__leaker~__](../objects/leaker~.md) The `leaker~` object performs a spectral crossfade between two input audio signals.
- :material-tune: [__mindwarp~__](../objects/mindwarp~.md) The `mindwarp~` object performs spectral envelope warping, primarily utilizing frequency shaping.
- :material-tune: [__morphine~__](../objects/morphine~.md) `morphine~` performs spectral morphing, enabling a smooth transition between two audio signals in the frequency domain.
- :material-tune: [__multyq~__](../objects/multyq~.md) `multyq~` is a four-band spectral equalizer designed for audio processing.
- :material-tune: [__pileup~__](../objects/pileup~.md) The `pileup~` object performs spectral persistence by maintaining amplitude and phase information in frequency bins.
- :material-tune: [__pvcompand~__](../objects/pvcompand~.md) `pvcompand~` is a spectral compander that either expands or compresses the dynamic range of audio signals in the frequency domain.
- :material-tune: [__pvgrain~__](../objects/pvgrain~.md) `pvgrain~` is a spectral granulator that tracks an input sound and synthesizes grains based on its spectral characteristics.
- :material-tune: [__pvharm~__](../objects/pvharm~.md) `pvharm~` is an audio harmonizer that transposes an input signal into two pitches.
- :material-tune: [__pvoc~__](../objects/pvoc~.md) The `pvoc~` object performs phase vocoding, a technique for time-stretching or pitch-shifting audio by analyzing its frequency content.
- :material-tune: [__pvtuner~__](../objects/pvtuner~.md) `pvtuner~` is a frequency-quantized oscillator bank resynthesis object that allows users to impose arbitrary tunings.
- :material-tune: [__pvwarpb~__](../objects/pvwarpb~.md) `pvwarpb~` is a spectral warper that applies an internal frequency warping function to audio signals.
- :material-tune: [__pvwarp~__](../objects/pvwarp~.md) `pvwarp~` is a Pure Data object designed for spectral warping of audio signals.
- :material-tune: [__reanimator~__](../objects/reanimator~.md) The `reanimator~` object performs audio texture mapping by analyzing a "texture" sound using spectral analysis (FFT) and then re-synthesizing audio based on a "driver" sound.
- :material-tune: [__resent~__](../objects/resent~.md) `resent~` is a spectral sample buffer that captures an input audio signal for manipulation.
- :material-tune: [__residency_buffer~__](../objects/residency_buffer~.md) `residency_buffer~` is an audio object that manages a spectral sample buffer, similar to `residency~`.
- :material-tune: [__residency~__](../objects/residency~.md) The `residency~` object samples audio input into an internal buffer, primarily for spectral processing.
- :material-tune: [__schmear~__](../objects/schmear~.md) `schmear~` performs spectral smearing by convolving the amplitude spectrum of an input signal with a user-supplied kernel.
- :material-tune: [__scrape~__](../objects/scrape~.md) `scrape~` is an audio object designed for shaped noise reduction.
- :material-tune: [__shapee~__](../objects/shapee~.md) The `shapee~` object is designed to shape the frequency evolution of an audio signal.
- :material-tune: [__swinger~__](../objects/swinger~.md) `swinger~` is a cross-synthesis object that replaces the phase of one input signal (the amplitude source) with the phase of another input signal (the phase source).
- :material-tune: [__taint~__](../objects/taint~.md) The `taint~` object performs spectral multiplication, combining the frequency spectra of two input audio signals.
- :material-tune: [__thresher~__](../objects/thresher~.md) The `thresher~` object sustains the amplitude and frequency of audio signals, particularly in lower-energy parts, by applying damped bin-level feedback.
- :material-tune: [__vacancy~__](../objects/vacancy~.md) The `vacancy~` object performs spectral compositing, allowing for the manipulation and combination of audio in the frequency domain.
- :material-tune: [__xsyn~__](../objects/xsyn~.md) The `xsyn~` object performs cross synthesis by filtering its first audio input with the spectral characteristics of its second audio input.
</div>