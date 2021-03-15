# COVAL - COVID-19 Vaccine Appointment Locator

** **Pennsylvania Rite Aid Stores ONLY** **

## About
Most pharmacies (e.g. CVS) will tell you where COVID-19 vaccine appointments are available.

However, Rite Aid's website design means you have to check each store individually to find available appointments. This is quite burdensome.

The goal of COVAL is to take the guesswork out of finding a COVID-19 vaccine appointment at Rite Aid in Pennsylvania.

## Instructions

Confirm you are elligible here: https://www.riteaid.com/covid-vaccine-apt

**DO NOT LIE ABOUT OCCUPATION AND/OR MEDICAL CONDITOINS ON THE RITE AID FORM.**

In the `COVAL.py` file, go to the `SET ZIP CODE RANGE HERE` section, read the instructions, and set your ZIP code range.

Run COVAL using Python 3 from the command line,
e.g. `python3 COVAL.py`

COVAL will give you a set of ZIP codes that have appointment slots available. Slots go quick, so they may be gone by the time you try to secure one. Run COVAL and try again, or wait and try again another time.

Currently, only Pennsylvania Rite Aid stores with confirmed vaccine allocation (as of date in `CHANGE LOG` below) are included in the data COVAL uses.

To update the data used by COVAL, follow the instructions in the `SET STORE DATA HERE` section of the `COVAL.py` file.

## Change Log

* v0.1.314
  * data added 03/14/2021
