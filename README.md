# x42_ee_toolbox

## About

This is my collection of x42 ([HP-42S](https://www.hpmuseum.org/hp42s.htm), [SwissMicros DM42](https://www.swissmicros.com/product/dm42), [Free42](https://thomasokken.com/free42/)) programs. These programs are little helpers for my daily work as an **electrical engineer**, researcher and teacher and I preferably use them on a DM42. I admit that sometimes the programs may not be written optimally: I'm a kid of the 80s, my calculators during school were a TI-30 and a TI-Voyage-200 (which I never programmed) - my first programming language was C. I started using RPN calculaters in my 30s just for fun (thanks to a colleague). However I really like the programmability of the x42. I think there is no modern tool/software that gives the possibility to write such little everyday helpers in such a simple and clean way.

## Program documentation

Information on program usage is written in the according program files.

### functions (use with `SOLVER`)

- `CCOAX`: Coaxial/zylinder capacitor
- `CPLATE`: Plate capacitor
- `FPBW`: Full power bandwidth of an op-amp
- `LC`: Resonant frequency of an LC resonant cirucit
- `RC`: Cut-off frequency of a passive RC low pass filter
- `RPAR`: Parallel resistance of two resistors
- `RTD`: Resistance-temperature relation of Platinum type RTDs (e.g. Pt100)
- `VREG`: Voltage regulator (e.g. LM317)
- `XC`: Reactance of capacitor
- `XL`: Reactance of inductor

### programs (use with `XEQ`)

- `C→Z`, `L→Z`: Impedance of an element, [HP42-EE]
- `CONJ`: Complex conjugate of x stack
- `DY`: Delta-wye conversion, [HP42-EE]
- `I÷`: Current divider, [HP42-EE]
- `NIST`: Physical constants
- `QUAD`: Roots of quadratic equation
- `RFIT`, `RVIEW`, `ESER`: Find a combination of two standard resistors for a desired value
    - <u>*Timing tests with fitting 1234 Ohm with E12 series, solving for 10 results:*</u>
    - *Result without delay on Free42 computer app*
    - *8 s on USB powered DM42*
    - *21 s on battery powered DM42*
- `V÷`: Voltage divider, [HP42-EE]
- `X||Y`: Parallel impedance of x and y stack

### non-engineering

- `TVM`: Time value of money (solver function), [HP42-OM]
- `TVM2`: Time value of money, [HP42-PE]

## Toolchain

All programs are human readable text files with UTF8 encoding, so any editor should work fine to read the code. Files with the ending `.hp42s` are limited to the original HP-42S commands, while files ending with `.free42` may contain some commands only available on Free42. 

To get the program onto the platform you want, you can of course transcode it (if you are fortunate enough to have an HP-42S, this is also the only option). To get the programs onto a SissMicros DM42, I recommend using the desktop version of [Free42](https://thomasokken.com/free42/) to encode the programs. Simply put the application into program mode and copy and paste the program into the application. Then a raw or state file can be exported for further use on a DM42.

## Additional literature

Scans of great HP calculator related literature can be found on [hpcalc.org](https://literature.hpcalc.org).
Direkt link to some HP-42S related files:
- [HP42-QR]: [HP-42S Quick Reference Guide](https://literature.hpcalc.org/community/hp42s-qrg-en.pdf)
- [HP42-OM]: [HP-42S Owner's Manual](https://literature.hpcalc.org/community/hp42s-om-en.pdf)
- [HP42-PE]: [HP-42S Programming Examples and Techniques](https://literature.hpcalc.org/community/hp42s-prog-en.pdf)
- [HP42-EE]: [HP-42S Electrical Engineering](https://literature.hpcalc.org/community/hp42s-elec-en.pdf)