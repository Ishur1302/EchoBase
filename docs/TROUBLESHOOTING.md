# Troubleshooting EchoBase

## Git Push Issues
- **Problem:** Terminal says 'Everything up-to-date' but GitHub is empty.
- **Fix:** Run `git branch` to ensure you are on `main`. If on `master`, run `git push origin master`.

## Audio Latency
- **Problem:** Response takes >2 seconds.
- **Fix:** Check `LATENCY_STRATEGY.md` and ensure VAD aggressiveness is set to 3.
