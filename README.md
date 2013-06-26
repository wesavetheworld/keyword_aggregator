# Google Adwords Aggregator

You've started a business. You know the market space: who your competitors are, who your partners will be, who you might get confused for... but now you want keywords to focus your messaging around. This tool takes all the SEO efforts your enemies have put into their businesses, and aggregates it into keywords for you.

## Installation and Usage

First, get the code:

    git clone git@github.com:garbados/keyword_aggregator.git
    cd keyword_aggregator

Then, configure. In the `Makefile`, change the variables to suit your needs:

* `RESULTS`: Where you want to output results. Defaults to `results.csv`
* `DOWNLOADS`: Where you'll download keywords from Google. Defaults to `~/Downloads`
* `CSV_DIR`: Where you want your downloaded keywords to live. Defaults to `data`

Now, we'll need those keywords. Go to [Google's Keyword Planner](https://adwords.google.com/ko/KeywordPlanner/Home), click "Search for keyword and ad group ideas", then, one by one...

* Enter the name of a competitor / partner
* Download the resulting keywords as an Adwords Editor CSV.

Once you've downloaded your lists of keywords, head back to the terminal and run `make`. It'll spit out a CSV into the file you specified in `RESULTS` of the top 1000 keywords aggregated amongst all the groups you downloaded.