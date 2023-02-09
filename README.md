# JPA TUNE UP CODE:

# Usage:

0. Take reference data (all amplifiers tuned away) using Measurement Browser through Labber
```
Counter Value (number of SA traces to consider -> used for calculating average SNR)
```

1. Take data using Measurement Browser through Labber with the following loop order (**Keep SA span the same as the above step**)
```
Counter Value (number of SA traces to consider -> used for calculating average SNR)
Power Bounds
Source Current Bounds
```

2. `$ python tune_up_jpa_power_current_only.py`

or ** Run on Spyder **


---

## Example Usage:

**Labber Measurement Window:**

![labber](labber_measurement_windo.png)


```shell
$ python tune_up_jpa_power_current_only.py

File Location of JPA Data: \path\to\jpa\sweep\data.hdf5

File Location of Reference Data: \path\to\reference\data.hdf5

```


**Result**

![snr](figures/JPA_Tune_Up_10_05_2022_170547.png)
