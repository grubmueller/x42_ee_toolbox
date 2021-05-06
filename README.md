# x42_ee_toolbox
## About
This is my collection of x42 ([HP-42S](https://www.hpmuseum.org/hp42s.htm), [SwissMicros DM42](https://www.swissmicros.com/product/dm42), [Free42](https://thomasokken.com/free42/)) programs. These programs are little helpers for my daily work as an **electrical engineer**, researcher and teacher. I've to admit that the  programs may not always be written in best style. I'm a kid of the 80s: My calculators during school was a TI 30 and later I had a TI Voyage 200 (which I never programmed) - my first programming language was C. I started using RPN calculaters in my 30s just for fun (thanks to a colleague), and it still challenges me. However I really like the programmability of the 42. I think there is no modern tool/software that gives the possibility to write such little everyday helpers in such a simple and clean way.
## Toolchain
All programs are human readable text files with UTF8 encoding, so any editor should work fine to read the code. Files with the ending `.hp42s` are limited to the original HP-42S commands, while files ending with `.free42` may contain some commands only available on Free42. For writing programs and encoding I use - and highly recommend - the [Microsoft Visual Studio Code](https://code.visualstudio.com) editor with the [HP42S-free42](https://marketplace.visualstudio.com/items?itemName=JHeilingbrunner.vscode-hp42s-free42) extension. The extension allows synthax highlighting and generating the necessary `.raw` files. The programs should also work with the online [SwissMicros Programming Tool](https://technical.swissmicros.com/decoders/dm42/), however I did not test it.
## File organisation
Files are organized into three folders:
- `/pgrm`: This folder contains **programs** to be executed with `XEQ`.
- `/fctn`: Files in this folder are **functions** to be used with the 42 `SOLVER` program. Files are marked with a starting underscore `_` and function labels start with a dot `.`.
- `/lib`: This folder contains programs, that are used from within other programs but may not be quite useful standalone.
## Program documentation
The following listings only give a short program description. More detailed documentation may be found in the source files itself.
### pgrm - programs
- `CONV`: Unit conversions
- `dB`: Various dB conversions
- `ESER`: E-series for electrical components
- `LCR`: LCR resonant circuit design
- `LP1`: Transfer function of a first order low-pass filter
- `QUAD`: Roots of quadratic equation
- `RFIT`: Find two standard resistors to get (close to) a desired non-standard resistance value (*Program tests all possibilities without further intelligence. Fitting 1.234 kOhm with E12 series resistors takes about 15 seconds on a battery powered DM42.*)
- `X||Y`: Parallel impedanze of two impedances from stack
- `Z`: Impedance of inductor or capacitor at given frequency
### fctn - functions
- `.DIODE`: Shockley diode model
- `.FPBW`: Full power bandwidth of op-amp
- `.LC`: Resonant frequency of an LC resonant cirucit
- `.PTX`: Resistance/temperature relation of Platinum type RTDs
- `.RC`: Cut-off frequency of a passive RC lowp ass filter
- `.R||R`: Parallel resistance of two resistors
- `.VDIV`: Voltage divider
- `.VREG`: Voltage regulator
### lib - library
All following programs are summarized in one file `LIB.hp42s`.
- `STOD`, `RCLD`: Store/recall display settings
- `STOST`, `RCLST`: Store/recall stack
- `CLTMP`: Clear temporary variables
