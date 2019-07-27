# The Mueller Report
**20 points**
## Description
> The redacted version of the Mueller report was finally released this week! There's some pretty funny stuff in there, but maybe the report has more beneath the surface.
## Hint
> You won't be able to use Ctrl+F to find this Russian secret, try some command line functions related to strings and searches instead.
---
## Writeup
I couldn't open the pdf file so I used `file` to check if it is indeed a pdf file.

`full-mueller-report.pdf: PDF document, version 1.6`

So it IS a pdf file. I then looked at the hint and used `strings`.

`strings full-mueller-report.pdf | grep 'actf'`

flag: actf{no0o0o0_col1l1l1luuuusiioooon}