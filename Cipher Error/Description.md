# Description

The cyber security team has detected an error in a cipher algorithm that generates secure keys. Without the keys, the bank will be unable to complete transactions safely and service will be negatively impacted.

In order to keep the bank running smoothly, the cyber security team need to reconstruct the correct keys. The reconstruction process is complex, so the team breaks it down into smaller steps which can be tackled more easily.

As part of this reconstruction process, the team have asked Clarisa to write a method that receives a key as a character string, and splits it into a comma delimited string based on a change of character.

The cyber security team gives Clarisa the following guidance:

- Repeated characters should not be split by commas.
- For better visibility, add a space before the comma delimiter
- Strings may contain special characters
- Blanks are also characters and should be treated as such

For example, `"BGGG3//zz\++tt"` should be split and show `"B ,GGG ,3 ,// ,zz ,\ ,++ ,tt "`.
Clarisa must make sure she is accurate so that the reconstruction process doesn’t fail. She also needs to be quick so that the impacts on the bank’s services are minimised.

The cyber security team, and the bank, are counting on Clarisa.