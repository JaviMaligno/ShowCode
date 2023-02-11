# Challenge description

Particle Physicists use detectors to track particle decay. The set-up you are using measures the total energy every second and each time you measure there is a chance of a decay happening. If a particle decays, it causes an energy spike according to the formula of `A*t*exp(-0.4*t)` where t is the time elapsed since the particle decay and A is an unknown factor, different for each decay.

Given a list of decimal measurements (to 6dp where needed), find the total number of particle decays. Assume that decay will not occur on the final measurement, that the decay factor A is always at least 1, and there is always at least 1 energy reading.