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

* v0.1.315
  * improve results legibility
* v0.1.314
  * data added 03/14/2021

## Example output
```
======================================================================
                                 COVAL
                 COVID-19 Vaccine Appointment Locator
                  Pennsylvania Rite Aid Stores ONLY
======================================================================

Date / time:

   2021-03-15 02:10:11.907991

ZIP code range:

   0 - 99999

Finding slots:
..............1..............................................1......1.
.....................1.........11............1.............1......11..
.............1........11.1............................1.............

Results:

   208 out of 208 stores within ZIP code range analyzed (0 errors)

   15 stores with available slots

   Result #   Store #    ZIP code
   1            10976       15801
   2            07850       15834
   3            02476       15853
   4            07853       15857
   5            03449       16125
   6            10995       16148
   7            01496       16301
   8            10999       16316
   9            11002       16323
   10           04616       16354
   11           01406       16735
   12           02474       16743
   13           11016       16901
   14           01976       16915
   15           11116       19073

======================================================================
```
