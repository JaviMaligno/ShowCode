# Challenge description


Many of Next's product are made using recyled materials. Your task is, given a list of materials in a product and information about the various materials, determine what total percentage of the product has been made of recycled material, rounded to the nearest integer. A material has the format

```
[name] - [x]% recycled
```

or

```
[name]: [A]% [materialA] [B]% [materialB] etc...
```

where name is the case-insensitive alphanumeric name of the product, x is the percentage of that material which has been made of recycled material. For composite materials, their materials and associated percentages are listed such that the percentages add up to 100%. Assume all percentages are integers. Note that these percentages do not correspond to Next's real-life products!
