# rust-tracker
This app is/will be designed to pull stats from marketplace items on SkinEarn.com and Steam Marketplace.  Data is stored per item and organized by date, so prices across time can be tracked and also so price differences between the two sites can be tracked as well.

# Background
While taking a Social Media Mining class at UMBC (CS491), we did some exercises with data scraping.  Me being a competant python programmer, decided to take some of the ideas from class and apply them to a personal application.  The idea was to keep myself sharp and to save myself some time, since I was monitoring prices for some items in the two stores mentioned above. 
 
## Roadmap
this is a rough sketch of where I would like to take this program

1. ~~Pull and parse data from SkinEarn.com and Steam Marketplace for rust for specific items~~  **Done**

2. Merge extracted data from both sites into one data object

    A. ex: {"name": 'item', "steamPrice" : $x.xx, "skinearn price": yyyyy, "date": 'yy-mm-dd' }
    
    B. possibly ommit records if no price change

3. Manage loading & adding on to persistent storage file

4. Set up automation. (steam only allows 1 query per minute)

5. Add a way to easily search for new items

## Warranty - License
(MIT liscense)
Copyright 2018 Bwilso1 - github.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
the software is provided "as is", without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose and noninfringement. in no event shall the authors or copyright holders be liable for any claim, damages or other liability, whether in an action of contract, tort or otherwise, arising from, out of or in connection with the software or the use or other dealings in the software.

-----
In short. use this code for whatever you want, but at your own risk. I have made the software as compliant as possible, but if you get blacklisted, banned, or anything else, that is not my problem.  If you do use some of my code, just reference where you found it.
