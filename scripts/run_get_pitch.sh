#!/bin/bash

# Put here the program (maybe with path)
GETF0="get_pitch"

for fwav in pitch_db/train/*.wav; do
    ff0=${fwav/.wav/.f0}
    echo "$GETF0 $fwav $ff0 ----"
    $GETF0 $fwav $ff0 > /dev/null || ( echo -e "\nError in $GETF0 $fwav $ff0" && exit 1 )
done

#pitch_evaluate pitch_db/train/*.f0ref

exit 0
