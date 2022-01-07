**Brainstorming!**

*Different ways to improve imeter:*

+ account for degenerative sequences
+ account for – and + strands
+ set up a way to weigh the beginning of the intron vs the end of the intron (should work on finding a geometric decay in it)
	+ would be calculated during counts, so like count += decay, total += decay
+ account for sequence repetition due to splice variants
+ decoding, putting things into libraries (proper program in argparse, put functions into some shared library)
	+ trainer program
	+ decoder program
+ scientific studies
+ controls? Experimental data and controls ( R squared value
+ do certain kmers predict long introns? Long introns will contribute more kmers, if one is more common in long kmers, will be disproportionately weighted.
	+ could weight kmers on length of parent intron
	+ could weight kmers based on composition of sequence? might be something good
+ use expression as a response variable,  like a checker.
+ incorporate 4-5 fold cross val, eventually*
+ sort sequences at end, by score, - to +
+ we could score the kmers separately??
	+ if we score without weight based on position in intron?
	+ then after with weight? or developing a secondary metric?
		+ like adding a second log-odds, across the single intron cutoff at an arbitrary(?) point, sortof the same math ? ? ?
	+ is there a virtue in more stringent cutoffs? i.e, is there a virtue in making a deadzone, so to speak, where introns are ignored because they aren't 'distal' or 'proximal' enough?
	+ in general, the approach relies on big data sets, is there something we could account for for the future for smaller ones (this is out of scope for a rotation, more out of curiosity)
	+ split based on expression level?
		+ could expression be a separate function? perhaps accounting for constitutive expression or high expression
		+ what is the optimal way to split? there are many parameters
+ potential to experimentally determine best split options....
+ investigate python itertools combinations, or something to handle permutations, ie (ACTG, 5), then it makes all the possible combinations
