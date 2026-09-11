## Lost Voyager

Lost Voyager has an audio file with a SSTV (Slow Scan Television) transmission encoded in Robot36 in it.

There are a few ways to solve the challenge, the coolest I feel like is with the smartphone (Robot36 app on android, iOS has an app names SSTV Slow Scan TV but I couldn't test that so yeah), with these apps you just play the audio and line by line an image appears.


Anothe possible solution is with this GitHub Repo `https://github.com/colaclanth/sstv.git` which can also decode the image `sstv -d lost_voyager_signal.wav -o recovered_flag.png`.

Then in the image is the flag, thats it.