Title: Apartment Hunting with Python & jq
Date: 2015-09-04 00:00
Modified: 2015-09-04 00:00
Category: Tech
Tags: svbtle-migrated,python,jq,web-scraping
Slug: apartmenthunting-with-python-jq
Author: Jamie Luck
Summary: Scraping Craigslist for apartment listings so I don't have to do it manually

The worst thing about finding a new apartment is the anticipation that happens during the long periods of inevitable waiting. I got pretty anxious, and decided to try to automate my stress out the window!

I'm looking for apartments on Craigslist, to both save money and hopefully meet people that won't cut me up and put me in little buckets. I decided I'd write a Craigslist scraper in python using the wonderful [beautifulsoup](http://www.crummy.com/software/BeautifulSoup/) HTML parsing library.

This is essentially a data munging exercise. All the data I want (prices, location, washer and dryer combinations) are inside of this website, and whatever I write should just grab it in an organized fashion and put it into something usable. I decided that my output format would be JSON so I can query the information in a more structured way than a CSV. (Plus, a lot of the post titles contained commas, and I'm lazy!)

# The Data

The starting point for our data is an index page. It looks something like this:

[![2015-09-03-234636_641x375_scrot.png](https://svbtleusercontent.com/nbrqnqghdquwkw_small.png)](https://svbtleusercontent.com/nbrqnqghdquwkw.png)

Under the hood, Craigslist will probably output all of their posting data in some kind of a loop, so the source should be pretty predictable:

[![2015-09-03-234835_660x514_scrot.png](https://svbtleusercontent.com/28oyflgb3xiyjg_small.png)](https://svbtleusercontent.com/28oyflgb3xiyjg.png)

Bingo! Look at all those `<p class="row">`! Thankfully, with beautifulsoup, these are really easy to isolate out. I'm going to pretend for the next code block that we have some magical function called `get_craigslist_html()` that pulls down the whole HTML for that page. We'll fill in the bones on this later.

With beautifulsoup, you can navigate the page's source like a tree. You can use methods like `find_all()` to pick out individual subtrees of that, which instead of being rooted at `<html>` are rooted at some arbitrary tag (like `<p class="row">`!)

```python
source = get_craigslist_html()
rootsoup = BeautifulSoup(source)
for post in rootsoup.find_all('p', 'row'):
  # do the stuff
```

Great, now we can operate on our posts! What's inside of each of those big `<p>` tags?

[![2015-09-03-235451_638x358_scrot.png](https://svbtleusercontent.com/hxkzwj7nsmgtqa_small.png)](https://svbtleusercontent.com/hxkzwj7nsmgtqa.png)

Ok... so now what? There's definitely some information we want in here, but where can we find it?

Well, here's a few things, after looking at that source:

| Information | Location |
| ----- | ------ |
| Title of posting | the text inside the highlighted `<a>` in the image above |
| URL of the post | the href of the highlighted `<a>` |
| Time it was posted | the `<time>` tag inside of the `<span class="pl">` |
| Rent | `<span class="price">` inside of the `<span class="l2">` |
| Location | `<span class="pnr">`'s `<small>` tag |

Well, let's expand our example and try to get some of that pulled out! I'm going to put it into a python dict, because they're fast and are easily transferable to JSON!

```python
source = get_craigslist_html()
rootsoup = BeautifulSoup(source)
for post in rootsoup.find_all('p', 'row'):
  listing = {}
  pl_container = post.find('span', 'pl')
  listing['title'] = pl_container.find('a').text
  listing['url'] = pl_container.find('a').get('href')
  listing['time'] = pl_container.find('time').get('datetime')
  if post.find('span','price') is not None:
    listing['price'] = post.find('span','price').text.strip()
  if post.find('span','pnr').small is not None:
    loc_raw = post.find('span','pnr').small
    # get rid of the surrounding () & whitespace
    listing['location'] = loc_raw.text.strip()[1:-1]
```

How neat is that?
[![foo.jpg](https://svbtleusercontent.com/6zjkuzmkhjfwwg_small.jpg)](https://svbtleusercontent.com/6zjkuzmkhjfwwg.jpg)

Great, if we have one of these dictionaries per listing we can assemble them all together and query them as a group!

```python
def get_craigslist_index(url):
  source = get_craigslist_html(url)
  rootsoup = BeautifulSoup(source)
  posts_from_page = []
  for post in rootsoup.find_all('p','row'):
      try:
        listing = {}
        listing['repost'] = 'data-repost-of' in post.attrs
        pl_container = post.find('span', 'pl')
        listing['title'] = pl_container.find('a').text
        listing['url'] = pl_container.find('a').get('href')
        listing['time'] = pl_container.find('time').get('datetime')
        if post.find('span','price') is not None:
          listing['price'] = post.find('span','price').text.strip()
        if post.find('span','pnr').small is not None:
          loc_raw = post.find('span','pnr')
          listing['location'] = loc_raw.small.text.strip()[1:-1]
        posts_from_page.append(listing)
  return posts_from_page
```

That's the general logic of the [script](https://github.com/delucks/scripts/blob/master/cdump.py) I wrote, which does this for multiple pages until it hits a desired amount of results. 

Now that we have the right tool for this job, let's download some posts!

# Running It

[![2015-09-03-233453_956x188_scrot.png](https://svbtleusercontent.com/eemazwtikq8cg_small.png)](https://svbtleusercontent.com/eemazwtikq8cg.png)

After running this command, all results are stored in `sfbay-apa.json`. We're now going to use the excellent command-line JSON processor [`jq`](https://stedolan.github.io/jq/) to, well, process our JSON.

[![2015-09-03-233547_745x57_scrot.png](https://svbtleusercontent.com/qrljytwa2jorw_small.png)](https://svbtleusercontent.com/qrljytwa2jorw.png)

Let's say I'm looking for Craigslist-listed apartments in Sunnyvale (which I am). This is the filter string I put together to do that:

```
.[] | (.location=="sunnyvale") then .url else empty end
```

The part before the pipe (`|`) will output every element of the list at the top-level of the JSON (for those of you reading along, [line 61 of cdump.py](https://github.com/delucks/scripts/blob/master/cdump.py#L61)). This then pipes each of those into a conditional statement that checks if the ["location" field of the dictionary](https://github.com/delucks/scripts/blob/master/cdump.py#L34) matches the string "sunnyvale". If so, it'll output the ["url" field](https://github.com/delucks/scripts/blob/master/cdump.py#L28), or nothing (`empty`) if not. 

So, this ought to output a list of URLs we'd be interested in (apartments listed on Craigslist for rent in Sunnyvale). 

[![2015-09-03-233553_895x968_scrot.png](https://svbtleusercontent.com/2uk1eojgm2n8g_small.png)](https://svbtleusercontent.com/2uk1eojgm2n8g.png) 

It did! Now if we set up a quick, poorly written bash loop, we can open them all at once.

[![2015-09-03-233658_934x109_scrot.png](https://svbtleusercontent.com/ea1anpsxyr6pw_small.png)](https://svbtleusercontent.com/ea1anpsxyr6pw.png)

And, my web browser is surprisingly not dead.

[![2015-09-03-233730_535x89_scrot.png](https://svbtleusercontent.com/ytp4uqwrysxeg_small.png)](https://svbtleusercontent.com/ytp4uqwrysxeg.png)

# Results

I spent 2+ hours doing something I could have done in 30 minutes. I'm now wallowing in the irony. 
