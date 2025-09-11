# File I/O

<div class="grid cards" markdown>

- :material-tune: [__presets__](presets.md) The `presets` object in Pure Data allows users to save and recall multiple configurations of patch parameters, including GUI elements, numbers, symbols, and arrays.
- :material-tune: [__midi__](midi.md) The `midi` object in Pure Data is a versatile tool for playing, recording, and manipulating raw MIDI data streams.
- :material-tune: [__model__](model.md) The `model` object in Pure Data renders 3D models saved in the Alias/Wavefront OBJ format.
- :material-tune: [__brane.m~__](brane.m~.md) The `brane.m~` object is a comprehensive granulator sampler with stretch/compress capabilities and a harmonizer pitch shifter.
- :material-tune: [__scala__](scala.md) The `scala` object imports musical scales from `.scl` files, a format used by the Scala software for microtonal tunings.
- :material-tune: [__sfload__](sfload.md) The `sfload` object loads sound files into Pure Data arrays, supporting various audio formats like MP3, WAV, and FLAC.
- :material-tune: [__sfont.m~__](sfont.m~.md) The `sfont.m~` object is a convenient wrapper around `sfont~` designed for soundfont-based synthesis.
- :material-tune: [__pix_writer__](pix_writer.md) The `pix_writer` object saves the current GEM texture (image) to a file on disk.
- :material-tune: [__gran.player~__](gran.player~.md) `gran.player~` is a granular audio player that allows for independent time stretching and pitch shifting of loaded sound files.
- :material-tune: [__capture~__](capture~.md) The `capture~` object is designed for signal debugging and investigation, capturing audio samples into an internal buffer.
- :material-tune: [__sf-play_record__](sf-play_record.md) The `sf-play_record` object provides a hard disk recording and playback system for Pure Data, enabling multi-track audio recordings.
- :material-tune: [__rec__](rec.md) The `rec` object records incoming messages across multiple tracks and plays them back.
- :material-tune: [__sfont~__](sfont~.md) `sfont~` is a sampler synthesizer that plays SoundFont (.sf2/.sf3) files, based on FluidLite.
- :material-tune: [__pix_buffer_filmopen__](pix_buffer_filmopen.md) The `pix_buffer_filmopen` object reads a movie file into a named `pix_buffer` for subsequent image processing within GEM.
- :material-tune: [__glsl_geometry__](glsl_geometry.md) The `glsl_geometry` object loads and compiles a GLSL geometry shader from a specified file.
- :material-tune: [__msgfile__](msgfile.md) The `msgfile` object reads and writes messages to text files, extending the functionality of `textfile`.
- :material-tune: [__pix_multiimage__](pix_multiimage.md) The `pix_multiimage` object loads multiple image files (TIFF, JPEG, PNG) into memory, which can then be used as textures or for bitblitting within GEM.
- :material-tune: [__pix_movie__](pix_movie.md) The `pix_movie` object loads and plays digital video files, making their frames available as textures for real-time graphics rendering within GEM.
- :material-tune: [__score__](score.md) The `score` object is a Pure Data score sequencer that uses a custom text-based syntax to define musical events.
- :material-tune: [__presets.m__](presets.m.md) The `presets.m` object in Pure Data enables saving and recalling parameter presets for "MERDA modules" within a patch.
- :material-tune: [__modelfiler__](modelfiler.md) The `modelfiler` object loads 3D model data from Alias/Wavefront OBJ files into Pure Data tables.
- :material-tune: [__pix_record__](pix_record.md) The `pix_record` object in Pure Data is used to record sequences of video frames (pixes) to an output file, pipe, or video device.
- :material-tune: [__freadln__](freadln.md) The `freadln` object reads text files line by line, outputting each line as a list.
- :material-tune: [__buffer~__](buffer~.md) The `buffer~` object stores audio data in memory as a multichannel array, supporting up to 64 channels.
- :material-tune: [__play.file~__](play.file~.md) `play.file~` is a Pure Data object that reads and plays audio files from your computer, supporting various formats like AAC, FLAC, MP3, and WAV.
- :material-tune: [__sample~__](sample~.md) The `sample~` object creates and manages an audio buffer, enabling users to load, record, save, and manipulate audio samples.
- :material-tune: [__text3d__](text3d.md) The `text3d` object in Pure Data renders a single line of text within a 3D graphical environment, leveraging GEM's transformations.
- :material-tune: [__funbuff__](funbuff.md) The `funbuff` object stores and manages ordered pairs of x/y integer values.
- :material-tune: [__multimodel__](multimodel.md) The `multimodel` object loads and renders multiple 3D Alias/Wavefront (`.obj`) models.
- :material-tune: [__seq__](seq.md) The `seq` object in Pure Data is a MIDI sequencer that can play, record, load, and save MIDI streams to and from MIDI or text files.
- :material-tune: [__pix_image__](pix_image.md) The `pix_image` object loads image files (like TIFFs and JPEGs) into Pure Data, primarily for use as textures or for bitblitting operations within the GEM environment.
- :material-tune: [__pic__](pic.md) The `pic` object in Pure Data displays image files (`.gif`, `.ppm`, `.pgm`) within a patch.
- :material-tune: [__pix_fiducialtrack__](pix_fiducialtrack.md) The `pix_fiducialtrack` object detects and tracks fiducial markers in black and white grayscale images, utilizing a system similar to reacTable.
- :material-tune: [__coll__](coll.md) The `coll` object in Pure Data is a versatile data collection and manipulation tool.
- :material-tune: [__pix_imageInPlace__](pix_imageInPlace.md) The `pix_imageInPlace` object efficiently loads multiple image files (TIFF, JPEG, PNG) into texture RAM, enabling very fast switching between them.
- :material-tune: [__mtr__](mtr.md) The `mtr` object in Pure Data functions as a multi-track message recorder and playback system.
- :material-tune: [__dir__](dir.md) The `dir` object allows you to access and manage files within directories.
- :material-tune: [__pix_film__](pix_film.md) The `pix_film` object loads and plays digital video files, providing frames as textures for use within Pure Data's GEM environment.
- :material-tune: [__capture__](capture.md) The `capture` object stores incoming messages (floats and symbols) in the order they are received, acting as a sequential data buffer.
- :material-tune: [__glsl_vertex__](glsl_vertex.md) The `glsl_vertex` object loads and compiles a GLSL vertex shader into a module.
- :material-tune: [__openfile__](openfile.md) The `openfile` object in Pure Data is a utility that allows users to open local folders, files, or web links.
- :material-tune: [__batch.rec~__](batch.rec~.md) `batch.rec~` is a convenient Pure Data abstraction for batch recording audio signals to a sound file.
- :material-tune: [__sfz~__](sfz~.md) The `sfz~` object is a Pure Data synthesizer that plays SFZ instruments, which are text-based definitions for sample-based and hybrid synthesis.
- :material-tune: [__rec.file~__](rec.file~.md) The `rec.file~` object records incoming audio signals to a sound file, serving as a convenient wrapper around `writesf~`.
- :material-tune: [__sfinfo__](sfinfo.md) The `sfinfo` object queries information from sound files, such as the number of channels or instrument metadata for AIFF files.
- :material-tune: [__pvoc.player~__](pvoc.player~.md) The `pvoc.player~` object is an audio file player that offers independent time stretching and pitch shifting capabilities through a phase vocoder.
- :material-tune: [__player~__](player~.md) `player~` is a versatile Pure Data object for playing back audio files.
- :material-tune: [__pix_buffer__](pix_buffer.md) `pix_buffer` is a named storage object for images, functioning similarly to a table but without direct visual access to its contents.
- :material-tune: [__fwriteln__](fwriteln.md) The `fwriteln` object writes text files line by line, serving as a simplified version of `textfile`.
- :material-tune: [__score2__](score2.md) The `score2` object is a sequencer that plays back musical scores using a rhythmic notation syntax similar to `pattern`.
- :material-tune: [__pix_write__](pix_write.md) The `pix_write` object captures a snapshot of the current GEM frame buffer and saves it to a file.

</div>