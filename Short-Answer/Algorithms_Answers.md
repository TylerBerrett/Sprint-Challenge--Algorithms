#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) Linear O(n) because n is getting raised by 3 and waiting tell a is going to become grater but a is groing by n ^ 2 so n ^ 3 - n^ 2 == n


b) Linearithmic O(n log n) because the its a for loop which is O(n) and then there is a nested loop which is growing faster then n is so that one is O(log n) so together they are O(n log n)


c) Linear O(n) because you just get rid of the constants which is the two and you just have a for loop that just iterates back words

## Exercise II

n = stories of the building
f = floor

start with floor n / 2 so half way up the building
drop an egg if it breaks than means every floor above you it would break too so with the remaining floors the ones below you goto the middle of that
else if it doesn't break goto the middle of the floors above you
then when in the middle of either the upper or lower floors repeat this process
then if its the last room remaining then its it the floor highest you can drop it
or if you are safe in one floor and it breaks in that floor then the floor previous is the right one

Big O: log(n)


