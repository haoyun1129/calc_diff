# calc_diff
Calculate the difference of each continuous values (piped data is OK)

adb logcat | gawk -F " " '/mono_ts/ {printf "%f\n", $23};fflush()' | python calc_diff.py --max 0.035 --min 0.0338 -  
