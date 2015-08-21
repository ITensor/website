<span class='article_title'>Philosophy of ITensor</span>

<span class='article_sig'>E. Miles Stoudenmire & Thomas E. Baker&mdash;August 19, 2015</span>

ITensor is a code used for sorting and keeping track of tensors in calculations.  Our core philosophy is that you should dream up a calculation, that the interface should be easily translatable into your theory (by making our code match diagrams you might draw), and we should take care of ensuring that calculation is done quickly and correctly. 

## Interface

For now, we've chosen C++ as the front end for our library.  C++ is quick and efficient for many purposes.  The ITensor library that is built on top of it provides an easy user interface to directly translate tensor network methods into code.  An extensive knowledge of pointers is not needed for most applications.

We also use common sense conventions such as starting vectors with an index of one instead of zero.

## Readable and Useful Documentation

We provide on this website a comprehensive list of concepts you need to run calculations but that might not be clear in the literature.  "Everyone knows that" is a phrase that now applies to the helper sections on this website.  If there's something you need to know and we don't have a tutorial, send us an email!

## Modular Design

One main goal of ITensor is to get all users to feel comfortable with modifying the code and pushing the changes to the library.  This way the community can help us make a living code that responds to your needs.
<!--
## Coding as Research
--->

We've also made ITensor modular, so if a new development comes around (or a suggestion from you!) then we'll implement it without fundamentally rewriting major parts of the library.

Feel free to check out how to contribute code improvements to ITensor through our GitHub repository.

