# GPS Decoding

Follow along with PSAS GPS class.

Some of my blog posts about GPS:

 - [GPS Visualization](http://natronics.github.io/blag/2014/gps-viz-1)
 - [The GPS PRN](http://natronics.github.io/blag/2014/gps-prn)
 - [GSP Spreading](http://natronics.github.io/blag/2014/gps-spreading)


## Data

We've been using a sample data set recorded by amateur radio enthusiasts.
The dataset I'm writing this decoder against is from the
[GNSS-SDR project](http://www.gnss-sdr.org/)

 - [2013_04_04_GNSS_SIGNAL_at_CTTC_SPAIN.tar.gz](http://sourceforge.net/projects/gnss-sdr/files/data/2013_04_04_GNSS_SIGNAL_at_CTTC_SPAIN.tar.gz/download) (_warning! 1.5 GB file_)


# Run

Make sure you have dependencies:

    $ pip install -r requirements.txt

To run the program, pipe the datafile into `gps.py`:

    $ ./gps.py < PATH/TO/DATA.dat
