# PyHashBench
A tiny tool that finds SHA256 hashes starting with a certain amount of zeros for random challenges. I wanted to mess around with my new Pi 3 and see how it behaves under full load ;) Also I feel like writing something ;)

##Usage

For a default run just type:

```
python pyhashbench.py
```

The default run will utilize all available CPU cores and test 1.000.000 variations of a random challenge whether their SHA256 hash starts with four zeros.

However, you can easily set custom values:

```
--threads n   (The number of threads to be used. Default: No. of detected CPU cores)
--zeros n     (The number of zeros a matching hash should start with. Default: 4)
--hashes n    (The number of hashes to be calculated. Default: 1.000.000)
```

##What does it do?
1. At first we create a random challenge e.g. "abcde"
2. Then, we prepend a random number e.g. "1234"
3. We calculate the hash SHA256(1234abcde)
4. See if the hex representation of the hash starts with four zeros.

This process is spread over the amount of threads to be used. By default, this is the amount of logical CPU cores.

##ToDo
Instead of showing the calculation time we should introduce a score rating the run results.

##License

See LICENSE file
